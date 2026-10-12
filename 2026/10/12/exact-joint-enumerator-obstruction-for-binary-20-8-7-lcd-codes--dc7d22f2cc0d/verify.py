#!/usr/bin/env python3
"""Exact rational Farkas verifier for the binary (20,8,7) LCD joint enumerator.
Requires Python 3 standard library and the sibling CERTIFICATE.json file.
"""
import json
from array import array
from fractions import Fraction
from math import comb
from pathlib import Path

N=20
K=8
D=7
H=((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))

def tuples_of_degree(n):
    return [(n-b-c-e,b,c,e) for b in range(n+1)
            for c in range(n-b+1) for e in range(n-b-c+1)]

def hadamard_coefficients():
    prev_tuples=[(0,0,0,0)]
    prev_rows=[array('q',[1])]
    for n in range(1,N+1):
        dest=tuples_of_degree(n)
        dest_ix={x:i for i,x in enumerate(dest)}
        old_ix={x:i for i,x in enumerate(prev_tuples)}
        shift=[]
        for t in range(4):
            shifts=array('i')
            for x in prev_tuples:
                xx=list(x)
                xx[t]+=1
                shifts.append(dest_ix[tuple(xx)])
            shift.append(shifts)
        rows=[]
        for alpha in dest:
            r=next(r for r in range(4) if alpha[r])
            pred=list(alpha)
            pred[r]-=1
            parent=prev_rows[old_ix[tuple(pred)]]
            out=array('q',[0])*len(dest)
            for t in range(4):
                sign=H[r][t]
                sh=shift[t]
                if sign==1:
                    for i,c in enumerate(parent):
                        out[sh[i]]+=c
                else:
                    for i,c in enumerate(parent):
                        out[sh[i]]-=c
            rows.append(out)
        prev_tuples,prev_rows=dest,rows
    return prev_tuples,prev_rows

def krawtchouk(j,w):
    return sum((-1)**t*comb(w,t)*comb(N-w,j-t)
               for t in range(max(0,j-(N-w)),min(j,w)+1))

def base_coefficient(row,quad):
    a,b,c,e=quad
    idx=lambda w: (N-w,0,w,0)
    bidx=lambda w: (N-w,w,0,0)
    if row<63:
        w,typ=divmod(row,3)
        if typ==0:
            return int(c+e==w)-2**(N-K)*int(quad==idx(w))
        if typ==1:
            return int(b+e==w)-2**K*int(quad==bidx(w))
        return int(b+c==w)
    if row==63:
        return int(quad==(N,0,0,0))
    j=row-64
    answer=2**K*int(quad==bidx(j))
    if b==e==0:
        answer-=krawtchouk(j,c)
    return answer

def base_rhs(row):
    if row<63 and row%3==2:return comb(N,row//3)
    if row==63:return 1
    return 0

def main():
    data=json.loads((Path(__file__).resolve().parent/'CERTIFICATE.json').read_text(encoding='utf-8'))
    assert data['schema_version']==1 and (data['n'],data['k'],data['d'])==(N,K,D)
    denominator=data['denominator']
    assert denominator==10**12 and data['positive_slack_denominator']==10000
    base=data['base_multipliers']
    joint=data['hadamard_multipliers']
    assert len({i for i,_ in base})==len(base)
    assert len({i for i,_,_ in joint})==len(joint)
    assert all(0<=i<85 and isinstance(n,int) for i,n in base)
    assert all(0<=i<1771 and n!=0 and positive>0 for i,n,positive in joint)
    Q,transform=hadamard_coefficients()
    assert len(Q)==comb(N+3,3)==1771
    index={quad:i for i,quad in enumerate(Q)}
    assert all(sum(quad)==N for quad in Q)
    # Check Hadamard transform on the highest monomial and an involution checksum.
    first=index[(N,0,0,0)]
    assert transform[first][first]==1
    assert sum(transform[first])==4**N
    assert sum(1 for idx,quad in enumerate(Q) if quad[3]%2==0 and (quad[2]+quad[3]>=D or quad[2]+quad[3]==0) and not (quad[1]==quad[2]==0 and quad[3]>0))==686
    admissible=[]
    for i,(a,b,c,e) in enumerate(Q):
        if (e%2 or 1<=c+e<D or (b==0 and c==0 and e>0)):
            continue
        admissible.append(i)
    assert len(admissible)==686
    # The additional uniform positive term is the sum of the 21
    # ambient-shell equalities divided by 2**N. It has coefficient 1 on
    # every joint enumerator variable and RHS 1.
    eps=Fraction(1,data['positive_slack_denominator'])
    RHS=sum(Fraction(int(n)*base_rhs(i),denominator) for i,n in base)+eps
    assert RHS==Fraction(-999899898449,10**12)
    assert RHS<0
    min_lhs=None
    for j in admissible:
        quad=Q[j]
        total=eps
        total+=Fraction(sum(n*base_coefficient(i,quad) for i,n in base),denominator)
        for row,n,positive in joint:
            coefficient=int(transform[j][row])-(2**N if j==row else 0)
            if coefficient:
                total+=Fraction(n*coefficient,denominator*positive)
        if min_lhs is None or total<min_lhs:
            min_lhs=total
        assert total>=0,('negative coefficient',quad,total)
    assert min_lhs>0
    # Every feasible nonnegative joint M satisfies the 85 base equalities,
    # selected 427 of the 680 Hadamard equations and the ambient-shell
    # equalities; the weighted sum would be nonnegative but equals RHS<0.
    print('DIMENSION',N,K,'MIN_DISTANCE_BOUND',D-1)
    print('JOINT_VARIABLES',len(Q),'FREE_NONNEGATIVE_VARIABLES',len(admissible))
    print('BASE_CERT_ROWS',len(base),'HADAMARD_CERT_ROWS',len(joint))
    print('FARKAS_RHS',str(RHS))
    print('MIN_FARKAS_COEFFICIENT',str(min_lhs))
    print('VERIFY_OK')

if __name__=='__main__':
    main()

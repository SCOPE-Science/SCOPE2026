#!/usr/bin/env python3
"""Finite-field checks for derivation-induced bracket-rank strata."""
import itertools
import random
from collections import Counter

triples=[(0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2)]
index={v:i for i,v in enumerate(triples)}

def prod(a,b):
    u,v=triples[a],triples[b]
    if len(set(u+v))<len(u)+len(v) or len(u)+len(v)>3: return (0,None)
    if (len(u),len(v)) not in [(1,1),(1,2),(2,1)]:return (0,None)
    seq=u+v
    swaps=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    sign=(-1)**swaps
    if len(u)==1 and len(v)==2:sign=-sign
    return (sign,index[tuple(sorted(seq))])

def mul(x,y,p):
    z=[0]*7
    for i,a in enumerate(x):
        if not a:continue
        for j,b in enumerate(y):
            if b:
                s,k=prod(i,j)
                if s:z[k]=(z[k]+a*b*s)%p
    return z

def add(*rows,p):return [sum(v)%p for v in zip(*rows)]

def e(i):return [int(i==j) for j in range(7)]

def derivation(cols,p):
    # cols are arbitrary D(e_0),D(e_1),D(e_2).
    D=list(cols)+[None]*4
    for j,k in [(0,1),(0,2),(1,2)]:
        D[index[(j,k)]]=add(mul(D[j],e(k),p),mul(e(j),D[k],p),p=p)
    D[6]=add(mul(D[3],e(2),p),mul(e(3),D[2],p),p=p)
    return D

def bracket(a,b,D,p):return add(mul(D[a],e(b),p),mul(D[b],e(a),p),p=p)

def rank(vectors,p):
    if not vectors:return 0
    rows=[list(v) for v in vectors]; r=0
    for j in range(len(rows[0])):
        pivot=next((i for i in range(r,len(rows)) if rows[i][j]%p),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        inv=pow(rows[r][j]%p,-1,p)
        rows[r]=[(c*inv)%p for c in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][j]%p:
                m=rows[i][j]
                rows[i]=[(a-m*b)%p for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return r

def A_rank_type(A,p):
    scalar=next((t for t in range(p) if all(A[j][i]==(t if i==j else 0) for i in range(3) for j in range(3))),None)
    if scalar is not None:return 0
    if any(rank([[A[j][i]-(t if i==j else 0) for j in range(3)] for i in range(3)],p)==1 for t in range(p)):
        return 2
    return 3

def check(A,p,extra=None):
    if extra is None:extra=[[0]*4 for _ in range(3)]
    cols=[[A[j][i]%p for j in range(3)]+[v%p for v in extra[i]] for i in range(3)]
    D=derivation(cols,p)
    # independently check derivation on all 49 basis pairs
    for i in range(7):
        for j in range(7):
            s,k=prod(i,j)
            lhs=[s*t%p for t in D[k]] if s else [0]*7
            rhs=add(mul(D[i],e(j),p),mul(e(i),D[j],p),p=p)
            assert lhs==rhs,("not derivation",i,j,A,extra,lhs,rhs)
    b=[bracket(i,j,D,p) for i in range(7) for j in range(i,7)]
    actual=rank(b,p)
    ty=A_rank_type(A,p)
    nonzero=any(a for col in A for a in col)
    predicted=(ty+1) if nonzero else None
    if nonzero:assert actual==predicted,('bad rank',p,A,extra,actual,predicted)
    # anomaly coefficient exhaustive for basis triples
    witness=any(mul(mul(e(i),e(j),p),D[k],p)[6] for i in range(3) for j in range(3) for k in range(3))
    assert witness==nonzero,('anomaly',p,A,extra,witness,nonzero)
    return actual

def main():
    assert all(prod(i,j)[0]==-prod(j,i)[0] for i in range(7) for j in range(7))
    # 3^9 exact census for induced linear maps, independent of closed formula.
    p=3
    actual=Counter()
    for xs in itertools.product(range(p),repeat=9):
        A=[list(xs[i*3:(i+1)*3]) for i in range(3)]
        typ=A_rank_type(A,p)
        actual[typ]+=1
    expected={0:p,2:p*(p**3-1)**2//(p-1),3:p**9-p-p*(p**3-1)**2//(p-1)}
    assert dict(actual)==expected,(actual,expected)
    print('F3_EXHAUSTIVE_LINEAR_TYPE',dict(actual))
    rng=random.Random(80401)
    counts=Counter()
    for p in [5,7,11]:
        for k in range(750):
            if k<250:A=[[rng.randrange(p) for _ in range(3)] for __ in range(3)]
            elif k<500:
                t=rng.randrange(p);u=[rng.randrange(p) for _ in range(3)];v=[rng.randrange(p) for _ in range(3)]
                A=[[((t if i==j else 0)+u[j]*v[i])%p for j in range(3)] for i in range(3)]
            else:
                t=rng.randrange(p);A=[[t if i==j else 0 for j in range(3)] for i in range(3)]
            extra=[[rng.randrange(p) for _ in range(4)] for __ in range(3)]
            r=check(A,p,extra)
            counts[(p,r)]+=1
        # explicit representatives of rank 1, 3, 4.
        for A,r in [([[1,0,0],[0,1,0],[0,0,1]],1),([[2,0,0],[0,1,0],[0,0,1]],3),([[1,0,0],[0,2,0],[0,0,3]],4)]:
            assert check(A,p)==r,(p,r,A)
    print('RANDOM_VERIFIED',sum(counts.values()),sorted(counts.items()))
    print('VERIFY_OK')

if __name__=='__main__':main()

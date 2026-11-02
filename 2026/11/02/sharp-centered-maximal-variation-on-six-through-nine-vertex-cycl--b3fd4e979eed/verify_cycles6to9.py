#!/usr/bin/env python3
"""Standard-library exact proof checker for the C6--C9 centered-maximal variation bounds.
Usage: python3 verify_cycles6to9.py cycles6to9_dual_certificates.json
No floating point operations or optimization package is used in verification.
"""
import itertools,json,math,sys
from fractions import Fraction as F

def balls(n):
    R=n//2+1
    return [[frozenset((i+j)%n for j in range(-r,r+1)) for r in range(R)] for i in range(n)]

def branch_matrix(n,ball_sets,sigma,radii,scale):
    R=n//2+1
    c=[sigma[(i-1)%n]-sigma[i] for i in range(n)]
    plus=[i for i in range(n) if c[i]>0]
    minus=[i for i in range(n) if c[i]<0]
    assert len(radii)==len(plus)
    dim=2*n-1+len(minus)
    A=[]; b=[]
    for i in range(n):
        row=[0]*dim
        if (i+1)%n:row[(i+1)%n-1]+=scale
        if i:row[i-1]-=scale
        row[n-1+i]=-scale
        A.append(row); b.append(0)
        row=[-x for x in row]; row[n-1+i]=-scale
        A.append(row); b.append(0)
    row=[0]*dim
    for i in range(n):row[n-1+i]=scale
    A.append(row);b.append(scale)
    for j,i in enumerate(minus):
        for r in range(R):
            row=[0]*dim
            S=ball_sets[i][r]
            v=scale//len(S)
            for k in S:
                if k>0:row[k-1]=v
            row[2*n-1+j]=-scale
            A.append(row);b.append(0)
    obj=[0]*dim
    for i,r in zip(plus,radii):
        S=ball_sets[i][r]
        v=scale//len(S)*c[i]
        for k in S:
            if k>0:obj[k-1]+=v
    for j,i in enumerate(minus):obj[2*n-1+j]+=scale*c[i]
    return A,b,obj

def variation(seq):
    return sum(abs(seq[(i+1)%len(seq)]-seq[i]) for i in range(len(seq)))

def verify(path):
    with open(path,encoding='utf-8') as f: doc=json.load(f)
    assert doc['schema_version']==1 and doc['vertices']==[6,7,8,9]
    assert doc['target']=='(n-1)/n'
    total_branches=0;total_inequalities=0
    for n in doc['vertices']:
        B=balls(n)
        scale=math.lcm(*(len(s) for row in B for s in row))
        entries=doc['by_n'][str(n)]
        expected_count=0;last_bound=F(0)
        entries_iter=iter(entries)
        for bits_tuple in itertools.product('01',repeat=n):
            bits=''.join(bits_tuple)
            sigma=[1 if bit=='1' else -1 for bit in bits]
            plus=[i for i in range(n) if sigma[(i-1)%n]-sigma[i]>0]
            for radii in itertools.product(range(n//2+1),repeat=len(plus)):
                entry=next(entries_iter)
                bit_recorded,selected,nonzero=entry
                assert bit_recorded==bits and selected==list(radii)
                A,b,obj=branch_matrix(n,B,sigma,radii,scale)
                denom=1; last_index=-1
                for idx,num,den in nonzero:
                    assert type(idx)==int and last_index<idx<len(b)
                    assert type(num)==int and type(den)==int and num>0 and den>0
                    last_index=idx
                    denom=math.lcm(denom,den)
                pairs=[(idx,(denom//den)*num) for idx,num,den in nonzero]
                # Integer-scaled exact rational LP dual feasibility.
                for k,z in enumerate(obj):
                    assert sum(y*A[idx][k] for idx,y in pairs)>=denom*z, (n,bits,radii,k)
                dual_num=sum(y*b[idx] for idx,y in pairs)
                assert n*dual_num <= (n-1)*scale*denom,(n,bits,radii)
                last_bound=max(last_bound,F(dual_num,scale*denom))
                total_inequalities+=len(obj)
                expected_count+=1
        assert next(entries_iter,None) is None
        point=[F(int(i==0)) for i in range(n)]
        out=[max(sum(point[k] for k in S)/len(S) for S in row) for row in B]
        assert variation(point)==2 and variation(out)==2*F(n-1,n)
        assert last_bound==F(n-1,n)
        total_branches+=expected_count
        print('PASS C%d: %d exact LP branches; sharp total-variation factor %s' %(n,expected_count,F(n-1,n)),flush=True)
    print('PASS ALL:',total_branches,'dual certificates,',total_inequalities,'exact integer inequalities, four independent point-mass witnesses')

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('usage: verify_cycles6to9.py certificates.json')
    verify(sys.argv[1])

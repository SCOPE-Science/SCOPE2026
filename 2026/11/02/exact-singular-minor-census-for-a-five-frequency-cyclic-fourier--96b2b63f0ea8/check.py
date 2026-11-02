#!/usr/bin/env python3
"""Exact algebraic and counting checks for a five-row cyclic Fourier minor family."""
from itertools import combinations
from math import comb
def monic_divide(num, den):
    arr=num[:]
    while len(arr)>=len(den):
        t=arr[-1]
        if t:
            start=len(arr)-len(den)
            for j,v in enumerate(den):arr[start+j]-=t*v
        assert arr[-1]==0
        arr.pop()
    assert not any(arr),('nonexact division',num,den,arr)
    return_q=[]  # quotient is reconstructed separately below

def cyclotomic(N):
    phis={}
    for m in range(1,N+1):
        if N%m:continue
        poly=[-1]+[0]*(m-1)+[1]
        for d in sorted(phis):
            if m%d==0:
                den=phis[d]
                q=[0]*(len(poly)-len(den)+1)
                arr=poly[:]
                while len(arr)>=len(den):
                    t=arr[-1]
                    idx=len(arr)-len(den)
                    q[idx]=t
                    for j,v in enumerate(den):arr[idx+j]-=t*v
                    assert arr[-1]==0
                    arr.pop()
                assert not any(arr)
                poly=q
        phis[m]=poly
    return phis[N]

def coords(N):
    cp=cyclotomic(N)
    deg=len(cp)-1
    out=[]
    residue=[1]+[0]*(deg-1)
    for j in range(N):
        out.append(residue[:])
        shifted=[0]+residue
        t=shifted.pop()
        residue=[shifted[i]-t*cp[i] for i in range(deg)]
    return out

def vanish(vs, inds):
    return all(sum(vs[j][i] for j in inds)==0 for i in range(len(vs[0])))

def is_pentagon(N, inds):
    if N%5: return False
    a=inds[0]% (N//5)
    return all(j%(N//5)==a for j in inds)

def is_pair_triple(N, inds):
    if N%6: return False
    s=set(inds)
    for a in inds:
        b=(a+N//2)%N
        if b in s and b!=a:
            rem=s-{a,b}
            if len(rem)==3:
                r=min(rem)
                if {r,(r+N//3)%N,(r+2*N//3)%N}==rem:return True
    return False

for N in [6,7,8,9,10,11,12,15,18,20,24,30]:
    vs=coords(N)
    z=[]
    for inds in combinations(range(N),5):
        actual=vanish(vs,inds)
        classified=is_pentagon(N,inds) or is_pair_triple(N,inds)
        if actual!=classified:raise AssertionError(('five classification',N,inds,actual,classified))
        if actual:z.append(inds)
    expected=(N//5 if N%5==0 else 0)+(N*(N-6)//6 if N%6==0 else 0)
    assert len(z)==expected,(N,len(z),expected)
    print('FINITE_N',N,'all_column_subsets',comb(N,5),'singular',len(z))

# Mann's reduction: any minimal sum of <=5 roots has ratios of order dividing 30.
# Exhaust every distinct subset of 30th roots up to size five;
# only minimal vanishing sets need classify.  In a minimal k-set,
# each nonempty proper subset must have nonzero cyclotomic sum.
vs=coords(30)
zero=[]
for k in range(2,6):
    minimal=[]
    for inds in combinations(range(30),k):
        if not vanish(vs,inds):continue
        proper=False
        for j in range(2,k):
            if any(vanish(vs,v) for v in combinations(inds,j)):
                proper=True;break
        if not proper:minimal.append(inds)
    zero.append(len(minimal))
    for inds in minimal:
        if k==2:assert (inds[1]-inds[0])%30==15
        elif k==3:assert set(inds)=={inds[0],(inds[0]+10)%30,(inds[0]+20)%30}
        elif k==5:assert is_pentagon(30,inds)
        else:raise AssertionError(('unexpected minimal',k,inds))
    print('MINIMAL_30',k,'count',len(minimal))
assert zero==[15,10,0,6],zero
print('VERIFY_OK exact_cyclotomic_all_five_subsets_and_exhaustive_Mann_reduction')

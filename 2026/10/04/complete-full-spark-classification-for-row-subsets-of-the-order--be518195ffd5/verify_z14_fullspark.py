#!/usr/bin/env python3
import itertools, math
from collections import Counter

N=14
UNITS=tuple(a for a in range(N) if math.gcd(a,N)==1)
PHI14=[1,-1,1,-1,1,-1,1]  # 1-x+x^2-x^3+x^4-x^5+x^6, low-to-high
PRIMES=((29,4),(43,2))       # roots have exact order 14
BAD_LOW={
    (0,1,3,4):(0,1,2,8),
    (0,1,2,3,6):(0,1,4,6,8),
    (0,1,2,3,6,11):(0,1,2,4,6,7),
    (0,1,2,3,5,6,11):(0,1,2,3,4,8,10),
}
EXPECTED_UNIFORM_BY_SIZE={1:14,2:42,3:210,4:210,5:420,6:140,7:70,8:140,9:420,10:210,11:210,12:42,13:14}
EXPECTED_BAD_BY_SIZE={1:0,2:0,3:0,4:42,5:84,6:14,7:28,8:14,9:84,10:42,11:0,12:0,13:0}

def uniform(S):
    m=len(S)
    for d in (2,7):
        counts=[sum(x%d==r for x in S) for r in range(d)]
        lo=m//d; hi=(m+d-1)//d
        if any(c not in (lo,hi) for c in counts): return False
    return True

def affine(S,a,b):
    return tuple(sorted((a*x+b)%N for x in S))

def orbit(S):
    return {affine(S,a,b) for a in UNITS for b in range(N)}

def complement(S):
    ss=set(S)
    return tuple(x for x in range(N) if x not in ss)

def canonical(S):
    return min(orbit(S))

def det_mod(A,p):
    A=[list(map(lambda x:x%p,row)) for row in A]
    n=len(A); det=1
    for i in range(n):
        piv=next((r for r in range(i,n) if A[r][i]),None)
        if piv is None:return 0
        if piv!=i:
            A[i],A[piv]=A[piv],A[i]; det=(-det)%p
        pv=A[i][i]; det=det*pv%p; inv=pow(pv,p-2,p)
        for r in range(i+1,n):
            f=A[r][i]*inv%p
            if f:
                for c in range(i,n): A[r][c]=(A[r][c]-f*A[i][c])%p
    return det%p

def det_eval_mod(S,cols,p,root):
    A=[[pow(root,(r*c)%N,p) for c in cols] for r in S]
    return det_mod(A,p)

def sign_perm(perm):
    inv=0
    for i in range(len(perm)):
        for j in range(i+1,len(perm)):
            inv += perm[i]>perm[j]
    return -1 if inv%2 else 1

def det_poly(S,cols):
    # determinant as integer polynomial in x after replacing zeta_14 by x
    m=len(S); coeff={}
    for perm in itertools.permutations(range(m)):
        e=sum((S[i]*cols[perm[i]])%N for i in range(m))
        coeff[e]=coeff.get(e,0)+sign_perm(perm)
    d=max(coeff, default=0)
    a=[0]*(d+1)
    for e,v in coeff.items():a[e]=v
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def rem_phi14(a):
    a=a[:]
    # PHI14 monic degree 6
    while len(a)>6:
        k=len(a)-1
        lead=a[-1]
        if lead:
            shift=k-6
            for j,c in enumerate(PHI14): a[shift+j]-=lead*c
        while len(a)>1 and a[-1]==0:a.pop()
    return a

def exact_zero_minor(S,cols):
    r=rem_phi14(det_poly(S,cols))
    return all(v==0 for v in r)

def main():
    # Roots really have exact order 14.
    for p,r in PRIMES:
        assert pow(r,14,p)==1 and pow(r,7,p)!=1 and pow(r,2,p)!=1 and r%p!=1

    uniform_sets=[]
    for m in range(1,N):
        for S in itertools.combinations(range(N),m):
            if uniform(S):uniform_sets.append(S)
    by=Counter(map(len,uniform_sets))
    assert dict(sorted(by.items()))==EXPECTED_UNIFORM_BY_SIZE
    assert len(uniform_sets)==2142

    # Affine orbits; reduce to size <=7 using complementary-minor duality.
    seen=set(); reps=[]
    for S in uniform_sets:
        if S in seen:continue
        O=orbit(S); seen|=O; reps.append((S,len(O)))
    assert len(reps)==38
    low=[(S,osz) for S,osz in reps if len(S)<=7]
    assert len(low)==20

    # Exact bad witnesses.
    for S,cols in BAD_LOW.items():
        assert uniform(S)
        assert exact_zero_minor(S,cols), (S,cols,rem_phi14(det_poly(S,cols)))

    # For every low affine-orbit representative not in BAD_LOW, every maximal minor
    # is nonzero in characteristic zero: each minor is nonzero under at least one
    # of the two reductions zeta_14 -> 4 mod 29 or zeta_14 -> 2 mod 43.
    detected_bad=[]
    minor_checks=0
    for S,osz in low:
        joint_zero=[]
        m=len(S)
        for cols in itertools.combinations(range(N),m):
            minor_checks+=1
            vals=[det_eval_mod(S,cols,p,r) for p,r in PRIMES]
            if all(v==0 for v in vals):joint_zero.append(cols)
        if joint_zero:
            detected_bad.append(S)
            assert S in BAD_LOW
            assert any(exact_zero_minor(S,c) for c in joint_zero)
        else:
            assert S not in BAD_LOW
    assert set(detected_bad)==set(BAD_LOW)

    # Build all seven exceptional affine orbits: four low-cardinality ones and
    # complements of the first three. The 7-set orbit is self-complementary.
    bad_sets=set()
    for S in BAD_LOW:
        bad_sets |= orbit(S)
        if len(S)<7: bad_sets |= orbit(complement(S))
        else: assert canonical(complement(S))==canonical(S)
    assert len(bad_sets)==308
    bad_by=Counter(map(len,bad_sets))
    for m in range(1,14): assert bad_by[m]==EXPECTED_BAD_BY_SIZE[m]
    assert bad_sets <= set(uniform_sets)

    # Every uniformly distributed set is classified by an affine orbit (if <=7)
    # or by the affine orbit of its complement (>7).
    low_bad_can={canonical(S) for S in BAD_LOW}
    for S in uniform_sets:
        T=S if len(S)<=7 else complement(S)
        is_bad=(canonical(T) in low_bad_can)
        assert is_bad == (S in bad_sets)

    full_by={m:EXPECTED_UNIFORM_BY_SIZE[m]-EXPECTED_BAD_BY_SIZE[m] for m in range(1,14)}
    assert sum(full_by.values())==1834
    print('VERIFY_OK')
    print('uniform_total=2142')
    print('affine_orbits=38 low_orbits=20')
    print('modular_minor_checks=',minor_checks)
    print('bad_uniform_total=308')
    print('full_spark_total=1834')
    print('bad_by_size=',dict(sorted(bad_by.items())))
    print('full_by_size=',full_by)
    for S,w in BAD_LOW.items(): print('bad_rep',S,'witness_cols',w,'orbit',len(orbit(S)))

if __name__=='__main__': main()

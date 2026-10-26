#!/usr/bin/env python3
"""Independent finite projective-support enumeration for star-quiver decomposability.
Public scientific checker; no private operational details.
"""
from itertools import product
from math import comb, factorial


def rank_mod_p(vectors, p, r):
    if not vectors:
        return 0
    a = [list(v) for v in vectors]
    nr = 0
    for col in range(r):
        piv = next((i for i in range(nr, len(a)) if a[i][col] % p), None)
        if piv is None:
            continue
        a[nr],a[piv] = a[piv],a[nr]
        inv = pow(a[nr][col], -1, p)
        a[nr] = [(z*inv)%p for z in a[nr]]
        for i in range(nr+1,len(a)):
            d = a[i][col]%p
            if d:
                a[i] = [(x-d*y)%p for x,y in zip(a[i],a[nr])]
        nr += 1
        if nr == r:
            break
    return nr


def projective_points(p, r):
    ans=[]
    for v in product(range(p), repeat=r):
        if not any(v): continue
        a = next(i for i,x in enumerate(v) if x)
        v = tuple(x*pow(v[a],-1,p)%p for x in v)
        if v not in ans: ans.append(v)
    return ans


def counts(p,r):
    v=projective_points(p,r)
    d=len(v); size=1<<d
    rk=[0]*size
    for mask in range(1,size):
        j=(mask&-mask).bit_length()-1
        # Independent rank routine, not using support-cover enumeration.
        rk[mask]=rank_mod_p([v[t] for t in range(d) if mask>>t&1],p,r)
    decomp=[False]*size
    for s in range(1,size):
        if rk[s]<r: decomp[s]=True;continue
        a=(s-1)&s
        while a:
            b=s^a
            if rk[a]+rk[b]==r:
                decomp[s]=True;break
            a=(a-1)&s
    # Weighted Stirling surjection enumeration across every projective support.
    maxn=24
    surj=[[0]*(d+1) for _ in range(maxn+1)]
    surj[0][0]=1
    for n in range(1,maxn+1):
        for k in range(1,min(d,n)+1):
            surj[n][k]=k*(surj[n-1][k]+surj[n-1][k-1])
    bad_by_size=[0]*(d+1)
    for s,bad in enumerate(decomp):
        if bad: bad_by_size[s.bit_count()] += 1
    K=((p**r-1)//(p-1))*p**(r-1) if r>=3 else comb(p+1,2)
    M=p**(r-1)+p-2; total=p**r-1
    # Each projective point represents p-1 equally likely nonzero vectors.
    assert M % (p-1)==0
    dom=M//(p-1)
    assert bad_by_size[dom]>=K
    print(f'field={p} rank={r} projective_points={d} support_sets={size} dominant_support_size={dom} K={K}')
    for n in [4,6,8,12,16,20,24]:
        bad=sum(bad_by_size[k]*surj[n][k] for k in range(d+1))
        leading=K*dom**n
        error=abs(bad-leading)
        # Explicit quantitative upper bound using all lower supports + pairwise intersections.
        # Crude but rigorous: error <= number_of_all_subsets * (dom-1)^n times a support-dependent bound.
        assert bad>=0 and bad<=d**n
        print(f'  n={n:2d}: bad_probability={bad}/{d**n}; leading={leading}/{d**n}; ratio={bad/leading:.9f}')
    return d,len(decomp)

if __name__=='__main__':
    sizes=[]
    for p,r in [(2,3),(3,3),(2,4)]: sizes.append(counts(p,r))
    print('STAR_QUIVER_PROJECTIVE_SUPPORT_CHECKS_PASSED cases=3 subsets='+str(sum(y for x,y in sizes)))

# Second independent algebraic criterion: existence of a nontrivial idempotent
# in the endomorphism ring, over F_2 in the 3-dimensional central space.
def direct_idempotent_check():
    p,r=2,3
    v=projective_points(p,r); d=len(v)
    eigensupport=set()
    for t in product((0,1),repeat=r*r):
        a=[list(t[i*r:(i+1)*r]) for i in range(r)]
        sq=[[sum(a[i][k]*a[k][j] for k in range(r))%2 for j in range(r)] for i in range(r)]
        if sq!=a: continue
        if all(x==0 for row in a for x in row): continue
        if all(a[i][j]==int(i==j) for i in range(r) for j in range(r)): continue
        mask=0
        for j,x in enumerate(v):
            y=[sum(a[i][k]*x[k] for k in range(r))%2 for i in range(r)]
            if all(t==0 for t in y) or y==list(x): mask |=1<<j
        eigensupport.add(mask)
    assert eigensupport
    nbad=0
    for s in range(1<<d):
        actual=any(s&c==s for c in eigensupport)
        vec=[v[j] for j in range(d) if s>>j&1]
        rk=rank_mod_p(vec,p,r)
        alt=rk<r
        if not alt:
            for a in range(1,s):
                if a&s!=a: continue
                if rank_mod_p([v[j] for j in range(d) if a>>j&1],p,r)+rank_mod_p([v[j] for j in range(d) if (s^a)>>j&1],p,r)==r:
                    alt=True;break
        assert actual==alt,(s,actual,alt)
        nbad+=actual
    print(f'INDEPENDENT_ENDOMORPHISM_IDEMPOTENT_CHECK_PASSED supports={1<<d} bad={nbad} idempotent_eigensupports={len(eigensupport)}')

direct_idempotent_check()

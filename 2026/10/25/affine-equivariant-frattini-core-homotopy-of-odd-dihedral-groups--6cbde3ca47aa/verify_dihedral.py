#!/usr/bin/env python3
"""Independent finite checks of dihedral Frattini-core nerve and affine symmetry.
Scientific output only: no external packages. Group elements are indexed
0..n-1 for rotations r**k and n..2*n-1 for r**k*s.
"""
from itertools import combinations
from math import gcd, prod


def primes(n):
    a=[];d=2
    while d*d<=n:
        if n%d==0:
            a.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:a.append(n)
    return a


def nerve(n):
    assert n>=3 and n%2
    ps=primes(n);q=prod(ps)
    universe=(1<<(2*n))-1
    phi=sum(1<<k for k in range(0,n,q))
    cover=[sum(1<<k for k in range(n))]
    labels=[('R',0)]
    for p in ps:
        for t in range(p):
            m=sum(1<<k for k in range(0,n,p))
            m|=sum(1<<(n+k) for k in range(t,n,p))
            cover.append(m)
            labels.append((p,t))
    def predicted(mask):
        if not mask:return True
        fam={}
        has_R=bool(mask&1)
        for j,(p,t) in enumerate(labels[1:],1):
            if mask>>j&1:fam.setdefault(p,[]).append(t)
        if len(fam)<len(ps):return True
        if has_R:return False
        return all(len(ts)==1 for ts in fam.values())
    counts=[0]*(len(labels)+1)
    for mask in range(1,1<<len(labels)):
        inter=universe
        for j,m in enumerate(cover):
            if mask>>j&1:inter&=m
        observed=bool(inter&~phi)
        exp=predicted(mask)
        assert observed==exp,(n,mask,observed,exp)
        if observed:counts[mask.bit_count()]+=1
    reduced_euler=sum((-1)**(k-1)*counts[k] for k in range(1,len(counts)))-1
    assert reduced_euler==(-1)**(len(ps)-1)*q,(n,counts,reduced_euler)
    return ps,q,cover,labels,counts


def lefschetz(n,ps,labels,cover,u,v):
    q=prod(ps)
    m=len(labels)
    perm=[]
    for label in labels:
        if label[0]=='R':perm.append(0)
        else:
            p,t=label;perm.append(labels.index((p,(u*t+v)%p)))
    # Alternating signed trace over augmented simplicial chain groups.
    reduced_trace=-1
    for mask in range(1,1<<m):
        inds=[j for j in range(m) if mask>>j&1]
        mapped=[perm[j] for j in inds]
        if set(mapped)!=set(inds):continue
        inter=(1<<(2*n))-1
        for j in inds:inter&=cover[j]
        phi=sum(1<<k for k in range(0,n,q))
        if not (inter&~phi):continue
        inversions=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        sign=(-1)**inversions
        reduced_trace+=(-1)**(len(inds)-1)*sign
    nfixed=sum((u*a+v-a)%q==0 for a in range(q))
    assert reduced_trace==((-1)**(len(ps)-1))*nfixed,(n,u,v,reduced_trace,nfixed)
    return nfixed


def run():
    for n in (3,5,9,15,21,45,105):
        ps,q,cover,labels,counts=nerve(n)
        print('nerve',n,'radical',q,'omega',len(ps),'maximal',len(labels),
              'faces',sum(counts),'reducedEuler',(-1)**(len(ps)-1)*q)
        # Independently compute trace as alternating face-permutation signs.
        if n<=21:
            checked=0
            for u in range(n):
                if gcd(u,n)!=1:continue
                for v in range(n):
                    lefschetz(n,ps,labels,cover,u,v)
                    checked+=1
            print('automorphism traces',n,checked)
        elif n==45:
            for u,v in ((1,0),(1,1),(2,3),(4,2),(11,7)):
                lefschetz(n,ps,labels,cover,u,v)
            print('automorphism traces',n,5)
        else:
            for u,v in ((1,0),(1,1),(2,3),(4,2),(11,7)):
                lefschetz(n,ps,labels,cover,u,v)
            print('automorphism traces',n,5)
    print('ALL CHECKS PASSED')
if __name__=='__main__':run()

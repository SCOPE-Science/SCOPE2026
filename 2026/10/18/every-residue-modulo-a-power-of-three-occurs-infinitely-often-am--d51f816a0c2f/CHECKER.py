#!/usr/bin/env python3
"""Finite diagnostic checks for the theorem; not a substitute for its infinite proof."""
from math import comb, gcd

def v3(n):
    c=0
    while n and n%3==0:
        c+=1;n//=3
    return c

def check():
    for t in range(7):
        a=1 if t==0 else (3**t+1)//2
        assert v3(comb(2*a,a))==t,(t,a)
    for r in range(1,7):
        assert comb(2*3**r,3**r)%9==2,r
    for k in range(1,5):
        mod=3**k
        # Every b_R (R>=1) is a primitive root modulo 3**k.
        for r in range(1,6):
            u=comb(2*3**r,3**r)%mod
            order=2*3**(k-1)
            assert pow(u,order,mod)==1
            for q in (2,3):
                if order%q==0: assert pow(u,order//q,mod)!=1,(k,r)
        # Direct integer comparisons of the 3-adic separated-block lemma.
        for r in range(2,7):
            N=3**r
            for a in range(1,25):
                if r>=k+max(v3(i) for i in range(1,2*a+1)):
                    assert (comb(2*(N+a),N+a)-comb(2*N,N)*comb(2*a,a))%mod==0,(k,r,a)
    # Modular factorial prefix yields exact Catalan residues with no giant factorials.
    high=30000
    mod=3**5
    units=[1]*(2*high+1);vals=[0]*(2*high+1)
    for i in range(1,2*high+1):
        t=i;v=0
        while t%3==0:t//=3;v+=1
        units[i]=units[i-1]*(t%mod)%mod
        vals[i]=vals[i-1]+v
    sets={k:set() for k in range(1,6)}
    for n in range(high):
        val=vals[2*n]-vals[n]-vals[n+1]
        if val>=5:c=0
        else:c=pow(3,val,mod)*units[2*n]*pow(units[n]*units[n+1]%mod,-1,mod)%mod
        if n<=120:assert c==comb(2*n,n)//(n+1)%mod,n
        for k in sets:sets[k].add(c%(3**k))
    for k,seen in sets.items():assert len(seen)==3**k,(k,len(seen))
    print('VERIFY_OK: Kummer seeds, primitive roots, exact split, 30000 Catalan residues through 3^5')
if __name__=='__main__':check()

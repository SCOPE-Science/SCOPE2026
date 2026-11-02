#!/usr/bin/env python3
"""Arithmetic proof checks for recovering Jordan types from Engel probabilities."""
from fractions import Fraction

def partitions(d,maxpart):
    def loop(n,maxv):
        if n==0:
            yield ()
        else:
            for v in range(min(n,maxv),0,-1):
                for tail in loop(n-v,v):yield (v,)+tail
    return [x for x in loop(d,maxpart)]

def rank_seq(partition,p):
    return [sum(max(0,s-k) for s in partition) for k in range(p+1)]

def profile(partition,p):
    r=rank_seq(partition,p)
    ans=[]
    for k in range(1,p):
        s=Fraction(1,p*p if k==1 else p)
        ans.append(s+(1-s)*Fraction(1,p**r[k]))
    return tuple(ans)

def reconstruct(profile,p,d):
    r=[d]
    for k,z in enumerate(profile,1):
        s=Fraction(1,p*p if k==1 else p)
        a=(z-s)/(1-s)
        assert a>0
        rank=0
        while a<1:
            a*=p;rank+=1
        assert a==1
        r.append(rank)
    r.append(0)
    m=[r[j-1]-2*r[j]+r[j+1] for j in range(1,p)]
    m.append(r[p-1])
    assert all(x>=0 for x in m)
    return tuple(i for i in range(p,0,-1) for _ in range(m[i-1]))

if __name__=='__main__':
    total=0
    for p in (3,5,7):
        for d in range(1,12):
            seen={}
            for blocks in partitions(d,p):
                sig=profile(blocks,p)
                assert sig not in seen,(p,d,blocks,seen.get(sig))
                seen[sig]=blocks
                assert reconstruct(sig,p,d)==blocks,(p,d,blocks,reconstruct(sig,p,d))
                total+=1
        a=(p,p-2);b=(p-1,p-1)
        ra=rank_seq(a,p);rb=rank_seq(b,p)
        assert ra[:p-1]==rb[:p-1] and ra[p-1]!=rb[p-1],(p,ra,rb)
        assert profile(a,p)[:-1]==profile(b,p)[:-1]
        assert profile(a,p)[-1]!=profile(b,p)[-1]
        print('SHARP_PAIR',p,a,b,'prefix_equal_lengths',p-2,
              'distinguishing_word_length',p-1)
    print('TYPES_TESTED',total)
    print('VERIFY_OK')

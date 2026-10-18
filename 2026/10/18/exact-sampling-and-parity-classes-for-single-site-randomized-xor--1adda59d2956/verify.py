#!/usr/bin/env python3
"""Exact finite-field checks for fixed-coordinate shift register walk."""
from math import gcd
from collections import defaultdict

def A(v,n): return (v>>1)|((v.bit_count() & 1)<<(n-1))

def rank(vs):
    bas={}
    for v in vs:
        while v:
            k=v.bit_length()-1
            if k not in bas: bas[k]=v;break
            v^=bas[k]
    return len(bas)

ranks=0; laws=0
for n in range(1,81):
    for j in range(1,n+1):
        d=gcd(j,n+1)
        v=1<<(j-1); vs=[]
        for t in range(n+4):
            assert rank(vs)==min(t,n+1-d),(n,j,t)
            ranks+=1
            vs.append(v);v=A(v,n)
        # Check algebraic identity and minimal vectors
        assert v==A(vs[-1],n)
        if n<=8:
            for x in {0, (1<<n)-1, n% (1<<n)}:
                cnt={x:1}
                for t in range(0,n+4):
                    vals=list(cnt.values())
                    rt=min(t,n+1-d)
                    assert len(cnt)==2**rt and set(vals)=={2**(t-rt)},(n,j,x,t,rt,len(cnt),set(vals))
                    laws+=1
                    if t<n+3:
                        nxt=defaultdict(int)
                        for y,c in cnt.items():
                            nxt[A(y,n)]+=c
                            nxt[A(y^(1<<(j-1)),n)]+=c
                        cnt=dict(nxt)
def rotation_word(v, g, s=1):
    mask=(1<<g)-1
    return ((v<<s)|(v>>(g-s))) & mask

necklace_checks=0
for g in range(1,13):
    words={v for v in range(1<<g) if v.bit_count()%2==0}
    orbits=[]
    while words:
        v=min(words)
        orb=set()
        x=v
        while x not in orb:
            orb.add(x)
            x=rotation_word(x,g)
        assert orb<=words
        words-=orb
        orbits.append(orb)
    fix_count=0
    for s in range(g):
        d=gcd(g,s)
        repeat=g//d
        fix_count+=(2**d if repeat%2==0 else 2**(d-1))
    assert fix_count%g==0 and len(orbits)==fix_count//g
    necklace_checks+=1
print('PASS:',ranks,'orbit rank checks,',laws,
      'full-state exact-law checks,',necklace_checks,'cyclic-class count checks')

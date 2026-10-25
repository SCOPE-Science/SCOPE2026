#!/usr/bin/env python3
"""Exact census of genus-two hyperelliptic sextics with six split rational fibers."""
from itertools import product
from collections import Counter
from math import comb
P=5

def deg(a):
    while len(a)>1 and a[-1]%5==0: a.pop()
    return len(a)-1

def rem(a,b):
    a=[v%5 for v in a];b=[v%5 for v in b]
    d=deg(b); assert b[d]
    while deg(a)>=d and a[-1]:
        c=a[-1]*pow(b[-1],-1,5)%5
        delta=len(a)-1-d
        for j in range(d+1): a[delta+j]=(a[delta+j]-c*b[j])%5
        deg(a)
    return a

def squarefree(a):
    b=[i*a[i]%5 for i in range(1,7)]
    if not any(b):return False
    x=list(a)
    while any(b):x,b=b,rem(x,b)
    return deg(x)==0

def ev(a,x,y): return sum(a[i]*pow(x,i,5)*pow(y,6-i,5) for i in range(7))%5

def canonical(v):
    k=next(k for k,a in enumerate(v) if a)
    iv=pow(v[k],-1,5)
    return tuple(t*iv%5 for t in v)

def matrices():
    out={}
    for a,b,c,d in product(range(5),repeat=4):
        if (a*d-b*c)%5:
            v=canonical((a,b,c,d));out[v]=v
    assert len(out)==120
    return list(out)

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%5
    return out

def transform(a,M):
    # x->A*x+B*y, y->C*x+D*y; a_i x^i y^(6-i)
    A,B,C,D=M
    powers1=[[1]];powers2=[[1]]
    for i in range(6):
        powers1.append(mul(powers1[-1],[B,A]))
        powers2.append(mul(powers2[-1],[D,C]))
    o=[0]*7
    for i,v in enumerate(a):
        if not v:continue
        z=mul(powers1[i],powers2[6-i]); assert len(z)==7
        for j in range(7):o[j]=(o[j]+v*z[j])%5
    return tuple(o)

def main():
    squares={1,4}
    candidates=[]
    for coeff in product(range(5),repeat=7):
        if coeff[-1] not in squares: continue
        if not all(ev(coeff,x,1) in squares for x in range(5)):continue
        if squarefree(list(coeff)):candidates.append(coeff)
    eligible=set(candidates)
    G=matrices()
    assert all(transform(x,G[0]) in eligible for x in candidates)
    seen=set();orbits=[]
    for f in sorted(eligible):
        if f in seen:continue
        orb=set()
        for M in G:
            fM=transform(f,M)
            for r in (1,4):orb.add(tuple(r*x%5 for x in fM))
        assert orb<=eligible,(f,len(orb-eligible))
        seen|=orb
        orbits.append((f,len(orb),120*2//len(orb)))
    assert seen==eligible
    print('candidate_count',len(candidates),'orbit_count',len(orbits),'group',len(G)*2)
    print('orbit_frequencies',dict(sorted(Counter(s for f,s,stab in orbits).items())))
    for f,s,stab in orbits:print('representative',f,'orbit_size',s,'stabilizer',stab)
if __name__=='__main__':main()

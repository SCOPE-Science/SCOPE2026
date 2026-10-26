#!/usr/bin/env python3
"""Exact finite-field checks for the Fano-cubic net. No external dependencies."""
from collections import Counter

def gf(m):
    poly={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}[m]
    q=1<<m
    def mul(a,b):
        c=0
        while b:
            if b&1:c^=a
            b>>=1;a<<=1
            if a&q:a^=poly
        return c
    def power(a,n):
        t=1
        while n:
            if n&1:t=mul(t,a)
            a=mul(a,a);n>>=1
        return t
    def norm(v):
        z=next((a for a in v if a),None)
        if z is None:return None
        inv=power(z,q-2)
        return tuple(mul(a,inv) for a in v)
    return q,mul,power,norm

def triples(q,norm):
    return sorted({norm((a,b,c)) for a in range(q) for b in range(q) for c in range(q) if a or b or c})

def invertible_binary():
    out=[]
    def det3(M):
        a,b,c,d,e,f,g,h,i=M
        return (a&e&i)^(a&f&h)^(b&d&i)^(b&f&g)^(c&d&h)^(c&e&g)
    for i in range(512):
        M=tuple((i>>j)&1 for j in range(9))
        if det3(M):out.append(M)
    return out
GL=invertible_binary()
assert len(GL)==168

def act(M,v,norm):
    return norm(tuple((v[0] if M[3*i] else 0)^(v[1] if M[3*i+1] else 0)^(v[2] if M[3*i+2] else 0) for i in range(3)))

def incidence(v):
    a,b,c=v
    return sum(t==0 for t in (a,b,c,a^b,a^c,b^c,a^b^c))

def orbits(m):
    q,mul,power,norm=gf(m)
    pts=triples(q,norm)
    by=Counter(incidence(v) for v in pts)
    assert len(pts)==q*q+q+1
    assert by[3]==7 and by[1]==7*(q-2) and by[0]==(q-2)*(q-4)
    cusps={v for v in pts if incidence(v)==0}
    orb_counts=Counter();stab_counts=Counter();reps=[]
    while cusps:
        v=min(cusps)
        orb={act(M,v,norm) for M in GL}
        assert orb<=cusps
        assert all(incidence(x)==0 for x in orb)
        assert len(GL)%len(orb)==0
        stab=len(GL)//len(orb)
        orb_counts[len(orb)]+=1;stab_counts[stab]+=1;reps.append((v,len(orb),stab))
        cusps-=orb
    return {'q':q,'forms':len(pts),'triple_lines':by[3], 'tangent_conic':by[1], 'cusps':by[0], 'orbits':dict(sorted(orb_counts.items())), 'stabilizers':dict(sorted(stab_counts.items())),'representatives':reps}



def check_rational_cusp_points(m):
    q,mul,power,norm=gf(m)
    a,b,c=next(v for v in triples(q,norm) if incidence(v)==0)
    def term(x,y):return mul(x,mul(y,x^y))
    count=sum((mul(a,term(x,y))^mul(b,term(y,z))^mul(c,term(z,x)))==0
              for x,y,z in triples(q,norm))
    assert count==q+1
    return count

if __name__=='__main__':
    print('PGL3(2)',len(GL))
    for m in range(1,7):
        r=orbits(m)
        print('m',m,{k:v for k,v in r.items() if k!='representatives'},'first reps',r['representatives'][:2])

    for m in (3,4): print('direct_cusp_points',1<<m,check_rational_cusp_points(m))

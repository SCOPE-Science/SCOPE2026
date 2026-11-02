#!/usr/bin/env python3
"""Exhaustive order-eight modular group-algebra square-zero checks."""
from collections import Counter

NAMES = ('C8', 'C4xC2', 'C2^3', 'D8', 'Q8')

def group_table(name):
    if name == 'C8': return [[(a+b)%8 for b in range(8)] for a in range(8)]
    if name == 'C4xC2':
        return [[(a%4+b%4)%4+4*((a//4+b//4)%2) for b in range(8)] for a in range(8)]
    if name == 'C2^3': return [[a^b for b in range(8)] for a in range(8)]
    if name in ('D8', 'Q8'):
        k = int(name == 'Q8')
        return [[(a%4 + (-1)**(a//4)*(b%4)+2*k*(a//4)*(b//4))%4
                  +4*((a//4+b//4)%2) for b in range(8)] for a in range(8)]
    raise ValueError(name)

def field_mult(a,b,q):
    if q == 2: return a&b
    v=0
    if b&1: v^=a
    if b&2: v^=a<<1
    if v&8: v^=0b1100
    if v&4: v^=0b111
    return v

def square_zero_count(name,q):
    t=group_table(name)
    sq=[t[i][i] for i in range(8)]
    cross=[(i,j,t[i][j],t[j][i]) for i in range(8) for j in range(i+1,8)
           if t[i][j]!=t[j][i]]
    fm=[[field_mult(a,b,q) for b in range(q)] for a in range(q)]
    sqr=[fm[a][a] for a in range(q)]
    count=0
    for code in range(q**8):
        x=code
        coeff=[0]*8
        for i in range(8): coeff[i]=x%q; x//=q
        result=[0]*8
        for i,a in enumerate(coeff):
            if a: result[sq[i]] ^= sqr[a]
        for i,j,z,w in cross:
            p=fm[coeff[i]][coeff[j]]
            if p: result[z]^=p; result[w]^=p
        count += not any(result)
    return count

def predicted(name,q):
    return {'C8':q**4, 'C4xC2':q**6, 'C2^3':q**7,
            'D8':(2*q-1)*q**4, 'Q8':q**4}[name]

def f2_mult(a,b,t):
    out=0
    for i in range(8):
        if a>>i&1:
            for j in range(8):
                if b>>j&1: out^=1<<t[i][j]
    return out

def verify_dihedral_orbits():
    t=group_table('D8'); units=[x for x in range(256) if x.bit_count()%2]
    roots=[x for x in range(256) if f2_mult(x,x,t)==0]
    central=[x for x in roots if all(f2_mult(x,u,t)==f2_mult(u,x,t) for u in units)]
    assert len(central)==16
    powers={}
    for u in units:
        u2=f2_mult(u,u,t); u3=f2_mult(u2,u,t); assert f2_mult(u3,u,t)==1
        powers[u]=u3
    seen=set(); spectrum=Counter()
    for a in roots:
        if a in seen: continue
        orb={f2_mult(f2_mult(u,a,t),powers[u],t) for u in units}
        assert all(b in roots for b in orb)
        seen.update(orb);spectrum[len(orb)]+=1
    assert len(seen)==48 and spectrum=={1:16,4:8}, spectrum
    print('D8 GF2 conjugacy of square-zero elements:', dict(spectrum), 'PASS')

if __name__=='__main__':
    for q in (2,4):
        for name in NAMES:
            got=square_zero_count(name,q)
            expected=predicted(name,q)
            assert got==expected, (name,q,got,expected)
            print(name, 'GF'+str(q), got, 'PASS')
    verify_dihedral_orbits()
    for name in ('D8','Q8'):
        t=group_table(name)
        roots=[x for x in range(256) if f2_mult(x,x,t)==0]
        commuting=sum(f2_mult(a,b,t)==f2_mult(b,a,t) for a in roots for b in roots)
        expected=2*2**10-2**8 if name=='D8' else 2**8
        assert commuting==expected, (name,commuting,expected)
        print(name, 'GF2 square-zero commuting ordered pairs:', commuting, 'PASS')
    print('ORDER8_GROUP_ALGEBRA_SQZERO_OK')

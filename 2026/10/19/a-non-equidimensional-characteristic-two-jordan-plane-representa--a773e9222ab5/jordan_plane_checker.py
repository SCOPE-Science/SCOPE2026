"""Finite-field independent checks for the two-dimensional Jordan-plane representation census.

Run: python jordan_plane_checker.py
No external packages. The polynomial moduli represent GF(2), GF(4), GF(8).
"""
from itertools import product


def field(q):
    mod = {2: 0b11, 4: 0b111, 8: 0b1011}[q]
    mask = q - 1
    def mul(a, b):
        r = 0
        while b:
            if b & 1:
                r ^= a
            b >>= 1
            a <<= 1
            if a & q:
                a ^= mod
        return r & mask
    return mul


def run(q):
    mul = field(q)
    elems = range(q)
    def multiply(A,B):
        a,b,c,d = A
        e,f,g,h = B
        return (mul(a,e)^mul(b,g), mul(a,f)^mul(b,h),
                mul(c,e)^mul(d,g), mul(c,f)^mul(d,h))
    def add(A,B):
        return tuple(x^y for x,y in zip(A,B))
    def det(A):
        a,b,c,d=A
        return mul(a,d)^mul(b,c)
    def inv(A):
        a,b,c,d=A
        s=next(t for t in elems if mul(t,det(A))==1)
        return (mul(s,d),mul(s,b),mul(s,c),mul(s,a))
    mats=list(product(elems, repeat=4))
    gl=[(G,inv(G)) for G in mats if det(G)]
    found={}
    for X in mats:
        for Y in mats:
            if add(multiply(X,Y),multiply(Y,X))!=multiply(Y,Y):
                continue
            found[(X,Y)]=None
    assert len(found)==q**5+q**4-q**3, (q,len(found))
    visited=set()
    orbit_counts={'y_zero':0,'y_nonzero_nilpotent':0,'y_invertible':0}
    orbit_sizes={}
    for X,Y in found:
        if (X,Y) in visited:
            continue
        orbit={(multiply(multiply(G,X),Gi),multiply(multiply(G,Y),Gi)) for G,Gi in gl}
        assert orbit.issubset(found)
        assert not orbit.intersection(visited)
        visited.update(orbit)
        kind=('y_zero' if Y==(0,0,0,0) else
              'y_nonzero_nilpotent' if det(Y)==0 else 'y_invertible')
        orbit_counts[kind]+=1
        orbit_sizes.setdefault(kind,{}).setdefault(len(orbit),0)
        orbit_sizes[kind][len(orbit)]+=1
    assert visited==set(found)
    assert orbit_counts=={'y_zero':q*q+q,
                          'y_nonzero_nilpotent':q*q,
                          'y_invertible':q*(q-1)}, (q,orbit_counts)
    assert sum(orbit_counts.values())==3*q*q
    assert orbit_sizes['y_nonzero_nilpotent']=={q*q-1:q*q}
    assert orbit_sizes['y_invertible']=={q*(q*q-1):q*(q-1)}
    split=sum(1 for X,Y in found if Y==(0,0,0,0))
    component=sum(1 for X,Y in found if (X[0]^X[3])==0)
    meet=sum(1 for X,Y in found if Y==(0,0,0,0) and X[0]^X[3]==0)
    assert (split,component,meet)==(q**4,q**5,q**3)
    print(f'q={q}: solutions={len(found)}, orbits={sum(orbit_counts.values())} types {orbit_counts}; B={component}, A={split}, intersection={meet}')
    print('  orbit sizes by type:',orbit_sizes)


if __name__=='__main__':
    for q in (2,4):
        run(q)
    print('VERIFY_JORDAN_PLANE_OK')

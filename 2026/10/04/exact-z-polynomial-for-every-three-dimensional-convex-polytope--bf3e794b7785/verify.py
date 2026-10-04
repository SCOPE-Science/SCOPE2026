#!/usr/bin/env python3

def coeffs(v,e,f):
    s=v+f
    a1=s
    a2=4*e
    rank3_g1=4*e-3*s
    h3=a1-4
    h2=6-3*a1+a2+rank3_g1
    return [1,h3,h2,h3,1]

def expected(v,e,f):
    assert v-e+f==2
    s=v+f
    return [1,s-4,2*s-10,s-4,1]

def gamma(v,e,f):
    c=coeffs(v,e,f)
    g1=c[1]-4
    g2=c[2]-6-2*g1
    return [1,g1,g2]

examples=[
    (4,6,4),   # tetrahedron
    (8,12,6),  # cube
    (6,12,8),  # octahedron
    (20,30,12),# dodecahedron
    (12,30,20),# icosahedron
]
for triple in examples:
    v,e,f=triple
    c=coeffs(v,e,f)
    assert c==expected(v,e,f)
    gam=gamma(v,e,f)
    assert gam==[1,v+f-8,0]
    assert gam[1]>=0
    s=v+f
    # (1+x)^2 (x^2+(s-6)x+1)
    factor=[1,s-4,2*s-10,s-4,1]
    assert factor==c
    disc=(s-6)**2-4
    assert disc==(s-8)*(s-4)
    assert disc>=0
print('VERIFY_OK')

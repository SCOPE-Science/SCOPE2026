"""Exact rational verification of claimed periodic itineraries for the farthest-projection triangle map.

Run with Python 3 (standard library only). This checks finitely many rational shape parameters;
the accompanying argument supplies the all-parameter proof.
"""
from fractions import Fraction as F

P = ((F(-1), F(0)), (F(1), F(0)), (F(0), F(1)))
V = tuple(tuple(P[(i+1)%3][j]-P[i][j] for j in range(2)) for i in range(3))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(k,a): return tuple(k*x for x in a)
def inner(a,b,z): return a[0]*b[0]+z*a[1]*b[1]
def position(i,u): return add(P[i],scale(u,V[i]))
def project(i,u,j,z):
    x=position(i,u)
    t=inner(sub(x,P[j]),V[j],z)/inner(V[j],V[j],z)
    y=position(j,t)
    d=inner(sub(x,y),sub(x,y),z)
    return t,d

def formula(word,z):
    D=z**3+4*z**2+z+2
    if word == (0,1,2):
        return (F(2)/(z+3),F(2)/(z+3),(z-1)/(z+3))
    if word == (0,1,0,2):
        return (F(1)/(z+2),F(2)/(z+2),(z+1)/(z+2),z/(z+2))
    if word == (0,1,2,1,0,2,1,2):
        return ((3*z*z+1)/D,2*(z*z+1)/D,z*(z-1)*(z+1)/D,
                2*(3*z*z+1)/D,(z+1)*(z*z+1)/D,z*(z+1)**2/D,
                2*(2*z*z+z+1)/D,z*(z-1)**2/D)
    raise ValueError(word)

def P4(z): return z*z-z-1
def Q8(z): return z**5-5*z**4-5*z**3-4*z*z-2*z-1
def R8(z): return z**6-13*z**5-3*z**4-10*z**3-5*z*z-z-1

def admissible(word,z):
    if word==(0,1,2): return z>1 and z*z-6*z-3<0
    if word==(0,1,0,2): return z>1 and P4(z)<0
    return z>1 and Q8(z)>0 and R8(z)<0

def test(word,z):
    vals=formula(word,z)
    for i,(e,f) in enumerate(zip(word,word[1:]+word[:1])):
        t,d=project(e,vals[i],f,z)
        assert t==vals[(i+1)%len(word)],('projection mismatch',word,z,i,t)
        other=3-e-f
        _,dc=project(e,vals[i],other,z)
        if admissible(word,z):
            assert F(0)<vals[i]<F(1), ('foot outside edge',word,z,i)
            assert d>dc,('wrong chosen branch',word,z,i,d,dc)
    if not admissible(word,z):
        assert any(project(e,vals[i],f,z)[1] <= project(e,vals[i],3-e-f,z)[1]
                   for i,(e,f) in enumerate(zip(word,word[1:]+word[:1]))), ('unexpected legal cycle',word,z)

if __name__=='__main__':
    words=((0,1,2),(0,1,0,2),(0,1,2,1,0,2,1,2))
    grid={F(k,10) for k in range(11,161)}
    grid.update(F(k,100) for k in range(100,720))
    grid.update((F(13,8),F(21,13),F(1618,1000),F(1619,1000),F(5961,1000),F(5962,1000),
                 F(6),F(25,4),F(323,50),F(1293,200),F(7),F(10),F(13)))
    n=0
    for z in sorted(grid):
        if z<=1: continue
        for word in words:
            test(word,z);n+=1
    # Analytic-separation inputs are also checked by exact arithmetic.
    assert Q8(F(59,10))<0<Q8(F(6))
    assert R8(F(7))<0
    assert P4(F(8,5))<0<P4(F(17,10))
    print('CHECK_OK exact projected itineraries:', n, '; endpoint brackets and rational grid verified')

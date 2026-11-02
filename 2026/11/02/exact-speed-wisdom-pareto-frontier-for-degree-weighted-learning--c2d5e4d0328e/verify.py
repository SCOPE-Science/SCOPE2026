#!/usr/bin/env python3
"""Reproducibility checks for degree-biased DeGroot learning on cones over regular graphs.

Requires Python 3 and SymPy. Exact spectral and stationary identities are tested
on multiple nonisomorphic regular base graphs and rational hub-transition rates.
These finite tests complement, rather than replace, the all-size proof.
"""
from sympy import Matrix, Rational, Symbol, diff, factor, expand, zeros


def cycle(n):
    return n, [(i, (i+1)%n) for i in range(n)]

def complete(n):
    return n, [(i,j) for i in range(n) for j in range(i+1,n)]

def disjoint(*parts):
    offset=0; edges=[]
    for n,e in parts:
        edges.extend((a+offset,b+offset) for a,b in e)
        offset+=n
    return offset,edges

def bipartite(a,b):
    return a+b, [(i,a+j) for i in range(a) for j in range(b)]

def prism():
    return 6, [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]

def petersen():
    return 10, ([(i,(i+1)%5) for i in range(5)]
                +[(i,5+i) for i in range(5)]
                +[(5+i,5+(i+2)%5) for i in range(5)])

def check_case(name,base,rate):
    n,edges=base
    H=zeros(n)
    for u,v in edges:
        assert u!=v and H[u,v]==0
        H[u,v]=H[v,u]=1
    degs=[sum(H[i,j] for j in range(n)) for i in range(n)]
    d=degs[0]
    assert d>=1 and all(t==d for t in degs) and n>d+1, name
    p=Rational(rate)
    t=(1-p)/d
    T=zeros(n+1)
    for j in range(n):T[0,j+1]=Rational(1,n)
    for i in range(n):
        T[i+1,0]=p
        for j in range(n):T[i+1,j+1]=t*H[i,j]
    assert T*Matrix([1]*(n+1))==Matrix([1]*(n+1))
    stationary=Matrix([[p/(1+p)]+[1/(n*(1+p))]*n])
    assert stationary*T==stationary and sum(stationary)==1
    for i in range(n+1):
        for j in range(n+1):
            assert stationary[i]*T[i,j]==stationary[j]*T[j,i]
    # Independent characteristic-polynomial computation of the entire model.
    x=Symbol('x')
    hpoly=H.charpoly(x).as_expr()
    nontriv=factor(hpoly/(x-d))
    assert factor((x-d)*nontriv-hpoly)==0
    predicted=(x-1)*(x+p)*t**(n-1)*nontriv.subs(x,x/t)
    assert factor(predicted-T.charpoly(x).as_expr())==0, (name,rate)
    base_spectrum=H.eigenvals()
    assert sum(base_spectrum.values())==n
    eivals=T.eigenvals()
    assert sum(eivals.values())==n+1
    radius=max(abs(complex(z)) for z in base_spectrum if (z!=d or base_spectrum[z]>1))
    rho=max(float(p),radius*float(t))
    actual=max(abs(complex(z)) for z in eivals if z!=1)
    assert abs(rho-actual)<1e-9, (name,rate,rho,actual)
    var=(p*p+Rational(1,n))/(1+p)**2
    assert stationary[0]**2+n*stationary[1]**2==var
    return n,d

def main():
    cases={
        'two disjoint edges':disjoint(complete(2),complete(2)),
        'two triangles':disjoint(complete(3),complete(3)),
        'triangle and square':disjoint(cycle(3),cycle(4)),
        'two squares':disjoint(cycle(4),cycle(4)),
        'C4':cycle(4),'C5':cycle(5),'C6':cycle(6),'C7':cycle(7),
        'triangular prism':prism(), 'K33':bipartite(3,3),
        'Petersen':petersen(),
        'two K4':disjoint(complete(4),complete(4)),
    }
    checks=0
    for name,g in cases.items():
        for p in [Rational(1,7),Rational(1,3),Rational(1,2),Rational(3,4)]:
            check_case(name,g,p)
            checks+=1
    p=Symbol('p',positive=True)
    n=Symbol('n',positive=True)
    v=(p*p+1/n)/(1+p)**2
    assert factor(diff(v,p)-2*(p-1/n)/(1+p)**3)==0
    for N in range(4,101):
        pv=Rational(1,N); ps=Rational(1,2)
        V=lambda z:(z*z+Rational(1,N))/(1+z)**2
        assert V(pv)==Rational(1,N+1)
        assert V(ps)/V(pv)==Rational((N+1)*(N+4),9*N)
        checks+=1
    print('PASS:',checks,'exact full-matrix/variance instances; tested',len(cases),'regular periphery graphs including connected, disconnected, bipartite and nonbipartite examples.')
if __name__=='__main__':main()

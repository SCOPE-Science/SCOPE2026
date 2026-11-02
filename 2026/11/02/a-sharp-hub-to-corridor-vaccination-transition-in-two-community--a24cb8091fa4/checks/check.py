"""Standalone exact checks for a symmetric two-community tree immunization theorem.

No external data or network is needed. Run with Python 3 and SymPy.
"""
from fractions import Fraction
from collections import deque
import sympy as sp

p, s = sp.symbols('p s', positive=True)


def g(j):
    return sum(p**i for i in range(j+1)) + s*p**(j+1)


def hub_score(L):
    R = p*g(L-1)
    return sp.expand(1 + 2*s*p + 2*R + s*(s-1)*p**2 + 2*s*p*R)


def inner_score(L, j):
    return sp.expand(2*g(j)*g(L-j)-1)


def graph(s_count, L):
    n = L+1+2*s_count
    adj = [set() for _ in range(n)]
    for i in range(L):
        adj[i].add(i+1)
        adj[i+1].add(i)
    for h in range(s_count):
        u = L+1+h
        v = L+1+s_count+h
        adj[u].add(0)
        adj[0].add(u)
        adj[v].add(L)
        adj[L].add(v)
    return adj


def exhaustive_score(adj, v, prob):
    n=len(adj)
    distances = []
    for i in range(n):
        ds = [-1]*n
        ds[i]=0
        q=deque([i])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if ds[y]<0:
                    ds[y]=ds[x]+1
                    q.append(y)
        distances.append(ds)
    benefit=Fraction(0)
    for i in range(n):
        for j in range(n):
            if distances[i][j] == distances[i][v]+distances[v][j]:
                benefit += prob ** distances[i][j]
    return benefit


def intended_coefficients(L, sc):
    if L==2:
        return [-2*(sc-1), sc*(3-sc)]
    if L==3:
        return [-2*(sc-1), -sc*sc+sc+2, 2*sc]
    m=L//2
    out=[-2*(sc-1), 4-sc*sc-sc]
    for k in range(2,m):
        out.append(2*(k+1-sc))
    if L%2:
        out.append(2*m)
        start=m+1
    else:
        start=m
    for k in range(start,L):
        out.append(2*(sc+L-1-k))
    assert len(out)==L
    return out


def check():
    count=0
    # Independent path enumeration at many small sizes/parameters.
    for sc in range(2,8):
        for L in range(2,11):
            adj=graph(sc,L)
            b0=hub_score(L).subs(s,sc)
            for prob in [Fraction(1,9),Fraction(1,3),Fraction(2,3),Fraction(9,10)]:
                for v in range(len(adj)):
                    direct=exhaustive_score(adj,v,prob)
                    if v==0 or v==L:form=b0
                    elif 1<=v<L:form=inner_score(L,v).subs(s,sc)
                    else:form=None
                    if form is not None:
                        expected=Fraction(sp.Rational(form.subs(p,sp.Rational(prob.numerator, prob.denominator))))
                        assert direct==expected,(sc,L,v,prob,direct,expected)
                    else:
                        assert direct < exhaustive_score(adj, 0, prob), (sc,L,v,prob)
                    count+=1
            m=L//2
            D=sp.Poly(sp.cancel((inner_score(L,m)-hub_score(L))/p).subs(s,sc),p)
            assert [D.nth(j) for j in range(L)]==intended_coefficients(L,sc),(sc,L,D)
            count+=1
            assert sp.expand(inner_score(L,m)-hub_score(L)).subs({p:1,s:sc}) == 2*m*(L-m)-sc*(sc-1)
            count+=1
    # Strict root and phase witness, with two communities of 3 leaves
    # each and a corridor of 3 internal vertices.
    L=4
    sc=3
    delta=sp.factor((inner_score(L,2)-hub_score(L)).subs(s,sc))
    assert sp.expand(delta-2*p*(3*p**3+4*p**2-4*p-2))==0
    roots=[float(sp.re(r)) for r in sp.nroots(3*p**3+4*p**2-4*p-2) if abs(float(sp.im(r)))<1e-12 and 0<float(sp.re(r))<1]
    assert len(roots)==1 and abs(roots[0]-0.916188398055051)<1e-12
    for pp,target in [(Fraction(1,2),'hub'),(Fraction(49,50),'midpoint')]:
        adj=graph(sc,L)
        vals=[exhaustive_score(adj,v,pp) for v in range(len(adj))]
        tops={v for v,t in enumerate(vals) if t==max(vals)}
        assert tops==({0,L} if target=='hub' else {2}),(pp,tops)
    print('PASS',count,'independent ordered-path exact-rational tests, coefficient identities, and crossover witness')
    print('example crossover p = %.15f' % roots[0])


if __name__=='__main__':
    check()

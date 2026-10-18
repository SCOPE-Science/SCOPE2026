"""Exact checks for four-vertex network-quadratic-payoff comparison.
Requires Python 3, SymPy and NetworkX. Re-running does not depend on external data.
"""
from collections import defaultdict
from math import comb
import networkx as nx
import sympy as S

b = S.Symbol('b', real=True)
F = {
 '3path_to_triangle':6*b**3-4*b**2-b+2,
 'star_to_paw':3*b**6-9*b**5-14*b**4+16*b**3-3*b**2-3*b+2,
 'path_to_paw':4*b**6+b**5-4*b**4+11*b**3-8*b**2-4*b+2,
 'path_to_cycle':2*b**3+3*b+2,
 'paw_to_diamond':11*b**7-8*b**5-14*b**4+25*b**3-8*b**2-4*b+2,
 'cycle_to_diamond':12*b**3-12*b**2-3*b+2,
 'diamond_to_clique':13*b**3-8*b**2+b+2
}

def canonical(g):
    for gg in nx.graph_atlas_g():
        if len(gg) != len(g) or not nx.is_connected(gg):
            continue
        if nx.is_isomorphic(g, gg):
            return (len(g),gg.number_of_edges(),tuple(sorted(dict(gg.degree()).values())))
    raise ValueError('No canonical graph')

def classify(g,h):
    n = len(g)
    if n == 3:
        return '3path_to_triangle'
    deg1 = sorted(dict(g.degree()).values())
    deg2 = sorted(dict(h.degree()).values())
    ed1=g.number_of_edges()
    if ed1 == 3:
        return ('star_to_paw' if deg1 == [1,1,1,3] else 'path_to_paw') if deg2==[1,2,2,3] else 'path_to_cycle'
    if ed1 == 4:
        return 'cycle_to_diamond' if deg1 == [2,2,2,2] else 'paw_to_diamond'
    return 'diamond_to_clique'

reported = defaultdict(set)
checks=0
for n in (3,4):
    for g in nx.graph_atlas_g():
        if len(g)!=n or not nx.is_connected(g):
            continue
        A = S.zeros(n)
        for i,j in g.edges(): A[i,j]=A[j,i]=1
        x=(S.eye(n)+b*A).inv()*S.ones(n,1)
        for i in range(n):
            for j in range(i):
                if g.has_edge(i,j): continue
                h=g.copy();h.add_edge(i,j)
                B=A.copy(); B[i,j]=B[j,i]=1
                y=(S.eye(n)+b*B).inv()*S.ones(n,1)
                D=S.factor((y.dot(y)-x.dot(x))/2)
                key=classify(g,h)
                if key=='star_to_paw':
                    expected=b*(b-1)*F[key]/((3*b*b-1)**2*(b**3+3*b*b-b-1)**2)
                elif key=='path_to_paw':
                    expected=-b*F[key]/((b*b-b-1)**2*(b**3+3*b*b-b-1)**2)
                elif key=='path_to_cycle':
                    expected=-b*F[key]/((2*b+1)**2*(b*b-b-1)**2)
                elif key=='paw_to_diamond':
                    expected=-b*F[key]/((4*b*b-b-1)**2*(b**3+3*b*b-b-1)**2)
                elif key=='cycle_to_diamond':
                    expected=-b*F[key]/((2*b+1)**2*(4*b*b-b-1)**2)
                elif key=='diamond_to_clique':
                    expected=-b*F[key]/((3*b+1)**2*(4*b*b-b-1)**2)
                else:
                    expected=-b*F[key]/((2*b+1)**2*(2*b*b-1)**2)
                assert S.cancel(D-expected) == 0,(key,g.edges(),i,j)
                checks+=1
                reported[key].add((canonical(g), canonical(h)))
print('Individual labeled atlas edge additions checked:',checks)
assert len(reported)==7
for k,v in reported.items():
    print(k, 'distinct graph-class pairs:',len(v))
    assert len(v)==1

def bernstein_coeffs(poly, limit):
    p=S.Poly(S.expand(poly),b)
    d=p.degree()
    a=[p.nth(i) for i in range(d+1)]
    return [S.factor(sum(a[k]*limit**k*S.Rational(comb(j,k),comb(d,k)) for k in range(j+1))) for j in range(d+1)]
for name, limit in [('star_to_paw',S.Rational(1,3)),('paw_to_diamond',S.Rational(5,12))]:
    c=bernstein_coeffs(F[name],limit)
    print('Bernstein positivity',name,limit,c)
    assert all(v>0 for v in c)

p=F['cycle_to_diamond']
q=F['path_to_paw']
assert p.subs(b,0)>0 and p.subs(b,S.Rational(1,2))<0
assert q.subs(b,0)>0 and q.subs(b,S.sqrt(2)-1)<0
assert p.subs(b,S.Rational(349,1000))>0 and p.subs(b,S.Rational(350,1000))<0
assert q.subs(b,S.Rational(357,1000))>0 and q.subs(b,S.Rational(358,1000))<0
# p' = 36b^2-24b-3 < 0 on [0,1/2]; q' decomposes as
# b^3(24b^2+5b-16)+b(33b-16)-4 < 0 on [0,sqrt(2)-1].
assert S.factor(S.diff(q,b)-(b**3*(24*b*b+5*b-16)+b*(33*b-16)-4)) == 0
print('threshold C4',S.nroots(p,maxsteps=100))
print('threshold P4',S.nroots(q,maxsteps=100))

# Fully independent elementary rational certificate at b=3/8
r=S.Rational(3,8)
C=nx.cycle_graph(4)
B=nx.cycle_graph(4);B.add_edge(0,2)
# Use exact integer SymPy adjacency here (not a floating point array).
def eq(g):
    M=S.eye(len(g))
    for i,j in g.edges(): M[i,j]=M[j,i]=r
    return M.inv()*S.ones(len(g),1)
x,y=eq(C),eq(B)
assert sorted(x)==[S.Rational(4,7)]*4
assert sorted(y)==[S.Rational(4,13)]*2+[S.Rational(10,13)]*2
assert S.factor(sum(y)-sum(x)) == -S.Rational(12,91)
assert S.factor((y.dot(y)-x.dot(x))/2) == S.Rational(276,8281)
print('Witness efforts:',list(x), list(y))
print('Witness total effort loss',sum(y)-sum(x), 'payoff increase',(y.dot(y)-x.dot(x))/2)

# For every connected n<=4 graph adjacency eigenvalues satisfy lambda_min>=-2,
# since maximum degree <=3 and for n=4 graphs spectral calculation is finite.
for g in nx.graph_atlas_g():
    if len(g) not in (2,3,4) or not nx.is_connected(g):continue
    A=S.zeros(len(g))
    for i,j in g.edges(): A[i,j]=A[j,i]=1
    assert (S.eye(len(g))+S.Rational(1,2)*A).is_positive_semidefinite
print('All checks passed.')

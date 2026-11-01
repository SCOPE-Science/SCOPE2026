#!/usr/bin/env python3
"""Exact-rational checks for endpoint actuation of reflection-symmetric two-rail paths.
Run with Python 3 and SymPy (tested with SymPy 1.13). No external data files.
"""
from fractions import Fraction
import sympy as sp

x=sp.Symbol('x')

def base_laplacian(weights):
    n=len(weights)+1
    M=sp.zeros(n)
    for i,w in enumerate(weights):
        w=sp.Rational(w)
        M[i,i]+=w; M[i+1,i+1]+=w
        M[i,i+1]-=w; M[i+1,i]-=w
    return M

def parity_polynomials(weights):
    L=base_laplacian(weights)
    n=L.rows
    basis={+1:[],-1:[]}
    for j in range(n//2):
        for parity in (+1,-1):
            v=sp.zeros(n,1)
            v[j]=1; v[n-1-j]=parity
            basis[parity].append(v)
    if n%2:
        v=sp.zeros(n,1);v[n//2]=1
        basis[+1].append(v)
    ans={}
    for sign in (+1,-1):
        vectors=basis[sign]
        if not vectors:
            ans[sign]=sp.Poly(1,x);continue
        B=sp.Matrix.hstack(*vectors)
        A=(B.T*B).inv()*B.T*L*B
        ans[sign]=sp.Poly(A.charpoly(x).as_expr(),x).monic()
    return ans

def degree_gcd(a,b):
    return sp.degree(sp.gcd(a,b))

def predicted_ranks(weights,g):
    n=len(weights)+1
    P=parity_polynomials(weights)
    d=2*sp.sympify(g)
    translated={p:sp.Poly(P[p].as_expr().subs(x,x+d),x,extension=True) for p in (+1,-1)}
    same=degree_gcd(P[1],translated[1])+degree_gcd(P[-1],translated[-1])
    opposite=degree_gcd(P[1],translated[-1])+degree_gcd(P[-1],translated[1])
    return (2*n-int(same),2*n-int(opposite))

def kalman_rank(weights,g,opposite=False):
    n=len(weights)+1
    H=sp.kronecker_product(base_laplacian(weights),sp.eye(2)) + sp.kronecker_product(sp.eye(n),sp.sympify(g)*sp.Matrix([[1,-1],[-1,1]]))
    B=sp.zeros(2*n,2)
    B[0,0]=1
    B[2*(n-1)+(1 if opposite else 0),1]=1
    cols=B; v=B
    for j in range(1,2*n):
        v=H*v
        cols=cols.row_join(v)
    return cols.rank()

def check(weights,g):
    assert list(weights)==list(reversed(weights)) and all(w>0 for w in weights)
    p=predicted_ranks(weights,g)
    k=(kalman_rank(weights,g),kalman_rank(weights,g,True))
    assert p==k, (weights,g,p,k)
    return p

def main():
    count=0
    for n in range(2,8):
        for g in (sp.Rational(1,2),sp.Rational(1),sp.Rational(3,2),sp.Rational(2,3)):
            check([sp.Rational(1)]*(n-1),g);count+=1
    # Variably weighted mirror-symmetric paths, both rational and repeated eigenvalue gaps.
    weights=[(sp.Rational(2),sp.Rational(2)),(sp.Rational(1),sp.Rational(3),sp.Rational(1)),
             (sp.Rational(2),sp.Rational(3),sp.Rational(2)),
             (sp.Rational(1),sp.Rational(4),sp.Rational(4),sp.Rational(1)),
             (sp.Rational(3,2),sp.Rational(5,3),sp.Rational(3,2)),
             (sp.Rational(2),sp.Rational(3),sp.Rational(4),sp.Rational(3),sp.Rational(2))]
    for w in weights:
        for g in [sp.Rational(1,2),sp.Rational(1),sp.Rational(3,2)]:
            check(w,g);count+=1
    # Explicit first simultaneous failure on the six-rung unit ladder.
    assert predicted_ranks([sp.Integer(1)]*5,sp.Rational(1,2))==(11,10)
    assert predicted_ranks([sp.Integer(1)]*5,sp.Rational(1))==(11,11)
    # Precise separate resonance examples on the four-rung ladder.
    assert predicted_ranks([sp.Integer(1)]*3,sp.Rational(1))==(7,8)
    # Collision at gap sqrt(2), where the opposite-rail rank loses two dimensions.
    assert predicted_ranks([sp.Integer(1)]*3,sp.sqrt(2)/2)==(8,6)
    assert check([sp.Integer(1)]*3,sp.sqrt(2)/2)==(8,6)
    # Exhaustively identify both index-parity difference sets in the small unit paths.
    for n in range(2,7):
        spectrum=[2-2*sp.cos(sp.pi*k/n) for k in range(n)]
        even_gaps={sp.simplify(spectrum[i]-spectrum[j]) for i in range(n) for j in range(i) if (i-j)%2==0}
        odd_gaps={sp.simplify(spectrum[i]-spectrum[j]) for i in range(n) for j in range(i) if (i-j)%2==1}
        common=even_gaps.intersection(odd_gaps)
        assert common==(set() if n<6 else {sp.Integer(1),sp.Integer(2)}), (n,common)
    print('PASS: %d exact-rational predicted-versus-Kalman rank comparisons; four boundary assertions; five exhaustive exact small-path gap-set checks.'%count)

if __name__=='__main__':main()

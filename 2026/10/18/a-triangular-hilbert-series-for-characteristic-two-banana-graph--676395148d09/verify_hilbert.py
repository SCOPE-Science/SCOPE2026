"""Exact reproducibility checks for the characteristic-two banana Jacobian theorem.
No randomization or floating-point arithmetic is used.
Usage: python verify_hilbert.py
"""
import itertools
import math
import sympy as sp


def e(indices, r, x):
    return sum((sp.prod(x[i] for i in I) for I in itertools.combinations(indices, r)), sp.Integer(0))


def polynomial_data(n):
    x=sp.symbols('x0:'+str(n))
    F=e(range(n), n-1,x)
    J=[F]+[sp.diff(F,z) for z in x]
    g={}
    for s in range(2,n+1):
        tail=sp.prod(x[j]**2 for j in range(s,n))
        for i in range(s-1):
            g[s,i]=sp.expand(tail*e([j for j in range(s) if j!=i],s-2,x))
    return x,F,J,g


def initial_monomials(n):
    return [tuple((0 if j==i or j==s-1 else 1) if j<s else 2 for j in range(n))
            for s in range(2,n+1) for i in range(s-1)]


def monomial_numerator(n,mons):
    # Inclusion--exclusion over lcm lattice, exact, for the initial monomial ideal.
    values={(0,)*n:1}
    for m in mons:
        d=dict(values)
        for a,c in values.items():
            z=tuple(max(a[j],m[j]) for j in range(n))
            d[z]=d.get(z,0)-c
        values={a:c for a,c in d.items() if c}
    num={}
    for a,c in values.items():
        k=sum(a)
        num[k]=num.get(k,0)+c
    return num


def denominator_reduce(num, steps):
    v=dict(num)
    for _ in range(steps):
        w={}; running=0
        for k in range(max(v)+1):
            running+=v.get(k,0)
            w[k]=running
        assert running==0, ('not_divisible',v)
        v={k:c for k,c in w.items() if c}
    return v


def check(n):
    x,F,J,g=polynomial_data(n)
    gb=sp.groebner(J,*x,order='grevlex',modulus=2)
    predicted=initial_monomials(n)
    actual=[tuple(z for z in p.terms()[0][0]) for p in gb.polys]
    assert set(actual)==set(predicted) and len(actual)==len(predicted)
    # Independently construct the proposed basis, check that all its elements
    # lie in the true Jacobian ideal, and that all true generators reduce to 0.
    for polynomial in g.values():
        assert gb.reduce(polynomial)[1]==0
    proposed=sp.groebner(list(g.values()),*x,order='grevlex',modulus=2)
    for polynomial in J:
        assert proposed.reduce(polynomial)[1]==0
    h=denominator_reduce(monomial_numerator(n,predicted),3)
    target={k:math.comb(k+2,2) for k in range(n-2)}
    target.update({2*n-5-k:math.comb(k+2,2) for k in range(n-2)})
    assert h==target
    assert sum(h.values())==2*math.comb(n,3)
    # Symbolically check the adjacent-level syzygy identities in GF(2).
    if n<=8:
        for s in range(3,n):
            for i in range(s-1):
                lhs=sp.Poly((x[s-1]+x[s])*g[s,i]+x[s]**2*g[s+1,i],*x,modulus=2)
                if i<s-2: rhs=g[s-1,i]
                else: rhs=sum((g[s-1,j] for j in range(s-2)),sp.Integer(0))
                assert sp.Poly(lhs.as_expr()-rhs,*x,modulus=2).is_zero
                lhs2=sp.Poly(x[i]*g[s,i]+x[s]**2*g[s+1,s-1],*x,modulus=2)
                rhs2=x[s]*sum((g[s,j] for j in range(s-1)),sp.Integer(0))
                rhs2+=x[s-1]*sum((g[s,j] for j in range(s-1) if j!=i),sp.Integer(0))
                rhs2+=rhs
                assert sp.Poly(lhs2.as_expr()-rhs2,*x,modulus=2).is_zero
        for s in range(3,n+1):
            for i in range(s-1):
                for j in range(i+1,s-1):
                    lhs=(x[i]+x[s-1])*g[s,i]+(x[j]+x[s-1])*g[s,j]
                    def virt(i):return g[s-1,i] if i<s-2 else sum((g[s-1,q] for q in range(s-2)),sp.Integer(0))
                    assert sp.Poly(lhs-virt(i)-virt(j),*x,modulus=2).is_zero
    return n,len(actual),sum(h.values()),len(h)


if __name__=='__main__':
    for n in range(4,12):
        print('n, basis_count, degree, h_length:',check(n),flush=True)
    print('VERIFY_OK')

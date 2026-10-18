"""Reproducibility checks for exact Bernstein overiteration endpoint norm.

Requires Python 3 and SymPy. Finite checks illustrate, but do not
replace, the all-degree and all-iterate analytic arguments.
"""
from math import comb
from sympy import Matrix, Rational, eye, simplify

checks = 0

def eq(a, b):
    global checks
    assert simplify(a - b) == 0, (a, b)
    checks += 1


def weights(n, x):
    return Matrix([[comb(n, j) * x**j * (1-x)**(n-j) for j in range(n+1)]])


def transition(n):
    return Matrix.vstack(*[weights(n, Rational(i,n)) for i in range(n+1)])

for n in range(2, 9):
    P = transition(n)
    Q = P[1:n, 1:n]
    interior_ones = Matrix([1]*(n-1))
    v = interior_ones
    for k in range(1, 8):
        # v = Q^(k-1) 1, and Bernstein initial sampling occurs at x.
        x0 = Rational(1,2)
        b = weights(n, x0)
        norm_from_survival = 2 * (b[:, 1:n]*v)[0]
        full_distribution = b * (P**(k-1))
        a0 = -(1-x0)
        a1 = -x0
        signed = Matrix([[full_distribution[j] + (a0 if j == 0 else a1 if j == n else 0) for j in range(n+1)]])
        eq(sum(abs(z) for z in signed), norm_from_survival)
        eq((signed*Matrix([1]*(n+1)))[0], 0)
        eq((signed*Matrix([Rational(j,n) for j in range(n+1)]))[0], 0)
        for i in range(11):
            x = Rational(i,10)
            value = (weights(n,x)[:,1:n]*v)[0]
            assert value <= norm_from_survival/2, (n,k,x,value)
            checks += 1
        # Exact discrete strict concavity of the survival function on nodes.
        values = [(weights(n,Rational(i,n))[:,1:n]*v)[0] for i in range(n+1)]
        for i in range(n-1):
            assert values[i]-2*values[i+1]+values[i+2] < 0
            checks += 1
        v=Q*v
    # Perron mode of the absorbing kernel.
    lam = Rational(n-1,n)
    h = Matrix([Rational(i,n)*(1-Rational(i,n)) for i in range(1,n)])
    eq((Q*h-lam*h).norm(),0)
    eigvec = (Q.T-lam*eye(n-1)).nullspace()
    assert len(eigvec)==1
    p=eigvec[0]/sum(eigvec[0]); H=(p.T*h)[0]
    assert all(pi>0 for pi in p) and H>0
    checks+=2
    eq((p.T*Q-lam*p.T).norm(),0)
    for k in (25,60):
        # Distinct eigenvalues yield convergence toward 1/(2H).
        survival=(weights(n,Rational(1,2))[:,1:n]*(Q**(k-1))*interior_ones)[0]
        est=2*survival/(lam**k)
        if n>=4:
            assert abs(est-Rational(1,2)/H)<Rational(1,100)  # n<=8, k>=25
        else:
            eq(est,Rational(1,2)/H)
        checks+=1

# Completely explicit degree-four example, valid for all k by a
# two-dimensional invariant symmetric sector and the first two checks.
n=4
Q=transition(n)[1:n,1:n]
for k in range(1,13):
    central=(weights(n,Rational(1,2))[:,1:n]*(Q**(k-1))*Matrix([1]*(n-1)))[0]
    eq(central, Rational(25,21)*Rational(3,4)**k-Rational(4,21)*Rational(3,32)**k)

print(f"PASS: {checks} exact-rational finite assertions")

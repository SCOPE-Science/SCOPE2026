import sympy as sp
from itertools import product

t,x,y,a,b = sp.symbols("t x y a b")
vars = [t,x,y,a,b]
weights = [0,1,1,2,2]

sec = [t*a-x**2, t*b-y**2]
tan = [t*a-x**2, t*b-x*y, x*b-a*y]

def lie_data(Fs):
    n = len(vars)
    m = len(Fs)
    Avars = sp.symbols("A0:%d" % (n*n))
    Bvars = sp.symbols("B0:%d" % (m*m))
    A = sp.Matrix(n,n,Avars)
    xv = sp.Matrix(vars)
    dvars = list(A*xv)

    monoms = [vars[i]*vars[j] for i in range(n) for j in range(i,n)]
    eqs = []
    for i,F in enumerate(Fs):
        expr = sum(sp.diff(F,vars[k])*dvars[k] for k in range(n))
        expr -= sum(Bvars[i*m+j]*Fs[j] for j in range(m))
        P = sp.Poly(sp.expand(expr), *vars, domain=sp.QQ.frac_field(*Avars,*Bvars))
        for mon in monoms:
            exp = sp.Poly(mon,*vars).monoms()[0]
            eqs.append(P.coeff_monomial(exp))

    unknown = list(Avars)+list(Bvars)
    M,_ = sp.linear_eq_to_matrix(eqs,unknown)
    null = M.nullspace()
    dim = len(null)

    # Project the nullspace to the A-coordinates.  Since the generators
    # Fs are linearly independent, B is uniquely determined by A.
    PA = sp.Matrix([[v[i] for v in null] for i in range(n*n)])
    assert PA.rank() == dim

    graded = {}
    for d in range(-2,3):
        allowed = [
            i*n+j for i in range(n) for j in range(n)
            if weights[i]-weights[j] == d
        ]
        disallowed = [k for k in range(n*n) if k not in allowed]
        dim_d = dim - PA[disallowed,:].rank()
        if dim_d:
            graded[d] = dim_d
    assert sum(graded.values()) == dim
    return dim, graded

def compositions(total,n,prefix=()):
    if n == 1:
        yield prefix+(total,)
    else:
        for i in range(total+1):
            yield from compositions(total-i,n-1,prefix+(i,))

def hilbert_values(Fs,maxd=8):
    G = sp.groebner(Fs,*vars,order="grevlex",domain=sp.QQ)
    lms = [p.LM(order=G.order).exponents for p in G.polys]
    H = []
    for d in range(maxd+1):
        c = 0
        for e in compositions(d,len(vars)):
            if not any(all(ei>=mi for ei,mi in zip(e,lm)) for lm in lms):
                c += 1
        H.append(c)
    return H

# Discriminant restrictions for binary quadrics A X^2+B XY+C Y^2.
A,B,C = sp.symbols("A B C")
disc = B**2 - 4*A*C
u,v = sp.symbols("u v")
disc_sec = sp.expand(disc.subs({A:u,B:0,C:v}))
disc_tan = sp.expand(disc.subs({A:u,B:v,C:0}))
assert disc_sec == -4*u*v
assert disc_tan == v**2

# Parametrizations land in the asserted ideals.
s,p,q = sp.symbols("s p q")
sec_sub = {t:s**2,x:s*p,y:s*q,a:p**2,b:q**2}
tan_sub = {t:s**2,x:s*p,y:s*q,a:p**2,b:p*q}
assert all(sp.expand(F.subs(sec_sub)) == 0 for F in sec)
assert all(sp.expand(F.subs(tan_sub)) == 0 for F in tan)

# The tangent equations are the 2x2 minors of [[t,x,y],[x,a,b]].
M2 = sp.Matrix([[t,x,y],[x,a,b]])
minors = [
    sp.expand(M2[:,[0,1]].det()),
    sp.expand(M2[:,[0,2]].det()),
    sp.expand(M2[:,[1,2]].det())
]
assert minors == tan

# Hilbert functions have stable second differences equal to the degrees.
Hsec = hilbert_values(sec)
Htan = hilbert_values(tan)
D2sec = [Hsec[i]-2*Hsec[i-1]+Hsec[i-2] for i in range(2,len(Hsec))]
D2tan = [Htan[i]-2*Htan[i-1]+Htan[i-2] for i in range(2,len(Htan))]
assert set(D2sec) == {4}
assert set(D2tan) == {3}

# Secant singular locus contains the whole boundary line t=x=y=0:
Jsec = sp.Matrix([[sp.diff(F,z) for z in vars] for F in sec])
Jboundary = Jsec.subs({t:0,x:0,y:0})
assert Jboundary.rank() == 1

dim_sec, grad_sec = lie_data(sec)
dim_tan, grad_tan = lie_data(tan)
assert dim_sec == 5 and grad_sec == {0:3,1:2}
assert dim_tan == 7 and grad_tan == {-1:1,0:4,1:2}

print("secant_discriminant=-4*u*v")
print("tangent_discriminant=v^2")
print("secant_degree=4")
print("tangent_degree=3")
print("secant_cone_aut_dim=5")
print("secant_euler_weights=0:3,1:2")
print("tangent_cone_aut_dim=7")
print("tangent_euler_weights=-1:1,0:4,1:2")
print("VERIFY_OK")

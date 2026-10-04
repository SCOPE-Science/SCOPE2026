from fractions import Fraction

def mat_moment(p,s):
    return (
        (1-2*p*s+p*s*s, -2*p*(1-s), p),
        ((1-p)*s, 1-p, 0),
        ((1-p)*s*s, 2*(1-p)*s, 1-p),
    )

def coeffs(p,s):
    a1 = -p*s*s + 2*p*s + 2*p - 3
    a2 = p*p*s*s + 2*p*p*s + p*p - p*s*s - 2*p*s - 4*p + 3
    a3 = -(1-p)*(1-p)
    return a1,a2,a3

def jury(p,s):
    a1,a2,a3=coeffs(p,s)
    return (
        1-abs(a3),
        1+a1+a2+a3,
        1-a1+a2-a3,
        1-a2+a1*a3-a3*a3,
    )

def branch_moments(p,s,x,e):
    # success
    xs=(1-s)*x-e
    es=Fraction(0)
    # failure
    xf=x
    ef=e+s*x
    X=p*xs*xs+(1-p)*xf*xf
    Y=p*xs*es+(1-p)*xf*ef
    Z=p*es*es+(1-p)*ef*ef
    return X,Y,Z

def apply(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))

# Exact branch averaging and coefficient/Jury identities.
for p in (Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(1)):
    for s in (Fraction(1,10),Fraction(1,2),Fraction(3,2)):
        x=Fraction(7,5); e=Fraction(-2,7)
        direct=branch_moments(p,s,x,e)
        calc=apply(mat_moment(p,s),(x*x,x*e,e*e))
        assert direct==calc

        a1,a2,a3=coeffs(p,s)
        j0,j1,jm,jr=jury(p,s)
        assert j0 == 1-(1-p)*(1-p)
        assert j1 == p*s*(2*p-(2-p)*s)
        assert jm == p*p*s*s+2*p*p*s+2*p*p-4*p*s-8*p+8

        jr_formula = p*(-p**3+p*p*s*s-2*p*p*s+2*p*p-3*p*s*s+2*p*s+2*s*s)
        assert jr == jr_formula

# The two nonbinding Jury conditions are positive at their analytic minima/base points.
for p in (Fraction(1,20),Fraction(1,5),Fraction(1,2),Fraction(9,10),Fraction(1)):
    sv=(2-p)/p
    _,_,jm,_=jury(p,sv)
    assert jm==(2-p)*(2-p) > 0
    _,_,_,jr0=jury(p,Fraction(0))
    assert jr0==p**3*(2-p) > 0

# Boundary factor, renewal factor, and cycle optimum.
for p in (Fraction(1,20),Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(1)):
    cap=2*p/(2-p)
    _,j1,_,_=jury(p,cap)
    assert j1==0

    def qcycle(s):
        return 1-2*s/p+(2-p)*s*s/(p*p)

    sopt=p/(2-p)
    assert qcycle(sopt)==(1-p)/(2-p)
    assert qcycle(cap)==1
    assert qcycle(cap/Fraction(2))<1
    assert qcycle(cap*Fraction(11,10))>1

    # Exact geometric moments.
    # E[J]=1/p, E[J^2]=(2-p)/p^2.
    assert 1-2*sopt*(1/p)+sopt*sopt*((2-p)/(p*p)) == qcycle(sopt)

# Memoryless Bernoulli dropout has the compression-independent stability threshold 2.
for p in (Fraction(1,20),Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(1)):
    def qplain(s):
        return 1-2*p*s+p*s*s
    assert qplain(Fraction(1))==1-p
    assert qplain(Fraction(1))<1 or p==0
    assert qplain(Fraction(2))==1
    assert qplain(Fraction(21,10))>1

print("verification passed")

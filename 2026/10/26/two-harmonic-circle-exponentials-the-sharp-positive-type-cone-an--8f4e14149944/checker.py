"""Independent numerical checks for the two-harmonic exponential circle kernel.

Standard Python 3 only. Numeric checks are illustrations, not substitutes for
infinite-frequency proofs. All Fourier integrals use midpoint-independent
uniform periodic trapezoidal sums.
"""
import math

TAU=2*math.pi

def sample_coeff(p,q,a,b,n,mesh=32768):
    return sum(math.exp(a*math.cos(p*TAU*j/mesh)+b*math.cos(q*TAU*j/mesh))
               *math.cos(n*TAU*j/mesh) for j in range(mesh))/mesh

def bessel_i(n,x):
    assert x >= 0
    n=abs(n)
    s=0.0
    for k in range(100):
        t=(x/2)**(2*k+n)/math.factorial(k)/math.factorial(k+n)
        s+=t
        if k>10 and abs(t)<1e-18:
            break
    return s

def positive_convolution(p,q,a,b,n,limit=40):
    total=0.0
    for j in range(-limit,limit+1):
        if (n-q*j)%p==0:
            total += bessel_i((n-q*j)//p,a)*bessel_i(j,b)
    return total

def discrete_eigenvalue(p,q,a,b,n,N):
    return sum(math.exp(a*math.cos(p*TAU*j/N)+b*math.cos(q*TAU*j/N))
               *math.cos(n*TAU*j/N) for j in range(N))

# 1. Two independent algorithms agree in the strictly positive quadrant.
max_error=0.0
for p,q,a,b in ((1,2,0.8,0.6),(2,5,1.2,0.7),(3,7,0.9,0.3)):
    for n in range(16):
        c=sample_coeff(p,q,a,b,n)
        d=positive_convolution(p,q,a,b,n)
        max_error=max(max_error,abs(c-d))
assert max_error<2e-11,max_error

# 2. Explicit negative Fourier witnesses in both signed regimes.
cases=((1,2,1.0,-0.5,2),
       (1,3,2.0,-0.3,3),
       (2,5,1.2,-0.2,1),
       (1,2,-0.4,1.2,1),
       (2,3,-0.1,0.9,2))
neg=[]
for p,q,a,b,n in cases:
    c=sample_coeff(p,q,a,b,n)
    assert c < -1e-3,(p,q,a,b,n,c)
    neg.append(round(c,12))

# 3. Finite equally spaced configurations actually exhibit negative
#    eigenvalues in a clearly forbidden parameter regime.
N=32
negative_grid_eigenvalue=discrete_eigenvalue(1,2,1.0,-0.5,2,N)
assert negative_grid_eigenvalue < -1.0,negative_grid_eigenvalue

# 4. Fixed-grid camouflage: a strictly positive baseline survives a small
#    negative second harmonic on the grid, although global positivity fails.
Nsmall=16
small_b=-1e-7
small_grid=[discrete_eigenvalue(1,2,1.0,small_b,n,Nsmall)
            for n in range(Nsmall)]
assert min(small_grid)>0, min(small_grid)

# 5. Directly check the complex-radius logarithmic growth mechanism.
#    This is not the proof; the inequalities diverge analytically with r.
def delta(r,p,q,a,b,theta):
    return (a/2)*(math.cos(p*theta)-1)*(r**p+r**(-p)) + \
           (b/2)*(math.cos(q*theta)-1)*(r**q+r**(-q))
assert delta(30,1,2,1.0,-0.5,math.pi/2)>100
assert delta(40,2,5,-0.1,0.9,2*math.pi/5)>10

print('PASS: positive convolution/trapezoid comparisons =',3*16)
print('maximum Fourier comparison error = %.3g'%max_error)
print('PASS: five signed negative Fourier coefficients =',neg)
print('PASS: finite-grid negative eigenvalue = %.10f'%negative_grid_eigenvalue)
print('PASS: finite-grid camouflage min eigenvalue = %.10g'%min(small_grid))
print('PASS: two complex-radius growth inequalities')

"""Exact symbolic and independent finite-dimensional checks for quadratic metric-graph projection.

Requires Python 3 and SymPy. The infinite-dimensional/index-parametric statements
are established by the accompanying analytic argument, not by these finite tests.
"""
import sympy as S

x, z = S.symbols('x z', real=True)
n = S.symbols('n', positive=True)
h = x * (1 - x)
phi = S.expand(1 - x - S.Rational(5, 2) * h)
psi = S.expand(x - S.Rational(5, 2) * h)
assert S.integrate(h*h, (x,0,1)) == S.Rational(1,30)
assert S.integrate(phi*h, (x,0,1)) == 0
assert S.integrate(psi*h, (x,0,1)) == 0
assert S.integrate(phi**2, (x,0,1)) == S.Rational(1,8)
assert S.integrate(phi*psi, (x,0,1)) == -S.Rational(1,24)
assert S.simplify(phi+psi+5*h-1) == 0

D = 9*n*n - 8*n + 4
J = (5+2*S.sqrt(5))/30
I = n/6 + D**S.Rational(3,2)/(75*n*n)
N = S.factor(12/(3*n-2)*(I+(n-2)*J/2))
L = S.Rational(61,25)+2*S.sqrt(5)/15
B = S.Rational(24,25)+8*S.sqrt(5)/45
assert S.simplify(S.limit(N,n,S.oo)-L)==0
assert S.simplify(S.limit(n*(L-N),n,S.oo)-B)==0

deriv = 8*(5*S.sqrt(5)*n**3 + (9*n*n-22*n+8)*S.sqrt(D))/(25*n**3*(3*n-2)**2)
assert S.simplify(S.diff(N,n)-deriv)==0
assert 9*3*3-22*3+8 > 0   # polynomial is increasing on n>=3
assert S.simplify((9*n*n-22*n+8).subs(n,2))==0
assert S.N(N.subs(n,5),40)<S.Rational(5,2)<S.N(N.subs(n,6),40)

# Exact original (non-orthogonalized) nodal-plus-edge-bubble Gram matrix.
# In this basis the endpoint functions on an edge are 1-t and t; the bubble is t(1-t).
def direct_kernel_check(size):
    edges=[(i,j) for i in range(size) for j in range(i+1,size)]
    q=size+len(edges)
    mat=S.zeros(q,q)
    local=S.Matrix([[S.Rational(1,3),S.Rational(1,6),S.Rational(1,12)],
                    [S.Rational(1,6),S.Rational(1,3),S.Rational(1,12)],
                    [S.Rational(1,12),S.Rational(1,12),S.Rational(1,30)]])
    for eid,(i,j) in enumerate(edges):
        ids=[i,j,size+eid]
        for a in range(3):
            for b in range(3):
                mat[ids[a],ids[b]]+=local[a,b]
    inverse=mat.inv()
    col=inverse[:,0]
    beta=S.Rational(12,(3*size-2)*(size-1))
    alpha=(2*size-1)*beta
    for eid,(i,j) in enumerate(edges):
        kern=S.expand(col[i]*(1-x)+col[j]*x+col[size+eid]*h)
        want=S.expand((alpha*phi+beta*psi) if i==0 else beta*(phi+psi))
        assert S.simplify(kern-want)==0, (size,(i,j),kern,want)
    # Node Gram inverse and direct Schur complement agree.
    H=S.Matrix(size,size,lambda i,j:S.Rational(size-1,8) if i==j else -S.Rational(1,24))
    Hinv=H.inv()
    for i in range(size):
        for j in range(size):
            assert Hinv[i,j] == (alpha if i==j else beta)
    # Analytic absolute integral also follows from root formula, checked numerically
    # at high precision using independent quadrature on the direct kernel.
    from mpmath import mp
    mp.dps=45
    val=(mp.mpf(str(S.N(N.subs(n,size),42))))
    # roots of incident polynomial (5m)t^2+(2-7m)t+(2m-1)
    delta=9*size*size-8*size+4
    lo=(7*size-2-mp.sqrt(delta))/(10*size)
    hi=(7*size-2+mp.sqrt(delta))/(10*size)
    qpoly=lambda t:5*size*t*t+(2-7*size)*t+(2*size-1)
    iabs=mp.quad(lambda t:abs(qpoly(t)),[0,lo,hi,1])
    rr=(5-mp.sqrt(5))/10;ss=(5+mp.sqrt(5))/10
    jabs=mp.quad(lambda t:abs(1-5*t+5*t*t),[0,rr,ss,1])
    direct=12/mp.mpf(3*size-2)*(iabs+(size-2)*jabs/2)
    assert abs(direct-val)<mp.mpf('1e-35')
    return len(edges)

count=0
for m in [3,4,5,6,7,8]:
    count+=direct_kernel_check(m)
# Proof-supporting shape-function identity, with sign ranges 0-2/5, 2/5-3/5, 3/5-1:
assert S.factor(1-(phi-psi+2*h)) == 2*x*x
assert S.simplify(1-(-phi-psi+2*h) - (2-7*x*(1-x))) == 0
assert S.simplify(1-(psi-phi+2*h)-2*(1-x)**2)==0
print('PASS: exact Gram, inverse, kernel, roots, monotonicity, limits, and',count,'independent edge kernels.')

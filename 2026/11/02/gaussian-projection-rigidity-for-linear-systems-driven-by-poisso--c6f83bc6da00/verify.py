"""Exact algebraic checks for reset-Brownian linear response (SymPy required).

The proof for general networks and infinitely many possible parameter values is
in RESULT.md; finite/symbolic consistency tests here are auxiliary.
"""
import sympy as sp

a,r,D=sp.symbols('a r D',positive=True)
M={(0,0):sp.Integer(1)}
# Generator: -a*y*d_y+x*d_y+D*d_xx+r[f(y,0)-f(y,x)].
# The recursion is triangular in (total degree, y degree).
for total in range(1,5):
    for q in range(total+1):
        p=total-q
        term=sp.Integer(0)
        if q:
            term+=q*M[p+1,q-1]
        if p>=2:
            term+=D*p*(p-1)*M[p-2,q]
        M[p,q]=sp.factor(term/(q*a+(r if p else 0)))

m2=sp.factor(M[0,2])
m4=sp.factor(M[0,4])
k4=sp.factor(m4-3*m2*m2)
assert sp.simplify(m2-2*D/(a*r*(a+r)))==0
assert sp.simplify(k4-24*D**2*(3*a+7*r)/(a*r**2*(a+r)**2*(2*a+r)*(3*a+r)))==0
assert sp.simplify(k4/m2**2-6*a*(3*a+7*r)/((2*a+r)*(3*a+r)))==0
assert (m2.subs({a:1,r:1,D:1}),m4.subs({a:1,r:1,D:1}),k4.subs({a:1,r:1,D:1}))==(1,8,5)

# Every coordinate velocity has a nonzero boundary input response.
checks=0
for n in [2,3,4,5,8]:
    eye=sp.eye(n)
    L=sp.diag(*([2]*n))
    for j in range(n-1):
        L[j,j+1]=-1
        L[j+1,j]=-1
    E=sp.zeros(n)
    E[0,0]=1
    E[n-1,n-1]=1
    for mass,k,gamma,s in [(1,1,1,1),(2,3,1,2),(3,2,4,1)]:
        resolvent=(mass*s*s*eye+gamma*s*E+k*L).inv()
        for j in range(n):
            for boundary in [0,n-1]:
                val=sp.factor(k*s*resolvent[j,boundary])
                assert val.is_positive, (n,j,boundary,val)
                checks+=1
print('PASS: stationary generator fourth cumulant, Gaussian comparison and',checks,'exact boundary-transfer positivity checks')

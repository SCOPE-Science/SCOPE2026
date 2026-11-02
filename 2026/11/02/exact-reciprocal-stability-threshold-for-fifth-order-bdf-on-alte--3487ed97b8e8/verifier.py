"""Exact symbolic replay for the alternating-step BDF5 Floquet theorem.

Requires Python 3 with sympy; numpy is optional for supplementary sampling.
No external input files are used.
"""
import sympy as S

r,z,w = S.symbols('r z w', positive=True)
D=(4*r**3+30*r**2+63*r+40)*(40*r**3+63*r**2+30*r+4)
A=304*r**6+1348*r**5+2442*r**4+2781*r**3+2442*r**2+1348*r+304
B=16*r**6+108*r**5+362*r**4+547*r**3+362*r**2+108*r+16
C=-r*(36*r**4+170*r**3+269*r**2+170*r+36)
E=4*r*(r+1)**2*(r+2)*(2*r+1)
P=4*r**6-8*r**5-83*r**4-143*r**3-83*r**2-8*r+4

def update(lengths):
    k=len(lengths)
    positions=[S.Integer(0)]
    for v in lengths: positions.append(positions[-1]+v)
    alpha=[sum(1/positions[j] for j in range(1,k+1))]
    for j in range(1,k+1):
        a=-1/positions[j]
        for l in range(1,k+1):
            if j!=l: a*=positions[l]/(positions[l]-positions[j])
        alpha.append(S.cancel(a))
    assert S.factor(sum(alpha))==0
    beta=[S.factor(sum(alpha[:j+1])) for j in range(k)]
    M=S.zeros(k-1)
    for j in range(1,k):M[0,j-1]=S.cancel(-beta[j]/beta[0])
    for j in range(1,k-1): M[j,j-1]=1
    return M

U=update([r,1,r,1,r])
V=update([1,r,1,r,1])
T=V*U
expected=[S.Integer(1),A/D,B/D,C/D,E/D]
actual=T.charpoly(z).all_coeffs()
for j,(a,b) in enumerate(zip(actual,expected)):
    assert S.cancel(a-b)==0, ('characteristic coefficient',j)
print('Exact 5-step interpolation and 2-step characteristic polynomial: PASS')

Q=S.Poly(S.expand(D*(1+w)**4+A*(1+w)**3*(1-w)+B*(1+w)**2*(1-w)**2+C*(1+w)*(1-w)**3+E*(1-w)**4), w)
q=list(reversed(Q.all_coeffs()))
qexpected=[
480*(r+1)**6,
8*(156*r**6+1068*r**5+2900*r**4+3977*r**3+2900*r**2+1068*r+156),
8*(116*r**6+1068*r**5+3334*r**4+4769*r**3+3334*r**2+1068*r+116),
16*(2*r**6+188*r**5+797*r**4+1226*r**3+797*r**2+188*r+2),
-32*P]
for j,(a,b) in enumerate(zip(q,qexpected)):
    assert S.expand(a-b)==0, ('Cayley coefficient',j)
print('Cayley transform and signed leading coefficient: PASS')

half2=[1480,29992,280120,1393254,4109082,7683087,9431320]
half3=[230400,6166272,74849696,543723184,2642541168,9125913628,23234325050,44646921618,65712229619,74682902480]

def symmetric_poly(half):
    n=2*(len(half)-1)
    v=half+half[-2::-1]
    assert len(v)==n+1
    return sum(v[j]*r**j for j in range(n+1))

H2=S.expand(q[3]*q[2]-q[4]*q[1])
H3=S.expand(q[3]*q[2]*q[1]-q[3]**2*q[0]-q[4]*q[1]**2)
assert S.expand(H2-128*symmetric_poly(half2))==0
assert S.expand(H3-1024*symmetric_poly(half3))==0
assert all(x>0 for x in half2+half3)
print('Two strictly positive Hurwitz-determinant certificates: PASS')

v=S.symbols('v')
g=4*v**3-8*v**2-95*v-127
assert S.cancel(P-r**3*g.subs(v,r+1/r))==0
assert S.sign(g.subs(v,2))==-1
assert S.Poly(g,v).count_roots(2,S.oo)==1
beta=S.nroots(g, maxsteps=100)
root=float([x for x in beta if abs(S.im(x))<1e-12 and S.re(x)>2][0])
th=(root+(root**2-4)**.5)/2
print('Exact unique reciprocal thresholds: PASS')
print('large critical ratio:',format(th,'.15f'),'small critical ratio:',format(1/th,'.15f'))

try:
    import numpy as np
    for x in [.01,.1,.2,.5,1.,2.,5.,10.,100.]:
        vals=np.roots([1.]+[float(y.subs(r,x).evalf()) for y in expected[1:]])
        k=int(np.sum(np.abs(vals)>1+1.e-8))
        predicted=int(x<th**-1 or x>th)
        assert k==predicted,('numeric sample',x,vals)
    print('Nine supplementary root-count samples: PASS')
except ImportError:
    print('Numpy absent; optional supplementary samples skipped')
print('ALL EXACT CHECKS PASSED')

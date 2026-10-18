"""Exact and numerical checks for two-row Kaczmarz momentum-rate results.

Requires sympy and numpy. Proof is given in RESULT.md; these checks independently
construct the covariance map and verify the nontrivial algebra used in that proof.
"""
import sympy as sp
import numpy as np

checks = 0

def check(cond, label):
    global checks
    if not bool(cond):
        raise AssertionError(label)
    checks += 1

c, m = sp.symbols('c m')
q, r = (1-c)/2, (1+c)/2
t2 = q*r
L0 = sp.factor(q*q+r*r)

# Reflection-even covariance coordinates: (S_ee11, S_ee22,
# S_ey11, S_ey22, S_yy11, S_yy22).
E = sp.Matrix([
    [q*q,t2,2*m*q,0,m*m,0],
    [t2,r*r,0,2*m*r,0,m*m],
    [q*q-q,t2,-m*c,0,m*m,0],
    [t2,r*r-r,0,m*c,0,m*m],
    [r*r,t2,-2*m*r,0,m*m,0],
    [t2,q*q,0,-2*m*q,0,m*m]])
# Reflection-odd coordinates: (S_ee12,S_ey12,S_ey21,S_yy12).
O = sp.Matrix([
    [2*t2,m*q,m*r,m*m],
    [2*t2-q,m*q,-m*q,m*m],
    [2*t2-r,-m*r,m*r,m*m],
    [2*t2,-m*r,-m*q,m*m]])

# Compare formulas to the full, directly constructed 4x4 stochastic state
# transition on a rational nonorthogonal pair of rows, c=3/5.
cv,mv=sp.Rational(3,5),sp.Rational(1,10)
qq,rr,tt=sp.Rational(1,5),sp.Rational(4,5),sp.Rational(2,5)
I=sp.eye(2)
transitions=[]
for sign in (1,-1):
    Q=sp.Matrix([[qq,sign*tt],[sign*tt,rr]])
    P=I-Q
    transitions.append(Q.row_join(mv*I).col_join((-P).row_join(mv*I)))

def advance(S):
    return sp.expand((transitions[0]*S*transitions[0].T+transitions[1]*S*transitions[1].T)/2)

def symmetric_basis(i,j):
    Z=sp.zeros(4)
    Z[i,j]=1; Z[j,i]=1
    return Z

even_bases=[symmetric_basis(0,0),symmetric_basis(1,1),
            symmetric_basis(0,2),symmetric_basis(1,3),
            symmetric_basis(2,2),symmetric_basis(3,3)]
odd_bases=[symmetric_basis(0,1),symmetric_basis(0,3),
           symmetric_basis(1,2),symmetric_basis(2,3)]
even_idx=[(0,0),(1,1),(0,2),(1,3),(2,2),(3,3)]
odd_idx=[(0,1),(0,3),(1,2),(2,3)]
for block,bases,idx in ((E,even_bases,even_idx),(O,odd_bases,odd_idx)):
    B=block.subs({c:cv,m:mv})
    for j,S in enumerate(bases):
        Y=advance(S)
        for i,(a,b) in enumerate(idx):
            check(sp.simplify(Y[a,b]-B[i,j])==0,'covariance matrix entry')
        for a in range(4):
            for b in range(a,4):
                if (a,b) not in idx:
                    check(Y[a,b]==0,'reflection symmetry')

# Verify exact M=0 spectra and derivative of the simple dominant eigenvalue.
lam=sp.symbols('lam')
PE=E.charpoly(lam).as_expr()
PO=O.charpoly(lam).as_expr()
check(sp.factor(PE.subs(m,0) - lam**5*(lam-L0))==0,'even zero-M polynomial')
check(sp.factor(PO.subs(m,0) - lam**3*(lam-2*t2))==0,'odd zero-M polynomial')
a=sp.factor(-sp.diff(PE,m).subs({m:0,lam:L0})/sp.diff(PE,lam).subs({m:0,lam:L0}))
a_target=-2*c*c*(1-c*c)/(1+c*c)**2
check(sp.factor(a-a_target)==0,'mean-square derivative')
Bterm=(sp.diff(PE,m,2)/2+sp.diff(PE,m,lam)*a+sp.diff(PE,lam,2)*a*a/2)
b=sp.factor(-Bterm.subs({m:0,lam:L0})/sp.diff(PE,lam).subs({m:0,lam:L0}))
check(b.subs(c,0)==1,'second Taylor coefficient')
check(sp.limit(a/c**2,c,0)==-2,'small-coherence derivative')
check(sp.limit((b-1)/c,c,0)==0,'evenness of quadratic term')

# A complete scalar moment recurrence at c=0 (unsmoothed momentum).
R=sp.Matrix([[sp.Rational(1,2)+m+m*m,-m-2*m*m,m*m],
             [sp.Rational(1,2)+m,-m,0],[1,0,0]])
PR=R.charpoly(lam).as_expr()
check(sp.factor(PR-(lam**3-(sp.Rational(1,2)+m*m)*lam**2+m**3*lam-m**3))==0,
      'orthogonal cubic')
check(sp.factor(PR.subs(lam,sp.Rational(1,2))+m*m*(2*m+1)/4)==0,
      'orthogonal strict slowdown sign')

# Rational direct-update moment propagation, starting at e=(1,2), y=(0,0).
z=sp.Matrix([1,2,0,0]); S=z*z.T
EE=E.subs({c:cv,m:mv}); OO=O.subs({c:cv,m:mv})
ve=sp.Matrix([S[i,j] for i,j in even_idx]); vo=sp.Matrix([S[i,j] for i,j in odd_idx])
for k in range(15):
    check(sp.simplify((S[0,0]+S[1,1])-(ve[0]+ve[1]))==0,
          'exact error second moment')
    S=advance(S); ve=EE*ve; vo=OO*vo
    for i,(a0,b0) in enumerate(even_idx):
        check(sp.simplify(S[a0,b0]-ve[i])==0,'even finite iterate')
    for i,(a0,b0) in enumerate(odd_idx):
        check(sp.simplify(S[a0,b0]-vo[i])==0,'odd finite iterate')

# Numerical checks of the branch and its asymptotic near-orthogonal law.
def spectrum(coh,mom):
    e=np.array(E.subs({c:coh,m:mom}),dtype=float)
    o=np.array(O.subs({c:coh,m:mom}),dtype=float)
    return max(np.max(np.abs(np.linalg.eigvals(e))),np.max(np.abs(np.linalg.eigvals(o))))
for coh in [0.5,0.6,0.8]:
    base=(1+coh*coh)/2
    h=1e-6
    got=(spectrum(coh,h)-base)/h
    theory=float(a_target.subs(c,coh))
    check(abs(got-theory)<5e-5,'numerical first variation')
    check(spectrum(coh,h)<base,'strict nonorthogonal improvement')
for coh in [.1,.05,.02]:
    base=(1+coh*coh)/2
    value=spectrum(coh,coh*coh)
    check(value<base,'positive weak-coherence gain')
    check(abs((base-value)/coh**4-1)<8*coh**2,'sharp gain coefficient')
print('PASS:',checks,'checks; exact covariance construction, spectral derivatives and finite-step moments')

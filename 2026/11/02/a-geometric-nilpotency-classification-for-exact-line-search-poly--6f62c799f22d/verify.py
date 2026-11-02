"""Standalone exact-arithmetic checks for the triangular vertex-sweep theorem.

Run: python verify.py
Requires: sympy >= 1.12; Python >= 3.10.
These checks supplement, but do not replace, the analytic proof in RESULT.md.
"""
from itertools import permutations
import random
import sympy as S

Q = S.Rational
I = S.eye(2)
verts = [S.Matrix(x) for x in [(0, 0), (2, 0), (0, 2)]]
target = S.Matrix([Q(2,5), Q(4,5)])
H = S.eye(2)

def proj(n, metric):
    return S.eye(2) - n * (n.T * metric) / (n.T * metric * n)[0]

def inner(a,b,metric):
    return (a.T*metric*b)[0]

def sweep_jac(v,t,metric,order):
    n = [w-t for w in v]
    P = [proj(w,metric) for w in n]
    J = S.eye(2)
    for i in order: J = P[i]*J
    return J, n, P

def step_unconstrained(x,v,t,metric):
    d = v-x
    return x - inner(x-t,d,metric)/inner(d,d,metric)*d

def exact_clipped_step(x,v,index,vertices,t,metric):
    # Barycentric weights for this exact triangle; this routine tests the
    # actual source's feasible line-search interval, not a surrogate step.
    w2 = x[0]/2; w3=x[1]/2; w1=1-w2-w3
    lam=[w1,w2,w3][index]
    assert 0 < lam < 1
    d=v-x
    alpha=-inner(x-t,d,metric)/inner(d,d,metric)
    gamma=lam/(1-lam)
    alpha=max(-gamma,min(S.Integer(1),alpha))
    return x+alpha*d,alpha

def formal_quadratic_coefficients(order, hdir):
    eps = S.symbols('eps')
    x = target + eps*S.Matrix(hdir)
    for i in order:
        x = step_unconstrained(x, verts[i], target, H)
        x = x.applyfunc(S.cancel)
    return S.Matrix([S.factor(S.diff(z,eps).subs(eps,0)) for z in x]), S.Matrix([S.factor(S.diff(z,eps,2).subs(eps,0)/2) for z in x])

checks=0
Jf,n,P=sweep_jac(verts,target,H,(0,1,2))
Jr,_,_=sweep_jac(verts,target,H,(0,2,1))
assert Jf==S.zeros(2)
assert Jr==S.Matrix([[Q(1,5),-Q(1,10)],[Q(2,5),-Q(1,5)]])
assert Jr!=S.zeros(2) and Jr*Jr==S.zeros(2)
assert inner(n[0],n[1],H)==0
assert inner(n[0],n[2],H)!=0 and inner(n[1],n[2],H)!=0
checks+=6
for p in P:
    assert p*p==p and p.T==p
    checks+=2

lin_f,q_f=formal_quadratic_coefficients((0,1,2),(1,0))
lin_r,q_r=formal_quadratic_coefficients((0,2,1),(1,0))
assert lin_f==S.zeros(2,1) and q_f==S.Matrix([-Q(3,5),-Q(1,5)])
assert lin_r==Jr*S.Matrix([1,0]) and q_r==S.Matrix([-Q(3,20),-Q(11,20)])
checks+=4
_,q_r_2=formal_quadratic_coefficients((0,2,1),(0,1))
_,q_r_12=formal_quadratic_coefficients((0,2,1),(1,1))
vec=Jr*S.Matrix([1,0]); cross=q_r_12-q_r-q_r_2
quad_Jvec=vec[0]**2*q_r+vec[1]**2*q_r_2+vec[0]*vec[1]*cross
q_r_twosweep=Jr*q_r+quad_Jvec
assert q_r_twosweep==S.Matrix([Q(1,40),Q(1,20)])
checks+=1

# The actual line-search algorithm, including feasible away-step bounds,
# agrees with the local analytic expansion at sufficiently small inputs.
for nstep in [50,100,500,1000]:
    x0=target+S.Matrix([Q(1,nstep),0])
    for order in [(0,1,2),(0,2,1)]:
        actual=x0
        unclip=x0
        for i in order:
            actual,_=exact_clipped_step(actual,verts[i],i,verts,target,H)
            unclip=step_unconstrained(unclip,verts[i],target,H)
            assert actual==unclip
            checks+=1
checks+=24

# Reproducible exact random metric and triangle trials, testing the
# universal rank-one identity and permutation invariance algebraically.
rng=random.Random(171763)
for _ in range(100):
    vs=[S.Matrix([Q(rng.randint(-8,8),5),Q(rng.randint(-8,8),5)]) for _ in range(3)]
    det=S.det(S.Matrix.hstack(vs[1]-vs[0],vs[2]-vs[0]))
    if det==0: continue
    a,b,c=[rng.randint(1,9) for _ in range(3)]
    metric=S.Matrix([[a*a+b*b,b*c],[b*c,c*c+2]])
    if metric.det()<=0: continue
    lam=[Q(1,5),Q(1,3),Q(7,15)]
    t=sum((lam[j]*vs[j] for j in range(3)),S.zeros(2,1))
    n0=[v-t for v in vs]
    D=[inner(v,v,metric) for v in n0]
    ds=[inner(n0[0],n0[1],metric),inner(n0[1],n0[2],metric),inner(n0[2],n0[0],metric)]
    lam_formula=S.cancel(ds[0]*ds[1]*ds[2]/(D[0]*D[1]*D[2]))
    for order in permutations(range(3)):
        J,_,_=sweep_jac(vs,t,metric,order)
        assert S.simplify(J.trace()-lam_formula)==0
        assert S.simplify(J.det())==0
        assert all(S.simplify(v)==0 for v in (J*J-lam_formula*J))
        checks+=3

# Compare the one-sided vanilla PolyCD direction: its second step is clipped.
eps=S.symbols('eps',positive=True)
e1=S.Matrix([1,0])
assert P[1]*P[0]==S.zeros(2)
assert P[2]*P[0]*e1==S.Matrix([Q(3,5),Q(1,5)])
checks+=2

# A direct execution of the source's clipped interval updates verifies that
# the two-sweep coefficient is observable in actual feasible iterations.
for denominator in [50,100,300]:
    eps0=Q(1,denominator)
    x0=target+eps0*S.Matrix([1,0])
    for order,wanted in [((0,1,2),S.Matrix([-Q(3,5),-Q(1,5)])),
                         ((0,2,1),S.Matrix([Q(1,40),Q(1,20)]))]:
        x=x0
        repetitions=1 if order==(0,1,2) else 2
        for _ in range(repetitions):
            for idx in order:
                x,_=exact_clipped_step(x,verts[idx],idx,verts,target,H)
        observed=(x-target)/eps0**2
        assert max(abs(float(v)) for v in observed-wanted)<4*float(eps0)
        checks+=1

# Vanilla PolyCD disallows away steps. Its second local update is clipped at
# zero in the indicated direction, leaving a nonzero first-order error.
for denominator in [100,500,1000]:
    eps0=Q(1,denominator)
    x=target+eps0*S.Matrix([1,0])
    statuses=[]
    for idx in (0,1,2):
        d=verts[idx]-x
        uncon=-inner(x-target,d,H)/inner(d,d,H)
        alpha=max(S.Integer(0),min(S.Integer(1),uncon))
        statuses.append(alpha==0)
        x=x+alpha*d
    assert statuses==[False,True,False]
    predicted=S.Matrix([Q(3,5),Q(1,5)])
    assert max(abs(float(v)) for v in (x-target)/eps0-predicted)<4*float(eps0)
    checks+=1

print('PASS',checks,'exact symbolic/rational checks. Analytic proof required for all geometric statements.')

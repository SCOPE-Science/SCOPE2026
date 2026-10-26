"""Reproducible finite checks for exact diagonal RMSProp two-cycle formulas.
These checks are diagnostic, not proofs of universal statements.
"""
import math
import itertools

def F(x,v,a,h,eps,beta):
    vn=beta*v+(1-beta)*(a*x)**2
    return (x-h*a*x/(math.sqrt(vn)+eps),vn)

def jac(x,v,a,h,eps,beta):
    vn=beta*v+(1-beta)*(a*x)**2
    u=math.sqrt(vn); den=u+eps
    vx=2*(1-beta)*a*a*x
    vv=beta
    ux=vx/(2*u)
    uv=vv/(2*u)
    return [[1-h*a/den+h*a*x*ux/(den*den),h*a*x*uv/(den*den)],[vx,vv]]

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def rho_from_trace(s,beta):
    discriminant=s*s-4*beta
    if discriminant<=0:
        return beta
    z=(abs(s)+math.sqrt(discriminant))/2
    return z*z

count=0
for beta in (.01,.0625,.15,.5,.9):
    for q in (1.03,1.2,1.45,2,4,5.8,12,50):
        a,eps=1.7,.9
        h=2*eps*q/a
        r=h/2-eps/a
        p,w=F(r,a*a*r*r,a,h,eps,beta)
        p2,w2=F(p,w,a,h,eps,beta)
        assert abs(p+r)<1e-10 and abs(p2-r)<1e-10
        assert abs(w-a*a*r*r)<1e-10 and abs(w2-w)<1e-10
        Jp=jac(r,w,a,h,eps,beta)
        Jm=jac(-r,w,a,h,eps,beta)
        R=mul(Jm,Jp)
        trace=R[0][0]+R[1][1]
        det=R[0][0]*R[1][1]-R[0][1]*R[1][0]
        s=-1+3*beta+2*(1-beta)/q
        assert abs(trace-(s*s-2*beta))<2e-11,(q,beta,trace,s*s-2*beta)
        assert abs(det-beta*beta)<2e-11
        assert rho_from_trace(s,beta)<1
        count+=1
print('EXACT_SCALAR_TWO_STEP_JACOBIAN_AND_SCHUR_PASS',count)

for active in range(1,6):
    states=[]
    for pattern in itertools.product((-1,0,1), repeat=active):
        if any(pattern) and next(u for u in pattern if u)!=-1:
            states.append(pattern)
    assert len(states)==(3**active-1)//2
    stable=[v for v in states if all(u for u in v)]
    assert len(stable)==2**(active-1)
    print('PRODUCT_ORBIT_CENSUS_PASS',active,len(states),len(stable))

beta=1/16
qm=2*(1-beta)/(1-3*beta+2*math.sqrt(beta))
qp=2*(1-beta)/(1-3*beta-2*math.sqrt(beta))
assert abs(qm-10/7)<1e-12 and abs(qp-6)<1e-12
for qs,expect in [([1.45,2.9,5.8],True),([1.2,6.5],False)]:
    isoptimal=all(qm-1e-12<=q<=qp+1e-12 for q in qs)
    assert isoptimal==expect
    assert (max(rho_from_trace(-1+3*beta+2*(1-beta)/q,beta) for q in qs)<=beta+1e-12)==expect
print('SHARP_MEMORY_PLATEAU_AND_CONDITION_RATIO_PASS',qm,qp,qp/qm)
print('UNIVERSAL_CLASSIFICATION_AND_ROBUSTNESS_REQUIRE_ANALYTIC_PROOF')

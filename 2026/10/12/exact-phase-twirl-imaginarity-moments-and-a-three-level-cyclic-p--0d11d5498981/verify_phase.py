"""Finite consistency checks for the phase-twirl imaginarity moments."""
import cmath
import itertools
import math


def analytic(rho):
    d = len(rho)
    P = sum(abs(rho[i][j]) ** 2 for i in range(d) for j in range(d))
    D = sum(abs(rho[i][i]) ** 2 for i in range(d))
    mean = (1 + D/P)/2
    var = sum(abs(rho[i][j])**4 for i in range(d) for j in range(i+1,d))/(2*P**2)
    cubic = 3*sum((rho[i][j]**2*rho[j][k]**2*rho[k][i]**2).real
                  for i in range(d) for j in range(i+1,d) for k in range(j+1,d))/(2*P**3)
    return mean, var, cubic


def direct_moments(rho, q=7):
    d=len(rho)
    P=sum(abs(rho[i][j])**2 for i in range(d) for j in range(d))
    moments=[0.0]*3
    for phases in itertools.product(range(q),repeat=d):
        z=[cmath.exp(2j*math.pi*k/q) for k in phases]
        # D rho D^*: values are phase-conjugated, R is their squared-entry sum.
        R=sum((z[i]*rho[i][j]*z[j].conjugate())**2
              for i in range(d) for j in range(d)).real
        value=(1+R/P)/2
        for k in range(3):moments[k] += value**(k+1)/(q**d)
    mu=moments[0]
    return mu, moments[1]-mu*mu, moments[2]-3*mu*moments[1]+2*mu**3


def verify_edge_balances(d):
    edges=[(i,j) for i in range(d) for j in range(d) if i!=j]
    two={}
    three={}
    for sequence in itertools.product(edges,repeat=3):
        degree=[0]*d
        for i,j in sequence:
            degree[i]+=1;degree[j]-=1
        if any(degree):continue
        support=tuple(sorted({tuple(sorted(e)) for e in sequence}))
        three[support]=three.get(support,0)+1
    assert len(three)==math.comb(d,3)
    assert set(three.values())=={12}
    for e,f in itertools.product(edges,repeat=2):
        degree=[0]*d
        for i,j in (e,f):degree[i]+=1;degree[j]-=1
        if degree==[0]*d:
            support=tuple(sorted(e))
            two[support]=two.get(support,0)+1
    assert len(two)==math.comb(d,2)
    assert set(two.values())=={2}
    return sum(two.values()),sum(three.values())


def make_qutrit(phase, eps=0.08):
    r=[[0j]*3 for _ in range(3)]
    for i in range(3): r[i][i]=1/3
    r[0][1]=r[1][0]=eps
    r[1][2]=r[2][1]=eps
    r[2][0]=eps*phase
    r[0][2]=eps*phase.conjugate()
    return r

if __name__=='__main__':
    counts=[verify_edge_balances(d) for d in range(3,6)]
    vals=[]
    for phase in (1+0j,1j):
        rho=make_qutrit(phase)
        aa=analytic(rho)
        bb=direct_moments(rho,7)
        for a,b in zip(aa,bb):
            assert abs(a-b)<2e-12,(a,b)
        vals.append(aa)
    assert abs(vals[0][0]-vals[1][0])<1e-13
    assert abs(vals[0][1]-vals[1][1])<1e-13
    assert vals[0][2]>0 and vals[1][2]<0
    assert abs(vals[0][2]+vals[1][2])<1e-14
    print('VERIFY_OK', 'oriented_edge_counts',counts,
          'qutrit_7_phase_assignments',2*7**3,
          'opposite_skewness',vals[0][2],vals[1][2])

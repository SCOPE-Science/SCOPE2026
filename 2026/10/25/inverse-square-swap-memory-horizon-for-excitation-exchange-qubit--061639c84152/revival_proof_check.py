"""Reproduce selected checks for a two-qubit partial-reset collision model.

Run: python3 revival_proof_check.py. Uses only Python's standard library.
Finite tests corroborate, but do not establish, the asymptotic theorem.
"""
import math


def matrix(lam, eps):
    c, s = math.sqrt(eps), math.sqrt(1-eps)
    return ((eps, 1-eps, -2*c*s),
            (lam*(1-eps), lam*eps, 2*lam*c*s),
            (lam*c*s, -lam*c*s, lam*(2*eps-1)))


def mv(a, v):
    return tuple(sum(a[i][j]*v[j] for j in range(3)) for i in range(3))


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def adj(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def run_direct(lam, eps, length):
    c,s=math.sqrt(eps),math.sqrt(1-eps)
    u=[[0j]*4 for _ in range(4)]
    for i in (0,3):u[i][i]=1.0
    u[1][1]=c;u[2][2]=c;u[1][2]=-1j*s;u[2][1]=-1j*s
    rho=[[0j]*4 for _ in range(4)];rho[2][2]=1.0
    results=[]
    for step in range(length):
        rho=mm(mm(u,rho),adj(u))
        results.append(float((rho[2][2]+rho[3][3]).real))
        partial=[[sum(rho[2*a+e][2*b+e] for e in range(2)) for b in range(2)] for a in range(2)]
        rho=[[(lam*rho[i][j]+(1-lam)*partial[i//2][j//2]
              if i%2==j%2==0 else lam*rho[i][j])
              for j in range(4)] for i in range(4)]
    return results


def coefficient(lam):
    u=math.sqrt(lam)
    return u*(1-u*u)*math.log((1+u)/(1-u))/(2*(1+6*u*u+u**4))


def finite_reviving_steps(lam, eps, steps):
    t=matrix(lam,eps)
    v=(1.,0.,0.);count=0;locations=[]
    for n in range(steps):
        nxt=mv(t,v)
        if nxt[0]>v[0]: count+=1;locations.append(n)
        v=nxt
    return count,locations


def main():
    checks=0
    for lam in (0.1,0.25,0.5,0.75):
        for eps in (0.01,0.04,0.15,0.4,0.9):
            p=1.;vec=(1.,0.,0.)
            direct=run_direct(lam,eps,35)
            for q in direct:
                vec=mv(matrix(lam,eps),vec)
                assert abs(vec[0]-q)<5e-12, (lam,eps,vec[0],q)
                assert -1e-12<=vec[0]<=1+1e-12
                checks+=2
            # Exact two-collision polynomial, from the update matrix.
            expected=lam - 4*eps*lam + eps*eps*(3*lam+1)
            vec=mv(matrix(lam,eps),mv(matrix(lam,eps),(1.,0.,0.)))
            assert abs(vec[0]-expected)<2e-14
            checks+=1
    for lam in (0.1,0.25,0.5):
        for eps in (0.002,0.001):
            expected=coefficient(lam)
            count,loc=finite_reviving_steps(lam,eps,2000)
            assert abs(eps*count-expected)<0.008, (lam,eps,count,expected)
            assert all(n%2==1 for n in loc),loc
            checks+=2
    print('PASS',checks,'checks (direct joint CPTP vs reduced recurrence; near-SWAP counting).')
    for lam in (0.1,0.25,0.5):
        eps=.001
        count,_=finite_reviving_steps(lam,eps,2000)
        print('retention',lam,'epsilon',eps,'revivals',count,
              'epsilon*revivals',eps*count,'limit',coefficient(lam))

if __name__=='__main__':main()

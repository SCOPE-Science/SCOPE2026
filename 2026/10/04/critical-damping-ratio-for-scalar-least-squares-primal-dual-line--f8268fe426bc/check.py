#!/usr/bin/env python3
import cmath, math

def roots(a, r, sigma):
    tau = r/(sigma*a*a)
    M = (
        ((1+sigma-r)/(1+sigma), -tau*a*(1-r)/(1+sigma)),
        (sigma*a/(1+sigma), (1-r)/(1+sigma)),
    )
    T = M[0][0] + M[1][1]
    D = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    disc = T*T - 4*D
    h = cmath.sqrt(disc)
    l1 = (T+h)/2
    l2 = (T-h)/2
    return M,T,D,l1,l2

for a in (0.5, 1.0, 3.0):
    for r in (0.05, 0.2, 0.5, 0.8, 0.95):
        sc = 2*math.sqrt(r*(1-r))
        beta = 4*a*a*(1-r)
        tau = sc/beta
        assert abs(tau*sc*a*a-r) < 2e-14
        M,T,D,l1,l2 = roots(a,r,sc)
        assert abs(T-(2+sc-2*r)/(1+sc)) < 2e-14
        assert abs(D-(1-r)/(1+sc)) < 2e-14
        rho_star = math.sqrt(1-r)/(math.sqrt(r)+math.sqrt(1-r))
        assert abs(abs(l1)-rho_star) < 2e-8
        assert abs(abs(l2)-rho_star) < 2e-8
        # Strict decrease before and strict increase after the coalescence.
        left=[]
        for fac in (0.2,0.4,0.6,0.8,0.99):
            _,_,_,u,v=roots(a,r,fac*sc)
            left.append(max(abs(u),abs(v)))
        assert all(left[i] > left[i+1] for i in range(len(left)-1))
        right=[]
        for fac in (1.01,1.2,1.5,2.0,4.0):
            _,_,_,u,v=roots(a,r,fac*sc)
            right.append(max(abs(u),abs(v)))
        assert all(right[i] < right[i+1] for i in range(len(right)-1))
print("VERIFY_OK")

#!/usr/bin/env python3
"""Deterministic diagnostics for Cartan automorphisms and 2x2 triangular criteria.
Run: python checks/cartans_two_level.py (requires numpy, scipy).
Not a proof of the infinite-function-class claim.
"""
import numpy as np
from scipy.linalg import fractional_matrix_power

def test():
    g = np.random.default_rng(26102026)
    count = 0
    for p,q in ((2,2),(2,3),(3,2),(1,3),(3,1)):
        for _ in range(40):
            B = g.normal(size=(p,q)) + 1j*g.normal(size=(p,q))
            B *= 0.55/np.linalg.norm(B,2)
            Z = g.normal(size=(p,q)) + 1j*g.normal(size=(p,q))
            Z *= 0.85/np.linalg.norm(Z,2)
            Db = fractional_matrix_power(np.eye(p)-B@B.conj().T,0.5)
            Da = fractional_matrix_power(np.eye(q)-B.conj().T@B,0.5)
            Phi = np.linalg.solve(Db,(Z-B)@np.linalg.inv(np.eye(q)-B.conj().T@Z)@Da)
            RHS = Db@np.linalg.inv(np.eye(p)-Z@B.conj().T)@(np.eye(p)-Z@Z.conj().T)@np.linalg.inv(np.eye(p)-B@Z.conj().T)@Db
            assert np.linalg.norm(np.eye(p)-Phi@Phi.conj().T-RHS,2)<5e-10
            assert np.linalg.norm(Phi,2)<1
            count+=2
    for _ in range(200):
        rho=float(g.uniform(0.02,0.95))
        c=complex(g.normal(),g.normal())
        c*=0.7*np.sqrt(max(0,1/rho**2-1))/(abs(c)+1e-15)
        b=complex(g.normal(),g.normal());b*=.8/(max(1,abs(b)))
        # A disk automorphism maps 0 to b and rho to a.
        a=(b+rho)/(1+np.conj(b)*rho)
        M=np.array([[a,c*(a-b)],[0,b]],dtype=complex)
        assert np.linalg.norm(M,2) <= 1+1e-11
        d=abs((a-b)/(1-np.conj(b)*a))
        assert d<=rho+1e-11
        count+=2
    for _ in range(100):
        a=complex(g.normal(),g.normal());a*=.7/max(1,abs(a))
        w=complex(g.normal(),g.normal());w*=0.8*(1-abs(a)**2)/(abs(w)+1e-15)
        M=np.array([[a,w],[0,a]],dtype=complex)
        assert np.linalg.norm(M,2)<=1+1e-11
        count+=1
    print(f'PASS: {count} deterministic finite assertions')
if __name__=='__main__':test()

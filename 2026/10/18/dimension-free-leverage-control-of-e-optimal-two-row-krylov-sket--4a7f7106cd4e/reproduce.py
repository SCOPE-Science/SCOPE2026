#!/usr/bin/env python3
"""Finite checks for a two-row E-optimality versus distortion theorem.

Requires Python 3 with NumPy and SymPy. Infinite claims are proved separately.
"""
import itertools
import math
import numpy as np
import sympy as sp


def exact_frame(n):
    assert isinstance(n, int) and n >= 5
    u = sp.zeros(n, 1)
    v = sp.zeros(n, 1)
    u[0] = sp.sqrt(n) / sp.sqrt(n + 1)
    u[2] = 1 / sp.sqrt(n + 1)
    v[1] = 2 / sp.sqrt(n + 1)
    for i in range(3, n):
        v[i] = 1 / sp.sqrt(n + 1)
    return u.row_join(v)


def symbolic_family_checks():
    count = 0
    for n in range(5, 16):
        Q = exact_frame(n)
        assert sp.simplify(Q.T * Q) == sp.eye(2)
        count += 1
        all_smins = []
        all_kappas = []
        for i, j in itertools.combinations(range(n), 2):
            sub = Q.extract([i,j],[0,1])
            gram = sp.simplify(sub.T * sub)
            eigs = sorted((sp.simplify(t) for t,m in gram.eigenvals().items() for _ in range(m)), key=lambda t: float(t))
            if eigs[0] == 0:
                continue
            smin2 = eigs[0]
            kap2 = sp.simplify(eigs[1]/eigs[0])
            all_smins.append((float(smin2),i,j))
            all_kappas.append((float(kap2),i,j))
            count += 1
        top = sorted(all_smins,reverse=True)
        assert top[0][1:] == (0, 1) and top[0][0] > top[1][0]
        assert sp.simplify(Q.extract([0,1],[0,1]).T*Q.extract([0,1],[0,1]) - sp.diag(n,4)/(n+1)) == sp.zeros(2)
        assert abs(min(k[0] for k in all_kappas)-1) < 1e-12
        assert abs((n/4)**.5 - (sp.sqrt(n)/2).evalf()) < 1e-12
        # Two-step symmetric Krylov realization.
        u,v=Q[:,0],Q[:,1]
        A=u*v.T+v*u.T+2*(sp.eye(n)-Q*Q.T)
        assert sp.simplify(A-A.T)==sp.zeros(n)
        assert sp.simplify(A*u-v)==sp.zeros(n,1)
        assert sp.simplify(A*v-u)==sp.zeros(n,1)
        assert sp.simplify(A*Q-Q*sp.Matrix([[0,1],[1,0]]))==sp.zeros(n,2)
        count += 4
    return count


def leverage_bound_checks():
    rng=np.random.default_rng(32152)
    count=0
    for n in range(5, 16):
        for trial in range(120):
            V,_=np.linalg.qr(rng.normal(size=(n,2)),mode='reduced')
            rowsq=np.sum(V**2,axis=1)
            rho=max(rowsq)/min(rowsq)
            pairs=[]
            for i,j in itertools.combinations(range(n),2):
                sv=np.linalg.svd(V[[i,j],:],compute_uv=False)
                if sv[-1] < 1.e-11: continue
                pairs.append((sv[-1],sv[0]/sv[-1]))
            ssmax=max(x[0] for x in pairs)
            kappamin=min(x[1] for x in pairs)
            ekappamin=min(x[1] for x in pairs if x[0]>=ssmax-1e-12)
            assert ekappamin**2 <= rho*(kappamin*kappamin+1)-1 + 1e-7
            assert ekappamin/kappamin <= math.sqrt(2*rho-1)+1e-8
            count += 1
    return count

if __name__ == '__main__':
    c1=symbolic_family_checks()
    c2=leverage_bound_checks()
    print('PASS',c1,'symbolic family and Krylov checks;',c2,'random-frame bound checks')

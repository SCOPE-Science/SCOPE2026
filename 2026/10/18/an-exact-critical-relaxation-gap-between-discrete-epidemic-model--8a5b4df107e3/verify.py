"""Standalone checks for exact critical SIS relaxation coefficients.

Only standard-library operations are used. The finite computations corroborate
an analytical asymptotic argument, and are not substitutes for that proof.
"""
import math


def trajectory(edges, rho, v, delta, initial, steps=100000):
    n = len(v)
    beta = delta / rho
    norm = sum(x*x for x in v)
    w = [x/norm for x in v]
    s = sum(w[i]*v[i]*v[i] for i in range(n))
    e2 = sum(w[i]*sum(v[j]*v[k] for j in edges[i] for k in edges[i] if j < k) for i in range(n))
    coeff_wir = delta*(1-delta)*s + beta*beta*e2
    coeff_wor = delta*s + beta*beta*e2
    assert abs((coeff_wor-coeff_wir)-delta*delta*s) < 1e-12
    out = []
    for reinfect, kappa in ((True,coeff_wir),(False,coeff_wor)):
        x = initial[:]
        for _ in range(steps):
            q = [1-math.prod(1-beta*x[j] for j in neighbors) for neighbors in edges]
            if reinfect:
                x = [(1-delta)*x[i] + (1-(1-delta)*x[i])*q[i] for i in range(n)]
            else:
                x = [(1-delta)*x[i] + (1-x[i])*q[i] for i in range(n)]
            assert all(-1e-12<=a<=1+1e-12 for a in x)
        actual = [steps*xi for xi in x]
        expected = [vi/kappa for vi in v]
        max_rel = max(abs(a-b)/b for a,b in zip(actual,expected))
        assert max_rel < 0.004, (reinfect, actual, expected, max_rel)
        out.append((reinfect,kappa,max_rel))
    print('network',n,'delta',delta,'WIR/WOR kappa and largest relative errors',out)


def checks():
    trajectory([[1],[0]],1.0,[1.,1.],0.4,[0.3,0.65])
    trajectory([[1,2],[0,2],[0,1]],2.0,[1.,1.,1.],0.6,[0.5,0.3,0.2])
    trajectory([[1],[0,2],[1]],math.sqrt(2),[1.,math.sqrt(2),1.],0.4,[0.15,0.4,0.55])
    # Exceptional endpoint: K2 WIR is a swap, WOR a scalar logistic recurrence.
    p = [0.2, 0.7]
    q = p[:]
    for step in range(100):
        q = [q[1],q[0]]
        assert q == ([0.7,0.2] if step % 2==0 else p)
    x=0.3
    for _ in range(100000):
        x = x*(1-x)
    assert abs(100000*x-1) < 0.001
    # Exact homogeneous second-order coefficients for regular graphs.
    for degree in (1,2,3,7):
        d=0.4
        pair=d*d*(degree-1)/(2*degree)
        assert abs(d*(1-d)+pair-(d-d*d*(degree+1)/(2*degree)))<1e-13
        assert abs(d+pair-(d+d*d*(degree-1)/(2*degree)))<1e-13
    print('All verification checks passed')

if __name__ == '__main__':
    checks()

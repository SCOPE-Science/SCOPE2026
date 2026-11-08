"""Exact-rational checks for Gaussian tree-recombination depth formulas."""
from fractions import Fraction as F


def merge(left, right):
    """Apply Gaussian parent conditioning with diagonal child prior covariance."""
    ml, vl, nl = left
    mr, vr, nr = right
    assert nl == nr and nl > 0
    # The prior covariance of the two child integrals is nl times identity.
    # Their reported variances become diagonal pseudo-observation noise.
    wl = F(nl, 1) / (nl + vl)
    wr = F(nr, 1) / (nr + vr)
    return (wl * ml + wr * mr, nl * (1 - wl) + nr * (1 - wr), nl + nr)


def compute(ys, v):
    assert ys and (len(ys) & (len(ys)-1)) == 0 and v > 0
    level = [(y / (1 + v), v / (1 + v), 1) for y in ys]
    while len(level) > 1:
        level = [merge(level[j], level[j+1]) for j in range(0,len(level),2)]
    return level[0]


def run():
    count = 0
    for v in (F(1,8), F(1,2), F(1), F(3,2), F(3), F(13,7)):
        for h in range(0,9):
            n = 1 << h
            for seed in range(6):
                ys = [F((7*j+seed*3)%29-13, j%5+1) for j in range(n)]
                mean, var, size = compute(ys,v)
                D = 1 + (h+1)*v
                assert size == n
                assert mean == sum(ys,F(0))/D
                assert var == n*v/D
                # The coherent posterior conditions each independent cell once.
                coherent_mean = sum(ys,F(0))/(1+v)
                coherent_var = n*v/(1+v)
                assert coherent_var / var == D/(1+v)
                # Unconditional variance of the error of the tree point estimate.
                mse = n*((D-1)**2+v)/D**2
                ratio = (1+(h+1)**2*v)/D
                assert mse/var == ratio
                if h:
                    assert var < coherent_var
                else:
                    assert var == coherent_var and mean == coherent_mean
                count += 7
    print('PASS',count,'exact rational identities')

if __name__ == '__main__':
    run()

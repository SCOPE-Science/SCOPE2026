"""Independent finite-chain and implicit-root checks for parity-periodic quantum transport."""
import numpy as np
from scipy.optimize import brentq
from scipy.sparse import diags, kron, identity, coo_matrix
from scipy.sparse.linalg import expm_multiply


def scgf(h, gp0, gm0, gp1, gm1, theta):
    total = gp0 + gm0
    assert min(gp0, gm0, gp1, gm1) > 0
    assert abs(total - gp1 - gm1) < 1e-13
    c0 = gp0 * np.exp(theta) + gm0 * np.exp(-theta)
    c1 = gp1 * np.exp(theta) + gm1 * np.exp(-theta)
    beta = 4 * abs(h) * abs(np.sinh(theta / 2))

    def equation(x):
        s = x + total
        a = 1 / np.sqrt(s*s - beta*beta)
        b = 1 / np.sqrt(s*s + 16*h*h * np.cosh(theta/2)**2)
        return 1 - (c0+c1)*(a-b)/2 - c0*c1*a*b

    left = beta - total + 1e-9
    right = total + 10 + 4*abs(h)
    while equation(right) <= 0:
        right = right*2 + 1
    assert equation(left) < 0
    return brentq(equation, left, right, xtol=1e-13)


def predicted(gp0, gm0, gp1, gm1, h):
    total = gp0 + gm0
    assert abs(total - gp1 - gm1) < 1e-13
    difference0 = gp0 - gm0
    difference1 = gp1 - gm1
    drift = (difference0 + difference1) / 2
    variance_rate = (total + 4*h*h/total
                     - (difference0-difference1)**2 / (2*(total+np.sqrt(total*total+16*h*h))))
    return drift, variance_rate


def finite_lindblad(n, h, gp0, gm0, gp1, gm1, times):
    assert n % 2 == 1
    total = gp0 + gm0
    one = identity(n, format='csr', dtype=complex)
    hop = diags([[h]*(n-1), [h]*(n-1)], [-1, 1], shape=(n,n),format='csr')
    rows, cols, values = [], [], []
    for j in range(n):
        plus, minus = (gp0,gm0) if (j-n//2)%2 == 0 else (gp1,gm1)
        for direction, rate in [(1, plus), (-1, minus)]:
            dest = j + direction
            if 0 <= dest < n:
                rows.append(dest*n+dest)
                cols.append(j*n+j)
                values.append(rate)
    gains = coo_matrix((values,(rows,cols)),shape=(n*n,n*n)).tocsr()
    generator = (-1j*(kron(hop,one,format='csr')-kron(one,hop,format='csr'))
                 - total*identity(n*n,format='csr',dtype=complex) + gains)
    state = np.zeros(n*n,complex)
    state[(n//2)*n+n//2] = 1.0
    coordinate = np.arange(n)-n//2
    output=[]
    for time in times:
        evolved=expm_multiply(generator*time,state)
        probability=evolved.reshape((n,n)).diagonal().real
        mass=probability.sum()
        mean=coordinate@probability
        var=(coordinate*coordinate)@probability-mean*mean
        output.append((float(mean),float(var),float(mass)))
    return output


def main():
    tested=0
    families=[(.65,.75,.45,.25,.95),(.5,.6,.3,.3,.6),
              (1.2,.9,.4,.55,.75),(2.0,.7,.7,.5,.9),
              (1e-5,.9,.3,.15,1.05),(0.0,.9,.3,.15,1.05)]
    for h,p0,m0,p1,m1 in families:
        drift, spread = predicted(p0,m0,p1,m1,h)
        step=3e-4
        L=scgf(h,p0,m0,p1,m1,-step)
        Z=scgf(h,p0,m0,p1,m1,0)
        R=scgf(h,p0,m0,p1,m1,step)
        numeric_drift=(R-L)/(2*step)
        numeric_spread=(R-2*Z+L)/(step*step)
        assert abs(Z)<1e-10, (h,Z)
        assert abs(drift-numeric_drift)<3e-6, (h,drift,numeric_drift)
        assert abs(spread-numeric_spread)<3e-5, (h,spread,numeric_spread)
        tested+=1
    p0,m0,p1,m1=.75,.45,.25,.95
    h=.65
    results=finite_lindblad(91,h,p0,m0,p1,m1,[8.0,16.0])
    drift, spread=predicted(p0,m0,p1,m1,h)
    observed_drift=(results[1][0]-results[0][0])/8
    observed_spread=(results[1][1]-results[0][1])/8
    assert all(abs(mass-1)<1e-9 for _,_,mass in results)
    assert abs(observed_drift-drift)<3e-5, (observed_drift,drift)
    assert abs(observed_spread-spread)<4e-5, (observed_spread,spread)
    assert abs(spread-(p0+m0 + 4*h*h/(p0+m0)
                -(p0-m0-p1+m1)**2/(2*(p0+m0+np.sqrt((p0+m0)**2+16*h*h)))))<1e-12
    print('VERIFY_OK scgf_curvatures=%d finite_chain=2 '
          'max_drift_error=%.3g max_diffusivity_error=%.3g'
          % (tested,abs(observed_drift-drift),abs(observed_spread-spread)))


if __name__ == '__main__':
    main()

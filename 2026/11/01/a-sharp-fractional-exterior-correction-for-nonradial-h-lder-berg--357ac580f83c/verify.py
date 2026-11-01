"""Reproduce finite Gram recurrences and large-degree asymptotics for one-mode planar Bergman polynomials.

Run: python verify.py (requires mpmath >= 1.3).
Finite computations illustrate, but do not replace, the proof of the all-degree theorem.
"""
import mpmath as mp
mp.mp.dps = 45
alpha = mp.mpf('0.6')
tau = mp.mpf('1.2')
eps = mp.mpf('0.2')
power = 1 + alpha + 1j*tau

def gamma(n):
    return 2*eps*mp.beta(2*n+2, power)

def cross(i,j):
    if i==j: return mp.mpf(1)/(i+1)
    if i==j+1: return gamma(i)
    if j==i+1: return mp.conj(gamma(j))
    return mp.mpf(0)

h=[mp.mpf(1)]
q=[[mp.mpf(1)]]
for n in range(1,14):
    a=gamma(n)/h[-1]
    poly = [-a*c for c in q[-1]]+[mp.mpf(0)]
    poly[-1]+=1
    q.append(poly)
    hn = mp.mpf(1)/(n+1)-abs(gamma(n))**2/h[-1]
    h.append(hn)
    direct = sum(poly[i]*mp.conj(poly[j])*cross(i,j)
                 for i in range(n+1) for j in range(n+1))
    assert abs(direct-hn)<mp.mpf('1e-35')
    for k in range(n):
        ip = sum(poly[i]*cross(i,k) for i in range(n+1))
        assert abs(ip)<mp.mpf('1e-35')

# Independent numerical quadrature of the beta moment for several degrees.
for n in (1,3,7):
    integ = 2*eps*mp.quad(lambda r: r**(2*n+1)*mp.power(1-r, alpha+1j*tau),[0, mp.mpf('0.8'),1])
    assert abs(integ-gamma(n))<mp.mpf('1e-32')

for n in range(14,1501):
    h.append(mp.mpf(1)/(n+1)-abs(gamma(n))**2/h[-1])

A = eps*mp.power(2,-alpha-1j*tau)*mp.gamma(power)
N=1500
an=gamma(N)/h[N-1]
leading=1/mp.sqrt(h[N])
ratio_a=an/(A*mp.power(N,-alpha-1j*tau))
ratio_k=(leading/mp.sqrt(N+1)-1)/(mp.mpf('0.5')*abs(A)**2*mp.power(N,-2*alpha))
assert abs(ratio_a-1)<mp.mpf('0.01')
assert abs(ratio_k-1)<mp.mpf('0.02')
print('CHECK_OK: Gram orthogonality, beta moments, monic recurrence, fractional asymptotics')
print('n=1500 first-coefficient ratio:',mp.nstr(ratio_a,11))
print('n=1500 normalization-response ratio:',mp.nstr(ratio_k,11))

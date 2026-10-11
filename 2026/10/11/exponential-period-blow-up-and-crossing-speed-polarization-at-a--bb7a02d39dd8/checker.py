"""Numerical sanity checks for the nilpotent cubic period and crossing formulas."""
import mpmath as m

m.mp.dps = 55


def values(b, A=1):
    b = m.mpf(b)
    A = m.mpf(A)
    d = 8 - b*b
    assert d > 0
    B = b / (2*m.sqrt(d))
    alpha = m.atan(b/m.sqrt(d))
    c = 2**m.mpf('1.25') * m.exp(B*alpha) / (A*d**m.mpf('.25'))
    integral = m.quad(lambda t: m.exp(B*t)/m.sqrt(m.cos(t)), [-m.pi/2, 0, m.pi/2])
    T_quad = c*integral
    T_gamma = 2**m.mpf('1.75')*m.pi**m.mpf('1.5')*m.exp(B*alpha) / (A*d**m.mpf('.25')*abs(m.gamma(m.mpf('.75')+1j*B/2))**2)
    up = A*A/m.sqrt(2)*m.exp(-b/m.sqrt(d)*(m.pi/2+alpha))
    down = -A*A/m.sqrt(2)*m.exp(b/m.sqrt(d)*(m.pi/2-alpha))
    assert abs((T_gamma-T_quad)/T_gamma) < m.mpf('1e-25')
    assert abs(m.log(abs(down)/up)-m.pi*b/m.sqrt(d)) < m.mpf('1e-35')
    return T_gamma, up, down


for b in ('0', '1', '-1', '2', '-2'):
    T, up, down = values(b)
    T2, _, _ = values(b, 2)
    assert abs(2*T2/T-1) < m.mpf('1e-30')

boundary_constant = 2*m.sqrt(m.pi/m.e)
for d in ('0.1', '0.01', '0.0001'):
    b = m.sqrt(8-m.mpf(d))
    T, up, down = values(b)
    scale = m.exp(-m.pi*b/(2*m.sqrt(d)))
    assert abs(T*scale/boundary_constant-1) < m.mpf('0.02')
    assert abs(-down/(m.e/m.sqrt(2))-1) < m.mpf('0.02')
    assert abs(up*m.exp(m.pi*b/m.sqrt(d))/(m.e/m.sqrt(2))-1) < m.mpf('0.02')
print('CHECK_OK')

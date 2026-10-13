from fractions import Fraction as F


def energy(s, x, u, v):
    return ((s + 2) / s * x * x
            + s * (s + 1) * u * u
            + 3 * s * (s + 1) * v * v
            - 2 * s * x * u)


def transition(s, x, u, v, sigma):
    return ((1 - s) * x + s * sigma * v,
            (x + u - sigma * v) / 2,
            (v + sigma * (x - u)) / 2)


def residual(s, x, u, v):
    plus = energy(s, *transition(s, x, u, v, 1))
    minus = energy(s, *transition(s, x, u, v, -1))
    return ((plus + minus) / 2 - energy(s, x, u, v)
            - (3 * s * s - 4) * x * x)

# Exact symbolic polynomial certificate via interpolation:
# Multiplication by s clears the only denominator in V_s.
# Each resulting state-quadratic coefficient has degree <= 5 in s:
# coefficients of s*V_s have degree <= 3; updates are at most linear
# in s; squaring raises the degree by at most two.
# Six independent states determine all quadratic-form coefficients.
states = [(1,0,0), (0,1,0), (0,0,1),
          (1,1,0), (1,0,1), (0,1,1)]
steps = [F(n, 1) for n in range(1, 7)]
for s in steps:
    for xx, uu, vv in states:
        x, u, v = F(xx), F(uu), F(vv)
        assert s * residual(s, x, u, v) == 0, (s,x,u,v)

# Principal-minor positivity at representative s values;
# general positivity is proved algebraically as 3s+2>0.
for s in (F(1,10), F(1), F(6,5), F(3)):
    assert (s+2)/s > 0
    assert (s+2)*(s+1)-s*s == 3*s+2 > 0
    assert 3*s*(s+1)>0

assert 3*F(1)**2 - 4 == -1
assert 3*F(6,5)**2 - 4 == F(8,25)

# The cached-gradient update really replaces one stored point
# by the OLD x. Check both sigma choices exactly.
for x,u,v in [(F(1), F(3), F(2)), (F(-2), F(1,2), F(-3,2))]:
    y1, y2 = u+v, u-v
    for sigma in (-1, 1):
        xn,un,vn = transition(F(2,3),x,u,v,sigma)
        assert (un+vn, un-vn) == ((x,y2) if sigma==1 else (y1,x))

print('VERIFY_OK')
print('exact_quadratic_state_tests', len(steps)*len(states))
print('critical_scaled_step', '2/sqrt(3)')

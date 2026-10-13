#!/usr/bin/env python3
import math

def errors(q, T, h):
    N = round(T / h)
    assert abs(N*h-T) < 1e-12
    r = q*q*h
    exact_second = math.exp(N*r)
    common = (1+r+r*r/2)**N
    cross_minus = (1+r-r*r/2)**N
    mse_minus = common + exact_second - 2*cross_minus
    mse_plus = exact_second - common
    return mse_minus, mse_plus

q = 0.7
T = 1.0
limit_minus = 2*math.exp(q*q*T)*q**4*T
limit_plus = math.exp(q*q*T)*q**6*T/6
vals = []
for k in range(6, 13):
    h = 2.0**(-k)
    em, ep = errors(q,T,h)
    assert em > 0 and ep > 0
    vals.append((h, em/h, ep/(h*h)))
# The finest meshes must be close to the proved limits.
h, sm, sp = vals[-1]
assert abs(sm/limit_minus-1) < 0.002
assert abs(sp/limit_plus-1) < 0.01
# Successive root-mean-square slopes approach 1/2 and 1.
for sign_index, target in [(0,0.5),(1,1.0)]:
    h1=vals[-2][0]; h2=vals[-1][0]
    e1=errors(q,T,h1)[sign_index]; e2=errors(q,T,h2)[sign_index]
    slope=math.log(math.sqrt(e2/e1))/math.log(h2/h1)
    assert abs(slope-target) < 0.02
print('VERIFY_OK')
print('printed_sign_MSE_over_h', vals[-1][1], 'limit', limit_minus)
print('correct_sign_MSE_over_h2', vals[-1][2], 'limit', limit_plus)

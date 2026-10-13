#!/usr/bin/env python3
import math

def data(mu):
    m=abs(mu)
    assert 0.0 < m < 1.0
    t=2*m/(1+m*m)
    y=(math.sqrt(t*t+8.0)-t)/4.0
    x=(2.0/math.pi)*math.asin(y)
    lam=x-0.5
    pc=2.0/(1.0-lam)
    residual=math.cos(math.pi*x)-t*math.sin(math.pi*x/2.0)
    endpoint_power=pc*(lam-1.0)+1.0
    return lam,pc,residual,endpoint_power

mus=[0.10,0.25,0.50,0.75,0.99]
rows=[data(m) for m in mus]
assert all(abs(r[2]) < 2e-14 for r in rows)
assert all(abs(r[3]+1.0) < 2e-14 for r in rows)
assert all(rows[i+1][0] < rows[i][0] for i in range(len(rows)-1))
assert all(rows[i+1][1] < rows[i][1] for i in range(len(rows)-1))
assert 12.0/7.0 < rows[-1][1] < rows[0][1] < 2.0
print('VERIFY_OK lambda_half=%.15f pc_half=%.15f pc_099=%.15f' % (rows[2][0],rows[2][1],rows[-1][1]))

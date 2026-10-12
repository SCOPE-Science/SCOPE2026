def A(k):
    return (1.0 + k/12.0)**(4.0/3.0)

k = 1
a, A0, B, C = A(k-1), A(k), A(k+1), A(k+2)
hm = A0-a
hp = B-A0
hn = C-B
integral = (
    hn/A0**4
    + 2.0/A0**2*(1.0/C - 1.0/B)
    + (1.0/(3.0*B**3) - 1.0/(3.0*C**3))
)
constant = A0**6 * integral / (8.0*hm*hp*hn)
assert constant > 0.0

def scaled_tail(t, nx=500):
    total = 0.0
    for i in range(nx):
        r = (i + 0.5)/nx
        x = hm*r*r
        wx = 2.0*r/nx
        um_inv2 = (A0-x)**-2
        for j in range(nx):
            s = (j + 0.5)/nx
            y = hp*s*s
            wy = 2.0*s/nx
            u_inv2 = (A0+y)**-2
            den = um_inv2-u_inv2
            target = u_inv2-t*den
            if target <= 0.0:
                pz = 0.0
            else:
                zcrit = target**-0.5-B
                if zcrit <= 0.0:
                    pz = 1.0
                elif zcrit >= hn:
                    pz = 0.0
                else:
                    pz = (hn-zcrit)/hn
            total += wx*wy*pz
    return t*t*total

vals = [scaled_tail(t) for t in (20.0, 40.0, 80.0, 120.0)]
assert all(v > 0.90*constant for v in vals)
assert all(v < 1.02*constant for v in vals)
assert abs(vals[-1]-constant) < 0.02*constant
print('VERIFY_OK')
print(f'constant={constant:.12f}')
print('scaled_tail=' + ','.join(f'{v:.12f}' for v in vals))

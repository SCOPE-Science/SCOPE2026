#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 80

def A(x,h):
    s1 = mp.sqrt(h*h + x*x)
    s2 = mp.sqrt(h*h + (2-x)*(2-x))
    s3 = mp.sqrt(5*h*h + (x+2)*(x+2))
    return 6 + s1 + 2*s2 + s3

def E1(x,h):
    s1 = mp.sqrt(h*h + x*x)
    s2 = mp.sqrt(h*h + (2-x)*(2-x))
    s3 = mp.sqrt(5*h*h + (x+2)*(x+2))
    return x/s1 + 2*(x-2)/s2 + (x+2)/s3

def E2(x,h):
    s1 = mp.sqrt(h*h + x*x)
    s2 = mp.sqrt(h*h + (2-x)*(2-x))
    s3 = mp.sqrt(5*h*h + (x+2)*(x+2))
    return 3*h*h*(1/s1 + 2/s2 + 5/s3) - 2*A(x,h)

xstar,hstar = mp.findroot((E1,E2),(mp.mpf('0.90405'),mp.mpf('3.25029')),tol=mp.mpf('1e-70'),maxsteps=100)
assert abs(E1(xstar,hstar)) < mp.mpf('1e-60')
assert abs(E2(xstar,hstar)) < mp.mpf('1e-60')

x_expected = mp.mpf('0.904050686013942251293839610966')
h_expected = mp.mpf('3.250288839010336161340549266368')
assert abs(xstar-x_expected) < mp.mpf('1e-29')
assert abs(hstar-h_expected) < mp.mpf('1e-29')

Fstar = A(xstar,hstar)**3/(4*hstar*hstar)
assert abs(Fstar-mp.mpf('329.6143694038955')) < mp.mpf('1e-12')

# For fixed h, A_x is strictly increasing because A is strictly convex in x.
# Reproduce the source's four fixed-height numerical experiments.
source = [
    (1, mp.mpf('0.9169')),
    (2, mp.mpf('0.9079')),
    (3, mp.mpf('0.9045')),
    (4, mp.mpf('0.9031')),
]
computed = []
for h, quoted in source:
    root = mp.findroot(lambda x: E1(x,mp.mpf(h)), mp.mpf('0.9'))
    computed.append(root)
    assert abs(root-quoted) < mp.mpf('0.00006')

# Independent finite-difference checks of the two analytic stationarity identities.
eps = mp.mpf('1e-8')
Ax_fd = (A(xstar+eps,hstar)-A(xstar-eps,hstar))/(2*eps)
Ah_fd = (A(xstar,hstar+eps)-A(xstar,hstar-eps))/(2*eps)
assert abs(Ax_fd) < mp.mpf('1e-12')
assert abs(3*hstar*Ah_fd-2*A(xstar,hstar)) < mp.mpf('1e-11')

print("VERIFY_OK")
print("x_star =", mp.nstr(xstar,40))
print("h_star =", mp.nstr(hstar,40))
print("F_star =", mp.nstr(Fstar,30))
print("fixed_height_centers =", [mp.nstr(z,18) for z in computed])

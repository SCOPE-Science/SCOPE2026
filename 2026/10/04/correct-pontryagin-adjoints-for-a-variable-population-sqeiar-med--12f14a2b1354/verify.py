#!/usr/bin/env python3
import math

# Strictly positive interior state, controls, costates, and parameters.
x = [400.0, 200.0, 300.0, 50.0, 60.0, 35.0]  # S,Q,E,I,A,R
u = [0.37, 0.28, 0.41]
lam = [0.7, -0.2, 0.1, 0.8, -0.5, 0.3]
p = {
    'beta':0.26, 'theta':0.6, 'Lambda':5.0, 'mu':0.03, 'lambda_q':0.12,
    'sigma':0.2, 'rho':0.65, 'gammaI':0.11, 'muI':0.015, 'gammaA':0.09,
    'A1':1.3, 'A2':0.8, 'B1':2.0, 'B2':2.4, 'B3':1.7,
}

def incidence(x,u,beta=None):
    S,Q,E,I,A,R = x
    u1,u2,u3 = u
    N = sum(x)
    U = u1*I + u2*A
    V = I + p['theta']*A
    bb = p['beta'] if beta is None else beta
    return bb*math.exp(-U/N)*S*V/N

def H(x,u, beta=None):
    S,Q,E,I,A,R = x
    u1,u2,u3 = u
    F = incidence(x,u,beta)
    L = p['A1']*I + p['A2']*A + 0.5*(p['B1']*u1*u1+p['B2']*u2*u2+p['B3']*u3*u3)
    f = [
        -F-u3*S+p['lambda_q']*Q+p['Lambda']-p['mu']*S,
        u3*S-p['lambda_q']*Q-p['mu']*Q,
        F-p['sigma']*E-p['mu']*E,
        p['sigma']*p['rho']*E-p['gammaI']*I-p['muI']*I-p['mu']*I,
        p['sigma']*(1-p['rho'])*E-p['gammaA']*A-p['mu']*A,
        p['gammaI']*I+p['gammaA']*A-p['mu']*R,
    ]
    return L + sum(a*b for a,b in zip(lam,f))

def corrected_costates(x,u):
    S,Q,E,I,A,R = x
    u1,u2,u3 = u
    N = sum(x)
    U = u1*I+u2*A
    V = I+p['theta']*A
    F = incidence(x,u)
    C = U/N**2 - 1.0/N
    D = lam[0]-lam[2]
    return [
        D*F*(1.0/S+C)+(lam[0]-lam[1])*u3+p['mu']*lam[0],
        D*F*C+(lam[1]-lam[0])*p['lambda_q']+p['mu']*lam[1],
        D*F*C+p['sigma']*(lam[2]-p['rho']*lam[3]-(1-p['rho'])*lam[4])+p['mu']*lam[2],
        -p['A1']+D*F*(1.0/V-u1/N+C)+(lam[3]-lam[5])*p['gammaI']+(p['muI']+p['mu'])*lam[3],
        -p['A2']+D*F*(p['theta']/V-u2/N+C)+(lam[4]-lam[5])*p['gammaA']+p['mu']*lam[4],
        D*F*C+p['mu']*lam[5],
    ]

def finite_diff_state(j):
    h = 1e-4*max(1.0,abs(x[j]))
    xp=x[:]; xm=x[:]
    xp[j]+=h; xm[j]-=h
    return -(H(xp,u)-H(xm,u))/(2*h)

def finite_diff_control(j):
    h=1e-6
    up=u[:]; um=u[:]
    up[j]+=h; um[j]-=h
    return (H(x,up)-H(x,um))/(2*h)

corr = corrected_costates(x,u)
fd = [finite_diff_state(j) for j in range(6)]
for a,b in zip(corr,fd):
    assert abs(a-b) < 3e-7, (a,b,a-b)

S,Q,E,I,A,R=x; u1,u2,u3=u; N=sum(x); F=incidence(x,u); D=lam[0]-lam[2]
ctrl = [
    p['B1']*u1+D*F*I/N,
    p['B2']*u2+D*F*A/N,
    p['B3']*u3+(lam[1]-lam[0])*S,
]
fdc=[finite_diff_control(j) for j in range(3)]
for a,b in zip(ctrl,fdc):
    assert abs(a-b) < 3e-7, (a,b,a-b)

U=u1*I+u2*A
C=U/N**2-1.0/N
assert C < 0.0
assert abs(D*F*C) > 1e-8
assert abs(corr[5]-p['mu']*lam[5]) > 1e-8

# Isolate the quarantine coupling with transmission suppressed.
def H_beta0(x,u):
    return H(x,u,beta=0.0)
h=1e-4*max(1.0,abs(x[0]))
xp=x[:]; xm=x[:]; xp[0]+=h; xm[0]-=h
fdS_beta0=-(H_beta0(xp,u)-H_beta0(xm,u))/(2*h)
correct_beta0=(lam[0]-lam[1])*u3+p['mu']*lam[0]
printed_quarantine_beta0=(lam[0]-lam[2])*u3+p['mu']*lam[0]
assert abs(fdS_beta0-correct_beta0) < 3e-8
assert abs(fdS_beta0-printed_quarantine_beta0) > 1e-3

print('VERIFY_OK')
print('C', repr(C))
print('corrected_costates', *[repr(v) for v in corr])
print('finite_difference_costates', *[repr(v) for v in fd])
print('control_gradients', *[repr(v) for v in ctrl])
print('finite_difference_controls', *[repr(v) for v in fdc])

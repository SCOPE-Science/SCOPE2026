"""Independent finite diagnostics for the exact two-node Fourier interpolation spectrum.
The infinite-degree and coalescence statements are proved analytically in RESULT.md.
"""
import math
import numpy as np


def dirichlet(n, x):
    if abs(x) < 1e-12:
        return 2*n + 1.0
    return math.sin((n + 0.5)*x)/math.sin(x/2)


def predicted(n, theta):
    N = 2*n+1
    h = 2*math.pi/N
    delta=theta*h
    a=dirichlet(n,delta)/N
    b=dirichlet(n,h-delta)/N
    c=dirichlet(n,h-2*delta)/N
    roots=[]
    for s in (1,-1):
        tr=2+s*c
        det=(a+s*b)**2
        gap=math.sqrt(max(0.0,tr*tr-4*det))
        roots.extend([(tr-gap)/2,(tr+gap)/2])
    return np.array(sorted([1.0]*(N-4)+roots))


maxerr=0.0
num=0
for N in (5,7,9,11,15,21,31,55):
    n=(N-1)//2
    for theta in (0.025, 0.1, 0.25, 0.37, 0.49):
        h=2*math.pi/N
        delta=h*theta
        xs=np.array([delta,h-delta]+[j*h for j in range(2,N)])
        F=np.exp(1j*np.outer(xs,np.arange(-n,n+1)))/math.sqrt(N)
        numerical=np.linalg.eigvalsh(F@F.conj().T)
        err=float(np.max(np.abs(numerical-predicted(n,theta))))
        maxerr=max(maxerr,err)
        assert err < 2e-12,(N,theta,err)
        num+=1

# Verify derivative coefficient of the Dirichlet ratio and the condition-number law.
for N in (5,11,31,101):
    n=(N-1)//2
    h=2*math.pi/N
    z=math.pi/(2*N)
    kn=math.pi*math.cos(z)/(N*N*math.sin(z)**2)
    d=1/(N*math.sin(z))
    limbig=(3+math.sqrt(9-16*d*d))/2
    cn=math.sqrt(limbig)/kn
    ratios=[]
    for eta in (0.02,0.01,0.005):
        theta=(1-eta)/2
        vals=predicted(n,theta)
        sigma=math.sqrt(vals[0])
        kappa=math.sqrt(vals[-1]/vals[0])
        ratios.append((sigma/eta, eta*kappa))
    assert abs(ratios[-1][0]-kn)/kn < 2e-4,(N,kn,ratios)
    assert abs(ratios[-1][1]-cn)/cn < 2e-4,(N,cn,ratios)

print('PASS: 40 independently assembled Fourier Gram spectra')
print('maximum absolute eigenvalue error: %.3g' % maxerr)
print('PASS: four small-gap singular-value and condition-number limit diagnostics')
print('All numerical checks supplement, but do not replace, the analytic proof.')

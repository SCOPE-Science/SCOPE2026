import numpy as np
from math import cos, pi, sin, sqrt

def calc_jac(N,a,b):
    # Real Jacobian of intensities of two-point periodized STFT at x=1.
    theta=2*np.pi*np.arange(N)/N
    J=np.zeros((N*N,2*N))
    for j in range(N):
        for k,th in enumerate(theta):
            c=a+b*np.exp(1j*th)
            # y= a*x[j] + b*exp(i th)*x[j+1]
            row=j*N+k
            # derivative intensity = 2 Re(conj(c)*dy)
            for l,coef in ((j,a),((j+1)%N,b*np.exp(1j*th))):
                z=2*np.conj(c)*coef
                J[row,l]+=z.real
                J[row,N+l]+=-z.imag
    return J

def bands(N,t):
    vals_mag=np.array([4-4*t+12*t*cos(2*pi*k/N) for k in range(N)])
    vals_ph=np.array([4*t*(1-cos(2*pi*k/N)) for k in range(N)])
    return sorted(np.r_[vals_mag,vals_ph])

for N in range(3,25):
    c = 1 if N%2==0 else cos(pi/N)
    s2=sin(pi/N)**2
    tstar=1/(1+3*c+2*s2)
    assert tstar<=.2500000000001,(N,tstar)
    for t in (0.1,0.2,tstar,0.25):
        a=sqrt((1+sqrt(1-4*t))/2)
        b=sqrt((1-sqrt(1-4*t))/2)*np.exp(1j*0.42)
        J=calc_jac(N,a,b)
        ev=np.linalg.eigvalsh(J.T@J/N)
        want=np.array(bands(N,t))
        assert np.max(abs(ev-want)) < 3e-12,(N,t,np.max(abs(ev-want)))
        val=ev[1]
        predicted=min(4-4*t*(1+3*c),8*t*s2)
        assert abs(val-predicted)<2e-12,(N,t,val,predicted)
    print(f'N={N:2d}, optimum t={tstar:.10f}, lambda={8*tstar*s2:.10f}, OK')
print('ALL TESTS PASS')

# Independent centered finite difference of the defining nonlinear intensity map.
rng=np.random.default_rng(20261009)
for N in [3,4,5,6,7,8,13]:
    t=1/(1+3*(1 if N%2==0 else cos(pi/N))+2*sin(pi/N)**2)
    aa=sqrt((1+sqrt(1-4*t))/2)*np.exp(0.37j)
    bb=sqrt((1-sqrt(1-4*t))/2)*np.exp(-0.74j)
    J=calc_jac(N,aa,bb)
    v=rng.normal(size=2*N)
    v/=np.linalg.norm(v)
    theta=2*pi*np.arange(N)/N
    def map_y(signal):
        return np.array([abs(aa*signal[j]+bb*np.exp(1j*theta[k])*signal[(j+1)%N])**2
                         for j in range(N) for k in range(N)])
    delta=1e-5
    vec=v[:N]+1j*v[N:]
    fd=(map_y(np.ones(N)+delta*vec)-map_y(np.ones(N)-delta*vec))/(2*delta)
    assert np.linalg.norm(fd-J@v)<2e-8,(N,np.linalg.norm(fd-J@v))
    print(f'N={N:2d}, centered intensity finite difference OK')
print('ALL INDEPENDENT DIFFERENCE TESTS PASS')

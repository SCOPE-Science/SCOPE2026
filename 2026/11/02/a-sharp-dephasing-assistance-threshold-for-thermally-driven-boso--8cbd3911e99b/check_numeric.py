"""Independent covariance-system checks for a detuned bosonic trimer.

Run: python check_numeric.py
Requires numpy. This builds the full nine-real-dimensional steady-state
linear system instead of substituting the closed form into its own equations.
"""
import numpy as np


def analytic(J, k, detune, gamma, left, right):
    contrast = left - right
    t = 4 * J**2 + k * (k + gamma)
    denom = t*t + 4 * (detune*k)**2
    x = J*k*contrast*t/denom
    u = -2*detune*J*k*k*contrast/denom
    z = -4*detune*J*J*k*contrast/denom
    p = np.array([left-2*J*x/k, (left+right)/2,
                  right+2*J*x/k])
    C = np.diag(p).astype(complex)
    C[0,1] = u + 1j*x
    C[1,0] = u - 1j*x
    C[1,2] = -u + 1j*x
    C[2,1] = -u - 1j*x
    C[0,2] = 1j*z
    C[2,0] = -1j*z
    return C, 2*J*x


def generator(X, J, k, detune, gamma):
    h = np.array([[0, J, 0],[J,detune,J],[0,J,0]], dtype=complex)
    baths = np.array([k,0,k])
    out = -1j*(h@X-X@h)
    for r in range(3):
        for c in range(3):
            out[r,c] -= (baths[r]+baths[c])*X[r,c]/2
            if r != c and (r == 1 or c == 1):
                out[r,c] -= gamma*X[r,c]/2
    return out


def unpack(X):
    return np.array([X[0,0].real, X[1,1].real, X[2,2].real,
                     X[0,1].real,X[1,2].real,X[0,2].real,
                     X[0,1].imag,X[1,2].imag,X[0,2].imag])


def basis():
    out=[]
    for j in range(3):
        X=np.zeros((3,3),complex);X[j,j]=1;out.append(X)
    for j,k in ((0,1),(1,2),(0,2)):
        X=np.zeros((3,3),complex);X[j,k]=X[k,j]=1;out.append(X)
    for j,k in ((0,1),(1,2),(0,2)):
        X=np.zeros((3,3),complex);X[j,k]=1j;X[k,j]=-1j;out.append(X)
    return out


def direct(J,k,detune,gamma,left,right):
    b=basis()
    m=np.column_stack([unpack(generator(X,J,k,detune,gamma)) for X in b])
    source=np.diag([k*left,0,k*right]).astype(complex)
    coords=np.linalg.solve(m,-unpack(source))
    return sum((coords[j]*b[j] for j in range(9)), np.zeros((3,3),complex))


def check():
    rng=np.random.default_rng(20261025)
    tested=0
    for z in range(256):
        J=np.exp(rng.uniform(-2,2));k=np.exp(rng.uniform(-2,2))
        detune=rng.uniform(-8,8)*J
        gamma=np.exp(rng.uniform(-3,3)) if z%7 else 0.
        right=rng.uniform(0,3);left=right+rng.uniform(.05,4)
        C,I=analytic(J,k,detune,gamma,left,right)
        C2=direct(J,k,detune,gamma,left,right)
        scale=1+np.linalg.norm(C2)
        assert np.linalg.norm(C-C2) < 5e-10*scale, (z,C,C2)
        source=np.diag([k*left,0,k*right]).astype(complex)
        residual=generator(C,J,k,detune,gamma)+source
        assert np.linalg.norm(residual)<5e-10*(1+np.linalg.norm(C))*(1+J+k+abs(detune)+gamma)
        assert abs(I-2*J*C2[0,1].imag)<1e-9*(1+abs(I))
        tested+=1
    # Check the global optimizer against sampled rates, both sides of the transition.
    opt_cases=0
    for J,k,d in [(1,1,0),(1,1,2.5),(1,1,5),(2,3,10),(.3,2,.6),(.4,1,4),(1,.1,40)]:
        gp=max(0.,2*abs(d)-k-4*J*J/k)
        peak=analytic(J,k,d,gp,1.,0.)[1]
        for candidate in np.linspace(0,max(4*gp+3.,50.),250):
            assert peak >= analytic(J,k,d,candidate,1.,0.)[1] - 1e-10
            opt_cases += 1
    print('PASS: %d independent 9-variable covariance comparisons; %d optimizer inequalities' % (tested,opt_cases))


if __name__=='__main__':
    check()

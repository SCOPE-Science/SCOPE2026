"""Numerical checks of the two-coset Gaussian sampling collision formula.

Run: python gaussian_period2_check.py
Requires NumPy. The infinite theorem follows from the accompanying proof,
not from finite truncations of the series used here.
"""
import numpy as np

def theta3(w, a):
    r = np.arange(-35, 36)
    return sum(np.exp(-2*a*r*r) * np.cos(r*w))

def theta4(w, a):
    r = np.arange(-35, 36)
    return sum((-1.0)**r * np.exp(-2*a*r*r) * np.cos(r*w))

def kernel_row(x, w, a):
    n = np.arange(-35, 36)
    ph = np.exp(-1j*n*w)
    return np.array([np.sum(np.exp(-a*(2*n+x-t)**2)*ph) for t in (0, 1)], dtype=complex)

def derivative_first(x, w, a):
    n = np.arange(-35, 36)
    ph = np.exp(-1j*n*w)
    z = 2*n+x
    return np.sum(-2*a*z*np.exp(-a*z*z)*ph)

def lower_upper(a, eps, W):
    smallest = np.inf
    largest = 0.0
    min_w = None
    for w in W:
        H = np.stack([kernel_row(.5-eps,w,a),kernel_row(.5+eps,w,a)])
        eig = np.linalg.eigvalsh(H.conj().T @ H)
        if eig[0] < smallest:
            smallest,min_w = eig[0],w
        largest = max(largest,eig[1])
    return smallest, largest, min_w

def main():
    W = np.linspace(0,np.pi,1001)
    tests = 0
    print('Gaussian period-two collision checks (numerical; not an infinite proof)')
    for a in (0.5,1.0,2.0):
        n = np.arange(-35,36)
        z = 2*n+.5
        A = np.sum(np.exp(-2*a*z*z))
        Ap = np.sum(-4*a*z*np.exp(-2*a*z*z))
        assert Ap < 0
        c = (Ap*Ap/A)*(theta4(0,a)**2/theta3(0,a))
        umax = 4*A*theta3(0,a)
        cc=[]
        for w in W:
            u = kernel_row(.5,w,a)[0]
            du = derivative_first(.5,w,a)
            c_direct = 4*(np.real(np.conj(u)*du)**2)/abs(u)**2
            c_theta = (Ap*Ap/A)*theta4(w,a)**2/theta3(w,a)
            assert abs(c_direct-c_theta)<1e-10*max(1,c_direct)
            cc.append(c_theta)
            tests += 1
        assert min(cc) == cc[0] and cc[-1]>cc[0]
        tests += 2
        for eps in (0.04,0.02,0.01,0.005):
            b,u,w = lower_upper(a,eps,W)
            relative = b/(eps*eps*c)
            assert abs(relative-1) < 0.2
            assert abs(u/umax-1) < 0.02
            print(f'a={a:g} eps={eps:g} lower/(c eps^2)={relative:.9f} upper/U0={u/umax:.9f} min_w={w:.6f}')
            tests += 2
        print(f'a={a:g}: c={c:.12g}, upper_limit={umax:.12g}, strict theta-minimum at 0')
    print(f'PASS: {tests} numerical assertions / symbolic reduction crosschecks')

if __name__=='__main__':main()

"""Independent numerical stress tests for the two-arc Fourier sampling formulas.

Run: python checker.py  (requires NumPy). Numerical tests corroborate,
but do not substitute for, the closed-form proof in RESULT.md.
"""
import math
import numpy as np


def gram_normalized(width, separation):
    a = math.sin(width) / width
    b = math.sin(2 * width) / (2 * width)
    c = math.cos(separation)
    return np.array([[1, a*c, b*(2*c*c-1)],
                     [a*c, 1, a*c],
                     [b*(2*c*c-1), a*c, 1]], dtype=float)


def fp(width, separation):
    return float(np.linalg.norm(gram_normalized(width, separation) - np.eye(3), 'fro')**2)


def optimal_separation(width):
    d = math.cos(width)**2
    return math.acos(math.sqrt(max(0.0, (2*d-1)/(4*d))))


assertions = 0
widths = [.02, .06, .10, .18, .3, .5, .7,
          math.pi/4 - .001, math.pi/4, math.pi/4 + .001, .9, 1.0, 1.2, 1.5]
for w in widths:
    A, B = math.sin(w)/w, math.sin(2*w)/(2*w)
    d = math.cos(w)**2
    c0 = 2*w/math.pi
    tstar = optimal_separation(w)
    zstar = max(0, (2*d-1)/(4*d))
    assert w <= tstar+1.e-14 <= math.pi/2 + 1.e-14
    assertions += 1
    assert abs(math.cos(tstar)**2-zstar) < 1e-12
    assertions += 1
    assert abs(fp(w, tstar)-A*A*(2-1/(2*d)) if w < math.pi/4 else fp(w,tstar)-2*B*B) < 1e-10
    assertions += 1
    if w < math.pi/4:
        assert abs(fp(w, math.pi/2)-fp(w, tstar)-A*A*(2*d-1)**2/(2*d)) < 1e-10
        assertions += 1
    for t in np.linspace(w, math.pi/2, 251):
        x=math.cos(t)
        m=gram_normalized(w,t)
        eig=np.linalg.eigvalsh(m)
        assert np.min(eig)>-1e-12
        assertions += 1
        assert abs(np.trace(m)-3) < 1e-12
        assertions += 1
        assert fp(w,t)+1e-11 >= fp(w,tstar)
        assertions += 1
        assert eig[0] <= 1-B + 1e-12
        assertions += 1
        if t < math.pi/2-1e-6:
            assert eig[0] < 1-B-1e-12
            assertions += 1
        # Direct quadrature on two arcs, using midpoint integration.
        if t in (w, math.pi/2):
            pass
    # Direct closed-form integral of exponentials on both arcs.
    for t in (w, tstar, math.pi/2):
        mm=np.zeros((3,3),dtype=complex)
        for j in range(3):
            for k in range(3):
                n=k-j
                if n==0: mm[j,k]=c0
                else:
                    mm[j,k]=(2*math.sin(n*w)*math.cos(n*t))/(math.pi*n)
        assert np.max(np.abs(mm/c0-gram_normalized(w,t)))<1e-12
        assertions += 1

for e in (.01,.005,.002,.001):
    t=optimal_separation(e)
    emin=np.linalg.eigvalsh(gram_normalized(e,t))[0]
    opt=np.linalg.eigvalsh(gram_normalized(e,math.pi/2))[0]
    assert abs(emin/opt - .5) < 2.0 * e
    assertions += 1

for e in (.01,.005,.002,.001):
    w=math.pi/4-e
    assert abs((math.pi/2-optimal_separation(w))/math.sqrt(e)-1) < 2*math.sqrt(e)
    assertions += 1

print('PASS:', assertions, 'numerical assertions; finite checks only')

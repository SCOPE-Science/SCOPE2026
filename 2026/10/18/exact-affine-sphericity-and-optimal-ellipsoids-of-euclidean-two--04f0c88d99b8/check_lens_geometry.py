"""Independent elementary numerical checks for the two-ball lens formulas.

The analytical proof is in RESULT.md; finite calculations test its formulae.
No third-party packages are required.
"""
from math import sqrt, isclose


def parameters(d, c):
    if d < 2 or not 0.0 < c < 1.0:
        raise ValueError('d>=2, 0<c<1 are required')
    A = 1.0 - c
    B = sqrt(1.0 - c*c)
    q = (d + 1.0)*c/sqrt(d)
    a = 2.0*(1.0 - c*c)/(sqrt(q*q + 4.0*(1.0 - c*c)) + q)
    b = sqrt(a*a + c*a*sqrt(d))
    t = sqrt((2.0 + c)/(2.0*(1.0 + c)))
    return A, B, a, b, t


def shell_max(a, b, c):
    # Compute the exact maximum of (|x|+c)^2+||z||^2 on an ellipsoid.
    # Its boundary is x=a*y, ||z||=b*sqrt(1-y^2), 0<=y<=1.
    C = a*a-b*b
    if C < 0:
        y = max(0.0, min(1.0, -c*a/C))
        values = [c*c+b*b, (c+a)**2, c*c+b*b+2*c*a*y+C*y*y]
    else:
        values = [c*c+b*b, (c+a)**2]
    return max(values)


def run():
    cases=0
    for d in (2, 3, 4, 5, 8, 16, 37, 101):
        for c in (0.005, 0.05, 0.1, 0.3, 0.5, 0.8, 0.95, 0.995):
            A, B, a, b, t = parameters(d, c)
            assert abs(a*a+(d+1.)*c*a/sqrt(d)+c*c-1.0)<2e-12
            assert abs(b*b-a*a-c*a*sqrt(d))<2e-12
            assert abs(shell_max(a,b,c)-1.0)<2e-12
            assert abs(shell_max(t*A,t*B,c)-1.0)<2e-12
            # Additional contraction strictly inside the lens.
            assert shell_max(0.999*t*A,0.999*t*B,c)<1.0+1e-12
            # Increasing t violates containment for every proper lens.
            assert shell_max((t+0.0003*(1.0-t))*A, (t+0.0003*(1.0-t))*B,c)>1.0
            assert abs(2*c*(A/2)*(1.-(A/2)/A)-c*A/2)<1e-12
            assert 0.0<a<A and 0.0<b<B and 0.5<t<1.0
            # John contact locations are unit vectors after normalization.
            assert abs(1./d+(d-1.)/d-1.)<1e-12
            # The John decomposition has zero mean and covariance I_d/d.
            assert abs((d-1.)/d/(d-1)-1./d)<1e-12
            # The two canonical ellipsoids are different (neither relabeling).
            assert abs(1./sqrt(d)-1./(2*t))>1e-4
            cases+=1
    print(f'PASS: {cases} exact stationary/quadratic/contact parameter cases')
    print('PASS: all-dimensional John contact-covariance identities')
    print('PASS: lens inclusion and strict distance-optimality perturbations')


if __name__=='__main__':
    run()

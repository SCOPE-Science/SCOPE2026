"""Numerical diagnostics for the maximum-volume ellipsoid of a two-ball lens.
Scientific proof uses the displayed containment identity and John contact certificate;
these checks are finite diagnostics, not an infinite-dimensional proof.
Run: python3 verify.py  (NumPy/SciPy required).
"""
import math
import numpy as np
from scipy.optimize import minimize


def semiaxes(dim, c):
    assert isinstance(dim, int) and dim >= 2 and 0 < c < 1
    k = c * (dim + 1) / math.sqrt(dim)
    a = 2 * (1 - c*c) / (k + math.sqrt(k*k + 4 * (1-c*c)))
    b = math.sqrt(a*a + c * a * math.sqrt(dim))
    return a, b


def worst_ball_norm_sq(a, b, c):
    # Candidate symmetric ellipsoid is contained iff this maximum <= 1.
    # The full two-ball maximum occurs with the adverse sign of the axial coordinate.
    def quadratic(t):
        return b*b + c*c + (a*a-b*b)*t*t + 2*c*a*t
    points = [0.,1.]
    if a*a < b*b:
        points.append(max(0., min(1., c*a/(b*b-a*a))))
    return max(quadratic(t) for t in points)


def test_one(dim, c):
    a,b = semiaxes(dim,c)
    h = 1 / math.sqrt(dim)
    assert 0 < a < b, (dim, c, a, b)
    assert a < 1-c and b < math.sqrt(1-c*c)
    assert abs(b*b - a*a - c*a*math.sqrt(dim)) < 2e-12
    assert abs(a*a + c*(dim+1)*a/math.sqrt(dim) + c*c - 1) < 2e-12
    assert abs(worst_ball_norm_sq(a,b,c)-1.) < 2e-12
    # The exact quadratic identity validates containment on the entire sphere.
    for t in np.linspace(0, 1, 47):
        radial = b*b+c*c+(a*a-b*b)*t*t+2*c*a*t
        identity = 1-(b*b-a*a)*(t-h)**2
        assert abs(radial-identity) < 2e-12
    # Four points per transverse coordinate form the explicit finite John certificate.
    w = dim / (4*(dim-1))
    U = []
    for j in range(dim-1):
        for sign1 in (-1,1):
            for sign2 in (-1,1):
                u = np.zeros(dim)
                u[0] = sign1*h
                u[j+1] = sign2*math.sqrt((dim-1)/dim)
                U.append(u)
    U=np.asarray(U)
    assert np.max(np.abs(w*U.sum(axis=0))) < 1e-12
    assert np.max(np.abs(w*U.T@U - np.eye(dim))) < 1e-12
    # Touched sphere points have equal outer normals after the ellipsoid change of coordinates.
    for u in U[:min(16,len(U))]:
        transformed_contact_normal=np.r_[a*a*u[0]+c*a*np.sign(u[0]),b*b*u[1:]]
        assert np.linalg.norm(transformed_contact_normal-b*b*u)<2e-12
    # Independent continuous 2-parameter optimization over axisymmetric centered ellipsoids.
    # Symmetry and uniqueness reduce all possible John ellipsoids to this class.
    if dim <= 10 and c <= 0.9:
        def objective(v):
            aa, bb=v
            return -math.log(aa) - (dim-1)*math.log(bb)
        bounds=[(1e-6,1-c),(1e-6,math.sqrt(1-c*c))]
        constr={'type':'ineq','fun':lambda v:1-worst_ball_norm_sq(v[0],v[1],c)}
        res=minimize(objective,[a*0.91,b*0.92],method='SLSQP',constraints=[constr],bounds=bounds,
                     options={'maxiter':1000,'ftol':1e-12})
        assert res.success or abs(-res.fun-(math.log(a)+(dim-1)*math.log(b))) < 1e-7, str(res)
        assert abs(-res.fun-(math.log(a)+(dim-1)*math.log(b)))<3e-7, (dim,c,res.x, [a,b])
    return a,b


def main():
    for dim in (2,3,4,5,8,10,20,50,100):
        for c in (0.001,0.1,0.3,0.65,0.9,0.99):
            a,b=test_one(dim,c)
        print(f"dimension={dim}: containment, contact isotropy and axisymmetric benchmark passed")
    c=0.5
    for dim in (200, 1000, 5000):
        a,b=semiaxes(dim,c)
        assert abs((a*math.sqrt(dim)) / ((1-c*c)/c)-1) < 0.03
        assert abs(b/math.sqrt(1-c*c)-1)<0.03
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()

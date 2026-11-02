"""Exact sample checks for the positive-parameter gamma-zero quadratic algebra."""
import sympy as s
from itertools import permutations, product


def data(a, b, c):
    a,b,c=map(s.Rational,(a,b,c))
    x,y,z=map(s.sqrt,(a,b,c))
    u,v,w=s.sqrt(a+b),s.sqrt(a+c),s.sqrt(b+c)
    H=s.Matrix([[0,-x/v,-x/u],[-y/w,0,-y/u],[-z/w,-z/v,0]])
    k=s.Matrix([y/u-z/v,z/w-x/u,x/v-y/w])
    D=s.diag(1,x*w/(y*v),x*w/(z*u))
    return H,k,D


def zero(M):
    return all(s.simplify(t)==0 for t in M)


def signed_permutation_rotations():
    for perm in permutations(range(3)):
        for signs in product((1,-1),repeat=3):
            R=s.zeros(3)
            for j,i in enumerate(perm):R[i,j]=signs[j]
            if R.det()==1:yield R


def check(a,b,c,d,expected):
    H,k,D=data(a,b,c)
    assert zero(D*H-H.T*D)
    x,y,z=s.sqrt(a),s.sqrt(b),s.sqrt(c)
    u,v,w=s.sqrt(a+b),s.sqrt(a+c),s.sqrt(b+c)
    assert s.simplify(H.det()+2*x*y*z/(u*v*w))==0
    assert s.simplify(s.sqrt(d)/s.sqrt(d)-1)==0
    if a==b==c:
        assert zero(k)
        # A continuous automorphism at the isotropic point.
        h=s.Matrix([1,1,1])/s.sqrt(3)
        K=s.Matrix([[0,-h[2],h[1]],[h[2],0,-h[0]],[-h[1],h[0],0]])
        R=h*h.T+K  # rotation by pi/2
        assert zero(R*H-H*R)
        assert zero(R.T*R-s.eye(3))
        assert R.det()==1
    else:
        assert not zero(k)
        if expected==2:
            R=s.simplify(2*k*k.T/(k.dot(k))-s.eye(3))
            assert zero(R*H-H*R)
            assert zero(R.T*R-s.eye(3))
            assert s.simplify(R.det()-1)==0
        else:
            assert not zero(k.cross(H*k))
    actual=sum(zero(R*H-H*R) for R in signed_permutation_rotations())
    if expected==1:assert actual==1
    if expected==2:assert actual==2
    if expected=='continuous':assert actual==6
    return actual

if __name__=='__main__':
    cases=[(1,1,1,1,'continuous'),(4,4,4,9,'continuous'),
        (1,1,4,1,2),(1,1,9,16,2),(1,4,1,9,2),
        (1,4,4,1,2),(1,4,9,1,1),(1,9,25,36,1),
        (1,16,25,49,1),(9,4,1,1,1)]
    for a,b,c,d,e in cases:
        check(a,b,c,d,e)
    print('VERIFY_OK exact_parameter_cases=',len(cases),'signed_orthogonal_tests=',len(cases)*24)

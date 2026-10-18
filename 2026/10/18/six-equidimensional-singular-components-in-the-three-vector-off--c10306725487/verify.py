"""Finite exact symbolic cross-checks for the three-vector orthogonal-frame theorem.

Requires Python 3 and SymPy. This verifies representative Jacobian and
transverse Hessian ranks, not the all-dimensions geometric proof.
"""
import sympy as s


def dot(u, v):
    return sum(a*b for a, b in zip(u, v))


def certificate(m, kind):
    xs = s.symbols('x0:'+str(3*m))
    v = [s.Matrix(xs[k*m:(k+1)*m]) for k in range(3)]
    q = [dot(v[0],v[1]), dot(v[0],v[2]), dot(v[1],v[2])]
    J = s.Matrix([[s.diff(f,x) for x in xs] for f in q])
    point = {x:s.Integer(0) for x in xs}
    if kind == 'linear':
        point[xs[2*m]] = 1  # v3=e1
        dep = q[0]
    else:
        # v1=0, v2=v3=(1,i,0,...), an isotropic nonzero vector
        for j in (1,2):
            point[xs[j*m]] = 1
            point[xs[j*m+1]] = s.I
        dep = q[1]-q[0]
    vals = [s.simplify(f.subs(point)) for f in q]
    assert vals==[0,0,0], (m,kind,vals)
    JJ = J.subs(point)
    assert JJ.rank()==2, (m,kind,JJ.rank())
    basis = s.Matrix.hstack(*JJ.nullspace())
    hess = s.hessian(dep, xs)
    trans_hess = s.simplify(basis.T*hess*basis)
    assert trans_hess.rank()==2*m-2,(m,kind,trans_hess.rank())
    assert trans_hess.shape==(3*m-2,3*m-2)
    return JJ.rank(),trans_hess.rank()


def main():
    a,b,c=s.symbols('a b c')
    hollow=s.Matrix([[0,a,b],[a,0,c],[b,c,0]])
    assert s.factor(hollow.det())==2*a*b*c
    ca,cb,cc=s.symbols('c1 c2 c3')
    relation=s.Matrix([[cb,cc,0],[ca,0,cc],[0,ca,cb]])
    assert s.factor(relation.det())==-2*ca*cb*cc
    for m in (3,4,5,6):
        for kind in ('linear','isotropic'):
            r,h=certificate(m,kind)
            print('M=',m,'stratum=',kind,'Jacobian rank=',r,'restricted Hessian rank=',h)
        assert 3+3*(2*(m-1))==6*m-3
    print('VERIFY_OK')

if __name__=='__main__':
    main()

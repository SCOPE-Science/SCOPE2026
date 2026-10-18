#!/usr/bin/env python3
"""Independent finite-field and symbolic checks for the rational-tangent discriminant theorem.

Uses only Python stdlib for finite-field enumeration; optional sympy is required
for geometric smoothness certificates of the displayed quartic examples.
This program does not assert that finite searches prove the uniform theorem.
"""
from collections import Counter


def projective_points(p):
    ans=[]
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if not (x or y or z):continue
                t=next(v for v in (x,y,z) if v)
                a=tuple((v*pow(t,-1,p))%p for v in (x,y,z))
                if a not in ans:ans.append(a)
    return sorted(ans)


def normalize(vec,p):
    t=next((v%p for v in vec if v%p),None)
    assert t is not None
    return tuple(v*pow(t,-1,p)%p for v in vec)


def cross(u,v,p):
    return tuple((u[(i+1)%3]*v[(i+2)%3]-u[(i+2)%3]*v[(i+1)%3])%p for i in range(3))


def gradient(x,y,z,k,p):
    return ((-x*x*y+z**3+k*x*x*z)%p,
            (x**3-y*y*z)%p,
            (y**3-x*z*z-k*x**3)%p)


def T(line,k,p):
    a,b,c=line
    return (a**3*b+b**3*c+a*c**3+k*(b**4+a*b*c*c))%p


def residual_on_line(pt,line,k,p):
    a,b,c=line; x,y,z=pt
    assert (a*x+b*y+c*z)%p==0
    return ((c+k*b)*x*x+a*y*y+b*z*z)%p


def check_prime(p,k):
    pts=projective_points(p)
    N=p*p+p+1
    assert len(pts)==N
    tangent={}
    for pt in pts:
        g=gradient(*pt,k,p)
        assert g != (0,0,0), ('rational singular',p,k,pt)
        tangent[pt]=normalize(g,p)
    fibers=Counter(tangent.values())
    assert set(fibers.values())<={1,2}
    flex=sum(v==1 for v in fibers.values())
    bitangent=sum(v==2 for v in fibers.values())
    assert 2*bitangent+flex==N
    assert sum(T(line,k,p)==0 for line in pts)==flex
    # From the *separate* restriction-quadratic viewpoint:
    q_mult=Counter()
    for line in pts:
        roots=[pt for pt in pts if (sum(a*b for a,b in zip(pt,line))%p==0)
                and residual_on_line(pt,line,k,p)==0]
        assert len(roots)<=2
        q_mult[len(roots)]+=1
        assert len(roots)==fibers.get(line,0)
        assert (T(line,k,p)==0)==(len(roots)==1)
    assert q_mult[1]==flex and q_mult[2]==bitangent and q_mult[0]==bitangent
    print(f'GF({p}) k={k}: N={N}, quartic/flex={flex}, bitangents={bitangent}, '
          f'no-rational-tangent lines={q_mult[0]}')
    return flex,bitangent


def check_quartic_smoothness(p,k):
    try:
        import sympy as sp
    except ImportError:
        print('sympy unavailable, skip geometric smoothness certificates')
        return
    x,y,z=sp.symbols('x y z')
    polynomial=x**3*y+y**3*z+x*z**3+k*(y**4+x*y*z**2)
    J=[polynomial]+[sp.diff(polynomial,u) for u in (x,y,z)]
    for u in (x,y,z):
        G=sp.groebner(J+[u-1],x,y,z,modulus=p)
        assert G.contains(sp.Poly(1,x,y,z,modulus=p)), (p,k,u,G)
    print(f'GF({p}) k={k}: quartic smooth over algebraic closure (three unit ideals)')


def check_general_symbolic_identity():
    import sympy as sp
    a,b,c,k=sp.symbols('a b c k')
    D=sp.diag(c+k*b,a,b)
    expected=a**3*b+b**3*c+a*c**3+k*(b**4+a*b*c*c)
    assert sp.expand((sp.Matrix([[a,b,c]])*D.adjugate()*sp.Matrix([a,b,c]))[0]-expected)==0
    # General rectangular Cauchy--Binet identity is proved in RESULT, not inferred
    # merely from this expansion.
    print('symbolic adjugate determinant identity: PASS')


if __name__=='__main__':
    check_general_symbolic_identity()
    for p,k in [(3,2),(5,4),(7,1),(11,1),(13,1),(17,4),(19,1)]:
        check_prime(p,k)
        check_quartic_smoothness(p,k)
    print('all finite and exact checks passed')

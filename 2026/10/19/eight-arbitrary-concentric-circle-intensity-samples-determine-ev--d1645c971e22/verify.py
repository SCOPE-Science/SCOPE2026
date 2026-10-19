"""Exact finite rational stress tests for eight-evaluation quadratic phaseless frames.

The general arbitrary-angle result is established by polynomial interpolation in
RESULT.md; these symbolic tests independently exercise its kernel predictions.
"""
from sympy import Matrix, I, Rational, simplify

A = [1, -1, I, -I, Rational(3, 5) + Rational(4, 5)*I]
A2 = [1, I, -I, Rational(-3, 5)+Rational(4, 5)*I, Rational(5,13)-Rational(12,13)*I]
O1 = [1, -1, I]
O2 = [1, Rational(3,5)+Rational(4,5)*I, -I]
O3 = [I, -1, Rational(5,13)+Rational(12,13)*I]

B=[]
for j in range(3):
    x=Matrix.zeros(3); x[j,j]=1; B.append(x)
for j,k in [(0,1),(0,2),(1,2)]:
    x=Matrix.zeros(3); x[j,k]=x[k,j]=1; B.append(x)
for j,k in [(0,1),(0,2),(1,2)]:
    x=Matrix.zeros(3); x[j,k]=I; x[k,j]=-I; B.append(x)

def measure(H,z):
    w=Matrix([1,z,z*z])
    return simplify((w.transpose()*H*w.conjugate())[0])

def lift(points):
    M=Matrix([[measure(X,z) for X in B] for z in points])
    assert all(s.is_rational for s in M)
    return M

cases=[(Rational(2),A,O1),(Rational(1,2),A2,O2),(Rational(3),A2,O3)]
for R,inners,angles in cases:
    assert len(set(inners))==5 and all(simplify(z*z.conjugate())==1 for z in inners)
    assert len(set(angles))==3 and all(simplify(z*z.conjugate())==1 for z in angles)
    samples=inners+[R*z for z in angles]
    M=lift(samples)
    assert M.rank()==8
    D=Matrix.diag(R**2,-(1+R**2),1)
    ns=M.nullspace(); assert len(ns)==1
    assert all(measure(D,z)==0 for z in samples)
    for col in range(9):
        # In these ordered Hermitian basis coordinates, D is diagonal.
        assert simplify(ns[0][col]*D[0,0] - ns[0][0]*(D[col,col] if col<3 else 0))==0
    gap=min(R**4,Rational(1))/(2*(R**4+R**2+1))
    assert gap>0
    print('radius=',R,'rank=',M.rank(),'kernel=',tuple(D[i,i] for i in range(3)),'sharp_gap_squared=',gap)

# Repeated outer sample reduces the number of effective intensity constraints.
assert lift(A+[2,2,2*I]).rank()<=7
# Coalescing radii makes all circles collapse into one Laurent degree-two curve.
assert lift(A+O3).rank()<=5
print('repetition_and_equal_radius_obstructions=PASS')
print('checks=PASS')

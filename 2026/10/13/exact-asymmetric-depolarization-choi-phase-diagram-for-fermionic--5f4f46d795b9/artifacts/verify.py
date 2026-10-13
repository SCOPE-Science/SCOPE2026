"""Independent finite-matrix checks of a four-mode fermionic Choi concurrence formula.
Requires only Python 3 standard library. The analytic theorem is proved in RESULT.md.
"""
import cmath
import math
from fractions import Fraction


def eye(n):
    return [[complex(i == j) for j in range(n)] for i in range(n)]


def kron(A, B):
    return [[a * b for a in ra for b in rb] for ra in A for rb in B]


def mv(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def inner(u, v):
    return sum(a.conjugate() * b for a, b in zip(u, v))


def scale(A, c):
    return [[c * z for z in row] for row in A]


def diff(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

I = eye(2)
X = [[0, 1], [1, 0]]
Y = [[0, -1j], [1j, 0]]
Z = [[1, 0], [0, -1]]
PAULI = {'I': I, 'X': X, 'Y': Y, 'Z': Z}
R = [[0j for _ in range(4)] for _ in range(4)]
R[3][0] = 1
R[2][1] = -1j
R[1][2] = 1j
R[0][3] = -1
Phi = [0j] * 16
for k in range(4):
    Phi[4 * k + k] = .5
J = scale(kron(kron(X, Y), kron(X, Y)), -1)
labels = [a+b for a in 'IXYZ' for b in 'IXYZ']
KM = {s: kron(kron(PAULI[s[0]], PAULI[s[1]]), eye(4)) for s in labels}
EVEN = ['II','IZ','XX','XY','YX','YY','ZI','ZZ']
ODD = ['IX','IY','XI','XZ','YI','YZ','ZX','ZY']
PAIRS = [('II','ZZ'),('IZ','ZI'),('XX','YY'),('XY','YX'),
         ('IX','ZY'),('IY','ZX'),('XI','YZ'),('XZ','YI')]
partner = {k: v for u,v in PAIRS for k in [u]}
partner.update({v:u for u,v in PAIRS})


def overlap(delta):
    U = eye(4)
    for i in range(4):
        U[i][i] = cmath.exp((1j if i in (0,3) else -1j) * delta / 4)
    psi = mv(kron(U, R), Phi)
    branch = {k: mv(KM[k], psi) for k in labels}
    # Verify orthonormality of all sixteen noise branches.
    for a in labels:
        for b in labels:
            assert abs(inner(branch[a],branch[b]) - int(a == b)) < 1e-12
    # Antiunitary Majorana conjugation: J followed by complex conjugation.
    conj = {k: mv(J, [z.conjugate() for z in branch[k]]) for k in labels}
    om = {(a,b):inner(branch[a],conj[b]) for a in labels for b in labels}
    eta = abs(math.sin(delta/2))
    xi = math.sqrt(max(0., 1-eta*eta))
    for a in labels:
        for b in labels:
            v = abs(om[(a,b)])
            want = eta if a == b else xi if b == partner[a] else 0.
            assert abs(v-want) < 1e-11, (delta,a,b,v,want)
    return om, eta


def singulars(u, v, eta):
    root = math.sqrt(eta*eta*(u-v)**2 + 4*u*v)
    return ((root+eta*abs(u-v))/2,(root-eta*abs(u-v))/2)


def concurrences(om,p1,p2,eta):
    aa=1-3*p1/4;bb=p1/4;cc=1-3*p2/4;dd=p2/4
    w={s:(aa if s[0]=='I' else bb)*(cc if s[1]=='I' else dd) for s in labels}
    out=[]
    for sector in (EVEN,ODD):
        sv=[]
        for a,b in PAIRS:
            if a not in sector: continue
            u,v=w[a],w[b]
            # Derive singular values from Frobenius norm and determinant
            # of the independent numeric 2-by-2 weighted overlap block.
            aa1=u*om[(a,a)]
            bb1=math.sqrt(u*v)*om[(a,b)]
            cc1=math.sqrt(u*v)*om[(b,a)]
            dd1=v*om[(b,b)]
            sqsum=sum(abs(t)**2 for t in (aa1,bb1,cc1,dd1))
            prod=abs(aa1*dd1-bb1*cc1)
            sumsv=math.sqrt(max(0,sqsum+2*prod))
            diffsq=max(0,sqsum-2*prod)
            diffsv=math.sqrt(diffsq)
            sv.extend([(sumsv+diffsv)/2,(sumsv-diffsv)/2])
            expected=singulars(u,v,eta)
            assert abs(max(sv[-2:])-expected[0])<1e-10
        sv.sort(reverse=True)
        out.append(max(0,2*sv[0]-sum(sv)))
    pred=max(0,eta*(aa*cc-bb*dd)-math.sqrt(eta**2*(aa*dd-bb*cc)**2+4*aa*bb*cc*dd)-4*bb*dd)
    assert abs(out[0]-pred)<2e-10 and abs(out[1])<2e-10
    return out[0],out[1]

for delta in (0.,0.42,1.3,2.7,math.pi):
    om,eta=overlap(delta)
    for p1,p2 in ((0,0),(.35,.83),(.62,.62),(.5,.5),(1,0),(.6,.7),(.12,.98),(.4,.8),(0,1)):
        concurrences(om,p1,p2,eta)

for u,v in ((Fraction(0),Fraction(1)),(Fraction(2,5),Fraction(4,5)),(Fraction(3,5),Fraction(3,5)),(Fraction(1,2),Fraction(1,2))):
    a=1-3*u/4;b=u/4;c=1-3*v/4;d=v/4
    Delta=a*c-a*d-b*c-5*b*d
    expected=1-u-v+Fraction(5,8)*u*v
    assert Delta==expected
assert 1-Fraction(2,5)-Fraction(4,5)+Fraction(5,8)*Fraction(8,25)==0
assert 1-2*Fraction(3,5)+Fraction(5,8)*Fraction(9,25)==Fraction(1,40)
pcrit=(8-2*math.sqrt(6))/5
assert abs(1-2*pcrit+5*pcrit*pcrit/8)<1e-14
print('VERIFY_OK')

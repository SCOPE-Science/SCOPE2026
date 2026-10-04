from fractions import Fraction

def project(V):
    a,b = V[0]
    c,d = V[1]
    r1,r2 = a+b,c+d
    s1,s2 = a+c,b+d
    S = r1+r2
    return [[r1*s1/S, r1*s2/S],
            [r2*s1/S, r2*s2/S]]

def det2(V):
    return V[0][0]*V[1][1]-V[0][1]*V[1][0]

def marginals(V):
    rows = [sum(V[0]),sum(V[1])]
    cols = [V[0][0]+V[1][0],V[0][1]+V[1][1]]
    return rows,cols

tests = [
    [[Fraction(3),Fraction(2)],[Fraction(5),Fraction(7)]],
    [[Fraction(1,10),Fraction(9,10)],[Fraction(9,10),Fraction(1,10)]],
    [[Fraction(4),Fraction(6)],[Fraction(2),Fraction(3)]],
]
for V in tests:
    P = project(V)
    S = sum(sum(row) for row in V)
    q = det2(V)/S
    E = [[-q,q],[q,-q]]
    for i in range(2):
        for j in range(2):
            assert P[i][j]-V[i][j] == E[i][j]

V = [[Fraction(6),Fraction(10)],[Fraction(9),Fraction(15)]]
assert det2(V) == 0
assert project(V) == V

for M in (1,10,100,10000):
    V = [[Fraction(1),Fraction(0)],[Fraction(0),Fraction(M)]]
    assert project(V)[0][0] == Fraction(1,1+M)

for den in (10,100,1000):
    eps = Fraction(1,den)
    A = [[eps,1-eps],[1-eps,eps]]
    B = [[1-eps,eps],[eps,1-eps]]
    P = [[Fraction(1,2),Fraction(1,2)],[Fraction(1,2),Fraction(1,2)]]
    assert marginals(A) == marginals(B)
    assert project(A) == P and project(B) == P
    assert project(A)[0][0]/A[0][0] == Fraction(den,2)
    assert B[0][0]/A[0][0] == den-1

beta = Fraction(9,10)
for den in (10,100,1000):
    eps = Fraction(1,den)
    c = eps*eps
    A = [[eps,1-eps],[1-eps,eps]]
    B = [[1-eps,eps],[eps,1-eps]]
    C = [[c,Fraction(0)],[Fraction(0),Fraction(0)]]
    VA11 = (beta*A[0][0]+C[0][0])/(1+beta)
    VB11 = (beta*B[0][0]+C[0][0])/(1+beta)
    assert VB11/VA11 > Fraction(den,3)
    rA,cA = marginals(A)
    rB,cB = marginals(B)
    rC,cC = marginals(C)
    assert rA == rB and cA == cB
    assert [beta*rA[i]+rC[i] for i in range(2)] == [beta*rB[i]+rC[i] for i in range(2)]
    assert [beta*cA[i]+cC[i] for i in range(2)] == [beta*cB[i]+cC[i] for i in range(2)]

print("verification passed")

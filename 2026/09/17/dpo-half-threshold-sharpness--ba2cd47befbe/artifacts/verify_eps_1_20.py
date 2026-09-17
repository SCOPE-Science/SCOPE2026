from fractions import Fraction as Q
from itertools import product

def inv2(M):
    a,b,c,d=M
    det=a*d-b*c
    assert det != 0
    return (d/det,-b/det,-c/det,a/det)

def sub_diag(A,z):
    a,b,c,d=A
    return (a-Q(z[0]),b,c,d-Q(z[1]))

def solve2(M,b):
    a,b0,c,d=inv2(M)
    return (a*b[0]+b0*b[1],c*b[0]+d*b[1])

def potential(A,z,b):
    x=solve2(sub_diag(A,z),b)
    return Q(z[0])*x[0]+Q(z[1])*x[1],x

eps=Q(1,20)
B=(Q(11,20),-Q(1,2),Q(0),-Q(1,20))
A=inv2(B)
b=(-Q(1),-Q(3))

assert A==(Q(20,11),-Q(200,11),Q(0),-Q(20))
norm1=max(abs(B[0])+abs(B[2]),abs(B[1])+abs(B[3]))
assert norm1==Q(11,20)

vals={}
for z in product((-1,1),repeat=2):
    vals[z]=potential(A,z,b)

expected={
    (-1,-1):(-Q(484,589),(Q(391,589),Q(3,19))),
    (-1, 1):(-Q(92,217),(Q(123,217),Q(1,7))),
    ( 1,-1):( Q(364,171),(Q(391,171),Q(3,19))),
    ( 1, 1):( Q(44,21),(Q(41,21),Q(1,7))),
}
assert vals==expected
assert vals[(1,-1)][0] > max(vals[z][0] for z in vals if z!=(1,-1))
assert vals[(1,-1)][1][0] > 0 and vals[(1,-1)][1][1] > 0
assert vals[(1,1)][1][0] > 0 and vals[(1,1)][1][1] > 0

gap=vals[(1,-1)][0]-vals[(1,1)][0]
assert gap==Q(40,1197)

xbad=vals[(1,-1)][1]
bad_residual=(Q(0),-2*xbad[1])
assert bad_residual==(Q(0),-Q(6,19))

print("epsilon =",eps)
print("A^{-1} =",B)
print("A =",A)
print("||A^{-1}||_1 = rho(|A^{-1}|) =",norm1)
for z in sorted(vals):
    print("z =",z,"x(z) =",vals[z][1],"F(z) =",vals[z][0])
print("bad-minus-solution potential gap =",gap)
print("AVE residual at bad maximizer =",bad_residual)
print("verified")

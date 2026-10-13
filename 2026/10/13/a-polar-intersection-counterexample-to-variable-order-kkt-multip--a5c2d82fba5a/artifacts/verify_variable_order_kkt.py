from fractions import Fraction as F

rho = F(1,10)
tau = F(1,5)
Aplus = ((F(2),F(1)),(F(1),F(0)))
Aminus = ((F(1),F(2)),(F(0),F(1)))
Azero = ((F(1),F(0)),(F(0),F(1)))

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def dil(A,t):
    s=(A[0][0]+A[1][0],A[0][1]+A[1][1])
    return tuple((r[0]+t*s[0],r[1]+t*s[1]) for r in A)

def mv(A,z):
    return tuple(r[0]*z[0]+r[1]*z[1] for r in A)

def row_coeff(A,xi):
    a,b=A[0]; c,d=A[1]; D=det(A)
    return ((xi[0]*d-xi[1]*c)/D,(a*xi[1]-b*xi[0])/D)

for A in (Aplus,Aminus,Azero):
    assert det(A) != 0
    assert all(v>0 for v in mv(A,(F(1),F(1))))

Arp,Arm,Ar0 = dil(Aplus,rho),dil(Aminus,rho),dil(Azero,rho)
assert Arp == ((F(23,10),F(11,10)),(F(13,10),F(1,10)))
assert Arm == ((F(11,10),F(23,10)),(F(1,10),F(13,10)))
assert Ar0 == ((F(11,10),F(1,10)),(F(1,10),F(11,10)))
assert abs(det(Arp)) == abs(det(Arm)) == abs(det(Ar0)) == F(6,5)

w=(F(1),F(1))
assert mv(Arp,w)==(F(17,5),F(7,5))
assert mv(Arm,w)==(F(17,5),F(7,5))
assert mv(Ar0,w)==(F(6,5),F(6,5))

Atp,Atm,At0 = dil(Aplus,tau),dil(Aminus,tau),dil(Azero,tau)
assert abs(det(Atp)) == abs(det(Atm)) == abs(det(At0)) == F(7,5)
assert mv(Atp,(F(-1),F(1))) == (F(-7,5),F(-7,5))
assert mv(Atm,(F(1),F(-1))) == (F(-7,5),F(-7,5))

xi=(F(1,2),F(1,2))
assert xi[0]+xi[1] == 1
assert row_coeff(Arp,xi)==(F(1,2),F(-1,2))
assert row_coeff(Arm,xi)==(F(1,2),F(-1,2))
assert (Arp[1][0]+Arm[1][0],Arp[1][1]+Arm[1][1])==(F(7,5),F(7,5))

fprime=(F(1),F(-1))
assert mv(Aplus,fprime)==(F(1),F(1))
assert mv(Aminus,fprime)==(F(-1),F(-1))

print("VERIFY_OK")

from fractions import Fraction
from math import gcd

w = {"x":2, "y":6, "t":7, "z":9}
assert gcd(w["x"],w["y"]) == 2
assert gcd(w["y"],w["z"]) == 3
for a,b in [("x","t"),("x","z"),("y","t"),("t","z")]:
    assert gcd(w[a],w[b]) == 1

def F(x,y,t,z):
    return z*z + y*y*(y-x**3) + x*x*t*t

cv = {"Px":F(1,0,0,0),"Py":F(0,1,0,0),"Pt":F(0,0,1,0),"Pz":F(0,0,0,1)}
assert cv == {"Px":0,"Py":1,"Pt":0,"Pz":1}

q2 = (w["t"]%2,w["z"]%2)
q3 = (w["x"]%3,w["t"]%3)
assert q2 == (1,1)
assert q3 == (2,1)

px = (1,3)
assert tuple((2*a)%4 for a in px) == (2,2)

sol = [(a,b) for a in range(7) for b in range(7)
       if (3*a-2)%7==0 and (3*b-2)%7==0 and (a+b-6)%7==0]
assert sol == [(3,3)]

combined = (16,2)
inv16 = pow(16,-1,21)
normalized = (1,(combined[1]*inv16)%21)
assert inv16 == 4 and normalized == (1,8)

def neg_cf(n,d):
    out=[]
    while d:
        a=(n+d-1)//d
        out.append(a)
        n,d=d,a*d-n
    return out

assert neg_cf(21,8) == [3,3,3]
canonical_index = 21//gcd(21,9)
assert canonical_index == 7

M=[[Fraction(-3),Fraction(1),Fraction(0)],
   [Fraction(1),Fraction(-3),Fraction(1)],
   [Fraction(0),Fraction(1),Fraction(-3)]]
b=[Fraction(1),Fraction(1),Fraction(1)]
A=[M[i]+[b[i]] for i in range(3)]
for c in range(3):
    p=next(i for i in range(c,3) if A[i][c])
    A[c],A[p]=A[p],A[c]
    q=A[c][c]
    A[c]=[v/q for v in A[c]]
    for i in range(3):
        if i!=c:
            q=A[i][c]
            A[i]=[A[i][j]-q*A[c][j] for j in range(4)]
disc=tuple(A[i][3] for i in range(3))
assert disc==(Fraction(-4,7),Fraction(-5,7),Fraction(-4,7))
assert all(a>-1 for a in disc)

count=3+1+2+3
assert count==9

print("ambient_pair_gcds=xy:2,yz:3,others:1")
print(f"coordinate_membership={cv}")
print(f"Q2_tangent_weights_mod2={q2}")
print(f"Q3_tangent_weights_mod3={q3}")
print(f"Px_order4_weights={px}")
print(f"Pt_mu7_lift_weights={sol[0]}")
print(f"Pt_order21_raw_weights={combined}")
print(f"Pt_order21_normalized_weights={normalized}")
print(f"HJ_21_over_8={neg_cf(21,8)}")
print(f"canonical_index={canonical_index}")
print("discrepancies="+",".join(str(x) for x in disc))
print(f"exceptional_curve_count={count}")
print("VERIFY_OK")

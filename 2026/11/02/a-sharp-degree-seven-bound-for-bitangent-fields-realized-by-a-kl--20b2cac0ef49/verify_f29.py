"""Finite-field certificate for the Klein twist and its 28 bitangents."""
import csv
P=29

def mul(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B): C[i+j]=(C[i+j]+a*b)%P
    return tuple(C)

def power(A,n):
    C=(1,)
    for _ in range(n): C=mul(C,A)
    return C

def norm(A):
    a=next((x for x in A if x%P),None)
    return tuple(x*pow(a,-1,P)%P for x in A) if a is not None else tuple(A)

# All projective quadratic sections and their fourth-degree squares.
quad=[(1,u,v) for u in range(P) for v in range(P)]+[(0,1,v) for v in range(P)]+[(0,0,1)]
squares={norm(mul(Q,Q)):Q for Q in quad}
assert len(squares)==P*P+P+1
# All projective lines in the dual projective plane.
lines=[(a,b,1) for a in range(P) for b in range(P)]+[(a,1,0) for a in range(P)]+[(1,0,0)]
assert len(lines)==P*P+P+1
bit=[]
for a,b,c in lines:
    if c: X,Y,Z=(1,0),(0,1),((-a)%P,(-b)%P)
    elif b: X,Y,Z=(1,0),((-a)%P,0),(0,1)
    else: X,Y,Z=(0,0),(1,0),(0,1)
    t1=mul(power(X,3),Y);t2=mul(power(Y,3),Z);t3=mul(power(Z,3),X)
    F=tuple((t1[i]+t2[i]+t3[i])%P for i in range(5))
    if norm(F) in squares:bit.append((a,b,c))
assert len(bit)==28
assert all(c==1 for a,b,c in bit)

# Check each bitangent explicitly using coefficient identities (independent
# of the projective-square enumeration above).
for a,b,c in bit:
    assert c==1
    lam=(-a**3)%P
    A=(1-3*a*a*b)%P
    B=(-3*a*b*b)%P
    C=(-a-b**3)%P
    E=(-b)%P
    u=A*pow(2*lam,-1,P)%P
    v=((B*pow(lam,-1,P)-u*u)*pow(2,-1,P))%P
    assert (lam*(2*u))%P==A
    assert (lam*(u*u+2*v))%P==B
    assert (lam*(2*u*v))%P==C
    assert (lam*v*v)%P==E
with open('bitangents_F29.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['a','b','c'])
    w.writerows(bit)
# 2 is not a seventh power, and its Kummer Frobenius multiplier is 16.
assert pow(2,4,P)==16
assert pow(2,4,P)!=1
assert pow(16,7,P)==1 and all(pow(16,j,P)!=1 for j in range(1,7))
assert len({pow(16,j,P) for j in (1,2,4)})==3
# The automorphism of the split Klein curve acts on affine dual line
# coefficients by (a,b) -> (16*a,16^(-2)*b). Compute its exact orbits.
assert {(a,b) for a,b,c in bit} == {(16*a%P,pow(16,-2,P)*b%P) for a,b,c in bit}
remaining={(a,b) for a,b,c in bit};orbits=[]
while remaining:
    v=min(remaining);orbit=[]
    while v in remaining:
        remaining.remove(v);orbit.append(v)
        v=(16*v[0]%P,pow(16,-2,P)*v[1]%P)
    assert v==orbit[0]
    orbits.append(orbit)
assert sorted(map(len,orbits))==[7]*4
print('PROJECTIVE_LINES',len(lines),'QUARTIC_SQUARE_CLASSES',len(squares))
print('RATIONAL_BITANGENTS_ON_KLEIN',len(bit))
print('KUMMER_MULTIPLIER',16,'ORDER',7)
print('FOUR_DEGREE_SEVEN_BITANGENT_ORBITS_ON_TWIST')
print('VERIFY_F29_OK')

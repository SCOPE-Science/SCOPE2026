from fractions import Fraction

# Exact consistency checks for the two witness constructions in the proof.
# These finite checks do not replace the symbolic argument in RESULT.md.

def dot(a,x):
    return sum(ai*xi for ai,xi in zip(a,x))

def dist2(x,y):
    return sum((xi-yi)**2 for xi,yi in zip(x,y))

for A in range(1,31):
    for B in range(0,A+1):
        for G in range(0,B+1):
            alpha=Fraction(A); beta=Fraction(B); gamma=Fraction(G)
            a=(alpha,beta,gamma)
            if alpha >= beta+gamma:
                p=((beta-gamma)/alpha,Fraction(-1),Fraction(1))
                q=(Fraction(-1),Fraction(1),Fraction(-1))
                assert all(Fraction(-1) <= z <= Fraction(1) for z in p)
                assert dot(a,p)==0
                assert dot(a,q)<=0
                assert dist2(p,q)>=9
            else:
                assert beta>0
                p=(Fraction(-1),(alpha-gamma)/beta,Fraction(1))
                q=(Fraction(1),Fraction(-1),Fraction(-1))
                assert all(Fraction(-1) <= z <= Fraction(1) for z in p)
                assert dot(a,p)==0
                assert dot(a,q)<0
                assert dist2(p,q)>=9

# Coordinate central cut of [-1,1]^3: each half-box has diameter exactly 3.
verts=[]
for x in (Fraction(-1),Fraction(0)):
    for y in (Fraction(-1),Fraction(1)):
        for z in (Fraction(-1),Fraction(1)):
            verts.append((x,y,z))
mx=max(dist2(x,y) for x in verts for y in verts)
assert mx==9

# Scaling [-1,1]^3 by 1/2 scales diameter 3 to 3/2.
assert Fraction(3,2)==Fraction(1,2)*3
print('VERIFY_OK cube two-division diameter')

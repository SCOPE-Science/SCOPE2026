"""Exact characteristic-five branch and Hasse computations (standard library only)."""
from itertools import combinations
from collections import Counter

# F_25 = F_5[a]/(a^2-a+1); integers n= u+5*v denote u+v*a.
def add(x,y): return (x%5+y%5)%5 + 5*((x//5+y//5)%5)
def sub(x,y): return ((x%5-y%5)%5)+5*((x//5-y//5)%5)
def mul(x,y):
    a,b=x%5,x//5; c,d=y%5,y//5
    return (a*c-b*d)%5 + 5*((a*d+b*c+b*d)%5)
def power(x,n):
    z=1
    while n:
        if n&1:z=mul(z,x)
        x=mul(x,x);n//=2
    return z
def inv(x):
    assert x;return power(x,23)
def div(x,y):return mul(x,inv(y))

def trim(P):
    P=list(P)
    while len(P)>1 and P[-1]==0:P.pop()
    return P
def padd(P,Q):return trim([add(P[i] if i<len(P) else 0,Q[i] if i<len(Q) else 0) for i in range(max(len(P),len(Q)))])
def psub(P,Q):return trim([sub(P[i] if i<len(P) else 0,Q[i] if i<len(Q) else 0) for i in range(max(len(P),len(Q)))])
def pmul(P,Q):
    R=[0]*(len(P)+len(Q)-1)
    for i,a in enumerate(P):
        for j,b in enumerate(Q): R[i+j]=add(R[i+j],mul(a,b))
    return trim(R)
def prem(P,Q):
    P=trim(P);Q=trim(Q)
    assert Q != [0]
    while P != [0] and len(P)>=len(Q):
        c=div(P[-1],Q[-1]);j=len(P)-len(Q)
        P=psub(P,[0]*j+[mul(c,t) for t in Q])
    return P
def pgcd(P,Q):
    while Q!=[0]:P,Q=Q,prem(P,Q)
    return trim([mul(v,inv(P[-1])) for v in P])

def supersingular_four(S):
    F=[x for x in S if x!=-1]
    if -1 in S:
        a,b,c=F
        A=sub(c,a);B=sub(b,a)
        # A/B is anharmonic and B is nonzero.
        assert B
    else:
        a,b,c,d=F
        A=mul(sub(d,a),sub(c,b));B=mul(sub(d,b),sub(c,a))
        assert B
    return sub(add(mul(A,A),mul(B,B)),mul(A,B))==0

def h_counts(points):return sum(supersingular_four(S) for S in combinations(points,4))

def genus2_matrix(finite_five):
    f=[1]
    for root in finite_five:f=pmul(f,[sub(0,root),1])
    f2=pmul(f,f)
    return ((f2[4],f2[3]),(f2[9],f2[8]))
def determinant(M):return sub(mul(M[0][0],M[1][1]),mul(M[0][1],M[1][0]))

a=5;b=21
assert add(mul(a,a),sub(1,a))==0
assert add(mul(b,b),sub(1,b))==0
Bstar=[-1,0,1,a,b]
T=Counter(); sharp=[]
for x in range(25):
    if x in Bstar:continue
    B=Bstar+[x]
    h=h_counts(B)
    T[h]+=1
    if h>=3:
        assert determinant(genus2_matrix([z for z in B if z!=-1]))!=0
    if h==4:sharp.append(x)
assert T==Counter({2:12,3:6,4:3})
assert sharp==[2,3,4]

# If three supersingular quartets share exactly two points pairwise,
# their omitted pairs partition the six-point branch set. Normalize the
# three quartets to {infinity,0,1,a}, {infinity,0,b,c}, {1,a,b,c}.
# The second condition forces b=a*c or b=(1-a)*c. Confirm that no
# solution of the third condition can have singular genus-two Hasse matrix.
C=[0,1];ONE=[1];A=[a]
for t in (a,b):
    Bc=pmul([t],C)
    X=pmul(psub(C,ONE),psub(Bc,A))
    Y=pmul(psub(C,A),psub(Bc,ONE))
    constraint=padd(psub(pmul(X,X),pmul(X,Y)),pmul(Y,Y))
    # f(z)=z(z-1)(z-a)(z-t*c)(z-c), polynomial coefficients in c.
    f=[[1]]
    for root in ([0],ONE,A,Bc,C):
        new=[[0] for _ in range(len(f)+1)]
        for j,coeff in enumerate(f):
            new[j]=psub(new[j],pmul(coeff,root))
            new[j+1]=padd(new[j+1],coeff)
        f=new
    f2=[[0] for _ in range(2*len(f)-1)]
    for i,p in enumerate(f):
        for j,q in enumerate(f):f2[i+j]=padd(f2[i+j],pmul(p,q))
    det=psub(pmul(f2[4],f2[8]),pmul(f2[3],f2[9]))
    assert pgcd(constraint,det)==[1], (t,constraint,det,pgcd(constraint,det))

witness=[-1,0,1,2,a,b]
assert h_counts(witness)==4
assert determinant(genus2_matrix([0,1,2,a,b]))!=0
print('VERIFY_OK: GF25 exceptional five-set completions 12/6/3; max-four orbit x=2,3,4; all h>=3 genus-two quotients ordinary; both disjoint-block families Hasse-coprime; witness h=4')

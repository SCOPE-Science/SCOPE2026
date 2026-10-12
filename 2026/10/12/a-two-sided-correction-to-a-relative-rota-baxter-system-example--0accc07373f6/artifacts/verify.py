import sympy as sp
from itertools import product

# Coordinates and matrices.
a11,a12,a21,a22,b11,b12,b21,b22=sp.symbols(
    "a11 a12 a21 a22 b11 b12 b21 b22"
)
R=sp.Matrix([[a11,a12],[a21,a22]])
S=sp.Matrix([[b11,b12],[b21,b22]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
basis=(e1,e2)

# Leibniz bracket: [e2,e1]=[e2,e2]=e1.
def bracket(x,y):
    return sp.Matrix([sp.expand(x[1]*(y[0]+y[1])),0])

# Dual regular maps used in Example 2.3.
def Lstar(x):
    return sp.Matrix([[-x[1],0],[-x[1],0]])

def Rstar(x):
    return sp.Matrix([[0,0],[-(x[0]+x[1]),0]])

def rhoL(x):
    return Lstar(x)

def rhoR(x):
    return -Lstar(x)-Rstar(x)

def defects(u,v):
    Ru,Rv=R*u,R*v
    Su,Sv=S*u,S*v
    inside=sp.simplify(rhoL(Ru)*v + rhoR(Sv)*u)
    DR=sp.simplify(bracket(Ru,Rv)-R*inside)
    DS=sp.simplify(bracket(Su,Sv)-S*inside)
    return DR,DS

direct=[]
for u in basis:
    for v in basis:
        DR,DS=defects(u,v)
        direct.extend(sp.factor(x) for x in DR if x!=0)
        direct.extend(sp.factor(x) for x in DS if x!=0)

# Fourteen equations printed in Example 2.3, moved to the left.
source=[
    a21*(a11+a21)-((b11+b21)*a12+(a11+a12)*(b21-a21)),
    (b11+b21)*a22+(a21+a22)*(b21-a21),
    b21*(b11+b21)-((b11+b21)*b12+(b11+b12)*b21-(a11+a12)*a21),
    (b11+b21)*b22+(b21+b22)*b21-(a21+a22)*a21,
    a21*(a12+a22)-(b22*(a11+a12)+(b12+b22)*a12),
    b22*(a21+a22)+(b12+b22)*a22,
    b21*(b12+b22)-(b22*(b11+b12)+(b12+b22)*b12),
    b22*(b21+b22)+(b12+b22)*b22,
    a22*(a12+a22),
    b22*(b12+b22),
    a22*(a11+a21)-a22*(a11+a12),
    -a22*(a21+a22),
    b22*(b11+b21)-a22*(b11+b12),
    -a22*(b21+b22),
]

false_positive={
    a11:-2,a12:0,a21:2,a22:0,
    b11:-1,b12:0,b21:2,b22:0,
}
assert all(sp.simplify(f.subs(false_positive))==0 for f in source)
DR11,DS11=defects(e1,e1)
assert sp.simplify(DR11.subs(false_positive))==sp.zeros(2,1)
assert sp.simplify(DS11.subs(false_positive)-sp.Matrix([2,0]))==sp.zeros(2,1)

false_negative={
    a11:-2,a12:-2,a21:2,a22:0,
    b11:-2,b12:2,b21:2,b22:0,
}
for u in basis:
    for v in basis:
        DR,DS=defects(u,v)
        assert sp.simplify(DR.subs(false_negative))==sp.zeros(2,1)
        assert sp.simplify(DS.subs(false_negative))==sp.zeros(2,1)
assert sp.simplify(source[2].subs(false_negative))==-8
assert all(sp.simplify(source[i].subs(false_negative))==0 for i in range(len(source)) if i!=2)

# Repaired nonzero equal-lower-right branch.
t=sp.symbols("t")
branch={
    a11:t,a12:-t,a21:-t,a22:t,
    b11:t,b12:-t,b21:-t,b22:t,
}
for u in basis:
    for v in basis:
        DR,DS=defects(u,v)
        assert sp.simplify(DR.subs(branch))==sp.zeros(2,1)
        assert sp.simplify(DS.subs(branch))==sp.zeros(2,1)

# Direct equations force the branch entries in characteristic != 2:
# a12=-t, a21=-t, b21=-t, b12=-t,
# then 2t(a11-t)=2t(b11-t)=0.
subs_partial={a22:t,b22:t,a12:-t,a21:-t,b12:-t,b21:-t}
DR21,DS21=defects(e2,e1)
DR11,DS11=defects(e1,e1)
forced_a=sp.factor(DR21[0].subs(subs_partial))
forced_b=sp.factor(DS21[0].subs(subs_partial))
assert sp.simplify(forced_a-2*t*(a11-t))==0
assert sp.simplify(forced_b-2*t*(b11-t))==0

def bmod(x,y,q):
    return (x[1]*(y[0]+y[1])%q,0)

def matvec(M,x,q):
    return ((M[0]*x[0]+M[1]*x[1])%q,
            (M[2]*x[0]+M[3]*x[1])%q)

def lstarmod(x,u,q):
    return ((-x[1]*u[0])%q,(-x[1]*u[0])%q)

def rstarmod(x,u,q):
    return (0,(-(x[0]+x[1])*u[0])%q)

def rholmod(x,u,q):
    return lstarmod(x,u,q)

def rhormod(x,u,q):
    L=lstarmod(x,u,q); RR=rstarmod(x,u,q)
    return ((-L[0]-RR[0])%q,(-L[1]-RR[1])%q)

def is_system(Rm,Sm,q):
    bas=((1,0),(0,1))
    for u in bas:
        for v in bas:
            Ru=matvec(Rm,u,q); Rv=matvec(Rm,v,q)
            Su=matvec(Sm,u,q); Sv=matvec(Sm,v,q)
            L=rholmod(Ru,v,q); RR=rhormod(Sv,u,q)
            inside=((L[0]+RR[0])%q,(L[1]+RR[1])%q)
            if bmod(Ru,Rv,q)!=matvec(Rm,inside,q):
                return False
            if bmod(Su,Sv,q)!=matvec(Sm,inside,q):
                return False
    return True

for q in (3,5,7):
    sols=[]
    for A11,A12,A21,B11,B12,B21,T in product(range(q),repeat=7):
        if T==0:
            continue
        Rm=(A11,A12,A21,T)
        Sm=(B11,B12,B21,T)
        if is_system(Rm,Sm,q):
            sols.append((Rm,Sm))
    expected={
        ((T,(-T)%q,(-T)%q,T),(T,(-T)%q,(-T)%q,T))
        for T in range(1,q)
    }
    assert set(sols)==expected,(q,len(sols),sols)
    print({"q":q,"equal_nonzero_lower_right_systems":len(sols)})

print("VERIFY_OK")

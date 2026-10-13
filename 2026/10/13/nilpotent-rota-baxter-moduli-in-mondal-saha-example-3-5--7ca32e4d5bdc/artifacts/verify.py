import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d,e,f,g,h,i=sp.symbols("a b c d e f g h i")
T=sp.Matrix([[a,b,c],[d,e,f],[g,h,i]])
E=[sp.eye(3)[:,j] for j in range(3)]

def br(x,y):
    return sp.Matrix([x[2]*y[0],x[2]*(y[0]+y[1]),0])

def defect(M,x,y):
    Mx,My=M*x,M*y
    return sp.simplify(br(Mx,My)-M*(br(Mx,y)+br(x,My)))

eqs=[]
for x,y in product(E,repeat=2):
    for z in defect(T,x,y):
        z=sp.factor(z)
        if z!=0 and z not in eqs and -z not in eqs:
            eqs.append(z)
assert any(sp.factor(z-h**2)==0 or sp.factor(z+h**2)==0 for z in eqs)
assert any(sp.factor(z-g*(g+h))==0 or sp.factor(z+g*(g+h))==0 for z in eqs)
assert any(sp.factor(z-b*(a+b+e))==0 or sp.factor(z+b*(a+b+e))==0 for z in eqs)

D,F,C=sp.symbols("D F C")
N1=sp.Matrix([[0,0,0],[D,0,F],[0,0,0]])
N2=sp.Matrix([[0,0,C],[0,0,F],[0,0,0]])
for M in (N1,N2):
    for x,y in product(E,repeat=2):
        assert all(sp.simplify(z)==0 for z in defect(M,x,y))
    assert sp.simplify(M**2)==sp.zeros(3)

def mv(M,v,q):
    return tuple(sum(M[3*r+s]*v[s] for s in range(3))%q for r in range(3))
def bracket(x,y,q):
    return (x[2]*y[0]%q,x[2]*(y[0]+y[1])%q,0)
def mm(A,B,q):
    return tuple(sum(A[3*r+k]*B[3*k+s] for k in range(3))%q for r in range(3) for s in range(3))
def inv3(M,q):
    A=[[M[3*r+s]%q for s in range(3)]+[1 if r==s else 0 for s in range(3)] for r in range(3)]
    for col in range(3):
        piv=next((r for r in range(col,3) if A[r][col]%q),None)
        if piv is None:return None
        A[col],A[piv]=A[piv],A[col]
        z=pow(A[col][col],-1,q); A[col]=[(z*x)%q for x in A[col]]
        for r in range(3):
            if r!=col and A[r][col]%q:
                z=A[r][col]%q
                A[r]=[(A[r][s]-z*A[col][s])%q for s in range(6)]
    return tuple(A[r][s+3]%q for r in range(3) for s in range(3))
def is_rb(M,q):
    bas=((1,0,0),(0,1,0),(0,0,1))
    for x,y in product(bas,repeat=2):
        Tx,Ty=mv(M,x,q),mv(M,y,q)
        lhs=bracket(Tx,Ty,q)
        p1,p2=bracket(Tx,y,q),bracket(x,Ty,q)
        inside=tuple((p1[k]+p2[k])%q for k in range(3))
        if lhs!=mv(M,inside,q): return False
    return True
def is_nilpotent(M,q):
    return all(x%q==0 for x in mm(mm(M,M,q),M,q))
def nijset(q):
    S=set()
    for dd,ff in product(range(q),repeat=2):
        S.add((0,0,0,dd,0,ff,0,0,0))
    for cc,ff in product(range(q),repeat=2):
        S.add((0,0,cc,0,0,ff,0,0,0))
    return S
def autset(q):
    return {(u,0,0,v,u,0,0,0,1) for u in range(1,q) for v in range(q)}
def is_aut(M,q):
    if inv3(M,q) is None:return False
    bas=((1,0,0),(0,1,0),(0,0,1))
    return all(mv(M,bracket(x,y,q),q)==bracket(mv(M,x,q),mv(M,y,q),q) for x,y in product(bas,repeat=2))
def conj(M,G,q):
    return mm(mm(G,M,q),inv3(G,q),q)

q=3
ambient={M for M in product(range(q),repeat=9) if is_rb(M,q) and is_nilpotent(M,q)}
assert ambient==nijset(q)

for q in (3,5,7):
    S=nijset(q); G=autset(q)
    assert len(S)==2*q*q-q and len(G)==q*(q-1)
    assert all(is_aut(x,q) for x in G)
    seen=set(); orbits=[]
    for M in S:
        if M in seen: continue
        O={conj(M,x,q) for x in G}; assert O<=S
        seen|=O; orbits.append(O)
    assert len(orbits)==2*q+1
    reps={(0,0,0,dd,0,0,0,0,0) for dd in range(q)}
    reps|={(0,0,0,dd,0,1,0,0,0) for dd in range(q)}
    reps.add((0,0,1,0,0,0,0,0,0))
    assert all(len(O&reps)==1 for O in orbits)
    print({"q":q,"nilpotent_rb":len(S),"orbits":len(orbits),
           "orbit_sizes":dict(sorted(Counter(map(len,orbits)).items()))})
print("VERIFY_OK")

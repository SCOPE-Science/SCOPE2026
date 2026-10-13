import sympy as sp
from itertools import product

a,u,v,b,c,d,e,f,g=sp.symbols('a u v b c d e f g')
R=sp.Matrix([[a,u,v],[b,c,d],[e,f,g]])
E=[sp.eye(3)[:,i] for i in range(3)]

def mul(x,y):
    return sp.Matrix([0,0,sp.expand(x[0]*y[0])])

def defect(M,x,y):
    Mx=M*x; My=M*y
    return sp.simplify(mul(Mx,My)-M*(mul(Mx,y)+mul(x,My)))

eq=[]
for x in E:
    for y in E:
        eq.extend([sp.factor(z) for z in defect(R,x,y) if z!=0])
# Consequences visible directly in basis pairs.
assert u**2 in eq or -u**2 in eq
assert v**2 in eq or -v**2 in eq
# After u=v=0, nonzero defects generate 2*a*d and a*(a-2*g).
red=set()
for z in eq:
    zz=sp.factor(z.subs({u:0,v:0}))
    if zz!=0: red.add(zz)
expected={sp.factor(2*a*d),sp.factor(a*(a-2*g))}
assert all(any(sp.factor(z/t) in (1,-1) for t in expected if t!=0) or z in expected or -z in expected for z in red),red
assert expected.issubset(red) or {-x for x in expected}.issubset(red) or all(any(sp.factor(z)==t or sp.factor(z)==-t for z in red) for t in expected)

# Printed-family witness over Q.
W=sp.Matrix([[1,0,0],[0,0,1],[0,0,sp.Rational(1,2)]])
D=defect(W,E[0],E[0])
assert D==sp.Matrix([0,-2,0]),D

def rank_mod(mat,p):
    A=[[x%p for x in row] for row in mat]
    m=len(A); n=len(A[0]); r=0
    for col in range(n):
        piv=next((i for i in range(r,m) if A[i][col]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][col],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][col]%p:
                t=A[i][col]%p
                A[i]=[(A[i][j]-t*A[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

def is_rb(flat,p):
    M=[list(flat[0:3]),list(flat[3:6]),list(flat[6:9])]
    def mv(x): return [sum(M[i][j]*x[j] for j in range(3))%p for i in range(3)]
    def mm(x,y): return [0,0,(x[0]*y[0])%p]
    bas=[[1,0,0],[0,1,0],[0,0,1]]
    for x in bas:
        for y in bas:
            X=mv(x); Y=mv(y)
            lhs=mm(X,Y)
            inn=[(mm(X,y)[i]+mm(x,Y)[i])%p for i in range(3)]
            if lhs!=mv(inn): return False
    return True

for p in (2,3):
    hist={0:0,1:0,2:0,3:0}; total=0
    for flat in product(range(p),repeat=9):
        if is_rb(flat,p):
            total+=1
            M=[list(flat[0:3]),list(flat[3:6]),list(flat[6:9])]
            hist[rank_mod(M,p)]+=1
    if p==2:
        expected_total=p**6
        expected_hist={0:1,1:(p+1)*(p**3-1),2:(p**3-1)*(p**3-p),3:0}
    else:
        expected_total=p**6+(p-1)*p**4
        expected_hist={0:1,1:(p+1)*(p**3-1),2:(p**3-1)*(p**3-p)+p**3*(p-1),3:p**3*(p-1)**2}
    assert total==expected_total,(p,total,expected_total)
    assert hist==expected_hist,(p,hist,expected_hist)
    print({'q':p,'count':total,'rank_histogram':hist})
print('VERIFY_OK')

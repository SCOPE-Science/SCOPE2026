import sympy as sp
from itertools import product

A,B=sp.symbols("A B", nonzero=True)
r,t,s,v=sp.symbols("r t s v")
R=sp.Matrix([[r,B*(r-t)/A],[0,t]])
S=sp.Matrix([[s,B*(s-v)/A],[0,v]])
E=[sp.Matrix([1,0]),sp.Matrix([0,1])]

def mul(x,y):
    return sp.Matrix([
        sp.expand(x[0]*y[0]+B*x[0]*y[1]+B*(1-A)/A*x[1]*y[0]),
        sp.expand((1-A)*x[0]*y[1]+A*x[1]*y[0]+B/A*x[1]*y[1])
    ])

def defects():
    out=[]
    for x,y in product(E,repeat=2):
        Rx,Ry=R*x,R*y
        Sy=S*y
        common=mul(Rx,y)+mul(x,Sy)
        out.extend(list(sp.simplify(mul(Rx,Ry)-R*common)))
        Sx=S*x
        out.extend(list(sp.simplify(mul(Sx,Sy)-S*common)))
    return [sp.factor(z) for z in out if sp.factor(z)!=0]

D=defects()
# Necessary factors occur literally up to a nonzero scalar.
def has_factor(target):
    for z in D:
        q=sp.factor(z/target)
        if not q.has(r,t,s,v):
            return True
    return False
assert has_factor(r*s)
assert has_factor(t*v)
assert has_factor(t*(r-s-t))
assert has_factor((A-1)*v*(r-s+v))

# Sufficiency away from A=1 is checked branchwise from the four equations.
def predicted_quad(q,a,r,t,s,v):
    if a%q==1:
        return (r*s)%q==0 and (t*v)%q==0 and (t*(r-s-t))%q==0
    return ((r*s)%q==0 and (t*v)%q==0 and (t*(r-s-t))%q==0 and (v*(r-s+v))%q==0)

def line_form(q,a,r,t,s,v):
    if a%q!=1:
        fam={
            (u,0,0,0) for u in range(q)
        }|{(u,0,0,(-u)%q) for u in range(q)}|{(u,u,0,0) for u in range(q)}|{(0,0,u,0) for u in range(q)}|{(0,0,u,u) for u in range(q)}|{(0,(-u)%q,u,0) for u in range(q)}
        return (r,t,s,v) in fam
    fam={(rr,0,0,vv) for rr,vv in product(range(q),repeat=2)}|{(0,0,ss,vv) for ss,vv in product(range(q),repeat=2)}|{(u,u,0,0) for u in range(q)}|{(0,(-u)%q,u,0) for u in range(q)}
    return (r,t,s,v) in fam

def mv(M,x,q):
    return tuple(sum(M[2*i+j]*x[j] for j in range(2))%q for i in range(2))

def mulq(x,y,q,a,b):
    inva=pow(a,-1,q)
    return ((x[0]*y[0]+b*x[0]*y[1]+b*(1-a)*inva*x[1]*y[0])%q,
            ((1-a)*x[0]*y[1]+a*x[1]*y[0]+b*inva*x[1]*y[1])%q)

def direct(q,a,b,r,t,s,v):
    inva=pow(a,-1,q)
    RR=(r%q,(b*(r-t)*inva)%q,0,t%q)
    SS=(s%q,(b*(s-v)*inva)%q,0,v%q)
    bas=((1,0),(0,1))
    for x,y in product(bas,repeat=2):
        Rx,Ry=mv(RR,x,q),mv(RR,y,q)
        Sx,Sy=mv(SS,x,q),mv(SS,y,q)
        common=tuple((mulq(Rx,y,q,a,b)[i]+mulq(x,Sy,q,a,b)[i])%q for i in range(2))
        if mulq(Rx,Ry,q,a,b)!=mv(RR,common,q): return False
        if mulq(Sx,Sy,q,a,b)!=mv(SS,common,q): return False
    return True

for q in (2,3,5,7):
    for a in range(1,q):
        expected_count=2*q*q+q-2 if a==1 else 6*q-5
        for b in range(q):
            got=0
            for r0,t0,s0,v0 in product(range(q),repeat=4):
                d=direct(q,a,b,r0,t0,s0,v0)
                p=predicted_quad(q,a,r0,t0,s0,v0)
                f=line_form(q,a,r0,t0,s0,v0)
                assert d==p==f,(q,a,b,r0,t0,s0,v0,d,p,f)
                got+=d
            assert got==expected_count,(q,a,b,got,expected_count)
    print({"q":q,"verified_all_a_b":True})

print("VERIFY_OK")

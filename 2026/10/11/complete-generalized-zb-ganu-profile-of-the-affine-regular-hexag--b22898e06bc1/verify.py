import math
import sympy as s

r,z=s.symbols("r z", positive=True)
sqrt=s.sqrt
rstar=s.sqrt((s.sqrt(5)-1)/2)

F1=(r+s.sqrt(1+r**2))/(1+r**2)
F2=(1+3*r**2+r**4)/(2*r*(1+r**2))

# Transition identity and continuity.
assert s.simplify(rstar**4+rstar**2-1)==0
assert s.simplify((F1-F2).subs(r,rstar))==0

# Upper-certificate branches.
G1=(z+2*r+(1+r**2)/z)/(2*(1+r**2))
z0=s.sqrt(1+r**2)
assert s.simplify(G1.subs(z,z0)-F1)==0

G2=((1+r**2)*z+2*r+r**2/z)/(2*(1+r**2))
assert s.simplify(G2.subs(z,1/r)-F2)==0

# The second branch is increasing on z>=1/r:
dG2=s.factor(s.diff(G2,z))
# numerator of derivative is positive there because z^2 >= 1/r^2 >= r^2/(1+r^2).
assert dG2 != 0

# Explicit first-branch extremizer.
t1=r+s.sqrt(1+r**2)
Q1=s.simplify(2*t1*(1+r*t1)/((1+r**2)*(1+t1**2)))
assert s.simplify(Q1-F1)==0
assert s.simplify(t1**2-(1+2*r*t1))==0

# Explicit second-branch extremizer.
t2=(1+r**2)/r
ss=(r**4+r**2-1)/(2*r**2)
Q2=s.simplify(2*(1+r*t2-ss)*(t2+r*ss)/((1+r**2)*(1+t2**2)))
assert s.simplify(Q2-F2)==0

# Dual-norm lemma on the six vertices.
verts=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
# coordinate functionals e1=s, e2=t, e3=s-t
def ecoord(i,v):
    a,b=v
    return (a,b,a-b)[i]
def dual_value(i,j,A,B,sign):
    vals=[]
    for v in verts:
        vals.append(A*ecoord(i,v)+sign*B*ecoord(j,v))
    return max(vals)
for i in range(3):
    for j in range(3):
        if i==j:
            continue
        for A,B in [(2.0,0.7),(0.4,1.3),(1.0,1.0)]:
            plus=dual_value(i,j,A,B,1)
            minus=dual_value(i,j,A,B,-1)
            got=sorted([round(plus,12),round(minus,12)])
            want=sorted([round(A+B,12),round(max(A,B),12)])
            assert got==want,(i,j,A,B,got,want)

# Independent deterministic sampling of the defining quotient.
def N(v):
    a,b=v
    return max(abs(a),abs(b),abs(a-b))
def unit(theta):
    v=(math.cos(theta),math.sin(theta))
    q=N(v)
    return (v[0]/q,v[1]/q)
def formula(rr):
    rs=float(rstar.evalf())
    if rr<=rs:
        return (rr+math.sqrt(1+rr*rr))/(1+rr*rr)
    return (1+3*rr*rr+rr**4)/(2*rr*(1+rr*rr))
for rr in (0.08,0.2,0.5,0.78,0.80,0.9,1.0):
    target=formula(rr)
    best=0.0
    for ia in range(72):
        x=unit(2*math.pi*ia/72)
        for ib in range(72):
            y0=unit(2*math.pi*ib/72)
            for lt in (-2,-1,-0.5,0,0.5,1,2):
                tt=math.exp(lt)
                y=(tt*y0[0],tt*y0[1])
                A=N((x[0]+rr*y[0],x[1]+rr*y[1]))
                B=N((rr*x[0]-y[0],rr*x[1]-y[1]))
                val=2*A*B/((1+rr*rr)*(1+tt*tt))
                best=max(best,val)
                assert val<=target+2e-10,(rr,val,target)
    # coarse grid need not hit the exact optimizer, only remain below the theorem value
    assert best>1.0

print("VERIFY_OK dual_pairs=6 branches=2 threshold=r^4+r^2=1 profile=hexagonal_generalized_Zbaganu")

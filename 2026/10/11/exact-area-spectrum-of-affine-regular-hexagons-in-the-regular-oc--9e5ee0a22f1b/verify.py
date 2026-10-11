#!/usr/bin/env python3
import sympy as sp

s,t=sp.symbols('s t', real=True)
r2=sp.sqrt(2)
q=r2/2
r=r2-1
V=[(1,0),(q,q),(0,1),(-q,q),(-1,0),(-q,-q),(0,-1),(q,-q)]
N=[(1,r),(r,1),(-r,1),(-1,r),(-1,-r),(-r,-1),(r,-1),(1,-r)]

def edge(i,z):
    a=V[i]; b=V[(i+1)%8]
    return (sp.expand(a[0]+z*(b[0]-a[0])),sp.expand(a[1]+z*(b[1]-a[1])))

def dot(a,b):
    return sp.expand(a[0]*b[0]+a[1]*b[1])

def det(a,b):
    return sp.expand(a[0]*b[1]-a[1]*b[0])

def sign_exact(x):
    x=sp.simplify(x)
    if x==0: return 0
    return 1 if sp.N(x,50)>0 else -1

u=edge(0,s)
feasible=[]
for j in range(8):
    v=edge(j,t)
    w=(sp.expand(v[0]-u[0]),sp.expand(v[1]-u[1]))
    for k,nk in enumerate(N):
        eq=sp.expand(dot(nk,w)-1)
        sol=sp.solve(eq,t)
        if not sol: continue
        ts=sp.simplify(sol[0])
        if ts.has(t): continue
        vv=(sp.expand(v[0].subs(t,ts)),sp.expand(v[1].subs(t,ts)))
        ww=(sp.expand(vv[0]-u[0]),sp.expand(vv[1]-u[1]))
        constraints=[s,1-s,ts,1-ts]+[sp.expand(1-dot(n,ww)) for n in N]
        lo=sp.Integer(0); hi=sp.Integer(1); ok=True
        for e in constraints:
            a=sp.simplify(sp.diff(e,s)); b=sp.simplify(e.subs(s,0))
            if a==0:
                if sign_exact(b)<0: ok=False; break
                continue
            root=sp.simplify(-b/a)
            if sign_exact(a)>0:
                if sign_exact(root-lo)>0: lo=root
            else:
                if sign_exact(root-hi)<0: hi=root
        if (not ok) or sign_exact(hi-lo)<0: continue
        D=sp.factor(det(u,vv))
        feasible.append((j,k,sp.simplify(ts),sp.simplify(lo),sp.simplify(hi),D))

assert len(feasible)==6
positive=[c for c in feasible if sign_exact(c[5].subs(s,(c[3]+c[4])/2))>0]
assert [(c[0],c[1]) for c in positive]==[(1,2),(1,3),(2,3)]

expected=[
    (0,1-q,(2-r2)*s**2+(2*r2-3)*s+(3-r2)/2),
    (1-q,q,(1-r2/2)*s**2+(r2/2-1)*s+(2+r2)/4),
    (q,1,(2-r2)*s**2-s+(1+r2)/2),
]
Dmin=(2+3*r2)/8
Dmax=(3-r2)/2
for case,exp in zip(positive,expected):
    _,_,_,lo,hi,D=case
    elo,ehi,eD=exp
    assert sp.simplify(lo-elo)==0
    assert sp.simplify(hi-ehi)==0
    assert sp.simplify(D-eD)==0
    crit=sp.simplify(sp.solve(sp.diff(D,s),s)[0])
    assert sign_exact(crit-lo)>=0 and sign_exact(hi-crit)>=0
    assert sp.simplify(D.subs(s,crit)-Dmin)==0
    assert sp.simplify(D.subs(s,lo)-Dmax)==0
    assert sp.simplify(D.subs(s,hi)-Dmax)==0

Amin=sp.simplify(3*Dmin)
Amax=sp.simplify(3*Dmax)
Ao=2*r2
assert sp.simplify(Amin/Ao-(9+3*r2)/16)==0
assert sp.simplify(Amax/Ao-(9*r2-6)/8)==0

print('VERIFY_OK')
print('feasible_oriented_chambers =',len(feasible))
print('positive_chambers =',[(c[0],c[1]) for c in positive])
print('det_min =',Dmin)
print('det_max =',Dmax)
print('area_min =',Amin)
print('area_max =',Amax)

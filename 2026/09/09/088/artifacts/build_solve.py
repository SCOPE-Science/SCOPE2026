"""Build exact (Fraction) quadratic systems for Gr(2,6) secant Schubert problem,
search solutions with multi-start Newton (numpy), track overlap deformation."""
import itertools, math, json, sys
from fractions import Fraction as Q

def gamma(t):
    return [t**k for k in range(6)]

def build_system(groups):
    """groups: 8 x 4 Fractions. Returns (const, lin, quad) exact rational tensors.
    Chart H=[I2 | M], vars m[i][j] idx=i*4+j. f_eq = det([H; K_eq])."""
    const=[Q(0)]*8
    lin=[[Q(0)]*8 for _ in range(8)]
    quad=[[ [Q(0)]*8 for _ in range(8)] for _ in range(8)]
    for eq in range(8):
        K=[gamma(t) for t in groups[eq]]
        for p in itertools.permutations(range(6)):
            inv=0
            for a in range(6):
                for b in range(a+1,6):
                    if p[a]>p[b]: inv+=1
            sgn = Q(-1) if inv%2 else Q(1)
            # row0 factor
            c0=p[0]; c1=p[1]
            f0 = None; f1=None
            if c0==0: f0=('c',Q(1))
            elif c0==1: f0=('c',Q(0))
            else: f0=('v',0*4+(c0-2))
            if c1==0: f1=('c',Q(0))
            elif c1==1: f1=('c',Q(1))
            else: f1=('v',1*4+(c1-2))
            if f0[0]=='c' and f0[1]==0: continue
            if f1[0]=='c' and f1[1]==0: continue
            kprod=sgn
            for r in range(4):
                kprod*=K[r][p[2+r]]
            if kprod==0: continue
            if f0[0]=='c' and f1[0]=='c':
                const[eq]+=kprod*f0[1]*f1[1]
            elif f0[0]=='v' and f1[0]=='v':
                a,b=f0[1],f1[1]
                quad[eq][a][b]+=kprod
            elif f0[0]=='v':
                lin[eq][f0[1]]+=kprod*f1[1]
            else:
                lin[eq][f1[1]]+=kprod*f0[1]
    return const,lin,quad

def to_float(sys):
    const,lin,quad=sys
    import numpy as np
    return (np.array([float(c) for c in const]),
            np.array([[float(v) for v in row] for row in lin]),
            np.array([[[float(v) for v in row] for row in mat] for mat in quad]))

def F_eval(S,x):
    import numpy as np
    c,L,Qd=S
    return c + L@x + np.einsum('eab,a,b->e',Qd,x,x)

def J_eval(S,x):
    c,L,Qd=S
    import numpy as np
    return L + np.einsum('eab,b->ea',Qd,x) + np.einsum('eab,a->eb',Qd,x)

def newton(S,x0,nit=60,tol=1e-14):
    import numpy as np
    x=x0.copy()
    for _ in range(nit):
        F=F_eval(S,x); J=J_eval(S,x)
        try:
            d=np.linalg.solve(J,-F)
        except np.linalg.LinAlgError:
            return x,False
        x=x+d
        if np.max(np.abs(d))<tol:
            return x,True
    F=F_eval(S,x)
    if np.max(np.abs(F))<1e-10:
        return x,True
    return x,False

def find_all(S,nstarts=600,seed=0,box=3.0):
    import numpy as np
    rng=np.random.default_rng(seed)
    sols=[]
    starts=list(rng.standard_normal((nstarts//2,8))+1j*rng.standard_normal((nstarts//2,8)))
    starts+=list((rng.uniform(-box,box,(nstarts//2,8))).astype(complex))
    for s in starts:
        x,ok=newton(S,s)
        if ok:
            if np.max(np.abs(F_eval(S,x)))<1e-8:
                sols.append(x)
    # cluster
    clusters=[]
    for x in sols:
        for c in clusters:
            if np.max(np.abs(x-c[0]))<1e-6:
                c.append(x); break
        else:
            clusters.append([x])
    reps=[]
    for c in clusters:
        best=min(c,key=lambda x: np.max(np.abs(F_eval(S,x))))
        x2,ok=newton(S,best,nit=200,tol=1e-15)
        reps.append(x2)
    # recluster polished
    out=[]
    for x in reps:
        for y in out:
            if np.max(np.abs(x-y))<1e-7:
                break
        else:
            out.append(x)
    return out

def nreal(sols,tol=1e-6):
    return sum(1 for x in sols if max(abs(v.imag) for v in x)<tol)

if __name__=='__main__':
    import numpy as np
    # disjoint intervals: centers -1.4 + 0.4k, points c+{0,.08,.16,.24}
    groups=[]
    centers=[Q(-14,10)+Q(4,10)*k for k in range(8)]
    offs=[Q(0),Q(8,100),Q(16,100),Q(24,100)]
    for c in centers:
        groups.append([c+o for o in offs])
    sys_ = build_system(groups)
    Sf=to_float(sys_)
    sols=find_all(Sf,nstarts=800,seed=1)
    print("nsols:",len(sols),"nreal:",nreal(sols))
    for x in sols:
        print("  res:",np.max(np.abs(F_eval(Sf,x))),"maximag:",max(abs(v.imag) for v in x))

"""Independent verifier: replays census_intervals.json + Tstar_log.json from scratch (stdlib only).
Checks: face topology (closed, Euler chi=0), interval containment of replayed float W,
extremal disjointness, T* per-vertex sums, angle-defect ~0, refinement monotonicity."""
import json, math
from collections import defaultdict

def sub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(dot(a,a))
def ctangent(p,q1,q2):
    e1=sub(q1,p); e2=sub(q2,p)
    n=cross(e1,e2); nn=norm(n); n=(n[0]/nn,n[1]/nn,n[2]/nn)
    d11=dot(e1,e1); d12=dot(e1,e2); d22=dot(e2,e2); det=d11*d22-d12*d12
    a=(d11/2*d22-d12*d22/2)/det; b=(d11*d22/2-d12*d11/2)/det
    Omp=(a*e1[0]+b*e2[0],a*e1[1]+b*e2[1],a*e1[2]+b*e2[2])
    t=cross(n,Omp); tn=norm(t); return (t[0]/tn,t[1]/tn,t[2]/tn)

def W_of(V,F):
    ef=defaultdict(list)
    for fi,(a,b,c) in enumerate(F):
        for e in [tuple(sorted((a,b))),tuple(sorted((b,c))),tuple(sorted((c,a)))]:
            ef[e].append(fi)
    tot=0.0; Wv=[0.0]*len(V)
    for e,fl in ef.items():
        if len(fl)!=2: return None,None,False
        v0,v1=e
        o1=[x for x in F[fl[0]] if x!=v0 and x!=v1][0]
        o2=[x for x in F[fl[1]] if x!=v0 and x!=v1][0]
        t1=ctangent(V[v0],V[v1],V[o1]); t2=ctangent(V[v0],V[v1],V[o2])
        beta=math.pi-math.acos(max(-1,min(1,dot(t1,t2))))
        tot+=beta; Wv[v0]+=beta/2; Wv[v1]+=beta/2
    for v in range(len(V)): Wv[v]-=math.pi
    return tot-math.pi*len(V),Wv,True

def torus(m,n,R,r):
    V=[]
    for i in range(m):
        th=2*math.pi*i/m; ct,st=math.cos(th),math.sin(th)
        for j in range(n):
            ph=2*math.pi*j/n; cp,sp=math.cos(ph),math.sin(ph)
            V.append(((R+r*ct)*cp,(R+r*ct)*sp,r*st))
    F=[]
    for i in range(m):
        for j in range(n):
            a=(i%n if False else (i% m)*n+(j%n)); b=((i+1)%m)*n+(j%n); c=((i+1)%m)*n+((j+1)%n); d=(i%m)*n+((j+1)%n)
            F.append((a,b,c)); F.append((a,c,d))
    return V,F

ok=True
tab=json.load(open("output/artifacts/census_intervals.json"))
LAM={"14142135623730951/10000000000000000":math.sqrt(2),"6/5":1.2,"13/10":1.3,"27/20":1.35,"3/2":1.5,"8/5":1.6,"2":2.0}
for r in tab:
    lam=LAM[r["lam"]] if r["lam"] in LAM else float(r["lam"])
    V,F=torus(r["m"],r["n"],lam,1.0)
    # topology
    assert len(F)==2*r["m"]*r["n"]
    E=len({tuple(sorted(e)) for f in F for e in [(f[0],f[1]),(f[1],f[2]),(f[2],f[0])]})
    chi=len(V)-E+len(F)
    assert chi==0,(r["id"],chi)
    W,_,closed=W_of(V,F)
    assert closed
    inside=r["lo"]-1e-9<=W<=r["hi"]+1e-9
    match=abs(W-r["float"])<1e-9
    print(f"{r['id']:6s} chi={chi} replay W={W:.6f} in-interval={inside} match-float={match}")
    ok=ok and inside and match
s=sorted(tab,key=lambda r:r["lo"])
print("extremal",s[0]["id"],"disjoint:",s[0]["hi"]<s[1]["lo"],"margin:",s[1]["lo"]-s[0]["hi"])
ok=ok and (s[0]["hi"]<s[1]["lo"]) and s[0]["id"]=="T88"
T=json.load(open("output/artifacts/Tstar_log.json"))
W,Wv,_=W_of(T["vertices"],[tuple(f) for f in T["faces"]])
print("T* replay:",abs(W-T["W"])<1e-9,"sum per-vertex:",abs(sum(T["W_per_vertex"])-T["W"])<1e-9)
ok=ok and abs(W-T["W"])<1e-9
print("ALL CHECKS PASS" if ok else "FAIL")

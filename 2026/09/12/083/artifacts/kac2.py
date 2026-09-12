"""Optimized Freudenthal-Kac for affine G2 level-2 vacuum + string extraction.
Precompute integer pairings. Only vacuum Lam=(0,0)."""
from fractions import Fraction as Q
from collections import defaultdict
import json, time
t0=time.time()

# scale: work in units where Gram entries *3: G3=[[6,-3],[-3,2]]; dot3 integer.
def dot3(u,v):
    return 6*u[0]*v[0]-3*u[0]*v[1]-3*u[1]*v[0]+2*u[1]*v[1]
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def mul(s,u): return (s*u[0],s*u[1])
POS=[(1,0),(1,3),(2,3),(0,1),(1,1),(1,2)]
ALLR=POS+[(-a,-b) for (a,b) in POS]
RHO=(3,5); KPL=6; K=2
# dd numerator: base3 - (dot3(w+rho,w+rho) - 36*n) all over 3? dd = (base3 - dot3 + 36 n)/3
# s: pairings (dot3(w+ja,a)+3*K*np)/3 etc. Keep everything x3: S3 integer; m = 2*S3/dd3... dd_true = dd3/3, s_true = S3/3 -> m = 2*S3/dd3.
N=9; B=14
Lam=(0,0)
base3=dot3(RHO,RHO)
keys=[]
for n in range(N+1):
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            keys.append((n,(a,b)))
keys.sort(key=lambda k:(k[0],(Lam[0]-k[1][0])+(Lam[1]-k[1][1])))
m={(0,Lam):Q(1)}
def asF(fr): return fr
from fractions import Fraction as Q
for key in keys:
    if key==(0,Lam): continue
    n,w=key
    wr=add(w,RHO)
    dd3=base3-(dot3(wr,wr)-36*n)
    if dd3==0: m[key]=Q(0); continue
    S3=0
    for (a,b) in POS:
        j=1
        while True:
            kk=(n,(w[0]+j*a,w[1]+j*b))
            if abs(kk[1][0])>B or abs(kk[1][1])>B: break
            c=m.get(kk)
            if c:
                wa=add(w,mul(j,(a,b)))
                S3+= (dot3(wa,(a,b)))*c
            j+=1
    for np in range(1,n+1):
        for (a,b) in ALLR:
            j=1
            while j*np<=n:
                kk=(n-j*np,(w[0]+j*a,w[1]+j*b))
                if abs(kk[1][0])<=B and abs(kk[1][1])<=B:
                    c=m.get(kk)
                    if c:
                        wa=add(w,mul(j,(a,b)))
                        S3+=(dot3(wa,(a,b))+3*K*np)*c
                j+=1
        j=1
        while j*np<=n:
            kk=(n-j*np,w)
            c=m.get(kk)
            if c: S3+=(3*K*np)*2*c
            j+=1
    m[key]=(2*S3)/dd3 if dd3!=0 else Q(0)
print('recursion time', time.time()-t0)
A=defaultdict(dict)
for (n,w),v in m.items():
    if v!=0: A[n][w]=int(v)
print('grade totals:', [sum(A[n].values()) for n in range(N+1)])
def E36(w):
    x,y=w; return 18*x*x-18*x*y+6*y*y
def mod2(w): return (w[0]%2,w[1]%2)
c=defaultdict(dict); conf=0
for n in range(N+1):
    for w,v in A[n].items():
        cl=mod2(w); e=36*n-E36(w)
        if e<0: conf+=1; continue
        if e in c[cl]:
            if c[cl][e]!=v: conf+=1
        else: c[cl][e]=v
print('conflicts',conf)
for cl in sorted(c):
    es=sorted(c[cl])
    print('class',cl,[(e,c[cl][e]) for e in es if e<=9*36][:20])
json.dump({str(cl):{str(e):c[cl][e] for e in sorted(c[cl])} for cl in c}, open('output/artifacts/string00.json','w'))

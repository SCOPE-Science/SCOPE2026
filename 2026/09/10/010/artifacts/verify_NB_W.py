"""N,B,W,Wmax,rho-ledger for the fan datum (proof inputs, recomputable).
Caps: K_disc=5 discs radius 0.2 along xi1=0 + R^-1/2-cap decomposition for N/B counting.
N/B protocol: decompose each fat cap into r0=0.1 sub-caps; pairwise separation of
sub-cap centers >= 0.1 -> broad. Pairs within same sub-cap -> narrow.
W protocol: one tube per FAT cap (central tube), wall-bound iff centerline frac>=0.5
in N_10(Z(P*)), P*=x1x2x3. Both W-count and energy rho reported; fallback needs
W>=0.70 Wmax and energy rho>=0.70.
"""
import math, itertools
R=100.0; Wd=10.0
K=5; rcap=0.2
centers=[(0.0,-0.8+1.6*k/(K-1)) for k in range(K)]
# sub-caps radius 0.1 covering each fat cap: center + 4 offsets
offs=[(0,0),(0.1,0),(-0.1,0),(0,0.1),(0,-0.1)]
sub=[]
for (c1,c2) in centers:
    for (o1,o2) in offs:
        sub.append((c1+o1,c2+o2))
print("subcaps:",len(sub))
nt=nb=0
for a,b in itertools.combinations(range(len(sub)),2):
    nt+=1
    if math.dist(sub[a],sub[b])>=0.1-1e-9: nb+=1
B=nb/nt; N=1-B
print(f"N={N:.5f} B={B:.5f} N+B={N+B:.5f}")
def gdir(c):
    gx=c[0]+0.025*c[0]*c[0]; gy=c[1]
    n=math.sqrt(gx*gx+gy*gy+1.0)
    return (-gx/n,-gy/n,1.0/n)
# tubes: central tube per fat cap, base (0, by_k) with by spread; also per-subcap tube census
def wallfrac(base,d,w=Wd):
    hit=0; tot=0
    s=0.0
    while s<=100.0:
        x=base[0]+s*d[0]; y=base[1]+s*d[1]; z=s*d[2]
        if x*x+y*y+z*z<=R*R:
            tot+=1
            if min(abs(x),abs(y),abs(z))<=w: hit+=1
        s+=1.0
    return hit/max(tot,1)
import random
random.seed(512)
Wt=0; rows=[]
for k,(c1,c2) in enumerate(centers):
    by=-36+18*k
    f=wallfrac((0.0,by),gdir((c1,c2)))
    rows.append(((c1,c2),by,[round(v,3) for v in gdir((c1,c2))],round(f,3)))
    Wt+= (f>=0.5)
print(f"fat-cap tubes: W={Wt}/{K} rho_count={Wt/K:.3f}")
for r in rows: print(r)
# subcap tube census (25 tubes, bases spread in wall slab |bx|<=5)
Ws=0
for k,(c1,c2) in enumerate(sub):
    f=wallfrac((random.uniform(-5,5),random.uniform(-45,45)),gdir((c1,c2)))
    Ws+=(f>=0.5)
print(f"subcap tubes: W={Ws}/{len(sub)} rho_count={Ws/len(sub):.3f}")

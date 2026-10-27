"""Independent exact-count checks for the four-orientation bounded-run language.
No external dependencies. Run: python verify_counts.py
"""
from collections import defaultdict
from math import pi, sqrt
from itertools import product
SIG=(0,45,-45,90)
NEI={a:tuple(b for b in SIG if b!=a and min(abs(a-b)%180,180-abs(a-b)%180)<=45) for a in SIG}
assert all(len(NEI[a])==2 for a in SIG)

def enumerate_counts(n, mirror=False):
    cur={(a,1,int(a==45)-int(a==-45),int(a==0),int(a==90)):1 for a in SIG}
    for k in range(2,n+1):
        nxt=defaultdict(int)
        for (a,r,d,c0,c90),v in cur.items():
            if r<3: nxt[a,r+1,d+(a==45)-(a==-45),c0+(a==0),c90+(a==90)]+=v
            for b in NEI[a]:
                nxt[b,1,d+(b==45)-(b==-45),c0+(b==0),c90+(b==90)]+=v
        cur=nxt
    t=(n+9)//10
    acceptable=lambda a,r,d,c0,c90: (not mirror or r==1) and d==0
    bal=sum(v for (a,r,d,c0,c90),v in cur.items() if acceptable(a,r,d,c0,c90))
    ten=sum(v for (a,r,d,c0,c90),v in cur.items() if acceptable(a,r,d,c0,c90) and c0>=t and c90>=t and (n-c0-c90)//2>=t)
    eq=sum(v for (a,r,d,c0,c90),v in cur.items() if acceptable(a,r,d,c0,c90) and n%4==0 and c0==n//4 and c90==n//4)
    total=sum(v for (a,r,d,c0,c90),v in cur.items() if not mirror or r==1)
    return (total,bal,ten,eq)

def check_bare(n):
    out=[]
    for w in product(SIG,repeat=n):
        if not all((w[i]==w[i-1] or w[i] in NEI[w[i-1]]) for i in range(1,n)):continue
        if any(w[i:i+4]==(w[i],)*4 for i in range(n-3)):continue
        d=w.count(45)-w.count(-45);t=(n+9)//10
        good=d==0
        out.append((good,good and all(w.count(a)>=t for a in SIG),good and n%4==0 and all(w.count(a)==n//4 for a in SIG)))
    return len(out),sum(q[0] for q in out),sum(q[1] for q in out),sum(q[2] for q in out)

for n in range(1,8): assert enumerate_counts(n)==check_bare(n),(n,enumerate_counts(n),check_bare(n))
assert enumerate_counts(48)==(31056472857623585226752,1928147653129777177600,1899989961206244002236,98266297652879155168)
assert enumerate_counts(24,mirror=True)[:3]==(144527708160,12651215232,11236189644)
# Root and Gaussian constants, with no scientific inference from the numerical fit.
lo,hi=.0,1.0
for _ in range(90):
    mid=(lo+hi)/2
    if 2*(mid+mid**2+mid**3)>1: hi=mid
    else:lo=mid
rho=(lo+hi)/2
K=1/(rho*(1+2*rho+3*rho*rho))
mu=2*(rho+2*rho*rho+3*rho**3)
nu=2*(rho+4*rho*rho+9*rho**3)
sigma2=nu/(2*mu); tau2=(nu-mu*mu)/mu
C=K/sqrt(2*pi*sigma2)
Cstar=8*K/((2*pi)**1.5*sigma2*sqrt(tau2))
Cmirror=2*rho*C
assert abs(C-.6235633407316379)<1.e-10
assert abs(Cstar-1.617518528363286)<1.e-10
assert abs(Cmirror-.42715090453458684)<1.e-10
print('VERIFIED exact locally-compliant, balanced, ten-percent and equal-composition counts at n=48:',enumerate_counts(48))
print('VERIFIED mirror half length 24, full length 48:',enumerate_counts(24,True))
print('VERIFIED brute-force words at n=1,...,7 and analytic constants',rho,1/rho,K,mu,nu,sigma2,tau2,C,Cstar,Cmirror)

from fractions import Fraction
N=10; M=N+1
def pmul(a,b):
    c={}
    for i,ca in a.items():
        for j,cb in b.items():
            c[i+j]=c.get(i+j,0)+ca*cb
    return {k:v for k,v in c.items() if v!=0}
d0={0:Fraction(1)}; d1={1:Fraction(-4)}; d2={1:Fraction(-4),2:Fraction(4)}
S=[None]*(M+1); S[0]={0:Fraction(1)}
def dcoef(n): return d0 if n==0 else (d1 if n==1 else (d2 if n==2 else {}))
for n in range(1,M+1):
    acc=dict(dcoef(n))
    for k in range(1,n):
        for i,ca in S[k].items():
            for j,cb in S[n-k].items():
                acc[i+j]=acc.get(i+j,0)-ca*cb
    S[n]={k:v*Fraction(1,2) for k,v in acc.items() if v!=0}
P=[None]*(M+1); P[0]={k:v for k,v in ({0:Fraction(-1)}|{k:S[0].get(k,0)+v for k,v in {}.items()}).items() if v!=0}
P[0]={0:Fraction(-1)}
for k,v in S[0].items(): P[0][k]=P[0].get(k,0)+v
P[0]={k:v for k,v in P[0].items() if v!=0}
assert P[0]=={}, P[0]
for n in range(1,M+1):
    Pn=dict(S[n])
    if n==1:
        for k,v in {1:Fraction(2),2:Fraction(-2)}.items(): Pn[k]=Pn.get(k,0)+v
    if n==2:
        for k,v in {1:Fraction(2),2:Fraction(-4),3:Fraction(2)}.items(): Pn[k]=Pn.get(k,0)+v
    P[n]={k:v for k,v in Pn.items() if v!=0}
q1={2:Fraction(-2)}; q2={2:Fraction(-2),3:Fraction(2)}
E=[None]*(N+1)
for n in range(1,M+1):
    # q1 E_{n-1} = P_n - q2 E_{n-2}
    acc=dict(P[n])
    if n-2>=0 and E[n-2] is not None:
        sub=pmul(q2,E[n-2])
        for k,v in sub.items(): acc[k]=acc.get(k,0)-v
    acc={k:v for k,v in acc.items() if v!=0}
    En={}
    for deg,c in acc.items():
        assert deg>=2,(n,deg,acc)
        En[deg-2]=c/Fraction(-2)
    E[n-1]=En
for n in range(N+1):
    print(n,{k:int(v) for k,v in sorted(E[n].items())})
import json
from collections import defaultdict
D123=json.load(open("output/artifacts/tri_123_n10.json"))
ok=True
for n in range(N+1):
    d=defaultdict(int)
    if n==0: d={0:1}
    else:
        for k,v in D123[str(n)]["tri"].items():
            dd=int(k.split(",")[2]); d[dd]+=v
    ef={k:int(v) for k,v in sorted(E[n].items())}
    match=(dict(sorted(d.items()))==ef)
    ok&=match
    print(f"n={n} census={dict(sorted(d.items()))} GF={ef} match={match}")
print("GF_MATCH_ALL:",ok)

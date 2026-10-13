#!/usr/bin/env python3
import json
from pathlib import Path
K,R=10,4
def sb(w):
    n=len(w)
    for m in range(1,n//K+1):
        if w[n-K*m:]==w[n-m:]*K:return True
    for m in range(1,n//R+1):
        s=w[n-R*m:]
        if len({s[j*m:(j+1)*m] for j in range(R)})==R:return True
    return False
def fb(w):
    n=len(w)
    for i in range(n):
        for m in range(1,(n-i)//K+1):
            if w[i:i+K*m]==w[i:i+m]*K:return True
        for m in range(1,(n-i)//R+1):
            s=w[i:i+R*m]
            if len({s[j*m:(j+1)*m] for j in range(R)})==R:return True
    return False
def grow(test):
    L=[[""]]
    for _ in range(42):
        z=[]
        for w in L[-1]:
            for c in "01":
                q=w+c
                if not test(q):z.append(q)
        L.append(z)
    return L
root=Path(__file__).resolve().parent
C=json.loads((root/"certificate.json").read_text())
A=grow(sb);B=grow(fb)
assert A==B
assert [len(x) for x in A]==C["survivor_counts_length_0_to_42"]
assert A[41]==C["length_41_extremizers"] and len(A[42])==0
x,y=A[41]
assert y=="".join("1" if c=="0" else "0" for c in x)
assert x==x[::-1] and y==y[::-1]
for w in A[41]:
    assert not fb(w)
    assert fb(w+"0") and fb(w+"1")
print("VERIFY_OK k=10 r=4 threshold=42 count41=2 count42=0 complement_orbit=1 palindromes=2 engines=2 counts32_42="+",".join(str(len(A[n])) for n in range(32,43)))

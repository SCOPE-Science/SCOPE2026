#!/usr/bin/env python3
"""Independent extension-field root/Jacobian verifier for bidegree-(2,4)."""
from collections import Counter
import json
MOD={1:0b11,2:0b111,3:0b1011,4:0b10011}

def product(a,b,d):
    out=0; p=MOD[d]; bit=1<<d
    while b:
        if b&1: out^=a
        b>>=1;a<<=1
        if a&bit:a^=p
    return out

def power(a,k,d):
    v=1
    while k:
        if k&1:v=product(v,a,d)
        a=product(a,a,d);k>>=1
    return v

def evaluate(f,x,d):
    v=0
    for i in range(4,-1,-1):v=product(v,x,d)^((f>>i)&1)
    return v

def derivative(f):return ((f>>1)&1)|(((f>>3)&1)<<2)

cache={}
for b in range(1,32):
    cache[b]={d:[x for x in range(1<<d) if evaluate(b,x,d)==0] for d in MOD}

def rank(b):
    n1=len(cache[b][1]); n2=len(cache[b][2]);n3=len(cache[b][3]);n4=len(cache[b][4]);
    assert (n2-n1)%2==0 and (n3-n1)%3==0 and (n4-n2)%4==0
    nr=n1+(n2-n1)+(n3-n1)+(n4-n2)+(int(not (b&16)))
    return nr-1

def smooth(a,b,c):
    if not b:return False
    for d in MOD:
        for x in cache[b][d]:
            aa,cc=evaluate(a,x,d),evaluate(c,x,d)
            if aa==cc==0:return False
            s=power(cc,1<<(d-1),d);t=power(aa,1<<(d-1),d)
            da=evaluate(derivative(a),x,d)
            db=evaluate(derivative(b),x,d)
            dc=evaluate(derivative(c),x,d)
            delta=product(da,product(s,s,d),d)^product(db,product(s,t,d),d)^product(dc,product(t,t,d),d)
            if delta==0:return False
    if not (b&16):
        aa,cc=(a>>4)&1,(c>>4)&1
        if aa==cc==0:return False
        if (((a>>3)&1)&cc)^(((b>>3)&1)&aa&cc)^(((c>>3)&1)&aa)==0:return False
    return True

def pointcount(a,b,c):
    total=0
    for bitmask in [1,31,16]:
        aa=(a&bitmask).bit_count()%2
        bb=(b&bitmask).bit_count()%2
        cc=(c&bitmask).bit_count()%2
        total+=sum(1 for s,t in [(1,0),(0,1),(1,1)] if not (aa*s^bb*s*t^cc*t))
    return total

def main():
    result=Counter()
    for a in range(32):
        for b in range(1,32):
            r=rank(b)
            for c in range(32):
                if smooth(a,b,c):result[(r,pointcount(a,b,c))]+=1
    out={'count':sum(result.values()), 'joint':[
        dict(p_rank=i,points=j,count=n) for (i,j),n in sorted(result.items())]}
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__':main()

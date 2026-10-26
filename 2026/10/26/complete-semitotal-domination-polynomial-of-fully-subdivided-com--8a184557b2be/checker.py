"""Direct adjacency-based exhaustive comparison for the cardinality polynomial for semitotal domination on S(K_n)."""
from math import comb
from collections import Counter
import json

def predicted(n):
    from math import comb
    def prod(a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): out[i+j]+=x*y
        return out
    def binompow(k): return [comb(k,j) for j in range(k+1)]
    N=n+comb(n,2)
    ans=[0]*(N+1)
    for b in range(n+1):
        a=n-b
        mandatory=a+comb(b,2)
        cross=a*b
        q=prod(binompow(comb(a,2)),binompow(cross))
        if b>=1 and a>=1 and (b<=2 or a==1):
            q=[q[j]-(comb(comb(a,2),j) if j<=comb(a,2) else 0) for j in range(len(q))]
        for j,x in enumerate(q): ans[j+mandatory]+=comb(n,b)*x
    return ans

def verify(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    N=n+len(edges)
    adj=[0]*N
    for k,(i,j) in enumerate(edges):
        t=n+k;adj[i]|=1<<t; adj[j]|=1<<t; adj[t]|=(1<<i)|(1<<j)
    within2=[]
    for v in range(N):
        a=adj[v];two=a
        t=a
        while t:
            bit=t&-t;t-=bit;w=bit.bit_length()-1
            two|=adj[w]
        two &= ~(1<<v)
        within2.append(two)
    count=[0]*(N+1); all_bits=(1<<N)-1
    for s in range(1,1<<N):
        t=all_bits ^ s
        ok=True
        while t:
            bit=t&-t; t-=bit; v=bit.bit_length()-1
            if not adj[v]&s:
                ok=False;break
        if not ok:continue
        t=s
        while t:
            bit=t&-t;t-=bit;v=bit.bit_length()-1
            if not within2[v]&s:
                ok=False;break
        if ok: count[s.bit_count()]+=1
    expected=predicted(n)
    assert count==expected,(n,count,expected)
    low=next(i for i,x in enumerate(count) if x)
    return {'n':n,'vertices':N,'tested_subsets':(1<<N)-1,'minimum_size':low,'minimum_count':count[low], 'coefficient_list':count}

if __name__=='__main__':
    data=[verify(n) for n in (3,4,5,6)]
    print(json.dumps(data,sort_keys=True,separators=(',',':')))

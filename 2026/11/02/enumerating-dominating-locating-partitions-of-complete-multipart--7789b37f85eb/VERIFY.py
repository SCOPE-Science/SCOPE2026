"""Direct exhaustive checks of the DLDS and double-LD partition enumerators."""
from itertools import product
from math import prod

def polynomial_prediction(sizes):
    p=[n for n in sizes if n>=2]
    s=len(sizes)-len(p)
    if len(p)<2:
        if len(p)==1 and s>=2:
            return {1:s,2:s*p[0]}
        return {1:s} if s else {}
    poly=[1]
    for a in p:
        nxt=[0]*(len(poly)+1)
        for k,v in enumerate(poly):
            nxt[k]+=v
            nxt[k+1]+=a*v
        poly=nxt
    result=[0]*(len(poly)+1)
    for k,v in enumerate(poly):
        result[k]+=v
        result[k+1]+=s*v
    result[0]-=1
    result[1]-=sum(p)
    return {i:v for i,v in enumerate(result) if v}

def double_prediction(sizes):
    p=[n for n in sizes if n>=2]
    s=len(sizes)-len(p)
    if any(n>2 for n in p) or s>2:
        return {}
    if s==2:
        return {len(p)+1:2**(len(p)+1)}
    if s==1 and len(p)>=2:
        return {len(p):2**len(p),len(p)+1:2**len(p)}
    if s==0 and len(p)>=2:
        return {len(p):2**len(p)}
    return {}

def graph(sizes):
    parts=[]
    for i,n in enumerate(sizes):parts += [i]*n
    N=len(parts)
    masks=[]
    for v in range(N):
        masks.append(sum(1<<w for w in range(N) if parts[v]!=parts[w]))
    return masks

def dom(masks, subset):
    N=len(masks)
    return all(subset>>v&1 or subset&masks[v] for v in range(N))

def ld(masks, subset):
    if not dom(masks,subset):return False
    signatures=[]
    for v in range(len(masks)):
        if not(subset>>v&1):
            s=masks[v]&subset
            if s in signatures:return False
            signatures.append(s)
    return True

def direct(sizes):
    masks=graph(sizes);n=len(masks)
    p={};d={}
    for A in range(1<<n):
        B=((1<<n)-1)^A
        if dom(masks,A) and ld(masks,B):
            p[A.bit_count()]=p.get(A.bit_count(),0)+1
        if ld(masks,A) and ld(masks,B):d[A.bit_count()]=d.get(A.bit_count(),0)+1
    return p,d

if __name__=='__main__':
    tested=0;subsets=0
    for k in range(2,7):
        for sizes in product(range(1,6),repeat=k):
            if sum(sizes)>12 or any(a>b for a,b in zip(sizes,sizes[1:])):continue
            expected=polynomial_prediction(sizes); expdouble=double_prediction(sizes)
            actual,directdouble=direct(sizes)
            assert actual==expected,(sizes,actual,expected)
            assert directdouble==expdouble,(sizes,directdouble,expdouble)
            tested+=1;subsets+=2**sum(sizes)
    print('VERIFY_OK profiles='+str(tested)+' subsets='+str(subsets)+' both_complete_weight_enumerators=true')

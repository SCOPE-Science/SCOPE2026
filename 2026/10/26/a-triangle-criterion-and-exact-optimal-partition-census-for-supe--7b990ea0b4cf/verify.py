from itertools import combinations
from math import comb
from random import Random


def setparts(n,k):
    def go(i,labs,top):
        if i==n:
            if top+1==k:
                yield [sum(1<<j for j,c in enumerate(labs) if c==v) for v in range(k)]
            return
        for a in range(min(top+1,k-1)+1):
            labs.append(a)
            yield from go(i+1,labs,max(top,a))
            labs.pop()
    yield from go(1,[0],0)

def test_graph(n,ed):
    nb=[0]*n
    for i,j in ed: nb[i]|=1<<j;nb[j]|=1<<i
    if 0 in nb: return False
    whole=(1<<n)-1
    def issp(mask):
        left=whole^mask
        for v in range(n):
            if not(left>>v&1):continue
            if not any((mask>>u&1) and (nb[u]&left)==(1<<v) for u in range(n)):return False
        return True
    if any(issp(whole^sum(1<<i for i in c)) for c in combinations(range(n),3)):return False
    pairs=[(i,j) for i,j in combinations(range(n),2) if issp(whole^(1<<i)^(1<<j))]
    e=len(pairs); t=sum(all((x,y) in pairs for x,y in [(i,j),(i,k),(j,k)]) for i,j,k in combinations(range(n),3))
    mm2=sum(len(set(a+b))==4 for a,b in combinations(pairs,2))
    mm3=sum(len(set(a+b+c))==6 for a,b,c in combinations(pairs,3))
    count={}
    for k in (3,4):
        count[k]=sum(all(not issp(b) and any(issp(b|c) for j,c in enumerate(bl) if i!=j) for i,b in enumerate(bl)) for bl in setparts(n,k))
    assert count[4]==t,(n,ed,'4',count[4],t)
    formula=comb(n,2)-e+e*(n-2)+mm2-2*((n==5)*mm2+(n==6)*mm3)
    assert count[3]==formula,(n,ed,'3',count[3],formula)
    assert max(k for k in (3,4) if count[k]>0)==(4 if t else 3)
    return True

def main():
    rnd=Random(260722686);nt=0
    for n in (5,6,7):
        E=list(combinations(range(n),2))
        total=(1<<len(E)) if n==5 else 1200
        for j in range(total):
            mask=j if n==5 else rnd.getrandbits(len(E))
            ed=[e for k,e in enumerate(E) if mask>>k&1]
            nt+=int(test_graph(n,ed))
    print('VERIFY_OK: high-super-domination graphs tested',nt)
if __name__=='__main__':main()

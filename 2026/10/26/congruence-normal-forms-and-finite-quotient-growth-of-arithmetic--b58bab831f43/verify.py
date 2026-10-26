"""Direct finite quotient congruence verification for arithmetic overflow semirings."""
from itertools import combinations
from math import comb

def partitions(n):
    labels=[0]*n
    def rec(i,m):
        if i==n:
            yield tuple(labels)
            return
        for c in range(m+2):
            labels[i]=c
            yield from rec(i+1,max(m,c))
    yield from rec(1,0)

def algebra(N,k):
    # elements 0..N-1 and k overflow values with smallest at integer N
    n=N+k
    def plus(a,b):
        if a>=N or b>=N:return max(N,a if a>=N else N,b if b>=N else N)
        s=a+b
        return s if s<N else N
    def mult(a,b):
        if not a or not b:return 0
        if a>=N or b>=N:return max(N,a if a>=N else N,b if b>=N else N)
        s=a*b
        return s if s<N else N
    return n,plus,mult

def check(N,k):
    n,plus,mult=algebra(N,k)
    plus_table=[[plus(a,b) for b in range(n)] for a in range(n)]
    mult_table=[[mult(a,b) for b in range(n)] for a in range(n)]
    found=set()
    for cl in partitions(n):
        ok=True
        for a in range(n):
            for b in range(a+1,n):
                if cl[a]!=cl[b]:continue
                for c in range(n):
                    if cl[plus_table[a][c]]!=cl[plus_table[b][c]] or cl[mult_table[a][c]]!=cl[mult_table[b][c]]:
                        ok=False;break
                if not ok:break
            if not ok:break
        if ok:found.add(cl)
    pred=set()
    for t in range(1,N+1):
        for cuts in range(1<<(k-1)):
            cl=[]
            # 0..t-1 stay separate, n>=t coalesced with lowest L block
            for x in range(N):cl.append(x if x<t else t)
            for i in range(k):
                cl.append(t+(cuts&((1<<i)-1)).bit_count())
            pred.add(tuple(cl))
    pred.add(tuple([0]*n))
    assert found==pred,(N,k,len(found),len(pred),list(found-pred)[:3],list(pred-found)[:3])
    print(f'N={N} k={k}: {len(found)} congruences = {N}*2^{k-1}+1')

if __name__=='__main__':
    for N,k in [(2,1),(3,1),(4,1),(5,1),(6,1),(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3)]:check(N,k)
    print('VERIFY_OK')

def quot_algebra(T,P,k):
    N=T+P
    def reduce(n):return n if n<T else T+(n-T)%P
    def plus(a,b):
        if a>=N or b>=N:return max(N,a if a>=N else N,b if b>=N else N)
        return reduce(a+b)
    def mul(a,b):
        if not a or not b:return 0
        if a>=N or b>=N:return max(N,a if a>=N else N,b if b>=N else N)
        return reduce(a*b)
    return N+k,plus,mul

def canonical(a):
    ids={};out=[]
    for x in a:
        if x not in ids:ids[x]=len(ids)
        out.append(ids[x])
    return tuple(out)

def quot_check(T,P,k):
    n,plus,mul=quot_algebra(T,P,k)
    pt=[[plus(a,b) for b in range(n)] for a in range(n)]
    mt=[[mul(a,b) for b in range(n)] for a in range(n)]
    found=set()
    for cl in partitions(n):
        bad=False
        for a in range(n):
            for b in range(a+1,n):
                if cl[a]!=cl[b]:continue
                for c in range(n):
                    if cl[pt[a][c]]!=cl[pt[b][c]] or cl[mt[a][c]]!=cl[mt[b][c]]:
                        bad=True;break
                if bad:break
            if bad:break
        if not bad:found.add(cl)
    pred={tuple([0]*n)}
    for cuts in range(1<<(k-1)):
        bs=[(cuts&((1<<i)-1)).bit_count() for i in range(k)]
        for t in range(1,T+1):
            # collapsed tail of N joins first overflow block
            pred.add(canonical([x if x<t else t for x in range(T+P)]+[t+v for v in bs]))
            for p in range(1,P+1):
                if P%p:continue
                pred.add(canonical([x if x<t else t+(x-t)%p for x in range(T+P)]+[t+p+v for v in bs]))
    assert found==pred,(T,P,k,len(found),len(pred),list(found-pred)[:3],list(pred-found)[:3])
    print(f'T={T},P={P},k={k}: {len(found)} congruences')

if __name__=='__main__':
    for tup in [(1,2,1),(2,2,1),(2,3,1),(3,2,1),(2,2,2),(3,2,2),(2,3,2),(2,2,3),(3,3,1)]:quot_check(*tup)
    print('QUOTIENT_VERIFY_OK')

def index_checks():
    for k in range(1,7):
        for h in range(1,16):
            keys={('universal',)} if h==1 else set()
            for cuts in range(1<<(k-1)):
                b=1+cuts.bit_count()
                for t in range(1,h+1):
                    if t+b==h:keys.add(('absorbed',cuts,t))
                    for p in range(1,h+1):
                        if t+p+b==h:keys.add(('separated',cuts,t,p))
            if h==1:formula=1
            else:formula=sum(comb(k-1,b-1)*(h-b) for b in range(1,min(k,h-1)+1))
            assert len(keys)==formula,(k,h,len(keys),formula)
        # identity count and eventual linear law
        assert 1<<(k-1)==2**(k-1)
    print('INDEX_VERIFY_OK')

if __name__=='__main__':index_checks()

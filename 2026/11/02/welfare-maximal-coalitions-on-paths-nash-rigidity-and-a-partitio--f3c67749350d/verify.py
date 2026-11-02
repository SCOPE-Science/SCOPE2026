from itertools import product
from math import comb

def compositions(n):
    if n==0:
        yield ()
    else:
        for j in range(1,n+1):
            for rest in compositions(n-j): yield (j,)+rest

def w(l,p,q):return 2*p*(l-1)-q*(l-1)*(l-2)
def sharp(n,p,q):
    v=[]
    for k in range(1,n+1):
        t,r=divmod(n,k)
        v.append(((k-r)*w(t,p,q)+r*w(t+1,p,q),k,comb(k,r)))
    W=max(z[0] for z in v)
    return W, sum(z[2] for z in v if z[0]==W)

def utility(v, coalition,p,q):
    C=sorted(coalition)
    if len(C)==1:return 0
    if any(b-a>1 for a,b in zip(C,C[1:])):return float('-inf')
    return sum(p if abs(w-v)==1 else -q for w in C if w!=v)

def partitions(n):
    def rec(j, blocks):
        if j==n:
            yield tuple(tuple(z) for z in blocks);return
        for k in range(len(blocks)):
            blocks[k].append(j)
            yield from rec(j+1,blocks)
            blocks[k].pop()
        blocks.append([j])
        yield from rec(j+1,blocks)
        blocks.pop()
    yield from rec(0,[])

def stable(P,p,q):
    for B in P:
        for v in B:
            u=utility(v,B,p,q)
            if u < 0:return False
            for C in P:
                if C is B:continue
                if utility(v,C+(v,),p,q)>u:return False
    return True

def run():
    checked=0;stable_checked=0;max_checks=0
    for n in range(2,9):
        ps=list(partitions(n))
        for p,q in product(range(1,6),range(1,5)):
            formula,num=sharp(n,p,q)
            valid=[]
            for P in ps:
                ww=sum(utility(v,B,p,q) for B in P for v in B)
                valid.append((ww,P))
                checked+=1
            best=max(v for v,_ in valid)
            opt=[P for v,P in valid if v==best]
            assert best==formula,(n,p,q,best,formula)
            assert len(opt)==num,(n,p,q,len(opt),num)
            for P in opt:
                assert stable(P,p,q),(n,p,q,P)
                stable_checked+=1
            max_checks+=1
    print('PASS',checked,'all-partition welfare comparisons,',stable_checked,'optimum Nash checks,',max_checks,'formula/count profiles')
    for L in range(2,7):
        p=L*(L+1)//2-1;q=1
        d=w(L,p,q)/L
        assert w(L+1,p,q)/(L+1)==d
        a=[0]*101;a[0]=1
        for n in range(1,101):a[n]=(a[n-L] if n>=L else 0)+(a[n-L-1] if n>=L+1 else 0)
        for n in range(L*(L-1),101):
            W,cnt=sharp(n,p,q)
            assert W==n*d and cnt==a[n],(L,n,W,cnt,a[n])
    print('PASS critical entropy formulas for 5 parameter choices, n up to 100')
if __name__=='__main__':run()

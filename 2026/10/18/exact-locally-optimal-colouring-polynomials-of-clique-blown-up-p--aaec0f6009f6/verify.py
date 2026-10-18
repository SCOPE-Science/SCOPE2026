"""Independent brute-force checks of locally-optimal colorings of clique blowups.
Only Python standard library is needed. Tested domains are finite; no infinite theorem is inferred.
"""
from itertools import product
from math import comb


def cycle_chromatic(r,q):
    assert r>=2
    return (q-1)**r + (-1)**r*(q-1)


def expected(n,s,q,kind):
    if kind=='path':
        if n==1:return q
        return sum(comb(n-r-1,r-1)*q*(q-1)**(r-1) for r in range(1,n//2+1))
    if kind=='cycle':
        assert n>=3
        total=q
        for r in range(2,n//2+1):
            num=n*comb(n-r-1,r-1)
            assert num%r==0
            total+=(num//r)*cycle_chromatic(r,q)
        return total
    raise ValueError(kind)


def graph_neighbors(n,s,kind):
    neighbors=[]
    for i in range(n):
        for a in range(s):
            nb=[]
            for j in range(n):
                if i==j:
                    nb.extend(j*s+b for b in range(s) if a!=b)
                elif (kind=='cycle' and ((i-j)%n in (1,n-1))) or (kind=='path' and abs(i-j)==1):
                    nb.extend(j*s+b for b in range(s))
            neighbors.append(tuple(nb))
    return neighbors


def brute(n,s,q,kind):
    neighbors=graph_neighbors(n,s,kind)
    total=0; checked=0
    for assignment in product(range(q),repeat=n*s):
        checked+=1
        valid=True
        for v,adj in enumerate(neighbors):
            counts=[0]*q
            for u in adj:
                counts[assignment[u]]+=1
            own=counts[assignment[v]]
            if any(count>=own for color,count in enumerate(counts) if color!=assignment[v]):
                valid=False
                break
        if valid:total+=1
    return total,checked


def main():
    cases=[]
    for kind in ('path','cycle'):
        lower=1 if kind=='path' else 3
        cases += [(kind,n,2,2) for n in range(lower,9)]
        cases += [(kind,n,2,3) for n in range(lower,7)]
        cases += [(kind,n,3,2) for n in range(lower,7)]
    assignments=0
    for kind,n,s,q in cases:
        actual,volume=brute(n,s,q,kind)
        predicted=expected(n,s,q,kind)
        assert actual==predicted,(kind,n,s,q,actual,predicted)
        assignments+=volume
        print('PASS kind=%s n=%d s=%d q=%d actual=%d expected=%d enumerated=%d'%(kind,n,s,q,actual,predicted,volume))
    print('SUCCESS cases=%d assignments=%d'%(len(cases),assignments))

if __name__=='__main__':main()

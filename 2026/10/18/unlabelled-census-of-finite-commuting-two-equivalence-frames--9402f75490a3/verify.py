from collections import Counter
from itertools import permutations,product
from functools import lru_cache
from fractions import Fraction
from math import gcd,lcm,factorial,comb

def partitions(n):
    def rec(k,blocks):
        if k==n:
            yield tuple(tuple(block) for block in blocks)
            return
        for i in range(len(blocks)):
            blocks[i].append(k)
            yield from rec(k+1,blocks)
            blocks[i].pop()
        blocks.append([k]);yield from rec(k+1,blocks);blocks.pop()
    yield from rec(0,[])

def classes(part,n):
    result=[0]*n
    for i,b in enumerate(part):
        for x in b:result[x]=i
    return tuple(result)

def commute(p,q):
    n=len(p)
    # relational products applied in both orders
    for x in range(n):
        for y in range(n):
            a=any(p[x]==p[k] and q[k]==q[y] for k in range(n))
            b=any(q[x]==q[k] and p[k]==p[y] for k in range(n))
            if a!=b: return False
    return True

@lru_cache(None)
def matrix_orbit(rows):
    r,s=len(rows),len(rows[0]);best=None
    for rp in permutations(range(r)):
        for cp in permutations(range(s)):
            arr=tuple(rows[i][j] for i in rp for j in cp)
            if best is None or arr<best:best=arr
    return r,s,best

def signature(p,q):
    n=len(p);E=sorted(set(p));F=sorted(set(q)); components=[]; unseen=set(range(n))
    while unseen:
        comp={next(iter(unseen))}; pending=list(comp)
        while pending:
            x=pending.pop()
            for y in list(unseen):
                if y not in comp and (p[x]==p[y] or q[x]==q[y]):
                    comp.add(y);pending.append(y)
        unseen-=comp
        rr=sorted({p[x] for x in comp});cc=sorted({q[x] for x in comp})
        rows=tuple(tuple(sum(p[x]==a and q[x]==b for x in comp) for b in cc) for a in rr)
        if any(z==0 for row in rows for z in row):raise AssertionError('nonrectangular commuting relation')
        components.append(matrix_orbit(rows))
    return tuple(sorted(components))

def exact_partitions(n, printout=False):
    P=list(partitions(n));labels=[classes(p,n) for p in P]
    sig=set();total=0
    for p in labels:
        for q in labels:
            if commute(p,q):
                sig.add(signature(p,q));total+=1
    if printout:print('label direct',n,total,len(sig),flush=True)
    return total,len(sig)

# Independent Burnside formula for unlabelled connected structures

def intparts(n,lo=1):
    if n==0:
        yield ()
        return
    for j in range(lo,n+1):
        for p in intparts(n-j,j):yield (j,)+p

def convolve(a,b,N):
    out=[Fraction(0)]*(N+1)
    for i,x in enumerate(a):
        if x:
            for j in range(N-i+1):out[i+j]+=x*b[j]
    return out

def closed_counts(N):
    ps={i:list(intparts(i)) for i in range(1,N+1)}
    def zpart(lam):
        return __import__('functools').reduce(lambda x,t:x*t**lam.count(t)*factorial(lam.count(t)),set(lam),1)
    con=[Fraction(0)]*(N+1)
    for r in range(1,N+1):
        for s in range(1,N//r+1):
            for lam in ps[r]:
                for mu in ps[s]:
                    poly=[Fraction(1)]+[Fraction(0)]*N
                    for a in lam:
                        for b in mu:
                            d=lcm(a,b);g=gcd(a,b)
                            orbit=[Fraction(0)]*(N+1)
                            for t in range(g,N//d+1):orbit[d*t]=comb(t-1,g-1)
                            poly=convolve(poly,orbit,N)
                    w=zpart(lam)*zpart(mu)
                    for j in range(1,N+1):con[j]+=poly[j]/w
    assert all(x.denominator==1 for x in con)
    connected=[int(x) for x in con]
    unlab=[1]+[0]*N
    for weight in range(1,N+1):
        step=[0]*(N+1)
        for k in range(0,N//weight+1):step[k*weight]=comb(connected[weight]+k-1,k)
        unlab=[sum(unlab[j]*step[i-j] for j in range(i+1)) for i in range(N+1)]
    return connected,unlab

if __name__=='__main__':
    c,u=closed_counts(11)
    assert c==[0,1,3,5,10,14,27,36,64,90,150,213],c
    assert u==[1,1,4,9,25,54,136,294,684,1476,3271,6958],u
    for n in range(1,7):
        labelled,unlabelled=exact_partitions(n,True)
        assert labelled==[0,1,4,19,117,864,7459][n],(n,labelled)
        assert unlabelled==u[n],(n,unlabelled,u[n])
    print('VERIFY_OK',flush=True)

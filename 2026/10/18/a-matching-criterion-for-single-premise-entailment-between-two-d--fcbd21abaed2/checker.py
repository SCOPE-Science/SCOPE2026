"""Finite constructive checks for two-disjunct FD entailment (no external dependencies)."""
from itertools import combinations
from random import Random
Q=3

def fd_imp(d,e):
    x,y=d; a,b=e
    return b==y and set(x)<=set(a)

def matching(src,dst):
    return ((fd_imp(src[0],dst[0]) and fd_imp(src[1],dst[1])) or
            (fd_imp(src[0],dst[1]) and fd_imp(src[1],dst[0])))

def holds(T,d):
    x,y=d; got={}
    for row in T:
        a=tuple(row[j] for j in x)
        if a in got and got[a]!=row[y]:return False
        got[a]=row[y]
    return True

def witness(src,dst,n):
    # each ordinary coordinate is (u,v) encoded as integer 3*u+v.
    from itertools import product
    universe=list(product(range(9),repeat=n-1))
    E=[[list(z[:j])+[None]+list(z[j:]) for z in universe] for j in range(n)]
    im=[[fd_imp(src[i],dst[j]) for j in range(2)] for i in range(2)]
    for i in range(2):
        if not any(im[i]):
            X,y=src[i];rows=[]
            for z in universe:
                r=list(z[:y])+[None]+list(z[y:])
                r[y]=sum(r[a]//3 for a in X)%3
                rows.append(tuple(r))
            return rows,('single',i)
    # No matching and neither row zero implies both rows match the same target.
    j=0 if all(im[i][0] for i in range(2)) else 1
    k=1-j
    A,b=dst[j];B,c=dst[k]
    rows=[]
    for i in range(2):
        X,y=src[i]
        assert y==b and set(X)<=set(A) and not im[i][k]
        for z in universe:
            r=list(z[:b])+[None]+list(z[b:])
            v=sum(r[a]//3 for a in X)%3 if c==b else 0
            r[b]=100+10*i+v
            rows.append(tuple(r))
    return rows,('double',j)

def density_check(rows,src,dst,case):
    assert not matching(src,dst)
    kind,j=case
    if kind=='single':
        assert holds(rows,src[j]);target_ids=[0,1]
        for a in target_ids:
            F=dst[a]; X,y=F; fibers={}
            for row in rows:
                key=tuple(row[x] for x in X)
                fibers.setdefault(key,{}).setdefault(row[y],0)
                fibers[key][row[y]]+=1
            maximum=sum(max(counts.values()) for counts in fibers.values())
            assert 3*maximum <=len(rows),(case,F,maximum,len(rows))
    else:
        t=dst[j];o=dst[1-j];s1=rows[:len(rows)//2];s2=rows[len(rows)//2:]
        assert holds(s1,src[0]) and holds(s2,src[1])
        for F,limit in [(t,2),(o,3)]:
            X,y=F;fibers={}
            for row in rows:
                key=tuple(row[x] for x in X)
                fibers.setdefault(key,{}).setdefault(row[y],0)
                fibers[key][row[y]]+=1
            maximum=sum(max(counts.values()) for counts in fibers.values())
            assert limit*maximum<=len(rows),(case,F,maximum,len(rows))

if __name__=='__main__':
    rng=Random(20261014)
    n=3;fds=[]
    for y in range(n):
        others=[i for i in range(n) if i!=y]
        for size in range(n):
            for X in combinations(others,size):fds.append((X,y))
    checks=0
    for _ in range(140):
        src=[rng.choice(fds) for _ in range(2)]
        dst=[rng.choice(fds) for _ in range(2)]
        if matching(src,dst):continue
        team,c=witness(src,dst,n)
        density_check(team,src,dst,c)
        checks+=1
    assert checks>80
    print('FD_MATCHING_WITNESSES_OK',checks)

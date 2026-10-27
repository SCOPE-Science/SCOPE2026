from functools import lru_cache
from itertools import combinations

def parts(n):
    if n==0:
        yield []
        return
    for P in parts(n-1):
        for j in range(len(P)):
            out=[set(b) for b in P]
            out[j].add(n-1)
            yield out
        yield [*map(set,P),{n-1}]

def conn_count(n):
    vals=[]
    pairs=list(combinations(range(n),2))
    for Q in range(1<<len(pairs)):
        parent=list(range(n))
        def root(i):
            while parent[i]!=i:i=parent[i]
            return i
        for ix,(u,v) in enumerate(pairs):
            if Q>>ix&1: parent[root(u)]=root(v)
        c=len({root(i) for i in range(n)})
        vals.append((Q,c))
    return vals

def formulas(n):
    vals=conn_count(n)
    A=sum(1<<(n*c) for _,c in vals)
    B=sum(1 << sum(len(b)*(len(b)-1)//2 for b in P) for P in parts(n))
    return A,B

for n in range(1,7):
    a,b=formulas(n)
    print('n',n,'A',a,'B',b,'A/2^n^2',float(a/(1<<(n*n))), 'B/2^N',float(b/(1<<(n*(n-1)//2))))

# Direct checks all pairs for n<=3, and equivalence R for n<=4
for n in range(1,4):
    pairs=list(combinations(range(n),2)); qlist=[(i,j) for i,j in pairs]
    a_direct=b_direct=0
    vals=conn_count(n)
    # all binary Rs, bit at coordinate (i,j)
    for q,_ in vals:
        Q={(i,i) for i in range(n)}|{v for k,e in enumerate(qlist) if q>>k&1 for v in (e,(e[1],e[0]))}
        for r in range(1<<(n*n)):
            R={(i,j) for i in range(n) for j in range(n) if r>>(i*n+j)&1}
            if all((v,t) in R for u,v in Q for t in range(n) if (u,t) in R):
                a_direct+=1
                if all((i,i) in R for i in range(n)) and all((j,i) in R for i,j in R) and all((i,k) in R for i,j in R for j2,k in R if j==j2):
                    b_direct+=1
    aa,bb=formulas(n)
    assert (a_direct,b_direct)==(aa,bb),(n,a_direct,b_direct,aa,bb)
    print('DIRECT_OK',n,a_direct,b_direct)
print('QUANTUM_MODAL_PAIR_ENUMERATION_OK')

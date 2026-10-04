from itertools import product

def greedy(f, N):
    g=2*f+3
    S=[f,g]
    forb=bytearray(2*N+5)
    forb[f+g]=1
    for x in range(g+1,N+1):
        if not forb[x]:
            for a in S:
                y=a+x
                if y<len(forb): forb[y]=1
            S.append(x)
    return set(S)

def predicted(f,N):
    M=5*f+5
    E={f}|set(range(2*f+3,3*f+3))
    R=set(range(f-2,f+1))|set(range(2*f+4,3*f+1))|set(range(4*f+3,4*f+7))
    T=set(E)
    for n in range(4*f+3,N+1):
        if n%M in R: T.add(n)
    T.discard(6*f+3)
    T.discard(11*f+8)
    T.add(8*f+6)
    return T

def checks(f):
    M=5*f+5
    E={f}|set(range(2*f+3,3*f+3))
    R=set(range(f-2,f+1))|set(range(2*f+4,3*f+1))|set(range(4*f+3,4*f+7))
    comp=set(range(M))-R
    ER={(e+r)%M for e in E for r in R}
    RR={(a+b)%M for a in R for b in R}
    assert ER==comp
    assert not (RR & R)
    d=(8*f+6)%M
    assert not ({(d+r)%M for r in R}&R)
    assert len(R)==f+4

cases=0
for f in range(6,201):
    N=20*(5*f+5)
    G=greedy(f,N)
    P=predicted(f,N)
    assert G==P, (f, sorted(G^P)[:10])
    checks(f)
    cases+=1
print(f"VERIFY_OK f_cases={cases} range=6..200 periods=20")

# Direct verification of structure constant N=4088 for fixed z, and C(z)-orbit count.
import json, itertools, math, time
N=12
def compose(a,b): return [b[a[i]] for i in range(len(a))]
def inv(a):
    b=[0]*len(a)
    for i,v in enumerate(a): b[v]=i
    return b
def ctype(p):
    s=[False]*N; t=[]
    for i in range(N):
        if not s[i]:
            j=i;c=[]
            while not s[j]: s[j]=True;c.append(j);j=p[j]
            if len(c)>1: t.append(len(c))
    t=sorted(t,reverse=True); t+=[1]*(N-sum(t)); return tuple(sorted(t,reverse=True))
d=json.load(open("triple.json"))
v0,v1,vinf=d["v0"],d["v1"],d["vinf"]
z=vinf; zinv=inv(z)
t0=time.time(); count=0; match=0; pairs=[]
pts=list(range(N))
for q4 in itertools.combinations(pts,4):
    q4s=set(q4); rest=[p for p in pts if p not in q4s]
    m=min(q4); others=[p for p in q4 if p!=m]
    for a,b,c in itertools.permutations(others):
        # build base 4-cycle images
        for q2 in itertools.combinations(rest,2):
            count+=1
            # x = 4-cycle (m a b c), transposition q2
            # y = x^{-1} z; check type (5,4,3) via quick parity/length? full ctype
            # x^{-1}: inverse images
            # compute y array directly:
            # x maps: m->a,a->b,b->c,c->m, q2 swap, else fix
            # xinverse maps: a->m,b->a,c->b,m->c, swap q2
            # y[i] = z[xinv[i]]
            xinv=list(range(N))
            xinv[a]=m; xinv[b]=a; xinv[c]=b; xinv[m]=c
            xinv[q2[0]]=q2[1]; xinv[q2[1]]=q2[0]
            y=[z[xinv[i]] for i in range(N)]
            if ctype(y)==(5,4,3):
                match+=1
                if len(pairs)<100000:
                    # store x compactly
                    x=list(range(N))
                    x[m]=a; x[a]=b; x[b]=c; x[c]=m
                    x[q2[0]]=q2[1]; x[q2[1]]=q2[0]
                    pairs.append((x,y))
print("enumerated:",count,"(expect 83160) matches:",match,"(expect 4088) time:",round(time.time()-t0,1))

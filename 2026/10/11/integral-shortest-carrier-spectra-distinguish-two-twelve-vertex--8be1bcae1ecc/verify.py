#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from math import gcd

CPPP = {
(1,2,3,4,5),(1,2,3,4,8),(1,2,3,5,8),(1,2,4,5,6),(1,2,4,6,7),(1,2,4,7,9),(1,2,4,8,9),
(1,2,5,6,8),(1,2,6,7,9),(1,2,6,8,9),(1,3,4,5,6),(1,3,4,6,7),(1,3,4,7,8),(1,3,5,6,11),
(1,3,5,7,8),(1,3,5,7,12),(1,3,5,11,12),(1,3,6,7,10),(1,3,6,10,11),(1,3,7,10,12),(1,3,9,10,11),
(1,3,9,10,12),(1,3,9,11,12),(1,4,7,8,9),(1,5,6,8,9),(1,5,6,9,10),(1,5,6,10,11),(1,5,7,8,9),
(1,5,7,9,11),(1,5,7,11,12),(1,5,9,10,11),(1,6,7,9,12),(1,6,7,10,12),(1,6,9,10,12),(1,7,9,11,12),
(2,3,4,5,9),(2,3,4,8,9),(2,3,5,7,8),(2,3,5,7,9),(2,3,6,7,8),(2,3,6,7,9),(2,3,6,8,9),
(2,4,5,6,7),(2,4,5,7,9),(2,5,6,7,8),(3,4,5,6,9),(3,4,6,7,8),(3,4,6,8,9),(3,5,6,9,12),
(3,5,6,11,12),(3,5,7,9,10),(3,5,7,10,12),(3,5,9,10,12),(3,6,7,9,11),(3,6,7,10,11),(3,6,9,11,12),
(3,7,9,10,11),(4,5,6,7,8),(4,5,6,8,9),(4,5,7,8,9),(5,6,9,10,12),(5,6,10,11,12),(5,7,9,10,11),
(5,7,10,11,12),(6,7,9,11,12),(6,7,10,11,12)
}
CPPM = {
(1,2,3,5,8),(1,2,3,5,11),(1,2,3,6,7),(1,2,3,6,12),(1,2,3,7,8),(1,2,3,11,12),
(1,2,4,7,8),(1,2,4,7,9),(1,2,4,8,9),(1,2,5,6,8),(1,2,5,6,10),(1,2,5,10,11),(1,2,6,7,9),
(1,2,6,8,9),(1,2,6,10,12),(1,2,10,11,12),(1,3,4,5,9),(1,3,4,5,10),(1,3,4,6,7),(1,3,4,6,11),
(1,3,4,7,8),(1,3,4,8,9),(1,3,4,10,11),(1,3,5,8,9),(1,3,5,10,11),(1,3,6,11,12),
(1,4,5,6,7),(1,4,5,6,12),(1,4,5,7,9),(1,4,5,10,12),(1,4,6,11,12),(1,4,10,11,12),
(1,5,6,7,9),(1,5,6,8,9),(1,5,6,10,12),(2,3,4,5,9),(2,3,4,5,12),(2,3,4,6,9),(2,3,4,6,10),
(2,3,4,10,12),(2,3,5,7,8),(2,3,5,7,9),(2,3,5,11,12),(2,3,6,7,9),(2,3,6,10,12),
(2,4,5,6,8),(2,4,5,6,11),(2,4,5,7,8),(2,4,5,7,9),(2,4,5,11,12),(2,4,6,8,9),(2,4,6,10,11),
(2,4,10,11,12),(2,5,6,10,11),(3,4,5,10,12),(3,4,6,7,8),(3,4,6,8,9),(3,4,6,10,11),
(3,5,6,10,11),(3,5,6,10,12),(3,5,6,11,12),(3,5,7,8,9),(3,6,7,8,9),(4,5,6,7,8),
(4,5,6,11,12),(5,6,7,8,9)
}

def faces(F,k):
    return sorted({tuple(c) for f in F for c in combinations(f,k)})

def reduce_units(A, track_qinv=False, track_p=False):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if m else 0
    Qinv=[[int(i==j) for j in range(n)] for i in range(n)] if track_qinv else None
    P=[[int(i==j) for j in range(m)] for i in range(m)] if track_p else None
    k=0
    while k<min(m,n):
        pos=None
        for i in range(k,m):
            for j in range(k,n):
                if abs(A[i][j])==1:
                    pos=(i,j); break
            if pos is not None: break
        if pos is None: break
        i,j=pos
        if i!=k:
            A[k],A[i]=A[i],A[k]
            if P is not None: P[k],P[i]=P[i],P[k]
        if j!=k:
            for row in A: row[k],row[j]=row[j],row[k]
            if Qinv is not None: Qinv[k],Qinv[j]=Qinv[j],Qinv[k]
        if A[k][k]==-1:
            A[k]=[-x for x in A[k]]
            if P is not None: P[k]=[-x for x in P[k]]
        for i2 in range(m):
            if i2!=k and A[i2][k]:
                q=A[i2][k]
                A[i2]=[x-q*y for x,y in zip(A[i2],A[k])]
                if P is not None:
                    P[i2]=[x-q*y for x,y in zip(P[i2],P[k])]
        for j2 in range(n):
            if j2!=k and A[k][j2]:
                q=A[k][j2]
                for i2 in range(m):
                    A[i2][j2]-=q*A[i2][k]
                if Qinv is not None:
                    Qinv[k]=[x+q*y for x,y in zip(Qinv[k],Qinv[j2])]
        k+=1
    return k,A,Qinv,P

def matvec(M,x):
    return [sum(a*b for a,b in zip(row,x)) for row in M]

def canon(v):
    for x in v:
        if x<0: return tuple(-z for z in v)
        if x>0: return tuple(v)
    return tuple(v)

def analyze(F):
    V=tuple(range(1,13))
    E,T,Q=faces(F,2),faces(F,3),faces(F,4)
    assert (len(V),len(E),len(T),len(Q),len(F))==(12,57,148,165,66)
    EI={e:i for i,e in enumerate(E)}
    TI={t:i for i,t in enumerate(T)}

    d2=[[0]*len(T) for _ in E]
    for j,(a,b,c) in enumerate(T):
        for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
            d2[EI[e]][j]=s
    r2,D2,Qinv,_=reduce_units(d2,track_qinv=True)
    assert r2==46
    assert all(D2[i][j]==(1 if i==j and i<46 else 0)
               for i in range(len(D2)) for j in range(len(D2[0])))

    d3cols=[]
    for a,b,c,d in Q:
        x=[0]*len(T)
        for t,s in [((b,c,d),1),((a,c,d),-1),((a,b,d),1),((a,b,c),-1)]:
            x[TI[t]]=s
        y=matvec(Qinv,x)
        assert all(v==0 for v in y[:r2])
        d3cols.append(y[r2:])

    kdim=len(T)-r2
    H=[[d3cols[j][i] for j in range(len(Q))] for i in range(kdim)]
    r3,D3,_,P=reduce_units(H,track_p=True)
    assert r3==100 and kdim-r3==2
    assert all(D3[i][j]==(1 if i==j and i<100 else 0)
               for i in range(len(D3)) for j in range(len(D3[0])))

    def coords(x):
        y=matvec(Qinv,x)
        assert all(v==0 for v in y[:r2])
        w=matvec(P,y[r2:])
        return tuple(w[r3:])

    carriers=[]
    for S in combinations(V,4):
        tris=list(combinations(S,3))
        if not all(t in TI for t in tris):
            continue
        a,b,c,d=S
        x=[0]*len(T)
        for t,s in [((b,c,d),1),((a,c,d),-1),((a,b,d),1),((a,b,c),-1)]:
            x[TI[t]]=s
        co=coords(x)
        if S in Q:
            assert co==(0,0)
        else:
            carriers.append((S,co))
    assert len(carriers)==72
    assert all(c!=(0,0) for _,c in carriers)
    assert all(gcd(abs(c[0]),abs(c[1]))==1 for _,c in carriers)

    integral=Counter(canon(c) for _,c in carriers)
    mod2=Counter((c[0]%2,c[1]%2) for _,c in carriers)
    reps={}
    for S,c in carriers:
        reps.setdefault(canon(c),S)
    return integral,mod2,reps

a,a2,ra=analyze(CPPP)
b,b2,rb=analyze(CPPM)

assert a==Counter({(1,0):33,(0,1):33,(1,-1):3,(1,1):3})
assert b==Counter({(1,0):33,(0,1):33,(1,1):6})
assert a2==Counter({(1,0):33,(0,1):33,(1,1):6})
assert b2==Counter({(1,0):33,(0,1):33,(1,1):6})
assert ra[(1,0)]==(1,2,3,6)
assert ra[(1,-1)]==(1,2,3,9)
assert ra[(0,1)]==(1,3,5,9)
assert ra[(1,1)]==(5,6,7,10)
assert rb[(1,0)]==(1,2,3,4)
assert rb[(0,1)]==(1,2,3,10)
assert rb[(1,1)]==(1,2,4,10)

print(
    "VERIFY_OK f_both=12,57,148,165,66 H2_Z=Z^2 "
    "min_vertex_support=4 carriers=72_each all_primitive=yes "
    "integral_spectra=33,33,3,3|33,33,6 "
    "mod2_spectra=33,33,6|33,33,6 "
    "reps_pp=1236|1359|1239|56710 reps_pm=1234|12310|12410"
)

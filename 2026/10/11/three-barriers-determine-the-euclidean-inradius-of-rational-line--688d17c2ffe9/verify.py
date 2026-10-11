#!/usr/bin/env python3
import itertools, math

def solve(A,b,eps=1e-11):
    n=len(A)
    M=[list(map(float,A[i]))+[float(b[i])] for i in range(n)]
    for c in range(n):
        p=max(range(c,n), key=lambda i:abs(M[i][c]))
        if abs(M[p][c])<eps:
            return None
        M[c],M[p]=M[p],M[c]
        z=M[c][c]
        M[c]=[x/z for x in M[c]]
        for i in range(n):
            if i==c: continue
            z=M[i][c]
            if abs(z)>eps:
                M[i]=[M[i][j]-z*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def closed(a,ap,b,bp,d,l):
    A=a+d*b
    Ap=ap+d*bp
    DA=A-Ap
    Db=b-bp
    NA=math.sqrt(1+d*d+DA*DA)
    Nb=math.sqrt(1+Db*Db)
    return min(
        l/2,
        b*l/(1+Db+Nb),
        A*l/(1+d+DA+NA)
    )

def brute(a,ap,b,bp,d,l):
    A0=a+d*b
    Ap0=ap+d*bp
    DA=A0-Ap0
    Db=b-bp
    NA=math.sqrt(1+d*d+DA*DA)
    Nb=math.sqrt(1+Db*Db)

    # Variables are s,t,v,r.  Each row encodes lhs >= rhs.
    rows=[
        ([1,0,0,-1],0),                 # s-r >=0
        ([0,1,0,-1],0),                 # t-r >=0
        ([0,0,1,-1],0),                 # v-r >=0
        ([0,0,-1,-1],-l),               # l-v-r >=0
        ([-1,-d,-DA,-NA],-A0*l),        # Al-s-dt-DAv-NA r >=0
        ([0,-1,-Db,-Nb],-b*l),          # bl-t-Dbv-Nb r >=0
        ([0,0,0,1],0),                  # r>=0
    ]
    best=-1.0
    for act in itertools.combinations(range(len(rows)),4):
        M=[rows[i][0] for i in act]
        rhs=[rows[i][1] for i in act]
        x=solve(M,rhs)
        if x is None:
            continue
        if all(sum(c*z for c,z in zip(row,x)) >= rr-2e-9
               for row,rr in rows):
            best=max(best,x[3])
    return best

cases=0
for a in range(1,5):
    for ap in range(1,a+1):
        for b in range(1,5):
            for bp in range(1,b+1):
                for d in range(0,4):
                    for l in (1,2,3):
                        r1=closed(a,ap,b,bp,d,l)
                        r2=brute(a,ap,b,bp,d,l)
                        assert r2>=0
                        assert abs(r1-r2) <= 2e-8*max(1.0,r1), (a,ap,b,bp,d,l,r1,r2)
                        A=a+d*b
                        Ap=ap+d*bp
                        DA=A-Ap
                        Db=b-bp
                        NA=math.sqrt(1+d*d+DA*DA)
                        Nb=math.sqrt(1+Db*Db)
                        # Canonical center (r,r,r) satisfies all shifted clearances.
                        assert l-r1 >= r1-1e-10
                        assert b*l-(1+Db)*r1 >= r1*Nb-1e-10
                        assert A*l-(1+d+DA)*r1 >= r1*NA-1e-10
                        cases+=1

print(f"VERIFY_OK staged-tree-prismatoid-inradius cases={cases} active_set_lp=yes")

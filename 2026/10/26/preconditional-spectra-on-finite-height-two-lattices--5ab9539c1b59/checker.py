#!/usr/bin/env python3
"""Direct finite-domain evaluation of Holliday's five preconditional axioms."""
from itertools import product
from math import factorial

def counts(m):
    n=m+2; hi=n-1
    def le(a,b): return a==b or a==0 or b==hi
    def meet(a,b): return a if le(a,b) else b if le(b,a) else 0
    out=[0,0,0]
    for d in range(n):
        choices=[]
        for a in range(1,m+1):
            options=[]
            for c in range(n):
                for t in (a,hi):
                    row=[c if (x==0 or (1<=x<=m and x!=a)) else t for x in range(n)]
                    if all(le(meet(a,b),row[b]) and le(row[b],row[meet(a,b)]) for b in range(n)) and all(not le(b,v) or le(row[b],row[v]) for b in range(n) for v in range(n)):
                        options.append(row)
            choices.append(options)
        for rows in product(*choices):
            f=[[d]*n]+list(rows)+[list(range(n))]
            p1=all(le(f[hi][a],a) for a in range(n))
            p2=all(le(meet(a,b),f[a][b]) for a in range(n) for b in range(n))
            p3=all(le(f[a][b],f[a][meet(a,b)]) for a in range(n) for b in range(n))
            p4=all(le(f[a][meet(b,c)],f[a][b]) for a in range(n) for b in range(n) for c in range(n))
            p5=all(le(f[a][f[meet(a,b)][c]],f[meet(a,b)][c]) for a in range(n) for b in range(n) for c in range(n))
            if not all((p1,p2,p3,p4,p5)): continue
            out[0]+=1
            if all(f[a][a]==hi and meet(a,f[a][0])==0 for a in range(n)):
                out[1]+=1
                if all(le(a,f[f[a][0]][0]) for a in range(n)):
                    out[2]+=1
    return out

def expected(m):
    k=(m+3)**m +2**m+2*m*3**(m-1)
    t=m**m
    f=sum(factorial(m)//(2**j*factorial(j)*factorial(m-2*j)) for j in range(m//2+1))
    return [k,t,f]

if __name__=='__main__':
    for m in (2,3,4):
        actual=counts(m)
        exp=expected(m)
        assert actual==exp,(m,actual,exp)
        print('m=',m,'K,T,F:',actual)

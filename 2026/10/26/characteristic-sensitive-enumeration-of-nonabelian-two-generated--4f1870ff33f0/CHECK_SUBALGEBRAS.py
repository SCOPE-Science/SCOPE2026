#!/usr/bin/env python3
from collections import defaultdict,Counter
from itertools import product
from itertools import product

def bracket(x,y,q):
 a,b,c,d,e,f=x; A,B,C,D,E,F=y
 return (0,0,0,(a*B-b*A)%q,(b*C-c*B)%q,(a*E-e*A+d*C-c*D)%q)

def rref(rows,q):
    rows=[list(row) for row in rows]
    i=0;res=[]
    for j in range(6):
        k=next((k for k in range(i,len(rows)) if rows[k][j]%q),None)
        if k is None: continue
        rows[i],rows[k]=rows[k],rows[i]
        inv=pow(rows[i][j]%q,-1,q)
        rows[i]=[(x*inv)%q for x in rows[i]]
        for k in range(len(rows)):
            if k!=i and rows[k][j]%q:
                c=rows[k][j]
                rows[k]=[(u-c*v)%q for u,v in zip(rows[k],rows[i])]
        res.append(tuple(rows[i]));i+=1
    return tuple(tuple(row) for row in rows[:i])

def run(q):
    seen={}
    E=tuple(product(range(q),repeat=6))
    for x in E:
        for y in E:
            c=bracket(x,y,q)
            d=bracket(x,c,q)
            e=bracket(y,c,q)
            sub=rref([x,y,c,d,e],q)
            if sub not in seen:
                seen[sub]='filiform' if len(sub)==4 else 'Heisenberg' if len(sub)==3 else 'abelian'
    out=Counter((len(k),v) for k,v in seen.items())
    L=q*q+q+1
    H=(q+1 if q%2==0 else 2)
    K=L-1-H
    expected={(0,'abelian'):1,(1,'abelian'):(q**6-1)//(q-1), (2,'abelian'):2*q**5+3*q**4+2*q**3+2*q*q+q+1,(3,'Heisenberg'):(H+2)*q**4,(4,'filiform'):K*q*q}
    assert dict(out)==expected, (q,out,expected)
    print('SUBALGEBRAS EXHAUSTIVE',q,dict(sorted(out.items())))
run(2)
run(3)
print('N4_SUBALGEBRA_CLASSIFICATION_OK')

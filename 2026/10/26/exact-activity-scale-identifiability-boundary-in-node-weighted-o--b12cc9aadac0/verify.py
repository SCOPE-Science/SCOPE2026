"""Exact arithmetic checks for bipartite node-weight interaction laws.
Run with Python 3 standard library: python verify.py
The full theorems follow from the supplied algebraic proof, not enumeration.
"""
from fractions import Fraction as F
from itertools import combinations


def connected(A, B, edges):
    vertices=set(A)|set(B)
    found={next(iter(vertices))}
    while True:
        nxt=found|{y for x,y in edges if x in found}|{x for x,y in edges if y in found}
        if nxt==found:
            return nxt==vertices
        found=nxt


def laws(A,B,edges,w):
    assert all(w[i]>0 for i in A+B)
    WA=sum(w[i] for i in A); WB=sum(w[j] for j in B)
    NA={i:[j for j in B if (i,j) in edges] for i in A}
    NB={j:[i for i in A if (i,j) in edges] for j in B}
    assert all(NA.values()) and all(NB.values())
    QA={ (i,j): w[i]/WA*w[j]/sum(w[k] for k in NA[i]) for i,j in edges }
    QB={ (i,j): w[j]/WB*w[i]/sum(w[k] for k in NB[j]) for i,j in edges }
    P={(i,j): w[i]/(WA+WB)*w[j]/sum(w[k] for k in NA[i])+w[j]/(WA+WB)*w[i]/sum(w[k] for k in NB[j]) for i,j in edges}
    assert sum(QA.values())==sum(QB.values())==sum(P.values())==1
    assert all(P[e]==WA/(WA+WB)*QA[e]+WB/(WA+WB)*QB[e] for e in edges)
    return QA,QB,P

def tv(P,Q):
    return sum(abs(P[e]-Q[e]) for e in P)/2

checks=0
for na in range(1,7):
    for nb in range(1,7-na):
        A=tuple(range(na));B=tuple(range(na,na+nb))
        potential=tuple((i,j) for i in A for j in B)
        for mask in range(1,1<<len(potential)):
            edges=tuple(e for h,e in enumerate(potential) if (mask>>h)&1)
            if not connected(A,B,edges): continue
            w={v:F(1) for v in A+B}
            qa,qb,p=laws(A,B,edges,w)
            full=len(edges)==len(potential)
            if full:
                assert qa==qb
                for i,j in edges:
                    assert p[(i,j)]==w[i]*w[j]/(sum(w[x] for x in A)*sum(w[y] for y in B))
                checks+=len(edges)
            else:
                # A vertex i and B vertex j with no edge provide a finite
                # exact witness using B weights 1 and 2; the algebraic proof
                # covers arbitrary positive weights.
                missing=next((i,j) for i,j in potential if (i,j) not in edges)
                j=missing[1]
                w2=dict(w);w2[j]=F(2)
                qa2,qb2,p2=laws(A,B,edges,w2)
                assert qa!=qb or qa2!=qb2
                checks+=1

A=(0,2);B=(1,3); E=((0,1),(2,1),(2,3)); w={i:F(1) for i in range(4)}
qa,qb,p=laws(A,B,E,w)
w3={0:F(3),1:F(1),2:F(3),3:F(1)}
_,_,p3=laws(A,B,E,w3)
assert [p[e] for e in E]==[F(3,8),F(1,4),F(3,8)]
assert [p3[e] for e in E]==[F(7,16),F(1,4),F(5,16)]
assert tv(p,p3)==F(1,16)
assert tv(qa,qb)==F(1,4)
checks+=5

A=(0,2,4);B=(1,3,5);E=((0,1),(0,5),(2,1),(2,3),(4,3),(4,5))
_,_,p=laws(A,B,E,{v:F(1) for v in A+B})
_,_,p7=laws(A,B,E,{v:(F(7) if v in A else F(1)) for v in A+B})
assert p==p7=={e:F(1,6) for e in E}
checks+=6

A=(0,1,2);B=(3,4,5,6);E=tuple((i,j) for i in A for j in B)
w={0:F(2),1:F(3),2:F(5),3:F(7),4:F(11),5:F(13),6:F(17)}
_,_,p=laws(A,B,E,w)
w7={v:w[v]*(F(7) if v in A else F(1)) for v in A+B}
_,_,p7=laws(A,B,E,w7)
assert p==p7
assert all(p[(i,j)]==w[i]*w[j]/(F(10)*F(48)) for i,j in E)
checks+=12
print(f'CERTIFICATE_OK: {checks} exact graph/edge checks across connected bipartite graphs up to six vertices plus examples')

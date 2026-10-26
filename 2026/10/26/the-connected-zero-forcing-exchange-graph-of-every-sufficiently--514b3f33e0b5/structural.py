#!/usr/bin/env python3
"""Independent orbit construction and local 3-overlap adjacency verification."""
from collections import Counter
import sys

def representatives(n):
    u=lambda i:i%n
    v=lambda i:n+i%n
    return {'A':frozenset((u(0),u(1),u(2),u(3))),
            'B':frozenset((u(0),u(1),u(2),v(0))),
            'C':frozenset((u(0),u(1),v(0),v(1))),
            'D':frozenset((u(0),u(1),v(1),v(2)))}

def orbit(n,seed):
    result=set()
    for shift in range(n):
      for reflection in (-1,1):
       for swap in (0,1):
        result.add(frozenset((((x//n)^swap)*n+((reflection*(x%n)+shift)%n)) for x in seed))
    return result

def check(n):
    reps=representatives(n);classes={k:orbit(n,rep) for k,rep in reps.items()}
    assert {k:len(v) for k,v in classes.items()}=={'A':2*n,'B':4*n,'C':n,'D':2*n}
    allsets=set().union(*classes.values())
    assert len(allsets)==9*n
    expected={'A':{'A':2,'B':4},'B':{'A':2,'B':1,'C':1,'D':2},
              'C':{'B':4,'D':4},'D':{'B':4,'C':2}}
    byset={s:k for k,part in classes.items() for s in part}
    for typ,rep in reps.items():
        count=Counter(byset[t] for t in allsets if len(t&rep)==3)
        assert dict(count)==expected[typ],(n,typ,count)
    # Independent direct local forcing check for each representative.
    adj=[]
    for r in range(2):
      for i in range(n):adj.append((r*n+(i-1)%n,r*n+(i+1)%n,(1-r)*n+i))
    for rep in reps.values():
        blue=set(rep)
        while True:
            delta={w[0] for v in blue if len(w:=[x for x in adj[v] if x not in blue])==1}
            if not delta:break
            blue|=delta
        assert len(blue)==2*n,(n,rep)
    return n,len(allsets),28*n
if __name__=='__main__':
 for n in range(6,int(sys.argv[1])+1):print(check(n))

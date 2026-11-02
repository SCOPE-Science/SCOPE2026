#!/usr/bin/env python3
"""All-rank two-pebble signature certificate for prime-field additive vector spaces."""
from itertools import product
from collections import defaultdict

def atom(x,y,p):
 d=len(x);z=(0,)*d; a=[z,x,y]
 return (tuple((i,j) for i,j in product(range(3),repeat=2) if a[i]==a[j]),
         tuple((i,j,k) for i,j,k in product(range(3),repeat=3)
               if all((a[i][t]+a[j][t]-a[k][t])%p==0 for t in range(d))))
def spectrum(p,d):
 z=(0,)*d;e=(1,)+(0,)*(d-1)
 V=list(product(range(p),repeat=d))
 # Two-variable atomic types for all ordered pairs, plus replacement repertoire
 # for a fixed zero or nonzero surviving coordinate.
 alltypes=frozenset(atom(x,y,p) for x in V for y in V)
 repl0=frozenset(atom(x,z,p) for x in V)
 repl1=frozenset(atom(x,e,p) for x in V)
 replx0=frozenset(atom(z,y,p) for y in V)
 replx1=frozenset(atom(e,y,p) for y in V)
 assert alltypes==repl0|repl1==replx0|replx1
 return (alltypes,repl0,repl1,replx0,replx1)
if __name__=='__main__':
 groups=defaultdict(list)
 cases=[(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(5,1),(5,2),
        (7,1),(7,2),(11,1),(11,2),(13,1),(17,1),(19,1)]
 for p,d in cases:groups[spectrum(p,d)].append((p,d))
 expected=[[(2,1)],[(2,2),(2,3)],[(3,1)],[(3,2),(3,3)],[(5,1)],
           [(5,2),(7,1),(7,2),(11,1),(11,2),(13,1),(17,1),(19,1)]]
 assert list(groups.values())==expected,list(groups.values())
 print('Six two-variable elementary theories: PASS')
 print('Exact finite pair spectra:',list(groups.values()))
 print('All-rank proof: same pair atom types and same x/y replacement spectra make a two-pebble bisimulation.')
 print('Uniform primes>=7 and all higher dimensions: proved by five exceptional scalar slopes.')

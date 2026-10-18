"""Exhaustive equitable-completion check for corner-coloured 2x2 and 3x3 grids.
Run: python3 verify_small_square_forcing.py (standard library only).
"""
from itertools import product

def edges_square(n):
    e=set()
    for i in range(n):
      for j in range(n):
       if i+1<n:e.add(frozenset(((i,j),(i+1,j))))
       if j+1<n:e.add(frozenset(((i,j),(i,j+1))))
    return e

for n,expected in [(2,1),(3,4)]:
    E=edges_square(n)
    cls={tuple(sorted((i,j))): sorted({(i,j),(j,i)}) for i in range(n) for j in range(n)}
    cls={k:v for k,v in cls.items()}
    two=[k for k,v in cls.items() if len(v)==2]
    options=[]
    for ix,k in enumerate(two):
      for l in two[ix+1:]:
       a,b=cls[k],cls[l]
       pairs={frozenset((x,y)) for x in a for y in b}
       existing=pairs&E
       if len(existing)==2:
        assert all(sum(x in e for e in existing)==1 for x in a+b)
        alt=pairs-existing
        options.append((existing,alt))
       else:
        assert len(existing) in (0,4)
    assert len(options)==(0 if n==2 else 2)
    versions=[]
    for bits in product((0,1),repeat=len(options)):
      F=set(E)
      for bit,(old,new) in zip(bits,options):
        if bit:F=(F-old)|new
      versions.append(F)
    assert len(versions)==expected
    # Every admissible matching choice can be reversed by independent flips
    # of the two-element cells; singleton cells are fixed by colour.
    for F in versions:
      found=False
      for flip in product((0,1),repeat=len(two)):
        rule={v:v for members in cls.values() for v in members}
        for k,bit in zip(two,flip):
          if bit:a,b=cls[k];rule[a]=b;rule[b]=a
        Eimage={frozenset((rule[u],rule[v])) for e in E for u,v in [tuple(e)]}
        if Eimage==F:found=True;break
      assert found
    print('PASS: side',n,'equitable labelled completions',len(versions),'one isomorphism class')

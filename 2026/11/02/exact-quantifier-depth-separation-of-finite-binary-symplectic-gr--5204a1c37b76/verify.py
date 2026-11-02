#!/usr/bin/env python3
"""Standalone finite-graph calculation of binary symplectic graph FO ranks <=4.
Only checks finite representatives; the infinite theorem has a separate proof.
"""
from itertools import product

def symp(x,y,d):
    return sum((((x>>(2*i))&1)*((y>>(2*i+1))&1)+((x>>(2*i+1))&1)*((y>>(2*i))&1)) for i in range(d)) & 1

def graph(d):
    v=list(range(1,1<<(2*d)))
    a={x:0 for x in v}
    for x in v:
        mask=0
        for y in v:
            if symp(x,y,d): mask|=1<<y
        a[x]=mask
    return v,a

def atom(t,A):
    return tuple(2 if x==y else (1 if A[x]>>y&1 else 0)
                 for i,x in enumerate(t) for y in t[i+1:])

def calc(d):
    V,A=graph(d)
    S={}
    full=sum(1<<x for x in V)
    # Cache membership of extension patterns for length-3 tuples.
    T3={}
    for x in V:
      ax=A[x]
      for y in V:
       ay=A[y]
       for z in V:
        az=A[z]
        fresh=full & ~(1<<x) & ~(1<<y) & ~(1<<z)
        support=0
        for i in range(8):
          mask=fresh
          mask &= (ax if (i&1) else full^ax)
          mask &= (ay if (i&2) else full^ay)
          mask &= (az if (i&4) else full^az)
          if mask: support|=1<<i
        T3[x,y,z]=(atom((x,y,z),A),support)
    # Relative depth 2 for pairs: all third-element one-extension types.
    T2={}
    for x in V:
      for y in V:
        T2[x,y]=(atom((x,y),A),frozenset(T3[x,y,z] for z in V))
    # Relative depth 3 for singleton vertices.
    T1={x:((),frozenset(T2[x,y] for y in V)) for x in V}
    return dict(order=len(V),rank2=frozenset(((),frozenset(atom((x,y),A) for y in V)) for x in V),
                rank3=frozenset(((),frozenset((atom((x,y),A),frozenset(atom((x,y,z),A) for z in V)) for y in V)) for x in V),
                rank4=frozenset(T1.values()), T3_count=len(set(T3.values())),
                T2_count=len(set(T2.values())))

def claw(d):
    V,A=graph(d)
    for w in V:
      ns=[v for v in V if A[w]>>v&1]
      for i,x in enumerate(ns):
        for j in range(i+1,len(ns)):
          y=ns[j]
          if A[x]>>y&1:continue
          for z in ns[j+1:]:
            if not A[x]>>z&1 and not A[y]>>z&1:
              return (w,x,y,z)
    return None

def main():
    results={}
    for d in (1,2,3):
      r=calc(d)
      results[d]=r
      print(f'SYMPLECTIC_GRAPH d={d} vertices={r["order"]} triple_extension_types={r["T3_count"]} pair_depth2_types={r["T2_count"]} claw={claw(d)}')
    for q in (2,3,4):
      bits=[int(results[i][f'rank{q}']==results[j][f'rank{q}']) for i,j in ((1,2),(2,3))]
      print(f'RANK{q}_EQUIV (d1,d2)={bits[0]} (d2,d3)={bits[1]}')
      assert bits==({2:[0,1],3:[0,1],4:[0,0]}[q])
    assert claw(2) is None and claw(3) is not None
    print('VERIFY_OK')

if __name__=='__main__':main()

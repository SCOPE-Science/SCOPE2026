#!/usr/bin/env python3
"""Independent enumerations and Euler-transform checks for unlabeled permissible transformation pairs."""
import itertools,math

def mul(A,B,N):
  C=[0]*(N+1)
  for i,a in enumerate(A):
    if not a: continue
    for j,b in enumerate(B[:N+1-i]):
      if b: C[i+j]+=a*b
  return C

def factors(exponents,N):
  a=[0]*(N+1);a[0]=1
  for d in range(1,N+1):
    for rep in range(exponents(d)):
      for k in range(d,N+1): a[k]+=a[k-d]
  return a

def euler_transform(b,N):
  out=[0]*(N+1);out[0]=1
  for n in range(1,N+1):
    out[n]=sum(out[n-k]*sum(d*b[d] for d in range(1,k+1) if k%d==0) for k in range(1,n+1))//n
    assert n*out[n] == sum(out[n-k]*sum(d*b[d] for d in range(1,k+1) if k%d==0) for k in range(1,n+1))
  return out

def generate(N):
  U=[0]+[1]*N
  P=factors(lambda d:1,N)
  H=factors(lambda d:d//2,N)
  R0=mul(U,P,N)
  R=mul(R0,H,N)
  A=euler_transform(R,N); A0=euler_transform(R0,N)
  return {'all':A,'no2':A0,'rank3':[a-b for a,b in zip(A,A0)],'root_fiber':R,'root_fiber_no2':R0}

def pair_orbits(n):
  elems=range(n)
  pairs=set()
  for t in itertools.product(elems,repeat=n):
    tt=tuple(t[t[i]] for i in elems)
    if any(t[tt[i]]!=t[i] for i in elems):continue
    fixed=[i for i in elems if t[i]==i]
    if not fixed:continue
    # each t-component is represented by its attractor (singleton or paired roots)
    comps={}
    for i in elems:
      c=tuple(sorted((tt[i],t[i])))
      comps.setdefault(c,[]).append(i)
    for r in range(1,len(fixed)+1):
      for R in itertools.combinations(fixed,r):
        # e must fix red roots; all others have chosen an image root
        other=[c for c in comps if not any(j in R for j in c)]
        forced={c:c[0] for c in comps if any(j in R for j in c)}
        for assignment in itertools.product(R,repeat=len(other)):
          m=dict(forced)
          m.update(zip(other,assignment))
          e=tuple(m[tuple(sorted((tt[i],t[i])))] for i in elems)
          if len(set(e)) != len(R):
            print('bad assignment')
            raise Exception()
          pairs.add((t,e))
  def swap_pair(x,i):
    t,e=x; j=i+1
    def sw(k):return j if k==i else i if k==j else k
    return tuple(sw(t[sw(k)]) for k in elems),tuple(sw(e[sw(k)]) for k in elems)
  orbits=[0,0,0,0]
  while pairs:
    seed=pairs.pop()
    seen={seed};q=[seed]
    for item in q:
      for i in range(n-1):
        nxt=swap_pair(item,i)
        if nxt not in seen:
          seen.add(nxt);q.append(nxt)
    pairs.difference_update(seen)
    t,e=seed
    rank=len({t,tuple(t[t[k]] for k in elems),e})
    orbits[rank]+=1
  return orbits

if __name__=='__main__':
  g=generate(15)
  for k,v in g.items():print(k,v[:13])
  for n in range(1,6):
    oc=pair_orbits(n)
    print('n',n,'orbits by rank',oc,'GF r3',g['rank3'][n], 'GF r<=2',g['no2'][n])
    assert oc[3]==g['rank3'][n] and oc[1]+oc[2]==g['no2'][n]
  print('VERIFY_OK')

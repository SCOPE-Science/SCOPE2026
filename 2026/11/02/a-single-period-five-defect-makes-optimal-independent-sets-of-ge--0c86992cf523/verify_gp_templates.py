"""Independent bitset checker using the actual graph's 3n edges.
Checks template maximality, all one-for-one exchanges, and the exact cycle
edges, with no use of the symbolic dynamic programming verifier.
"""
from itertools import combinations

def graph(n):
    e=[]
    for i in range(n):
      e.extend(((i,(i+1)%n),(n+i,n+(i+2)%n),(i,n+i)))
    assert len(set(tuple(sorted(pair)) for pair in e))==3*n
    adj=[0]*(2*n)
    for a,b in e:adj[a]|=1<<b;adj[b]|=1<<a
    return adj

def encode(n,seq):
    return sum(1<<(j if x==1 else n+j) for j,x in enumerate(seq) if x)

def independent(mask,adj):
    return all(not(mask & (1<<i) and mask & adj[i]) for i in range(len(adj)))

def shifted(n,seq,i):
    return tuple(seq[(j-i)%n] for j in range(n))

def templates(n):
    if n%5==0:
      return {('frozen',i):encode(n,shifted(n,(0,1,2,2,1)*(n//5),i)) for i in range(5)}
    assert n%5==4
    ans={}
    for label,short in [('alpha',(1,2,1)),('beta',(1,2,2)),('gamma',(2,2,1))]:
      word=(0,)+short+(0,1,2,2,1)*((n-4)//5)
      for i in range(n):ans[label,i]=encode(n,shifted(n,word,i))
    return ans

def replacement_neighbors(mask,adj):
    candidates=[];nverts=len(adj)
    for i in range(nverts):
      if not mask>>i&1:continue
      reduced=mask & ~(1<<i)
      for j in range(nverts):
        if mask>>j&1:continue
        if reduced & adj[j]:continue
        candidates.append(reduced|(1<<j))
    assert len(candidates)==len(set(candidates))
    return set(candidates)

def check(n):
    adj=graph(n);states=templates(n)
    assert len(set(states.values()))==len(states)
    assert all(independent(m,adj) for m in states.values())
    assert all(m.bit_count()==4*n//5 for m in states.values())
    reverse={mask:key for key,mask in states.items()}
    expected={key:set() for key in states}
    if n%5==4:
      for i in range(n):
        a=('alpha',i);b=('beta',i);c=('gamma',i);d=('gamma',(i+5)%n)
        for x,y in ((a,b),(a,c),(b,d)):
          expected[x].add(y);expected[y].add(x)
    for key,mask in states.items():
      neighbors=replacement_neighbors(mask,adj)
      assert neighbors.issubset(reverse),(n,key,'other_maximum_candidate')
      assert {reverse[z] for z in neighbors}==expected[key],(n,key)
    if n%5==4:
      assert set(len(v) for v in expected.values())=={2}
      seen=set();todo=[('alpha',0)]
      while todo:
        x=todo.pop()
        if x in seen:continue
        seen.add(x);todo+=list(expected[x]-seen)
      assert len(seen)==3*n
    return len(states),sum(map(len,expected.values()))//2

def brute_small(n):
    adj=graph(n);required=4*n//5
    actual=set()
    for choice in combinations(range(2*n),required):
      mask=sum(1<<i for i in choice)
      if independent(mask,adj):actual.add(mask)
    assert actual==set(templates(n).values())
    print('DIRECT_COMBINATIONS_PASS',n,len(actual),flush=True)

if __name__=='__main__':
    for n in (5,9,10):brute_small(n)
    for n in range(5,100):
      if n%5 not in (0,4):continue
      a,b=check(n)
      print('BITSET',n,a,b,flush=True)
    print('INDEPENDENT_GRAPH_BITSET_EXCHANGE_CHECK_PASS')

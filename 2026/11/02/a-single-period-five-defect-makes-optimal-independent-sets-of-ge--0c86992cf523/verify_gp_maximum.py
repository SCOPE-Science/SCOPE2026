"""Independent finite enumeration of maximum stable sets in GP(n,2).
Pure standard-library verifier for n=5,9,10,14,19,24.
"""
from functools import lru_cache
from collections import Counter,deque

def independent(seq):
    n=len(seq)
    return all(not (seq[i]==seq[(i+1)%n]==1 or seq[i]==seq[(i+2)%n]==2) for i in range(n))

def enumerate_maximum(n):
    # Dynamic programming by the last two column symbols, with all boundary
    # constraints checked at termination. Unlike the template verifier, this
    # enumerates every optimal word from the local graph constraints.
    answer=[]; optimum=-10**6
    for a in range(3):
      for b in range(3):
        if a==b==1:continue
        @lru_cache(None)
        def score(i,previous,before_previous):
          if i==n:
            return 0 if previous!=a or a!=1 else -10**6
          best=-10**6
          for x in range(3):
            if x==previous==1 or x==before_previous==2:continue
            if i==n-1 and (x==a==1 or x==b==2):continue
            if i==n-2 and x==a==2:continue
            best=max(best,int(x>0)+score(i+1,x,previous))
          return best
        total=int(a>0)+int(b>0)+score(2,b,a)
        if total<optimum:continue
        current=[]
        def recover(i,p,q,word):
          if i==n:
            if score(i,p,q)==0:current.append(tuple(word))
            return
          best=score(i,p,q)
          for x in range(3):
            if x==p==1 or x==q==2:continue
            if i==n-1 and (x==a==1 or x==b==2):continue
            if i==n-2 and x==a==2:continue
            if int(x>0)+score(i+1,x,p)==best:
              recover(i+1,x,p,word+[x])
        recover(2,b,a,[a,b])
        if total>optimum:optimum=total;answer=current
        else:answer+=current
    assert len(answer)==len(set(answer))
    for word in answer:
      assert independent(word)
      assert sum(x!=0 for x in word)==optimum
    return optimum,set(answer)

def families(n):
    if n%5==0:
      return {tuple((0,1,2,2,1)[(j-t)%5] for j in range(n)) for t in range(5)}
    assert n%5==4
    k=(n-4)//5
    words=[]
    for short in ((1,2,1),(1,2,2),(2,2,1)):
      base=(0,)+short+(0,1,2,2,1)*k
      assert len(base)==n
      for i in range(n):words.append(tuple(base[(j-i)%n] for j in range(n)))
    assert len(set(words))==3*n
    return set(words)

def graph_edges(ss):
    seq=list(ss);where={x:i for i,x in enumerate(seq)}
    edges=set()
    for i,a in enumerate(seq):
      for j,x in enumerate(a):
        if not x:continue
        for h,y in enumerate(a):
          for z in (1,2):
            if h==j:
              if z==x:continue
            elif y:continue
            b=list(a);b[j]=0;b[h]=z
            ii=where.get(tuple(b))
            if ii is not None and i!=ii:edges.add(tuple(sorted((i,ii))))
    return edges,seq

def expected_edges(n,seq):
    where={x:i for i,x in enumerate(seq)}
    k=(n-4)//5
    shifts={}
    for t,short in enumerate(((1,2,1),(1,2,2),(2,2,1))):
      base=(0,)+short+(0,1,2,2,1)*k
      for i in range(n):shifts[t,i]=where[tuple(base[(j-i)%n] for j in range(n))]
    result=set()
    for i in range(n):
      for a,b in [((0,i),(1,i)),((0,i),(2,i)),((1,i),(2,(i+5)%n))]:
        result.add(tuple(sorted((shifts[a],shifts[b]))))
    return result

def main():
  for n in (5,9,10,14,15,19,20,24):
    m,computed=enumerate_maximum(n)
    assert m==4*n//5
    assert computed==families(n),(n,len(computed),len(families(n)))
    edges,seq=graph_edges(computed)
    if n%5==0:assert not edges
    else:
      assert edges==expected_edges(n,seq)
      adj=[[] for _ in seq]
      for i,j in edges:adj[i].append(j);adj[j].append(i)
      assert set(map(len,adj))=={2}
      seen={0};todo=[0]
      while todo:
        for h in adj[todo.pop()]:
          if h not in seen:seen.add(h);todo.append(h)
      assert len(seen)==len(seq)
    print('OK',n,m,len(computed),len(edges),flush=True)
  print('DP_ENUMERATION_AND_ALL_EXCHANGES_PASS')
if __name__=='__main__': main()

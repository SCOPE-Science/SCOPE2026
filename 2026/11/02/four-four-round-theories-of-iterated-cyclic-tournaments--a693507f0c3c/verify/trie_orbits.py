from collections import defaultdict
from functools import lru_cache
import sys

def analyze(h,Q=5):
  size=3**h
  digits=[[v//(3**(h-1-i))%3 for i in range(h)] for v in range(size)]
  @lru_cache(maxsize=None)
  def orbit(vs):
    def go(I,depth):
      if depth==h:return I
      children=[]
      for d in range(3):
        children.append(go(tuple(i for i in I if digits[vs[i]][depth]==d),depth+1))
      a,b,c=children
      return min((a,b,c),(b,c,a),(c,a,b))
    return go(tuple(range(len(vs))),0)
  nodes=[]; edges=[]
  states={orbit(()) : ()}
  nodes.append(states)
  for r in range(Q):
    next_states={}; ed={}
    for code,vs in states.items():
      near=set()
      for v in range(size):
        ww=vs+(v,)
        cc=orbit(ww)
        near.add(cc)
        if cc not in next_states:next_states[cc]=ww
      ed[code]=near
    edges.append(ed);states=next_states;nodes.append(states)
    print('h',h,'r',r+1,'orbits',len(states),flush=True)
  # terminal rank-zero atomic diagrams
  sig=[{} for _ in range(Q+1)]
  for code,vs in nodes[Q].items():
    mat=[]
    for i in range(Q):
      for j in range(i+1,Q):
        if vs[i]==vs[j]:mat.append(0)
        else:
          k=next(k for k in range(h) if digits[vs[i]][k]!=digits[vs[j]][k])
          mat.append(1 if (digits[vs[j]][k]-digits[vs[i]][k])%3==1 else 2)
    sig[Q][code]=tuple(mat)
  for r in range(Q-1,-1,-1):
    for code,vs in nodes[r].items():
      mat=[]
      for i in range(r):
        for j in range(i+1,r):
          if vs[i]==vs[j]:mat.append(0)
          else:
            k=next(k for k in range(h) if digits[vs[i]][k]!=digits[vs[j]][k])
            mat.append(1 if (digits[vs[j]][k]-digits[vs[i]][k])%3==1 else 2)
      sig[r][code]=(tuple(mat),frozenset(sig[r+1][cc] for cc in edges[r][code]))
  return sig[0][orbit(())], [len(node) for node in nodes]
if __name__=='__main__':
  Q=int(sys.argv[1]) if len(sys.argv)>1 else 4
  hmax=int(sys.argv[2]) if len(sys.argv)>2 else 5
  ranks=[]
  for h in range(1,hmax+1):
   s,c=analyze(h,Q);ranks.append(s)
  for i,s in enumerate(ranks):print('h',i+1,'class',ranks.index(s)+1,flush=True)

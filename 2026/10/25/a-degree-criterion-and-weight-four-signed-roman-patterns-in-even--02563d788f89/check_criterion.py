from itertools import combinations
from random import Random

def criterion(n, H_A, H_B):
 a=n//2-1;b=n-a
 da=[sum(v in e for e in H_A) for v in range(a)]
 db=[sum(v in e for e in H_B) for v in range(a,n)]
 t=len(H_A)+len(H_B);T=2-n//2+t
 dmax=max(da)+max(db)
 if T < 1+dmax or t <= dmax:return False
 for u,v in combinations(range(a),2):
  if T+8-da[u]-da[v]+2*int((u,v) in H_A)<1:return False
 for u,v in combinations(range(a,n),2):
  if T-db[u-a]-db[v-a]+2*int((u,v) in H_B)<1:return False
 return True

def direct(n,H_A,H_B):
 a=n//2-1
 edges=list(combinations(range(n),2))
 f={e: (2 if e in H_A or e in H_B else (1 if (e[0]<a)==(e[1]<a) else -1)) for e in edges}
 for edge,v in f.items():
  if v+sum(w for e,w in f.items() if not set(e)&set(edge))<1:return False
  if v==-1 and not any(w==2 and not set(e)&set(edge) for e,w in f.items()):return False
 return True

def run():
 count=0
 for n in [6,8]:
  a=n//2-1
  inner=[e for e in combinations(range(n),2) if (e[0]<a)==(e[1]<a)]
  for mask in range(1<<len(inner)):
   HA={e for j,e in enumerate(inner) if (mask>>j)&1 and e[0]<a}
   HB={e for j,e in enumerate(inner) if (mask>>j)&1 and e[0]>=a}
   assert criterion(n,HA,HB)==direct(n,HA,HB),(n,mask)
   count+=1
 print('PASS structural criterion, exhaustively',count,'candidate internal subgraphs on n=6,8')
 rnd=Random(20261019)
 n=12;a=n//2-1
 inner=[e for e in combinations(range(n),2) if (e[0]<a)==(e[1]<a)]
 for i in range(300):
  chosen={e for e in inner if rnd.randrange(2)}
  HA={e for e in chosen if e[0]<a};HB=chosen-HA
  assert criterion(n,HA,HB)==direct(n,HA,HB)
 print('PASS structural criterion, 300 randomized profiles on n=12')
if __name__=='__main__':run()

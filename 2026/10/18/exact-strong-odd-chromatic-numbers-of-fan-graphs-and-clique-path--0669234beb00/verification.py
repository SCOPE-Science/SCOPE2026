from collections import defaultdict
from functools import lru_cache

TEMPLATES={
 1:'0',2:'01',3:'012',4:'0123',5:'01234',6:'012345',
 7:'0120340',8:'01201301',12:'012013023123'
}

def expected(n):
 if 1<=n<=6:return n
 r=n%6
 return 3 if r==3 else 4 if r in (0,2,4) else 5

def word(n):
 if n<=8:return TEMPLATES[n]
 r=n%6
 bases={0:12,1:7,2:8,3:3,4:4,5:5}
 b=bases[r]
 return '012012'*((n-b)//6)+TEMPLATES[b]

def valid_word(s,require_all_odd=True):
 if any(s[i]==s[j] for i in range(len(s)) for j in range(i+1,min(len(s),i+3))):return False
 if require_all_odd and any(s.count(c)%2 !=1 for c in set(s)):return False
 return True

def dp(n,k):
 states={(-1,-1,0):1}
 for _ in range(n):
  next_states=defaultdict(int)
  for (a,b,mask),v in states.items():
   for c in range(k):
    if c!=a and c!=b:
     next_states[b,c,mask^(1<<c)]+=v
  states=next_states
 return sum(v for (a,b,mask),v in states.items() if mask == (1<<k)-1)

def brute_partitions(n):
 # Canonically label colors in order of first appearance; verify original fan graph neighborhoods.
 result={}
 def walk(prefix,k):
  i=len(prefix)
  if i==n:
   if any(sum(x==c for x in prefix)%2==0 for c in range(k)):return
   # Actual graph check at every vertex, with hub color k.
   graph=[set() for _ in range(n+1)]
   for p in range(n):
    graph[n].add(p);graph[p].add(n)
    if p+1<n:
     graph[p].add(p+1);graph[p+1].add(p)
   colors=prefix+[k]
   for v in range(n+1):
    if any(sum(colors[u]==c for u in graph[v])%2==0
           for c in {colors[u] for u in graph[v]}):return
    if any(colors[v]==colors[u] for u in graph[v]):return
   result[k]=result.get(k,0)+1
   return
  for c in range(k+1):
   if i>=1 and c==prefix[-1]:continue
   if i>=2 and c==prefix[-2]:continue
   walk(prefix+[c],max(k,c+1))
 walk([],0)
 return result

if __name__=='__main__':
 for n in range(1,201):
  w=word(n)
  assert len(w)==n and valid_word(w) and len(set(w))==expected(n), (n,w)
 print('Templates and length-six insertion checked: all n=1..200')
 for n in range(1,81):
  ks=[k for k in range(1,7) if dp(n,k)]
  assert min(ks)==expected(n),(n,ks)
 print('Parity dynamic programming: exact minima n=1..80, palette at most 6')
 for n in range(1,13):
  b=brute_partitions(n)
  assert min(b)==expected(n),(n,b)
  print('n',n,'minimum',min(b),'unlabelled optimal partitions',b[min(b)])
 print('Independent direct-neighborhood graph enumeration: n=1..12')

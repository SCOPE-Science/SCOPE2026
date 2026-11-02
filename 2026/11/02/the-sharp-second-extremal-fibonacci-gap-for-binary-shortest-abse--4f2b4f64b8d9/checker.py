"""Independent checks of the Fibonacci second-extremal statement."""
from itertools import product
from collections import Counter

def fib(n):
 a,b=0,1
 for _ in range(n):a,b=b,a+b
 return a

def seq_count(s):
 # First-available greedy subsequence automaton: d(i), c(i) on suffixes.
 n=len(s)
 nxt=[[n,n] for _ in range(n+1)]
 for i in range(n-1,-1,-1):
  nxt[i]=nxt[i+1][:]; nxt[i][int(s[i])]=i
 d=[1]*(n+1); c=[2]*(n+1)
 for i in range(n-1,-1,-1):
  opts=[(1 if pos==n else 1+d[pos+1],1 if pos==n else c[pos+1]) for pos in nxt[i]]
  d[i]=min(x[0] for x in opts)
  c[i]=sum(nc for lv,nc in opts if lv==d[i])
 return d[0],c[0]

def rec_count(bits):
 m=len(bits)
 E=[0]*(m+1); O=[0]*m
 E[m]=2; O[m-1]=1; E[m-1]=3
 for j in range(m-2,-1,-1):
  O[j]=O[j+1] if bits[j]==bits[j+1] else E[j+2]
  E[j]=E[j+1]+O[j]
 return E[0]

def short_absent(s):
 # independent check via explicit enumeration, used only at tiny lengths
 l,c=seq_count(s)
 if l>11:return None
 def is_sub(u):
  it=iter(s)
  return all(any(v==a for v in it) for a in u)
 return sum(not is_sub(''.join(bits)) for bits in product('01',repeat=l))

for m in range(2,12):
 results=[]
 for bits in product('01',repeat=m):
  bits=''.join(bits)
  s=''.join('01' if b=='0' else '10' for b in bits)
  ell,c=seq_count(s)
  assert ell==m+1
  assert c==rec_count(bits),(m,bits,c,rec_count(bits))
  if m<=5:
   assert c==short_absent(s)
  results.append((c,bits))
 top=sorted(set(v for v,p in results),reverse=True)
 predicted=fib(m+3)-fib(m-2)
 if m>=5:
  runner=[bits for c,bits in results if c==predicted]
  assert top[:2]==[fib(m+3),predicted],(m,top[:2])
  assert len(runner)==4,(m,runner)
  assert all(sum(bits[j]==bits[j+1] for j in range(m-1))==1 for bits in runner)
 print('paired',m,'top',top[:3],'runner_count',sum(c==predicted for c,p in results) if m>=5 else '-',flush=True)

for m in range(5,10):
 hist=Counter()
 for bits in product('01',repeat=2*m):
  c=seq_count(''.join(bits))[1]
  hist[c]+=1
 t=sorted(hist,reverse=True)
 assert t[:2]==[fib(m+3),fib(m+3)-fib(m-2)],(m,t[:5])
 assert hist[t[0]]==2 and hist[t[1]]==4,(m,hist[t[0]],hist[t[1]])
 print('all_binary',2*m,'top',t[:3],'multiplicities',[hist[v] for v in t[:3]],flush=True)
print('ALL_CHECKS_PASS')

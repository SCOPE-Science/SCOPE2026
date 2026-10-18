from collections import defaultdict

def count(n):
 D={(0,-1):1}; end=0
 for i in range(n):
  Q=defaultdict(int)
  for (prevmin,M),w in D.items():
   end+=w # choose empty row; all following empty
   for s in range(1,1<<n):
    m=(s&-s).bit_length()-1
    if m<prevmin:continue
    T=M
    if s: T=max(M,s.bit_length()-1)
    if (((1<<(T+1))-1)&~(s|((1<<(M+1))-1) if M>=0 else s))!=0:continue
    Q[m,T]+=w
  D=Q
 return end+sum(D.values())

def direct(n):
 # tests FS1 and FS2 using straightforward pair relation compositions
 full=0
 for code in range(1<<(n*n)):
  rows=[(code>>(n*i))&((1<<n)-1) for i in range(n)]
  fs1=all(not(rows[j]&(1<<k)) or any(rows[i]&(1<<ell) for ell in range(k+1)) for i in range(n) for j in range(i,n) for k in range(n))
  if not fs1:continue
  fs2=all(not(rows[i]&(1<<j)) or any(rows[ell]&(1<<k) for ell in range(i+1)) for i in range(n) for j in range(n) for k in range(j+1))
  if fs2:full+=1
 return full
if __name__=='__main__':
 for n in range(1,9):
  v=count(n); print(n,v,'direct' if n<=4 else '',direct(n) if n<=4 else '', flush=True)

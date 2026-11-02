from collections import deque
def trans(p):
    n=3*p
    a=list(range(n)); b=list(range(n))
    for j in range(1,p):
        u,v=2*j-1,2*j; a[u]=v; a[v]=u
    a[2*p-1]=2*p; a[2*p]=2*p+1; a[2*p+1]=3
    for u in range(2*p+2,n-1,2): a[u]=u+1; a[u+1]=u
    for j in range(p):
        u,v=2*j,2*j+1; b[u]=v; b[v]=u
    b[2*p]=2
    for u in range(2*p+1,n-1,2): b[u]=u+1; b[u+1]=u
    return a,b
import sys,time

def go(p):
 aa,bb=trans(p); n=len(aa); full=(1<<n)-1
 def apply(S,T):
  R=0
  while S:
   u=S&-S;R|=1<<T[u.bit_length()-1];S^=u
  return R
 Q=deque([full]); data={full:(0,1)}; found=-1; total=0; terminal={};edges=0
 while Q:
  S=Q.popleft();d,cnt=data[S]
  if found>=0 and d>=found: break
  for T in (aa,bb):
   R=apply(S,T);edges+=1
   if R not in data:
    data[R]=(d+1,cnt);Q.append(R)
   else:
    prev,count=data[R]
    assert prev<=d+1
    if prev==d+1:data[R]=(prev,count+cnt)
   if R.bit_count()==1:
    found=d+1
    terminal[R]=data[R][1]
 return found,sum(terminal.values()),len(data),edges, {x.bit_length()-1:c for x,c in terminal.items()}
if __name__=='__main__':
 for p in range(3,int(sys.argv[1])+1):
  t=time.time();r=go(p);print(p,r,'secs',round(time.time()-t,3),flush=True)

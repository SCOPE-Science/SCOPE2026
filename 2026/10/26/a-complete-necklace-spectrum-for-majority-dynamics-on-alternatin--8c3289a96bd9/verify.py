"""Standalone reproducibility checks for periodically switching cubic-graph majority dynamics.
Checks small-state exhaustivity and symbolic recurrence formulas; uses no dependencies.
"""
from math import gcd
from collections import defaultdict

def make(n,phase):
    # n is half the number of two-vertex clusters.
    assert n>=2 and phase in (0,1)
    cl=2*n; N=2*cl
    edges=set()
    def link(j,k,a,b):
        u=2*(j%cl)+a; v=2*(k%cl)+b
        assert u!=v
        edges.add(tuple(sorted((u,v))))
    for j in range(0,cl,2):
        # phase 0: dense (j,j+1) and sparse (j-1,j).
        # phase 1: sparse (j,j+1) and dense (j-1,j).
        for a in (0,1):
            for b in (0,1):
                if phase==0: link(j,j+1,a,b)
                else: link(j-1,j,a,b)
            if phase==0:link(j-1,j,a,a)
            else:link(j,j+1,a,a)
    adj=[[] for _ in range(N)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    assert all(len(v)==3 for v in adj)
    seen={0};todo=[0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen: seen.add(v); todo.append(v)
    assert len(seen)==N
    return adj

def upd(x,adj):
    o=0
    for i,js in enumerate(adj):
        if sum((x>>j)&1 for j in js)>=2:o|=1<<i
    return o

def mvec(x,n):
    return [((x>>(2*j))^(x>>(2*j+1)))&1 for j in range(2*n)]

def recurrent(x,n):
    p=mvec(x,n)
    return all(p[i]==p[0] for i in range(0,2*n,2)) and all(p[i]==p[1] for i in range(1,2*n,2))

def macro_payload(m,pattern,n):
    # two bits for each cluster, pattern (mixed-even,mixed-odd)
    return sum(((m>>j)&1) << (2*j) | (((m>>j)&1)^pattern[j%2]) << (2*j+1) for j in range(2*n))

def mobius(d):
    p=0;x=d
    for k in range(2,d+1):
        if k*k>x:break
        if x%k==0:
            x//=k;p+=1
            if x%k==0:return 0
            while x%k==0: x//=k
    if x>1:p+=1
    return (-1)**p

def longest_cyclic_ones(word, n):
    if word == (1<<n)-1: return 0
    return max(sum((word>>((j+k)%n))&1 for k in range(n) if all((word>>((j+r)%n))&1 for r in range(k+1))) for j in range(n))

def tau_formula(x,n):
    M=mvec(x,n)
    E=sum(M[2*j]<<j for j in range(n))
    O=sum(M[2*j+1]<<j for j in range(n))
    return max(longest_cyclic_ones(E,n),longest_cyclic_ones(O,n))

def bcount(n,t):
    return sum(longest_cyclic_ones(w,n)<=t for w in range(1<<n))

def matrix_power_trace_no_run(n,t):
    # Count non-all-one labelled cyclic words without 1^(t+1).
    s=t+1
    T=[[0]*s for _ in range(s)]
    for j in range(s):
        T[j][0]+=1
        if j<t:T[j][j+1]+=1
    def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(s)) for j in range(s)] for i in range(s)]
    P=[[int(i==j) for j in range(s)] for i in range(s)]
    for _ in range(n):P=mm(P,T)
    return sum(P[j][j] for j in range(s))

def main():
  tested=0
  for n in range(2,5):
    A=make(n,0);B=make(n,1)
    nbits=4*n; M=(1<<nbits)
    # Validate graph-isomorphism under cyclic shifting of clusters.
    for i in range(nbits):
      aa=set((v+2)%nbits for v in A[i])
      bb=set(B[(i+2)%nbits])
      assert aa==bb,(n,i,aa,bb)
    cnt=defaultdict(int);depth=defaultdict(int)
    for x in range(M):
      cur=x;t=0
      while not recurrent(cur,n):
        cur=upd(cur,A if t%2==0 else B);t+=1
        assert t<=n-1,(n,x,t)
      depth[t]+=1
      assert t==tau_formula(x,n),(n,x,t,tau_formula(x,n))
      if recurrent(x,n):
        cnt['recur']+=1
        y=x
        for k in range(1,n+1):
          y=upd(upd(y,A),B)
          if y==x:
            cnt[k]+=1;break
        else:assert False
      tested+=1
    assert cnt['recur']==4**(n+1),(n,cnt)
    assert max(depth)==n-1,(n,depth)
    for t in range(n):
       b=bcount(n,t)
       assert b==1+matrix_power_trace_no_run(n,t),(n,t,b)
       assert sum(v for k,v in depth.items() if k<=t)==(1<<(2*n))*b*b,(n,t,b,depth)
    for d in range(1,n+1):
      if n%d==0:
        fixed=4*(4**gcd(n,d))
        actual=sum(v for k,v in cnt.items() if isinstance(k,int) and d%k==0)
        assert actual==fixed,(n,d,actual,fixed,cnt)
    print('EXHAUSTIVE',n,'states',M,'recurrent',cnt['recur'],'primitive-period-count',dict(cnt),'transient-depths',dict(depth))
  # Structural checks for all recurrent templates, including larger rings.
  for n in range(2,9):
    A=make(n,0);B=make(n,1)
    for pattern in [(0,0),(1,1),(0,1),(1,0)]:
      for payload in range(1<<min(2*n,12)):
        x=macro_payload(payload,pattern,n)
        assert recurrent(x,n)
        y=upd(x,A);z=upd(y,B)
        assert recurrent(y,n) and recurrent(z,n)
        # Exact double-step return upper bound, even beyond exhaustive 2^12 payloads.
        w=x
        for _ in range(n):w=upd(upd(w,A),B)
        assert w==x,(n,pattern,payload)
    print('TEMPLATE',n,'patterns',4,'payloads per pattern',1<<min(2*n,12))
  print('VERIFY_OK',tested)
if __name__=='__main__':main()

"""Exact finite checks for the complete-multipartite parity automaton theorem.
Pure Python 3 standard library, no external data.  Run: python verify.py
"""
from itertools import product

def graph(part_sizes):
    N=sum(part_sizes)
    groups=[]
    for i,n in enumerate(part_sizes):groups.extend([i]*n)
    rows=[]
    for i in range(N):
        rows.append(sum(1<<j for j in range(N) if groups[j]!=groups[i]))
    return rows

def bitrank(rows,N):
    a=rows[:];rank=0
    for j in range(N):
        idx=next((h for h in range(rank,N) if a[h]>>j&1),None)
        if idx is None:continue
        a[rank],a[idx]=a[idx],a[rank]
        for h in range(N):
            if h!=rank and a[h]>>j&1:a[h]^=a[rank]
        rank+=1
    return rank

def compose(A,B):
    return [__import__('functools').reduce(int.__xor__,(B[j] for j in range(len(B)) if row>>j&1),0) for row in A]

def upd(A,x,include_self):
    return sum(((x&row).bit_count()%2 ^ ((x>>i)&1 if include_self else 0))<<i for i,row in enumerate(A))

def verify():
    checked=0;cases=0
    for r in range(2,7):
      for part in product((1,2,3),repeat=r):
        N=sum(part)
        if N>10:continue
        A=graph(part);I=[1<<i for i in range(N)]
        A2=compose(A,A);A3=compose(A2,A);A4=compose(A3,A)
        k=sum(n%2 for n in part);e=r-k
        r1=r if r%2==0 else r-1
        r2=k if k%2==0 or e>0 else k-1
        r3=k if k%2==0 else k-1
        assert bitrank(A,N)==r1
        assert bitrank(A2,N)==r2
        assert bitrank(A3,N)==r3
        checked+=3
        assert (A4==A2 if k%2==0 else A4==A3)
        checked+=1
        for self_term in (0,1):
          B=[row^(1<<i if self_term else 0) for i,row in enumerate(A)]
          counts={1:0,2:0,4:0}
          for x in range(1<<N):
            y=x;tracks={0:x}
            for t in range(1,9):
              y=upd(A,y,self_term)
              if t in counts and y==x:counts[t]+=1
              tracks[t]=y
            if self_term:
              if k%2==0:assert tracks[4]==tracks[2]
              else:assert tracks[5]==tracks[1]
            else:
              if k%2==0:assert tracks[4]==tracks[2]
              else:assert tracks[4]==tracks[3]
            checked+=1
          if not self_term:
             s1=1 if k==0 else 2**(k-1)
             s2=2**(k if k%2==0 else max(0,k-1))
             s4=s2
          else:
             s1=2**(N-r1)
             s2=2**(N-r2)
             s4=2**(N-r3)
          assert (counts[1],counts[2],counts[4])==(s1,s2,s4),(part,self_term,counts,(s1,s2,s4))
          assert counts[1]<=counts[2]<=counts[4]
          assert (counts[2]-counts[1])%2==0
          assert (counts[4]-counts[2])%4==0
          checked+=4
        cases+=1
    print('VERIFY_OK', 'graphs=',cases,' assertions=',checked)

if __name__=='__main__':verify()

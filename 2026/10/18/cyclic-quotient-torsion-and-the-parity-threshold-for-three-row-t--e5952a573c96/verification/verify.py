"""Independent modular homology checks of an odd-column cyclic quotient.
Pure Python; fixed finite n=5 computation is an experiment, not the infinite proof.
"""
from collections import defaultdict
from itertools import combinations
from math import comb

def faces(n):
    ss=[()]+[(i,) for i in range(n)]+list(combinations(range(n),2))
    for A in ss:
      for B in ss:
        for C in ss:
          if set(A)&set(B)&set(C): continue
          yield tuple(sorted((i*n+j for i,R in enumerate((A,B,C)) for j in R)))
def shift(face,n,t):return tuple(sorted((v//n)*n+(v%n+t)%n for v in face))
def canonical(f,n):return min(shift(f,n,t) for t in range(n))
def sign_to_canonical(f,n,can):
    for t in range(n):
        seq=[(v//n)*n+(v%n+t)%n for v in f]
        if tuple(sorted(seq))==can:
            inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
            return (-1)**inv
    raise ValueError

def sparse_rank(columns,p):
    piv={}; rank=0
    for col in columns:
        d={i:(v%p) for i,v in col.items() if v%p}
        while d:
            i=max(d)
            if i not in piv:
                a=pow(d[i],-1,p); piv[i]={j:(c*a)%p for j,c in d.items()};rank+=1;break
            factor=d[i]; v=piv[i]
            for j,c in v.items():
                d[j]=(d.get(j,0)-factor*c)%p
                if d[j]==0:del d[j]
    return rank

def test(n):
    listing=list(faces(n)); levels=defaultdict(list)
    for f in listing:
       if f and f==canonical(f,n): levels[len(f)-1].append(f)
    levels={k:sorted(v) for k,v in levels.items()}
    assert 1+sum(len(levels[d]) for d in levels)*n==len(listing)
    for t in range(1,n):
      assert all(shift(f,n,t)!=f for f in listing if f)
    idx={k:{f:i for i,f in enumerate(levels[k])} for k in levels}
    bounds={}
    for k in sorted(levels):
      if k==0:continue
      columns=[]
      for face in levels[k]:
        d=defaultdict(int)
        for j in range(len(face)):
          f=face[:j]+face[j+1:]
          canon=canonical(f,n)
          d[idx[k-1][canon]]+=(-1)**j*sign_to_canonical(f,n,canon)
        columns.append(dict(d))
      bounds[k]=columns
    # Exact cellular differential-square check over the integers.
    for k in sorted(bounds):
      if k<2:continue
      for col in bounds[k]:
        dd=defaultdict(int)
        for mid,coeff in col.items():
          for lower,c in bounds[k-1][mid].items(): dd[lower]+=coeff*c
        assert all(v==0 for v in dd.values()), (n,k,dd)
    print('PASS: integer quotient boundary square is zero in every degree.')
    for p in (2,5,7):
      ranks={k:sparse_rank(cols,p) for k,cols in bounds.items()}
      bet={k:len(levels[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in levels}
      assert bet[0]==1 and bet[1]==(1 if p==5 else 0) and bet[2]==(1 if p==5 else 0) and bet[3]==(1 if p==5 else 0) and bet[4]==(1 if p==5 else 0) and bet[5]==(1+(sum((-1)**len(f) for f in listing)-1)//n), (p, bet)
      print('n=%s p=%s cells=%s boundary_ranks=%s mod_p_betti=%s'%(n,p,tuple(len(levels[k]) for k in sorted(levels)),ranks,bet))

if __name__=='__main__':
    test(5)
    for n in (5,7):
      ff=list(faces(n))
      for k in range(1,n):
        assert all(shift(f,n,k)!=f for f in ff if f)
      euler=sum((-1)**len(f) for f in ff)
      b=1-n+comb(n,2)
      b=b**3+n*(2-n)**3+comb(n,2)
      assert euler==b and (b+n-1)%n==0
      print('PASS: n=%d cyclic column action is free on all %d nonempty faces; predicted top rank=%d.'%(n,len(ff)-1,(b+n-1)//n))
    for n in (4,6,8):
      f=(0,n//2)
      assert shift(f,n,n//2)==f
      print('PASS: n=%d half-turn fixes a nonempty face.'%n)
    print('PASS: all quotient and parity finite checks.')

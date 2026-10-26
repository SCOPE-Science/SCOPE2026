"""Finite checks for a sharp temporal representation separation; standalone Python 3."""
from itertools import product, combinations
from functools import lru_cache

def ballot_sets(n,m,L,ballots):
    # ballots indexed voter,round, represented by bitmask over candidates
    return [[ballots[i*L+r] for r in range(L)] for i in range(n)]

def sats(A, outcome):
    return [sum(bool(A[i][r]&(1<<outcome[r])) for r in range(len(outcome))) for i in range(len(A))]

def pareto(A,outcome):
    n=len(A);L=len(outcome);m=max(1,max((x.bit_length() for row in A for x in row),default=0))
    base=sats(A,outcome)
    for o in product(range(m), repeat=L):
        vals=sats(A,o)
        if all(a>=b for a,b in zip(vals,base)) and any(a>b for a,b in zip(vals,base)):
            return False
    return True

def h(A,S,r,m):
    return max(sum(bool(A[i][r]&(1<<c)) for i in S) for c in range(m))

def ejrp(A,outcome,m):
    n=len(A); L=len(outcome);v=sats(A,outcome)
    for Sm in range(1,1<<n):
        S=[i for i in range(n) if Sm>>i&1]
        hb=[h(A,S,r,m) for r in range(L)]
        for sigma in range(1,n+1):
          tau=sum(x>=sigma for x in hb)
          if not tau: continue
          b=sigma*tau//n
          if b<=max(v[i] for i in S):continue
          for r in range(L):
            if all(A[i][r]!=0 for i in S):
              common=(1<<m)-1
              for i in S:common&=A[i][r]
              if common and not (common&(1<<outcome[r])):
                return False
    return True

def fjrp(A,outcome,m):
    n=len(A);L=len(outcome);v=sats(A,outcome)
    for Sm in range(1,1<<n):
       S=[i for i in range(n) if Sm>>i&1]
       hb=[h(A,S,r,m) for r in range(L)]
       for beta in range(1,L+1):
          if max(v[i] for i in S)>=beta:continue
          ss=sum(hb)
          if ss>n*beta or (Sm==(1<<n)-1 and ss>=n*beta):return False
          if any(sigma*sum(x>=sigma for x in hb)>=n*beta for sigma in range(1,n+1)):
             return False
    return True

def fjr(A,outcome,m):
    n=len(A);L=len(outcome);v=sats(A,outcome)
    for Sm in range(1,1<<n):
      S=[i for i in range(n) if Sm>>i&1]
      highest=max(v[i] for i in S)
      for Tm in range(1,1<<L):
        T=[r for r in range(L) if Tm>>r&1];q=len(T)*len(S)//n
        if q<=highest: # mu<=q so cannot violate
          continue
        for R in combinations(T,q):
          # if some subset R cannot guarantee highest+1, then no FJR violation on T
          can=False
          for picks in product(range(m),repeat=q):
            if all(sum(bool(A[i][r]&(1<<c)) for r,c in zip(R,picks))>highest for i in S):
              can=True;break
          if not can:break
        else:
          return False
    return True

def example():
    # n=3, L=3, two candidates a,b; voter 1 approves a rounds 1,2;
    # voter 2 approves a round 3; voter 3 approves b each round.
    A=[[1,1,0],[0,0,1],[2,2,2]]
    O=(1,1,1)
    assert sats(A,O)==[0,0,3]
    assert pareto(A,O)
    assert ejrp(A,O,2)
    assert fjr(A,O,2)
    assert not fjrp(A,O,2)
    print('WITNESS PASS: PE, EJR+, FJR and not FJR+; satisfaction',sats(A,O))

def exhaustive(n,L,m):
    outcomes=list(product(range(m),repeat=L)); examined=0;eligible=0
    for ballots in product(range(1<<m),repeat=n*L):
      A=ballot_sets(n,m,L,ballots)
      for O in outcomes:
        examined+=1
        if not pareto(A,O):continue
        if not ejrp(A,O,m):continue
        eligible+=1
        if not fjrp(A,O,m):
          print('COUNTEREXAMPLE',n,L,m,A,O)
          return False
    print('EXHAUSTIVE PASS: n,L,m,all/eligible',n,L,m,examined,eligible)
    return True
if __name__=='__main__':
    example()
    for n,L in [(1,1),(2,1),(2,2),(2,3),(3,1),(3,2)]:
      assert exhaustive(n,L,2)

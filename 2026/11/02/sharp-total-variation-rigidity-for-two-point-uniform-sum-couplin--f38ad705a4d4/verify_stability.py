from itertools import permutations
from fractions import Fraction

def ideal(j):
    return j+1 if j%2==0 else j-1

def stats(p):
    m=len(p); success=sum(abs(j-p[j])==1 for j in range(m));
    bad=sum(abs(j-p[j])==1 and p[j]!=ideal(j) for j in range(m));
    fail=m-success; tv=m-sum(p[j]==ideal(j) for j in range(m));
    assert tv==fail+bad
    return fail,bad,tv

def run():
  tests=0
  for k in range(1,5):
    m=2*k
    for p in permutations(range(m)):
      f,b,tv=stats(p)
      assert b <= (k-1)*f, (k,p,f,b)
      assert tv<=k*f
      tests+=2
    if k>1:
      p=list(map(ideal,range(m)))
      p[0]=m-1
      for j in range(2,m,2): p[j]=j-1
      assert sorted(p)==list(range(m))
      f,b,tv=stats(p)
      assert (f,b,tv)==(1,k-1,k), (k,p,f,b,tv)
      tests+=2
  print('PASS',tests,'exact finite permutation assertions k=1..4')
if __name__=='__main__': run()

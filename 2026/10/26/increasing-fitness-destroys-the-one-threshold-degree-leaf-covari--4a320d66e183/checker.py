from fractions import Fraction as F
from itertools import product

def formula(w):
 n=len(w);s=[F(0)]
 for x in w:s.append(s[-1]+x)
 leaf=[F(0)]*(n+1)
 for j in range(2,n+1):
  leaf[j]=F(1)
  for k in range(j+1,n+1):leaf[j]*=1-F(w[j-1],s[k-1])
 out=[]
 for i in range(1,n+1):
  c=F(0)
  for k in range(i+1,n+1):
   bracket= -leaf[i] if i>=2 else F(0)
   for j in range(2,k):
    if j!=i:bracket+=leaf[j]*F(w[j-1],s[k-1]-w[j-1])
   c+=F(w[i-1],s[k-1])*bracket
  out.append(c)
 return out

def enum(w):
 n=len(w);s=[0]
 for x in w:s.append(s[-1]+x)
 ed=[F(0)]*(n+1);el=F(0);edl=[F(0)]*(n+1)
 for parents in product(*(range(1,k) for k in range(2,n+1))):
  pr=F(1);degrees=[0]*(n+1)
  for k,j in enumerate(parents,2):
   pr*=F(w[j-1],s[k-1]);degrees[j]+=1
  L=sum(degrees[j]==0 for j in range(2,n+1))
  el+=pr*L
  for j in range(1,n+1):ed[j]+=pr*degrees[j];edl[j]+=pr*degrees[j]*L
 return [edl[i]-ed[i]*el for i in range(1,n+1)]

if __name__ == '__main__':
    checks = 0
    witness = [1,2,6,7,8]
    assert formula(witness) == [F(15049,62208),F(-2087,31104),F(25,10368),F(-1225,6912),F(0)]
    checks += 1
    assert formula(witness) == enum(witness)
    checks += 1
    # Exhaustively enumerate parent choices independently of the covariance formula.
    for n in range(2,7):
        for w in product([1,2],repeat=n):
            a, b = formula(w), enum(w)
            assert a == b, (w, a, b)
            checks += n
            if n >= 3:
                assert a[n-2] < 0, (w, a)
                checks += 1
    for n in range(2,6):
        for w in product([1,2,3],repeat=n):
            a, b = formula(w), enum(w)
            assert a == b, (w, a, b)
            checks += n
    print(f'PASS: {checks} exact rational assertions; strict-increasing witness and all enumerated cases match.')

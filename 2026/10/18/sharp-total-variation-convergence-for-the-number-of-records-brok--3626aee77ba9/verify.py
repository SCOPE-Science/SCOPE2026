from fractions import Fraction
from math import factorial,pi,sqrt,log
from itertools import permutations

def polyadd(a,b):
 c=[Fraction(0) for _ in range(max(len(a),len(b)))]
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return c

def scaled(a,s):return [v*s for v in a]

def rec_poly(n):
 q=[Fraction(1)]
 for j in range(1,n+1):
  out=[Fraction(0)]*(len(q)+1)
  for k,v in enumerate(q):
   out[k]+=v*Fraction(j-1,j)
   out[k+1]+=v*Fraction(1,j)
  q=out
 return q

def broken_poly(n):
 # direct mixture j=0..n
 result=[Fraction(0)]*(n+1)
 for j in range(n):
  f=rec_poly(j)
  for k,v in enumerate(f):result[k]+=v/Fraction((j+1)*(j+2))
 f=rec_poly(n)
 for k,v in enumerate(f):result[k]+=v/Fraction(n+1)
 return result

def broken_enumeration(n):
 ct=[0]*(n+1)
 for seq in permutations(range(n+1)):
  cur=[]; m=-1
  for i in range(n-1,-1,-1):
   if seq[i]>m:
    cur.append(seq[i]);m=seq[i]
  k=sum(v<seq[-1] for v in cur)
  ct[k]+=1
 return [Fraction(v,factorial(n+1)) for v in ct]

def verify_identity(n):
 a=rec_poly(n); b=broken_poly(n)
 # (2-z) F_n = 1 + ((1-z)/(n+1)) A_n
 lhs=polyadd(scaled(b,2),[Fraction(0)]+scaled(b,-1))
 rhs=polyadd([Fraction(1)],scaled(polyadd(a,[Fraction(0)]+scaled(a,-1)),Fraction(1,n+1)))
 lhs+= [Fraction(0)]*(max(len(lhs),len(rhs))-len(lhs))
 rhs+= [Fraction(0)]*(max(len(lhs),len(rhs))-len(rhs))
 assert lhs==rhs, (n,lhs,rhs)
 # (n+1)*(Geom - B_n)=(Geom*K_n - K_n), coefficients to degree n+8
 G=[Fraction(1,2**(k+1)) for k in range(n+9)]
 Gb=[v-(b[k] if k<len(b) else 0) for k,v in enumerate(G)]
 conv=[sum(a[i]*G[k-i] for i in range(min(k,len(a)-1)+1)) for k in range(len(G))]
 assert all((n+1)*Gb[k]==conv[k]-(a[k] if k<len(a) else 0) for k in range(len(G)))
 return b

for n in range(0,10):
 b=verify_identity(n)
 if 1<=n<=7:assert broken_enumeration(n)==b,(n,broken_enumeration(n),b)
 print('exact',n,b[:4])

# numerical TV exact formula via kernel and direct signed masses
for n in [1,2,5,10,50,100,1000,10000,100000]:
 a=[1.]
 for j in range(1,n+1):
  # floating K_n, direct coeff conv O(n^2) expensive; truncate tail states O(log n)
  r=[0.]*(min(len(a)+1,130))
  for k,v in enumerate(a):
   if k<len(r):r[k]+=v*(j-1)/j
   if k+1<len(r):r[k+1]+=v/j
  a=r
 D=[]
 for k in range(len(a)+15):
  D.append(sum(2.**(-r-1)*a[k-r] for r in range(min(k,len(a)-1)+1) if k-r < len(a)))
 mm=max(D)
 d=mm/(n+1)
 print('n',n,'dTV',d,'scale',(n+1)*sqrt(log(n))*d if n>1 else None, 'max k',D.index(mm),'vs',1/sqrt(2*pi))

# Exact single-crossing and distance checks for small horizons.
for n in range(1,10):
    a=rec_poly(n)
    b=broken_poly(n)
    geometric=[Fraction(1,2**(k+1)) for k in range(n+24)]
    tail=Fraction(1,2**(n+24))
    assert sum(geometric)+tail==1
    signed=[(b[k] if k<len(b) else Fraction(0))-geometric[k]
            for k in range(n+24)]
    signs=[1 if x>0 else -1 if x<0 else 0 for x in signed]
    nonzero=[s for s in signs if s]
    assert nonzero==sorted(nonzero,reverse=True), (n,nonzero)
    kernel=[]
    for k in range(n+1):
        kernel.append(sum(Fraction(1,2**(r+1))*a[k-r]
                          for r in range(k+1) if 0<=k-r<len(a)))
    # The signed error is positive below the crossing; all omitted values
    # of G are beyond the support of B_n and have strictly negative signs.
    tv=sum(x for x in signed if x>0)
    assert tv==max(kernel)/Fraction(n+1), (n,tv,kernel)
print('finite single-crossing, exact-distance and enumeration checks passed')

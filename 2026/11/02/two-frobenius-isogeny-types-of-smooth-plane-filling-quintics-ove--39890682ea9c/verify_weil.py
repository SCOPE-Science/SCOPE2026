"""Exact reconstruction of genus-six Weil numerators; irreducibility certificates mod 2."""
COUNTS={144:[13,13,55,13,208,913],432:[13,13,16,117,273,640]}
EXPECTED={
144:[1,9,42,144,399,900,1691,2700,3591,3888,3402,2187,729],
432:[1,9,42,131,308,601,1067,1803,2772,3537,3402,2187,729]}

def numerator(N):
 s=[0]+[3**n+1-N[n-1] for n in range(1,7)]
 a=[1]
 for n in range(1,7):
  numer=-sum(a[n-k]*s[k] for k in range(1,n+1))
  assert numer % n==0
  a.append(numer//n)
 a += [3**(k-6)*a[12-k] for k in range(7,13)]
 return a

def rem(a,b):
 while a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
 return a

def gcd(a,b):
 while b:a,b=b,rem(a,b)
 return a

def square_mod(a,f):
 z=0
 for i in range(a.bit_length()):
  if (a>>i)&1:z ^= 1<<(2*i)
 return rem(z,f)

def irreducible_mod2(a):
 f=sum((c&1)<<i for i,c in enumerate(a));n=len(a)-1
 x=2; cur=x
 for k in range(1,n+1):
  cur=square_mod(cur,f)
  if k in [n//p for p in (2,3) if n%p==0]:
   assert gcd(cur^x,f)==1, ('reducible',n,k)
 assert cur==x
 return True

def mulpoly(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out

for name,N in COUNTS.items():
 a=numerator(N)
 assert a==EXPECTED[name]
 assert irreducible_mod2(a if name==432 else [1,3,5,9,9])
 if name==144:
  q=[1,3,5,9,9]
  assert mulpoly(mulpoly(q,q),q)==a
 print(name,'Weil_numerator',a,'Jacobian_order',sum(a))
print('WEIL_CERTIFICATE_OK')

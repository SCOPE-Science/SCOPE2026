from math import gcd

def T(s):
 i=s.find('1');return s if i<0 else s[:i]+s[i+1:]+'1'

def word(p,q,n,a,b):
 # take x=(a+b)/(2q), where endpoints a/q, b/q
 X=a+b
 return ''.join(str((X+2*(i+1)*p)//(2*q)-(X+2*i*p)//(2*q)) for i in range(n))

trials=0
for q in range(2,22):
 for p in range(1,q):
  if gcd(p,q)!=1:continue
  h=(q-1)//p
  for n in range(1,2*q+2):
   markers=sorted((( -j*p)%q,j) for j in range(min(n,q-1)+1))
   records=[(a,word(p,q,n,a,markers[i+1][0] if i+1<len(markers) else q)) for i,(a,j) in enumerate(markers)]
   assert all(records[i][1]<records[i+1][1] for i in range(len(records)-1)), (p,q,n,'word-order')
   image=[T(x[1]) for x in records]
   assert image==sorted(image), (p,q,n,'image-order')
   for i in range(1,len(markers)):
    j=markers[i][1]
    pred=(j<n and j<=h and (n<q or n<q+j))
    actual=image[i-1]==image[i]
    assert pred==actual,(p,q,n,j,pred,actual)
    trials+=1
print('PASS',trials,'individual boundary identifications')

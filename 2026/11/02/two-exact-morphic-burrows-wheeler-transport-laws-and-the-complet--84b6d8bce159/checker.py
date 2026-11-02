from itertools import product

def bwt(s):
    n=len(s)
    rotations=sorted(range(n),key=lambda i:s[i:]+s[:i])
    return ''.join(s[(i-1)%n] for i in rotations)

def tau(s):return ''.join('010' if x=='0' else '011' for x in s)
def eta(s):return ''.join('0' if x=='0' else '01' for x in s)
def sigma(s):return ''.join('0010' if x=='0' else '1' for x in s)

count=0
for n in range(1,10):
 for bits in product('01', repeat=n):
  v=''.join(bits);z=v.count('0');o=v.count('1')
  a=bwt(tau(v));b='1'*z+bwt(v)+'0'*z+'1'*o+'0'*o
  c=bwt(eta(v));d=bwt(v)+'0'*o
  assert a==b,(v,a,b)
  assert c==d,(v,c,d)
  count+=1
print('universal identities:',count, 'words through length9 PASS')
h='0';c='0'
for n in range(0,8):
 if n>0:
  h=tau(h);c=sigma(c)
 assert c==eta(h)
 if len(c)>4000:break
 b=bwt(c);rr=1+sum(b[i]!=b[i-1] for i in range(1,len(b)))
 formula='1'*((3**n+2*n-1)//4) if n>=1 else '0'
 if n==1: formula='1000'
 if n>=2:
  for j in range(1,n):
   formula+= '0'*(4 if j==1 else 2*3**(j-1)) + '1'*((3**j-1)//2)
  formula+='0'*(2*3**(n-1)-1)
 print('Chacon',n,'len',len(c),'runs',rr,'same-formula',b==formula)
 assert b==formula,(n,b,formula)
print('PASS')

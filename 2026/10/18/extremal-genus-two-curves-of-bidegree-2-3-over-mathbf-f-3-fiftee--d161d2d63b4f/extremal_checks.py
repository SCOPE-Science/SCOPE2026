import sympy as sp,csv,collections
x=sp.symbols('x')

def coeff(n):
 return [(n//3**i)%3 for i in range(12)]
def disc(n):
 v=coeff(n);d=[0]*7
 for i in range(4):
  for j in range(4):d[6-i-j]=(d[6-i-j]+v[4+i]*v[4+j]-v[i]*v[8+j])%3
 return d

def fac(n):
 c=disc(n);f=sum(c[i]*x**i for i in range(7))
 fs=sp.factor_list(f,modulus=3)[1]
 ds=sorted([sp.degree(g,x) for g,m in fs for _ in range(m)])
 if c[6]==0:ds.append(1)
 return sorted(ds),[str(g) for g,m in fs]
# F9 numbers a+b*i, i^2=2. ints 0..8 with a=z%3,b=z//3
def mul(x,y):
 a,b=x%3,x//3;c,d=y%3,y//3
 return ((a*c+2*b*d)%3)+3*((a*d+b*c)%3)
def add(x,y):return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
def power(x,n):
 r=1
 for _ in range(n):r=mul(r,x)
 return r
P=[(1,0)]+[(a,1) for a in range(9)]
Q=[(1,0)]+[(a,1) for a in range(9)]
def ev(c,S,T):
 r=0
 for k in range(4):r=add(r,mul(c[k],mul(power(S,3-k),power(T,k))))
 return r

def pointcount(n):
 v=coeff(n);N=0
 for S,T in P:
  a,b,c=(ev(v[j:j+4],S,T) for j in (0,4,8))
  for U,V in Q:
   val=add(add(mul(a,power(U,2)),mul(b,mul(U,V))),mul(c,power(V,2)))
   if val==0:N+=1
 return N
rows=[]
for row in csv.DictReader(open('orbit_reps.csv')):
 n,N,r,size=[int(row[k]) for k in ('rep','N','r','orbit_size')]
 if N==8:
  f=fac(n)[0];N2=pointcount(n); rows.append((n,size,N2,(N2+6)//2,'+'.join(map(str,f))))
for row in rows:print(*row,sep=',')
print('total sizes',sum(x[1] for x in rows));print('byfactor',collections.Counter((x[4],x[2]) for x in rows))

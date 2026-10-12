from math import gcd

def norm(a,b,c,d,n):
    return (a+c*n)**2 + (b+d*n)**2

def gaussian_gcd_unit(a,b,c,d):
    # gcd=unit iff no shared gaussian prime: Euclidean algorithm in Z[i]
    z,w=complex(a,b),complex(c,d)
    # using exact pairs and rounded quotient
    x=(a,b);y=(c,d)
    while y!=(0,0):
        v=y[0]**2+y[1]**2
        re=(x[0]*y[0]+x[1]*y[1]); im=(x[1]*y[0]-x[0]*y[1]);
        qr=(2*re+v)//(2*v); qi=(2*im+v)//(2*v)
        x,y=y,(x[0]-qr*y[0]+qi*y[1], x[1]-qr*y[1]-qi*y[0])
    return x[0]**2+x[1]**2==1

cases=0; pairs=0; prime_factors=set()
for a in range(-6,7):
 for b in range(-6,7):
  for c in range(-4,5):
   for d in range(-4,5):
    if (c,d)==(0,0) or gcd(c,d)!=1 or not gaussian_gcd_unit(a,b,c,d):continue
    A=c*c+d*d; B=2*(a*c+b*d); Delta=a*d-b*c; K=A*A+4*Delta*Delta
    Q=K
    while Q%2==0:Q//=2
    if gcd(Q,A)!=1: raise AssertionError(('coprime',a,b,c,d))
    for n in range(-15,16):
     f=norm(a,b,c,d,n);g=norm(a,b,c,d,n+1);h=norm(a,b,c,d,n+2)
     actual=gcd(f,g); predicted=gcd(Q,A*(2*n+1)+B)
     if actual!=predicted or gcd(actual,h)!=1:
      raise AssertionError((a,b,c,d,n,actual,predicted,gcd(actual,h)))
     pairs+=1
    cases+=1
print('VERIFY_OK')
print('primitive_affine_lines=',cases)
print('adjacent_index_pairs_checked=',pairs)
print('full_exact_gcd_and_three_consecutive_coprime=PASS')
# Exhibit every possible divisor for a line whose K_odd has composite factors
for (a,b,c,d) in [(1,2,0,1),(2,1,0,1),(3,0,0,1),(1,5,0,1),(4,3,0,1)]:
 A=c*c+d*d;B=2*(a*c+b*d);Delta=a*d-b*c;K=A*A+4*Delta*Delta
 Q=K
 while Q%2==0:Q//=2
 counts={}
 for n in range(Q):
  z=gcd(norm(a,b,c,d,n),norm(a,b,c,d,n+1));counts[z]=counts.get(z,0)+1
 print('sample',a,b,c,d,'K_odd',Q,'gcd_fibers',sorted(counts.items()))

q=325
fibers={}
for n in range(q):
 g=gcd(9*9+n*n,9*9+(n+1)*(n+1))
 fibers[g]=fibers.get(g,0)+1
assert fibers=={1:240,5:48,13:20,25:12,65:4,325:1}
print('complete_325_fibers=PASS')

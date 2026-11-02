from itertools import permutations,product
from fractions import Fraction as F
from math import comb, factorial

def formula(n,d):
 p=sum(((-1)**k)*F(comb(n-1,k),(k+1)**d) for k in range(n))
 b=sum(((-1)**k)*comb(n-2,k)*F(1,((k+1)*(k+2))**d) for k in range(n-1))
 c=sum(((-1)**k)*comb(n-3,k)*(F(1,(2*(k+1))**d)-(F(k+4,2*(k+2)*(k+3)))**d) for k in range(n-2)) if n>=3 else 0
 v=n*(n-1)*(b+(n-2)*c-F(n,2**d)*p)
 return p,v

def exhaustive(n,d):
 perms=list(permutations(range(n)))
 total=factorial(n)**d
 ex=ey=exy=0
 for tup in product(perms, repeat=d):
  pts=list(zip(*tup))
  dominates=[[i!=j and all(pts[i][k]>=pts[j][k] for k in range(d)) for j in range(n)] for i in range(n)]
  m=sum(not any(dominates[j][i] for j in range(n)) for i in range(n))
  q=sum(sum(row) for row in dominates)
  ex+=m;ey+=q;exy+=m*q
 return F(exy,total)-F(ex,total)*F(ey,total)

if __name__ == '__main__':
    tests = [(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)]
    count = 0
    for n,d in tests:
        value = formula(n,d)[1]
        assert value == exhaustive(n,d), (n,d)
        count += 1
    for n in range(3,25):
        observed = formula(n,2)[1]
        harmonic = sum(F(1,j) for j in range(1,n+1))
        assert observed == -(n-harmonic)/2
        count += 1
    for n in range(3,13):
        residuals = []
        for d in (16,24,32):
            exact = formula(n,d)[1]
            approx = -F(n*(n-1),2**d)-F(n*(n-1)*(n-2),3**d)+F(n*(n-1)*(4*n-6),4**d)
            residuals.append(abs(exact-approx)/F(5,24)**d)
            assert abs(exact-approx) < F(10000000,1)*F(5,24)**d
            count += 1
    print(f'PASS: {count} exact-rational checks')

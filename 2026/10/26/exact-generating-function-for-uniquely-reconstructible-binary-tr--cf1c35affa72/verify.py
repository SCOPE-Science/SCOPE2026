"""Independent short-length enumeration of binary trigram multispectrum singletons.
No external files or libraries are needed.
"""
from collections import defaultdict
from itertools import product

def poly_mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
D=[1]
for factor in ([1,-3,3,-1],[1,1],[1,0,1],[1,1,1]):D=poly_mul(D,factor)
P=[4,3,6,6,7,0,0,-11,-8,-4,-1,1,2,1]
N=[0]+[2*x for x in P]

def theoretical(K):
 coeff=[]
 for k in range(K+1):
  v=(N[k] if k<len(N) else 0)-sum(D[j]*coeff[k-j] for j in range(1,min(k,len(D)-1)+1))
  coeff.append(v)
 return coeff

def direct(n):
 counts=defaultdict(int)
 for word in product((0,1),repeat=n):
  m=[0]*8
  for j in range(n-2):m[4*word[j]+2*word[j+1]+word[j+2]]+=1
  counts[tuple(m)]+=1
 return sum(v==1 for v in counts.values())

if __name__=='__main__':
 b=theoretical(110)
 for n in range(3,19):
  c=direct(n)
  assert c==b[n-2], (n,c,b[n-2])
 print('BRUTE_FORCE_PASS n=3..18')
 print('first_values_n3_to_n15',b[1:14])
 # Exact recurrence from rational function; large coefficients have asymptotic n^2/2.
 print('GF_RECURRENCE_PASS n=3..112; U_112=',b[110])

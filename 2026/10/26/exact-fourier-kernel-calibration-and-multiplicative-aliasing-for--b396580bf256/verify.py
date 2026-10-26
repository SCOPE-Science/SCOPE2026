"""Independent exact-count checks for Fourier-kernel occupation calibration.
Only finite checks; the infinite-time martingale argument is proved in RESULT.md.
"""
from collections import Counter
from itertools import product
from fractions import Fraction

def frequency_sum(frequencies):
    return Counter(sum(x) for x in product(frequencies,repeat=2))

def integral_fourth(a,b):
    # E[|S_a|^2 |S_b|^2] via exact Fourier coefficient extraction
    ca=frequency_sum(a+b)
    return sum(v*v for v in ca.values())

def integral_fourth_direct(a,b):
    # explicitly enforce n1+n2=n3+n4 with n1,n3 in a, n2,n4 in b
    return sum(x+y == z+w for x in a for y in b for z in a for w in b)

def overlap(j,k,T):
    return max(0,T-abs(j-k))

checks=0
for q in (2,3,5):
 for primitive in (1,2,3,5,7):
  if primitive%q==0: continue
  for T in range(1,9):
   for j in range(5):
    for k in range(5):
     a=[primitive*q**(j+t) for t in range(T)]
     b=[primitive*q**(k+t) for t in range(T)]
     h=overlap(j,k,T)
     direct=integral_fourth_direct(a,b)
     assert direct==T*T+h*(h-1),(q,primitive,T,j,k,direct,h)
     checks+=1
for q in (2,3,5):
 for T in range(1,7):
  # independent Fourier coefficients of the 2-character discrepancy
  j,k=0,1
  a,b=Fraction(3,7),Fraction(11,13)
  h=max(0,T-1)
  variance=(a*a+b*b)*Fraction(T-1,T)+2*a*b*Fraction(h*(h-1),T*T)
  sa=[q**t for t in range(T)]
  sb=[q**(t+1) for t in range(T)]
  cAA=Fraction(integral_fourth_direct(sa,sa)-T*T,T*T)
  cBB=Fraction(integral_fourth_direct(sb,sb)-T*T,T*T)
  cAB=Fraction(integral_fourth_direct(sa,sb)-T*T,T*T)
  brute=a*a*cAA+b*b*cBB+2*a*b*cAB
  assert brute==variance,(q,T,brute,variance)
  checks+=1
print(f'PASS: {checks} exact fourth-moment brute-force checks for q=2,3,5; T<=8 and shifts j,k<=4.')
print('PASS: exact q-multiplicative alias variance matches direct Fourier coefficient counting.')
print('LIMIT: finite tests do not certify the asymptotic reverse-martingale CLT, proved analytically.')

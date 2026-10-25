#!/usr/bin/env python3
"""Exact 64-case certificate for smooth pointless (2,4) divisors over F2.
The four allowed quartics take value 1 on all three P1(F2) points.
Representation: bit i is the coefficient of x^i for x=u/v.
"""
import json
from itertools import product
FOUR=(19,21,25,31)

def mul(a,b):
 out=0
 while b:
  if b&1:out^=a
  a<<=1;b>>=1
 return out

def rem(a,b):
 assert b
 while a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
 return a

def gcd(a,b):
 while b:a,b=b,rem(a,b)
 return a

def deriv(f):return sum(((f>>j)&1) <<(j-1) for j in (1,3))

def smooth(a,b,c):
 v=mul(deriv(a),c)^mul(a,deriv(c))
 disc=mul(v,v)^mul(mul(deriv(b),deriv(b)),mul(a,c))
 # b has coefficient 1 at x^4 for all four pointless candidates,
 # hence no discriminant zero at projective infinity.
 return gcd(b,disc)==1

def main():
 by_b={}; good=[];tables={}
 for b in FOUR:
  cells=[]
  for a in FOUR:
   row=[]
   for c in FOUR:
    isok=smooth(a,b,c);row.append(int(isok))
    if isok:good.append(a|(b<<5)|(c<<10))
   cells.append(row)
  tables[str(b)]=cells
  by_b[str(b)]=sum(sum(row) for row in cells)
 assert len(good)==33 and by_b=={'19':9,'21':6,'25':9,'31':9}
 print(json.dumps({'raw_pointless_models':len(FOUR)**3,'smooth_pointless_models':len(good),'smooth_by_middle_coefficient':by_b,'gcd_test_tables':tables,'all_smooth_pointless_codes':sorted(good)},indent=2,sort_keys=True))
if __name__=='__main__':main()

"""Independent exhaustive paired-domination definition check for seven-point triangular graph."""
from itertools import combinations
from collections import Counter

def check(n=7):
 E=list(combinations(range(n),2)); m=len(E); size=1<<m
 neigh=[0]*m
 for i,(a,b) in enumerate(E):
  for j,(c,d) in enumerate(E):
   if i!=j and (a in (c,d) or b in (c,d)):neigh[i]|=1<<j
 covered=[0]*size
 paired=bytearray(size); paired[0]=1
 counts=Counter()
 for s in range(1,size):
  bit=s&-s; i=bit.bit_length()-1; rem=s^bit
  covered[s]=covered[rem]|neigh[i]|bit
  if s.bit_count()%2: continue
  poss=rem&neigh[i]
  while poss:
   partner=poss&-poss
   if paired[rem^partner]:paired[s]=1;break
   poss^=partner
  if paired[s] and covered[s]==size-1:
   counts[s.bit_count()]+=1
 # an even-cardinality paired set cannot be empty
 print('n=',n,'tested_subsets=',size,'paired_dom_coeffs=',sorted(counts.items()))
 assert counts[4]==630
 assert not any(i%2 for i in counts)
 print('n7 COMPLETE BRUTE FORCE PASSED')
if __name__=='__main__':check()

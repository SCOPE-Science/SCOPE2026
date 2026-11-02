#!/usr/bin/env python3
"""Independent finite check of binary Lyndon-subsequence maximum counts."""
import itertools
EXPECTED_MAX=(0,1,3,4,6,8,13,18,28,41,63,96,141,225,335,538,803)
EXPECTED_TIES=(0,2,1,2,1,4,1,2,1,1,1,1,2,1,1,1,1)
EXPECTED_FIRST=('', '0','01','001','0011','00011','001011','0001011',
 '00101011','000101011','0010101011','00010101011','000101011011',
 '0001010101011','00010101011011','000101010101011',
 '0001010101101011')
EXPECTED_SUM=(0,2,7,20,54,144,384,1028,2767,7492,20404,55874,
 153786,425294,1181392,3295370,9227742)
for n in range(1,17):
 def is_ly(c):
  s=bin(c)[3:]
  return all(s<s[j:]+s[:j] for j in range(1,len(s)))
 ly={v for v in range(2,2**(n+1)) if is_ly(v)}
 best=-1; first=None; ties=0; sm=0
 for x in range(2**n):
  w=f'{x:0{n}b}'
  subseq={1}
  for char in w:
   b=int(char)
   subseq.update({2*t+b for t in tuple(subseq)})
  score=len(subseq.intersection(ly))
  sm+=score
  if score>best:
   best=score;first=w;ties=1
  elif score==best: ties+=1
 assert (best,ties,first,sm)==(EXPECTED_MAX[n],EXPECTED_TIES[n],EXPECTED_FIRST[n],EXPECTED_SUM[n]),(n,best,ties,first,sm)
print('VERIFY_OK independent_python_hosts=131070 exact_n=1..16 maximum_ties_first_witness_and_sum=checked')

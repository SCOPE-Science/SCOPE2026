from verify import fixed_stats,count_from_stats
from itertools import permutations
from math import factorial
stat={}
for n in range(1,5):
 s=[fixed_stats(n,p) for p in permutations(range(n))]
 stat[n]=tuple(sum(x[i] for x in s)//factorial(n) for i in range(4))
 print('n',n,'u_stats a b c d',stat[n],flush=True)
for p in range(2,5):
 for q in range(2,5):
  print('U',p,q,count_from_stats(stat[p],stat[q]))

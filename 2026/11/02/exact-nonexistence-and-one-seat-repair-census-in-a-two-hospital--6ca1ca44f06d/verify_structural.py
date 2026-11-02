from itertools import permutations,product
from collections import Counter
D=('a','b','s','t')
P={'AB':('A','B'),'BA':('B','A')}
opts=[(),('AB',),('BA',),('AB','BA'),('BA','AB')]
def pair_stable(s_A,s_B,pref,r):
    # singles s_A and s_B distinct
    for i,h in ((s_A,'B'),(s_B,'A')):
        if pref[i]==h and r[h][i]<r[h][s_B if h=='B' else s_A]: return False
    return True
def is_dominant(c,r):
    return all(r[h][i] < min(r[h]['s'],r[h]['t']) for i,h in zip(('a','b'),P[c]))
def blocks_single_pair(c,s_A,s_B,r):
    return r[P[c][0]]['a']<r[P[c][0]][s_A if P[c][0]=='A' else s_B] and r[P[c][1]]['b']<r[P[c][1]][s_A if P[c][1]=='A' else s_B]
ans=Counter();wit={}
for pa in permutations(D):
 for pb in permutations(D):
  r={'A':{x:pa.index(x) for x in D},'B':{x:pb.index(x) for x in D}}
  for pref_s,pref_t in product(('A','B'),repeat=2):
   pref={'s':pref_s,'t':pref_t}
   S=[(s_A,s_B) for s_A,s_B in (('s','t'),('t','s')) if pair_stable(s_A,s_B,pref,r)]
   assert S
   for o in opts:
    stable_c=any(is_dominant(c,r) for c in o)
    stable_s=any(not any(blocks_single_pair(c,u,v,r) for c in o) for u,v in S)
    no=not (stable_c or stable_s)
    ans[(o,no)]+=1
    if no and o not in wit:wit[o]=(pa,pb,pref_s,pref_t,S)
print('Totals and no-stability by couple options:')
for o in opts:print(o,ans[(o,False)],ans[(o,True)])
print('NO total',sum(ans[(o,True)] for o in opts),'ALL',sum(ans.values()))
print('Witnesses',wit)

assert sum(ans[(o,True)]+ans[(o,False)] for o in opts) == 11520
assert [ans[(o,True)] for o in opts] == [0,128,128,192,192]
print("PASS: structural criterion enumeration")

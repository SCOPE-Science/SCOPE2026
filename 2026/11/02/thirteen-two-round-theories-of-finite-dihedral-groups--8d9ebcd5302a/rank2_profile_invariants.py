from math import gcd
import collections

def atm(n,x,y):
    vals=[0,x,y];bits=0;t=0
    for i in range(3):
      for j in range(i+1,3):
        if vals[i]==vals[j]:bits|=1<<t
        t+=1
    for i in range(3):
      for j in range(3):
       for h in range(3):
        if (vals[i]+vals[j])%n==vals[h]: bits|=1<<t
        t+=1
    return bits

def prof(n,x):return frozenset(atm(n,x,y) for y in range(n))

codes={};examples=collections.defaultdict(list);nr=collections.defaultdict(set)
for n in range(1,145):
    if n%30==0:print('progress',n,flush=True)
    for x in range(n):
        P=prof(n,x)
        if P not in codes:codes[P]=len(codes)
        cid=codes[P];d=n//gcd(n,x)
        kind=(d, (x%gcd(n,2)==0),gcd(n,24),n)
        examples[cid].append((n,x,d, bool(n%2==0 and x%2==0)))
        nr[n].add(cid)
print('one type count',len(codes))
for k,ex in examples.items():
    counts=collections.Counter((a[2],a[3]) for a in ex if a[0]>=30)
    print(k,'first',ex[:6], 'order>30 examples',counts.most_common(12),'first n',min(a[0] for a in ex))
print('roots n reps')
for n in [3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,20,24,32,36,40,48,56,60,72,96,120,144]:print(n,sorted(nr[n]))

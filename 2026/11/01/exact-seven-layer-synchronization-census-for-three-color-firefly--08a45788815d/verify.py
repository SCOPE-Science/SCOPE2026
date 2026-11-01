from itertools import product
from collections import Counter

def update(states):
    c=states[0]
    leaves=states[1:]
    new_c=c if c==2 and any(x==1 for x in leaves) else (c+1)%3
    new_leaves=[x if x==2 and c==1 else (x+1)%3 for x in leaves]
    return (new_c,*new_leaves)

def t_sync(x):
    visited=set()
    for t in range(20):
        if all(a==x[0] for a in x):
            return t
        if x in visited:
            return None
        visited.add(x)
        x=update(x)
    raise RuntimeError('Unresolved')

def theory(r):
    q2=2**r-2
    q3=3**r-3*2**r+3
    return Counter({0:3,1:2+q2,2:2+q2,3:2+q2,4:q2,5:3*q2+q3,6:2*q2+q3,None:q3})

for r in range(1,10):
    cnt=Counter(t_sync(c) for c in product(range(3),repeat=r+1))
    expected=theory(r)
    cnt += Counter() 
    if cnt!= +expected:
       print('MISMATCH',r,sorted(cnt.items(),key=str),sorted(expected.items(),key=str))
       break
    print(r,dict(sorted(cnt.items(),key=lambda pair: str(pair[0]))))
else:
    print('ALL NINE SIZES EXACT')

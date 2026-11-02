from itertools import permutations,product
from collections import Counter
D=('a','b','s','t')
C={'AB':('A','B'),'BA':('B','A')}
options=[(),('AB',),('BA',),('AB','BA'),('BA','AB')]

def check(r,pref,o,caps):
    for cp in (None,*o):
        for ss,tt in product((None,'A','B'),repeat=2):
            match={'a':None,'b':None,'s':ss,'t':tt}
            if cp is not None:match['a'],match['b']=C[cp]
            seats={h:[i for i in D if match[i]==h] for h in ('A','B')}
            if any(len(seats[h])>caps[h] for h in seats):continue
            def admit(i,h):
                return len(seats[h])<caps[h] or any(r[h][i]<r[h][j] for j in seats[h])
            bad=False
            for i in ('s','t'):
                for h in ('A','B'):
                    if h==match[i]:continue
                    if match[i] is None or pref[i]==h:
                        if admit(i,h):bad=True
            if bad: continue
            for p in o:
                if p==cp:continue
                if cp is not None and o.index(p)>o.index(cp):continue
                h,g=C[p]
                if ((match['a']==h or admit('a',h)) and (match['b']==g or admit('b',g))):bad=True
            if not bad: return (cp,ss,tt)
    return None

counts=Counter(); witnesses=[]
for pa in permutations(D):
 for pb in permutations(D):
    r={'A':{v:i for i,v in enumerate(pa)},'B':{v:i for i,v in enumerate(pb)}}
    for ps,pt in product(('A','B'),repeat=2):
      pref={'s':ps,'t':pt}
      for o in options:
        b=check(r,pref,o,{'A':1,'B':1})
        a=check(r,pref,o,{'A':2,'B':1})
        c=check(r,pref,o,{'A':1,'B':2})
        key='stable' if b else 'both' if a and c else 'only_A' if a else 'only_B' if c else 'unresolved'
        counts[(o,key)]+=1
        if key=='only_A' and len(witnesses)<2:witnesses.append((pa,pb,ps,pt,o))
print('total',sum(counts.values()))
for o in options:print(o,[(x,counts[(o,x)]) for x in ('stable','both','only_A','only_B','unresolved')])
print('all',[(x,sum(counts[(o,x)] for o in options)) for x in ('stable','both','only_A','only_B','unresolved')])
print('witness',witnesses)

assert sum(counts.values()) == 11520
assert [counts[(o,"both")] for o in options] == [0,128,128,192,192]
assert sum(counts[(o,"stable")] for o in options) == 10880
assert all(counts[(o,k)] == 0 for o in options for k in ("only_A","only_B","unresolved"))
print("PASS: direct BIS enumeration")

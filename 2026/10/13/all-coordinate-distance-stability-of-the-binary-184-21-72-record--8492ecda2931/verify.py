#!/usr/bin/env python3
from collections import Counter

def pmul(a,b):
    r=0
    while b:
        if b&1: r ^= a
        b >>= 1; a <<= 1
    return r

def pdiv(a,b):
    q=0; db=b.bit_length()-1
    while a and a.bit_length()-1 >= db:
        s=(a.bit_length()-1)-db
        q ^= 1<<s; a ^= b<<s
    return q,a

def cyclic(a,m):
    while a.bit_length()-1 >= m:
        j=a.bit_length()-1
        a ^= 1<<j
        a ^= 1<<(j-m)
    return a

m=85
factors=[
    [1,0],
    [4,3,2,1,0],
    [8,6,5,4,2,1,0],
    [8,7,5,4,3,2,0],
]
h=1
for exps in factors:
    f=sum(1<<e for e in exps)
    h=pmul(h,f)
g,rem=pdiv((1<<m)^1,h)
assert rem==0 and h.bit_length()-1==21 and g.bit_length()-1==64
f2=sum(1<<e for e in [13,9,8,7,6,5,3,1,0])
tail_patterns=['11001','01001','00101','11101','11110','00111','11100','01010','10010','10001','11111','01110','10011','00110']
gens=[]
for i in range(21):
    b=1<<i
    a1=pmul(b,g)
    a2=cyclic(pmul(pmul(b,g),f2),m)
    tail=0
    for j,s in enumerate(tail_patterns):
        if int(s[i%5]): tail |= 1<<j
    gens.append(a1 | (a2<<85) | (tail<<170))
# First block bg has degree <85 and multiplication by nonzero g is injective for deg b<21.
assert len(set(gens))==21 and all(x!=0 for x in gens)
weight_counts=Counter()
minimum=[]
word=0; prev=0; minw=185
for z in range(1,1<<21):
    gray=z^(z>>1)
    diff=gray^prev
    i=(diff & -diff).bit_length()-1
    word ^= gens[i]
    prev=gray
    w=word.bit_count()
    weight_counts[w]+=1
    if w<minw:
        minw=w; minimum=[word]
    elif w==minw:
        minimum.append(word)
expected_weights={72:9826,76:25242,80:124849,84:199206,88:461108,92:452812,96:456603,100:220932,104:108154,108:31226,112:6818,116:374,176:1}
assert minw==72 and dict(sorted(weight_counts.items()))==expected_weights
freq=[0]*184
for w in minimum:
    x=w
    while x:
        lb=x&-x; j=lb.bit_length()-1
        freq[j]+=1; x-=lb
spectrum=Counter(freq)
expected={2108:1,2346:2,2482:2,2516:3,2550:6,3940:17,3956:17,3958:102,3968:34}
assert dict(sorted(spectrum.items()))==expected
assert sum(freq)==72*9826
assert min(freq)>0 and max(freq)<9826
# The preceding inequalities certify the two all-coordinate consequences:
# each puncture has a weight-71 image of a minimum word, and each shortening
# contains a weight-72 minimum word; the ambient lower bounds give equality.
print('MINIMUM',minw,'A72',len(minimum))
print('INCIDENCE_SPECTRUM',dict(sorted(spectrum.items())))
print('ALL_COORDINATES_COVERED_AND_AVOIDED',min(freq),max(freq))
print('PUNCTURES [183,21,71]: 184/184')
print('SHORTENINGS [183,20,72]: 184/184')
print('VERIFY_OK')

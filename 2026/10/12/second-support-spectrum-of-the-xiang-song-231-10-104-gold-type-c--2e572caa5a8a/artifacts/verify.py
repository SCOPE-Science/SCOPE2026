#!/usr/bin/env python3
from collections import Counter

M=10
MOD=(1<<10)|(1<<6)|(1<<5)|(1<<3)|(1<<2)|(1<<1)|1
MASK=(1<<M)-1

def mul(a,b):
    r=0
    while b:
        if b&1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & (1<<M):
            a ^= MOD
    return r & MASK

def power(a,e):
    r=1
    while e:
        if e&1:
            r=mul(r,a)
        a=mul(a,a)
        e >>= 1
    return r

def trace(a):
    s=0
    x=a
    for _ in range(M):
        s ^= x
        x=mul(x,x)
    assert s in (0,1)
    return s

alpha=2
# The displayed polynomial is primitive: alpha has multiplicative order 1023.
x=1
order=None
for k in range(1,1024):
    x=mul(x,alpha)
    if x==1:
        order=k
        break
assert order==1023

a1=alpha
a2=mul(alpha,alpha)
D=[]
for x in range(1,1<<M):
    f=power(x,33)
    if trace(mul(a1,f))==0 and trace(mul(a2,f))==0:
        D.append(x)
assert len(D)==231

# Reconstruct all 1023 nonzero codewords as Python bitsets.
words={}
for b in range(1,1<<M):
    z=0
    for j,x in enumerate(D):
        if trace(mul(b,x)):
            z |= 1<<j
    words[b]=z
source_weights=Counter(w.bit_count() for w in words.values())
assert source_weights==Counter({104:132,112:396,120:396,128:99})

# Every binary two-space has exactly three nonzero message vectors {u,v,u+v}.
# Enumerate it once by requiring u < v < u^v.
spectrum=Counter()
witness=None
for u in range(1,1<<M):
    for v in range(u+1,1<<M):
        w=u^v
        if w>v:
            s=(words[u] | words[v]).bit_count()
            spectrum[s]+=1
            if s==156 and witness is None:
                witness=(u,v,w)

expected=Counter({156:440,160:3564,164:13464,168:30558,172:45144,
                  176:43362,180:26664,184:9306,188:1584,192:165})
assert spectrum==expected
# Gaussian binomial [10 choose 2]_2.
assert sum(spectrum.values())==((2**10-1)*(2**9-1))//3==174251
assert min(spectrum)==156 and spectrum[156]==440
assert witness is not None
assert [words[t].bit_count() for t in witness]==[104,104,104]
# For a binary 2-space, |Supp <u,v>|=(wt(u)+wt(v)+wt(u+v))/2.
assert ((words[witness[0]].bit_count()+words[witness[1]].bit_count()+words[witness[2]].bit_count())//2)==156

print('FIELD_ORDER',order)
print('DEFINING_SET_SIZE',len(D))
print('WEIGHT_DISTRIBUTION',dict(sorted(source_weights.items())))
print('TWO_SPACE_TOTAL',sum(spectrum.values()))
print('TWO_SUPPORT_SPECTRUM',dict(sorted(spectrum.items())))
print('D2',min(spectrum),'MINIMIZERS',spectrum[min(spectrum)])
print('WITNESS_MESSAGES',witness)
print('VERIFY_OK')

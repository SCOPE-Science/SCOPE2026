#!/usr/bin/env python3
"""Independent exhaustive checks for open-/closed-neighborhood XOR on friendship graphs."""
from itertools import product

def update(x, m, inclusive=False):
    c=x[0]
    a=x[1:]
    S=sum(a[2*i]^a[2*i+1] for i in range(m))%2
    out=[S^ (c if inclusive else 0)]
    for i in range(m):
        ai,bi=a[2*i:2*i+2]
        out.extend((bi^c,ai^c) if not inclusive else (ai^bi^c,ai^bi^c))
    return tuple(out)

def apply(x,m,word):
    for t in word: x=update(x,m,t=='B')
    return x

def rank_from_map(m, word):
    inputs=[tuple(int(j==i) for j in range(2*m+1)) for i in range(2*m+1)]
    vecs=[]
    for x in inputs:
        bits=apply(x,m,word); vecs.append(sum(b<<i for i,b in enumerate(bits)))
    basis={}
    for v in vecs:
        while v:
            k=v.bit_length()-1
            if k not in basis: basis[k]=v;break
            v^=basis[k]
    return len(basis)

for m in range(1,7):
    n=2*m+1
    assert 2*m+1<=13
    f1=0; f2=0; hit1=0; complete=0
    for x in product((0,1),repeat=n):
        a=apply(x,m,'A'); a2=apply(x,m,'AA'); a3=apply(x,m,'AAA')
        b=apply(x,m,'B'); b2=apply(x,m,'BB')
        z=tuple(0 for _ in range(n))
        assert a3==a and apply(x,m,'BBB')==b2
        assert apply(x,m,'ABB')==z and apply(x,m,'BAB')==z and apply(x,m,'BBA')==z
        assert b2 == (b2[0],)*n
        assert apply(x,m,'AAB')==apply(x,m,'AB')
        assert apply(x,m,'ABA')==apply(x,m,'AB')
        if a==x:f1+=1
        if a2==x:f2+=1
        if len(set(b))==1:hit1+=1
        complete+=1
    assert f1==2**(m+(m%2))
    assert f2==2**(2*m)
    assert hit1==2**(m+(2 if m%2 else 1))
    assert complete==2**n
    expected={ '':n, 'A':2*m,'AA':2*m,'B':m+(1 if m%2==0 else 0),'AB':m-(1 if m%2 else 0),'BB':1,'ABB':0 }
    for w,r in expected.items(): assert rank_from_map(m,w)==r,(m,w,rank_from_map(m,w),r)
    if m>=2:
        images=[tuple(apply(x,m,w) for x in [tuple(int(i==j) for i in range(n)) for j in range(n)]) for w in expected]
        assert len(set(images))==7
    if m in (2,3):
        for ell in range(1,8):
            for letters in product('AB', repeat=ell):
                w=''.join(letters)
                ca=w.count('A'); cb=w.count('B')
                canonical= ('A' if ca%2 else 'AA') if cb==0 else ('B' if ca==0 else 'AB') if cb==1 else ('BB' if ca==0 else 'ABB')
                for x in product((0,1), repeat=n):
                    assert apply(x,m,w)==apply(x,m,canonical), (m,w,canonical,x)
    print('m',m,'states',complete,'fixed_A',f1,'fixed_A2',f2,'B_to_uniform_1',hit1,'ranks',[rank_from_map(m,w) for w in expected])
print('ALL CHECKS PASS')

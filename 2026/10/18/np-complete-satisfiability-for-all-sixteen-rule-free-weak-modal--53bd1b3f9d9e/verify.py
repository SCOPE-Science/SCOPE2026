"""Finite cross-checks for syntactic closure certificates in weak modal logic.
Uses finite unrestricted conjunction closure (bounded term size) and a second, separately
implemented finite Horn constraint enumeration on the input's subformula support.
Not an infinite proof.
"""
from itertools import combinations, product
from random import Random

RNG=Random(971104)
def atom(i):return ('p',i)
def conj(a,b):return ('&',a,b)
def implies(a,b):return ('>',a,b)
def neg(a):return ('!',a)
def box(a):return ('B',a)
TOP=('T',)

def size(a):return 1+sum(size(x) for x in a[1:] if isinstance(x,tuple))
def subs(a):
    z={a}
    for x in a[1:]:
        if isinstance(x,tuple):z |= subs(x)
    return z

def poly(G,S,ops):
    q=set(G)&set(S)
    if 'N' in ops and TOP in S:q.add(TOP)
    while 1:
        old=len(q)
        for x in tuple(q):
            if 'M' in ops and x[0]=='&':
                q.update(y for y in x[1:] if y in S)
            if 'K' in ops and x[0]=='>':
                if x[1] in q and x[2] in S:q.add(x[2])
        if 'C' in ops:
            arr=list(q)
            for a in arr:
                for b in arr:
                    ab=conj(a,b)
                    if ab in S:q.add(ab)
        if len(q)==old:return q

def full_bounded(G,ops,max_size):
    q=set(G)
    if 'N' in ops:q.add(TOP)
    while 1:
        old=len(q)
        arr=tuple(q)
        if 'M' in ops:
            for x in arr:
                if x[0]=='&':q.update(x[1:])
        if 'K' in ops:
            for x in arr:
                if x[0]=='>' and x[1] in q:q.add(x[2])
        if 'C' in ops:
            arr=tuple(q)
            for a in arr:
                for b in arr:
                    if size(a)+size(b)+1<=max_size:q.add(conj(a,b))
        if len(q)==old:return q

def randterm(depth=3):
    if depth<1 or RNG.random()<.36:return RNG.choice([atom(0),atom(1),atom(2),TOP])
    tag=RNG.choice(['&','>','!','B'])
    if tag in ['&','>']:return (tag,randterm(depth-1),randterm(depth-1))
    return (tag,randterm(depth-1))

def independently_valid_horn(q,S,ops):
    # Brute evaluate each axiom violation on each possible H subset S,
    # using an explicit list of Boolean implications (not forward saturation).
    if 'N' in ops and TOP in S and TOP not in q:return False
    for x in S:
        if 'M' in ops and x[0]=='&' and x in q:
            if any(y not in q for y in x[1:]):return False
        if 'K' in ops and x[0]=='>' and x in q and x[1] in q and x[2] not in q:return False
    if 'C' in ops:
        for x in S:
            if x[0]=='&' and x[1] in q and x[2] in q and x not in q:return False
    return True


def check():
    compares=0
    horn=0
    for opbits in product([0,1],repeat=4):
        ops={c for c,bit in zip('MCNK',opbits) if bit}
        for i in range(40):
            bodies={randterm(2) for _ in range(RNG.randint(1,3))}
            S={TOP}
            for x in bodies:S|=subs(x)
            if len(S)>36:continue
            G={x for x in bodies if RNG.random()<.65}
            # Bound to max subterm size plus 2, no larger synthetic term necessary
            # for S-membership in any supported test.
            threshold=5
            # Bound conjunction generation to avoid combinatorial explosion
            if max(map(size,S))>4:continue
            P=poly(G,S,ops)
            F=full_bounded(G,ops,threshold)
            assert P==F&S,(ops,i,G,P,F&S)
            compares+=1
            # independent exhaustive Horn valuations only for small S
            if len(S)<=9:
                arr=list(S); required=G&set(S)
                good=[]
                for mask in range(1<<len(arr)):
                    h={x for j,x in enumerate(arr) if mask>>j&1}
                    if not required<=h:continue
                    if independently_valid_horn(h,S,ops):good.append(h)
                assert good, (ops,G)
                intersection=set.intersection(*good)
                assert intersection==P,(ops,G,intersection,P)
                horn+=1
    return compares,horn

if __name__=='__main__':
    a,b=check()
    print(f'WEAK_MODAL_VERIFY_OK direct_bounded_closure={a} independent_horn_enumerations={b}')

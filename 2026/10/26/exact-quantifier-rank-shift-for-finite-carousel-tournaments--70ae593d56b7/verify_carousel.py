"""Exact bounded-round game checks for cyclic carousel tournaments.

Run: python verify_carousel.py
All computations use integer arithmetic and Python's standard library.
"""
from functools import lru_cache


def arc(n, x, y):
    d = (y - x) % n
    return 0 < d <= (n - 1) // 2


def anchored_arc(m, s, i, t, j):
    """s,t in {'A','B'}; 1<=i,j<=m. Repeated vertex has no arc."""
    if s == t:
        return i < j
    if s == 'A':
        return j <= i
    return j < i


def check_anchor(up_to=75):
    for m in range(1, up_to + 1):
        n = 2 * m + 1
        anchor = 0
        for s in ('A','B'):
            for i in range(1,m+1):
                x = i if s == 'A' else m+i
                assert arc(n,anchor,x) == (s=='A')
                for t in ('A','B'):
                    for j in range(1,m+1):
                        y = j if t == 'A' else m+j
                        assert arc(n,x,y) == anchored_arc(m,s,i,t,j)
    print('ANCHORED_TWO_CHAIN_IDENTITY_OK m=1..%d' % up_to)


def normalized(n, tup):
    if not tup: return ()
    return tuple((v-tup[0]) % n for v in tup)


def atomic(n,tup):
    out=[]
    for i in range(len(tup)):
        for j in range(i+1,len(tup)):
            if tup[i] == tup[j]: out.append(0)
            elif arc(n,tup[i],tup[j]): out.append(1)
            else: out.append(2)
    return tuple(out)


@lru_cache(None)
def tournament_signature(n,tup,rounds):
    # This is the exact Hintikka recursion, modulo the provable rotation automorphisms.
    a=atomic(n,tup)
    if rounds==0:return (a,)
    extensions=frozenset(tournament_signature(n, normalized(n,tup+(i,)),rounds-1)
                         for i in range(n))
    return (a,extensions)


@lru_cache(None)
def order_signature(m,tup,rounds):
    # Independent exact recursion on finite strict linear orders.
    a=tuple(0 if tup[i]==tup[j] else 1 if tup[i]<tup[j] else 2
            for i in range(len(tup)) for j in range(i+1,len(tup)))
    if rounds==0: return (a,)
    return (a,frozenset(order_signature(m,tup+(i,),rounds-1) for i in range(m)))


def checked_classes(q,ns):
    seen={}
    for n in ns:
        s=tournament_signature(n,(),q)
        seen.setdefault(s,[]).append(n)
    return list(seen.values())


def verify():
    check_anchor(75)
    for q,lim in ((1,35),(2,35),(3,35),(4,35),(5,13)):
        ns=list(range(3,lim+1,2))
        c=checked_classes(q,ns)
        cutoff=max(0,2**(q-1)-1)
        expected=[]
        for n in ns:
            key=min((n-1)//2,cutoff)
            if not expected or expected[-1][0]!=key:expected.append((key,[n]))
            else:expected[-1][1].append(n)
        assert c==[x[1] for x in expected],(q,c,expected)
        print('DIRECT_TOURNAMENT_EF_OK q=%d orders=3..%d classes=%d' % (q,lim,len(c)))
    for q in range(1,5):
        cutoff=2**q-1
        roots={}
        for m in range(1,24):
            roots.setdefault(order_signature(m,(),q),[]).append(m)
        assert len(roots)==cutoff
        for x in roots.values():
            assert {min(z,cutoff) for z in x}=={min(x[0],cutoff)}
        print('DIRECT_LINEAR_ORDER_EF_OK q=%d threshold=%d classes=%d' % (q,cutoff,len(roots)))
    for q in range(1,10):
        cutoff=max(0,2**(q-1)-1)
        assert all((min(m,cutoff)==min(n,cutoff)) == \
                  ((m==n and m<cutoff) or (m>=cutoff and n>=cutoff))
                  for m in range(1,100) for n in range(1,100))
    print('SYMBOLIC_CUTOFF_PARTITION_OK q=1..9 m,n=1..99')
    print('VERIFY_OK')


if __name__=='__main__':verify()

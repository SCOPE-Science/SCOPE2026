import itertools

def std(p):
    s = sorted(p)
    r = {v:i+1 for i,v in enumerate(s)}
    return tuple(r[v] for v in p)

def contains(pat, sub):
    # does pat contain sub as pattern?
    k = len(sub)
    for idx in itertools.combinations(range(len(pat)), k):
        if std([pat[i] for i in idx]) == tuple(sub):
            return True
    return False

def rev(p): return p[::-1]
def comp(p):
    n = len(p); return tuple(n+1-x for x in p)
def inv(p):
    n = len(p); q=[0]*n
    for i,v in enumerate(p): q[v-1]=i+1
    return tuple(q)

def orbit(p):
    s=set(); s.add(tuple(p))
    # dihedral + inverse closure
    cur=set([tuple(p)])
    # generate group by rev, comp, inv
    seen={tuple(p)}
    stack=[tuple(p)]
    while stack:
        q=stack.pop()
        for f in (rev,comp,inv):
            r=tuple(f(list(q)))
            if r not in seen:
                seen.add(r); stack.append(r)
    return seen

A=(1,2,3,6,5,4); B=(3,2,1,6,5,4)
print("A in U:", not contains(A,(2,4,1,3)) and not contains(A,(3,1,4,2)))
print("B in U:", not contains(B,(2,4,1,3)) and not contains(B,(3,1,4,2)))
oA=orbit(A); oB=orbit(B)
print("orbit A size:",len(oA), sorted(oA))
print("orbit B size:",len(oB), sorted(oB))
print("disjoint:", oA.isdisjoint(oB))
# dihedral only
def dorbit(p):
    seen={tuple(p)}; stack=[tuple(p)]
    while stack:
        q=stack.pop()
        for f in (rev,comp):
            r=tuple(f(list(q)))
            if r not in seen: seen.add(r); stack.append(r)
    return seen
print("dihedral A:", len(dorbit(A)), sorted(dorbit(A)))
print("dihedral B:", len(dorbit(B)), sorted(dorbit(B)))
print("A contains 132:", contains(A,(1,3,2)), "avoids 231:", not contains(A,(2,3,1)))
print("B contains 132:", contains(B,(1,3,2)), "avoids 231:", not contains(B,(2,3,1)))

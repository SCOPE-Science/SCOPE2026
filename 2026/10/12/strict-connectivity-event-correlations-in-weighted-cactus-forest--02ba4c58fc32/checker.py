"""Exact-arithmetic checks for the cactus arboreal-gas connectivity theorem.

Python 3, standard library only. These checks supplement the general proof;
finite tests do not establish the all-graph and all-weight theorem.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations, product

COUNT = 0


def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)


def macro_mass(odds, allowed):
    """Unnormalized mass of nonempty failed-arc subsets."""
    ans = Fraction(0)
    for flags in product((0, 1), repeat=len(odds)):
        failed = frozenset(i for i, flag in enumerate(flags) if flag)
        if failed and allowed(failed):
            term = Fraction(1)
            for i in failed:
                term *= odds[i]
            ans += term
    return ans


def cycle_algebra():
    values = (Fraction(1, 3), Fraction(1, 1), Fraction(3, 2), Fraction(7, 2))
    for a, b, c in product(values, repeat=3):
        odds = (a, b, c)
        A = lambda s: s <= {0} or s <= {1, 2}
        B = lambda s: s <= {0, 1} or s <= {2}
        z = (1+a)*(1+b)*(1+c)-1
        u = macro_mass(odds, A)
        v = macro_mass(odds, B)
        w = macro_mass(odds, lambda s: A(s) and B(s))
        numerator = w*z-u*v
        exact = a*c*(a+b+c+a*b+b*c)
        check(numerator == exact and numerator > 0, '3 terminals')
    for a, b, c, d in product(values, repeat=4):
        odds = (a, b, c, d)
        z = (1+a)*(1+b)*(1+c)*(1+d)-1
        L = a+b+c+d
        T = a*b*c+a*b*d+a*c*d+b*c*d
        A = lambda s: s <= {0, 1} or s <= {2, 3}
        B = lambda s: s <= {1, 2} or s <= {0, 3}
        u = macro_mass(odds, A)
        v = macro_mass(odds, B)
        w = macro_mass(odds, lambda s: A(s) and B(s))
        exact = L*(a*c+b*d)+L*T-(a*b+c*d)*(b*c+a*d)+L*a*b*c*d
        check(w*z-u*v == exact and exact > 0, 'crossing 4 terminals')
        A = lambda s: s <= {0} or s <= {1, 2, 3}
        B = lambda s: s <= {2} or s <= {0, 1, 3}
        u = macro_mass(odds, A)
        v = macro_mass(odds, B)
        w = macro_mass(odds, lambda s: A(s) and B(s))
        exact = a*c*((1+b)*(1+d)*(1+a+c)-1)
        check(w*z-u*v == exact and exact > 0, 'noncrossing 4 terminals')


def endpoints(block):
    vertices = set()
    for x,y in block:
        vertices.add(x); vertices.add(y)
    return vertices


def block_path(u,v,blocks,n):
    graph = [[] for _ in range(n+len(blocks))]
    for i,block in enumerate(blocks):
        node=n+i
        for vertex in endpoints(block):
            graph[node].append(vertex)
            graph[vertex].append(node)
    prev={u:-1}
    queue=deque([u])
    while queue and v not in prev:
        z=queue.popleft()
        for nxt in graph[z]:
            if nxt not in prev:
                prev[nxt]=z
                queue.append(nxt)
    check(v in prev,'block-incidence connectivity')
    out=set()
    z=v
    while z!=u:
        if z>=n:out.add(z-n)
        z=prev[z]
    return out


def weighted_cactus(blocks,n,seed):
    edges=[e for block in blocks for e in block]
    m=len(edges)
    assert len(set(tuple(sorted(e)) for e in edges)) == m
    weights=[(i+seed)%5+1 for i in range(m)]
    pairs=list(combinations(range(n),2))
    paths=[block_path(a,b,blocks,n) for a,b in pairs]
    single=[0]*len(pairs)
    joint=[[0]*len(pairs) for _ in pairs]
    total=0
    active_forests=0
    for flags in product((0,1),repeat=m):
        par=list(range(n))
        def root(x):
            while par[x]!=x:
                x=par[x]
            return x
        mult=1
        good=True
        for i,(a,b) in enumerate(edges):
            if flags[i]:
                ra,rb=root(a),root(b)
                if ra==rb:
                    good=False
                    break
                par[ra]=rb
                mult*=weights[i]
        if not good:
            continue
        total += mult
        active_forests += 1
        active=[i for i,(a,b) in enumerate(pairs) if root(a)==root(b)]
        for i in active:
            single[i]+=mult
            for j in active:
                joint[i][j]+=mult
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            numerator=joint[i][j]*total-single[i]*single[j]
            should_be_strict=bool(paths[i]&paths[j])
            check((numerator>0) if should_be_strict else (numerator==0),
                  'cactus strict/equality: blocks=%r pairs=%r %r numerator=%s' %
                  (blocks,pairs[i],pairs[j],numerator))
    return active_forests,m,n


def cyc(v):
    return list(zip(v,v[1:]+v[:1]))


def run():
    cycle_algebra()
    examples=[
        ([cyc([0,1,2])],3),
        ([cyc([0,1,2,3])],4),
        ([cyc([0,1,2,3,4,5])],6),
        ([cyc([0,1,2]),cyc([2,3,4])],5),
        ([cyc([0,1,2]),[(2,3)],cyc([3,4,5,6])],7),
        ([cyc([0,1,2]),cyc([2,3,4]),[(4,5)],cyc([5,6,7])],8),
        ([[(0,1)],[(1,2)],[(2,3)],[(3,4)]],5),
    ]
    for blocks,n in examples:
        for seed in (1,3):
            weighted_cactus(blocks,n,seed)
    print('PASS:',COUNT,'exact-rational/integer assertions on cycle identities and full graph forest laws.')
    print('Scope: finite checked instances only; all-weight and all-cactus claims use proof.')

if __name__=='__main__':
    run()

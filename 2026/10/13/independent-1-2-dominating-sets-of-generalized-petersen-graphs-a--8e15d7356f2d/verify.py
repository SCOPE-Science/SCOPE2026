"""Exact independent [1,2]-domination calculations for generalized Petersen P(n,2).

Requires Python 3 standard library only. All graph labels refer to the mathematical graph.
"""
from collections import Counter
from itertools import product
from math import ceil

ALPHABET = ((0, 0), (1, 0), (0, 1))
STATES = list(product(range(3), repeat=4))
POSITION = {s:i for i,s in enumerate(STATES)}
WEIGHT = (0,1,1)


def admissible(t):
    a0,b0=ALPHABET[t[0]]
    a1,b1=ALPHABET[t[1]]
    a2,b2=ALPHABET[t[2]]
    a3,b3=ALPHABET[t[3]]
    a4,b4=ALPHABET[t[4]]
    if a2 and (a1 or a3): return False
    if b2 and (b0 or b4): return False
    if not a2 and not 1<=a1+a3+b2<=2: return False
    if not b2 and not 1<=b0+b4+a2<=2: return False
    return True

ARCS = [[] for _ in STATES]
for i,s in enumerate(STATES):
    for k in range(3):
        if admissible(s+(k,)):
            ARCS[i].append((POSITION[s[1:]+(k,)],WEIGHT[k]))
assert len(STATES)==81 and sum(map(len,ARCS))==89


def cyclic_components():
    # Independent Kosaraju calculation of SCC decomposition.
    fwd=[[v for v,_ in row] for row in ARCS]
    rev=[[] for _ in STATES]
    for u,row in enumerate(fwd):
        for v in row:rev[v].append(u)
    seen=set();order=[]
    def dfs(u):
        seen.add(u)
        for v in fwd[u]:
            if v not in seen:dfs(v)
        order.append(u)
    for u in range(len(STATES)):
        if u not in seen:dfs(u)
    seen.clear();components=[]
    def back(u,comp):
        seen.add(u);comp.add(u)
        for v in rev[u]:
            if v not in seen:back(v,comp)
    for u in reversed(order):
        if u not in seen:
            comp=set();back(u,comp)
            if len(comp)>1 or any(v==u for v,_ in ARCS[u]):components.append(comp)
    return sorted(components,key=lambda c:(-len(c),min(c)))


def simple_cycles(nodes):
    """Enumerate each directed simple cycle once, up to cyclic rotation."""
    nodes=set(nodes);out=[]
    for root in sorted(nodes):
        def walk(u,path,used,weight):
            for v,w in ARCS[u]:
                if v==root:
                    out.append((frozenset(path),len(path),weight+w))
                elif v in nodes and v>root and v not in used:
                    walk(v,path+[v],used|{v},weight+w)
        walk(root,[root],{root},0)
    return out


def determinants_by_cycle_collections(cycles):
    """det(I-A): sum over vertex-disjoint directed cycles with (-1)^number."""
    ret=Counter({(0,0):1})
    def walk(i,used,ell,weight,sign):
        if i==len(cycles):
            if ell:ret[ell,weight]+=sign
            return
        walk(i+1,used,ell,weight,sign)
        vertices,l,w=cycles[i]
        if not (vertices & used):
            walk(i+1,used|vertices,ell+l,weight+w,-sign)
    walk(0,frozenset(),0,0,1)
    return {key:v for key,v in ret.items() if v}

COMPONENTS=cyclic_components()
assert list(map(len,COMPONENTS))==[17,3,3]
CYCLES=[simple_cycles(c) for c in COMPONENTS]
assert sorted((l,w) for _,l,w in CYCLES[0]) == [(5,4),(6,4),(6,4),(6,4),(7,5),(12,8)]
assert [sorted((l,w) for _,l,w in cs) for cs in CYCLES[1:]] == [[(3,2)],[(3,2)]]
assert determinants_by_cycle_collections(CYCLES[0])=={(0,0):1,(5,4):-1,(6,4):-3,(7,5):-1}
for c in CYCLES[1:]:
    assert determinants_by_cycle_collections(c)=={(0,0):1,(3,2):-1}


def trace_poly(n):
    """Exact transfer trace; polynomial represented by Counter of weights."""
    total=Counter()
    for root in range(len(STATES)):
        now={root:Counter({0:1})}
        for _ in range(n):
            nxt={}
            for s,pol in now.items():
                for t,w in ARCS[s]:
                    dst=nxt.setdefault(t,Counter())
                    for degree,cnt in pol.items():dst[degree+w]+=cnt
            now=nxt
        total.update(now.get(root,{}))
    return +total


def closed_polynomials(maxn):
    """Coefficient extraction from claimed exact rational series, all integer arithmetic."""
    p=[Counter() for _ in range(maxn+1)]
    num={5:Counter({4:5}),6:Counter({4:18}),7:Counter({5:7})}
    for n in range(5,maxn+1):
        p[n].update(num.get(n,{}))
        for shift,degree,mult in ((5,4,1),(6,4,3),(7,5,1)):
            if n>=shift:
                for k,v in p[n-shift].items():p[n][k+degree]+=mult*v
    second=[Counter() for _ in range(maxn+1)]
    for n in range(6,maxn+1,3):
        second[n][4+2*((n-6)//3)]=6
    return [p[n]+second[n] for n in range(maxn+1)]

FORM=closed_polynomials(100)
for n in range(5,31):
    assert trace_poly(n)==FORM[n],(n,trace_poly(n),FORM[n])
for n in range(5,101):
    if n==8:assert not FORM[n];continue
    assert FORM[n]
    minimum=ceil(2*n/3)+(n%6==4)
    assert min(FORM[n])==minimum,(n,min(FORM[n]),minimum)


def brute(n):
    # Independent graph-neighbor implementation: does not use the transfer states.
    vertex_count=2*n
    adjacency=[0]*vertex_count
    edges=set()
    for i in range(n):
        for x,y in ((i,(i+1)%n),(i,n+i),(n+i,n+(i+2)%n)):
            if x>y:x,y=y,x
            edges.add((x,y))
    for x,y in edges:
        adjacency[x]|=1<<y
        adjacency[y]|=1<<x
    polynomial=Counter()
    for mask in range(1<<vertex_count):
        is_independent=True
        selected=mask
        while selected:
            bit=selected&-selected;v=bit.bit_length()-1
            if adjacency[v]&mask:
                is_independent=False;break
            selected-=bit
        if not is_independent:continue
        okay=True
        for v in range(vertex_count):
            if not (mask>>v)&1 and not (1<=(mask&adjacency[v]).bit_count()<=2):
                okay=False;break
        if okay:polynomial[mask.bit_count()]+=1
    return +polynomial

for n in range(5,11):assert brute(n)==FORM[n],(n,brute(n),FORM[n])

# Check concrete shared-state closed walks used for every admissible order.
root=POSITION[(0,1,2,2)]
def witness(word):
    current=root
    for letter in word:
        target='0UV'.index(letter)
        transitions=[t for t,_ in ARCS[current] if STATES[t][-1]==target]
        assert len(transitions)==1,(word,current,letter)
        current=transitions[0]
    assert current==root,word
for word in ('U0UVV','0U0UVV','U0U0UVV'):
    witness(word)
assert not FORM[8] and FORM[9]==Counter({6:6})
print('VERIFY_OK states=81 arcs=89 cyclic_SCCs=17+3+3 simple_cycles=6+1+1 exact_det=passed trace_n=5..30 brute_n=5..10 brute_subsets=1397760 minimum_n=5..100 exceptional_n=8')

"""Finite independent checks of tripartite synchronous random-neighbor-majority.

Python 3 standard library only. Exact transition SUPPORT is checked, not an
approximation by random trials. This program corroborates the general proof.
"""
from itertools import product
from fractions import Fraction


def sink_sccs(adj):
    # Kosaraju, iterative DFS, avoids external dependencies.
    nodes=list(adj)
    seen=set(); order=[]
    for v in nodes:
        if v in seen:continue
        seen.add(v); stack=[(v,iter(adj[v]))]
        while stack:
            x,it=stack[-1]
            try:
                y=next(it)
                if y not in seen:
                    seen.add(y);stack.append((y,iter(adj[y])))
            except StopIteration:
                order.append(x);stack.pop()
    rev={v:[] for v in adj}
    for v,neigh in adj.items():
        for w in neigh:rev[w].append(v)
    seen=set(); components=[]
    for v in reversed(order):
        if v in seen:continue
        comp=set([v]);seen.add(v);stack=[v]
        while stack:
            x=stack.pop()
            for y in rev[x]:
                if y not in seen:
                    seen.add(y);comp.add(y);stack.append(y)
        if all(y in comp for x in comp for y in adj[x]):components.append(frozenset(comp))
    return set(components)


def macro_states(a,b,c):
    sizes=(a,b,c); out={}
    for counts in product(*(range(q+1) for q in sizes)):
        choices=[]
        for i,k in enumerate(sizes):
            blue=sum(counts)-counts[i]; degree=sum(sizes)-k
            if blue*2>degree: choices.append((k,))
            elif blue*2<degree: choices.append((0,))
            else: choices.append(tuple(range(k+1)))
        out[counts]=tuple(product(*choices))
    return out


def expected_macro(a,b,c):
    sizes=(a,b,c); n=sum(sizes)
    zero=(0,0,0); one=sizes
    classes={frozenset([zero]),frozenset([one])}
    mx=max(sizes); tops=[i for i,v in enumerate(sizes) if v==mx]
    if len(tops)==1:
        i=tops[0];s1=list(sizes);s1[i]=0
        s2=[0,0,0];s2[i]=sizes[i]
        classes.add(frozenset([tuple(s1),tuple(s2)]))
    if len(tops)==2:
        i,j=tops; k=next(q for q in range(3) if q not in tops)
        states=set()
        for small_count in range(sizes[k]+1):
            for phase in (0,1):
                x=[0,0,0];x[i]=sizes[i]*phase;x[j]=sizes[j]*(1-phase);x[k]=small_count
                states.add(tuple(x))
        classes.add(frozenset(states))
    return classes


def micro_states(a,b,c):
    sizes=(a,b,c);starts=(0,a,a+b); n=sum(sizes)
    masks=[((1<<q)-1)<<st for st,q in zip(starts,sizes)]
    out={}
    for x in range(1<<n):
        options=[0]
        for size,mask,start in zip(sizes,masks,starts):
            external=x & ~mask
            blues=external.bit_count(); deg=n-size
            if 2*blues>deg:choices=[mask]
            elif 2*blues<deg:choices=[0]
            else:choices=[q<<start for q in range(1<<size)]
            options=[(a|b) for a in options for b in choices]
        out[x]=tuple(options)
    return out


def expected_micro(a,b,c):
    sizes=(a,b,c);starts=(0,a,a+b);n=sum(sizes)
    ms=[((1<<q)-1)<<start for q,start in zip(sizes,starts)]
    classes={frozenset([0]),frozenset([(1<<n)-1])}
    mx=max(sizes);tops=[i for i,u in enumerate(sizes) if u==mx]
    if len(tops)==1:
        i=tops[0]
        classes.add(frozenset([ms[i],((1<<n)-1)^ms[i]]))
    if len(tops)==2:
        i,j=tops;k=next(t for t in range(3) if t not in tops)
        small=[q<<starts[k] for q in range(1<<sizes[k])]
        classes.add(frozenset(m|ms[i] for m in small)|frozenset(m|ms[j] for m in small))
    return classes


def edge_cut(x,sizes):
    # Direct enumeration of disagreements along all cross-part edges.
    starts=[0,sizes[0],sizes[0]+sizes[1]]
    counts=[((x >> st) & ((1<<size)-1)).bit_count() for st,size in zip(starts,sizes)]
    return sum(counts[i]*(sizes[j]-counts[j]) +
               (sizes[i]-counts[i])*counts[j]
               for i in range(3) for j in range(i+1,3))


def transition_probs(x,sizes):
    starts=[0,sizes[0],sizes[0]+sizes[1]]
    masks=[((1<<q)-1)<<st for st,q in zip(starts,sizes)]
    n=sum(sizes); choices=[(0,Fraction(1))]
    for size,mask,start in zip(sizes,masks,starts):
        b=(x & ~mask).bit_count();deg=n-size
        if 2*b>deg:part=[(mask,Fraction(1))]
        elif 2*b<deg:part=[(0,Fraction(1))]
        else:part=[(t<<start,Fraction(1,2**size)) for t in range(1<<size)]
        choices=[(v|u,p*q) for v,p in choices for u,q in part]
    return dict(choices)


def run():
    macro=0; micro=0; examples=[]
    for a,b,c in product(range(1,7),repeat=3):
        actual=sink_sccs(macro_states(a,b,c))
        expected=expected_macro(a,b,c)
        assert actual==expected,(a,b,c,actual,expected)
        macro+=1
    for a,b,c in product(range(1,4),repeat=3):
        actual=sink_sccs(micro_states(a,b,c))
        expected=expected_micro(a,b,c)
        assert actual==expected,(a,b,c,actual,expected)
        micro+=1
    for a,b,c in [(1,1,1),(1,2,2),(2,3,3),(2,2,3),(3,3,3),(2,4,4)]:
        classes=expected_micro(a,b,c)
        examples.append(((a,b,c),sorted(map(len,classes))))
    # For tied largest a=b>c, verify the unbiased redraw of every C vertex,
    # and exact phase swap in the full micro transition support.
    noise=0; cuts=0
    for L in range(2,6):
        for s in range(1,L):
            adj=micro_states(L,L,s)
            masks=[(1<<L)-1,((1<<L)-1)<<L]
            for phase in (0,1):
                hard=masks[phase]
                for tail in range(1<<s):
                    state=hard|(tail<<(2*L))
                    nxt=set(adj[state])
                    expected={masks[1-phase]|(v<<(2*L)) for v in range(1<<s)}
                    assert nxt==expected,(L,s,phase,tail)
                    noise+=1
                    # Independently recompute all cross-part disagreement edges.
                    assert edge_cut(state,(L,L,s))==L*(L+s)
                    probs=transition_probs(state,(L,L,s))
                    assert set(probs)==expected
                    assert all(p==Fraction(1,2**s) for p in probs.values())
                    assert sum(probs.values())==1
                    cuts+=1
    print('VERIFIED macro triples:',macro,'micro triples:',micro,
          'tied-class support checks:',noise,'cut checks:',cuts)
    print('Sample absorbing-class state sizes:',examples)

if __name__=='__main__':run()

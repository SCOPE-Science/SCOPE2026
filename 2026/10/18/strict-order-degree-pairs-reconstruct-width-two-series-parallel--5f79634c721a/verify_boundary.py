"""Exhaustive series/parallel poset generator and direct automorphism checker.
This verifier is independent of the normal-form reconstruction implementation.
Only standard Python modules are used.
"""
from functools import lru_cache
from itertools import product,permutations
from collections import Counter,defaultdict

@lru_cache(None)
def compositions(n):
    if n==0:return ((),)
    return tuple((i,)+tail for i in range(1,n+1) for tail in compositions(n-i))
@lru_cache(None)
def partitions(n,k=1):
    if not n:return ((),)
    return tuple((j,)+tail for j in range(k,n+1) for tail in partitions(n-j,j))
@lru_cache(None)
def all_sp(n):
    if n==1:return (('v',),)
    result=set()
    for sizes in compositions(n):
        if len(sizes)<2:continue
        for children in product(*(all_sp(sz) for sz in sizes)):
            if all(ch[0]!='s' for ch in children):
                result.add(('s',)+children)
    for sizes in partitions(n):
        if len(sizes)<2:continue
        for children in product(*(all_sp(sz) for sz in sizes)):
            if all(ch[0]!='p' for ch in children):
                result.add(('p',)+tuple(sorted(children)))
    return tuple(sorted(result))

def build(t):
    if t==('v',):return 1,set()
    children=list(map(build,t[1:])); offs=[];o=0
    for sz,E in children:offs.append(o);o+=sz
    E={(i+offs[k],j+offs[k]) for k,(sz,ee) in enumerate(children) for i,j in ee}
    if t[0]=='s':
        for k,(sz,_) in enumerate(children):
            for l in range(k+1,len(children)):
                E.update((i+offs[k],j+offs[l]) for i in range(sz) for j in range(children[l][0]))
    return o,E

def width(n,E):
    comparability={(min(i,j),max(i,j)) for i,j in E}
    return max((len(sub) for m in range(1<<n)
               for sub in [[v for v in range(n) if (m>>v)&1]]
               if all((i,j) not in comparability for i in sub for j in sub if i<j)),default=0)

def orbit_partition(n,E):
    parent=list(range(n))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for perm in permutations(range(n)):
        if all(((perm[i],perm[j]) in E) for i,j in E):
            # an edge-preserving bijection is an automorphism for finite digraphs
            for i,j in enumerate(perm):parent[root(i)]=root(j)
    return [root(i) for i in range(n)]

def run():
    failures=[]
    for n in range(1,7):
        failures_n=[]
        width2=0
        for t in all_sp(n):
            size,E=build(t);assert size==n
            lower=Counter(j for i,j in E);upper=Counter(i for i,j in E)
            deg=[(lower[i],upper[i]) for i in range(n)]
            orbits=orbit_partition(n,E)
            same=lambda i,j:orbits[i]==orbits[j]
            correct=all((deg[i]==deg[j])==same(i,j) for i in range(n) for j in range(n))
            w=width(n,E)
            if w<=2:
                width2+=1
                assert correct,('width-two failure',n,t)
            if not correct:failures_n.append((w,t,deg))
        print('n=%d canonical_sp=%d width_at_most_two=%d degree_orbit_failures=%d'%(
            n,len(all_sp(n)),width2,len(failures_n)))
        if n<5: assert not failures_n
        if n==5:
            assert len(failures_n)==2
            assert all(w==3 for w,t,deg in failures_n)
            for w,t,deg in failures_n:print('five_point_witness width=%d structure=%r degree_pairs=%r'%(w,t,deg))
        failures.extend(failures_n)
    print('BOUNDARY_VERIFY_PASS direct_automorphism_enumeration=yes')
if __name__=='__main__':run()

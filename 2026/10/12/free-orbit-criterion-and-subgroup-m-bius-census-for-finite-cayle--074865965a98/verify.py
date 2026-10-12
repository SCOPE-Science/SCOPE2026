#!/usr/bin/env python3
"""Finite checks for the regular involution-frame theorem (Python standard library)."""
from itertools import product, permutations
from collections import deque
from math import factorial
from random import Random

class FiniteGroup:
    def __init__(self, elements, identity, multiply, generators):
        self.elements=tuple(elements)
        self.idx={g:i for i,g in enumerate(self.elements)}
        self.n=len(self.elements)
        self.e=self.idx[identity]
        self.mul=tuple(tuple(self.idx[multiply(a,b)] for b in self.elements)
                       for a in self.elements)
        self.s=tuple(self.idx[x] for x in generators)
        assert all(self.mul[x][x]==self.e for x in self.s)
        assert self.generated(self.s)==frozenset(range(self.n))
        self.left=tuple(tuple(self.mul[s][i] for i in range(self.n)) for s in self.s)
        self.right=tuple(tuple(self.mul[i][g] for i in range(self.n)) for g in range(self.n))
    def generated(self, gen):
        seen={self.e}; queue=[self.e]
        while queue:
            x=queue.pop()
            for s in gen:
                for y in (self.mul[x][s],self.mul[s][x]):
                    if y not in seen:seen.add(y);queue.append(y)
        return frozenset(seen)
    def subgroups(self):
        seed=frozenset({self.e}); seen={seed}; queue=[seed]
        while queue:
            H=queue.pop()
            for g in range(self.n):
                if g in H:continue
                K=self.generated(tuple(H)+(g,))
                if K not in seen: seen.add(K);queue.append(K)
        return sorted(seen,key=lambda H:(len(H),tuple(sorted(H))))
    def free_polynomial(self,q):
        subs=self.subgroups(); mob={}
        for H in subs:
            if len(H)==1:mob[H]=1
            else:mob[H]=-sum(mob[K] for K in subs if K!=H and K.issubset(H))
        return sum(mob[H]*q**(self.n//len(H)) for H in subs),len(subs)
    def canonical(self,word):
        return min(tuple(word[self.right[g][i]] for i in range(self.n)) for g in range(self.n))
    def orbit_size(self,word):
        return len({tuple(word[self.right[g][i]] for i in range(self.n)) for g in range(self.n)})

def dihedral(m):
    def multiply(x,y):
        a,b=x; c,d=y
        return ((a+(-1 if b else 1)*c)%m,b^d)
    el=[(a,b) for b in range(2) for a in range(m)]
    return FiniteGroup(el,(0,0),multiply,((0,1),(1%m,1)))

def symmetric4():
    el=list(permutations(range(4)))
    def mul(x,y):return tuple(x[y[i]] for i in range(4))
    gens=[]
    for i in range(3):
        s=list(range(4));s[i],s[i+1]=s[i+1],s[i]
        gens.append(tuple(s))
    return FiniteGroup(el,tuple(range(4)),mul,gens)

def number_of_types(grp, colors, copies):
    n=grp.n; N=n*copies
    classes=[colors.index(v) for v in colors]  # arbitrary labels; only equalities matter
    # Encode partitions canonically each step.
    for _ in range(N+1):
        keys=[]
        for i in range(N):
            base=(i//n)*n; x=i%n
            keys.append((classes[i],tuple(tuple(sorted({classes[i],classes[base+grp.left[j][x]]}))
                for j in range(len(grp.s)))))
        idmap={key:i for i,key in enumerate(sorted(set(keys)))}
        revised=[idmap[key] for key in keys]
        if len(set(revised))==len(set(classes)):
            return len(set(revised))
        classes=revised
    raise AssertionError('partition failed to stabilize')

def classification(grp,colors,copies):
    orbits=[]
    for k in range(copies):
        w=colors[k*grp.n:(k+1)*grp.n]
        if grp.orbit_size(w)<grp.n:return False
        c=grp.canonical(w)
        if c in orbits:return False
        orbits.append(c)
    return True

def direct_closure(grp,colors,copies,bitcount):
    N=grp.n*copies; full=(1<<N)-1
    # Only bit-based propositional colors (not one predicate per abstract color).
    starts={0,full}
    for j in range(bitcount):
        starts.add(sum(((c>>j)&1)<<i for i,c in enumerate(colors)))
    seen=set(starts);queue=deque(starts)
    while queue:
        x=queue.popleft()
        add={full^x}
        for j in range(len(grp.s)):
            v=0
            for i in range(N):
                base=(i//grp.n)*grp.n
                if (x>>i)&1 or (x>>(base+grp.left[j][i%grp.n]))&1:
                    v|=1<<i
            add.add(v)
        for y in list(seen):
            add.add(x&y);add.add(x|y)
        for z in add-seen:
            seen.add(z);queue.append(z)
    return len(seen)

def primitive(q,m):
    def mobius(n):
        primes=[];p=2
        while p*p<=n:
            if n%p==0:
                n//=p
                if n%p==0:return 0
                primes.append(p)
            p+=1
        if n>1:primes.append(n)
        return (-1)**len(primes)
    return sum(mobius(m//d)*q**d for d in range(1,m+1) if m%d==0)

single=0;multi=0;closures=0;random_checks=0;mobius_cases=0
for m in (1,2,3,4):
    group=dihedral(m)
    for q in ((2,3,4) if m<=2 else (2,3)):
        A,subcount=group.free_polynomial(q)
        expected=primitive(q*q,m)-m*primitive(q,m)
        assert A==expected,(m,q,A,expected)
        mobius_cases+=1
        for w in product(range(q),repeat=group.n):
            full=number_of_types(group,w,1)==group.n
            direct=group.orbit_size(w)==group.n
            assert full==direct,(m,q,w,full,direct)
            single+=1
            # Exactly independently tally the free colorings via enumeration.
        enum=sum(group.orbit_size(w)==group.n for w in product(range(q),repeat=group.n))
        assert enum==A,(m,q,enum,A)
for m,c,q in ((1,2,2),(1,3,3),(2,2,2),(2,3,2),(3,2,2)):
    group=dihedral(m)
    A,_=group.free_polynomial(q)
    expected=1
    for i in range(c):expected*=A-group.n*i
    observed=0
    for w in product(range(q),repeat=group.n*c):
        full=number_of_types(group,w,c)==group.n*c
        good=classification(group,w,c)
        assert full==good,(m,c,q,w,full,good)
        observed+=good;multi+=1
    assert observed==expected,(m,c,q,observed,expected)
for group,c,bitcount in ((dihedral(1),2,1),(dihedral(2),1,1),(dihedral(2),2,1),(dihedral(3),1,1)):
    N=group.n*c
    for w in product(range(2),repeat=N):
        T=number_of_types(group,w,c)
        size=direct_closure(group,w,c,bitcount)
        assert size==2**T,(group.n,c,w,size,T)
        closures+=1
# Test a non-dihedral involution-generated group: S4 (permutation group).
s4=symmetric4()
for q in (2,3):
    A,number_subgroups=s4.free_polynomial(q)
    assert number_subgroups==30,(number_subgroups,A)
    assert 0<=A<=q**24 and A%24==0
    mobius_cases+=1
    rng=Random(7831+q)
    for _ in range(300):
        w=tuple(rng.randrange(q) for i in range(24))
        assert (number_of_types(s4,w,1)==24)==(s4.orbit_size(w)==24)
        random_checks+=1
print('VERIFY_OK single_modal_partition_checks',single,
    'multi_component_checks',multi,
    'direct_boolean_closures',closures,
    'subgroup_mobius_and_dihedral_cases',mobius_cases,
    'symmetric4_random_checks',random_checks,
    'symmetric4_subgroups',len(s4.subgroups()))
print('EXAMPLES D2 q2 free',dihedral(2).free_polynomial(2)[0],
    'D3 q2 free',dihedral(3).free_polynomial(2)[0],
    'S4 q2 free',s4.free_polynomial(2)[0])

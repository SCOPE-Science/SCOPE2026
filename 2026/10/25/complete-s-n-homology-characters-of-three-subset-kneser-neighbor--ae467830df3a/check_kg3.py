"""Exact finite cross-check of equivariant neighborhood Euler-character formula."""
from itertools import combinations
from collections import defaultdict
from math import factorial


def parts(n,minimum=1):
    if n==0:
        yield ()
    for i in range(minimum,n+1):
        for rem in parts(n-i,i):
            yield (i,)+rem

def perm(shape):
    p=list(range(sum(shape))); q=0
    for j in shape:
        for x in range(j):p[q+x]=q+(x+1)%j
        q+=j
    return p

def dp(n,p):
    visited=set(); orbs=[]
    for triple in combinations(range(n),3):
        if triple in visited: continue
        cur=triple; orbit=[]; support=0
        while cur not in visited:
            visited.add(cur); orbit.append(cur)
            for v in cur:support |= 1<<v
            cur=tuple(sorted(p[v] for v in cur))
        orbs.append(support)
    counts={0:1}
    for support in orbs:
        nex=counts.copy()
        for state,v in counts.items():
            nex[state|support]=nex.get(state|support,0)-v
        counts={k:v for k,v in nex.items() if v}
    return sum(v for mask,v in counts.items() if mask.bit_count()<=n-3),len(orbs)

def Q(a,b):
    return (a**4-10*a**3-4*a*a*b+31*a*a+12*a*b-30*a+4*b*b-12*b+4)//4

def sign(p):
    n=len(p);c=0;seen=set()
    for i in range(n):
        if i in seen:continue
        c+=1;cur=i
        while cur not in seen:seen.add(cur);cur=p[cur]
    return (-1)**(n-c)

def run():
    runs=0
    for n in range(6,13):
        for shape in parts(n):
            p=perm(shape);a=shape.count(1);b=shape.count(2)
            signedface,orbit_count=dp(n,p)
            # reduced chain Euler trace = -sum_{faces including empty}(-1)^orbits
            # actual rational H_{n-6} char = (-1)^{n-6}*(-signedface)
            predicted=sign(p)*Q(a,b)
            derived=(-1)**(n-6)*(-signedface)
            assert predicted==derived,(n,shape,predicted,derived)
            runs+=1
        expected=((n-5)*(n-3)*(n-2)*n)//4+1
        assert Q(n,0)==expected,(n,Q(n,0),expected)
    # Orthogonality checks for trivial and sign isotypic multiplicities.
    from collections import Counter
    for n in range(6,13):
        invariant_num=sign_num=0
        for shape in parts(n):
            z=1
            for length,multiplicity in Counter(shape).items():
                z*=length**multiplicity*factorial(multiplicity)
            num=factorial(n)//z
            a=shape.count(1);b=shape.count(2)
            invariant_num+=num*sign(perm(shape))*Q(a,b)
            sign_num+=num*Q(a,b)
        assert invariant_num==sign_num==0,(n,invariant_num,sign_num)
    print('KG3_FULL_AND_ALTERNATING_SYMMETRY_QUOTIENT_RATIONAL_ACYCLICITY_CHECKED')
    print('KG3_COMPLETE_CONJUGACY_CLASS_CHARACTER_VERIFIED',runs)
    print('KG3_KNOWN_WEDGE_RANKS_VERIFIED n=6..12')
if __name__=='__main__':run()

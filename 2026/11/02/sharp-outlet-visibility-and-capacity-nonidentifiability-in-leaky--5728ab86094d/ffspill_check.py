"""Exact-rational reproducibility checks for steady leaky fill-and-spill trees.

Usage: python ffspill_check.py
No external dependencies.  All arithmetic in the tests uses fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import permutations
import random


def water_tree(parent, weight, leak, spill, caps, intensity):
    """Return every upward spill, evaluated leaves-to-root (root is node 0).
    Parent indices must be smaller than child indices.
    """
    n = len(parent)
    beta = [spill[i]/(spill[i]+leak[i]) for i in range(n)]
    out = [F(0) for _ in range(n)]
    for i in range(n-1, -1, -1):
        feed = weight[i]*intensity + sum((out[j] for j in range(i+1,n) if parent[j]==i),F(0))
        out[i] = beta[i]*max(F(0),feed-leak[i]*caps[i])
    return out


def realize_targets(parent,weight,leak,spill,target):
    """Choose positive capacities to realize specified positive activation intensities."""
    n=len(parent)
    caps=[F(0)]*n
    for i in range(n-1,-1,-1):
        partial=water_tree(parent,weight,leak,spill,caps,target[i])
        # Only children matter here.  The current node's dummy capacity is immaterial.
        feed=weight[i]*target[i]+sum((partial[j] for j in range(i+1,n) if parent[j]==i),F(0))
        caps[i]=feed/leak[i]
    return caps


def slope_jump(parent,weight,leak,spill,caps,t):
    h=F(1,10000)
    a=water_tree(parent,weight,leak,spill,caps,t-h)[0]
    b=water_tree(parent,weight,leak,spill,caps,t)[0]
    c=water_tree(parent,weight,leak,spill,caps,t+h)[0]
    return (c-2*b+a)/h


def predicted_visible(parent,target,i):
    j=i
    while j!=0:
        j=parent[j]
        if not target[j]<target[i]:
            return False
    return True


def check_one(parent,weight,leak,spill,target):
    caps=realize_targets(parent,weight,leak,spill,target)
    assert min(caps)>0
    beta=[spill[i]/(spill[i]+leak[i]) for i in range(len(parent))]
    # Each target is exact: the node is dry just to its left and spills to its right.
    h=F(1,10000)
    for i,t in enumerate(target):
        assert water_tree(parent,weight,leak,spill,caps,t)[i]==0
        assert water_tree(parent,weight,leak,spill,caps,t-h)[i]==0
        assert water_tree(parent,weight,leak,spill,caps,t+h)[i]>0
        observed=slope_jump(parent,weight,leak,spill,caps,t)
        assert (observed>0)==predicted_visible(parent,target,i),(parent,target,i,observed)
        assert observed>=0
        if observed>0:
            # Activation creates an exact derivative jump propagated along active ancestors.
            feedleft=weight[i]
            before=water_tree(parent,weight,leak,spill,caps,t-h)
            earlier=water_tree(parent,weight,leak,spill,caps,t-2*h)
            for j in range(i+1,len(parent)):
                if parent[j]==i:
                    feedleft+=(before[j]-earlier[j])/h
            expected=beta[i]*feedleft
            j=i
            while j!=0:
                j=parent[j]
                expected*=beta[j]
            assert observed==expected,(observed,expected)
    return sum(predicted_visible(parent,target,i) for i in range(len(parent)))


def run():
    checks=0
    rng=random.Random(74125)
    for n in range(2,7):
        parents=[0]+[(i-1)//2 for i in range(1,n)]
        wt=[F(i+3,i+2) for i in range(n)]
        leak=[F((i%3)+1) for i in range(n)]
        spill=[F((i%4)+2) for i in range(n)]
        for perm in permutations(range(1,n+1)):
            got=check_one(parents,wt,leak,spill,tuple(map(F,perm)))
            assert 1<=got<=n
            checks+=n
    for n in range(2,13):
        for _ in range(65):
            parents=[0]+[rng.randrange(i) for i in range(1,n)]
            wt=[F(rng.randrange(1,9),rng.randrange(1,6)) for _ in range(n)]
            leak=[F(rng.randrange(1,6)) for _ in range(n)]
            spill=[F(rng.randrange(1,6)) for _ in range(n)]
            target=list(map(F,rng.sample(range(1,4*n+2),n)))
            check_one(parents,wt,leak,spill,target)
            checks+=n
        for k in range(1,n+1):
            # Realize exactly k observable breakpoints, including the outlet's.
            parents=[0]+[(i-1)//2 for i in range(1,n)]
            selected=set(range(1,k))
            target=[F(2)]
            for i in range(1,n):
                target.append(F(3+i) if i in selected else F(i,n+1))
            # The selected indices have increasing depth-or-index, so every
            # selected ancestor activates first.
            got=check_one(parents,[F(1)]*n,[F(1)]*n,[F(1)]*n,target)
            assert got==k,(n,k,got)
            checks+=n
    # Exact two-pool continuum witness: two distinct internal capacities,
    # identical outlet functions for every nonnegative input intensity.
    parent=[0,0]
    weight=leak=spill=[F(1),F(1)]
    cases=[(F(4),F(1)),(F(7,2),F(2))]
    for intensity in [F(0),F(1,3),F(1),F(2),F(3),F(7,2),F(10)]:
        v=[]
        for rootcap,leafcap in cases:
            v.append(water_tree(parent,weight,leak,spill,[rootcap,leafcap],intensity)[0])
        assert v[0]==v[1]==F(3,4)*max(F(0),intensity-F(3))
        checks+=1
    # Higher-dimensional capacity nonidentifiability witness on 4-node tree.
    parent=[0,0,0,1]; weight=leak=spill=[F(1)]*4
    for internal in [(F(1),F(1),F(1)),(F(2),F(1),F(2)),(F(1,2),F(5,2),F(3,2))]:
        caps=[F(0)]+list(internal)
        t=F(5)
        feed=weight[0]*t+sum((water_tree(parent,weight,leak,spill,caps,t)[j] for j in range(1,4) if parent[j]==0),F(0))
        caps[0]=feed
        for intensity in [F(0),F(1),F(2),F(4),F(5),F(6),F(10)]:
            val=water_tree(parent,weight,leak,spill,caps,intensity)[0]
            # all nodes active after I=5; full-active derivative L is 9/8.
            assert val==F(9,8)*max(F(0),intensity-t),(caps,intensity,val)
            checks+=1
    print('PASS:',checks,'exact-rational local and network checks')

if __name__=='__main__':
    run()

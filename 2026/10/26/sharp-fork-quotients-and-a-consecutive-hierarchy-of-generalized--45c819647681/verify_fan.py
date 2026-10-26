#!/usr/bin/env python3
"""Finite bounded-morphism tests for punctured products of rooted fans."""
from itertools import product

def nodes(b, m):
    top = b + 1
    return [v for v in product(range(top + 1), repeat=m) if v != (top,)*m]

def leq(x, y, b):
    return all(a == 0 or a == c or c == b+1 for a, c in zip(x,y))

def maxima(b, m):
    top = b + 1
    return [tuple(a if j == i else top for j in range(m)) for i in range(m) for a in range(1,b+1)]

def p_morphism(values, xs, ys, b, k):
    if set(values) != set(range(k+1)):
        return False
    for i, x in enumerate(xs):
        for j, xx in enumerate(xs):
            if leq(x,xx,b) and not (values[i] == 0 or values[i] == values[j]):
                return False
        for target in range(k+1):
            if values[i] == 0 or values[i] == target:
                if not any(leq(x,xx,b) and values[j]==target for j,xx in enumerate(xs)):
                    return False
    return True

def color_criterion(b,m,k,root=None):
    xs=nodes(b,m)
    if root is not None:
        xs=[v for v in xs if leq(root,v,b)]
    maxs=[v for v in maxima(b,m) if v in xs]
    ups=[tuple(i for i,y in enumerate(maxs) if leq(x,y,b)) for x in xs]
    target_mask=(1<<k)-1
    count=0
    witness=None
    for colors in product(range(1,k+1),repeat=len(maxs)):
        vals=[]
        for I in ups:
            mask=0
            for i in I:
                mask |= 1<<(colors[i]-1)
            if mask==target_mask:
                vals.append(0)
            elif mask.bit_count()==1:
                vals.append(mask.bit_length())
            else:
                break
        else:
            if len(vals)==len(xs) and 0 in vals and set(vals)==set(range(k+1)):
                count+=1
                witness=vals
                # The coloring criterion must construct a genuine p-morphism.
                assert p_morphism(vals,xs,list(range(k+1)),b,k)
    return count,witness

def direct_exhaustive(b,m,k):
    xs=nodes(b,m)
    n=0
    for vals in product(range(k+1), repeat=len(xs)):
        if p_morphism(vals,xs,list(range(k+1)),b,k):
            n+=1
    return n

def main():
    cases=[(1,1,2),(1,2,2),(1,2,3),(1,3,3),
           (2,1,2),(2,1,3),(2,2,2),(2,2,3),(2,3,3),
           (3,1,3),(3,1,4),(3,2,3),(3,2,4),(3,3,4)]
    for b,m,k in cases:
        n,w=color_criterion(b,m,k)
        if (b==1 and m==2 and k==2) or (b>=2 and m==1 and k<=b):
            assert n>0,(b,m,k,n)
        if k>max(b,2):
            assert n==0,(b,m,k,n)
        if (b,m,k) in [(1,1,2),(1,2,2),(1,2,3),(2,1,2),(2,1,3)]:
            direct=direct_exhaustive(b,m,k)
            assert n==direct,(b,m,k,n,direct)
        print('case',b,m,k,'onto_p_morphisms',n)
    # All principal generated subframes: a root with one active coordinate
    # can witness the b-fork even when the whole punctured product cannot.
    for b,m in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]:
        observed=[]
        for k in range(2,max(b,2)+2):
            witness_roots=0
            for root in nodes(b,m):
                n,_=color_criterion(b,m,k,root)
                if n:
                    witness_roots+=1
            observed.append((k,witness_roots))
        capacity=max([k for k,count in observed if count] or [0])
        expected=max(b,2) if m>=2 or b>=2 else 0
        assert capacity==expected,(b,m,capacity,observed)
        print('generated',b,m,'capacity',capacity,'witnesses',observed)
    print('FAN_PRODUCT_CAPACITY_CHECK_OK')
if __name__=='__main__': main()

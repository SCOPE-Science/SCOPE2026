"""Independent finite checks of four-run string-attractor classification.

Only tests finite parameter boxes; the general result requires the paper proof.
"""
from itertools import combinations, product


def word(a,b,c,d):
    return '0'*a+'1'*b+'0'*c+'1'*d


def theoretical_pairs(a,b,c,d):
    """Return predicted pairs, zero-indexed, by boundary classification."""
    A=range(0,a); B=range(a,a+b); C=range(a+b,a+b+c); D=range(a+b+c,a+b+c+d)
    out=set()
    if a>=c and b>=d:
        for x in A:
            if b==1 or x==a-1:
                out.add((x,a+b-1))
    if c>=a and d>=b:
        for y in D:
            if c==1 or y==a+b+c:
                out.add((a+b,y))
    if c>=a and b>=d:
        for t in range(1,b+1):
            for z in range(1,c+1):
                if (t==1 or z==c) and (t==b or z==1) and t<=d+1 and z>=c-a:
                    out.add((a+t-1,a+b+z-1))
    return {tuple(sorted(p)) for p in out}


def factor_position_masks(w):
    n=len(w)
    masks={}
    for i in range(n):
        mask=0
        for j in range(i,n):
            mask |= 1<<j
            x=w[i:j+1]
            masks[x]=masks.get(x,0)|mask
    return list(masks.values())


def actual_pairs_by_masks(w):
    masks=factor_position_masks(w)
    return {p for p in combinations(range(len(w)),2)
            if all(mask & ((1<<p[0])|(1<<p[1])) for mask in masks)}


def direct_is_attractor(w,S):
    all_factors=set()
    covered=set()
    for i in range(len(w)):
        for j in range(i+1,len(w)+1):
            substring=w[i:j]
            all_factors.add(substring)
            if any(i<=p<j for p in S):
                covered.add(substring)
    return all_factors==covered


def theoretical_cardinality(a,b,c,d):
    count=0
    if a>=c and b>=d: count+=a if b==1 else 1
    if c>=a and d>=b: count+=d if c==1 else 1
    if c>=a and b>=d:
        if b==1: count+=min(c,a+1)
        elif c==1: count+=min(b,d+1)
        else: count+=int(c-a<=1)+int(b-d<=1)
    return count


def predicted_min(a,b,c,d):
    return 3 if (a>c and b<d) or (c>=a+2 and b>=d+2) else 2


def witness_three(a,b,c,d):
    if b>=d:
        return (a-1,a+b-1,a+b+c-1)
    return (a-1,a+b,a+b+c)


def main():
    trial_count=0; pairs_checked=0
    for a,b,c,d in product(range(1,7),repeat=4):
        w=word(a,b,c,d)
        calculated=actual_pairs_by_masks(w)
        expected=theoretical_pairs(a,b,c,d)
        assert calculated==expected,(a,b,c,d,'pairs',calculated^expected)
        assert len(expected)==theoretical_cardinality(a,b,c,d),(a,b,c,d,'count')
        assert predicted_min(a,b,c,d)==(2 if calculated else 3),(a,b,c,d,'phase')
        p=witness_three(a,b,c,d)
        assert all(mask & sum(1<<t for t in p) for mask in factor_position_masks(w)),(a,b,c,d,'witness')
        trial_count+=1
        pairs_checked+=len(w)*(len(w)-1)//2
        if max(a,b,c,d)<=4:
            brute={s for s in combinations(range(len(w)),2) if direct_is_attractor(w,s)}
            assert brute==calculated,(a,b,c,d,'direct')
    assert theoretical_pairs(1,1,1,1)=={(0,1),(1,2),(2,3)}
    assert predicted_min(1,3,3,1)==3
    assert predicted_min(2,1,1,2)==3
    assert predicted_min(1,2,2,1)==2
    print('ALL_FOUR_RUN_CHECKS_PASSED', 'quadruples',trial_count,
          'candidate_pairs',pairs_checked,
          'direct_quadruples',4**4)

if __name__=='__main__':
    main()

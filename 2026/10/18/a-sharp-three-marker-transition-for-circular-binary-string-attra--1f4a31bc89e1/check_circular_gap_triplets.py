"""Standalone exact checker for binary circular attractors of distinct-gap triples.

Usage: python check_circular_gap_triplets.py [MAX_GAP]
The computation enumerates all circular factors (up to full length), constructs
for each factor the exact set of positions crossed by at least one occurrence,
then tests every two-position set. No hypothesized structural constraints are
used in the census. A second direct implementation cross-checks small cases.
"""
import itertools
import sys

def word(a, b, c):
    return '0'+'1'*a+'0'+'1'*b+'0'+'1'*c

def factor_masks(w):
    n=len(w)
    doubled=w+w
    # Each factor of length <= n has n circular occurrences.
    d={}
    for length in range(1,n+1):
        base=(1<<length)-1
        for start in range(n):
            fac=doubled[start:start+length]
            mask=((base<<start)&((1<<n)-1)) | ((base<<start)>>n)
            d[fac]=d.get(fac,0)|mask
    return tuple(d.values())

def attractors_of_size_two(w):
    masks=factor_masks(w)
    n=len(w)
    return {p for p in itertools.combinations(range(n),2)
            if all(mask & ((1<<p[0]) | (1<<p[1])) for mask in masks)}

def direct_attracts(w, positions):
    n=len(w)
    factors={}
    for length in range(1,n+1):
        for start in range(n):
            fac=''.join(w[(start+t)%n] for t in range(length))
            occupied={(start+t)%n for t in range(length)}
            factors.setdefault(fac,[]).append(occupied)
    return all(any(occ.intersection(positions) for occ in copies)
               for copies in factors.values())

def expected(a,b,c):
    z=a+1
    start=a+b+3
    return {(z,start+j-1) for j in range(c-a,a+2)}

def verify(max_gap=12):
    count=0
    with_two=0
    with_three=0
    for a,b,c in itertools.combinations(range(1,max_gap+1),3):
        w=word(a,b,c)
        actual=attractors_of_size_two(w)
        want=expected(a,b,c)
        assert actual==want,(a,b,c,actual,want)
        assert len(actual)==max(0,2*a+2-c)
        assert len(actual)>0 if c<=2*a+1 else len(actual)==0
        if c>2*a+1:
            z=a+1
            first=a+b+3
            marks={z,first+a,first+c-a-1}
            assert len(marks)==3
            masks=factor_masks(w)
            smask=sum(1<<t for t in marks)
            assert all(mask&smask for mask in masks),(a,b,c,marks)
            with_three+=1
        else: with_two+=1
        if c<=7:
            assert all(direct_attracts(w,s) for s in want)
            # Complete independent brute force on all mixed-letter pairs.
            brute={(p,q) for p,q in itertools.combinations(range(len(w)),2)
                   if direct_attracts(w,{p,q})}
            assert brute==want,(a,b,c,brute,want)
        count+=1
    print('ALL_DISTINCT_GAP_CIRCULAR_ATTRACTOR_CHECKS_PASSED',
          'triples',count,'two_phase',with_two,'three_phase',with_three,
          'max_gap',max_gap)

if __name__=='__main__':
    verify(int(sys.argv[1]) if len(sys.argv)>1 else 12)

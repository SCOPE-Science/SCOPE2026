"""Standalone exact verifier for the four-run attractor theorem.
Run: python3 verify.py (standard library only).
"""
from itertools import combinations, product


def prediction(a,b,c,d):
    """All predicted two-position attractors, zero-based."""
    A = range(a)
    B = range(a,a+b)
    C = range(a+b,a+b+c)
    D = range(a+b+c,a+b+c+d)
    out = set()
    def put(x,y):out.add(tuple(sorted((x,y))))
    if a>=c and b>=d:
        for z in (A if b==1 else (a-1,)):put(z,a+b-1)
    if c>=a and b>=d:
        if b==1:
            select = C if c==a else range(a+b+c-a-1,a+b+c)
            for z in select:put(z,a+b-1)
        elif d>=b-1:put(a+b+c-1,a+b-1)
    if d>=b and c>=a:
        for v in (D if c==1 else (a+b+c,)):put(a+b,v)
    if b>=d and c>=a:
        if c==1:
            select=B if b==d else range(a,a+d+1)
            for v in select:put(a+b,v)
        elif a>=c-1:put(a+b,a)
    return out


def direct_pairs(w):
    n=len(w)
    occurrences={}
    for i in range(n):
        mask=0
        for j in range(i,n):
            mask|=1<<j
            t=w[i:j+1]
            occurrences[t]=occurrences.get(t,0)|mask
    values=tuple(occurrences.values())
    return {pair for pair in combinations(range(n),2)
            if all((1<<pair[0]|1<<pair[1]) & m for m in values)}


def literal_hit(w,pair):
    # Completely independent occurrence test with no bit masks.
    factors={w[i:j] for i in range(len(w)) for j in range(i+1,len(w)+1)}
    for t in factors:
        m=len(t)
        if not any(w[u:u+m]==t and (u<=pair[0]<u+m or u<=pair[1]<u+m)
                   for u in range(len(w)-m+1)):
            return False
    return True


def main():
    tested=0
    pair_tests=0
    literal_tests=0
    phase_three=0
    for a,b,c,d in product(range(1,7),repeat=4):
        w='0'*a+'1'*b+'0'*c+'1'*d
        expected=prediction(a,b,c,d)
        actual=direct_pairs(w)
        assert actual==expected,(a,b,c,d,actual^expected)
        phase=(a>c and d>b) or (c>=a+2 and b>=d+2)
        assert (len(expected)==0)==phase, (a,b,c,d)
        phase_three+=phase
        tested+=1
        pair_tests+=len(w)*(len(w)-1)//2
        if max(a,b,c,d)<=3:
            for pair in combinations(range(len(w)),2):
                assert literal_hit(w,pair)==(pair in actual),(a,b,c,d,pair)
                literal_tests+=1
        if not actual:
            # Verify two explicit 3-position upper-bound constructions.
            if a>=c:
                three={a-1,a+b-1,a+b+c}
            else:
                three={a,a+b,a+b+c}
            occ={}
            for i in range(len(w)):
                for j in range(i+1,len(w)+1):
                    t=w[i:j]
                    if t not in occ:occ[t]=[]
                    occ[t].append(set(range(i,j)))
            assert all(any(x & three for x in sets) for sets in occ.values()),(a,b,c,d)
    print('VERIFY_OK quadruples=%d exact_two_pair_tests=%d literal_pair_tests=%d phase_three_cases=%d three_upper_witnesses=TRUE' % (tested,pair_tests,literal_tests,phase_three))

if __name__=='__main__': main()

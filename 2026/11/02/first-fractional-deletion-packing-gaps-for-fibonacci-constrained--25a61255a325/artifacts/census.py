#!/usr/bin/env python3
"""Independent exact maximum-clique search in the complement of deletion confusability graph.
It uses no solver and no certificates.
"""
import itertools

def exact(n):
    v=[''.join(x) for x in itertools.product('01',repeat=n) if '11' not in ''.join(x)]
    s=[{w[:i]+w[i+1:] for i in range(n)} for w in v]
    k=len(v)
    comp=[sum(1<<j for j in range(k) if j!=i and not(s[i]&s[j])) for i in range(k)]
    best=0
    def visit(size,avail):
        nonlocal best
        if size+avail.bit_count()<=best:return
        if not avail:
            best=max(best,size)
            return
        while avail:
            bit=avail&-avail
            j=bit.bit_length()-1
            avail^=bit
            visit(size+1,avail&comp[j])
            if size+avail.bit_count()<=best:return
    visit(0,(1<<k)-1)
    return best
if __name__=='__main__':
    vals=[exact(n) for n in range(1,8)]
    assert vals==[1,1,2,2,3,3,5],vals
    print('CENSUS_OK', vals)

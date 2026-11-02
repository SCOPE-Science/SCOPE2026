"""Finite independent checks for a squarefree Sylow-divisor classification.
These checks do not replace the proof for unbounded primes.
"""

def primes_below(limit):
    sieve = bytearray(b'\x01') * limit
    if limit: sieve[0] = 0
    if limit > 1: sieve[1] = 0
    for p in range(2,int((limit-1)**.5)+1):
        if sieve[p]:
            for i in range(p*p,limit,p):
                sieve[i] = 0
    return [p for p in range(limit) if sieve[p]]


def meets_condition_direct(p,q,r):
    divs=(p,q,r,p*q,p*r,q*r,p*q*r)
    return all(any(d>1 and d%t==1 for d in divs) for t in (p,q,r))


def main():
    ps=primes_below(1000)
    found=[]
    tested=0
    for i,p in enumerate(ps):
        for j in range(i+1,len(ps)):
            q=ps[j]
            for r in ps[j+1:]:
                tested+=1
                if meets_condition_direct(p,q,r):
                    found.append((p,q,r))
    assert found == [(2,3,5),(3,5,7)], found
    # Independently check prime-triplet shape in a larger prime range.
    large=primes_below(100_000)
    lookup=set(large)
    shape=[p for p in large if 2*p+1<100_000 and 2*p-1 in lookup and 2*p+1 in lookup]
    assert shape==[2,3],shape
    for p,q,r in found:
        assert meets_condition_direct(p,q,r)
    print('VERIFY_OK triples_tested=%d primes_below_1000=%d survivors=%s shape_primes=%s finite_only=YES' % (tested,len(ps),found,shape))

if __name__=='__main__':main()

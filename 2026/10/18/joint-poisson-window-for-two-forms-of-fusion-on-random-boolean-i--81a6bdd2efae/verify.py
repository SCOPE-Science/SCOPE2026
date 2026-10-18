"""Independent finite checks of join-modal witness counts and exact mixed/self moments.
All symbols describe mathematical data. Run: python3 verify.py
"""
from fractions import Fraction
from math import comb


def predicted(n, p):
    a, b, c = 3**n, 5**n, 2**n
    m1 = a*p*p
    s1 = Fraction(a-1,2)*p*p
    mv = a*p*p*(1-p*p)+2*(b-a)*p**3*(1-p)
    sv = Fraction(a-1,2)*p*p*(1-p*p)+(b-a-2*c+2)*p**3*(1-p)
    cov = (b-c)*p**3*(1-p)
    return m1,s1,mv,sv,cov


def exact_enumeration(n, numerator, denominator):
    q=2**n
    bits=2*q
    full=q-1
    mixed=[(u,v) for u in range(q) for v in range(q) if (u|v)==full]
    self_edges=[(u,v) for u in range(q) for v in range(u+1,q) if (u|v)==full]
    assert len(mixed)==3**n
    assert len(self_edges)==(3**n-1)//2
    tally=[0]*5
    mass=0
    p=Fraction(numerator,denominator)
    weights=[numerator**i*(denominator-numerator)**(bits-i) for i in range(bits+1)]
    for amask in range(1<<q):
        ac=amask.bit_count()
        s=sum(bool(amask>>u&1) and bool(amask>>v&1) for u,v in self_edges)
        for bmask in range(1<<q):
            m=sum(bool(amask>>u&1) and bool(bmask>>v&1) for u,v in mixed)
            w=weights[ac+bmask.bit_count()]
            mass+=w
            for k,v in enumerate((m,s,m*m,s*s,m*s)):
                tally[k]+=w*v
    assert mass==denominator**bits
    e_m,e_s,e_m2,e_s2,e_ms=[Fraction(t,mass) for t in tally]
    got=(e_m,e_s,e_m2-e_m*e_m,e_s2-e_s*e_s,e_ms-e_m*e_s)
    expected=predicted(n,p)
    assert got==expected,(n,p,got,expected)
    # Check that the self-join is witnessed by a distinct pair OR the top-world diagonal.
    for amask in range(1<<q):
        truth=any((amask>>u&1) and (amask>>v&1) and (u|v)==full
                  for u in range(q) for v in range(q))
        alt=bool(amask>>full&1) or any((amask>>u&1) and (amask>>v&1)
                                           for u,v in self_edges)
        assert bool(truth)==bool(alt)
    return len(mixed),len(self_edges)


def dependency_count(n):
    q=2**n; full=q-1
    mix=[(('A',u),('B',v)) for u in range(q) for v in range(q) if u|v==full]
    self_edges=[(('A',u),('A',v)) for u in range(q) for v in range(u+1,q) if u|v==full]
    edges=mix+self_edges
    max_second=0
    for i,e in enumerate(edges):
        for j in range(i+1,len(edges)):
            if set(e).intersection(edges[j]):
                max_second+=1
    degrees={('A',u):0 for u in range(q)}
    degrees.update({('B',u):0 for u in range(q)})
    for e in edges:
        for v in e:degrees[v]+=1
    assert sum(d*d for d in degrees.values())<=5*5**n
    cross=0
    for e in self_edges:
        cross+=sum(bool(set(e).intersection(f)) for f in mix)
    assert cross==5**n-2**n
    return len(edges),max_second

if __name__=='__main__':
    checks=0
    for n in range(0,4):
        for p_num,p_den in ((1,2),(1,3)):
            counts=exact_enumeration(n,p_num,p_den)
            checks+=1
            print('FINITE',n,p_num,p_den,counts)
    for n in range(0,4):
        print('DEPENDENCY',n,dependency_count(n))
    print('VERIFY_OK',checks,'exact enumerations and 4 dependency-graph checks')

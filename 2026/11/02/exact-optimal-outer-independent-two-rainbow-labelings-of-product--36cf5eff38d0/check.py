"""Independent graph-level checks of optimal outer-independent 2-rainbow functions.

Run with Python 3.10+; no dependencies.
"""
from itertools import product
from collections import Counter


def graph(s,t):
    vertices = [(i,j) for i in range(s) for j in range(t)]
    return [[v for v,(k,l) in enumerate(vertices) if k!=i and l!=j]
            for i,j in vertices]


def valid(a,adj):
    zeros=[i for i,z in enumerate(a) if z==0]
    for i in zeros:
        if any(a[j]==0 for j in adj[i]):
            return False
        mask=0
        for j in adj[i]:
            mask|=a[j]
        if mask != 3:
            return False
    return True


def formula(s,t):
    if s>t:s,t=t,s
    if s==2 and t==2:return 4,36
    if s==2 and t==3:return 4,48
    z=(1 if s<t else 2)*s
    return s*t-t,z*(2**((s-1)*t)-2*(1+t*(2**(s-1)-1)))


def exhaustive(s,t):
    adj=graph(s,t)
    best=2*s*t+1
    qty=0
    for a in product(range(4), repeat=s*t):
        weight=sum(x.bit_count() for x in a)
        if weight>best:continue
        if not valid(a,adj):continue
        if weight<best:best,qty=weight,0
        qty+=1
    return best,qty


def independent_matrix_count(s,t):
    # Independent enumeration of all two-color singleton matrices outside a zero row;
    # unlike formula(), this checks the actual neighbor sets in the product graph.
    assert 2<=s<=t and (s-1)*t<=20
    neighbors=graph(s,t)
    zero=[0]*t
    tally=0
    for b in product((1,2),repeat=(s-1)*t):
        f=zero+list(b)
        if valid(f,neighbors):tally+=1
    return tally


def witness(s,t):
    assert 2<=s<=t and not(s==2 and t<=3)
    a=[0]*t
    for r in range(1,s):
        for j in range(t):
            a.append(1 if r==1 and (s>=3 or j<2) else 2)
    assert valid(a,graph(s,t))
    assert sum(x.bit_count() for x in a)==s*t-t


def main():
    all_graph=[(2,2),(2,3),(2,4),(3,3)]
    for s,t in all_graph:
        a=exhaustive(s,t)
        b=formula(s,t)
        assert a==b,(s,t,a,b)
    n_matrix=0
    for s in range(2,6):
        for t in range(max(4,s),11):
            if (s-1)*t>18:continue
            actual=independent_matrix_count(s,t)
            expected=(formula(s,t)[1]//((2 if s==t else 1)*s))
            assert actual==expected,(s,t,actual,expected)
            n_matrix+=1
    for s in range(2,9):
        for t in range(max(4,s),31):
            witness(s,t)
    print('VERIFY_OK: %d complete four-symbol enumerations; %d independent matrix enumerations; %d large-parameter witnesses' % (len(all_graph),n_matrix,sum(31-max(4,s) for s in range(2,9))))

if __name__=='__main__':main()

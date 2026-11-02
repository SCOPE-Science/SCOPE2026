"""Finite independent checks for a conditional leaf-count theorem in Cayley trees.

Reconstructs undirected trees by a heap-based Prufer decoder; also computes the
claimed conditional laws by Stirling-number occupancy counting. No external
packages are required. Exact integer arithmetic throughout.
"""
import itertools
import math
from collections import Counter
from fractions import Fraction
from heapq import heapify, heappop, heappush

checks = 0
trees = 0

def verify(condition, note):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(note)


def tree_degrees_from_prufer(word, n):
    deg = [1] * n
    for x in word:
        deg[x] += 1
    avail = [i for i in range(n) if deg[i] == 1]
    heapify(avail)
    edges=[]
    for x in word:
        y=heappop(avail)
        edges.append((x,y))
        deg[x]-=1;deg[y]-=1
        if deg[x]==1:heappush(avail,x)
    a=heappop(avail);b=heappop(avail);edges.append((a,b))
    out=[0]*n
    for x,y in edges:
        out[x]+=1;out[y]+=1
    return out


def stirling2(n,k):
    if n==k==0:return 1
    if k<1 or k>n:return 0
    row=[0]*(k+1);row[0]=1
    for i in range(1,n+1):
        nxt=[0]*(k+1)
        for j in range(1,min(i,k)+1):
            nxt[j]=j*row[j]+row[j-1]
        row=nxt
    return row[k]


def model_mass(n,d,l):
    """Numerator over all (n-1)^(n-d-1) conditional codes."""
    m=n-1;t=n-d-1;offset=int(d==1)
    e=l-offset
    occupied=m-e
    if occupied<0 or occupied>m:return 0
    return math.comb(m,occupied)*math.factorial(occupied)*stirling2(t,occupied)


def dominates(a,b):
    # unnormalized masses A and B, representing probability vectors
    da=sum(a.values());db=sum(b.values())
    return all(sum(v for z,v in a.items() if z>=j)*db>=
               sum(v for z,v in b.items() if z>=j)*da
               for j in range(min(min(a),min(b)),max(max(a),max(b))+2))

for n in range(3,9):
    observed={d:Counter() for d in range(1,n)}
    for word in itertools.product(range(n),repeat=n-2):
        degrees=tree_degrees_from_prufer(word,n)
        d=degrees[0]
        leaves=sum(x==1 for x in degrees)
        observed[d][leaves]+=1
        trees += 1
    verify(sum(sum(c.values()) for c in observed.values())==n**(n-2),('total',n))
    for d in range(1,n):
        observed_n=sum(observed[d].values())
        predicted_n=math.comb(n-2,d-1)*(n-1)**(n-d-1)
        verify(observed_n==predicted_n,('degree marginal',n,d))
        for l in range(2,n):
            left=observed[d][l]*(n-1)**(n-d-1)
            right=model_mass(n,d,l)*observed_n
            verify(left==right,('conditional law',n,d,l,left,right))
        actual_mean=Fraction(sum(l*v for l,v in observed[d].items()),observed_n)
        p=Fraction(n-2,n-1)
        expected=int(d==1)+(n-1)*p**(n-d-1)
        verify(actual_mean==expected,('mean',n,d))
    # complete order claims
    if n>=4:
        verify(dominates(observed[1],observed[2]),('one vs two',n))
        verify(not dominates(observed[2],observed[1]),('strict one vs two',n))
        for d in range(2,n-1):
            verify(dominates(observed[d+1],observed[d]),('monotone',n,d))
            verify(not dominates(observed[d],observed[d+1]),('strict',n,d))
        verify(dominates(observed[n-1],observed[1]),('star',n))
        verify(not dominates(observed[1],observed[n-1]),('strict star',n))
    if n>=5:
        for d in range(3,n-1):
            verify(not dominates(observed[1],observed[d]),('incomparability A',n,d))
            verify(not dominates(observed[d],observed[1]),('incomparability B',n,d))
    degree_total=sum(d*sum(c.values()) for d,c in observed.items())
    leaf_total=sum(l*v for c in observed.values() for l,v in c.items())
    product_total=sum(d*l*v for d,c in observed.items() for l,v in c.items())
    tot=n**(n-2)
    verify(Fraction(product_total,tot)==Fraction(degree_total,tot)*Fraction(leaf_total,tot),('zero covariance',n))
    print('n=',n,'codes=',tot,'conditional laws, FSD and covariance checked')

for n in range(4,11):
    p=Fraction(n-2,n-1)
    diff=(n-1)*p**(n-4)*(1-p*p)-1
    verify((diff>0)==(n<=8),('degree-three mean threshold',n,diff))
print('PASS',checks,'exact assertions;',trees,'independently decoded labeled trees')

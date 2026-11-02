"""Independent finite checks for binary cyclic covers avoiding 010.

Usage: python3 verify.py
Pure standard library; infinite theorem requires the accompanying proof.
"""
from itertools import product
from collections import defaultdict


def allowed(s):
    return '010' not in s


def all_words(n):
    return (''.join(x) for x in product('01', repeat=n))


def pairs(n):
    m=n-1
    required=[w for w in all_words(n) if allowed(w)]
    vset={w[:-1] for w in required} | {w[1:] for w in required}
    indeg=defaultdict(int);outdeg=defaultdict(int)
    for w in required:
        outdeg[w[:-1]] += 1
        indeg[w[1:]] += 1
    sources={v for v in vset if outdeg[v]-indeg[v]==1}
    sinks={v for v in vset if indeg[v]-outdeg[v]==1}
    assert all(abs(outdeg[v]-indeg[v])<=1 for v in vset)
    return required,sources,sinks


def match(v):
    m=len(v)
    assert allowed(v) and v.endswith('01') and not v.startswith('10')
    k=next(i for i in range(1,m) if v[i:i+2]=='10') if '10' in v[1:] else m-1
    # The last cyclic pair is 10 only for the special sink 0..01.
    if k==m-1:
        assert v=='0'*(m-1)+'1'
    return k,v[k:]+v[:k][::-1]


def tour(n):
    required,sources,sinks=pairs(n)
    assert len(sinks)==len(sources)
    graph=defaultdict(list)
    for w in required:
        graph[w[:-1]].append((w[1:],w[-1]))
    used=[]
    for v in sorted(sinks):
        k,u=match(v)
        used.append((v,k,u))
        x=v
        for b in v[:k][::-1]:
            y=x[1:]+b
            graph[x].append((y,b))
            x=y
        assert x==u
    assert {u for v,k,u in used}==sources
    count_edges=sum(map(len,graph.values()))
    start='1'*(n-1)
    node_stack=[start]
    edges=[]
    while node_stack:
        u=node_stack[-1]
        if graph[u]:
            v,bit=graph[u].pop()
            node_stack.append(v)
        else:
            edges.append(node_stack.pop())
    edges=edges[::-1]
    assert edges[0]==edges[-1] and len(edges)==count_edges+1
    binary=''.join(w[-1] for w in edges[1:])
    assert len(binary)==count_edges
    cover={''.join(binary[(i+j)%len(binary)] for j in range(n)) for i in range(len(binary))}
    assert set(required) <= cover
    return len(required),sum(k for v,k,u in used),binary


def a_values(nmax):
    arr=[1,2,4]
    for n in range(3,nmax+1):
        arr.append(2*arr[-1]-arr[-2]+arr[-3])
    return arr


def gf_series_check(max_degree=50):
    """Multiply polynomial coefficients to check the claimed generating functions."""
    A=a_values(max_degree+1)
    E=[0]*(max_degree+1)
    for n in range(3,max_degree+1):
        E[n] = 1 if n==3 else 2 if n==4 else A[n-2]+A[n-5]-(n-1)
    # identity (1-z)^2(1-2z+z²-z³) E(z) = z³(1-2z+2z²)
    from itertools import accumulate
    p=[1,-4,6,-5,3,-1] # verify by direct polynomial multiplication below
    def conv(a,b):return [sum(a[i]*b[k-i] for i in range(max(0,k-len(b)+1),min(k+1,len(a)))) for k in range(len(a)+len(b)-1)]
    p=conv([1,-2,1],[1,-2,1,-1])
    lhs=conv(E,p)[:max_degree+1]
    rhs=[0]*(max_degree+1)
    for deg,c in ((3,1),(4,-2),(5,2)): rhs[deg]=c
    assert lhs==rhs,(p,[(i,a,b) for i,(a,b) in enumerate(zip(lhs,rhs)) if a!=b][:5])


def exhaustive_small(n,optimal):
    target={x for x in all_words(n) if allowed(x)}
    for L in range(1,optimal):
        for x in all_words(L):
            hits={''.join(x[(i+j)%L] for j in range(n)) for i in range(L)}
            assert not target <= hits,(n,L,x)


def main():
    A=a_values(50)
    for n in range(3,17):
        count,extra,binary=tour(n)
        assert count==A[n]
        expected=1 if n==3 else 2 if n==4 else A[n-2]+A[n-5]-(n-1)
        assert extra==expected, (n,extra,expected)
        print('n=%d required=%d extra=%d optimal=%d witness_sha256=%s' % (
            n,count,extra,count+extra,__import__('hashlib').sha256(binary.encode()).hexdigest()[:12]))
        if n in (3,4): exhaustive_small(n,count+extra)
    gf_series_check()
    print('GF_COEFFICIENT_IDENTITY_OK')
    print('VERIFY_OK')

if __name__=='__main__': main()

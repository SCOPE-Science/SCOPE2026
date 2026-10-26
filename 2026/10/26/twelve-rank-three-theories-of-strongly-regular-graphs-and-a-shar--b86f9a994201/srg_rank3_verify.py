"""Independent finite checks for the 3-round logical profile of strongly regular graphs.
No external dependencies. All graph edges are undirected, without loops.
"""
from itertools import combinations
from functools import lru_cache


def union_cliques(t,s):
    n=t*s
    return [set(j for j in range(n) if i!=j and i//s==j//s) for i in range(n)]


def multipartite(t,s):
    n=t*s
    return [set(j for j in range(n) if i//s!=j//s) for i in range(n)]


def cycle(n):
    return [set(((i-1)%n,(i+1)%n)) for i in range(n)]


def petersen():
    V=list(combinations(range(5),2))
    return [set(j for j,y in enumerate(V) if i!=j and set(x).isdisjoint(y)) for i,x in enumerate(V)]


def complement(G):
    return [set(range(len(G)))-{i}-row for i,row in enumerate(G)]


def rook(s):
    V=[(i,j) for i in range(s) for j in range(s)]
    return [set(j for j,y in enumerate(V) if i!=j and (x[0]==y[0] or x[1]==y[1])) for i,x in enumerate(V)]


def shrikhande():
    V=[(i,j) for i in range(4) for j in range(4)]
    ix={x:i for i,x in enumerate(V)}
    dirs={(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)}
    return [set(ix[((x[0]+a)%4,(x[1]+b)%4)] for a,b in dirs) for x in V]


def parameters(G):
    n=len(G)
    assert all(i not in G[i] for i in range(n))
    assert all((j in G[i])==(i in G[j]) for i in range(n) for j in range(n))
    k=len(G[0]);assert 0<k<n-1
    assert all(len(row)==k for row in G)
    a={len(G[i]&G[j]) for i in range(n) for j in range(i+1,n) if j in G[i]}
    b={len(G[i]&G[j]) for i in range(n) for j in range(i+1,n) if j not in G[i]}
    assert len(a)==len(b)==1
    lam=a.pop();mu=b.pop()
    assert k*(k-lam-1)==(n-k-1)*mu
    return n,k,lam,mu


def parameter_bits(p):
    n,k,l,m=p
    return tuple(int(x>0) for x in (l,k-1-l,n-2*k+l,m,k-m,n-2-2*k+m))


def game_signature(G,q=3):
    """Direct type recursion, NOT using SRG parameters or classification.
    For a tuple of length j, its remaining (q-j)-rank type is the
    atomic induced type and set of one-vertex extension types.
    """
    n=len(G)
    @lru_cache(None)
    def rec(t):
        atom=(tuple(int(x==y) for x in t for y in t),
              tuple(int(y in G[x]) for x in t for y in t))
        if len(t)==q: return (atom,)
        return (atom,frozenset(rec(t+(x,)) for x in range(n)))
    return rec(())


def main():
    Gs={
        '2K2':union_cliques(2,2),'3K2':union_cliques(3,2),
        '2K3':union_cliques(2,3),'3K3':union_cliques(3,3),
        'K2,2':multipartite(2,2),'K3,3':multipartite(2,3),
        'K2,2,2':multipartite(3,2),'K3,3,3':multipartite(3,3),
        'C5':cycle(5),'Petersen':petersen(),
        'complement Petersen':complement(petersen()),'rook3':rook(3)}
    more={'4K2':union_cliques(4,2),'4K4':union_cliques(4,4),
          'K4,4':multipartite(2,4),'K4,4,4':multipartite(3,4),
          'rook4':rook(4),'Shrikhande':shrikhande()}
    pairs=[];bits={};sigs={}
    for name,G in (Gs|more).items():
        p=parameters(G);b=parameter_bits(p)
        signature=game_signature(G)
        bits[name]=b;sigs[name]=signature
        pairs.append((name,p,''.join(map(str,b))))
    assert len({bits[x] for x in Gs})==12
    assert len({sigs[x] for x in Gs})==12
    assert len({game_signature(G,q=2) for G in Gs.values()})==1
    for name,G in (Gs|more).items():
        for name2,H in (Gs|more).items():
            assert (sigs[name]==sigs[name2])==(bits[name]==bits[name2])
    print('Twelve representative profiles, with independent rank-three game signatures:')
    for name,p,b in pairs: print(f'{name}: {p}; six flags={b}')
    print('PASS: all twelve graph representatives share one rank-two theory.')
    print('PASS: 12 distinct rank-three types among 12 representatives.')
    print('PASS: all 18 tested graphs satisfy signature equivalence iff six positive-extension flags agree.')
    print('PASS: in particular rook3, rook4 and Shrikhande have the same rank-three theory.')

if __name__=='__main__':main()

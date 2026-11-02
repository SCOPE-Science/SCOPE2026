"""Finite independent path-routing checks for complete bipartite graphs.

Scientific tests use finite enumeration only; the asymptotic statements use proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb


def formula(N, a, b):
    def q(targets, trials):
        return sum(((-1)**j)*comb(targets,j)*Fraction((N-j)**trials,N**trials) for j in range(targets+1))
    return q(N-b,comb(a,2))*q(N-a,comb(b,2))


def independent_paths(N,a,b):
    # Fixed selected sets 0..a-1 in the left part and 0..b-1 in the right.
    # A-side pairs choose a right-side midpoint; B-side pairs choose a left-side midpoint.
    aa=list(combinations(range(a),2)); bb=list(combinations(range(b),2))
    good=0; total=0
    for paths_a in product(range(N),repeat=len(aa)):
        for paths_b in product(range(N),repeat=len(bb)):
            total+=1
            covered_left=set(range(a))|set(paths_b)
            covered_right=set(range(b))|set(paths_a)
            if len(covered_left)==N and len(covered_right)==N:
                good+=1
    return Fraction(good,total)


def graph_routes(N,a,b):
    # Original graph metric verifies that the midpoint list enumerates ALL geodesics.
    vertices=[(side,i) for side in (0,1) for i in range(N)]
    adj={v:{w for w in vertices if v[0]!=w[0]} for v in vertices}
    selected=[(0,i) for i in range(a)]+[(1,j) for j in range(b)]
    for u,v in combinations(selected,2):
        if u[0]==v[0]:
            middles={w for w in vertices if w in adj[u] and v in adj[w]}
            assert middles=={(1-u[0],j) for j in range(N)}
        else:
            assert v in adj[u] # exactly the length-one path
    return True


def main():
    tested=0
    for N in range(2,5):
        for a in range(N+1):
            for b in range(N+1):
                if comb(a,2)+comb(b,2)>7: # bound finite enumeration
                    continue
                graph_routes(N,a,b)
                exact=independent_paths(N,a,b)
                theo=formula(N,a,b)
                assert exact==theo,(N,a,b,exact,theo)
                tested+=1
    assert formula(3,2,2)==Fraction(1,9)
    assert formula(4,3,3)==Fraction(37**2,64**2)
    print('VERIFY_OK instances=',tested,'including asymmetric source counts and original geodesic choices')
    print('N=3,a=b=2: ',formula(3,2,2))
    print('N=4,a=b=3: ',formula(4,3,3))

if __name__=='__main__':main()

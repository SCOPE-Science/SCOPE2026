#!/usr/bin/env python3
"""Separate symbolic census of extension-profile multiplicities from Moore axioms."""

def profiles(d):
    assert d>=3
    # Multiplicities for distinct 4th-vertex extension profiles, by triple type.
    # independent nonstar: three opposite-center vertices, three opposite-pair
    # witnesses, six sets of extra neighbors, and the untouched remainder.
    nonstar = [1]*3 + [1]*3 + [d-3]*6 + [(d-3)**2+1]
    # independent star: central point, other central neighbors, neighbors of
    # each leaf outside center, and vertices touching none of the four.
    star = [1,d-3]+[d-1]*3+[(d-1)*(d-3)]
    # one edge + isolated vertex: completing the forced 5-cycle, neighbors
    # of its five vertices outside cycle, vertices touching none.
    oneedge = [1]*2+[d-2]*5+[(d-2)*(d-3)]
    # two-edge path: neighbors of central vertex other than endpoints,
    # endpoint-only neighbors, and vertices outside their neighborhoods.
    path = [d-2,d-1,d-1,(d-1)*(d-2)]
    return {'independent_nonstar':nonstar,'independent_star':star,
            'single_edge':oneedge,'two_edge_path':path}

def main():
    for d in [3,4,5,7,57,127]:
        ps=profiles(d)
        target=d*d-2
        assert all(sum(xs)==target for xs in ps.values()),(d,ps,target)
        assert all(min(xs)>=0 for xs in ps.values())
        supports={name:sum(v>0 for v in xs) for name,xs in ps.items()}
        expected={'independent_nonstar':(7 if d==3 else 13),
                  'independent_star':(4 if d==3 else 6),
                  'single_edge':(7 if d==3 else 8),
                  'two_edge_path':4}
        assert supports==expected,(d,supports)
        print('d=',d,'n=',d*d+1,'support_sizes=',supports,'SUMS_AND_POSITIVITY_PASS')
    print('Symbolic Moore-tree profile verification: PASS')
if __name__=='__main__':main()

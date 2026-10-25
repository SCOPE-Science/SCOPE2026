# Independent mathematical audit

## correctness

PASS

PASS. For every n>=4, wheel K1∨C_n has KLX=DTC=ceil(n/2)+1, classical stc=3 and tw=3. In any ordered DFS tree with hub root or leaf the hub cut gives n-1 crossing non-tree edges. Otherwise pre-hub ancestors form one nonempty contiguous rim path length a, and all remaining rim vertices belong to hub's unique DFS-child subtree. Its entering and departing tree-edge cuts each cross two rim edges and respectively a or n-a hub spokes, hence backedge crossing-only congestion at least max(a+1,n-a+1). An explicit Hamiltonian DFS path with a=floor(n/2) rim vertices before hub makes all non-tree edges crossing and yields equality; hub star shows stc=3 and width-3 bags with a K4 minor prove tw=3. Boundary n=4 and excluded n=3 noted. Inspected source full traversal/arc verifier; its enumeration of n<=9 and explicit paths to n<=500 are support only, not proof of arbitrary n.

## originality

PASS

Best-of-knowledge PASS based on reading actual full source claims and comparing implications to materially inspected primary literature and published Resultary records. No identified stronger theorem implies the exact present final claim; named overlaps are credited, not asserted absent merely from search results. Residual risks of unindexed or incompletely inspected sources explicitly remain.

## value

PASS

PASS. DFS-restricted congestion versus conventional spanning-tree congestion is a natural comparison in the new KLX parameter. This theorem gives an exact unbounded additive and multiplicative penalty within planar three-connected fixed-treewidth wheel graphs, a structural separation not implied by a general maximum-degree lower bound. The two hub-adjacent cut argument is portable to other apex DFS problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.

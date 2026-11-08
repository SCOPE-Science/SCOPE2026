# Independent mathematical audit

## correctness

PASS

Odd Kneser graph KG(2k+1,k) has no 4-cycle: two different k-subsets share at most one disjoint k-neighbor. Every Hom cell has a singleton coordinate; contractible star-cover simplices intersect only in points corresponding to ordered disjoint pairs. Equivariant nerve is connected bipartite D_k with 2*C(2k+1,k) vertices and (k+1)*C(2k+1,k) edges, so H1 is its integral oriented cycle kernel of rank (k-1)*C(2k+1,k)+1, with swap reversing edge orientation. Decomposing ordered edges as Ind_{S_2k}^{S_(2k+1)} M^(k,k), complement sends two-row Specht S^(2k-j,j) to (-1)^j; the Pieri rule adds one box, all two-row terms cancel against H0 and the vertex representation, leaving exactly three-row S^(2k-j,j,1) with swap sign (-1)^(j+1). Fixed-chain trace yields 1-2^r precisely for one fixed point and all other cycles even, otherwise 1. Inspected program independently computes Frobenius-alternant characters of all cycle types k=2..5; did not interpret these finite tests as the unrestricted proof.

## originality

PASS

Earlier square-free graph Hom results provide ordinary homotopy/nerve reductions, but not the complete rational S_(2k+1) x C2 Specht decomposition and mixed-character dichotomy for every k>=3; the k=2 Petersen special case is excluded.

## value

PASS

The full multiplicity-free Specht spectrum and color-swap parity across an infinite canonical symmetric graph family are meaningful equivariant invariants not mechanically given by the known nonequivariant H1 rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.

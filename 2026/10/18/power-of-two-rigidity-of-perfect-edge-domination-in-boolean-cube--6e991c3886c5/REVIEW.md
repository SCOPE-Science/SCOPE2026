# Independent mathematical audit

## correctness

PASS

For an unchosen edge the two selected endpoint degrees sum to one. Thus any vertex with selected degree at least two has degree d in F. If a chosen edge joins two degree-one vertices, close it and another incident edge into a coordinate square; the two nonendpoints must have selected degree zero, yet their connecting edge would then be undominated. If two degree-d vertices are adjacent, a degree-one neighbor of either one gives a square whose fourth vertex would simultaneously have selected degree zero and be adjacent to a degree-d vertex. Hence the degree-d adjacency forces all neighbors to have degree d, and this propagates by connectivity to the full edge set. Otherwise there is a degree-d vertex (the empty set cannot dominate and degree-one pairs cannot form chosen edges). The degree-one vertices are independent, and the vertices of degrees zero and d together are independent. Connectivity identifies the two classes with the two parities. Each vertex in the degree-one class has exactly one selected neighbor of degree d, giving d|B|=2^(d−1) and |F|=2^(d−1). Thus d is a power of two. Conversely a single-parity center set with exact opposite cover gives precisely one selected incident edge at the opposite endpoint of each unchosen edge and none at its same-parity endpoint. The center set is recoverable as the degree-d vertices, because d≥2, and it is nonempty, so the parity choice is recoverable too. Existence follows by labeling coordinates with the elements of F₂^r: for every odd vertex its syndrome specifies exactly one bit flip to the even zero-syndrome code. This construction is nontrivial since |F| is strictly below the full-edge cardinality. In d=2 these are the four two-edge stars; d=1 is excluded. The supplied check was inspected, not executed; its Q4 loop tests parity-center candidates, not all edge sets.

## originality

PASS

The supported distinct claim is the square-forced classification of every non-full PEDS of the Boolean cube, yielding the exact power-of-two obstruction and minimum. It is not the general selected-degree coloring, the construction of Hamming codes, or the use of same-parity induced stars. Closest indexed PEDS results concern other graph families; the same-day Hamming-star lower bound concerns weaker open packing, not a rigidity/converse theorem for all cube PEDSs. Bounded comparison supports this distinction, not absolute priority.

## value

PASS

Perfect edge domination is a natural graph invariant distinct from perfect vertex coding or efficient edge domination. The rigidity unifies its existence, exact minimum, and all non-full configurations for an infinite graph family, and reduces any remaining configuration or enumeration problem to a familiar class of perfect codes. The parity rigidity and the uniqueness of the full set in every inadmissible dimension are useful even though the existence construction is classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.

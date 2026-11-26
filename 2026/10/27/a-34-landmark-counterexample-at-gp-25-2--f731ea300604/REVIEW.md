# Independent mathematical audit

## correctness

PASS

Independent distance-layer construction on the stated 50-vertex graph and testing endpoint neighborhoods gives 175 mutually maximally distant pairs, with outer offsets {5,7,9,11,12}, inner offsets {9,11}, and no mixed pairs. An MMD pair can only be strongly resolved by one of its endpoints: otherwise a geodesic through that endpoint continues to a neighbor farther from the other endpoint. Thus any omission set is independent in the MMD graph. Translating an outer omitted vertex to 0 leaves five cliques partitioning its permissible companions, so at most six outer omissions are possible. Five disjoint pentagons give at most ten inner omissions. I independently computed both maxima by maximum-clique search in the component complements; they are six and ten. I also checked the proposed complement of the 16 omissions directly against all 1225 shortest-path betweenness tests, so the upper bound does not rely on the converse MMD theorem. At k=6 the proposed equality predicts 35, so exactly 34 is a counterexample without contradicting the proved upper bound.

## originality

PASS

The defining source gives the upper bound 35 at this order and explicitly conjectures equality, not 34. Its exact computations do not reach this order. A distinct later-dated Resultary record substantially overlaps and extends the result, but does not establish earlier coverage of this frozen finding.

## value

PASS

The graph order and invariant are motivated by an explicit published family conjecture. An exact counterexample outside the published computational range determines that the conjecture is false, with a structural optimality certificate and a reproducible witness. The claim does not need a corrected family formula to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.

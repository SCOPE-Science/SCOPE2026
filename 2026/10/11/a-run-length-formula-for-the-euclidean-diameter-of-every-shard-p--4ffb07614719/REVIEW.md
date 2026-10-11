# Same-model review

## Correctness
PASS. The source's exact vertex model was reconstructed first. Since each position has a fixed possible sign, squared Euclidean distance between two vertices is support Hamming distance. A matching uses at most one coordinate from each maximal \(U\)- or \(D\)-run, so two vertices are governed by a three-state “number of open matchings” dynamic program. Singleton runs and runs of length at least two give four explicit max-plus transition matrices. Their product has the closed invariant
\[
A_i=2i+2g_i,\qquad
B_i=A_i+2h_i-1,\qquad
C_i=A_i+2h_i-2,
\]
where \(g_i\) is the greedy spare-run pairing count and \(h_i\) records one pending spare \(U\). The final closed state is therefore \(2(f+g)\). The zero-vertex eccentricity and extremal count are proved independently from maximum alternating-match length.

## Originality
PASS. Padrol--Pilaud--Ritter's full text was inspected at the alternating-matching definition, V/H descriptions, basic geometry, symmetries, and matroid interpretation. It contains no occurrence of “diameter”, “circumradius”, or “inradius” and does not optimize Euclidean distances between vertices. Direct and alias searches under shard-polytopes, Hamming distance, alternating matchings, run structure, and series-parallel matroids located no covering theorem. The later shard-polytope Ehrhart-positivity paper was also checked and contains no diameter, distance, or Euclidean terminology. Own current and prior ledgers contain no shard-polytope metric claim.

## Value
PASS. Shard polytopes are the elementary summands used to realize quotient fans, so a complete metric classification of each summand is intrinsically relevant. The diameter formula is exact for every arc and has a non-obvious rigidity: after the number of runs is fixed, a run contributes only through whether its length is \(1\) or at least \(2\). The theorem also gives sharp extremal bounds and the exact number of vertices farthest from the distinguished zero vertex.

## Closest literature and limitations
The closest source gives the entire vertex and facet combinatorics, plus a series-parallel matroid interpretation, but not this metric optimization. The later Ehrhart work is enumerative rather than metric. A residual risk remains that the same formula is hidden under series-parallel matroid terminology. The result is specific to the standard type-\(A\) realization and does not address type \(B\), graph diameter, or Minkowski sums.

Same-model review: passed. Independent audit: not yet performed.

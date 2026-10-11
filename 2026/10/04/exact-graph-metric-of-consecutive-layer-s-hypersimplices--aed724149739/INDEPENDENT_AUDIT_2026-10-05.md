# Independent mathematical audit

## correctness

PASS

Specializing the published edge criterion to consecutive layers gives exactly add/delete edges between adjacent weights and same-layer swaps only at weights \(a\) and \(b\). The submitted proof constructs paths of the three stated lengths \(H,L,U\). For the reverse inequality, \(D_B=\min(H,L,U)\) is one-Lipschitz on every edge: all candidates change by at most one on add/delete edges; on the lower boundary \(H-L=a-r\ge0\), and on the upper boundary \(H-U=q-r\ge0\), leaving the minimum of the two boundary candidates, each changing by at most one under a swap. Hence \(D_B\) is a valid lower-bound potential. Complement symmetry and explicit endpoint pairs then give diameter \(\min(b,d-a)\). Independent finite replay through small dimensions agrees with the closed formula and is corroborative only.

## originality

PASS

The primary S-hypersimplex paper supplies the local edge criterion but does not determine global all-pairs shortest paths or the diameter. Searches under S-hypersimplex, cardinality-homogeneous, cardinality-constrained, cube-slab and exact-diameter terminology did not uncover a theorem implying the three-route metric. The new one-Lipschitz potential is the substantive step converting the local edge description into a global metric theorem.

## value

PASS

The one-skeleton metric is a basic invariant of this natural polytope family. The theorem gives every pairwise distance, identifies the two precise boundary shortcuts to Hamming motion, and yields the sharp diameter in all dimensions; this is a structural result rather than a small-case computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

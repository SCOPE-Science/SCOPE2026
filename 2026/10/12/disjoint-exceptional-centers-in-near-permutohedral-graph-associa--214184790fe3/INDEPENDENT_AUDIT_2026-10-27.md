# Independent mathematical audit

## correctness

PASS

For n>=3, a connected simple graph G has graph nested-fan rays precisely for connected proper nonempty induced sets, while the braid fan Y_n has rays for all such sets. Exceptional prime divisors are exactly the missing (disconnected induced) rays. Two distinct braid invariant divisors meet iff their indices are nested in the braid chain fan, so they are disjoint precisely when disconnected proper induced subsets form an antichain. If the complement is a matching, the only disconnected proper subsets are the missing two-vertex pairs; all >=3-vertex induced subgraphs are connected because each vertex has at most one missing neighbor. Conversely, adjacent missing edges ab,ac force disconnected {a,b} strictly included in disconnected {a,b,c}; G connected makes n>=4 and the triple proper, so the corresponding prime divisors meet. For missing pair {a,b} in the matching case, adding this one connected tube is the smooth star subdivision of cone(u_a,u_b) with inserted ray u_{ab}=u_a+u_b, giving an ordinary codimension-2 toric blowup. Distinct missing pairs have incompatible cross-singleton tubes, hence disjoint centers. Compatible proper tubes at cone(u_a,u_b) are exactly {a,b}∪U with nonempty proper U in R=[n]\{a,b}; their chains give the braid fan on R in N/(u_a,u_b)≈Z^R/Z(1,...,1). Thus each center is Y_{n-2} (including Y_1 a point at n=3). Standard integral codimension-2 blowup decomposition A_n(t)=P_X(t)+r t A_{n-2}(t) gives torsion-free even Betti groups, odd vanishing, Euler characteristic n!-r(n-2)! and Picard rank 2^n-n-1-r. I checked the entire source RESULT.md and actual 7-file source tree, and independently verified the disconnected-antichain equivalence for all 770 connected labelled simple graphs on 3..5 vertices and the h-vectors/center star sizes using an independently coded maximal-clique tubing method in all 16 cases n=3..7, 0<=r<=floor(n/2); these finite checks corroborate, do not substitute for, the all-n proof.

## originality

PASS

Best-of-knowledge original geometric classification, not a claim of new nested-fan, stellar subdivision, Eulerian-polynomial or codimension-two blowup machinery. The closest inspected primary sources supply general graphical nested fans and h-vector formulas, a projective-space blowup/Hassett description, and Fano criteria. They do not state a complete iff classification of disjoint exceptional prime divisors for the canonical permutohedral-to-graph-associahedral contraction with all exceptional centers identified as Y_(n-2). The required graph antichain characterization and quotient star-fan computation are genuine additional steps, and the integral cohomology formula is a downstream consequence. Another published finding on identical graph family computes acyclic-orientation parity signatures, which does not imply toric exceptional centers or complex Betti groups. General machinery may implicitly provide a concise derivation; this residual priority risk is retained rather than equating unsuccessful searches with proof of novelty.

## value

PASS

The canonical toric birational contraction from the permutohedral to any graphical nested-fan variety is a natural, independently motivated family. Classifying exactly when its exceptional prime divisors are pairwise disjoint identifies an intrinsic birational-geometric boundary among ALL connected graphs, not an arbitrary graph slice. The uniform isomorphism of every exceptional codimension-two center with Y_(n-2) strengthens that geometric classification and yields exact integral even Betti groups and Euler characteristic for an infinite, parameterized family. These are concrete reusable structural data in graph-associahedral toric blowups, not merely a known-table recomputation, a trivial renaming, or a numerically tiny gain. The group-level cohomology decomposition is not a canonical cohomology-ring isomorphism; nothing is asserted for nonmatching complements beyond the iff divisor-intersection criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Review: Sharp nonrigidity rate of finite even hypergraph extensions

## Correctness (PASS)

PASS. The root assignment freely parametrizes every even A-valued (k+1)-hypergraph by binomial(n-1,k) independent coordinates. A fixed-root transposition moves exactly 2*binomial(n-3,\(k-1\)) coordinates in pairs and thus has codimension a=binomial(n-3,\(k-1\)). For all other fixed-root permutations, support-t orbit deficiencies and the fixed-subset bound yield at least \(3a/2\) for small t=3,4, linear-in-t times a for \(5\le t\le\varepsilon n\), and Omega(\(n^k\)) for large support. For derangements, the equivariant simplicial coboundary map bounds fixed-code dimension by k-subset orbit count, so codimension Omega(\(n^k\)). Distinct-transposition intersections impose two independent constraints for every disjoint fixed (\(k-1\))-set, giving lower-order total by Bonferroni. Burnside gives the stated second-order unlabeled correction. Finite independent \(\mathbf F_2\) row reduction checked all permutations for \(k\in\{2,3\}\) and \(n\le7\), with fixed-root orbit ranks, all transposition defects, conjugacy consistency and exact Burnside integrality; all checks passed. Boundary: n sufficiently large, k and s fixed, named \((\mathbf F_2)^s\) colors, no assertion for growing parameters.

The exact finite counts for the ordinary two-graph case agree with Mallows and Sloane's existing table, providing an independent normalization check. Finite tests alone do not establish the asymptotic; the proof supplies quantitative support-wise estimates and a Bonferroni overlap bound.

## Originality (PASS within inspected evidence)

PASS with recorded priority risk. Estrada 2026 constructs the parity-extension age and proves the transitive-extension criterion, not a finite asymmetry probability or second-order labelled-to-unlabelled correction. Mallows–Sloane 1975 already counts ordinary two-graphs exactly, so the \(k=2,q=2\) special enumerative case is treated as established background, not a separate novel enumeration. Cameron–Spiga 2015 concerns primitive switching-class automorphism groups and existence of a trivial-automorphism graph in a switching class, not the random probability that the class has nontrivial automorphisms. Published-record searches using finite even hypergraphs, parity cocycles, automorphisms, transpositions and sharp correction returned nearest studies of ordinary homogeneous hypergraphs' tuple orbits and switching reducts, which do not imply this code-fixed-subspace probability law. Chung–Graham's cohomological hypergraph work is a related source of general higher-dimensional parity techniques; the full proof was not inspected and equivalence under another formulation remains possible. No definitive independent priority certification is asserted.

The closest literature is Estrada (2026, arXiv:2604.12146), Mallows–Sloane (1975, DOI 10.1137/0128070), Cameron–Spiga (2015, arXiv:1407.5288), and Chung–Graham (1992, DOI 10.2307/2153987). The latter was not inspected in full; it remains a historical-priority risk. Previously established exact two-graph counts are acknowledged, not claimed anew.

## Value (PASS)

PASS. The finite age of the generic even higher-hypergraph extensions constructed by Estrada has a natural rigidity question. The theorem identifies the unique asymptotically dominant symmetry mechanism, supplies the exact sharp exponent and leading binomial coefficient for every fixed arity and color rank, and translates this into a second-order isomorphism-class census. This sharp correction is stronger than the qualitative assertion that almost all finite age members are asymmetric or the leading labelled-count estimate; it is useful in quantitative Fraisse-age enumeration and symmetry-sensitive finite model counting. The contribution is the all-arity parity-constrained fixed-subspace analysis, not a table recomputation or the previously known two-graph specialization.

## Limitations

Fixed arity \(k\ge2\) and fixed \(q=2^s\) with \(s\ge1\), with labelled colors forming the elementary abelian 2-group. Counts are for automorphisms preserving the named colors; no uniform estimate for growing k or q. The \(q=2,k=2\) unlabeled two-graph enumeration is classical and is credited. A related older cohomological-hypergraph paper was not available in full; priority remains provisional. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.

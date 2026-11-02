# Independent mathematical audit

## correctness

PASS

The complete finite domain was reconstructed independently from all 272 perfect matchings of Q4: enumerate disjoint unordered 4-factorizations by complement, then every two-factor alternating component, and perform every valid flip. The independent Python implementation obtains exactly 1840 states, 8808 undirected edges, one size-1712 and eight size-16 components. All-state breadth-first distances in the large component independently give eccentricity counts 133 at 6, 1342 at 7, 237 at 8. Small components independently match GP(8,3), and the product-of-matching-permutation-signs is preserved by alternating-cycle swaps. The supplied eight 16-element isomorphism maps and verify.py were inspected. Exhaustive finite enumeration is proof for precisely Q4, not for higher-dimensional cubes. The saved generator and BFS routines were checked for exhaustive branching rather than trusting a log.

## originality

PASS

The exact minimum-palette Kempe connectivity and geometry of Q4 are not implied by 2010/2014 results requiring extra colours, by 1993 rainbow-existence constructions, or by Behague’s hypercube factorization sign and square-switch invariance. The Behague sign is prior and agrees with the matching-product sign in dimension four; no novelty is claimed for the sign itself. The eight GP(8,3) exchange graphs, giant-component distances and full 1840-state decomposition are separate finite claims, checked against published-claim searches. Literature and databases cannot rule out unindexed preexisting computations.

## value

PASS

Q4 is the canonical first four-regular hypercube, exactly at the minimum-palette boundary not settled by the five-colour connectivity theorems. Complete reconfiguration classes, their unexpectedly nontrivial 16-vertex geometry, symmetry orbit, and exact connected-component metrics provide a motivated finite obstruction and reproducible structural benchmark, not an arbitrary small example or assertion of higher-dimensional novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

For the 18-vertex, 27-edge LCF Pappus graph, the fully reduced Świątkowski weight-three chain model has C3 rank 6528 and C2 rank 16524, with local two half-edge differences at each cubic vertex. The inspected code constructs the signed d3 using the graded Leibniz rule and graph edge variables; an independent sparse modular elimination rebuilt all 6528 columns and gives rank 6521 over F101 (nullity 7). The pinned verifier constructs seven explicitly checkable integral cycles with identity coefficients on seven free coordinates and verifies zero integral boundaries; these imply rational rank ≤6521, hence exactly 6521 and, because any integral kernel vector has integer values on the seven free coordinates, the seven cycles form an integral H3 basis. Direct independent graph automorphism backtracking gives exactly 216 adjacency-preserving permutations. The inspected chain-action algorithm transforms each local half-edge difference with Koszul signs and tests integral chain equality on the seven cycles for all 216 maps, recovering the class traces, order-three kernel, and central-sum eigenspaces 1,2,4. Its character squared norm is 3 (648/216), and distinct central eigenvalues split three absolutely irreducible rational constituents. Mean character zero gives invariant H3=0 and therefore only H3 of the quotient vanishes. This uses the published reduced-chain comparison theorem, not just a finite-field experiment.

## originality

PASS

Compared final theorem and implications with full material from the most relevant accessible papers, published mathematical results and indexed semantic searches; the new precise statement is not implied by the checked prior work. This is best-of-knowledge originality with the stated residual risks, not a proof of historical priority.

## value

PASS

The Pappus graph is a natural symmetric cubic graph whose three-particle top homology rank seven was already known but whose exact integral symmetry module was unspecified. Determining the faithful quotient, complete class traces and integral seven-dimensional action is a nontrivial refinement that matters for equivariant configuration topology; the known rank alone is insufficient to recover it.

The dated certificate retains the supplied scientific assessment, sources and limitations.

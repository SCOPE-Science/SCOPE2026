# Scientific review: sharp cyclic-jump bandwidth under classical \(123\)-avoidance

## Correctness

PASS. The theorem quantifies over every \(n\ge3\) and \(m\ge2\), while separately excluding \(m=1\). The first entry in a classically \(123\)-avoiding bounded-jump permutation must be at least \(n-m\); reverse-complementation yields a last entry at most \(m+1\). Bounding their closing edge gives \(n\le3m+1\). A completely explicit permutation attains this bound at every admissible pair, with jumps of sizes at most \(m\) and no increasing triple. Equality of the three inequalities pins two endpoint values, while uniqueness of the first exceedance pins their immediate neighbours. The standalone checker independently confirms exhaustive finite instances. Finite enumeration is not used to infer the infinite assertion.

## Originality

PASS under accessible-source comparison, with residual historical-priority risk. Nadler's 2026 reverse-diagonal localization already implies the *necessary* bound, and this is explicitly acknowledged. Nadler addresses linearly adjacent Hamiltonian paths, not closing edges, the exact least cyclic bottleneck for all orders, or boundary rigidity. Vella and Domagalski et al. use rotation-invariant cyclic pattern avoidance; Ehrenborg and OEIS A232864 concern cyclically **consecutive** avoidance. Neither implication nor equivalence establishes the new sufficiency and four-position rigidity. Searches for alternate formulations, including path powers, cyclic jump bandwidth, and bounded-gap classical avoidance, located no covering statement. Older or differently indexed literature may still contain an equivalent result.

## Mathematical value

PASS. The recently studied linearly constrained \(123\)-avoiding Hamiltonian paths exist for arbitrarily large orders at fixed jump bound, whereas requiring a return edge makes the feasible order finite. The exact, attained cutoff \(3m+1\), the equivalent optimum \(\max\{2,\lceil(n-1)/3\rceil\}\), and the four forced labels on extremal tours resolve this natural sharp bottleneck question for all parameters. The significance lies in the complete feasibility threshold and closing-edge rigidity, not in re-proving the prior localization inequality or presenting a small computed census.

## Closest literature and limits

Closest paper: Nadler, *123-Avoiding Permutations with an Adjacency Constraint* (arXiv:2610.02526, 2026), especially Theorem 1 and the Hamiltonian-path interpretation. Distinct notions occur in Vella (2003), Domagalski et al. (2021), and Ehrenborg (2013/2016). The proof does not enumerate all tours or treat rotation-invariant classical avoidance, consecutive pattern avoidance, or other forbidden patterns. Complete historical priority and independent audit remain open.

Self-review: passed. Independent audit: not yet performed.

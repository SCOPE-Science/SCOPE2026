# Self-review: finite graphical Lie-algebra abelian-subalgebra counts

## Correctness

**PASS.** For each ordered commuting frame, the independent central edge brackets force all \(2\times2\) minors of every graph-edge pair of vertex columns to vanish. Partitioning by the nonzero-column support and its induced connected components proves the commuting-frame polynomial exactly. Möbius inversion on the finite-field subspace lattice counts full-rank commuting frames, and division by \(|\operatorname{GL}_k(q)|\) counts commuting row spaces. Any abelian Lie subalgebra is uniquely specified by its commuting image, its intersection with the central edge subspace, and a linear lift. These steps prove all displayed formulas, including characteristic two, isolated vertices and both zero and top dimensions. Independent finite-field RREF enumeration passed 158 quotient-space graph-field cases and 44 full-Lie-algebra cases; the proof, not these tests, handles arbitrary finite graphs and prime powers.

## Originality

**PASS relative to inspected literature and available prior claims.** The closest predecessor is Aldi et al. (arXiv:2504.19836, Proposition 24), which controls the dimension of abelian subalgebras via independence numbers. The maximum dimension is therefore not claimed to be new. Lee (arXiv:2010.02268) provides a general finite-field subalgebra zeta-function computation framework but no inspected all-graph abelian formula. Barrionuevo–Tirao (arXiv:2206.10572) study graph Lie-algebra rigidity; Godoy Molina–Lagos (arXiv:2308.00272) study subgraph-defined subalgebras and ideals; Rossmann (doi:10.1112/blms.12665) enumerates graphical-group conjugacy classes. None of their inspected statements implies the exact all-rank abelian-subalgebra numbers, which is the assessed contribution.

The edge constraints are closely related to binomial edge ideals. A stronger unpublished or differently named rational-point formula for those varieties could cover some or all of this work; further comparison is a residual originality risk. Literature search provides best-knowledge comparison, not proof of global uniqueness.

## Value

**PASS.** The complete abelian-subalgebra enumerator is a natural invariant in finite Lie theory, with a uniform explicit graph-theoretic formula for an infinite family and all prime powers. It also distinguishes counts of maximal subalgebras from the known maximum dimension: even for the four-vertex path, the top multiplicity is \(2q+1\), rather than simply the number of maximum independent sets. The all-rank formula permits precise subalgebra zeta polynomials and comparison of graph Lie algebras that have the same independence number.

## Limitations and status

The result is a finite sum, not a claim of efficient computation for every input graph. It does not enumerate nonabelian subalgebras or automorphism orbits, and only the standard simple-graph Lie bracket is covered. Finite exhaustive tests cannot replace the general proof. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.

# Scientific review: flag-marked subspace-lattice orbit recovery

## Correctness — PASS

The quantifiers range over every prime-power field order \(q\), every positive ambient dimension, and every nested flag. The proof directly establishes that first-round counting identifies subspace dimension and which flag members contain each atom. Second-round predecessor counts therefore recover the number \((q^{e}-1)/(q-1)\) of one-dimensional subspaces in each flag intersection, which uniquely determines \(e\). An adapted-basis construction proves that equal intersection profiles are precisely orbits of the flag-preserving general linear group. Since colour refinement is automorphism invariant, those orbits are exactly the final classes. A graph-of-linear-map count proves the Gaussian class-size formula. The explicit \(\mathbb F_2^4\) example supplies a valid strict depth-two witness.

The included programs use different subspace representations: row-echelon enumeration, and spanning-set closure with explicit \(\mathrm{GL}_n(\mathbb F_2)\) action. They test colours, orbit classes, class sizes, and the round-one collision. Their finite scope is stated: the all-dimensions conclusion relies on the algebraic proof.

## Originality — PASS, with priority uncertainty

The closest mathematical framework is the correspondence between \(C^2\) and colour refinement for relational structures, together with finite-field Schubert-cell geometry. The 2011 Berget–Huang paper gives flag-geometric and Gaussian enumeration machinery, not the two-round refinement statement; its combinatorial geometry is credited as prior. The 2015 Kiefer–Schweitzer–Selman and Arvind–Köbler–Rattan–Verbitsky papers give general logical and refinability theory, but the inspected material does not cover the flagged full-subspace-lattice construction or its two-round sharpness. Searches for the direct statement, equivalent rank/intersection signatures, and broader coverage did not reveal a stronger theorem that implies it. Published mathematical research records with related subspace themes concern other invariants (subspace-intersection graph domination, Grassmannian harmonic restriction, and group-theoretic subspace lattices), not this strict-containment refinement claim.

No finite collection of searches proves publication priority. Specialized earlier work on parabolic buildings and counting refinement could still cover the statement; independent literature validation remains needed.

## Value — PASS

This is a natural, complete orbit classification for a non-distributive family of finite lattices of unbounded rank and field size. The exact two-round bound is independent of the enormous size of the lattice, and the exact number of stable colours is independent of \(q\) even though the individual class sizes depend strongly on \(q\). It supplies a descriptive-complexity counterpart to the well-motivated classical flag/Schubert strata and a sharp boundary for one-round detection. The result does not claim isomorphism identification among arbitrary posets, nonnested marked families, or cover-graph refinement.

## Sources and unresolved limits

Primary full-text material read: Berget–Huang (2011), arXiv:1106.1928, Sections 1–4; Kiefer–Schweitzer–Selman (2015), arXiv:1503.08792, introduction, preliminaries and general finite-structure discussion; Arvind–Köbler–Rattan–Verbitsky (2015), arXiv:1502.01255, introduction, refinability hierarchy and individualization/Johnson discussion. Computational checks cover finite samples and do not certify the unrestricted theorem independently. The source comparison is not a comprehensive priority search.

Self-review: passed. Independent audit: not yet performed.

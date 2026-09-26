# Independent audit — 2026/09/09/091

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

I rebuilt the 21×21 adjacency matrix independently from the 21 listed lexicographic S₃ voltages. It is symmetric, has row sum six, and its first six traces are (0,126,204,2074,7750,54636). The fiber-constant seven-dimensional subspace has trace at degree six 6⁶+6=46662, leaving 7974 as the sum of sixth powers of 14 real new eigenvalues. Therefore each |λ_new|⁶≤7974<8000=(2√5)⁶. The old nontrivial eigenvalues are −1; the graph is Ramanujan and λ₂<4.5 follows independently from 7974<4.5⁶. The edge-isoperimetric Cheeger bound h≥(6−λ₂)/2>0.75 holds for this regular graph. The claimed expected sixth trace is supported by the supplied exact walk-pattern enumeration; the explicit member and its stronger result do not rely on this expectation. The decimal spectral survey and purported exact expansion 16/9 were not used.

## Originality — PASS

Hall–Puder–Sawin establish a one-sided existence theorem for arbitrary covering degree, not this listed 21-vertex, two-sided certified member. The fixed voltage assignment and short integer trace certificate are a concrete contribution. I did not establish uniqueness or priority among every small-graph database.

## Scientific value — PASS

A fully checkable three-cover of K₇ with both-sided Ramanujan new spectrum and an expansion lower bound is a useful small explicit benchmark. The sixth-power method gives a loose bound relative to the reported numerical spectrum and does not establish optimality.

Sources: https://arxiv.org/abs/1506.02335 ; https://arxiv.org/abs/1304.4132 ; https://arxiv.org/abs/1801.00876 . Open preprints sufficed.

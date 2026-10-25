# Review of the six-point \(A_5\) local–global Frattini gap

## Correctness
**PASS.** The statement is restricted to the six-point permutation module associated with the Sylow \(5\)-subgroups of \(A_5\) and its finite direct sums over \(\mathbb F_2\). The proof identifies the four invariant submodules of the basic permutation module; shows that the unique maximal proper submodule is the even-coordinate-sum hyperplane; obtains the Frattini subgroup from all maximal subgroups of the split extension; and computes the local Frattini subgroup by intersecting the five Sylow \(2\)-orbit-matching subspaces. The finite group action, module lattice, and five disjoint matchings were independently recomputed with `artifacts/verify.py`, which outputs `VERIFY_OK`. The extension from one summand to any positive number of summands is algebraic, not numerical induction.

## Originality
**PASS, subject to the bounded-source risk stated below.** Costanzo (arXiv:2610.16821v1, full HTML read) supplies the definition and general containment \(\Psi\le\Phi\), but does not state the \(A_5\) six-point split family, its Sylow-orbit matchings, or an unbounded exact quotient formula. Semmen (2006, Example 5.6, full relevant section read from an accessible text rendering) identifies the same permutation module modulo its fixed line as a universal modular Frattini module; this establishes important prior module structure and is acknowledged, but does not compute the local Frattini subgroup of the split extensions. Targeted searches for the precise split group of order \(3840\), the family, and equivalent local/global index formulations found no direct covering source; this is not a claim that no such source can exist. The original Rose and Kaplan–Lev–Mann–Solomon full texts were not obtained, so an unindexed earlier equivalent application remains a residual risk.

## Value
**PASS.** The exact discrepancy \(\lvert\Phi(G_t):\Psi(G_t)\rvert=2^{4t}\) answers a natural quantitative question raised by the introduction of the local Frattini subgroup: the gap is unbounded even with fixed nonsolvable quotient \(A_5\) and elementary abelian kernel. The proof links modular permutation-module radicals to a five-matching partition of the fifteen edges of the complete graph on six points; this is a structural obstruction, not a renamed definition or an isolated arbitrary count.

## Scope and limitations
No optimality, minimal group order, or classification outside the displayed family is asserted. The conclusion is a self-review and not an independent validation or priority certification.

Self-review: passed. Independent audit: not yet performed.

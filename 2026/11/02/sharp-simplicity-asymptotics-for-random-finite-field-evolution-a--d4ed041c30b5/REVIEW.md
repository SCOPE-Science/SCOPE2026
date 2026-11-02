# Scientific review: Sharp simplicity asymptotics for random finite-field evolution algebras

## Correctness — PASS

The claim has precise sampling conventions: every structure matrix is labelled in a fixed natural basis; the conditional sample is uniform on \(\operatorname{GL}_n(\mathbb F_q)\); \(q\) is fixed as \(n\to\infty\); the finite error inequality starts at \(n\ge3\). The proof independently derives the simplicity criterion for invertible evolution algebras, counts every invariant coordinate cut by invertible-block enumeration, and uses two-sided Bonferroni bounds. The error has the correct scale because all non-elementary cuts have at least \(2(n-2)\) forced zeros while intersections of elementary cuts have at least \(2n-3\). The finite-case checker exhaustively verifies the cut formula, connectivity in two implementations, and the bounds in the listed cases; it is not used to infer the all-dimensional theorem. Risk: a reader must distinguish conditioned matrix entries from independent ones; the proof conditions only after unconditional zero-pattern counts, so there is no independence assumption after conditioning.

## Originality — PASS with historical-priority qualification

Kaygorodov–Martín González–Viruel, arXiv:2610.22248, explicitly pose simplicity probabilities for random structure matrices (Question 22) and give the graph criterion (Theorem 6). They do not state the sharp leading correction, the exact singleton-cut probability, or the typical unique source/sink mechanism in the relevant inspected sections. Wei–Zou, arXiv:2310.12368, enumerates isomorphism-class orbits, not the uniform labelled-matrix probability, and Alshatnawi–Costoya–Viruel, arXiv:2607.15154, concerns tensor decompositions and graph balance. Separate searches for coordinate-irreducible random invertible matrices, zero-pattern strong connectivity, and random evolution-algebra simplicity found no equivalent asymptotic formula. These absences are not a proof of priority. Residual risk: a general existing theorem on random irreducible support matrices or conditioned directed graphs might imply the result without using evolution-algebra language.

## Mathematical value — PASS

The survey's random-algebra question asks for the asymptotic simplicity probability; this result gives its exact fixed-field limit for the natural uniform-matrix model and the sharp exponential first correction. The conditional theorem isolates the algebraic effect of invertibility, with a field-dependent constant \(2(q-1)\), and identifies a unique local support obstruction governing almost all failures. It makes a quantitative and structural statement in all dimensions, unlike a fixed-small-parameter census or an elementary existence assertion. Scope limits: no claim about sparse-edge thresholds, isomorphism-class-uniform sampling, real matrices, or random automorphism groups.

## Closest literature and limitations

- I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248, Theorem 6 and Question 22.
- Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, Sections 1–2 and finite-dimensional orbit counts.
- I. Alshatnawi, C. Costoya, A. Viruel, *On the Grothendieck Ring of Finite-Dimensional Non-Degenerate Evolution Algebras*, arXiv:2607.15154, introduction and graph-balance theorems.

The numerical checks cover a few small prime fields only. A broader combinatorial random-matrix theorem could establish priority or subsumption. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.

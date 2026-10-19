# Scientific review

## Correctness — PASS
The universal estimate is obtained from the orthonormal-frame identity and a two-row determinant/trace bound. The constructed example has exactly orthonormal columns, and all row pairs can be classified by their coordinate-axis support. Every E-optimal pair has the asserted singular values, while another pair has condition number one. A standalone script exhaustively checks representative constructed dimensions and independently checks random frames. Numerical checks do not establish the infinite-family theorem; the displayed algebra does.

## Originality — PASS (qualified)
This is the **sharp-order comparison** between global E-optimal and K-optimal *two-row* selections of the same real orthonormal two-column frame. It does not claim that E- and K-optimal experimental designs are generally identical, nor that this distinction itself is new. Bergermann's 2026 deterministic-sketching work motivates the E-objective; Drmač–Gugercin and Avron–Boutsidis analyze inverse singular-value criteria; Ye–Zhou study condition-number design for polynomial regression. None of the inspected relevant statements establishes the \(\Theta(\sqrt N)\) E-versus-K extremal comparison on arbitrary two-column orthonormal frames. Related two-sensor Fourier results are restricted to structured sampling frames, not this worst-case design comparison.

Full-text inspections relevant to the scientific comparison included Sections 3–4 of Bergermann (arXiv:2604.07158), Section 2 of Drmač–Gugercin (arXiv:1505.00370), and the problem formulation/lower-bound arguments of Avron–Boutsidis (arXiv:1201.0127). The accessible abstract of Ye–Zhou (DOI:10.1137/110850268) identifies a different polynomial-regression domain but does not permit whole-paper noncoverage to be asserted. Broad K-optimality and known matrix-selection bounds leave a residual risk of an older unindexed equivalent result.

## Value — PASS
Maximizing a least singular value is a meaningful criterion for deterministic Krylov row sketches, whereas minimizing a distortion ratio is a different criterion. Even with an exactly orthonormal input basis, the two globally optimal selections can diverge by a factor growing with problem size. The example and universal bound together determine the correct dimensional order of the worst separation and identify the nonuniform-leverage mechanism. This is useful for distinguishing numerical design objectives, but is not a bound on an entire Krylov solver, nor on greedy Q-DEIM output.

Self-review: passed. Independent audit: not yet performed.

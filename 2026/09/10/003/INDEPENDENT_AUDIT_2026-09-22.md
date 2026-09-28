# Independent audit — SCOPE-20260910-003

## Scope
Independent review of `2026/09/10/003` at tree `6ac853d60d934237e8b9b4d431ba405e15b4408b`.

## Correctness
**PASS.** The displayed formula
`q P_n(q)=(q-1)^2[(q-1)^n(q^2-3q+3)+(-1)^n(2q-3)]`
checks against direct signed-coloring enumeration on small cases. The transfer-matrix derivation is consistent. The all-`n` zero-free statement is proved analytically: for `q>2`, the even case has two positive summands, while in the odd case `(q-1)f-g=q(q-2)^2>0` and `(q-1)^n >= q-1`. At `q=2`, every odd `n` has a root. The finite Sturm calculations are corroborative, not a substitute for the all-`n` proof.

## Originality
**PASS, narrowly.** Targeted review of the cited signed-chromatic literature found no prior statement of this exact one-edge signed-`K4` subdivision family formula or its sharp uniform real barrier `2`. The audit does not assert broader priority for transfer-matrix methods or zero-free arguments.

## Scientific value
**PASS.** An exact closed form for an infinite natural deformation family, together with a sharp uniform real-root barrier, is a reusable combinatorial datum rather than an isolated numerical observation.

## Literature checked
- Beck et al., *The Chromatic Polynomials of Signed Petersen Graphs*, arXiv:1311.1760.
- Jackson–Procacci–Sokal, *Complex zero-free regions at large |q| for multivariate Tutte polynomials*, arXiv:0810.4703.
- Sehrawat–Bhattacharjya, *Chromatic Polynomials of Signed Book Graphs*, arXiv:2206.08580.
- Greaves–Syatriadi–Utomo, *Chromatic polynomials of signed graphs and dominating-vertex deletion formulae*, arXiv:2407.00883.

## Limitations
The statement is in Zaslavsky's `q`-counting normalization. The originality conclusion is confined to the exact family and formula.

## Disposition
**PASSED.** No substantive research edit is required; add this audit evidence and update only the independent-audit channel in `VERIFICATION.md`.

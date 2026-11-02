# Review of the angularly uncertain rank-one spectral preconditioner

## Correctness

**PASS.** The proof determines the SPD congruence exactly, using its trace and determinant to reduce the condition number to an elementary scalar objective. Its endpoint minimizer is uniquely forced by arithmetic-geometric mean, and a nonnegative derivative for every admissible interior angle proves the same scale is minimax for the full uncertainty interval. A polynomial factorization supplies the unique unshifted failure boundary and exact equality case. All endpoint assumptions and asymptotic quantifiers are stated. The standalone numerical/rational checker returned `VERIFY_OK 42521`. The checker is finite corroboration, not the source of the infinite-domain proof.

## Originality

**PASS, self-review, with historical-priority uncertainty.** The closest directly inspected paper on randomized spectral limited-memory preconditioning supplies the base matrix form and numerical scale comparisons; its statements do not solve an unknown-angle minimax problem. Giraud–Gratton's relevant sensitivity study is first-order rather than an exact all-angle robust optimization, and Diouane et al. optimize fixed-iteration energy error using exact spectral directions rather than the present objective. Relevant published mathematical-result comparisons also concern fixed-oracle Nyström scaling, SOAP normalization and other non-equivalent models. No checked source implies the full claimed law. An older undiscovered exact specialization remains possible; a negative search result is not proof of uniqueness.

## Mathematical value

**PASS.** The theorem gives a sharp calibration of spectral clustering under uncertainty in one approximate Ritz direction, a concrete parameter regime in which an unshifted preconditioner increases condition number, and distinct angular rates needed to avoid such harm versus guarantee uniformly bounded robust condition. These are directly motivated by inexact spectral preconditioning in numerical linear algebra. The classification is intentionally limited to a two-mode real SPD model and does not predict full Krylov iteration counts, higher-rank preconditioner behavior, or finite-precision effects.

## Closest references and remaining limits

Daužickaitė et al., arXiv:2605.23571, Sections 3.1 and 4.2.1; Giraud–Gratton, DOI:10.1137/040617546, Sections 3.2–3.3; Diouane et al., arXiv:2603.28969 and arXiv:2410.02204. The material inspected contains related formulas but no implication establishing the exact robust-angle result. Historical priority requires further external scholarly validation.

Self-review: passed. Independent audit: not yet performed.

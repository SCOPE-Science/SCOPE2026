# Independent audit — Sharp convergence of the AESZ-28 Apéry approximants to zeta(3)

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/sharp-convergence-aesz28-apery-limit--b8f8144d73bc`  
**Audited tree:** `1abc3c4f91ca5fafcc0cb56bfa571a948a2178ca`

## Disposition

**PASSED.** Correctness, originality on the explicitly stated boundary, and scientific value pass. The record may remain in the validated set.

## Correctness

**PASS.** The Casoratian recurrence and its binomial closed form follow directly from the common second-order recurrence. I independently generated the solutions with exact rational arithmetic and verified the closed Casoratian for n=0,...,14. High-precision recurrence calculations then checked the asymptotic constants and first corrections: for n=30,50,80,120,160 the normalized quotient-error coefficient n(E_n/C-1) tends toward -35/48, the normalized linear-form coefficient tends toward -4/3, and n(A_n/(K64^n n^{-2})-1) tends toward -29/48. This independently corroborates the saddle/recurrence derivation and the geometric-tail transfer. The repository's saved verifier also reports 80/80 exact Casoratian checks and corrected ratios converging to 1.

## Originality

**PASS.** Henrik Bachmann's public arXiv abstract establishes the underlying finite Apéry-limit context, while targeted searches for the exact constants sqrt(2)pi^3/84 and sqrt(3)pi/9, the first corrections, and the positive telescoping zeta(3) series did not locate prior coverage. A later SCOPE record, `2026/09/19/sharp-aesz28-apery-limit-convergence--fdd653cbbbb0`, contains the same leading A_n and quotient-error constants but was committed at 20:17 UTC, whereas the assigned record was finalized at 02:13 UTC and is strictly stronger, so it is later overlap rather than prior art. The closely related Sato--Tasaka manuscript cited by Bachmann as in preparation was not publicly available and is retained as an explicit residual risk rather than treated as read.

## Scientific value

**PASS.** The record upgrades a qualitative Apéry limit to a sharp quantitative approximation theorem with leading constant and first correction, determines the associated linear form to two orders, and supplies an exact positive series whose partial sums are the rational approximants. These are coherent quantitative refinements with clear value even though they do not improve an irrationality measure.

## Independent checks

- Generated A_n and C_n independently from the recurrence using exact rational arithmetic and verified the closed Casoratian for n=0,...,14.
- Used 600-digit arithmetic to avoid cancellation and checked the quotient-error, linear-form, and A_n first-correction constants through n=160.
- Checked that the observed 1/n coefficients converge toward -35/48, -4/3, and -29/48 respectively.
- Inspected the saved verification output, which reports 80 exact Casoratian checks and normalized asymptotic ratios converging to 1.
- Compared commit chronology with the later overlapping SCOPE record and confirmed the assigned record predates it.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.18271 — Henrik Bachmann, A q-recurrence for a finite Apéry limit; public arXiv record for the underlying recurrence/limit context.
- https://arxiv.org/abs/2011.03400 — Chamberland--Straub, Apéry Limits: Experiments and Proofs; general Apéry-limit background.
- https://cydb.mathematik.uni-mainz.de/?m=lookup&search=true&sol=3948 — Calabi--Yau differential-operator database entry for AESZ no. 28, used as background for the singular scale.

- `2026/09/19/sharp-aesz28-apery-limit-convergence--fdd653cbbbb0/RESULT.md` (blob `9db6ce38aa47552a407dacac6984c528bde19cfa`) — Later same-day SCOPE record containing the leading A_n and quotient-error constants; committed 2026-09-19T20:17:37Z, after the assigned record's 02:13 UTC commits, so it does not defeat priority.

## Limitations

- The Sato--Tasaka manuscript cited by Bachmann as in preparation was not publicly accessible and was not treated as read; it remains the strongest identified external originality risk.
- The proof relies on standard multivariate lattice Laplace asymptotics for the positive double-binomial sum; the method itself is not new.
- The result does not establish new denominator bounds or an improved irrationality measure for zeta(3).

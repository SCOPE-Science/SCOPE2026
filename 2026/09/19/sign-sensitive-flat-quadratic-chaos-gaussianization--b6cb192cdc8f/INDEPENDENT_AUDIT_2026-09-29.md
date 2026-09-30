# Independent audit — Sign-sensitive sharp Gaussianization of flat quadratic-chaos maxima

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/sign-sensitive-flat-quadratic-chaos-gaussianization--b6cb192cdc8f`  
**Audited tree:** `0063af8d6a461596538c8a783621ee9b1cc15afd`

## Disposition

**PASSED.**

## Correctness

**PASS.** The signed-flat chaos calculation is correct. The exact cgf expands as K(t)=t^2/2+(sqrt(2) rho)/(3 sqrt(m)) t^3+t^4/(2m)+..., and Legendre inversion gives x^2/2-I(x)=(sqrt(2)rho)/(3sqrt(m))x^3+(1/2-rho^2)x^4/m+..., including the essential square-of-skewness term. The stated m/(log p)^(5/3)->infinity condition makes the next Cramer terms o(1) on x=O(sqrt(log p)); Mills/saddlepoint prefactors match, and independence transfers the tail ratio to the Gumbel shift a=4 alpha/3+2 beta and the closed Kolmogorov gap D(|a|).

## Originality

**PASS.** PASS on a narrowed boundary. The earlier SCOPE record `2026/09/18/signed-chaos-maxima-sign-sensitive-gaussianization--948f406a92ce` already contains the positive-flat log^3 threshold, balanced-flat log^2 threshold, their Gumbel shifts/Kolmogorov profiles, and the same-r4 separation. Those endpoint corollaries are therefore not original here. The surviving new content is the arbitrary sign-imbalance expansion with the explicit (1/2-rho^2) quartic correction and the two-parameter interpolating critical shift 4 alpha/3+2 beta; targeted literature searches did not locate that full interpolation for quadratic-chaos maxima.

## Scientific value

**PASS.** After removing credit for the already-published endpoints, the general interpolation still has standalone value: it identifies how skewness and kurtosis jointly control the extreme tail across partially balanced spectra and provides one formula connecting the log^3 and log^2 regimes. This is a meaningful extension rather than a mere restatement.

## Originality boundary

The 2026-09-18 SCOPE record already owns the endpoint log^3/log^2 thresholds, translated-Gumbel constants, and fixed-r4 separation. This audit credits the assigned record only for the arbitrary-rho tail formula and resulting two-parameter interpolation; no endpoint novelty is attributed to it.

## Independent checks

- Re-derived the exact cgf from the product of centered chi-square mgfs and confirmed kappa_3=2sqrt(2)rho/sqrt(m), kappa_4=12/m.
- Symbolically inverted a generic K(t)=t^2/2+A t^3+B t^4 and recovered I(x)=x^2/2-Ax^3+(9A^2/2-B)x^4+O(x^5), which gives the record's coefficient (1/2-rho^2)/m.
- Checked the extreme normalization b_p~sqrt(2 log p): the cubic term tends to 4 alpha/3 and the quartic term to 2 beta, while rho^2 L^2/m=alpha_p^2/L ->0 under the finite-window assumptions.
- Re-maximized the difference of two translated Gumbel cdfs, obtaining D(c)=(1-e^{-c}) exp[-c/(e^c-1)].
- Compared against the earlier 2026-09-18 SCOPE flat-chaos record and isolated the genuinely new arbitrary-rho interpolation from its already-known positive/balanced endpoints.
- Checked Cai–Hu's current abstract: their general theory is effective-rank driven and does not state the explicit flat sign-imbalance Cramer interpolation recorded here.

## Evidence and literature

- https://arxiv.org/abs/2609.20529 — Cai–Hu, Gaussian-chaos phase-transition framework for high-dimensional canonical U-statistics.
- https://arxiv.org/abs/2205.13307 — Fang–Koike, moderate deviations and the centered-chi-square sharp cubic range; background for the positive endpoint.
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/signed-chaos-maxima-sign-sensitive-gaussianization--948f406a92ce — Earlier SCOPE record already containing the positive/balanced sharp thresholds and same-r4 separation.

## Limitations

- Originality does not include the positive-flat and exactly balanced endpoint thresholds or their same-r4 separation; those were already published in SCOPE on 2026-09-18.
- Coordinates are independent and eigenvalue magnitudes are flat; dependence and non-flat spectra are outside the theorem.
- The tail expansion is only proved in the stated m/(log p)^(5/3)->infinity regime.
- Generic cubic and zero-skew quartic moderate-deviation mechanisms are prior art; the novelty boundary is the explicit partial-imbalance interpolation.

## Repository identity

The assigned source-tree SHA `0063af8d6a461596538c8a783621ee9b1cc15afd` exactly matched the current tree at the audited path on `main`; GitHub was read only during this audit.

# Independent audit — Sharp centered critical-point power moments and parity-dependent extremizers

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/sharp-centered-critical-point-moments--f5a111989016`  
**Audited tree:** `0c35a66e2218356f070c19534b7fb8b036555f58`

## Disposition

**PASSED.** Correctness, originality on the explicitly stated boundary, and scientific value pass. The record may remain in the validated set.

## Correctness

**PASS.** The reciprocal-moment inequality follows exactly from p(0)=0 and the constant-term identity prod z_k = n prod zeta_j, followed by AM--GM, so it holds for every lambda>0 and becomes infinite when the origin is a multiple critical zero. Equality forces every nonzero root to be unimodular and every critical point to have radius n^{-1/(n-1)}. Combining self-inversive coefficient identities for q=p/z and the rescaled derivative yields the stated coefficient equation; strict concavity leaves only the endpoint coefficients and, when n is odd, the middle coefficient. Independently, for n=2h+1 the derivative reduces after y=z^h to n y^2+(h+1)t eta y+eta^2, so all derivative roots have the required radius exactly when |t|<=2sqrt(n)/(h+1)=4sqrt(n)/(n+1), confirming the odd-degree family. The radial stability bounds follow directly from the same product identity and x-1-log x>=0.

## Originality

**PASS.** The public abstract of Teng Zhang's arXiv:2609.19126 establishes the global quadratic Tang--Zhang inequality and its binomial equality case, but it does not expose the all-positive-exponent centered theorem, the parity-dependent centered equality family, or the radial stability bounds. Targeted searches for the exact centered radius, equal-critical-radius classification and the sparse odd-degree family did not locate a prior statement, and no earlier SCOPE record found in the September 17--19 inventory gives this theorem. The closest internal polynomial-moment record, `sharp-root-critical-moment-comparison--93c4d53b8501`, is a different normalized complex-moment comparison. Older equal-critical-radius/Smale literature remains a residual risk.

## Scientific value

**PASS.** The result turns a centered product constraint into a complete sharp theorem for every positive reciprocal-power exponent, including subquadratic exponents, and classifies the entire equality locus. The odd-degree one-parameter bifurcation is a nontrivial structural feature not visible in the global quadratic equality case, and the radial stability estimates add quantitative information without overclaiming the harder noncentral problem.

## Independent checks

- Reproved the product identity and all-lambda AM--GM step, including the multiple-zero edge case.
- Re-derived the self-inversive coefficient restriction and checked the concavity argument that only endpoint and possible midpoint coefficients survive.
- For odd degree, reduced the derivative to a quadratic in z^h and independently recovered the sharp parameter bound |t|<=4sqrt(n)/(n+1).
- Re-derived both radial stability inequalities directly from the normalized product variables.
- Searched the repository and public literature for the exact parity-dependent family and found no duplicate.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.19126 — Teng Zhang, Beyond Sendov's conjecture: the quadratic Tang--Zhang inequality; public abstract states the global quadratic inequality and its equality case.
- https://doi.org/10.1017/CBO9780511543074 — T. Sheil-Small, Complex Polynomials (2002); identified as the strongest older residual-risk source for equal-critical-radius/Smale-type material. The relevant book pages were not accessible in this run and were not treated as read.
- https://doi.org/10.1017/S1446788710000030 — Hinkkanen--Kayumov, Smale's problem for critical points on certain two rays; related equal-critical-radius/critical-value context.

- `2026/09/19/sharp-root-critical-moment-comparison--93c4d53b8501/RESULT.md` (blob `4d2893bfab6844b2f3da314121ede2be134fa902`) — Earlier same-day but scientifically distinct theorem controlling normalized complex power moments of roots versus critical points; it does not give the centered reciprocal-radius inequality or parity-dependent equality classification.

## Limitations

- The theorem is only for the distinguished zero at the center; it does not solve the noncentral subquadratic Tang--Zhang range.
- The stability statement is radial and does not control angular distance to the extremizer family.
- The full cited pages of Sheil-Small's book were not accessible in this run and were not treated as read; equivalent older classification under different terminology remains a residual originality risk.

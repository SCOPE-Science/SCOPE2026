---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the lacunarity dichotomy

The proof is self-contained. The crucial exact identity is the adjacent-slope parametrization
\[
\|f_s\|_{\mathrm{Lip}}=\sup_n\|s_n\|,\qquad f_s(t_n)=\sum_{j=n}^\infty(t_j-t_{j+1})s_j.
\]
All series converge absolutely by telescoping. Every distance quotient on the ordered set is a convex combination of these coefficients. The sufficient direction estimates the difference between an adjacent slope and the slope from the accumulation point by \(2\|f\|_{\mathrm{Lip}}t_{n+1}/t_n\). The necessary direction chooses separated near-maximal coefficients at indices where that ratio is at least \(\delta\), giving the exact uniform bound
\[
\sup_n\|f(t_n)\|/t_n\le (1-\delta/2)\|f\|_{\mathrm{Lip}}.
\]
Isolated-point nonattainment additionally uses that every finite average of strictly subnorm coefficients stays strictly subnorm, while quotients toward the sole limit point converge to an already bounded, subnorm value.

A finite rational sanity test for the geometric example, using 100 weights and a sparse support every fourth index, produced a base-point quotient at most approximately 0.507 against the analytic upper bound 0.75 and strictly subnorm quotient values at the sampled isolated points. This is a check of the signs and indexing, **not** a substitute for the infinite proof. The analytic argument establishes all infinite claims. Source comparison is limited to the listed papers and searches; an independent audit has not been performed.

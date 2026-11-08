---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the simple symmetric K_{a,b} game (a,b≥1), an agent in U with old block type (u_i,v_i) strictly prefers a candidate (x,y) iff y*u_i>x*v_i; for W iff x*v_j>y*u_j. For each x,y≥1 independently choose x of A_pi(x,y) eligible U and y of B_pi(x,y) eligible W, giving the exact size polynomial and no duplicate coalitions; one-sided coalitions cannot strictly improve. Rational rank threshold sorting and binomial table yield the arithmetic-operation bound. In the a paired U-W plus m singleton W partition, paired W and paired U strict requirements conflict, so all selected W must be singletons: M(a,m)=sum_x sum_{y>x} C(a,x)C(m,y), m≤1 no blockers, m=2 exactly a blockers. For m=a+t√a+o(√a), 2^a ε=P(Y>X,X≥1)→Φ(t/√2) by binomial central limit; outside m/a→1 use Chebyshev. Formula does not use bit-complexity claims.

## originality

PASS

Best-of-knowledge originality is a statement/implication comparison, not a title-match test. The exact established object, parameters, finite tables and known stronger results were cross-checked against published Resultary findings and primary literature; no decisive prior coverage of the final claim was established. Highly plausible inaccessible sources and indirect possible corollaries are disclosed in residual_risks. Searches alone are not novel proof.

## value

PASS

For every partition, a natural stability statistic is the full blocking-size distribution, finer than existence of a stable partition or a generic ε-bound; the exact tractable formula makes size-selective deviations calculable. The matched-pair threshold and Gaussian imbalance transition identify a meaningful structural boundary in this canonical two-type setting, beyond a bare normalization computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

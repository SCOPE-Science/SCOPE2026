---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Using the weighted Matrix–Tree theorem, rooted Cayley-forest normalizer Phi_j(t)=t(j+t)^{j−1}, Phi0=1. Choosing two disjoint distinguished components yields exact E Z_k and E Z_k Z_l and their ratio R_{n;k,l}. For feasible k+l≤n, d log R/dt=−(t+1)[(t+n)^{−1}+(t+m)^{−1}−(t+n−k)^{−1}−(t+n−l)^{−1}]<0 by strict convexity of reciprocal. The t→0+ ratio exceeds 1 by strict log-convexity of j^{j−1}/j!, t→∞ tends to a strictly subunit factorial ratio, proving exactly one zero. Infeasible pairs have product count zero. Crossed second derivative of H_t(x)=(x−1)log(x+t)−logGamma(x+1) and uniform trigamma expansion give n² H_{c sqrt(n)}''→3/2−c², so t*/sqrt(n)→sqrt(3/2) for fixed k<l. Independently checked n3 k1 l2 ratio equation gives t*=3/sqrt(2); inspected exact independent Prüfer enumeration verifier for n≤6.

## originality

PASS

Pitman, Avena–Gaudillière and D’Achille–Enriquez–Melotti provide the root-weighted complete-graph forest measure, component counts and one-root local component laws; these are acknowledged rather than claimed new. The new claim is the sharp sign-reversal and universal square-root location of the covariance of *two distinct component-size counts*. Full current 2026 D’Achille article concerns one-component distribution/local limits, not a covariance theorem; any implicit consequence of more general forest partition formula remains a historical risk.

## value

PASS

The sign of correlations between two natural component-count observables changes exactly once as component fugacity varies. A universal sqrt(n) crossover constant independent of the fixed component sizes is a substantive structural phase diagram relevant to random labeled forests, even without CLT or arbitrary-graph generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.

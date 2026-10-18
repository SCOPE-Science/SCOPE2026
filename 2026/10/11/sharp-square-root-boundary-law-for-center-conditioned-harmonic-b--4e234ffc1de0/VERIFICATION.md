---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The final claim is for every complex harmonic f:D→closed D with |f(0)|=a and the two-sided Fourier majorant. Reconstructed L∞ Poisson boundary trace and Parseval: sum over n≠0 |c_n|²≤1−a². Cauchy–Schwarz against weights r^|n| yields B_f(r)−a≤sqrt(2(1−a²))r/sqrt(1−r²), equivalent to admissible r²≤(1−a)/(3+a). Independent Taylor integration of the explicit unimodular even trace exp(i ε cos θ) gives c_0=1−ε²/4+O(ε⁴) and c_{1}=c_{−1}=i ε/2+O(ε³). The first harmonic alone violates the majorant above r=(1−a)/(ε+O(ε³))=(1/2+o(1))sqrt(1−a). The mean is strictly decreasing for small ε>0 so witnesses every nearby a. Harmonic maximum principle at a=1 forces f constant and R_H(1)=1. Hence exact sharp endpoint law but no claim of globally exact R_H(a) for interior a.

## originality

PASS

Best-of-knowledge statement/implication comparison, including direct relevant published Resultary and primary-source reading. Exact assertions are distinguished from weaker bounds/other assumptions. No claim of exhaustive priority certification.

## value

PASS

The center-conditioned radius is a natural extremal invariant. Correcting a recent asserted best-possible linear radius on its actual all-bounded-harmonic class, with both a globally stronger admissible bound and an exact leading asymptotic constant, is mathematically useful; the discontinuity at the constant endpoint clarifies the absence of a center-uniform radius. This is not a reformulation of the older negative uniform-radius statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.

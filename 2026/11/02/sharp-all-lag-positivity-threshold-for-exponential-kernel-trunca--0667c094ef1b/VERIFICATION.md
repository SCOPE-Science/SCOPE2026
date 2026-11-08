---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reconstructed denominator recurrence P_0=1, P_1=5/2, P_2=25/4-a, P_n=(5/2)P_{n-1}-aP_{n-2}+(a^2/6)P_{n-3} with a=5/3+r. Exact rational expansion yields P_6=g(r)/46656. Read the actual verification certificate.py blob; independent rational Bernstein conversion verified 326 strictly positive Bernstein coefficients for n<=30, n!=6, on [4/5,9333/10000], and g has unique sign-changing zero in (9332/10000,9333/10000). For n>=31 the factorization into real pole s and conjugate pair of modulus R, with rho=s/R<997/1000, bounds rho^(n+1) sqrt((1-2rho c+rho^2)/(1-c^2))<1, proves positivity for every tail index, not by finite extrapolation. For r>15/16 nonreal dominant poles and analyticity at positive radius violate Pringsheim if all coefficients were >=0. Independent recurrence signs tested through n=600 at representative r. BDF2 threshold 1/2 checked separately.

## originality

PASS

Ferrari 2026 introduces and optimizes the TTR2 symbol, so the method is explicitly prior; the inspected full paper does not give coefficientwise exponential CQ all-lag sign threshold. Karaa 2024 studies positive-definite convolution forms, not all coefficient signs. This is a new exact sharp numeric/algebraic cutoff according to bounded primary comparison, with possible unindexed weight-sign literature residual.

## value

PASS

The threshold is a sharp coefficientwise monotonicity/positivity stability guarantee for a named second-order CQ method and scalar exponential memory kernel; the exact first failure at lag six and necessity for all larger steps are mathematically meaningful. It sharply differentiates entrywise positivity from A-stability and quadratic form positivity and quantifies gain over BDF2.

The dated certificate retains the supplied scientific assessment, sources and limitations.

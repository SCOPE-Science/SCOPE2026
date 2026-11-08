---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For Y_i=Z_i², decompose first n terms as T W_i with T~chi²_n and W~Dirichlet(1/2,...,1/2) independent. Then S=T² V_n and Δ=(q/m)(T/n−T′/q), with T′ independent chi²_q; conditionally beta_hat-beta=σG/(T sqrt(V_n)). T negative moments are finite iff exponent<n/2, and V_n^-r/2 near the interior barycenter iff r<n−1; this yields slope exponent r<n/2 and the n>=3 sharp tail constant. Conditional unbiasedness holds for n>=3, while T^-1 divergence destroys integrability for n=2 and T^-2 gives variance cutoff n>=5 (V^-1 also finite then). Total variance gives stated formula; independent sympy verifies rational simplification 2(n²+nq+4q)/[n²q(n−2)(n−4)] and corresponding gain threshold. The exact all-integer assertion follows from factorization and polar integrability, not MC checks.

## originality

PASS

The two-phase regression estimator itself is classical (Yang–Ding eq. 1); the assessed candidate is its exact heavy-tail, moment and MSE law when the same fitted slope is reused with chi-square-one auxiliary response. Earlier nested MFMC papers give optimal population coefficients or warnings about fitted variance but not the inspected exact cutoff n=5 and K_n criterion. Best-of-knowledge with explicit prior regression-literature risk.

## value

PASS

A precise small-pilot failure mode for a natural noisy quadratic auxiliary variable: exact unbiasedness can coexist with infinite variance, and the exact five-pair cutoff and fit-correction gain criterion are practical finite-sample invariants of a standard two-phase regression construction. The example is motivated by pilot reuse and ill-conditioned slope estimates, not an arbitrary distributional slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

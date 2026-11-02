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

# Verification

The accompanying `check.py` numerically integrates the two exact eigenvalue representations for three polynomial exponents, two complex Gaussian parameters and four sample degrees; it also checks the normalized complex Watson factor at a larger finite degree. It was executed from the delivered code and returned `CHECK_OK`. The calculations are finite evidence for normalization and signs, not proof of an infinite asymptotic or a novelty certificate.

The analytical checks are independent of numerical sample size: angular orthogonality gives the diagonal representation, Gamma–Laplace integration is valid since \(\operatorname{Re}a>0\), a split Watson estimate gives uniform \(O(n^{-1})\), and the endpoint Schatten conclusions follow by comparing \(|\lambda_n|\) to \(n^{-\tau}\). For approach-to-criticality, the relative \(O(n^{-1})\) produces a uniformly bounded error in \(p\)-th Schatten sums, while elementary Abelian asymptotics give the stated power and logarithmic constants.

Scope limitations: no extension to arbitrary Fock weights, arbitrary nonradial symbols, or naive whole-space unbounded-symbol Toeplitz products; independent audit not performed.

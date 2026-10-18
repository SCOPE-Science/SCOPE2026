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

# Verification record

The analytical proof uses exact finite-column Gram products, a compact rank-one defect, a strictly decreasing scalar secular equation, the classical digamma partial-fraction sum, the large-argument asymptotic of the digamma function, and Riemann-sum convergence. It also derives an exact finite-compression negative-index test by congruence.

Run `python verify.py` after installing `requirements.txt` to reproduce supplementary checks. In the tested package, the script passed 1,296 rational Gram identities and 85-digit root/detection-horizon diagnostics at \(\varepsilon=0.3,0.2,0.1,0.05,0.02\). At the smallest tested \(\varepsilon\), the first negative compression dimension exceeded \(10^{21}\), established by high-precision evaluation of the closed digamma test and integer bisection, **not** by constructing that matrix. The limiting prefactor and mode normalization were numerically approached, not certified for infinitely many parameters by computation.

The analytic proof, not the finite checks, establishes existence, uniqueness, the sharp limits, and the distributional statement. The original self-commutator's unique negative eigenvalue is not assigned the auxiliary defect's numerical size.

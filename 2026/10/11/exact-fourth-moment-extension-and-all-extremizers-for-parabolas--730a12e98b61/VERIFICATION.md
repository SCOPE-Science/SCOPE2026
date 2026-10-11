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

# Verification of the fourth-moment parabola theorem

Run `python3 checker.py` in this directory using Python 3 standard libraries; there are no downloaded data or package dependencies. The code reconstructs every quadratic pair fiber for the tested rings, checks all of their cardinalities against the valuation-based formula, evaluates the resulting quadratic collision bound with exact Gaussian-integer arithmetic, and confirms explicit extremizers. Some small-modulus cases are independently checked by direct complex Fourier summation.

The recorded successful execution returned `EXACT_CHECKS_PASSED 85388`, with test moduli \(3,5,7,11,9,25,49,27,125,81,243\). These are actual finite tests, not an exhaustive enumeration of complex inputs, not an automatic verification of every equality case, and not an infinite-family proof. The proof in `RESULT.md` derives the infinite-family formulas and equality characterization from orthogonality, congruence-root counts, convexity and equality-in-Cauchy arguments.

The original result concerns only odd-prime powers. No analysis of even moduli or mixed-prime moduli is claimed. Independent mathematical review remains unperformed.

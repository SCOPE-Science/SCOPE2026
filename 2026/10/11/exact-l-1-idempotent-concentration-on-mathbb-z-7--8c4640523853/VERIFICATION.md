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

The analytic proof reduces the unrestricted optimization to support sizes \(1\), \(2\), and \(3\), classifies the three-subsets into exactly two affine orbits, computes each candidate ratio, and separates them with exact algebraic inequalities.

`artifacts/verify.py` independently enumerates all \(127\) nonzero subsets of \(\mathbb Z_7\), checks that exactly the seven consecutive triples maximize the ratio, verifies the \(21+14\) affine-orbit split, checks the two relevant minimal polynomials and rational isolating signs, and verifies the difference-set Fourier magnitude identity.

Replay with `python artifacts/verify.py` using `artifacts/requirements.txt`. The finite enumeration confirms the classification; it is not used to infer any infinite statement.

Scientific limit: only modulus \(7\) is proved. No claim is made for arbitrary prime moduli or for the uniform asymptotic endpoint constant.

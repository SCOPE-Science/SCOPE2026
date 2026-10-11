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

# Reproduction and evidential limits

Run `python3 verify.py` using Python's standard library. The script exhaustively constructs each claimed nonsplit conic and verifies the uniqueness of each nonzero unordered two-sum. It recomputes convolution fourth moments over exact Gaussian integers and checks equality for a constructed optimizer at every tested field order. It also checks 100 deterministic random coefficient vectors against the proposed sharp bound per tested order.

Tested orders: \(3,5,7,9,11,13,25\). The orders \(9\) and \(25\) are implemented as explicit quadratic extensions, not treated as integers modulo a prime. All seven test cases pass.

The universal proof is in `RESULT.md`: anisotropic affine-line intersection gives two-sum uniqueness; the exact moment identity counts the zero fiber; triangle inequality, arithmetic–geometric mean, and Cauchy–Schwarz yield the sharp scalar maximum and equality classification. Numerical or finite-order trials alone would not prove that universal claim. No independent audit has been performed.

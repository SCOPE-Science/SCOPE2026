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

# Computational verification and limits

Run `python checker.py` using a standard Python 3 installation. The script has no third-party dependencies and expects the line `VERIFY_OK checks=7636 constant=5.284234933512 inner_outer_modulus=1.145311176707`.

The script checks 729 exact-integer sextic identities. It evaluates complex Fourier sixth moments directly on cyclic groups of orders \(7,8,9,10,11,12,13,14,17,19,23,31,47\), compares them with cubic convolution, and tests the sharp inequality for 260 deterministic complex coefficient vectors at each order. It separately verifies 11 extremal phase choices per group order and strict threshold failure for \(3\le N\le6\). A separate symbolic algebra expansion confirmed that the polynomial reduction and factored derivative identities hold identically, not just for the tested values.

The mathematical proof of the all-group result is in `RESULT.md`. Finite numerical experiments alone cannot justify unrestricted dimensions, all coefficients, exact equality, or originality. No independent mathematical audit has been performed.

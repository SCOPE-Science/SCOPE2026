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

The standalone stdlib Python checker `verify_nijenhuis_squarezero.py` can be run with `python3 verify_nijenhuis_squarezero.py`. It constructs the square-zero multiplication directly and verifies the full associative Nijenhuis identity on basis pairs for every linear map in the five enumerated small cases. It separately tests the necessary/sufficient block condition and then compares the exact rank histogram to the closed Gaussian-coefficient formula. An extension-field check uses GF(4) arithmetic modulo a degree-two irreducible polynomial.

Observed exhaustive outputs:

- `n=1, q=2`: 6 operators; ranks (0,1,2) have counts (1,3,2).
- `n=1, q=3`: 15 operators; ranks (0,1,2) have counts (1,6,8).
- `n=2, q=2`: 56 operators; ranks (0,1,2,3) have counts (1,16,27,12).
- `n=2, q=3`: 459 operators; ranks (0,1,2,3) have counts (1,58,208,192).
- `n=3, q=2`: 1,920 operators; ranks (0,1,2,3,4) have counts (1,78,623,882,336).
- `n=2, q=4`: 1,984 operators; ranks (0,1,2,3) have counts (1,138,765,1080). This last check enumerates parameter tuples rather than every linear map.

The complete run ends with `VERIFY_OK`. The arbitrary-field normal form and finite-field counts have algebraic proofs; these finite enumerations are consistency checks only and do not establish an infinite theorem. The verified statements concern the specified multiplication, not other nilpotent local algebras.

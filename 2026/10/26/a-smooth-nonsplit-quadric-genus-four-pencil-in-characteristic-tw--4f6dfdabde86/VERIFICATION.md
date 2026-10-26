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

# Reproduction and verification

Execute `python3 verify.py` in an environment with SymPy. No network, random seeds, external databases or precomputed mathematical logs are required.

The verifier expands the exact Segre pullback identity modulo two. Its independent binary-field implementation then chooses trace-one parameters and checks the rational point and intersection-Jacobian rank at every curve point for characteristic-two fields of orders \(4\), \(8\) and \(16\). It also checks the base-\(\mathbb F_4\) curve over \(\mathbb F_{16}\) and the base-\(\mathbb F_8\) curve over \(\mathbb F_{64}\). One completed execution returned:

```
GF(2^2) embedded in GF(2^2): c=2, t=2, kappa=2, points=7, singular=0
GF(2^2) embedded in GF(2^4): c=6, t=6, kappa=6, points=25, singular=0
GF(2^3) embedded in GF(2^3): c=1, t=2, kappa=2, points=13, singular=0
GF(2^3) embedded in GF(2^6): c=1, t=14, kappa=14, points=77, singular=0
GF(2^4) embedded in GF(2^4): c=8, t=2, kappa=14, points=23, singular=0
VERIFY_OK
```

The polynomial identity, derivative argument on both affine and boundary charts, connectedness, adjunction, and gonality proof in `RESULT.md` establish the infinite family. Checks at a finite set of field sizes are supplementary consistency tests and do not certify smoothness over an algebraic closure. Independent audit and validation have not been performed.

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

# Verification notes

The accompanying `verify.py` was executed with Python 3. The direct full enumeration of all Lie homomorphism matrices for the three-dimensional Heisenberg Lie algebra gave complete rank spectra for the finite fields of orders 2, 3, and 4: respectively `[1,21,18,24]`, `[1,104,192,432]`, `[1,315,900,2880]` in increasing rank order. The binary five-dimensional case independently enumerated all quotient matrices and center functionals and obtained the full rank profile `[1,465,15750,37800,11520]` for ranks `[0,1,2,3,5]`. The tested full enumeration had 65,536 maps. Exact normalizations and nonzero-rank support were additionally checked for finite field orders 2, 3, 4, 5, 7 and dimensions indexed by `m=1,...,7`.

The successful terminal token was `VERIFY_OK_HEISENBERG_ENDOMORPHISM_RANKS`. These finite tests do not certify the infinite family by themselves; the result rests on the symbolic symplectic-frame and rank proof. This verification is not an independent mathematical audit.

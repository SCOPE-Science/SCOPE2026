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

Run `python3 verify.py` in the directory extracted from the package; requires Python 3 and SymPy. Expected output: `VERIFY_OK: characteristic-three cubic discriminant identities and module basis`.

The actual test symbolically checks the polynomial parameter identity, its characteristic-three derivatives, three \(k[a,c]\)-module stability products, and the normalization cubic relation. The proof in RESULT.md establishes the **universal** conductor via coefficient-divisibility in a free module, not by interpolation or finite-field testing. This checker is a corroborating exact symbolic replay and is not independent scientific validation. The object is the affine monic discriminant; global projective claims are not asserted.

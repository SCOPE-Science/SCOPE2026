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

To reproduce the standard-library finite-field tests, execute `python3 verify_affine_quandle.py`. The program exhaustively checks every coefficient vector in six small prime-field affine-quandle algebras and compares the idempotent set to the parametric logarithmic formula. It additionally verifies logarithmic resonance generators for five larger primes. The observed marker is `MODULAR_AFFINE_QUANDLE_IDEMPOTENTS_OK 6 5`.

For the nonzero-idempotent closure claim, direct pairwise multiplication was separately verified for the 49-element subquandles at prime seven and parameters three and four, covering 2,401 products per quandle. The proof of the general quandle law is symbolic and does not rely on these finite tests. Arbitrary extension fields and all prime orders have not been exhaustively enumerated. Independent audit was not performed.

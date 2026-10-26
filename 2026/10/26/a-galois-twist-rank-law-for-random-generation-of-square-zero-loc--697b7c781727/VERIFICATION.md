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

The general proof uses a coefficient-field splitting, decomposition of the square-zero radical into Galois-twisted bimodules, the classification of crossed derivations, and independent rank counts after invertible row operations. No exhaustive finite computation is asserted to establish the theorem for arbitrary dimensions.

Run `python3 verify_generation.py` from the same directory. The script defines the field with four elements as a polynomial quotient over the binary field, implements the displayed algebra product, and closes all generated algebras under multiplication and binary linear span. It checks exact enumerations of ordered pairs in six radical configurations, two single-generator configurations, the conditional full profile for distinct twists, and the rank distribution when the same nontrivial twist occurs twice. The calculations are finite and reproduce explicit numerators and denominators independently of the general proof.

The identity-twist and nonidentity-twist cases differ because ordinary finite-field derivations vanish whereas crossed derivations are inner. The proof depends on the residue field being separable over the base field and on the square-zero hypothesis. The general result has not been independently validated.

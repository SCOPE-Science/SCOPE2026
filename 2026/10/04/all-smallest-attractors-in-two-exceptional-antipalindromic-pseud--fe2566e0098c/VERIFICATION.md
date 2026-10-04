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

The universal proof is the periodic occurrence-interval and residue argument in `RESULT.md`. The finite verifier is corroboration only.

`verify.py` first reconstructs each generalized pseudostandard prefix from the shortest antipalindromic-closure definition. It then builds, from scratch, the union of occurrence intervals for every distinct factor and tests every singleton and every position pair directly against the string-attractor definition. For \(2\le n\le14\), it compares the exhaustive pair sets with the stated closed-form classifications while checking the prefix identities. It independently stress-tests the closed-form words through \(n=40\).

The recorded execution ends with `VERIFY_OK A_n=2..40 B_n=2..40 exact_pair_classification`.

The verifier does not enumerate unbounded \(n\); it is therefore not a certificate for the universal statement without the written proof. It does not address other directive sequences or larger minimum-attractor sizes.

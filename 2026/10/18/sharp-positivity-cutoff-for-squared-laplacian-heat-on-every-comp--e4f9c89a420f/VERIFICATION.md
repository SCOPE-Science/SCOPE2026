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

The analytical proof covers all part counts and sizes. The root-ordering lemma is established by derivative sign changes in two variables, not by extrapolation from the numerical table. Cross-part entries, within-part entries, and endpoint norm identities follow from an exact projector decomposition.

`verify_biheat_multipartite.py` reconstructs each tested graph's squared Laplacian independently and uses standard-library scaling-and-squaring matrix exponentials, distinct from the closed-form projector derivation. The recorded run completed with `PASS 43847 numerical equalities; 82 graph designs; half_size_u 2.437511453744`. It also checks bounded-input norms at both sides of the cutoff and the two contrasting asymptotic regimes. Floating-point tolerances are explicit in the script. No claim of exhaustive computation or independent certification is made.

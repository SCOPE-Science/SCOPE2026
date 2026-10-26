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

# Reproducible verification and scope

Run the provided standalone `verify.py` with Python 3.8 or later; it has no external package dependencies. Its expected success marker is `VERIFY_OK`.

The checker uses explicit finite-field natural-basis square tables. A modular Gaussian elimination checks the determinant formula against all sampled coefficient tuples; the checker verifies every asserted lift of every rotation by comparing both sides of each defining square relation. For small \(n\), every possible monomial scalar assignment consistent with a graph rotation is enumerated and tested against multiplication, without assuming cubic roots in advance. These independent finite computations check critical calculations and the absence of extra field-point automorphisms in the enumerated cases; the complete infinite-domain argument rests on the proof in `RESULT.md`.

Actual replay results: 1,314 coefficient tuples checked for determinant and perfection, 15,390 explicit lifts checked, and 81 cases of exhaustive monomial scalar enumeration; success marker `VERIFY_OK`. The exceptional parameter case \(n=3,P\ne1\) originates in reference [1] and is not an originality claim. Group-scheme structure, unrestricted coefficients and characteristic two or three are not verified or asserted. Independent validation was not performed.

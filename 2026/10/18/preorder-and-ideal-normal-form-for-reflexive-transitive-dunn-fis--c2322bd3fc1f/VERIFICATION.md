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

The reproducibility program `verify.py` uses only the Python standard library. Execute `python3 verify.py` from a directory containing that program; successful execution ends with `VERIFY_OK`.

Method A exhausts all reflexive binary relations on a star with \(1\) to \(4\) leaves, filters by transitivity, then tests the original (FS1), (FS2), (CJ2) relational inclusions and the claimed canonical triple independently. It counts orbits under all permutations of leaves. Method B enumerates all labelled finite partial orders on up to five vertices, checks order ideals and the Stirling formula, canonicalizes partial orders, and applies Burnside's cycle formula to positive multiplicity assignments.

Expected labeled counts for leaf counts \(1\) through \(5\): \(4,20,189,3084,81536\). Expected unlabeled counts: \(4,13,50,232,1303\). The direct relation-orbit method checks both columns through four leaves; the poset method checks both through five. These exhaustive finite results are checks, not proofs for arbitrary widths; the unrestricted claims require the normal-form argument and Burnside derivation in `RESULT.md`.

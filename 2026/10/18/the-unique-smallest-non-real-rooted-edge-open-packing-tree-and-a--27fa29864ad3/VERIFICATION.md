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

# Reproducible checks

Run `python3 verify_roots.py` from this directory. Python standard library alone is sufficient. It enumerates all selected-edge subsets on canonical representatives of every unlabeled tree of order at most six and checks the full edge-open-packing coefficient vector by direct conflicts between distinct selected edges. It checks the exact polynomial for every one-subdivided star with \(2\le d\le9\), as well as the strict Newton inequality for \(4\le d\le100\). It prints `VERIFICATION_ROOTS_OK` on success; retained output is in `verification_roots_output.txt`.

The proof for unbounded broom size is the coefficient factorization and strict Newton inequality. The six-vertex minimality proof is a finite complete classification by tree isomorphism classes, not a partial sample. The verifier does not establish bibliographic priority, nor is this an independent mathematical audit.

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

## Exact reproducibility
Run `python verify_fano.py` in the directory of the embedded files. It enumerates all 35 triples, confirms exactly five translation orbits, tests all orbit pairs and the action of each unit multiplier. This is a finite exhaustive check, supplemented by the direct mathematical proof in RESULT.md.

## Scope and limits
The checks do not compute ambient homology, classify all subgroups of the symmetric group, or demonstrate uniqueness in all literature. The normalizer conclusion follows from the explicit affine-permutation argument rather than a computer-only observation. Independent external verification has not been performed.

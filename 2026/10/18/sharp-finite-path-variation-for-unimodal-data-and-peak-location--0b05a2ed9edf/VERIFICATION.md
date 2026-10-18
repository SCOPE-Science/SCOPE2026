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

# Verification of unimodal path maximal variation

Run `python verify.py` with a standard Python 3 interpreter. It uses the built-in `fractions` and `itertools` modules and no downloaded data. The script independently constructs every centered graph ball, computes its exact mean, and takes the maximum at each vertex.

An observed successful run printed:

`VERIFY_OK exact_unimodal_vectors=13652 nonconstant=13620 rational_profiles=4`

The exhaustive finite search covers all unimodal values in `{0,1,2,3}` for lengths 3 through 10, tests the maximal output's peak location, the exact peak-location lower deficit, the full sharp variation inequality and all nonconstant equality cases; it also covers four hand-selected rational vectors. No numerical tolerances occur: all averages use rational arithmetic.

Proof for arbitrary length and real values is supplied in `RESULT.md`; finite enumeration cannot certify infinite quantifiers. Historical priority is a qualified source-based comparison, not a machine-proved fact. Independent external audit has not been performed.

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

The proof uses a unique zero-gap decomposition, an exact formula for the scattered occurrence count, and a product bound on active gap weights. The upper bound on numerator exponent and the sharp boundary case are proved for all positive parameters; enumeration is an auxiliary check, not a substitute for these infinite arguments.

To reproduce the computational check, run `python3 check.py`. It verifies 702 parameter-length coefficient identities through word length 12, checks polynomial onset for each tested instance, and establishes nonzero boundary discrepancies in 54 parameter triples. The code independently computes subsequence occurrences by dynamic programming; the enumerator uses integer vector partitions. `check_output.txt` records its result. These finite checks do not prove novelty, completeness of the literature search, or correctness for untested parameters.

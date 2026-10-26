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

# Reproducibility and scope

Run `python3 verify.py` with a standard Python 3 interpreter; no nonstandard packages are used. Successful completion emits the marker `GENERALIZED_BASE_REFLECTION_PASS`.

The script performs exact finite modular-set tests for 104 base/modulus pairs (bases 3 through 10, moduli 3 through 15), comparing full predicted length-two, length-three and length-four factor sets with their gcd formulas, and checking reversal incompatibility. Separately, it generates digit-sum prefixes of lengths appropriate to 13 smaller base/modulus pairs, tests complete equality of 39 directly observed length-two/three/four factor sets with the symbolic predictions, and checks sampled length-five-through-eight reversal absence.

Those experiments cannot prove factor completeness or reversal avoidance throughout an infinite sequence. The unbounded result instead follows from the constructive adjacency-realization lemma and the proof that each length-four factor has at least two internal increments equal to \(+1\). Existing full-length factor-complexity values are attributed to Starosta (arXiv:1104.2476). Unindexed overlapping literature remains possible. No independent audit has been performed.

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

The analytical proof of the complete dyadic-residue Gram identity uses exact character orthogonality of the Walsh matrix on full blocks. It applies to every allowed dyadic ambient dimension, block size, coordinate support, signature, and sampled index tuple. In particular, it independently establishes all-support universal isometry, the one-residue rank ceiling, and the exact two-column binomial law.

The accompanying `check.py` script uses Python 3 standard-library integer arithmetic only. Executing `python3 check.py` evaluates 169168 direct Walsh Gram inner products against the closed formula, counts every small coordinate subset with distinct low-order residues (25 count checks), and exhaustively checks the rank-loss frequency for the indicated small parameter ranges. The actual replay returned `Passed 169168 exact Gram checks and 25 exact subset-count checks.` The computation is finite and is not an exhaustive certification of the all-dimension theorem.

The theorem does not assert an independent mathematical audit. Its limitations include lack of applicability to row-scrambled variants, non-coordinate subspaces, or sampling without replacement.

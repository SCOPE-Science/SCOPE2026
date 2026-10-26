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

# Reproducibility of the finite tree-automaton certificate

Run `python3 verify.py` with Python 3 and no third-party dependencies. It prints `VERIFY_OK`, the twelve first-appearance masks, a least reset height of 11, a full-context witness with 12 distinct variable leaves, and the least-height table for all 15 nonempty subset masks.

The `layer_reach` computation constructs the entire bounded-height closure under all unary and ordered binary applications. The `independent_min_height` routine obtains the minimal heights through a separate cost-fixpoint relaxation, using \(1+\max\) for a binary parent. The explicit witness is materialized with fresh variable identities and evaluated over all combinations of independent child images.

This is an exhaustive finite proof certificate for the displayed transition table, not a sampling argument. The universal upper bound and one-symbol exclusion have mathematical counting proofs in `RESULT.md`. The certificate does not address state counts greater than four and does not constitute external validation.

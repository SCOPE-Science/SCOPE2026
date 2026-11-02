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

# Reproducibility

Execute `python3 checker.py` using Python 3 standard library. The checker independently enumerates 19,683 combinations for the three-element chain's three-successor/modal truth-table aggregation and 1,048,576 combinations for the four-element Boolean algebra. It constructs a finite sparse universal model on every depth-type for parameter choices (two truth values, one variable, depths 1 and 2), (three truth values, one variable, depth 1), (four Boolean truth values, one variable, depth 1), and (two truth values, two variables, depth 1). For every constructed state it recomputes full depth signatures from the actual weighted graph, tests all characteristic-successor coordinates, and verifies exact state/positive-edge counts. The run ends with `ALL_CHECKS_OK`.

Proof boundaries: finite exhaustion checks do not prove the all-size result. The paper's lattice, truncation, distinguishability, realization, lower-bound, and equality-case arguments provide the general proof. This verification does not establish novelty, peer review, or independent certification.

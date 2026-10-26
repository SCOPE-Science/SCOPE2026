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

Run `python3 check_unitary_tail.py` from the extracted directory. It requires only the Python standard library. The recorded check passed 34,902 deterministic assertions covering dimensions \(2\) through \(22\), multiple thresholds above the theorem's boundary, rank-one phase-unitary constructions, strict event probabilities and their upper bound.

The universal upper bound relies on row-normalization and a support-counting argument. Its optimality uses the explicit complex rank-one phase perturbation with off-diagonal squared modulus approaching the qualifying threshold from below. The verifier confirms finite samples of these formulas; it does not establish infinite-dimensional quantifiers or external publication priority. Independent audit has not been performed.

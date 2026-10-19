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

The analytic proof is in `RESULT.md`. For independent finite checking, run `python verify_markov_run_tv.py` with Python 3 (standard library only). It exhaustively enumerates all binary strings through length eight under six pairs of exact rational Markov transition parameters and verifies the exact joint-probability ratio at every admissible count/run cell. It separately compares the explicit sharp limiting coefficient with numerically stabilized conditional finite probabilities for five parameter sets at \(n=4000\), including two exact equality cases. The last observed checker message is `PASS 281 independent finite/limit checks`.

The numerical comparisons test selected values only and do not constitute a proof of the local limit, equality classification, or universal limit. Those follow from the endpoint composition count, strict log-concavity, saddle-point concentration, and exact affine total-variation identity recorded in `RESULT.md`. The 2004 prior source could not be inspected in full; originality review is same-model and independent validation has not been performed.

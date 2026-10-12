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
# Reproducibility and mathematical limits

Run `python verify.py` using Python 3 and `numpy` as listed in `requirements.txt`. The script builds two-stage amplitude-damped density matrices from explicit local Kraus operators, applies intermediate and restoring NOT permutations, and computes the exact X-state concurrence from complementary diagonal pairs. It compares with the independent closed expression for all \(2\le n\le6\), every proper nonempty intermediate NOT mask size, five first-stage damping values, and four second-stage survival values. It further checks strict monotonic samples and the known zero-first-stage limit. Expected successful standard output is `VERIFY_OK 390`.

Proof obligations not discharged by a finite script are discharged algebraically in `RESULT.md`: the complement-pair count, the X-state concurrence identity (cited source), strict monotonicity and endpoint classification, unique critical incoming damping probability, and fixed-mask-size large-\(n\) asymptotic. The code does not certify novelty, independence, infinite-size verification, physical gate fidelity, or noise robustness.

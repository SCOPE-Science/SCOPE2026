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

Reproduce with `python3 artifacts/verify_general.py` using Python 3 standard library. The script does a fresh inverse-subset breadth-first search for every proper nonempty subset for all `2 <= n <= 10`, `1 <= d < n`; it independently computes directed-edge component products and count histograms for coprime displacements. It checks non-extensibility for noncoprime, cardinality-wise unique longest sets, and the displacement-one closed form. The captured output is in `artifacts/verification_output.txt`. Tests are finite and are not the proof of the infinite theorem. No independent validation has been conducted.

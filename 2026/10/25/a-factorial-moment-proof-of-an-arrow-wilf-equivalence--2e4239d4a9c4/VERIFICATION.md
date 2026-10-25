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

The standalone `verify.py` script independently computes both avoidance classes using the explicit Foata transformation and tests direct arrow containment through permutation length seven, with the decreasing-subsequence test through length eight. It also validates the two unrelated cycle-decomposition counts and their common formal generating series through order eighteen. The output file `verify_output.txt` records the actual local run. Execute `python3 verify.py` with Python 3 and the standard library.

The finite enumeration checks are not offered as proof for unbounded permutation size. The unrestricted claim is supported by the cycle-reconstruction and formal factorial-moment proof in `RESULT.md`. Separate primary full text of Zhou and Yu (arXiv:2609.29392) remained inaccessible; priority against unknown literature is not independently certified.

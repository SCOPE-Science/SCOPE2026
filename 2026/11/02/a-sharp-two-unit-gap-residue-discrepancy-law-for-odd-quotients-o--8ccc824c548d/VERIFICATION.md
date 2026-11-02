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

# Reproducibility and limits

The proof in `RESULT.md` is symbolic and covers all odd integers \(p\ge3\) and positive integers \(t\ge1\). Run `python3 verify.py` after extracting the package to independently enumerate all quotient gaps and compare against the exact formula in 1326 finite cases. The checker is exhaustive over its stated finite parameter window only. The calculation does not establish novelty or independently validate the proof.

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

Run `python3 verify_abelian_spectrum.py` with Python 3 and standard library. The script independently enumerates literal contiguous factors, computes their length-wise Parikh-vector counts, and compares the theorem for 3025 parameter cases (77656 tested lengths) with 3–6 distinct letters. The proof uses the circular consecutive-repetition lemma; the program is not a proof for unlimited parameters.

No independent audit has been performed.

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

Execute `python3 verify.py` using the accompanying standalone source. It checks absence of reversibly paired permitted difference triples for moduli 3 through 63, realizability by the displayed binary indices of every ordered pair for moduli 3 through 34, and explicit observed factor/reversal counts for moduli 3 through 8 and lengths 1 through 12 within the first 32768 symbols. The exact mathematical proof covers all integer moduli at least 3 and all lengths; the experiments are checks of its steps only.

No independent or external validation has been performed. Reproducibility requires only Python 3 (standard library).

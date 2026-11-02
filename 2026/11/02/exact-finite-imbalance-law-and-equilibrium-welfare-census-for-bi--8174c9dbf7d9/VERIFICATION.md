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

Execute `python3 verification.py` with Python 3.9 or newer; the test uses standard-library `itertools`, `collections`, and `math` only. It generates all 74,305 type assignments for cycles of size three through sixteen, checking predicted equilibrium welfare multiplicities against direct enumeration. For cycles through fifteen, it independently checks actual bilateral strict-improvement conditions for 35,103 colorings, evaluating every potentially improving opposite-type pair. Every tested stable coloring meets the exact minimum, maximum and total-count formulas.

The proof in `RESULT.md` is necessary for the universal claims: finite enumeration does not constitute an all-size proof. Computed inputs and assertions are tied to this exact package, and no external programs, data files or unrecorded numerical tolerances are required.

No independent audit or independent scientific validation has been performed.

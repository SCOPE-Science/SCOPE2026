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

# Reproducibility and verification

Run `python3 verify.py` with a standard Python 3 interpreter; no third-party packages are required. Expected exhaustive complete rank vectors, ordered by rank zero through four, are `q=2: [1,21,154,336,0]`, `q=3: [1,26,234,1116,810]`, and `q=5: [1,124,3100,27400,47500]`. The script derives the linear constraints for all endomorphisms from the multiplication table, rather than assuming the proposed derivation dimension, and checks the Leibniz identity for each enumerated derivation. It also uses binary and extension-field elimination to enumerate all symmetric matrices over \(\mathbb F_2\) in dimension four and \(\mathbb F_4\) in dimension three. Expected outputs for these last two cases respectively include rank vectors `[1,45,770,5040,10528]` and `[1,315,19908,241920]`.

Tests enumerate small finite fields and do not establish the infinite theorem; the proof in `RESULT.md` supplies the all-field normal form and the all-even-field counting argument. Rank conventions distinguish the full derivation from its top-left matrix. No independent external validation or publication-priority certification has been performed.

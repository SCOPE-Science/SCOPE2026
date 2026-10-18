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

The mathematical proof converts the two defining good-involution identities to a displacement map \(\delta:A/2A\to A[2]\), uses the exact involutivity condition to obtain weighted singleton/pair decompositions, and counts all such maps by the kernel and image of \(A[2]\to A/2A\). The text treats arbitrary finite abelian groups, including the trivial group.

Run `python check.py` in Python 3. It checks every permutation directly for the eleven displayed small groups and compares the observed fixed-point distribution with an independently evaluated coefficient formula. The expected final line is `CHECKER_OK`. Finite checks cannot prove the all-group theorem or literature originality; the general proof and source comparisons are given separately. Independent audit is not performed.

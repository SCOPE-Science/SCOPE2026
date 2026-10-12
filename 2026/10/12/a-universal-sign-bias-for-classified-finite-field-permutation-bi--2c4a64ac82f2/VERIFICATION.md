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

## Reproducible checks

Run `python3 VERIFY.py` in the directory containing this file; Python standard library only. The script constructs each small extension field directly, evaluates every eligible polynomial at every field element, checks the resulting permutation cycles and sign, and compares every norm/quadratic-character prediction. It then checks the closed even/odd coefficient counts.

The actual execution output is embedded separately as `VERIFY_OUT.txt`. Exactly 14 admissible parameter cases and 609 permutations passed. The universal theorem is proved algebraically in `RESULT.md`; 609 finite cases do not prove it. The two closely relevant full arXiv preprints were not obtained from the attempted lawful sources, so an independently stated equivalent parity theorem inside one remains a material originality uncertainty.

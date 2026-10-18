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

The symbolic proof gives a countably supported limiting law and a strict error below \(4/P_N\) at every level \(N\ge3\). The standalone script `verify.py` uses integer arithmetic for the labelled recurrence and exact `fractions.Fraction` values. Run `python3 verify.py` in the extracted directory. It cross-checks 2,500 individual greedy transitions by direct coprimality search, 64 labelled block recurrence entries against actual record enumeration through level 7, and the level-12 exact numerators obtained without high-primorial enumeration. Checks passed on execution. The script cannot prove the asymptotic; the proof is in RESULT.md.

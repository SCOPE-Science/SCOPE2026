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

Run `python3 checker.py` from the directory containing this note. The script enumerates compatibility graphs and set partitions directly for \(1\le n\le 6\); it separately checks the forcing implication against all binary modal relations and distinguishes equivalence-modal cases for \(1\le n\le3\). The expected exact count pairs \((A_n,B_n)\) are \((2,1)\), \((20,3)\), \((736,15)\), \((95584,121)\), \((46101248,1665)\), and \((87161615360,43883)\). The output ends with `QUANTUM_MODAL_PAIR_ENUMERATION_OK` when all tests pass.

No infinite mathematical conclusion is drawn from finite enumeration. In particular the asymptotic conclusions depend on the spanning-forest and partition-weight inequalities in RESULT.md. Independent external auditing has not been performed.

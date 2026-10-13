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
# Verification record

Run `python3 checks/verify_sunlet.py` from the package root using Python 3 and its standard library. The program has two separate finite tests: all \(3^n\) core assignments with direct feasible-leaf minimization for \(3\le n\le12\), and all \(3^{2n}\) full core-and-leaf assignments for \(3\le n\le6\). The recorded standard output in `checks/verification_output.txt` ends with `ALL CHECKS PASSED`.

For \(n=3,4,5,6,7,8,9,10,11,12\), the checked minimum-weight counts are \(6,32,20,12,140,64,24,480,176,48\), respectively. Each agrees with the analytical formula. The independent complete-label loop does not rely on the structural gap theorem; the core-only loop derives best leaf labels directly from adjacency requirements. Enumeration checks only these finite orders. The proof in `RESULT.md` establishes the result for all integer \(n\ge3\).

A scientific literature comparison was made against the scalar corona-product theorems and the recent Italian-domination counting paper; all independently performed audits remain unperformed.

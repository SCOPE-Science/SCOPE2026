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

# Reproducible finite checks

Run `python3 verify.py` with Python 3.10 or newer (standard library only). It directly builds each triangular graph from intersecting root edges, enumerates every nonempty vertex subset for \(2\le n\le7\), checks that each outside vertex has other than exactly one selected neighbor, and computes inclusion-minimality by exhaustive submask containment. Two independently formulated enumerators—degree constraints for all forts and rooted-star recursion plus cycles for minimal forts—agree coefficientwise with the direct enumeration.

The verified total fort counts for \(n=2,3,4,5,6,7\) are respectively \(1,4,45,828,29137,1977458\), and their minimum-fort counts are \(1,3,3,40,35,35\). The program prints `VERIFY_OK` after all checks.

The test covers only orders through seven; the stated theorem for arbitrary \(n\) follows from the analytic combinatorial proof. No independent mathematical audit or external certification has been performed.

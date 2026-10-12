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

# Verification of the rank-index formula

Run `python checker.py` with Python 3.9 or later. It requires only the standard library and prints `VERIFY_OK` if all assertions pass. It directly enumerates the defining distance-preserving partial maps for cycle sizes \(3\le n\le6\), without using the dihedral restriction theorem in that independent cross-check. It then enumerates every distinct dihedral restriction for \(3\le n\le10\), computes each power up to index \(n\), and compares complete rank polynomials with the transfer formula. A separate binary cyclic-word enumeration checks the transfer trace for orbit lengths \(1\le t\le10\) and all bounds \(1\le h\le11\).

The observed counts of all nilpotent elements at cycle sizes \(4,5,6,7,8,9,10\) are respectively \(41,141,307,897,1889,4393,9651\). The top-rank and maximal-index counts agree with \(n\varphi(n)\) throughout this tested range. The actual general proof relies on the permutation-restriction and cyclic-run arguments in `RESULT.md`; enumeration is a finite check only. Machine execution and self-review do not constitute independent certification.

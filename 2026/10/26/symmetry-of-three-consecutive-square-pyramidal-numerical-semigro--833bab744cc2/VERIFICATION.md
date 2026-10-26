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
Run `python3 verify.py` with Python 3's standard library. The verifier directly computes Apéry sets by shortest paths for every \(1\le n\le40\), derives Frobenius numbers and genera from those sets, and compares symmetry independently with the stated residue classification. It additionally checks three pair gcds, the exact cubic recurrence and gluing membership for \(3\le n\le10000\), and checks the Frobenius polynomial in all tested symmetric cases. The expected output is `VERIFY_OK: 40 independent Apery/Frobenius/genus cases, 9998 exact gcd/recurrence/gluing cases, all three gluing orientations.`

A finite test cannot certify the infinite result, and no claimed failure search is interpreted as impossibility. The universally quantified argument appears in `RESULT.md`. The references supply the classical complete-intersection criterion, which is not independently reproved. Independent validation: not performed.

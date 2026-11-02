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

# Reproducibility and proof boundaries

Run `python3 verify_trinomial_mod9.py` with the Python standard library; no network access or third-party packages are needed. The script constructs \(T_0=1\), \(T_1=1\), and then applies the exact recurrence \((n+1)T_{n+1}=(2n+1)T_n+3nT_{n-1}\). It checks every \(0\le n<6561\) against the stated base-three classifier, tests the three mod-\(9\) recurrences for \(2185\) positive indices, and compares counts for each \(2\le k\le8\). Recorded output: `VERIFY_OK terms=6561 zeros=5665 recurrences=2185 closed_counts=2..8 first_zeros=[8, 15, 16, 17, 20, 23, 24, 25, 26, 35, 42, 43, 44, 45, 46]`.

These computations do not prove an unbounded digit criterion. That follows from the explicit Laurent polynomial expansion, the zero/one/two digit appending recurrences, and the induction in RESULT.md. Bibliographic comparisons have not undergone independent validation.

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

# Verification

`python3 checker.py` uses only standard Python. For each case, it independently enumerates all allowed strict off-diagonal matrix entries, multiplies to test \(N^2=0\), computes \(\operatorname{rank}N\) by finite-field Gaussian elimination, and compares the entire histogram with the Gaussian-coefficient expression.

Complete exhaustive cases and computed rank multiplicities:

- \((a,b,c,q)=(1,1,1,2)\): \((1,5)\).
- \((1,2,1,2)\): \((1,13,6)\).
- \((2,1,2,2)\): \((1,33,78)\).
- \((2,2,1,2)\): \((1,33,78)\).
- \((2,2,2,2)\): \((1,81,630,216)\).
- \((1,1,1,3)\): \((1,14)\).
- \((1,2,1,3)\): \((1,50,48)\).
- \((1,1,1,4)\): \((1,27)\).
- \((1,2,1,4)\): \((1,123,180)\).
- \((2,2,1,4)\): \((1,555,7380)\).

The tests over \(\mathbb F_3\) verify the general square-zero matrix count only. They do **not** claim that \(1+N\) is involutive in odd characteristic. The tests over \(\mathbb F_4\) use explicit arithmetic in \(\mathbb F_2[X]/(X^2+X+1)\). `VERIFY_OK` is emitted only if every rank count matches. The infinite family is established by a surjective linear-map fiber argument; exhaustive small-field cases cannot prove the universal quantifiers. No independent audit has been performed.

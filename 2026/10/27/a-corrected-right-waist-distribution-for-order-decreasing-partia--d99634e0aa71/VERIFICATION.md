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

# Computational verification

Run `python3 verify.py` in a directory containing the standalone script. It uses only the Python standard library.

The script implements (i) direct enumeration of each partial injection on labeled chains of size one through seven, checking every order-decrease inequality and computing the actual maximum image; (ii) a separate subset-mask dynamic program which adds each possible domain input once and records exact occupied image positions for sizes up to sixteen; and (iii) the closed Stirling/falling-factorial formula. All three methods agree wherever their ranges overlap.

The direct enumeration returns the waist-count vector \((1,5,20,51,74,52)\) at size five. The conjectured vector from \(\binom nk B_k\) is \((1,5,20,50,75,52)\). The script additionally checks the Bell-total identity \(\sum_{k=0}^n F(n,k)=B_{n+1}\) and the exact degree-three discrepancy \(F(n,3)-5\binom n3=\binom{n-2}{3}\) through size 100.

Successful output ends with `VERIFY_OK_UMAR_RIGHT_WAIST_CORRECTION`. The all-size proof is combinatorial and is contained in `RESULT.md`; finite experiments do not establish infinity. No independent mathematical audit was performed.

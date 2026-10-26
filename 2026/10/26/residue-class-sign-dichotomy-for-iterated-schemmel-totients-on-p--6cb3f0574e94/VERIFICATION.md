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

# Verification and reproducibility

`verify.py` requires only Python 3 and its standard library. Executing `python3 verify.py` from the extracted package checked the multiplicative Schemmel function by direct integer factorization and computed the iterated sum by following the defining orbit until zero or one. The output was:

`VERIFY_OK: local threshold and prime-power signs: 987 checks; global m=4: 378 prime powers; density factors: [(2, 1, 1), (4, 1, 2), (6, 3, 4), (8, 15, 48), (10, 5, 12), (12, 135, 240)]`

The program also checks every small positive value of \(L_m(t)\) in its finite test intervals against the explicit bound \(B_m\), verifies sign implications at several prime powers, tests all prime-power cases for \(m=4\) with primes up to \(701\) and exponents \(1\) through \(3\), confirms the values at \(11,29,59\), and counts the allowed reduced residues exactly for six even moduli.

The mathematical proof is independent of the finite ranges of these calculations. The unbounded sign classification follows from the finite prime-factor obstruction, and the asymptotic counting requires the standard prime number theorem in arithmetic progressions, neither of which is certified by finite enumeration. Independent mathematical validation has not been performed.

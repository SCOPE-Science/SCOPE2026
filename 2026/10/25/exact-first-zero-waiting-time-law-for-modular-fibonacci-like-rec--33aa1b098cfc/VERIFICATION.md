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

Run `python3 verify.py` with the Python standard library. The script exhaustively iterates the recurrence for every ordered starting pair modulo each modulus \(1\) through \(90\), independently determines non-hitting states by repeated state detection, computes every divisor rank and Euler totient, and compares the entire histogram and each gcd stratum with the claimed law.

Actual replay output:

`VERIFY_OK: 90 moduli (1..90); 247065 independently iterated initial pairs; 5741 exact gcd-stratum/time cells; 16 published OEIS total counts`

The code also checks the exact first-hit waiting-time sum and the established OEIS A232656 totals for moduli \(1\) through \(16\). The universal theorem does not rely on these finite experiments. No independent external audit has been performed.

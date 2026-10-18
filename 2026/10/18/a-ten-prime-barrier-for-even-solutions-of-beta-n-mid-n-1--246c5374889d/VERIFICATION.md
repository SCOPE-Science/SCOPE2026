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

## Reproducibility
Run `python3 verify.py` with Python 3 (standard library only). The expected output terminates with `VERIFY_OK` and includes `CERTIFICATES_OK`, `EVEN_CENSUS_OK`, and `STRUCTURAL_SAMPLES_OK`.

The executable recalculates the exact rational products \(1062347/2654208\) and \(30808063/59719680\), verifies they exceed \(2/5\) and \(1/2\) respectively, checks the product thresholds across the next odd prime, evaluates every even \(n\le500000\), and tests \(120\) structured large integers. For \(n\le150\), it also compares prime-power factorization with the independent count of integers whose greatest common divisor with \(n\) is a perfect square.

All arithmetic is exact; no external data are necessary. These finite checks are supporting evidence. The complete proof for arbitrary sizes is in RESULT.md. No independent audit has been performed.

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

# Reproducibility

The standalone `verify.py` uses only Python 3 standard-library arithmetic. It computes \(eta(n)\) by the prime-power formula for every \(n\le10^6+1\), checks \(\Omega(n+1)\) for the complete even residue class \(n\equiv2\pmod4\), verifies the sole hit \(194\), and checks the exact small-prime totient inequalities used in `RESULT.md`.

The proof is unconditional for every integer satisfying the theorem, including integers above the tested range. The finite test does not establish the result by extrapolation. Independent audit has not been performed.

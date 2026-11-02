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

# Reproducibility and verification

From the extracted directory containing `verify.py`, execute `python3 verify.py` using Python 3 and only its standard library. The verifier computes exact finite-chain distributions on two-vertex and triangle graphs, checks the bound with rational arithmetic at several fixed lengths and lags, checks the complete-refresh equality, and independently enumerates 2,048 artificial genealogical configurations for the exact conditional Walsh variance formula. Recorded outcome: `PASS: 2084 exact checks (Walsh identities and finite voter distributions)`.

These exhaustive **bounded** tests neither establish the result on all graphs nor prove a central limit theorem. For that, inspect the source-sign representation, orthogonal degree-two character formula, distinct time-pair double-refresh witness, and conditional total-variance argument in `RESULT.md`. The CLT additionally invokes Lemma 2.3 and Theorem 2.7(1) in Benjamini, Helman Tov and Zhukovskii, DOI 10.1214/23-AOP1637, under the verified variance growth hypothesis. The underlying references and their limitations are explicitly stated in `RESULT.md`.

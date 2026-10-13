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

## Reproduction

Execute `python3 verify.py` in the directory containing this document and the standalone verifier. Python 3 standard library only; no external packages or downloads are needed. A successful run prints `PASS 2137 exact-rational checks; no proof of continuous parameters by enumeration`.

## Checks executed

The verifier constructs exact-rational block Gram matrices and explicitly evaluates each column's one-pivot Schur residual. It checks the two-block expected-risk formula over a finite grid of block sizes, diagonal ratios, and integer exponents. It also evaluates independent seeded integer Gram matrices, checking the comparison bound using exact integer powers rather than floating-point inequalities. It confirms the \(17\)-dimensional witness \(\mathcal E_1=32/5\), \(\mathcal E_2=10\), and ratio \(25/16\), and that a strictly positive-definite perturbation approximates the witness risk.

## Limitations

No finite checker establishes the real-exponent universal theorem, asymptotic limit, or optimality of the two-block extremum. Those depend on the written Hölder, residual, calculus, and limiting arguments. Independent scientific audit and independent validation have not been performed.

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

Run `python3 verify.py` with Python 3.9 or later. No packages or external data are needed.

The script independently evaluates the defining integer sums for Apéry and Almkvist–Zudilin numbers and separately evaluates Chan–Zudilin's second integer binomial expansion. Equality of the two latter exact integer sums is checked for every \(0\leq n\leq256\), followed by the claimed mod-sixteen congruence and bit-block expression. The derived binary-carry identity is checked for \(0\leq n<100000\), and explicit separated-block witnesses are checked for proposed periods \(1\leq d\leq512\). All computation is exact integer arithmetic. On success it prints `VERIFY_OK` and those three test counts.

Finite tests do not prove the statements for arbitrarily large indices or establish originality. The infinite proof uses the previously established alternative binomial identity, Legendre's valuation formula, Lucas's theorem and a finite Boolean identity. The normalization matters: the signed sequence defined in the result is the convention with initial values \(1,-3,9,-3,\ldots\); the other convention differs by \((-1)^n\). No independently performed audit is asserted.

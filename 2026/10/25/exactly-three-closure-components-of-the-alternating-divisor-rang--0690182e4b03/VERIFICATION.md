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
Run `python3 verify.py` using Python 3's standard library. The program checks all seven exact finite-prime tail inequalities, exact formulas for the Euler-product coefficients, strict overlaps and separations between the local prime-factor bands using rigorous rational enclosures for \(\pi\), and a direct sample over positive squarefull integers at most \(50000\). The expected successful final output begins with `VERIFY_OK`.

The mathematical proof also uses the classical Nagura theorem: for any real \(x\ge25\), there is a prime strictly between \(x\) and \(6x/5\). This theorem is a cited analytic input, not an experimental assertion. The greedy interval-filling argument for an infinite convergent sum is in RESULT.md. Numerical sampling is not an infinite proof and cannot determine whether a statement is original. Independent audit has not been conducted.

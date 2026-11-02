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

Extract `verify.py` beside this file and run `python3 verify.py` with a standard Python 3 interpreter. No third-party dependencies or external data are required.

The verifier uses the positive-composition recurrence \(B_n(r,m)=\sum_{t=1}^{\min(n,m)}B_{n-t}(r-1,m)\), an independent exact count via all subsets of the \(n-1\) cut positions, and exact integer determinants for all minors of orders one, two and three when \(1\le n\le9\). It checks the explicit even/odd three-row obstruction and compares the formulas to exact recurrence counts for each \(10\le n\le300\). The executed script reported **PASS: 15702 independent matrix comparisons, exact minor inequalities, and family-witness checks**.

The infinite sign statements are derived from \(-6(q^2-5q+2)<0\) for integer \(q\ge5\) and \(-12(q-4)(q-1)<0\) for integer \(q\ge5\), together with the enumerative proof of the matrix entries; finite replay does not replace this argument. Independent audit and independent validation have not been performed.

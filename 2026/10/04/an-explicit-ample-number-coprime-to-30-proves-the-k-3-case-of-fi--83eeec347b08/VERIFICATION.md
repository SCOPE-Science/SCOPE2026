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
Run `python3 verify.py`.

The program performs no floating-point arithmetic. It first checks that all 30 displayed bases are distinct primes exceeding \(5\) and that the exponent sum is \(280\). It then reconstructs the exact integer \(N\).

For each factorization length \(m\), the checker evaluates the exact inclusion-exclusion count
\[
K_m(N)=
\sum_{t=1}^m
(-1)^{m-t}\binom mt
\prod_i\binom{\alpha_i+t-1}{t-1}.
\]
It computes
\[
a(N)=2\sum_{m=1}^{280}K_m(N)
\]
and compares the result with the embedded decimal certificate.

As a normalization check independent of the large witness, several small exponent signatures are also evaluated directly from
\[
a(n)=1+\sum_{\substack{d\mid n\\d<n}}a(d)
\]
and compared with the ordered-factorization formula.

A successful run prints `VERIFY_OK` followed by the exact values of \(N\), \(a(N)\), and \(a(N)-N\). The computation proves only the displayed finite witness; the infinitely-many consequence additionally uses Fink's proved product closure for ample numbers.

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

# Verification of the Archimedean PQD/non-PMI counterexample

Run `python3 verify_pqd_not_pmi.py` in the directory containing this file. It uses no external library and reads no other file.

The analytic proof establishes the generator's convexity and monotone inverse, with \(\varphi''(t)\ge1/2\) and \(\varphi'(t)\le-3/4\) for \(0<t\le1\). Its global PQD proof is the exact identity \(f(uv)-f(u)-f(v)=\int_u^1\int_v^1(st-1/2)^2\,dt\,ds\). These facts are not inferred from numerical sampling.

The certificate checks exact rational brackets for the implicit copula equation using the first eight terms of the nonnegative arctanh series, plus an explicit rational remainder bound. Its three root brackets are denominated by \(10^{11}\), with numerators \((6433697255,6433697257)\), \((18897106192,18897106193)\), and \((56538957970,56538957971)\). Both \(\ell=-\varphi'\) and \(k=\varphi''\) are positive and strictly decreasing, giving outward density intervals. All comparisons required to conclude
\[
-\frac{19002196}{10^9}<c(1/4,1/4)-2c(1/4,3/4)+c(3/4,3/4)<-\frac{19002192}{10^9}
\]
are exact rational assertions. The code also checks the symbolic first-variation coefficient \(-11/576\). Printed decimal values are not used as proof data.

Limits: the certificate certifies one pointwise density-reflection violation. The mathematical integral argument separately establishes PQD throughout the unit square. No higher-dimensional copula property, converse implication, empirical inference, or exhaustive literature priority result is certified here.

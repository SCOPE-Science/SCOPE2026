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

The proof was checked directly against equations (4.2) and (4.4) of arXiv:1704.01933v1 for tree order \(k=2\).

At \(b=1\), exact algebra gives \(x_1=\widetilde a\), \(x_2x_3=\widetilde a^2\), and the reversible scalar factorization
\[
(m-1)\bigl(m^2+(1-a)m+1\bigr)=0.
\]
The quadratic discriminant is \((a-3)(a+1)\), and its two non-diagonal roots multiply to one. This proves the full parameter classification without sampling.

The accompanying symbolic script replays these identities and substitutes the exact counterexample \(a=7/2\), \(m=2\), \(t=1/2\) into the source equations. Its output is a consistency check, not an independent proof and not an independent audit.

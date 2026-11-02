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

# Reproduction and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses exact `fractions.Fraction` arithmetic and no external packages. Its recorded run was:

```
PASS 2563 exact rational identities, direct-enumeration, curvature, and minors
```

It checks direct two-stage subset/permutation enumeration and the factorial-mixture law for sizes \(2\le n\le6\), the generalized Laguerre polynomial coefficient identity, second-log-derivative signs for sizes \(2\le n\le10\), and strictly positive ordered minors through order four for sizes \(2\le n\le7\) at rational parameter grids. Check failures raise assertions with diagnostic parameters.

The finite checks are not certificates for all sizes or continuum parameter ranges. Those conclusions rely on the self-contained proof in `RESULT.md`: exact conditional distribution, total nonnegativity and a positive Cauchy–Binet summand, and Laguerre orthogonality/positive-root factorization. Positive simple roots are proven analytically; numerical root finding is unnecessary. Independent audit is not performed.

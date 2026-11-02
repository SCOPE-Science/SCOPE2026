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

# Verification and reproducibility

The proof is fully contained in `RESULT.md`. Its essential algebraic identity is
\[
A-\frac{(Au)(Au)^{\mathsf T}}{u^{\mathsf T}Au}=
\frac{\det(A)}{u^{\mathsf T}Au}(Ju)(Ju)^{\mathsf T},
\]
for positive-definite real \(2\times2\) matrices, followed by conditional Rademacher variance and exact Gaussian angular integration. The sign criterion follows from a polynomial factorization and strictly negative derivative of \(Q\). No finite collection of tests is treated as an infinite proof.

The accompanying `verify.py` script was actually executed with SymPy and returned:

```text
VERIFY_OK: symbolic identities=16, angular quadratures=28, critical_sqrt_ratio=1.752931245525, critical_ratio=3.072767951539, example_N=29/9_H=9/2
```

It checks the residual identity entry by entry for a general symbolic symmetric matrix, exact fourth-order ratio moment expressions, variance and comparison identities, exact examples including isotropy, an explicit rational factorization of \(Q'\), 28 independent Simpson quadratures of the angular variance, and the critical anisotropy root. Run `python verify.py` after installing `requirements.txt`.

Scientific boundaries: exact arithmetic, independent sketch and probes, rank-one Gaussian Nyström sketch, Rademacher correction and Hutchinson comparison; a separate perturbative existence argument extends strict reversals to higher dimensions. The computation does not verify an unpublished-priority claim, mathematical independence or certification. Independent audit: not performed.

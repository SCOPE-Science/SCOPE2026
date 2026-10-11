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
# Verification

The proof is analytic.

For a centered regular simplex of positive even dimension \(k\), the exact block formula gives defect
\[
\frac{4t(t+1)}{k}
\]
with multiplicity
\[
2\binom{k+1}{k/2-t},
\qquad
0\le t\le k/2.
\]
Orthogonality makes global defects additive, yielding the stated convolution factorization.

The smallest positive defect in a block is \(8/k\). Therefore the global smallest positive defect is \(8/K\), where \(K\) is the largest simplex dimension. If \(q\) blocks have that dimension, the multiplicity ratio between the first positive defect and defect zero is
\[
q\,
\frac{\binom{K+1}{K/2-1}}{\binom{K+1}{K/2}}
=
\frac{qK}{K+4}.
\]

Once \(K\) and \(q\) are recovered, the Laplace transform of the defect measure can be divided by the strictly positive real factor associated with \(q\) copies of \(\nu_K\). The quotient is the residual finite-measure transform. Uniqueness of finite measures from their Laplace transforms permits induction.

The packaged checker enumerates every admissible sharp block decomposition through ambient dimension \(16\), forms all defect measures exactly with rational arithmetic, verifies the first-defect formulas, and confirms no spectrum collisions for fixed \((n,d)\). This finite enumeration is only a stress test and is not used to infer the general theorem.

Unproved limits: no quantitative reconstruction under perturbed spectral data; no extension to nonsharp configurations; no determination of the unresolved optimal constants beyond the sharp equality regime.

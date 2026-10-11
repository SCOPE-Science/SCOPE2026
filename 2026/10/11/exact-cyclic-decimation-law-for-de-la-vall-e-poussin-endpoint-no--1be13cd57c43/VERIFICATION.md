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
The analytic chain checked in the proof is:

1. \(V_n(t)=\sin(nt/2)\sin(3nt/2)/(n\sin^2(t/2))\).
2. On each sample coset \(t_s+2\pi q/n\), the numerator product is invariant in \(q\).
3. Differentiation of the cotangent multiplication identity gives
\[
\sum_{q=0}^{n-1}\csc^2\!\left(x+\frac{\pi q}{n}\right)=n^2\csc^2(nx).
\]
4. Each coset therefore contributes \(n|1+2\cos(2\pi s/m)|\), including \(s=0\) by continuity.
5. Absolute row and column sums give the exact endpoint convolution norms.
6. The three formulas for \(A_m\) follow from the negative-index interval \(m/3<s<2m/3\) and a finite cosine sum.

The included `artifacts/verify.py` was executed from its package path. It returned:

`VERIFY_OK cases=4680 decimation_maxerr=4.086e-14 closed_maxerr=4.441e-16 csc_relerr=1.990e-15`

The numerical checks cover \(1\le n\le40\) and \(4\le m\le120\). They are regression tests only; they do not replace the exact proof or assert anything for arbitrary grid ratios or interior \(\ell^p\) norms.

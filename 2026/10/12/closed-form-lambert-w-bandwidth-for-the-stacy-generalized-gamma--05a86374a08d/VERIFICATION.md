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

For \(d>1\), direct differentiation gives the unique mode \(m=a((d-1)/p)^{1/p}\). With \(r=(x/m)^p\) and \(c=(d-1)/p\), cancellation of the density normalization yields
\[
\frac{f(x)}{f(m)}=\exp\!\left(c(\log r-r+1)\right).
\]
Therefore a \(y\)-level point satisfies
\[
r e^{-r}=e^{-1}y^{p/(d-1)}.
\]
For \(0<y<1\), the Lambert-W argument lies in \((-1/e,0)\). The principal branch gives \(0<r<1\), while the \(-1\) branch gives \(r>1\). This proves that the displayed expressions are exactly the two positive crossings and that their difference is the full width.

The ordinary-gamma check is exact: setting \(p=1\) gives mode \((d-1)a\), Lambert-W argument \(-e^{-1}y^{1/(d-1)}\), and the published gamma formula after identifying \(d\) with gamma shape and \(a\) with gamma scale.

The packaged `verify_formula.py` checks four parameter choices by direct density evaluation and asserts that both branch formulas return the requested level. The script is a finite numerical sanity check only; it is not used to establish the general theorem.

The proof does not cover \(d\le1\), shifted or reflected extensions, quantile widths, or numerical error bounds near the branch point.

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

The proof reduces exact Hausdorff distance to nearest integer composition of \(k\) in \(d=n+1\) coordinates. For \(q=kp\) and fractional vector \(f\) with integer sum \(r\), the nearest grid point rounds up precisely \(r\) coordinates after taking floors. The hypersimplex identity then gives
\[
\min_{|S|=r}\|f-\mathbf1_S\|_2^2\le r-\sum_i f_i^2\le\frac{r(d-r)}d.
\]
Equality requires and is achieved by \(f_i=r/d\) for all coordinates. Every feasible integer \(r\) is realized by a nonnegative composition of \(k-r\), yielding the complete profile and deep-hole list. The small-\(k\) uniqueness and high-\(k\) saturation statements follow from the discrete concavity of \(r(d-r)\).

The accompanying standalone Python checker enumerates integer composition grids for every \(2\le d\le8\) and \(1\le k\le6\). It checks every predicted equality site, their distinctness and count, and independent random interior points against the exact bound. No computational enumeration is used to establish the infinitely many \((n,k)\) cases.

Known literature supplies the full-space \(A_n\) root-lattice covering radius only; the finite-grid assertion is proved without appealing to an unproved lattice statement.

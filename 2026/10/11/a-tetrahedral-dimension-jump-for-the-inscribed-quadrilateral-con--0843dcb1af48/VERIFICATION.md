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
For a centered scalar four-tuple, direct expansion verifies
\[
\sum_{i<j}(a_i-a_j)^4=4\sum_i a_i^4+3\left(\sum_i a_i^2\right)^2.
\]
After summing by coordinates and applying Cauchy--Schwarz to the six coordinate-product sums, one obtains
\[
\sum_{i<j}\|x_i-x_j\|_4^4\le64.
\]
A second Cauchy--Schwarz inequality over the six pairwise squared distances gives the upper bound \(8\sqrt6\).

For the sharp tetrahedral configuration, every vector has unit \(\ell_4\)-norm, the vector sum is zero, and each pair has fourth-power distance \(32/3\), so the six squared distances total \(8\sqrt6\).

`verify.py` checks the algebraic identities symbolically. The infinite-dimensional theorem is proved analytically, not by finite enumeration.

No independent audit or independent validation has been performed.

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
The verification artifact uses only exact rational arithmetic and the Python standard library.

It implements exact Gaussian elimination for rational matrices and checks the identities
\[
C_h=2R_{h/2}-I,
\qquad
R_{h/2}\mathbf 1=\mathbf 1,
\qquad
C_h\mathbf 1=\mathbf 1
\]
on several reversible generators with rational stationary weights and conductances. It verifies that all off-diagonal entries are nonnegative and that entrywise positivity is equivalent to the diagonal \(1/2\) criterion.

For two-state generators it verifies the exact threshold \(2/|a-b|\) whenever \(a\ne b\), and unconditional positivity in the balanced case. For complete graphs with \(3\le n\le20\), it verifies the exact threshold \(2/[c(n-2)]\) at multiple rational rates.

The replay does not attempt to certify the infinite family by enumeration. The universal \(M\)-matrix argument, reversible spectral representation, monotonicity, spectral enclosure, and finite-state asymptotic classification are proved symbolically in RESULT.md.

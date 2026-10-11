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

# Verification of analytic calculations

For the critical matrix, two square-sum bounds establish \(T-L\in\mathcal S_2\): below the strict upper triangle, \(\sum_{n\ge m}|T_{nm}|^2\le C/[m(\log m)^2]\); above it, the same upper bound holds for \(\sum_{2\le n<m}|T_{nm}-L_{nm}|^2\). Their total converges.

For the discretization of the integral operator, the upper-triangle matrix error has squared sum bounded by a constant multiple of \(\sum_{m\ge3}[m(\log m)^2]^{-1}\); the diagonal is square summable. For the operator-kernel discrepancy, upper-triangle block variances sum to at most \(C\sum_m h_m^3/(\log m)^3\), and diagonal contributions to at most \(C\sum_m h_m^2/(\log m)^2\), both finite. These prove the Hilbert–Schmidt identification analytically.

The unitary logarithmic change of variables sends \(A\) to the explicit half-line exponential convolution. Its norm and essential norm are exactly \(2\), with normalized long-support test vectors as witnesses. The index is obtained from \(u'+(\lambda^{-1}-1/2)u=h/\lambda\). Interior and exterior cases use opposite integration directions. Boundary oscillatory packets are weakly null singular sequences; at zero, normalized matrix columns tend to zero.

No numerical sample, finite-rank truncation, or unexamined software output is treated as an infinite-dimensional proof. No independent audit was performed. The coefficient-space normalization and the inability to infer the raw two-space Fredholm spectrum are explicit scientific limitations.

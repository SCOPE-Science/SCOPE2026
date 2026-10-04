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
The proof uses the classical boundary-format degree
\[
D=\frac{(N+1)!}{k_1!\cdots k_r!}.
\]
For each prime \(p\), Legendre's digit-sum formula gives the exact valuation
\[
\nu_p(D)
=
\nu_p(N+1)
+
\frac{\sum_j s_p(k_j)-s_p(N)}{p-1}.
\]
The second term vanishes exactly when adding the \(k_j\) in base \(p\) produces no carries.

For \(p=2\), odd degree therefore requires \(N\) even and pairwise disjoint binary supports. The support blocks form a set partition of the \(s_2(N)\) one-bits, proving the Stirling count.

The bundled exact checker enumerates unordered integer partitions through \(N=36\), computes degrees from factorials, verifies prime valuations and carry tests, and confirms the Stirling counts. Those finite computations are regression evidence only.

Limits: complex boundary-format Segre duals; total hyperdeterminant degree; unordered smaller factors for the Stirling count.

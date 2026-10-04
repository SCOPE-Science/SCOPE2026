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

The primary source was checked in its first public version, arXiv:2609.30406v1. It states that a trivialization is an integral class \(u\in H^1(P;\mathbb Z)\), that the linear and quadratic multiplicities are independent of positive factorization, and that both equal the reference length \(m\) when \(u\) trivializes that factorization.

For a competing factorization set \(x_j=u([\gamma'_j])\). The checked source premises give
\[
\sum_j x_j=\sum_j x_j^2=m.
\]
Hence
\[
\sum_j x_j(x_j-1)=0.
\]
For every integer \(x\), the term \(x(x-1)\) is nonnegative and vanishes exactly at \(0\) and \(1\). This proves the universal zero-one statement and the exact zero count.

The source also gives factorization-independent \(\operatorname{rank}V\) and
\[
b_2=m-\operatorname{rank}V,\qquad \chi=2-d+m,
\]
so subtraction proves the topological defect equalities.

The bundled script at `artifacts/verify_binary_defect.py` checks the elementary integer lemma over a broad scalar window and exhaustively checks short tuples. It returns:

`VERIFY_OK integer_window=-10000..10000 exhaustive_lengths=0..7 values=-3..3 solutions=255 zero_one_only=true`

Finite enumeration is not used as proof of the universal result.

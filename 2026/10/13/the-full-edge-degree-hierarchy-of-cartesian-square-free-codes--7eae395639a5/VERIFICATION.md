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
`artifacts/verify.py` uses only the Python standard library.

For several heterogeneous Cartesian size vectors it constructs the full exponent box, builds every degree-\((m-1)\) monomial shadow directly, and checks every subset union against
\[
P+\sum_{i\in I}\prod_{j\ne i}(n_j-1).
\]
It verifies the minimizing index sets for every \(r\).

The script also performs a direct coding check over \(\mathbb F_3\) for
\[
X=\{0,1\}\times\mathbb F_3\times\mathbb F_3.
\]
It evaluates the three degree-two square-free monomials, enumerates all subspaces of the three-dimensional message space, and computes generalized weights
\[
(6,8,12).
\]
These equal the closed formula for Cartesian sizes \((2,3,3)\).

Successful replay prints `VERIFY_OK`.

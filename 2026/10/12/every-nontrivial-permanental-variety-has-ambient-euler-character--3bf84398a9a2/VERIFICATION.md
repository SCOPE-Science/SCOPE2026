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
The checker tests every format with
\[
2\le m\le5,
\qquad
m\le n\le6,
\qquad
2\le r\le m.
\]

For each format it verifies that the row-column weights
\[
2^i+2^{m+j}
\]
are pairwise distinct.

For every selected \(r\times r\) submatrix, it explicitly expands the permanent over all permutations and verifies that every term has the same torus weight.

It then evaluates every defining permanent at every matrix coordinate point and verifies that all values are zero.

The regression grid contains \(30\) formats, \(548\) coordinate-point tests, and \(202968\) explicit permanent-term evaluations.

Finite checks are not used as an infinite proof. The all-parameter result follows from the symbolic torus-invariance and fixed-point argument in `RESULT.md`.

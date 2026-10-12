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
The checker exhaustively enumerates the coordinate fixed points of
\[
\operatorname{Gr}(N-d-1,N)
\]
for a finite parameter grid. It designates \(v\) coordinates as toric vertex coordinates and counts directly which coordinate subspaces contain at least one of them. The direct count is compared with
\[
\binom{N}{d+1}-\binom{N-v}{N-d-1}.
\]

It also generates finite lattice supports for rational normal curves, Veronese surfaces, and rectangle/product-simplex examples and checks their hull-vertex counts before applying the same fixed-point census.

The finite computations do not prove the theorem for arbitrary toric configurations. The proof is the symbolic fixed-locus argument in `RESULT.md`.

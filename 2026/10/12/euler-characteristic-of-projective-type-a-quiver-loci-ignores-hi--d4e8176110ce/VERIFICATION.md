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
The checker enumerates direct sums of interval representations for equioriented type-\(A\) quivers with at most five vertices.

For each representation it reconstructs the full admissible composite-rank array
\[
r_{ij}=\operatorname{rank}(V_i\to V_j).
\]

It then tests every arrow-coordinate representation against every rank inequality. The coordinate-point count obtained from these independent inequality tests is compared with
\[
\sum_{i:r_{i,i+1}>0}d_i d_{i+1}.
\]

It also checks directly that every composite of length at least two vanishes on each coordinate representation.

Finite checks are regression evidence only. The infinite theorem is proved by the torus fixed-point argument in `RESULT.md`.

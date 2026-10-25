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

## Checks performed
- Reconstructed the edge-opposite-vertex triangles and verified that all nonexceptional affine diameters through a point correspond one-to-one with triangle membership.
- Verified that each longest diagonal is a side of exactly two relevant triangles on the same side of its line; a generic outward ray therefore loses two memberships at each crossing.
- Verified the exact central distance to each longest-diagonal line as \(R\sin(\pi/(2n))\), and the regular-polygon circumradius conversion by \(\cos(\pi/n)\).
- Recomputed the area ratio from the square of the circumradius ratio and checked the leading asymptotic \(\pi^2/(4n^2)\).
- Checked the special case \(n=5\) against the known pentagon values. Numerical overlay checks for \(n=5,7,9\) were treated only as sanity checks, not as proof.

## Limits
The proof does not calculate the probabilities for the intermediate multiplicities. It excludes only measure-zero exceptional segments for the almost-everywhere count; it does not classify every boundary point of the triangle arrangement. No independent audit or external validation has been performed.

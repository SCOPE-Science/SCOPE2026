---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Read the complete assigned RESULT.md and exact-rational verify.py. Its three-step return matrix M=[[2,2],[-2,2]] and inverse N=(1/4)[[1,-1],[1,1]] satisfy N^8=4096^-1 I; the strict prescribed quadrant conditions reduce to four halfspaces D_b centered at the known orbit r_b, and S_n=intersection_{j=0}^{n-1}N^j D_b. Since D_b is convex and contains zero, the eight residue classes of scaled copies are nested; n>=8 makes the last copy of each class controlling, proving the infinite-index homothety. The three finite b regimes use explicit polygons D_b, P_b, (2-b)Q, with affine-in-b endpoint support constraints and N-invariance. The actual checker certifies the edge-support and feasibility tests in exact rational arithmetic at interval endpoints, which analytically extends to every b in the closed regime; shoelace areas give the three C(b). Independent rational clipping checks at multiple b and n corroborated areas and the periodic homothety. The claim is CONDITIONAL survivor area only, not full basin/escape measure.

## originality

PASS

Bounded best-of-knowledge originality: the exact stated invariant and quantified result were compared by implication to the closest primary and published SCOPE sources; no decisive covering result found. Unread material and alternative nomenclature remain explicit, and source search is not proof of absolute novelty.

## value

PASS

The exact decay factor alone is a determinant exercise, but the sharp finite stabilization and previously uncomputed b-dependent area constants at b=3/2 and 7/4 are nontrivial bifurcations of a natural repelling itinerary cylinder. These quantify finite-time survival geometry of the same dynamically motivated planar family; they are not a discretionary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

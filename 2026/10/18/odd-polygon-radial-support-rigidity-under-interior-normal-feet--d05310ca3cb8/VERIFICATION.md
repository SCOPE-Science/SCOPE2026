---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For an internal perpendicular foot on edge i, its two positive acute radial angles are exactly arccos(h_i/d_i) and arccos(h_i/d_(i+1)), so their sum is the prescribed vertex-ray gap. Since f_h(d)=arccos(h/d) has derivative h/(d sqrt(d^2-h^2))>0, comparing two admissible solutions forces consecutive strict signs to alternate (or equality propagates around the cycle). Odd n forbids nonzero alternating comparisons. The log-radius Jacobian has only diagonal a_i=h_i/sqrt(d_i^2-h_i^2)>0 and cyclic-forward b_i>0; det J=product a_i+(-1)^(n-1)product b_i, positive for odd n. Analytic inverse-function theorem applies in the strict-foot open domain. Explicit even quadrilateral rays pi/4+k pi/2 with radii alternately sec t,csc t have all h_i=1 for t in (0,pi/2). Checked actual standard-library geometry script and independently evaluated cyclic Jacobians for odd n=3,5,7,9, plus direct nonuniform triangle and equal-support even family from the proof. Finite samples corroborate analytic argument, not prove it.

## originality

PASS

Best-of-knowledge after two real Resultary searches, public-primary reading and comparison of mathematical implications, not merely titles. The general unpublished/open formulation and tangential side-length parity do not imply the strict-foot radial comparison cycle theorem without deriving monotonic trigonometry; the latter is supplied explicitly and independently checked.

## value

PASS

The exact prescribed pair (labelled vertex radial directions, edge-support distances) is one of the unresolved input types catalogued in the contemporary convex-polygon reconstruction study. The strict-foot hypothesis is geometrically natural and removes a documented tangent-choice ambiguity; parity gives a sharp rigidity boundary, and nonsingularity gives meaningful local inverse structure. This is more than just renaming a known side-length tangential-polygon statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.

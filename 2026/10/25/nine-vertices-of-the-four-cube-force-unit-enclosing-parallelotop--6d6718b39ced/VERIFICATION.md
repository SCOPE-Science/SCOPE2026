---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For every nine-subset S of {0,1}^4, the rows B of the inverse affine map of any containing parallelotope lie in the compact width polar W_S, since each coordinate direction has a complete pair among nine corners. Multilinearity reduces |det B| to four vertices of W_S. Fresh independent JavaScript computation read actual cube9_width_polars.json and exhaustively verified all 384 signed-coordinate permutations, 11,440 nine-subsets in 56 orbits, exact feasibility of 1,066 candidate width-polar vertices, all 11,812 supporting facet quadruples against original width inequalities, full dimension, and all 290,663 4-row integer determinant tests |det|<=D^4; each orbit attained equality. Thus volume 1/|det B|>=1 for arbitrary invertible real A. Unit cube attains 1 and [0,1]^3 x [0,epsilon] has eight corners and volume tending to zero. Finite verification is exhaustive only because proof covers all 56 orbits and all polar facets, not as extrapolation.

## originality

PASS

The open majority-corners lattice-covering problem is a stronger conclusion than the present necessary volume inequality. Grozev–Nikolov prove a three-dimensional covering threshold and a higher-dimensional sufficient condition requiring a whole facet plus one opposite vertex. Nine arbitrary corners of the four-cube need not contain a whole facet, so those theorems do not imply the all-nine-subset determinant bound. The independent 56-orbit exact theorem was not found among the actually searched Resultary/published comparable outputs; this is a best-of-knowledge priority judgment.

## value

PASS

The threshold nine is the first integer beyond an eight-vertex cube facet, where any positive lower volume bound is impossible. The universal volume-one obstruction for all nine-corner subsets addresses a necessary geometric inequality toward a stated majority lattice-covering problem, while strictly distinguishing volume from the stronger covering property. Exact finite four-dimensional classification and sharp eight-versus-nine threshold are naturally motivated, not arbitrary slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.

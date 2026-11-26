---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The GQ axiom yields the point-collinearity strongly regular parameters and the incidence distance array used in the proof; no automorphism hypothesis is needed. Squared singular values of the incidence block are q+1 plus the three collinearity eigenvalues, giving the five adjacency spaces and the stated dimensions. Independent analytic replay: at ±(q+1) the distance-polynomial values are the valencies with the bipartite signs; at ±sqrt(2q) the row is (1, ±sqrt(2q), q−1, ∓sqrt(2q), −q); at 0 it is (1,0,−(q+1),0,q). Write u=1/N, w=q(q+1)/(4(q²+1)), z=q/(2(q+1)). Projector entries are the corresponding row times u, w or z divided by the distance valency. Their squared sums give c0=2u²+2w²+z², c1=2u²+4qw²/(q+1)², c2=2u²+2w²(q−1)²/[q²(q+1)²]+z²/q², c3=2u²+4qw²/[q⁴(q+1)²], c4=2u²+2w²/q⁴+z²/q⁴. Pairing these with the same eigenvalue rows gives the frozen spectrum. The negative radical branch is positive by the displayed sum of squares, the others by their factors. The positive-entry stochastic matrix has simple eigenvalue 1; the two other rational branches differ by (q+3)(q−1)/(8q(q+1)). If sqrt(2q) is irrational the radical branches cannot collide with those. Otherwise q=2r², and at common denominator 8q(q+1)(q²+1) the rational-branch differences from the radical midpoint have numerators 3 and 2 modulo 4, respectively, whereas the radical offset has numerator divisible by 4. At q=1 the spectrum is 1, 1/4 (three), and 0 (four), also following from the cycle formula. Replay is the distance-polynomial and trace proof in RESULT.md; VERIFICATION.md records the optional symbolic and finite-graph replay. The frozen verify.py was inspected, not executed. The uniform claim is only for existing balanced-order geometries.

## originality

PASS

Credit the Schur-square identity, association-scheme computations, and the thin-cycle rank to prior work. The supported distinction is the explicit thick-family profile and spectrum and the uniform positive-definiteness classification, not a new general average-mixing formula or a solution of the primitive distance-regular problem.

## value

PASS

The exact walk invariant for a natural incidence family resolves a rank question across all realizations of a fixed order without transitivity. Users can read off rank and the full spectrum rather than diagonalizing particular graphs, and can see precisely the contrast with the already known thin case. The result neither addresses primitive graphs nor asserts existence of GQs at arbitrary integer order.

The dated certificate retains the supplied scientific assessment, sources and limitations.

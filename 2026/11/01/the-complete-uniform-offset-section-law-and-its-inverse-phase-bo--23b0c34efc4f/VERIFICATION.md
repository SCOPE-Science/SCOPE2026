---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Read complete RESULT.md and verifier, source tree. Affine cube coordinates make height signs ±A±B±C; a generic level cuts exactly those of 12 edges whose end heights straddle T. Sorting four positive heights gives piecewise intervals: A>=B+C counts 3,4,5,4; A<B+C counts 3,4,5,6. Dividing lengths by W yields each claimed probability, with p3=p5+2p6 and mean four. Conversely solve for A/W=(p3+p4+p5)/2, B/W=(p3+p4)/2,C/W=p3/2 when p6>0; given invertible generator matrix, any positive normalized triple is attained by some normal. On p6=0 set rho=p3=p5 and derive C/W=rho/2, B/W in [rho/2,(1-rho)/2], A/W complementary; unique at rho=1/2, nonunique otherwise. Variance 2(p3+p6) takes 0 at C=0 and 2 at A=B=C, sharp vertices. Independently enumerated all twelve edges for 342 nonzero integer projection triples in [0,6]^3 with exact rational offset intervals and compared laws, including zero projections/ties. Universal law follows piecewise sign-order proof, not the sample.

## originality

PASS

Best-of-knowledge PASS for the joint complete fixed-normal uniform-offset law, all-realized mean-four simplex and inverse-identifiability fibers; previous mean-four theorem is explicitly credited. Plausible 1991 cube/probability source could not be fully inspected; retain specific priority risk rather than falsely describing its content or failing solely for access.

## value

PASS

The full side-count distribution is a natural stochastic geometric invariant of fixed-orientation parallelotope sections and refines a known mean theorem. Characterizing its entire feasible simplex plus a sharp inverse-identifiability phase change provides useful inverse stereological information: which unordered normal projection magnitudes can be recovered from section combinatorics. Sharp variance 0..2 and exact boundary fibers are meaningful geometry, not an arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.

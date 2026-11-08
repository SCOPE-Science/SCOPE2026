---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Surface-uniform lune sampling makes Z uniform[-1,1] and longitude uniform[-theta/2,theta/2]; first and second moment matrices yield mu=2R^2(1-h) and nu=4R^4(4/3-2h+2v^2 cos^2(x)/9), independently rederived by trace identities. Symbolic differentiation independently verified the exact kappa derivative factor H. An exact-rational independent degree-35 Bernstein test on t in [0,(11/7)^2] produced 36 coefficients, minimum 0.1092938969>0.1; the stated Taylor/Machin error bound <1e-4 proves global H>0, so kappa is strictly decreasing. The hemisphere gives 40/27, the zero-area limiting ratio is excluded. Small-x quadratic deficit and compact strict derivative yield optimal inverse 1/2-Hölder angle stability. Coupling the longitude differences yields strict chord stochastic ordering.

## originality

PASS

A natural two-parameter inverse geometric-probability problem has an exact complete feasible region and sharp stability exponent not found in inspected prior statements.

## value

PASS

The chord moments are intrinsic experimental statistics of a natural geodesically convex spherical region; determining both radius and angle with a complete range and sharp stability is an independently useful inverse result.

The dated certificate retains the supplied scientific assessment, sources and limitations.

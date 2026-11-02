---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Support h(phi)=|cos phi|+2|sin phi|+|cos phi+sin phi|, from the three actual centered segment generators. Center symmetry removes translation advantages. For fixed x=2theta, directional containment maximum reduces to h-breakpoints phi=0,pi/2,3pi/4 and reciprocal ratios by monotonicity of a quotient of sine-cosine forms between sign changes. Four interval lower bounds yield lambda(x)>=9/sqrt61. The sole minimizer x=pi/2+arctan(5/6) matches all six breakpoint constraints; support values (2,3,3sqrt2/2) and candidate evaluations (18/sqrt61,27/sqrt61,23/sqrt122) give maximum 9/sqrt61. Independent checks: Independently reconstructed all support values from generators and evaluated 100001 support angles for each test reflection x, using bounded scipy minimization; optimal x near 2.26553 and dilation 1.15233 agrees with 9/sqrt61. Read complete symbolic checker verify_chirality.py (Git blob ec3b2e6719ce77e2b47ca7b420df3989244fcbf8), which checks candidate radical identities, three breakpoint ratios, interval separation. Global lower bound rests on analytic 4-interval proof not sampling.

## originality

PASS

Caragea et al. arXiv:2504.13013v1 define alpha_1 chirality and solve triangles and parallelograms with general universal inequalities for centrally symmetric planar bodies. The hexagon is neither triangle nor parallelogram, and neither broad bound supplies its exact radical or unique minimizing line. Resultary related centrally symmetric hexagon results measure alpha_0 or translative enclosure, not alpha_1. Residual limits explicitly listed in originality.residual_risks.

## value

PASS

This concrete small-integer 3-generator zonotope represents the minimal nonparallelogram centrally symmetric polygon class. Its exact nontrivial reflection-optimization value and unique angle provide a tractable first benchmark for the comparatively new alpha_1 invariant beyond known exact triangle/parallelogram cases; an isolated computation, not a classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.

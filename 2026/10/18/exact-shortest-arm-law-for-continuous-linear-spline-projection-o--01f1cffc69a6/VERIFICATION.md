---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The hat-function Gram matrix has M00=S/3, M0j=ell_j/6, Mjj=ell_j/3, with positive Schur complement S/4 and inverse B00=4/S,B0j=-2/S,Bij=3 delta_ij/ell_i+1/S. Integrating |K(x,y)| on each arm gives center 5/3 and leaf i (7S+3ell_i)/(3(S+ell_i)); strict triangle inequality for interior points makes vertices the only maximizers. The function decreases strictly in ell_i; h<=S/m gives exact attainable range, h<S/3 gives >2, and P1=1 implies negative excursion half the signed kernel deficit. An independently written exact-Fraction Gram inverse and kernel integral recomputed four nontrivial length vectors, including the equilateral and unequal cases; finite tests corroborate the derived general proof.

## originality

PASS

Exact one-element-per-arm continuous graph-spline norm is not directly implied by the local affine simplex-projector result, nor by Oswald spline estimates on intervals/triangulations, nor Passenbrunner-Shadrin inverse Gram decay on intervals. Their different function spaces/domains do not supply the exact shortest-arm law. The plausible full 2013 Oswald spline-bound survey remained inaccessible through authorized institutional access (VPN disconnected), making hidden coverage a residual risk, not an automatic rejection.

## value

PASS

The explicit geometry-dependent Lebesgue/stability constant for the natural globally coupled graph finite element space, its sharp geometry range and positivity defect provide an intrinsic norm invariant relevant to stability and overshoot; this is more informative than a generic bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.

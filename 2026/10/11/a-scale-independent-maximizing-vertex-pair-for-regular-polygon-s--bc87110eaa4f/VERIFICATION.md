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

For regular Euclidean 2n-gon B_n and its polar B_n*, convexity in both primal arguments permits maxima at vertices. Dualizing N(x+ty)+N(x-ty) gives (1/2)max_{f,g in B_n*}[N*(f+g)+tN*(f-g)]. The polar vertices w_j=sec(beta)(cos((2j+1)beta),sin((2j+1)beta)), beta=pi/(2n), are an isometric rotated-scaled copy of primal regular vertices; dihedral symmetry reduces to angular differences 0<=j<=n. Chord norms are exactly 2 q_j cos(j beta) and 2 q_{n-j} sin(j beta) with q even=1, odd=sec beta, giving the stated finite affine envelope for all real t>=0. Since each maximizing dual vertex pair has equal Euclidean length, w_i+w_j perpendicular to w_i-w_j; choosing primal support endpoints for their perpendicular direction pair gives the same symmetric orbit (v_0,v_floor(n/2)) as an optimizer at every t, including zero-vector degenerate choices. Independently enumerated all 2n primal vertex competitors versus fixed pair and envelope for n=2..150 at 13 scales without disagreement (corroboration only). For n=5 the exact four undominated lines and their golden-ratio intersections yield rho(1)=(3sqrt5-5)/4. The mathematical proof is all n/t, not extrapolated from samples.

## originality

PASS

Best-of-knowledge PASS. Chmielinski--Khurana--Sain 2023 calculate polar vertices and norming-functional diameter for the same regular polygon, thereby controlling an infinitesimal derivative, but their inspected Section 4 does not supply the entire Day smoothness modulus as an affine envelope or the all-t common maximizing primal pair. Guirao--Ivanov--Lajara and Ivanov cover general smoothness moduli, not a verified complete regular-polygon scale profile. Resultary neighboring exact decagon curvature/James/P-angle results concern different invariant functions and do not imply this Day-modulus identity. The full all-n scale formula exceeds known derivative-only coverage.

## value

PASS

PASS. The entire classical smoothness modulus is a natural isometric invariant of these canonical finite-dimensional normed spaces, and a single scale-independent extremizing vertex pair is an unexpected rigid structural mechanism. Its explicit golden-ratio decagonal phase diagram adds concrete sharp parametric information beyond a value at t=1 or an asymptotic bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The universal proof checks analytically. Multiplying the intensity difference restricted to the unit circle by z² produces an ordinary degree-at-most-four polynomial; the five distinct roots force it to be identically zero. The Hermitian lift on (1,z,z²) then has diagonal (a,t−a,−t), H02=0 and H12=−H01=−u. Expanding gives (1−|z|²)(a+t|z|²+2 Re(uz)). Noncollinear anchors give rank three already in the constant and two linear columns; for collinear anchors, restriction to the line has three distinct zeros and hence is the zero quadratic, forcing t=0 and a unique linear equation up to real scaling. Since all anchors are off the unit circle their equations are genuinely imposed. Direct determinant expansion gives (t−a)(|u|²−at); the second factor is t² times the squared radius if t is nonzero, or |u|² for a line, so it is positive. Completing the square converts a=t precisely to orthogonality, with the line case passing through the origin. The Vandermonde spanning property rules out a nonzero semidefinite measurement-kernel matrix; therefore a singular nonzero Hermitian kernel generator has inertia (1,1,0) and yields two different rank-one intensities for non-phase-equivalent polynomials. An invertible generator precludes every such difference, including degree-deficient and zero cases. For at most seven measurements a two-dimensional real kernel exists, the cubic determinant is antipodally odd on a circle in it, and a nonzero singular matrix results; a nonspanning frame fails directly. For 0,2,2i, the verified parameters (0,1,−1+i) give determinant 2. For 0,2,3, the displayed witnesses are conjugate on the real line; on the unit circle they are conjugate after division by z, since z+z⁻¹ is real. Their common coefficient of z and different constants preclude phase equivalence. The frozen symbolic checker supports algebra only (one auxiliary example includes an anchor at 1); these analytic arguments cover the actual quantifiers.

## originality

PASS

Pass for the exact classification of all distinct off-unit anchor triples after the five reference measurements. Neither the eight-measurement lower bound nor the existence of some eight-point two-circle design is new. The full-trace theory includes a right-angle example and many uniqueness configurations; the distinct content here is the three-anchor completion in degree two and the uniform failure locus, including all other rational angles, disjoint/tangent configurations and lines.

## value

PASS

Gives a testable exact boundary for designing a minimal phaseless quadratic measurement family after a standard circular aperture. It makes degeneracy geometric, uniformly handles collinear and ordinary-circle anchors, and certifies when a design fails rather than giving only a successful arrangement. No stability or noise guarantees are inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.

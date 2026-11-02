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

The cited maximum-embedded-isosceles classification permits precisely three area ratios a/b, b and 1/(1+b^2-a^2) in longest-side-normalized host 0<a<=b<=1. For smallest host angle >=theta, law of cosines gives a^2>=1+b^2-2b cos(theta); at fixed b the a-dependent candidates strictly increase, so a is forced to the boundary a0. Feasibility gives b>=C=1/(2cos theta). The remaining objective max{b,C/b,a0/b} has one increasing term and two decreasing terms and hence a unique crossing. The first crossing b0=sqrt(C) is active exactly below u_*^4+u_*^3=1; above it the quartic b^4-b^2+2b cos theta-1=0 determines b. Endpoint theta=pi/3 is equilateral, and the theta->0 infimum 1/sqrt2 is unattained. The one-sided derivatives at theta_*=41.8316186926594 degrees are 0.36661930354211 and 0.53284165224654, a strict corner. Independent scalar minimizations of the three candidates for eight angles, theta=1..60 degrees, matched the formula within 5e-8. The infinite theorem follows from monotonic crossing, not the finite checks.

## originality

PASS

Best-of-knowledge original as the constrained sharp minimax profile, unique equality host, and phase transition. Ambrus–Csikós–Kiss–Pach–Somlai (2022/2023) prove the prerequisite pointwise classification of optimal embedded isosceles triangles and its three candidates, but do not themselves solve the family of outer optimizations under minimum host angle. The source’s actual Theorem 1.2(ii), Corollary 2.4, and area section were compared, not just titles.

## value

PASS

The minimum angle of a host triangle is a canonical mesh-shape/quality parameter. The theorem gives an exact worst-case guaranteed area retention and the unique worst host shape, including a nontrivial active-configuration switch. Its infinitely many threshold values are not a routine table and the phase corner matters for geometric optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.

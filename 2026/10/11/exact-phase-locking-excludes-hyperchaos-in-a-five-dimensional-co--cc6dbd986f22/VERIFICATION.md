---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

PASS. Direct differentiation of J=Im(conj(u)v)=x1x4−x2x3 for precisely the real integer-order system displayed in Lin et al. §2.1 yields J'=−(σ+1)J. Bounded completeness forbids nonzero J because backwards evolution explodes. Off the origin, u and v remain nontrivially collinear with fixed common phase by uniqueness and real coefficients, reducing dynamics to the stated 3D system. The 5D variational cocycle splits into base 3D block and a 2D transverse imaginary block along each fixed-phase orbit. On any non-equilibrium compact ergodic measure the flow vector and rotational group tangent each have exponent 0 (Poincaré recurrence and Oseledets existence), and the remaining 2D transverse exponent equals its constant trace −σ−1. The other two base exponents sum to constant divergence −σ−1−β, so at most one can be positive. Independent exact symbolic polynomial computation checked J decay, both divergences and transverse trace. It does not apply to Caputo orders α<1, arbitrary unbounded trajectories, or finite-time numerical exponents; the theorem does not prove absence of all chaos.

## originality

PASS

PASS, best knowledge subject to a high-priority full-text risk. Lin–Hou–Al-Towailb–Saberi-Nik (2022, published 2023) §2.1 explicitly prints the identical integer-order ODE and then studies a fractional-order Caputo model, boundedness and synchronization; inspected mathematical pages do not state the invariant J, a 3D fixed-phase quotient or the exact 5D Lyapunov splitting. Mahmoud–Al-Kashif–Farghaly (2008) advertises hyperchaotic attractors for a complex 5D model, rather than proving their exclusion; its abstract and bibliographic material are not sufficient for a whole-document noncoverage statement. Chien et al. similarly discuss numerical chaos/bounds, not an inspected theorem implying J' decay. The exact analytic identity gives a rigorous contrast to numerical two-positive-exponent claims. The inaccessible 2008 primary body remains material originality and model-comparison risk; Resultary was temporarily unavailable, not treated as proof of absence.

## value

PASS

PASS. Exponential decay of the gauge-invariant relative-phase determinant proves a global structural obstruction to compact hyperchaos for the ordinary system that previous numerical papers describe as hyperchaotic. The invariant 3D reduction and full Lyapunov decomposition are mathematically consequential and sharply distinguish true asymptotic invariant-measure exponents from finite-time estimates and fractional dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.

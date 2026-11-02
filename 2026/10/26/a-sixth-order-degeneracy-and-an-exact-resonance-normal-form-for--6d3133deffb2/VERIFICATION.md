---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The exact claim is restricted to fixed polynomial h orthogonal to z, and a fixed-real-(u,v) Dirichlet-unit four-mode path f_x=a(x)z+x z^2+u x^2 z^3+v x^3 z^4 for sufficiently small real x. Parseval gives D(f_x)=a^2+2x^2+3u^2x^4+4v^2x^6=1 and the second variation -sum_{n>=2}(n-2)|h_n|^2, flat only in z^2 among transverse polynomial modes. Independently derived the complete weighted-order-six Laurent log constant-term series from six independent exp(q_j z^{±j}) factors; it exactly matches the package formula, including cancellation of all q1^2 q2^2 terms. A separate symbolic substitution into q0,q1,q2,q3 verified [x^2]=0, [x^4]=-(2u-3)^2/4 and [x^6]=-2(9u^2-27uv+30u+9v^2-6v-5)/9. Setting u=3/2 makes the sextic deficit 1/24+2(v-31/12)^2; the unique real optimum v=31/12 has positive 1/24. The transformation f_{-x}(z)=-f_x(-z) establishes evenness and O(x^8) for fixed u,v. Phase-orbit minimization yields dist_D^2=2(1-a(x))=2x^2+O(x^4), hence (e-J)/dist_D^6→e/192, excluding every positive C for p<6. Independently evaluated a 256-point 50-digit boundary Fourier quadrature at x=.08,.04,.02, verifying convergence trend but not substituting numerics for analytic proof. This is not a proof of a full p=6 stability lower bound or an unrestricted optimum over all perturbations.

## originality

PASS

Best-of-knowledge PASS for the optimized real four-mode jet and necessary stability obstruction, not for the already known flat direction or sharp global inequality. Independent Resultary semantic searches returned sixth-order Fourier, finite-field and Sobolev examples but no matching Chang–Marshall jet; direct source-package GitHub code search for Chang-Marshall/Dirichlet sextic did not identify broader previously published SCOPE coverage. Full primary 2026 and 1994 texts were read and compared at the level of statements and implications. Highly relevant 1995/1996 texts were abstract-only; authorized 1996 full-text request returned VPN-disconnected, which is explicitly a residual priority risk rather than a scientific failure.

## value

PASS

This is a motivated structural near-equality invariant of the sharp critical Chang–Marshall Dirichlet embedding: the first Hessian-degenerate transverse mode forces a nontrivial cubic correction u=3/2 to cancel the quartic loss, followed by a uniquely optimized fourth-harmonic correction v=31/12. The positive 1/24 sextic loss and e/192 necessary constant impose a precise, reusable obstruction on any future quantitative Dirichlet-distance stability theorem. Neither the sharp global inequality, known quadratic flatness, nor numerical reproducibility alone supplies this nonlinear resonance. The finite four-mode scope is explicitly bounded; it is meaningful without promising a complete infinite-dimensional stability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

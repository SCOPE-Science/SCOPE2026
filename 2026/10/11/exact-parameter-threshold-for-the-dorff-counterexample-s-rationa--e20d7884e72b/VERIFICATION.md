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

The interval 0≤b<1/43 follows from endpoint signs of a convex x-quadratic numerator N_b(x) of the boundary angular derivative, with degree-one orientation and positive affine-normalization determinant E1<0<E2. Frozen verify_dorff_parameter.py (byte exact, Git blob 523bb5...) reconstructs variable Fourier coefficients c1,c2,c−1, normalization, the entire rational J_Fb(−99/100), and verifies the displayed factorization J=−14641 K H /[positive factors × E1³E2³]. Exact Bernstein coefficient tests over [0,1/43] prove K<0, H’>0, E1<0<E2 and exact root bracket 0.02218460173517970 < beta* < 0.02218460173517971. The verifier was executed and passed. At beta* Jacobian vanishes and after it sign reversal relative to J(0)=1 forces an interior singular point. This remains a conditional reconstruction from the source harmonic-map normalization, which could not be independently read in full this run.

## originality

PASS

Best-of-knowledge originality for the unique varying-b rational-witness threshold: published fixed-parameter results establish one negative witness or a spatial fold, not the parameter ray’s one algebraic threshold. Core exact Bernstein parameter classification is not implied by them. Inaccessible primary source is explicitly named; abstract-level access cannot certify full-text noncoverage, so this PASS is qualified with material residual priority risk.

## value

PASS

The original ellipse self-convolution counterexample is a natural test of a long-standing harmonic-map univalence question. The exact parameter boundary for its fixed rational witness along the entire maximal boundary-orientation ray quantifies robustness, distinguishes positive-, zero- and negative-Jacobian regimes, and supplies a continuum of non-univalent examples. Degree-18 algebraic uniqueness and Bernstein certificates make this a nontrivial motivated phase transition, not a random numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS. For each finite path K_N, eigenvalues are 2−2cos(jπ/(N+1)); the simple top eigenvector has all nonzero entries. At h_c=1/λ_top the weighted derivative K^(-1)DG=(K^(-1)−h_c I)+h_c diag(1+cos z_i) is PSD and singular only at p=(π,...,π), corank one. Integrated strict monotonicity gives a globally injective equivariant lift, and torus degree one yields a critical homeomorphism. In a small lift cube, 1−cos s≥s²/4 and ∫_0^1(a+tb)²dt≥b²/12 provide quartic coercivity and a 1/3 inverse Hölder bound; along the top eigenvector, the first nonzero image term is cubic, excluding any higher exponent. Odd Lyapunov–Schmidt reduction gives scalar −eps t+(1+eps)[1/(4(N+1))] t³+O_N(t⁵), exactly two nonzero roots with the claimed leading coordinates plus t=0. Compactness rules out remote inverse points for h↓h_c. D G_h(p)=I−hK has all multipliers in (−1,1) when h<2/λ_top. Independently solved N=2 odd mode for eps=.01: root 0.2440966957 versus leading sqrt(.06)=.2449489743. Analytic argument, not this sample, establishes all finite N.

## originality

PASS

Best-of-knowledge PASS. Primary Buescu–D’Aniello–Oliveira arXiv:2610.10993v1 (2026), Theorem 4.1 establishes exactly the strictly subcritical Morse–Smale diffeomorphism window and derivative singularity at equality. A singular Jacobian alone does not determine global injectivity. The audited claim proves topological critical invertibility, sharp inverse Hölder exponent, local three-point fiber immediately above threshold, and continued linear sink stability. These are not asserted by the inspected source theorem, despite standard local cusp/pitchfork principles furnishing antecedent techniques.

## value

PASS

PASS. It identifies the qualitative transition from a globally invertible torus homeomorphism with optimal cubic inverse loss to a genuinely three-to-one fiber, while the synchronization sink remains attracting. The gap between the diffeomorphism threshold and the attraction-flip threshold is motivated by the prior path-network model and is structurally informative across every finite path size, not just one small computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

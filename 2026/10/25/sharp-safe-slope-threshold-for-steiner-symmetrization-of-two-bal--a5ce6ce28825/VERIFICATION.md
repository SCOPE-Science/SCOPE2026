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

Read source RESULT.md blob dfb81c28837cba9881972abdb83bcce2b3dc19cd and SymPy verification program. For unit spherical upper cap f, −D²f=H(grad f); mixed upper symmetral h=(f1+f2)/2+C has ∇h=(p1+p2)/2, and every curvature ≥1 iff [H(p1)+H(p2)]/2−H((p1+p2)/2) is positive semidefinite in graph metric. At p=(sqrt R,0), directional matrix Hessian has determinant coefficients A=3(1+2R), B=−4R³+4R²+14R+6, C=2R³+7R²+8R+3; discriminant 16R²(1+R)²(R²−4R−2). For R<=2+sqrt6 positivity follows; beyond it, B<0 and the determinant becomes negative in mixed radial-transverse directions, proving the sharp disk radius. Construct p1,p2=p±εd and ball centers from q_i=−p_i/sqrt(1+||p_i||²), vertical offsets c=(s1+s2)/4. Strict inequalities |s1−s2|<2c<s1+s2 make a genuine open mixed fiber and the Hessian deficit negative for ε small. Independently re-derived symbolic determinant/discriminant and rational-gradient negative example (~−0.00343246) without executing opaque repo code. Claim is local smooth 2-ball R³ only, not nonsmooth curvature or >2 balls.

## originality

PASS

Best-of-knowledge PASS: full Artstein-Avidan–Florentin 2026 primary source establishes qualitative failure and arbitrarily large curvature loss. Published Resultary rank-one curvature-loss theorem proves at most one deficient principal direction but supplies no zero-deficiency sharp slope radius. The matrix Hessian cutoff is distinct quantitative content. Older equivalent matrix convexity formula might exist.

## value

PASS

The original two-ball Steiner lens counterexample leaves the precise safe-slope boundary unknown. The exact algebraic radius divides guaranteed preservation of *all* classical principal curvatures from attainable failure immediately outside, giving a natural curvature regularity criterion for the self-review, with a realizability construction rather than a loose necessary condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.

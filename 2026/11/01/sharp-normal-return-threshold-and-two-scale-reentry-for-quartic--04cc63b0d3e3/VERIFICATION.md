---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

At boundary point z=1 of Omega_A={|z^4+iA|<sqrt(1+A^2)}, the defining function gradient (8,8A) identifies gamma_A(t)=1+t(1+iA) as outward normal and curvature 1/sqrt(1+A^2)>0. Direct polynomial expansion factors phi(gamma)=t(1+A^2)H(t,A^2). When X=A^2<=7 all H coefficients are nonnegative; for X>7 Descartes' rule bounds positive roots by two. Substitution v=At makes H(v/A,A^2) a polynomial in 1/A with all positive-power coefficients positive and constant 8(1-v^2), proving strict monotonicity of the interior-return condition and a unique attained tangency threshold. Independently used SymPy to verify the exact Sylvester resultant = -262144(X-1)(X+1)^9 P(X), all 12 negative lower coefficients of P(7+Y), and P(134)<0<P(135). Thus exactly one X_*>7 discriminant root and A_*=sqrt(X_*); double tangency at equality and exactly two simple transverse crossings above follow from sign/Descartes. For large A the implicit-function expansions at v=1 and w=8^(1/5) with t=A^(-4/5)w give t_-=A^-1+31/16 A^-2+O(A^-3) and t_+=8^(1/5)A^(-4/5)-8^(-1/5)A^(-6/5)+O(A^(-8/5)). Finite algebra and sample-root evaluations corroborate; the monotonicity/root bound/IFT establish the continuous theorem.

## originality

PASS

The September 2026 Adamczewski quartic counterexample already has a normal return at A=64; the October 2026 Adamczewski-Colbrook work proves more general normal-return geometry and sufficient criteria for binomial lemniscates. The inspected Sections 3 and 4, especially Proposition 4.4, do not state the sharp fixed-quartic threshold A_*, complete two-crossing phase diagram, or explicit unequal-scale second-order expansions. These are narrower exact quantities for a motivated natural existing family, not a newly invented counterexample or a new universal mean-value bound. A classical unindexed discriminant calculation remains plausible priority risk.

## value

PASS

The quartic A=64 example motivates an exact phase diagram for the same canonical normal ray; specifying the sharp threshold and double-root contact is a natural complete one-parameter classification. Distinct A^-1 and A^-4/5 crossing scales, with explicit corrections, give substantive geometric structure beyond a cheap existence witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.

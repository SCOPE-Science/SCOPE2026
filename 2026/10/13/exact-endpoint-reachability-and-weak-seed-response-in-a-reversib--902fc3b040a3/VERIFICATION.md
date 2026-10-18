---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

With q,η,r>0 the source ODE preserves x,y,z≥0 and x+y+z≤1 since total derivative is −η z. Put s=x+y; s′=−ηr xz≤0, and z is nonnegative with finite ∫z; bounded z′ gives z→0. The forced linear equation x′+(1+q)x=s−ηr xz gives x→s∞/(1+q), y→q s∞/(1+q). Gronwall with s′≥−ηr s z and ∫z≤1/η yields s∞>0 for infected seeds with positive s0. A limit x∞>1/r would force eventual infected exponential growth, so every limit belongs to A=[0,min(1/r,1/(1+q))] on the disease-free ratio line. For balanced starting (u,qu,δ), s≤(1+q)u forces x≤u, and z≤δ exp(−η(1−ru)t). Integration yields the stated upper bound for u−Fδ(u) and dominated convergence gives its derivative ru/((1+q)(1−ru)). On any compact u interval interior to A the uniform exponential bound makes Fδ continuous; IVT brackets any target ξ exactly. Therefore all strict interior points are attained by genuinely infected trajectories and every closed attracting set for this seeded sector must contain their closure. Numerical IVP checks at u=1/5, q=5/3,r=2.7,η=100/33 corroborate the coefficient; proof is analytic.

## originality

PASS

The 2024 source Theorem 4.9 proves only that positive-infection limits lie inside the stable equilibrium segment. Section 5.2 explicitly conjectures that limits cover that segment. The reviewed argument proves surjectivity for interior endpoints by balanced-seed perturbations, and evaluates the derivative. Prior SIR control minimal-attractor work is acknowledged but its state equations lack the reversible exchange q>0. Best-of-knowledge original within this exact model.

## value

PASS

The model paper gives one-way convergence into a stable segment and explicitly conjectures its minimal attracting-set property. Exact reachability of each strict interior endpoint completes that missing half, with a rigorous seeded-domain qualification and a sharp local attack-rate coefficient. This is a structural dynamical claim about a concrete epidemic model, not merely rewording global convergence or numerical plots.

The dated certificate retains the supplied scientific assessment, sources and limitations.

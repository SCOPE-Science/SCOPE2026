# Independent mathematical audit

## correctness

PASS

The simplex is invariant, and the critical aggregate equations are multiplicative in Jᵢ; initial positivity persists. Since 1−S−σRⱼ≥Jᵢ, Riccati comparison gives Jᵢ=O(t⁻¹). Writing B=β₁J₁+β₂J₂, the stable equation for z=1−S gives z=O(t⁻¹), hence Jᵢ′ and B′ are O(t⁻²). Subtracting B/μ from z and γᵢJᵢ/μ from Rᵢ leaves stable equations with O(t⁻²) forcing, using Rⱼ≤z and O(t⁻²) secondary infections. This verifies the four reduced coefficients for the full solution, with multiplicative errors in the aggregates. The balance gives β₁>β₂ and k>0; b₂₁>0 since β₁−σ₁₂γ₁≥μ. With s=log t and uᵢ=tJᵢ, the ratio has log derivative −ku₁+O(e⁻ˢ), so is bounded above and converges after removing the integrable error. In particular u₁≤M u₂; comparison with y′=y(1/2−Cy) bounds u₂ away from zero eventually. A positive limiting ratio would contradict the integrated log derivative. Thus u₁→0 and logistic comparison gives u₂→1/a₂. The reciprocal ratio v solves v′=ku₂+ε(s)v, |ε(s)|=O(e⁻ˢ); the integrating factor gives v=O(1+s) and then v/s→k/a₂. Hence su₁→1/k. For w=u₂−1/a₂ the stable equation has coefficient a₂u₂→1 and forcing asymptotic to −b₂₁/(a₂ks); on scaling by s, the recent convolution has limiting mass one by dominated convergence and the part before s/2 is exponentially small. This gives the stated correction. Frozen verification support was inspected without executing the supplied code; its finite integrations are illustrative.

## originality

PASS

Best-of-knowledge pass for the global full-system two-rate law and the explicit subleading correction on the marginal double-critical surface. The demographic model and competitive normal-form ideas are not new; the closest inspected statements do not supply the asymptotics in this regime with the full-system error controlled.

## value

PASS

In a published deterministic model, the result distinguishes the two strains on a genuine boundary where their linear growth rates coincide. The full-system argument explains why an extra log appears and determines both leading constants and the faster-decaying strain's effect on the other's first correction. It is a global asymptotic statement, not a local linearization or a claim about stochastic elimination times.

The dated certificate retains the supplied scientific assessment, sources and limitations.

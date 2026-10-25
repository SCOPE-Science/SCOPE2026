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

Derived the threshold from the source payoff discriminant alpha(r/n-1)+beta*lambda/(beta+lambda)*(Wy-1/2), using alpha=1/20, beta=lambda=19/40 and r=3n/4. The scalar f(u)=0.5u+0.5*1_{u>21/38} strictly preserves the two threshold half-intervals, including tie to 0. Permutation equivariance gives exact y_t=P^t[sigma+2^{-t}(y0-sigma)] and all transient points converge to binary rotating words; Mobius inversion counts primitive necklaces. For perturbed stochastic W, ||aW||∞=1/2 and periodic affine forcing has a unique fixed orbit with ||Wy*-P sigma||≤epsilon/(1-a), giving strict threshold itinerary and local contraction if epsilon<17/76. Independently verified exact rational periodic solutions for n=3,4,5 fully connected off-diagonal W and 0<epsilon<17/76. The original Theorem 2 is in another all-defection symmetric-network parameter regime.

## originality

PASS

Best-of-knowledge novelty concerns the explicitly stated combined theorem, not its classical components; direct comparisons and material-reading limitations are recorded. The source formula supplies the dynamical system, not the orbit existence/period census. Conditional global convergence does not exclude attracting cycles outside its domain. The audited all-period construction is therefore not a disguised contradiction of an established theorem.

## value

PASS

The principal paper proposes whether equilibrium convergence may hold generally; this mathematically explicit family of attracting non-equilibrium cycles for arbitrarily large periods is a consequential sharp negative boundary under an update mode explicitly allowed by the model. Binary necklace enumeration and robustness to dense directed coupling make it much more than an isolated numerical cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.

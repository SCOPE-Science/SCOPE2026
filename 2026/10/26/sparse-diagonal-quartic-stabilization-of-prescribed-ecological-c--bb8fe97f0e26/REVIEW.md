# Scientific review: sparse diagonal quartic stabilization

## Correctness — PASS

The constructive parameters are explicit and strictly positive. Direct substitution cancels the per-capita growth at the prescribed positive equilibrium. Differentiation gives exact Jacobian entries and a strict Gershgorin left-half-plane inequality with any specified spectral margin. A maximum-coordinate comparison proves nonnegative forward invariance, a uniform absorbing box, and global forward existence. The worst-case diagonal-only support lower bound follows from the decoupled constant-negative-growth instance, where one monomial necessarily has a positive derivative at the required fixed point. The separately executable rational verifier passes all 1,400 generated cases. These calculations corroborate, but do not establish, the quantified statements.

## Originality — PASS, with limitations

The main comparison is Çelik et al., *Stable Coexistence in Ecologies and Games*, Theorem 4.2 (arXiv:2609.09286v1). That theorem obtains a stable equilibrium with unconstrained higher-order tensors, using mixed-species total-population polynomials. It does not imply a self-only positive-quadratic/negative-cubic intervention, sharp diagonal support budget, arbitrary prescribed abundance, or uniform dissipativity. Cui et al. (arXiv:2405.18333), particularly Theorem 5, Remark 7, and Corollaries 3–6, give restrictive tensor sign/dominance criteria, not the present universal fixed-pairwise self-only realization. Classical density-dependent stability theory is credited and is not asserted to be novel. The scalar lower-bound calculation is proved independently; it does not claim priority over existing third-order obstructions. No equivalent stronger statement was identified in the searches performed, but absence from search results cannot certify historical priority.

## Mathematical value — PASS

The unrestricted high-order existence result left the structural question of whether distinct-species higher-order terms are necessary to overcome arbitrary fixed pairwise obstructions. The theorem answers negatively with a sign-constrained and **support-minimal diagonal intervention**, while adding dissipativity and an adjustable stability margin. This is a precise sparse realization result, not merely a new numerical threshold or a reparameterization of an already fixed-point feasible system. It distinguishes cross-species interactions from density regulation within species, an ecologically meaningful modeling choice.

## Scientific limitations and residual risks

Local exponential stability does not imply global convergence, unique coexistence, exclusion of alternative boundary equilibria, or biological reasonableness of the potentially large intervention coefficients. Support optimality is restricted to own-density degree-two and degree-three terms, and is not asserted among unrestricted cross-species or arbitrary-degree polynomial interventions. Archival indexing may omit an older equivalent sparse realization argument; no independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.

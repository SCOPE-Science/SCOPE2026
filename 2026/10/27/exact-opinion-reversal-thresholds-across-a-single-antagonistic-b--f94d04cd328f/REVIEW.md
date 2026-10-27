# Scientific review

## Correctness

**PASS.** The claimed exact coordinate formula follows from the strictly convex signed-equilibrium energy by eliminating the interior vertices of the two positive communities. Their endpoint self-energies are \(A(u-1)^2/2\) and \(B(v-1)^2/2\), with \(A=1/(G_U)_{aa}\), \(B=1/(G_W)_{bb}\). Minimizing these together with the antagonistic term gives the denominator \(AB+t(A+B)\), strictly positive. The harmonic extension profiles are strictly positive and at most one by the killed-graph maximum principle. Multiplication by the denominator gives the threshold and the one-side-only criterion. Strict ascent along harmonic profiles proves the connectedness of their superlevel sets. No computation is treated as proof for all graph orders. The standalone package passed 4,556 exact-rational comparisons.

## Originality

**PASS, with publication-priority risk.** The closest source, Zhou et al., arXiv:2407.10680v1, Sections II–V, provides the signed equilibrium inverse, random-walk representation, aggregate conflict/polarization functionals, Laplacian solver, and opinion-seeding optimization. Xu et al., arXiv:2006.10961v1, Sections 2–3, provides the signed social trust equilibrium and aggregate opinion interventions. Their all-input equilibrium inverse formulas can be used to solve individual cases but do not themselves state the sharp *single-antagonistic-bridge* all-graph reversal criterion, rooted negative-region geometry, or the explicit thresholds from anchored Green functions. A 2026 weighted signed FJ seeding study was inspected only at the abstract/model/notation level; its full theorem details could not be confirmed. No direct duplicate was recovered from available mathematical-record searches or this slot's accessible historical claims. Broad sign-lifting, resistance, and matrix-perturbation results could still imply parts of the theorem; independent novelty assessment is outstanding.

## Value

**PASS.** The result determines, without solving the full signed system at every hostility strength, whether a single hostile intercommunity tie can reverse expressed opinions even if **all** agents personally agree. The complete quantitative reversal thresholds distinguish effective anchoring from simple node degree; the connected, one-sided, nested footprint gives structural information beyond the initial sign change. A three-agent example demonstrates successive reversals at different tie strengths, while another three-agent example proves that unequal topology alone can cause reversal even with uniform anchoring. The answer is specific to a natural bridge perturbation in a standard signed opinion model, not an arbitrary numerical slice.

## Limits and closest literature

The source papers establish the general model and many equilibrium properties; standard Schur-complement theory is not novel. The new claim is restricted to two connected positive communities, one negative intercommunity bridge, positive individual anchoring, and identical positive innate opinions. The 2026 paper addresses a different optimization but remains an access-limited publication-priority risk. Finite exact checks are not exhaustive over graphs. Independent scientific validation is outstanding.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness — PASS

The stated domain and normalization are explicit: fair independent nearest-neighbor steps; the maximum includes the initial state, and the return count excludes it. Reflection identifies the origin-return paths reaching an integer barrier with unconditioned endpoints at double that barrier. First-passage and Green-function products account for whether the barrier was reached before a return or must be reached afterward, with the initial return explicitly subtracted. Geometric summation proves the mixed generating function; a monotone-density Tauberian theorem gives its leading coefficient. The corresponding return-count moment transform and maximal moment convergence yield the limiting covariance and correlation. Two independent exact-rational computations agree on every coefficient through degree 16. The finite test is supplementary, not the infinite proof.

## Originality — PASS, subject to residual literature risk

Kirschenhofer and Prodinger (1996) is a close primary reference: its Sections 2 and 3 separately study counts of origin returns and counts of visits to the maximum, using bridge and fixed-endpoint decompositions. It does not identify the unconditioned simultaneous product of the **maximum height** and **zero-return count**. Pitman (1998) studies Brownian bridge local times and distributional identities; Denisov and Wachtel (2014) treat local times of killed and reflected walks; Csáki, Földes and Salminen (1987) treat diffusion maximum and argmax, with a different local-time maximum application. The published maximum–endpoint half-variance identity involves the terminal location, not the accumulated returns. A more general unpublished or overlooked bivariate path transform may imply the claim. Search nonmatches are not a uniqueness certificate.

## Mathematical value — PASS

The finding quantifies dependence between two intrinsically different path statistics: the largest positive excursion height and the accumulated frequency of origin returns. The exact mixed generating function provides finite-time moments, while its singularity yields an explicit strictly negative linear covariance coefficient and nonzero limiting correlation. This is a substantive joint-path statement rather than a recomputation of either marginal moment or a renamed endpoint-covariance formula.

## Scope and literature limitations

The formula is restricted to the symmetric simple walk, and the sign result is limiting rather than finite-universal. Plausible general joint functional transforms could subsume the exact identity; independent review and broad literature validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.

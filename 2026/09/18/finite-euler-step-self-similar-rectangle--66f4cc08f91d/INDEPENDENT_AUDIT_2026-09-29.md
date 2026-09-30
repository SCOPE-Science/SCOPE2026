# Independent Audit — 2026/09/18/finite-euler-step-self-similar-rectangle--66f4cc08f91d

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `083f3b92cc6bbba923ceedc46a9dd5d81bc0ef67`
- Disposition: **PASSED**

## Correctness

**PASS** — The asymptotic argument is sound under the finite-step hypotheses quoted from the source proposition. Every endpoint other than b_n is positive, nonincreasing and integrable, hence t x(t)->0; combined with b_n asymp 1/t this gives x=o(b_n). In the exact b_n equation, the prefactor tends to 1/2, all inner cosine differences are o(b_n^2), and the last interval contributes -2c_* b_n^2(1+o(1)), so b_n'=-c_*b_n^2(1+o(1)) and t b_n->1/c_*. The sector mass and weighted moment then have the stated limits. Scaled endpoints give L1 convergence to c_* 1_(0,1/c_*], while the Green-kernel limit t K_m(y/t,z/t)->-min(y,z) yields the displayed rescaled stream function. In logarithmic time, y+2G_*(y)=y(c_*y-1) on the support, so the limiting rectangle is stationary for the similarity transport field.

## Originality

**PASS** — The source preprint provides comparability of the rightmost endpoint and mass and integrability of the inner endpoints, while earlier scale-invariant Euler work gives qualitative relaxation mechanisms. Targeted searches located no prior statement of the exact constant t b_n->1/c_*, the universal rectangle profile, or the explicit scaled Green-field/velocity limit for this finite positive-step m>=4 system. The novelty claim is therefore limited to this sharp source-specific asymptotic refinement.

## Scientific value

**PASS** — The result upgrades two-sided decay bounds to a complete leading-order similarity law, identifies exactly which datum survives at the t^{-1} scale, and gives the limiting transport field. This is a useful structural description of the finite-step dynamics and provides a concrete asymptotic model for comparison with the source paper's more complicated infinite-stack dynamics.

## Sources

- Dense orbits for scale-invariant rotationally symmetric solutions of the 2D Euler equations (I. Suleiman): https://arxiv.org/abs/2609.20674 — Source finite-step endpoint system and decay/integrability estimates.
- On the long-time behavior of scale-invariant solutions to the 2d Euler equation and applications (T. M. Elgindi; R. W. Murray; A. R. Said): https://doi.org/10.24033/asens.2621 — Earlier qualitative long-time relaxation framework for scale-invariant Euler solutions.

## Limitations

- The result applies only to finite positive ordered step data and m>=4.
- It does not cover arbitrary regulated data, infinite stacks, or the m=3 regime.
- No convergence rate beyond the leading limits is established.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository write was performed. Open-access/preprint sources were checked first; Oxford Download was not needed for this record.

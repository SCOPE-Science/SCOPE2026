# Self-review

## Correctness — PASS

All quantifiers and boundaries have been reconstructed for \(1/2<a<1\), \(0<\varepsilon\le1\), \(0<b\le1\), and **only** central half-turn least-period-two cycles with heights in \((-1,1)\). The angular half-turn equation has exactly two momentum roots because the twist is positive, below one and strictly decreasing in absolute height on this strip. Splitting the two possible signs of successive heights exhausts the cycles. Product Jacobians yield exact trace identities and the full identity matrix at the reversing collision. The crossover derives from a strictly increasing scalar function on \((0,1/4)\). Symbolic and direct orbit checks in `verify_halfturn.py` passed. Linear ellipticity is not claimed to give nonlinear stability.

## Originality — PASS within inspected evidence

The 2022 defining model (arXiv:2209.07408) reports fixed points and primary reconnections, not these period-two formulas. The 2023 exact-model follow-up (arXiv:2305.17538, Section 4, Figure 6) observes the **same rotation-\(1/2\) collision numerically** and reports its bifurcation curve by numerical root search; its example \((a,\varepsilon)=(0.515,0.1)\), \(b\approx0.3259\), agrees with the new exact \(b_c\approx0.325836900672\). Classical reversing-symmetry work (arXiv:nlin/0411026) contains analogous indicator curves and even-period scenarios for the standard nontwist map and is explicitly credited, but does not state the nonzero-quartic exact family and the interlocking flip/collision threshold. The 2024 follow-up (arXiv:2409.00785) investigates transport, not this classification. Previously recorded work on this exact map treats fixed points only. Searches in indexed research records yielded no claim covering the exact two-cycle classification. An unindexed or generically formulated equivalent result remains a priority risk; no universal novelty proof is asserted.

## Value — PASS

The precise \(1/2\) collision occurs in a plotted, physically motivated parameter range of the published plasma-transport model. Replacing its numerical boundary with a closed algebraic curve is useful for resonance bifurcation diagrams; the exact identity monodromy separates this degeneracy from generic parabolic return. The additional sharp parameter \(a_*(\varepsilon)\) identifies the boundary of coexistence of two linearly elliptic cycles and two hyperbolic saddles, with an explicit closed form at \(\varepsilon=1\). This provides structural information not supplied by the approximate reconnection diagrams.

## Residual scientific limits

No exhaustive census of *all* cylinder period-two orbits, proof of nonlinear stability, or global transport inference is asserted. Full possible generic implications of classical reversible-map theory and unindexed calculations merit an independent priority review.

Self-review: passed. Independent audit: not yet performed.

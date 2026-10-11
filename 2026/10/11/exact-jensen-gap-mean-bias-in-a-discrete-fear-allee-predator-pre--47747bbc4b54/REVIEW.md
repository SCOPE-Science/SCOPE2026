# Same-model review

## Correctness
PASS. The coordinate ratios are reconstructed directly from the printed map. Invariance of \(\log N\) and \(\log P\) yields zero-mean logarithmic growth factors. Strict Jensen gives the exact prey-mean defect, and the equality case is reduced to the unique positive equilibrium. The completed-square calculation for \((1-N)(N-\theta)\) gives the predator ceiling. `verify.py` independently replays the algebraic identities.

## Originality
PASS. Targeted searches compared the claim with the source, its cited discrete predator–prey bifurcation literature, and semantically close public research records. The closest work concerns local flip, Neimark–Sacker/Hopf, invariant-curve, stability, or chaos results. No inspected source states or implies the exact invariant-measure Jensen-gap law or its strict two-sided support consequence. Residual risk remains that an unindexed paper could contain an equivalent stationary-balance observation.

## Value
PASS. The source's main dynamical phenomena include periodic oscillations and chaotic numerical regimes. The finding supplies a finite-amplitude, orbit-independent diagnostic for all compact positive recurrence: the mean prey density must be shifted above the coexistence coordinate, while recurrence still visits both sides of that coordinate. It also supplies a universal predator-mean ceiling. These statements remain informative away from the local bifurcation limit.

## Closest literature and limitations
The primary source is Hong and Zhang, DOI 10.3934/math.2023678. Related discrete predator–prey papers located in its bibliography analyze different maps and local bifurcations. The theorem requires compact invariant support strictly inside the positive quadrant and does not prove existence, uniqueness, ergodicity, or stability of any recurrent state.

Same-model review: passed. Independent audit: not yet performed.

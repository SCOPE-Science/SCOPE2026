# Independent mathematical audit

## correctness

PASS

Fold the circle by x=||t||. On [delta0,1/2] the induced distance map is bx-(b-1)/2 for odd b and b/2-bx for even b. In the odd case the allowed inverse branch fixes 1/2 and scales distances from it by 1/b. In the even case the two-step allowed folded interval is (delta,1/2-delta/b). The decreasing inverse y -> 1/2-y/b maps that interval into itself: its upper image endpoint is 1/2-delta/b and its lower one is delta0+delta/b^2 >= delta precisely up to the critical threshold. Thus every subsequent step scales length by 1/b; unfolding gives precisely two reflected intervals. The closed folded interval at equality collapses to the unique fixed distance b/[2(b+1)], attained by the stated two-cycle. In the odd case only 1/2 attains the maximal distance. Dividing nested Lebesgue probabilities gives the claimed conditional geometric tail, without independence. Separate exact breakpoint tests (python /workspace/independent_checks.py 1) passed 60 cases, including strict and non-strict critical boundaries, for five bases and horizons 2–4. The proof, not those tests, covers all bases and horizons.

## originality

PASS

The best-supported distinct contribution is the exact finite-horizon near-critical profile with parity-specific component counts and all-horizon conditional exit law. Inspected prior results treat the underlying loneliness objective or an infinite-horizon hole problem; neither supplies that profile. The critical optimizer calculation alone is elementary and is not relied on as a separate priority claim.

## value

PASS

A natural model speed family now has an exact near-critical density benchmark uniform in horizon and base, distinguishing a fixed point from an alternating two-cycle. The exact interval count and geometric conditional law are informative beyond a lower loneliness bound or a finite set of computed optimizer values. No claim is made outside the narrow stated strips.

The dated certificate retains the supplied scientific assessment, sources and limitations.

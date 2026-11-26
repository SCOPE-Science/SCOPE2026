# Independent mathematical audit

## correctness

PASS

For an independent count let z and o count nonempty subsequences ending in 0 and 1. Appending a block of ℓ zeros leaves o unchanged and increments z by ℓ(1+o), since the new ending-zero outputs after one append are exactly all previous outputs (including empty) with a final zero. The analogous update holds for ones. Iterating four blocks gives equation (1), without counting embeddings. Substitution at fixed p,q gives the displayed deficit. Aligning the signs of u=a−d and v=b−c lowers it strictly when uv<0. For α=|u| and β=|v| after alignment the change in the deficit from increasing α by 2 is [(α+1)(4+q²−β²)−4β]/4, strictly positive since β≤q−2. The analogous step in β has numerator (β+1)(4+4p+p²−α²)−4α, also positive since α≤p−2. Both magnitudes are therefore uniquely minimal in their respective parity classes, and matching signs are mandatory if both sums are odd. Substitution gives all four correction terms, including the p=2 or q=2 boundaries. The continuous critical point p*=n/2−1+O(n⁻¹) gives the upper asymptotic via H; taking lengths within O(1) of n/4 gives the matching lower asymptotic. The uniform O(n⁻¹) lower-order terms after division by n⁴ and strict AM–GM on the compact proportion simplex give the limiting rigidity in both directions.

## originality

PASS

Pass is for the simultaneous fixed-outer/inner-sum result, its sign-sensitive parity penalties and full equality classification, yielding an exact finite maximum on all lengths. The routine polynomial itself is covered as a specialization of general counting recurrences. Liron–Langberg already prove the global equal-run optimum at n=4k for every deletion count and a balancing lemma when the intervening runs are symmetric. Those results cover inner balancing and the symmetric-inner outer exchange, but not the full conditional problem with unequal inner runs and both sums odd, where orientation changes the answer. The closest Resultary overlap proves parity-dependent opposite-gap balancing in a different family (three singleton ones and variable zero gaps), with opposite optimal orientation. Its theorem does not imply the frozen criterion. These verified overlaps limit the credited claim.

## value

PASS

Four alternating runs are a natural first restricted binary family with two simultaneously movable opposite-run pairs. The complete conditional classification, including the odd–odd orientation, replaces a full run-composition search by one integer index without losing any maximizing configurations; the asymptotic rigidity then identifies exactly which proportions can be near the leading extremum. The contribution is the sharp constrained optimization, not using a known recurrence to compute four-run counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.

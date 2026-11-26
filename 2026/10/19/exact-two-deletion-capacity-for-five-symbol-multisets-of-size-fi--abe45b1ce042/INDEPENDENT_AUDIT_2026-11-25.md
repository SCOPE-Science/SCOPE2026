# Independent mathematical audit

## correctness

PASS

A common two-deletion output is precisely a size-three submultiset of the coordinatewise minimum; it exists iff the sum of those minima is at least three. On weight five, this is equivalent to a full ℓ₁ separation of less than six. An independent deletion-shadow replay checked the ten-word witness, reconstructed all 126 profiles and verified the printed case minima and incidences. A and B have a fixed common size-three submultiset and C has pairwise overlap at least three by the verified table and coordinate symmetry. Pointwise coverage is 16a+3b+c≥16, and the summed clique weights are exactly 5+20(3/16)+20(1/16)=10, proving the bound. Independent short proof: remove every word with some count ≥3 (at most one per symbol, and never two such counts in a single word), then insert all five pure words with no size loss and no conflict with the residual words. If a,b,c are the residual counts of types 221, 2111 and 11111, their disjoint size-three output sets use 4a+3b≤20 outputs with a double symbol and a+3b+10c≤10 all-distinct outputs. Twice the first plus the second gives 9a+9b+10c≤50, so at most five residual words coexist. The construction has five, hence 10 is exact.

## originality

PASS

Pass for the exact equality and attainment, not for the coding formulation, the weighted-cover method, or the numerical upper bound alone. Relevant earlier works cover the same multiset metric, the one-deletion optimum for these length/alphabet parameters, or exact unbounded ℓ₁ values only at weight ≤4. The stronger later Kreindel et al. v3 theorem yields the frozen upper bound mechanically and attributes it to Wei–Zhang (2023); thus the bound itself is not credited as a distinct result. The inspected statements and constructions did not settle the lower bound of 10. Wei–Zhang's primary full text remains material, unresolved risk for the capped construction and priority.

## value

PASS

This determines an exact quinary benchmark in the studied t=n−3 multiset regime and the first weight outside the cited unbounded weight-at-most-four results. The lower construction establishes that the general upper benchmark is attainable at these parameters; attainment with disjoint typed deletion shadows is not supplied by a size bound alone. The result gives a compact test instance for exact ℓ₁ and multiset-code bounds. Value is for the exact two-deletion capacity and witness, not for the generic clique-cover technique or for giving a second derivation of an upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.

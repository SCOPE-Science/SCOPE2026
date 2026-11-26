# Independent mathematical audit

## correctness

PASS

In round r the old burned vertices and their pairwise sums are contained in the span of the first r−1 sources, and the contemporaneous source can add only one vertex. For r≤m the resulting bound 2^(r−1) is insufficient. The same argument in round m+1 with a deficient prefix span excludes every dependent first-m tuple. Conversely, for an ordered basis, at the end of r≤m the burned set is exactly the nonzero preceding span plus the new basis vector: sums of the preceding basis vector with all old nonzero span vectors fill its coset, except for the vector itself which is already burned. The same final update fills the space before the last source can have any effect. There are 2^(m−1)−1 legal final choices for each ordered basis; the product and forced profile follow. Validity uses the previous round's burned set, not the set after current propagation. The recorded m=3,4 counts agree; no finite computation is used for the universal proof.

## originality

PASS

Credit the optimum length, the nested-hyperplane construction with a redundant final choice, and the standard lazy span closure to prior work. They are not the contribution. The inspected sources do not give the exact all-optima sequential classification with its forced synchronous profile and all-dimensional labelled count. The thesis could not be fully checked; the attributed small cases are not claimed as new.

## value

PASS

The labelled optimum-schedule count is a natural refinement of the established minimum-round invariant, with small instances already of computational interest. The result replaces finite enumeration with one structural description for arbitrary dimension and determines which rounds and choices matter. The basis product alone is routine; the contribution is identifying exactly the schedules to which it applies, including forced redundancy and its multiplicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.

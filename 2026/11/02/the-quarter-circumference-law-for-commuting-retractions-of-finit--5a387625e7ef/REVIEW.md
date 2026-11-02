# Self-review

## Correctness
PASS. The claim concerns every integer \(n\ge3\) and **only** commuting vertex-prefix retractions of the ordinary unit-edge metric cycle. Each Lipschitz norm is the maximum image distance of adjacent vertices and hence an integer. If all projection norms were below \(n/4\), signed geodesic arcs would define an integer degree. One parent-collapse step changes only the fiber of the newly fixed vertex; its interval-boundary quadrilateral has total length less than \(n\), so its degree contribution vanishes. This forbids changing the constant map of degree zero into the identity map of degree one. The four-anchor parent construction attains \(\lceil n/4\rceil\), including the small cases. A direct standalone checker passed for \(3\le n\le128\); the proof is independent of that finite range.

## Originality
PASS, subject to bibliographic risk. Novotný [1, Theorem 5] treats a distinct pointed metric that includes an additional center vertex at large distance from every rim vertex, and proves a weaker asymptotic lower bound there. Hájek–Medina [2, Theorem 2.6] treat general nets and do not calculate the optimal constant for ordinary cycles. Targeted searches for optimal commuting cycle retractions, alternative formulations, dominating general results, and exact tables did not return the quarter-circumference law. Failed searches alone do not certify novelty. Earlier isolated small-cycle values do not imply the all-length classification or its degree mechanism.

## Mathematical value
PASS. The invariant is naturally motivated by the sharp projection cost in retraction-derived finite Schauder filtrations. The result supplies the exact constant for an entire graph family and a winding-number obstruction showing why the quarter-circumference threshold, rather than a merely numerical bound, is sharp. The construction is explicit and the result distinguishes graph-metric cycles from centered-circle extensions.

## Closest literature and limitations
[1] M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188, Definition 3 and Theorem 5. [2] P. Hájek and R. Medina, *Schauder Bases in Lipschitz Free Spaces over Nets in Banach Spaces*, arXiv:2112.03095, Definition 1.2 and Theorem 2.6. The claim excludes weighted and continuous cycles, graphs with an extra center, and arbitrary nonretractional projection bases. An unindexed equivalent graph-filtration result remains possible. Independent external scientific review has not occurred.

Self-review: passed. Independent audit: not yet performed.

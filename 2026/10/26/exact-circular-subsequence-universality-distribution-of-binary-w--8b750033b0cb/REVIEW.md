# Independent mathematical audit

## correctness

PASS

An arch factor of a binary word must contain adjacent unequal letters. A k-universal rotation is partitionable into k disjoint complete-alphabet arches; each supplies a matching transition edge on the cyclic position graph. Conversely k vertex-disjoint unequal adjacent pairs can be placed as k separate arches under one cyclic cut. The transition vector has even parity and two word lifts. Runs of consecutive transition edges contribute ceil(length/2) matching edges; the all-ones even-cycle case is handled separately. Cyclic block-sequence logarithmic differentiation with parity marker v=+/-1 yields the rational generating function, and coefficient extraction gives every C_nk. Independent fresh direct enumeration over ALL indexed binary strings n=1..11 tested greedy arches over every rotation against the coefficient formula, matching every row and 4094 words total. The attached source verify.py independently checks through n=17 but was inspected, not used as substitute for the all-n proof. n=1, n=2, constants and alternating words were explicitly included.

## originality

PASS

The previous Resultary closed-form binary universality law counts the *linear* index and has generating function (1+z)/(1-z-2uz^2). The circular index is a maximum over a shared rotation, and its distribution is a genuinely different rational function. Barker et al., Fleischmann et al. and Schnoebelen–Veron establish arch decompositions and algorithms for a single word; inspected primary sections do not present the asserted all-length indexed binary circular distribution. A matching-equivalent enumeration in classical cyclic run theory is an explicit priority risk.

## value

PASS

Circular subsequence-universality is a standard word-theoretic invariant. The all-length distribution gives exact counts of words of each attainable index and extremizers for lengths 2k and 2k+1, complementing single-word algorithms and linear-index laws. The fixed alphabet and common cut are essential and clearly stated; the result is not a relabeling of the linear statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.

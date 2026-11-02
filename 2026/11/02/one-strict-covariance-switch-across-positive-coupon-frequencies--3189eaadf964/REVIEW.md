# Review of the packet-frequency covariance sign classification

## Correctness
**PASS.** The per-coupon binomial marginals and the conditional law of a second coupon after excluding a first are exact for independent uniformly sampled fixed-size groups. The resulting mixed moment is an ordered-pair count. Its factorization gives a strictly increasing frequency ratio, opposite endpoint signs and an arithmetic proof excluding ties. The exact enumeration checker confirms \(169\) independent finite moment identities, but does not substitute for the proof. The dense-packet transition follows from uniform logarithmic expansions.

## Originality
**PASS, qualified.** Mahmoud and Smythe (2012) previously proved a *general exact covariance formula* for the entire coupon-frequency spectrum, and Section 10 simplifies the special covariance between unseen and singleton classes. The finite mixed-moment formula itself is therefore not presented as the original discovery. Their paper does not explicitly articulate the strict all-positive-frequency one-switch classification, packet-width monotonicity, no-zero property or packet-width sign reversal. Betken–Thäle's full preprint focuses on marginal missing-count approximations; Schilling–Henze's accessible abstract focuses on low-frequency Poisson limits. The closest retrieved published result on iid uniform occupancy has a related single-switch pattern but does not model within-packet exclusion. Historical priority remains uncertain: prior general covariance identities might have been analyzed elsewhere, and mathematical consequences derivable from them may have been implicitly known.

## Value
**PASS, qualified.** Beyond an isolated second-moment value, this is a complete qualitative cross-dependence diagram for every positive coupon-frequency class at all feasible finite sizes. It proves one strict sign transition without exceptional arithmetic equalities and identifies the natural packet-width direction of reversal and its asymptotic location. Such an exact finite sign classification distinguishes frequency classes that co-fluctuate from those that oppose the unseen population in a repeated fixed-size sampling experiment. It is a focused structural consequence rather than a new covariance-generation technique.

## Limitation
The model assumes independent uniform fixed-size packets. Only covariance signs are established; no monotone stochastic coupling or joint limit law is inferred. Earlier general formulas are recognized as mathematically stronger for raw covariance evaluation. This self-review does not establish historical priority or independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.

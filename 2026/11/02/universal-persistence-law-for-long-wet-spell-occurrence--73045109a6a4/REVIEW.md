# Review: Universal persistence law for long wet-spell occurrence

## Correctness: PASS

The claim is scoped to a stationary two-state transition matrix with wet marginal \(1/2\), fixed \(k\ge3\), and long observation windows. A positive eigenvector recurrence derives the exact Perron equation. A strictly increasing change of variables transforms minimizing the Perron root into maximizing a scalar function. Its derivative has a strictly decreasing sign bracket, so there is a unique critical point and global optimum. The large-spell limit follows from a compactness argument, exclusion of a zero limit, and uniqueness of the limiting scalar equation. The independent standard-library checker verifies exact rational small cases, rational characteristic identities, finite Perron comparisons and asymptotic numerical instances (387 assertions). These calculations corroborate rather than replace the proof. No empirical or finite-window optimizing assertion is made.

## Originality: PASS under the inspected evidence, provisional

The full publicly available text of Fu, Wang and Lou (2003) establishes an exact longest-run distribution and the associated Perron decay rate with *fixed* transition probabilities; its Sections 2, 4, 5 and 6 were materially compared. The present theorem optimizes that rate over a symmetric equal-marginal transition family, proves a **unique** maximizer for every \(k\ge3\), and obtains two new large-length constants. An earlier two-wet-day theorem gives the \(k=2\) specialization; it does not give the all-length classification. The full text of Sen, Mohan and Agarwal (2013) concerns a different Markov success/failure pattern and does not state the result. Abstracts and bibliographic material of Koutras (1997), Lou (1996), Samarova (1982), Caskey (1963) and Weiss (1964) were checked. Complete full text of Koutras and Samarova was not accessible; earlier equivalent optimization is a remaining priority risk, not silently ruled out. Published transition-matrix distributions alone do not imply the new unique optimum or universal scaling without additional analysis.

## Value: PASS

Fixing the wet-day marginal isolates serial dependence from frequency. The result solves the exact structural design question: which persistence makes a rare long wet spell emerge at the greatest asymptotic exponential rate? Its sharp all-length answer and large-spell scaling constant are reusable for stress tests of binary rainfall generators and comparisons of spell-risk models; they are not a field forecast or a risk estimate for rainfall volume.

## Limitations and evidence

The Markov and equal-marginal assumptions are restrictive. The observation-window asymptotic is taken before the wet-run-length asymptotic. One directly relevant 1997 full manuscript and other older manuscripts remain incompletely inspected; no independent audit has taken place. Reproducibility code checks finite examples, and analytic arguments cover infinite quantifiers.

Self-review: passed. Independent audit: not yet performed.

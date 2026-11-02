# Scientific review

## Correctness — PASS

The claim is an all-order, exact two-level counting and characterization result. Each length-limited requirement includes all shorter factors. The single-position lower bound is absolute (both single-letter factors exist). The decisive local step is the exhaustive twelve-context comparison: the six length-three factors force two positions each covering three distinct triples, and only two of the eight complementary centered length-five pairs also cover both letters and all four bigrams. The list of twelve five-factors follows rigorously from the two parity offsets of the two-uniform substitution, so the table is exhaustive at every order. Exact pair-frequency recurrences yield the closed forms; there is no induction-to-infinity extrapolation from finite data. Direct factor-coverage enumeration agrees with the local criteria at orders through ten, and the five-factor frequency formulas are checked through order fourteen.

## Originality — PASS, with residual risk

The 2026 papers of Banbara et al. and Faro–Marino–Pavone enumerate **unrestricted** minimum attractors (four positions for the specified Thue–Morse orders), not minimum attractors limited to length-two and length-three factors. Even the general all-factor coverage antichain of the latter paper cannot imply the claimed shorter-factor optimum, since long-factor obligations are absent here. The older Fuchs–Whittington work establishes complexity of \(k\)-attractor optimization on general inputs, rather than the special all-order spectrum. Targeted research-record, prior-claim and external-literature searches uncovered no exact counterpart; indexing gaps and the lack of a full reading of some older general papers remain residual priority risks.

## Value — PASS

The count of *minimum attractor sets*, not merely optimum size, is a fine-grained repetitiveness invariant motivating recent complete classifications. The two elementary but distinct cutoffs already have different all-order spectra: both admit two-position solutions, but the \(3\)-attractor population is asymptotically one quarter as large as the \(2\)-attractor population. Both are quadratic in \(N\), while unrestricted minima for the same source words are bounded in number (32 for orders at least six). This separates short-factor coverage flexibility from rigid global coverage and supplies explicit test families for length-limited attractor algorithms. The local classification is part of the value; a numeric count alone would be less informative.

## Closest literature and limitations

See arXiv:2602.16152 and arXiv:2610.10950 for the canonical unrestricted case, and arXiv:2304.06523 for the general \(k\)-attractor problem. The theorem is limited to the canonical binary Thue–Morse iterates and the first two nontrivial factor cutoffs. It does not classify larger \(k\), nor arbitrary infinite-word factors. Formal external validation and a complete publication-priority check have not been performed.

Self-review: passed. Independent audit: not yet performed.

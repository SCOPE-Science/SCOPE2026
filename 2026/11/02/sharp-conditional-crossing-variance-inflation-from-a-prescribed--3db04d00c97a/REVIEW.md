# Scientific assessment

## Correctness — PASS

For each \(n\ge3\), conditioning on a prescribed chord leaves a uniformly paired set of \(2n-2\) endpoints. Elementary one- and two-edge matching probabilities yield exact degree moments. The nonstandard step is the mixed covariance between degree of the conditioned chord and crossings among the remaining chords, found by summing the length-dependent crossing expectation over every possible straddling pair. The finite double sum simplifies to \(ab(a-1)(b-1)/[6(2n-5)(2n-3)]\). Combining with the classical crossing variance gives the final conditional variance, and an independent finite-sum induction verifies that baseline. The equality and strict-maximality cases follow from an integer-product comparison. Exhaustive exact arithmetic passed 194 assertions on 293,194 matching instances. It is finite corroboration, not an infinite proof.

## Originality — PASS, with explicit priority risk

Flajolet–Noy (2000), inspected on the original report's crossings theorem and subsequent moment analysis, gives unconditioned moments. Acan (2015), inspected in its arXiv full-text section 2 and related sections, gives the fixed chord's degree moments, but not its covariance with the residual crossing count. The first-moment formula is not claimed as original: the new statement is the *conditional total crossing variance* and the strict sharp arc-size extremum, which neither inspected result implies without the missing joint covariance calculation. Pilaud–Rué (2013) is relevant through a crossing-count generating-function framework, but a full-text priority comparison was unavailable; indirect prior coverage remains a risk. Targeted research-record searches and the available previous claims revealed no direct formulation, but searches cannot prove global uniqueness.

## Mathematical value — PASS

The total crossing count is the canonical global edge count of the random intersection graph of a chord diagram. Conditioning on one specific local edge is a natural structural perturbation; the result quantifies an exact, strict, shape-dependent increase in its fluctuation, not merely the already-known degree variance. It reveals that the normally hidden covariance between the global residual crossings and the chosen chord degree is nonnegative and gives a sharp extremal classification. The maximal additional variance is of order \(n^2\), even though the unconditioned variance is of order \(n^3\). This provides a usable exact conditional second moment for rooted-edge models and validates/limits approximations treating the chord's degree as independent of other crossings.

## Residual limitations

Priority risk persists for historical refined crossing enumerators or formulations of root-chord conditioned diagrams. Only unrestricted uniform pairings with one fixed edge are proved; no multiedge conditioning, full crossing distribution, or nonuniform law follows. The source-date metadata is taken from the March 4, 2000 date printed in the public INRIA report, not from a separate repository deposit log.

Self-review: passed. Independent audit: not yet performed.

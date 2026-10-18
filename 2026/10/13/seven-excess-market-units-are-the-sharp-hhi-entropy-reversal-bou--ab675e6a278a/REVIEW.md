# Independent mathematical audit

## correctness

PASS

Write n_i=1+y_i, y_i≥0, sum y_i=r; for fixed k and N=k+r, HHI numerator=k+2r+Q(y), Q=∑y_i², while Shannon entropy E=log N−(1/N)log W(y), W=∏(1+y_i)^(1+y_i). Zero excess coordinates do not alter either Q or W, so integer partitions of r cover every fixed k with at least the nonzero excess count. Independent exact-int enumeration of all partitions for 0≤r≤7 gives strict reversal counts [0,0,0,0,0,0,0,1], and tie splits first occur at r=6. At r=7 the unique pair is (3,4) versus (1,1,5); values Q=25<27 and W=800000>746496. Padding zero excess to any k≥3 proves the universal first-layer sharpness; for k=2 both indices are monotone in the larger share, so no reversal ever. This uses no floating logarithms.

## originality

PASS

The classic economics literature compares HHI and Shannon entropy and establishes different weighting/ordering behavior, but the directly inspected full review does not state a sharp positive-integer first-reversal threshold valid for every k≥3, the tie-only r=6 boundary, and uniqueness of the first reversal. The exact partition reduction is a bounded new threshold theorem, with an explicit residual risk of a previously published exercise.

## value

PASS

A sharp resolution threshold for disagreement between two widely used concentration indices is a natural exact finite invariant for same-size fixed-firm market profiles, not a purpose-built arbitrary slice. The theorem identifies a universal first strict reversal across every k≥3, proves no reversal through six excess units, distinguishes a penultimate tie layer and proves uniqueness at the first layer, making the fact suitable for rigorous index-comparison applications.

The dated certificate retains the supplied scientific assessment, sources and limitations.

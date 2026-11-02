# Scientific review

## Correctness

PASS. The lower direction uses explicit three-variable, rank-bounded interval formulas for all interior thresholds up to \(2^r-1\), and the upper direction uses an ordinary unlimited-pebble game with a recursively halved arc-cap invariant. The proof covers repeated selections, the two initial anchors, equality and cyclic orientation, and the ranks \(0\) through \(2\). Two standard-library programs verify distinct finite consequences and recompute their recorded outputs, but the infinite claim rests on the induction, not on these experiments.

## Originality

PASS, with historical-priority qualifications. Spencer–St. John (doi:10.37236/1616), section 3, considers very sparse random circular bit sequences and gives logarithmic tenacity bounds; the inspected material does not state an exact uncoloured cyclic-order rank spectrum or the rank-preserving three-variable conclusion. Siders (doi:10.1016/j.ic.2009.11.006), Immerman's chapter 6 and the underlying Immerman–Kozen result concern linear orders, not the ternary circular signature. Previously published mathematical findings concern exact rank thresholds for directed paths and one-red linear orders; related prior results address successor-marked cycles and strict betweenness. Their relations are different; their results do not imply the present equivalence by a quantifier-rank-preserving interpretation. A stronger undocumented circular-order normal-form result could subsume the finding; the Siders full text was not obtained, although its published abstract was inspected.

## Mathematical value

PASS. The object is the standard ternary cyclic order, the size parameter is a natural measure of its finite approximation, and the sharp cutoff gives a complete hierarchy of rank types for every quantifier depth. The rank-preserving equality of \(\mathrm{FO}^3\) with unrestricted first-order sentence equivalence, against unrestricted-depth blindness of \(\mathrm{FO}^2\), explains the precise interaction between arity, variable resources and circular interval splitting. The exact class count and least distinguishing rank are not arbitrary finite samples.

## Boundaries

The result assumes strict, total, uncoloured oriented cyclic orders, with no constants, successor or counting. A full historical-priority determination and independent mathematical review have not been performed.

Self-review: passed. Independent audit: not yet performed.

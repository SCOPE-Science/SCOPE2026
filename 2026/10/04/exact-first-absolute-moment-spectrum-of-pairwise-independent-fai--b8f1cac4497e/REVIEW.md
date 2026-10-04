# Review

## Correctness

PASS. Pairwise independence fixes
\[
\mathbb E S=0,\qquad \mathbb E S^2=n.
\]
The absolute sum lies on one parity lattice. The lower bounds are exact affine minorants of \(r\) in the variable \(r^2\), while the upper bound is the affine majorant through the two consecutive parity-compatible magnitudes bracketing \(\sqrt n\). Equality supports follow algebraically.

Attainability is explicit: the proof symmetrizes the signed sum, converts it to \(K=(n+S)/2\), and uniformizes over Hamming slices. The exact first two factorial moments give the product two-coordinate marginals required for pairwise independence.

## Originality

PASS, with a residual elementary-literature risk. The full 2014 Pass--Spektor preprint was inspected. Its sharp equal-weight pairwise theorem treats absolute moments with exponent \(p\ge2\) and identifies the zero/unanimous construction as an upper-moment maximizer. It does not treat the \(p=1\) lower Khintchine problem, the parity-lattice upper first-moment envelope, or the complete attainable interval.

The later full revised treatment was also inspected. It formulates classical Khintchine inequalities for all positive exponents, but its limited-independence sharp theorem remains in the regime \(p\ge2\).

Targeted searches for first absolute moment, lower Khintchine inequalities, exchangeable pairwise-independent signs, and exact absolute-sum ranges did not return an equivalent formula.

## Value

PASS. The first absolute moment is the endpoint of the lower Khintchine problem. The result shows a qualitative collapse invisible from the fixed second moment: under pairwise independence, equal-weight sums can have normalized first absolute moment tending to zero, while another admissible law has normalized first absolute moment tending to one. The exact finite-length parity correction and complete interval distinguish the theorem from a single counterexample.

Same-model review: passed. Independent audit: not yet performed.


Replay: `VERIFY_OK pointwise_checks=12509998 construction_checks=9998 extreme_pair_checks=299 feasible_pair_laws=151864`.

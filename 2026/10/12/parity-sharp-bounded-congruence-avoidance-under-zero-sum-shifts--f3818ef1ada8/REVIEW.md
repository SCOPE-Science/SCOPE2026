# Self-review

## Correctness
PASS. The proof reduces the original congruences to one forbidden residue per coordinate using \(Q^{-1}\). Even \(m\) is handled by zero-sum pairs in \(\{-1,0,1\}\). Odd \(m\) reduces to one three-coordinate block: for \(\ell\ge5\), the \(19\) zero-sum triples in \([-2,2]^3\) outnumber the at most \(15\) triples removed by three forbidden coordinate slices; for \(\ell=3\), two-element allowed residue sets give a zero-sum residue triple and an explicit representative replacement turns any canonical sum \(\pm3\) into zero. The lower bounds are exact: radius \(0\) is impossible for the all-zero forbidden profile, and radius \(1\) is impossible for odd \(m\) by parity. The finite-set consequences follow from the same zero-sum selection and the triangle inequality. The attached exhaustive verifier corroborates the local cases but is not used to infer the universal statement.

## Originality
PASS. Chen's Lemma 2.2 states the same avoidance task with \(|t_i|\le m+1\) and derives factors \(2m+3\) and \(m(m+1)Q\); Lemma 2.8(ii) propagates those constants. The printed proof can produce a shift of magnitude \(m\), so the source does not already contain the parity-sharp radius as a hidden stated consequence. Searches of the source, a constructional predecessor, published mathematical findings, and broad web literature did not locate an equivalent or stronger bounded-integer-lift theorem. Classical prime-field sumset results do not imply the exact bounded integer representatives with zero integer sum.

Residual risk: because the lemma is elementary, an equivalent result could exist under different terminology. No decisive covering source was found.

## Value
PASS. The smallest uniform radius is a natural invariant of the recent perturbation mechanism, not an arbitrary parameter slice. Determining it exactly collapses a radius growing with \(m\) to \(1\) or \(2\), with corresponding direct finite-set overhead \(3\) or \(5\) and displacement \(mQ\) or \(2mQ\). The parity obstruction gives a structural boundary. The result does not change the motivating paper's exponent range by itself, but it materially sharpens a reusable quantitative lemma and the constants it feeds into.

Self-review: passed. Independent audit: not yet performed.

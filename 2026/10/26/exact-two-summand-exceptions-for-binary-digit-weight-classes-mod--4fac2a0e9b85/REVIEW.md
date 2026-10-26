# Self-review

## Correctness — PASS
The claim is proved by a full finite-state equivalence between (a) a precisely defined binary-addition nondeterministic automaton with carry and the two summand digit-weight residues and (b) explicit reverse-binary regular languages for three exceptional-set formulas. The 18 source states and residue tracker exhaust the exact arithmetic of two nonnegative summands. All possible reachable paired automaton states are processed; the three exhaustive counts are 108, 108 and 107. The last-bit-canonical representation condition and zero are checked separately. A second direct enumeration for integers through 10,000 corroborates the independent regular-language formulas but is not substituted for the infinite certificate. No unrestricted higher-summand assertion is made.

## Originality — PASS within inspected evidence
The closest primary paper, Allouche–Shallit (arXiv:2112.13627, v3, full 14-page preprint inspected), gives two-summand representation functions and higher-summand behavior for digit-weight **parity** classes; its finite-automaton generality establishes computability for other automatic sets but not the stated explicit exceptional families for modulo three. Shallit (arXiv:2103.10904, complete HTML text inspected) computes Frobenius invariants of *tails* of several automatic sequences, a different invariant. Public mathematical-record searches for weight-residue additive exceptions, repunit and shifted-repunit families and related sequence tables did not locate the same claim. Closest accessible published comparison on binary digit weight classifies **products** with prescribed weights, not two-term additive sums. Prioritization remains conditional on incomplete indexing and possible implicit earlier automata calculations.

## Mathematical value — PASS
For three natural automatic subsets of the nonnegative integers, this determines the exact obstruction to representation by at most two same-class summands, including infinite lacunary exceptions and sharp logarithmic counting laws. The statement goes beyond decidability or finite samples and is naturally motivated by the existing additive-representation literature. It does not claim an unmotivated isolated parameter or a general theorem for all digital classes.

## Residual limits
Possible unindexed earlier equivalent formulas or an indirect extraction from a broader precomputed automaton remain risks. The exhaustive finite-state proof and accompanying checker are not an independently audited formalized certificate.

Self-review: passed. Independent audit: not yet performed.

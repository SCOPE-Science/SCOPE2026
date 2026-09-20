# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The multinomial mode is the Jefferson--D'Hondt allocation by Elezović's theorem. Under rational independence, Janson's Theorem 3.7 applies to the same allocation sequence with uniform randomization of the house size, which is exactly Cesàro averaging. Jefferson seat excesses are deterministically bounded, so weak convergence of the displacement vector implies convergence of every fixed polynomial moment. Elezović's log coefficient is polynomial in those bounded displacements.

The main algebra was checked separately. Janson's marginal Jefferson limit is a constant plus one centered uniform of coefficient one and \(n-2\) centered uniforms of coefficient \(p_i\). Combining its moment-generating function with the Bernoulli-polynomial generating function gives
\[
e^w\bigl((e^w-1)/w\bigr)^{n-2},\qquad w=p_i z.
\]
Thus \(\mathbb E B_{k+1}(\Xi_i+1)\) carries the factor \(p_i^{k+1}\), which cancels Elezović's \(p_i^{-k}\) weight after summing because \(\sum_i p_i=1\). The remaining coefficient extraction agrees with the standard exponential generating function for Stirling numbers of the second kind. Low-order exact values and a direct Jefferson-sequence computation are included in the verification artifact.

The rational-independence conditions used by the two sources agree under \(\sum_i p_i=1\): an integer relation \(v\cdot p\in\mathbb Z\) can be converted to a homogeneous rational relation by subtracting the corresponding multiple of \((1,\ldots,1)\), and conversely.

## Originality

**PASS, to the best of our knowledge.** Elezović explicitly states that whether its Cesàro results survive passage to an on-slice reference such as the mode is open, and says that treatment of on-slice averages requires a genuinely different computation. Janson gives the fixed-\(p\) Jefferson displacement limit that makes this computation possible, but predates the multinomial all-orders coefficient formula and does not state the Bernoulli--Stirling cancellation proved here.

Searches covered the exact source paper, multinomial-mode/local-expansion terminology, Jefferson and D'Hondt rounding, Cesàro averages, Bernoulli-polynomial formulations, Stirling-number formulations, and older apportionment goodness-of-fit literature. No prior statement of the all-orders modal log-coefficient average or its probability-vector-independent Bernoulli--Stirling formula was found.

The closest older literature is the rounding-discrepancy and goodness-of-fit work of Heinrich--Pukelsheim--Schwingenschlögl (2004--2005), Heinrich--Schwingenschlögl (2006), and related references surveyed by Janson. These papers establish powerful limiting-law machinery for particular apportionment functionals; they are prior art for that machinery, not for the connection to Elezović's later coefficient family. The 2005 paper was inspected in full-text form. The 2006 Metrika paper was inspected through its abstract and available full-text excerpts but not exhaustively line by line; it is the most plausible residual literature risk. Because it predates the 2026 multinomial expansion, any overlap would most plausibly be an equivalent general polynomial-functional result rather than the same coefficient interpretation or Bernoulli--Stirling formula.

## Value

**PASS.** The result directly closes a question isolated in a recent probability paper and does so to all logarithmic orders rather than only for the first correction. The cancellation is structurally informative: although each modal displacement distribution depends on \(p_i\), the weighted Bernoulli moment contributing to each \(c_k\) has exactly one surviving factor \(p_i\), forcing universality after summation. The polynomial-transfer statement also supplies a systematic route to every fixed multiplicative coefficient.

## Limitations

The result assumes fixed dimension and rationally independent probabilities. It is a Cesàro theorem in \(N\), not a pointwise asymptotic for the oscillating coefficients, and no convergence rate is proved. Multiplicative Bell-polynomial coefficients have limits through the joint law but are not claimed to share the universal closed form of individual log coefficients. Independent audit has not been performed.

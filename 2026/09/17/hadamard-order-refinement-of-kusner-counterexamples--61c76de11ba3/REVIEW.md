# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The extension from Walsh matrices to an arbitrary normalized Hadamard matrix was checked against the four distance cases in Xiong's construction.

The required combinatorial facts are exactly:

- distinct rows of an order-\(m\) Hadamard matrix agree in \(m/2\) positions and differ in \(m/2\);
- distinct rows of \(K\otimes H\), of order \(4m\), differ in \(2m\) positions;
- normalization makes the distinguished column of \(H\) constant, so for equal \(i\) none of the four distinguished columns contributes a difference;
- for unequal \(i\), the \(4\times4\) character matrix contributes exactly two distinguished-column differences, with the same one-versus-two split among the two retained weighted coordinates as in Xiong's original cases.

With these counts, the distance formulas reduce to the same scalar constraint
\[
2A-B=2^{p-1}R(1+1/m).
\]
The intermediate-value argument requires only \(m>1/\Delta(p)\), not \(m=2^k\).

The endpoint identity
\[
\Phi_4(a)-1=-\frac{3(a^2-2)^2}{4(a^4+2)}
\]
and the derivative
\[
\Delta'(4)=\sqrt2\log(1+\sqrt2)-\frac74\log2
\]
were algebraically checked. The lower bound is a direct contrapositive use of Swanepoel's Corollary 1.4.

## Originality

**PASS, to the best of our knowledge.** The following coverage was checked:

- Xiong's arXiv:2609.14794, including the full construction, all four distance cases, and the existence argument;
- Swanepoel's 2014 quantitative stability result near \(p=4\);
- Swanepoel--Villa's 2013 Hadamard-matrix construction and their asymptotic-density lemma for Hadamard orders;
- recent and synonymous searches around Kusner counterexamples, Hadamard orders, the \(8m-2\) construction, first/smallest counterexample dimension, and near-\(4\) quantitative bounds;
- current SCOPE records under the same objects, source paper, and equivalent terminology.

No matching statement was found that extends Xiong's \(p>4\) construction from powers of two to arbitrary Hadamard orders or derives the displayed two-sided asymptotic bounds for \(d_*(4+\delta)\).

The Hadamard-density technique is explicitly **not** claimed as new: Swanepoel and Villa used it for a different \(p<2\) equilateral-set problem. The new point is its compatibility with Xiong's specific \(p>4\) construction.

Residual originality risk is elevated because arXiv:2609.14794 is very recent; an unpublished follow-up, comment, or revision could contain the same observation. No specific inaccessible paper was identified that is especially likely to contain this refinement.

## Value

**PASS.** The result converts Xiong's qualitative existence theorem into a quantitative near-threshold statement, identifies a reusable design-theoretic generalization of the construction, and halves the leading upper constant compared with the immediate power-of-two rounding. Together with the known \(p=4\) stability theorem, it localizes the first failure dimension within a logarithmic factor.

## Limitations

The true asymptotic order of \(d_*(4+\delta)\) remains open between the lower scale \(1/(\delta\log(1/\delta))\) and the upper scale \(1/\delta\). No independent validation or formal verification is asserted.

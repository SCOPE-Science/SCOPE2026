# Review

## Correctness

**PASS.** The arbitrary-Hadamard extension uses only two properties of the Walsh matrices appearing in the original construction: pairwise row orthogonality and a normalized constant column. Replacing the order-\(m\) Walsh matrix by any normalized Hadamard matrix \(H\), and the order-\(4m\) matrix by \(H_4\otimes H\), preserves every agreement/disagreement count in the four distance cases. The resulting distance equations reduce exactly to
\[
2A-B=2^{p-1}R(1+1/m).
\]

The near-\(4\) expansion is checked from the exact identity
\[
\Phi_4(a)=1-\frac{3(a^2-2)^2}{4(a^4+2)},
\]
whose unique global maximum is nondegenerate at \(a=\sqrt2\). Standard smooth perturbation of this maximum gives the envelope expansion, and direct differentiation gives
\[
c=\sqrt2\log(1+\sqrt2)-\frac74\log2>0.
\]
The Paley/PNT step supplies Hadamard orders with relative spacing \(1+o(1)\). The lower bound is a direct inversion of Swanepoel's published stability inequality.

No empirical calculation is used as a substitute for a proof.

## Originality

**PASS, to the best of our knowledge.** The primary September 2026 paper was inspected through its theorem, construction, and existence proof. It fixes \(m=2^k\) and obtains existence for sufficiently large \(m\); it does not state the arbitrary-Hadamard extension, optimize the parameter excess, derive the \(p\downarrow4\) asymptotic constant, or combine the construction with the fixed-dimension stability theorem to bound the first failure dimension.

Swanepoel's 2014 paper gives the explicit stability interval around \(p=4\), but predates the \(p>4\) counterexamples. Chalmers' 2026 counterexample concerns \(p=5\) and an unspecified neighborhood of \(5\). Searches using the source paper, author name, Kusner counterexamples, Hadamard/Paley orders, dimension bounds, and \(p-4\) asymptotics did not locate an equivalent result.

The all-\(p>4\) source is only days old, so unindexed or unpublished parallel work is the main residual originality risk.

## Value

**PASS.** The result converts qualitative existence just above the sharp boundary \(p=4\) into an explicit asymptotic dimension scale. It also identifies the exact first-order obstruction inside the construction and removes the factor-of-two oscillation caused by restricting to powers of two. The combination with the known stability theorem leaves only a logarithmic gap for the true first failure dimension.

## Limitations

The true asymptotic behavior of \(N(4+\varepsilon)\) is not determined. The coefficient \(8/c\) is optimal only within the Hadamard refinement of Xiong's construction. No claim is made that Hadamard matrices exist at every admissible order.

Same-model review: passed. Cross-model review: not yet performed.

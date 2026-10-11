# Review of the common-source joint numerical-radius theorem

## Correctness — PASS

The tuple norm reduces exactly to the Frobenius norm of the output synthesis map. Averaging evaluations at symmetric test vectors yields the sharp lower bound in terms of the largest singular value; rank at most \(\min\{k,m-1\}\) gives the dimension barrier. A separate nonperpendicular perturbation argument settles the delicate single-singular-value equality case; exact orthogonal-source evaluation constructs witnesses in every dimension and proves necessity/sufficiency. The standalone checker tests 70 dimension/tuple-size witnesses and 1680 randomized Gram inequalities. Its finite tests do not substitute for the analytic proof.

## Originality — PASS with stated residual risk

Mal, arXiv:2212.06500v1 / *Operators and Matrices* (2023), Theorem 3.11(i), proves the complex Hilbert **unrestricted** joint index only for \(k<m\), by a common-source construction. Its proof does not classify the minimizing common-source tuples, determine their sharp ratio when \(k\ge m\), or give a spectral defect. The range \(k<m\) agrees with known work and is not counted as the novelty. Grover–Singla, arXiv:2201.03055v1, gives subdifferential and Birkhoff–James characterizations instead, without this rank-limited spectral extremum. The original construction is credited by Mal to Drnovšek–Müller (2014), whose full text was unavailable; it remains a significant equivalence risk, not a source declared to be noncovering.

## Mathematical value — PASS

The class is not an arbitrary coordinate slice: it is exactly the rank-one construction used to attain the source paper's complex Hilbert bound. Determining its sharp behavior after the ambient perpendicular dimension saturates fills a natural parameter regime and completely identifies extremizing output geometry: orthogonal systems below the threshold, tight frames above it. The sharp spectral-defect identity makes near-extremizers quantitatively near equal-singular-value frames. This restricted result does not determine the unrestricted finite-dimensional Hilbert joint index above threshold.

Same-model review: passed. Independent audit: not yet performed.

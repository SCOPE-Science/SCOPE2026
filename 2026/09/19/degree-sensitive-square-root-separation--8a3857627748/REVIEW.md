# Review

## Scientific assessment

The result replaces the formal full sign cube in the recent explicit square-root separation argument by the actual Galois conjugates of the imaginary multiquadratic field. The resulting lower bound depends on the degree
\[
D=[\mathbb Q(\sqrt{-a_i}:m_i\ne0):\mathbb Q]
\]
and has coefficient exponent \(D/2-1\).

### Correctness: PASS

The proof was checked against the following points.

- Distinct square-free parts imply the active square roots are rationally independent, so the algebraic integer \(\gamma=\sum m_i\sqrt{-a_i}\) is nonzero and its field norm is a nonzero integer.
- The Galois characters attached to distinct negative square classes are distinct and nontrivial. Their character orthogonality gives exactly \(\sum_\sigma|\sigma\gamma|^2=D\sum m_i^2a_i\).
- Complex conjugation flips every imaginary radical, so the identity and conjugation terms both have absolute value \(\Lambda\). There can be no odd-parity squareclass relation among negative positive-radicand generators; equivalently, this conjugation element is well defined in the Galois group.
- AM--GM on the remaining \(D-2\) squared conjugate magnitudes gives the displayed inequality with exponent \((D-2)/4\). For full negative-squareclass rank \(D=2^k\), the formula reduces exactly to the first inequality of Aymone--Figueredo--Táfula.
- In the complete multiquadratic basis on \(r\) primes, adjoining \(i\) raises the real degree \(K=2^r\) to \(D=2K\), yielding coefficient exponent \(K-1\). A standard pigeonhole linear-form approximation gives the matching upper exponent for fixed radicands.
- The compact verification artifact independently checks the rank table, the exact norm and numerical bounds in the \(\{1,2,3,6\}\) example, and all 2400 nonzero coefficient vectors in \([-3,3]^4\) for that example.

No hidden positivity, primitivity, or coprimality condition on the coefficients is used. Zero coefficients are handled by restricting the main theorem to the active support; the complete-basis corollary may equivalently use the full ambient multiquadratic field.

### Originality: PASS, to the best of our knowledge

The full current arXiv text of Aymone--Figueredo--Táfula (arXiv:2609.14161v1) was inspected. Their theorem uses all \(2^K\) sign choices and does not state a refinement in terms of the actual multiquadratic field degree, negative-squareclass rank, or the optimal complete-basis exponent \(K-1\).

Burnikel--Fleischer--Mehlhorn--Schirra (2000) is important prior context: the literature already recognizes that algebraic dependence and overestimation of algebraic degree can weaken generic separation bounds. That general principle is therefore not claimed as new. No inspected source gave the explicit bound
\[
\Lambda\ge\left(\frac{D}{D-2}Q\right)^{-(D-2)/4}
\]
or the complete-multiquadratic-basis specialization with exponent \(K-1\).

Eisenbrand--Haeberle--Singer (2024) gives, for fixed radicands, a singly exponential coefficient bound via the Subspace Theorem with a positive radicand-dependent ineffective constant. It does not supply the present explicit field-degree formula.

Dubickas (2024), DOI 10.1016/j.jco.2024.101866, is the most relevant residual source risk. Its full text was not inspected. Bibliographic/abstract metadata were inspected, and the 2026 Aymone--Figueredo--Táfula paper explicitly describes Dubickas as using the idea of isolating a \(\Lambda^2\) factor in a product argument. Because that technique is close to the present proof, overlap inside the uninspected full text cannot be completely excluded. Searches using square-root separation, multiquadratic degree, squareclass rank, Galois norm, dependent radicals, and equivalent formulations did not identify the stated degree-sensitive theorem.

The motivating preprint is recent, so unindexed contemporaneous work remains an additional residual risk.

### Value: PASS

The improvement is structural rather than a small constant change. In dependent squareclass families the exponent is governed by the true multiquadratic degree. For the natural complete basis of a degree-\(K\) real multiquadratic field, the recent uniform exponent \(2^{K-1}-1\) becomes \(K-1\), and this exponent is optimal for fixed radicands. The rank parameter is elementary to compute by binary linear algebra on prime-parity vectors.

## Limitations

The theorem gives no improvement when the active negative square classes have full rank. It does not resolve general Sum-of-Square-Roots decision complexity, does not optimize the multiplicative constant in the fixed-basis optimality statement, and does not claim novelty for the general observation that algebraic dependence lowers effective degree. Numerical checks are supporting evidence only.

Same-model review: passed. Independent audit: not yet performed.

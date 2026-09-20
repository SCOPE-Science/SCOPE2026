# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The degree-four and degree-five Gegenbauer factorizations follow directly from the standard finite-sum formula and reduce the largest-zero problem to explicit quadratics in \(x^2\). Substitution gives the displayed formulas for \(z_{4,1}^2\) and \(z_{5,1}^2\), hence the factorizations \(F_{n,d}^2=A_nB_{n,d}\).

For the positive ranges, each rational factor \((s+a)/(s+b)\) with \(0\le a\le b\) is a Pick function nonnegative on \((0,\infty)\), hence complete Bernstein. The closure of complete Bernstein functions under fractional powers, positive affine combinations, and geometric means then proves sufficiency through \(d=3\) for \(n=4\) and through \(d=4\) for \(n=5\).

For necessity, if the numerator shift of \(B_{n,d}\) exceeds its denominator shift, the Möbius factor maps the upper half-plane to the lower half-plane. On the open real interval between its zero and pole, \(A_n\) has a positive real boundary value whereas \(B_{n,d}\) is negative and approached from below. Thus the positive-axis square-root branch acquires negative imaginary part immediately above that interval, contradicting the Pick characterisation of complete Bernstein functions. The lower endpoint \(d=1/2\) is forced by nonnegativity on \((0,\infty)\).

At the two maximal scales, Stieltjes inversion applied to the explicit boundary values yields the stated positive densities. Their support and endpoint behavior are consistent with the algebraic branch cuts. The accompanying symbolic/numerical verification reproduces the polynomial factorizations and zero formulas and checks both integral representations at three positive values to high precision.

## Originality

**PASS, to the best of our knowledge.** The directly relevant source, arXiv:2609.19186, was inspected at its complete-Bernstein characterisation, general square-root results, Appendix A threshold statements, and low-degree remarks. Its Appendix gives an exact threshold for nonlargest zeros, gives only a sufficient largest-zero range \(1/2\le d\le\lceil n/2\rceil\) for \(n\ge4\), and separately resolves \(n=2,3\). It does not state the exact \(n=4,5\) largest-zero thresholds \(3,4\) or the compact endpoint measures recorded here.

Searches using the source identifier and combinations of the exact low-degree formulas, largest ultraspherical/Gegenbauer zeros, complete Bernstein functions, Pick functions, operator monotonicity, and the endpoint scales found no equivalent result. Older literature on ultraspherical-zero monotonicity is relevant background but no located statement supplies the exact complete-Bernstein thresholds above. Residual risk remains because the source is recent and the low-degree formulas are elementary enough that an equivalent observation may exist under different terminology. No inaccessible source supplied concrete evidence of prior coverage.

## Value

**PASS.** The result closes the first two cases left open by the source's nonoptimal largest-zero sufficient bound and shows that this bound is already genuinely improvable in degrees four and five. The proof identifies a simple structural mechanism: the exact threshold is the point at which a Möbius factor stops preserving the upper half-plane. At the endpoint, cancellation exposes explicit compactly supported representing measures, giving more information than threshold membership alone.

## Limitations

Only degrees four and five are resolved here. The data for degrees two through five suggest the possible pattern \(d_{\max}=n-1\), but no theorem or conjectural certainty for \(n\ge6\) is asserted. The work does not classify other scale functions, other orthogonal-polynomial families, or the nonlargest-zero case beyond what is already known. Originality is to the best of our knowledge. No independent validation, independent audit, or formal proof-assistant verification is asserted.

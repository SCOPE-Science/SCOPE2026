# Review of A universal quantum-integer denominator for fixed-degree descendant series

## Correctness
**PASS.** Corollary 3.9 expresses each fixed-degree coefficient as a finite sum over partitions \(k\vdash p\). The refined tropical factor is Laurent-polynomial in \(q^{1/2}\), while every non-polynomial factor is an inverse quantum integer \([\ell]_q^{-k_{\ell j}}\). The partition identity \(\sum_\ell \ell k_{\ell j}=p_j\) gives \(k_{\ell j}\le\lfloor p_j/\ell\rfloor\), so \(D_p(q)\) clears all denominators. Theorem A then identifies the fixed-degree coefficient with \(F_p(u)\) after \(q=e^{iu}\). The root-of-unity pole bound follows from the simple zeros of \([\ell]_q\).

The bundled checker verifies the partition-exponent maximization for all \(p_j\le12\) and several multi-index vectors. This is only a consistency check; the universal proof is the inequality above.

## Originality
**PASS.** The initiating paper remarks that the answer has rationality properties, but full-text searches found no statement of a universal fixed-degree quantum-integer denominator, no root-of-unity pole envelope, and no componentwise exponent \(\sum_j\lfloor p_j/\ell\rfloor\). published-finding corpus searches for these formulations returned explicit toric refined-curve computations as the closest hits, not an implication of this statement. The current and prior owned ledgers contain no overlapping claim.

The closest earlier literature is the toric refined descendant correspondence and Bousseau's q-deformed mirror construction. The toric series is Laurent-polynomial and lacks the non-toric partition denominators. Bousseau's checked abstract-level material does not state the present degree-vector bound; a deeper implicit formulation remains a residual risk.

## Value
**PASS.** The result gives an effective denominator before any tropical-curve enumeration. It therefore constrains every fixed-degree all-genus series uniformly and identifies exactly which roots of unity can support poles, with an explicit order bound determined solely by \(p\). This is useful both as an arithmetic/analytic invariant and as a consistency check for future computations.

## Closest literature and limitations
The initiating source is Patrick Kennedy-Hunt, Qaasim Shafi, and Ajith Urundolil Kumaran, “Refined curve counting with descendants and quantum mirrors,” arXiv:2502.17236, published in Épijournal de Géométrie Algébrique 10 (2026). The earlier toric reference is their “Tropical Refined Curve Counting with Descendants,” Communications in Mathematical Physics 405 (2024), 240. The broader quantum-mirror framework is Pierrick Bousseau, Compositio Mathematica 156 (2020), 360--411.

The denominator here is not asserted to be reduced or optimal after summation. Pole bounds may be strict because of cancellations.

Self-review: passed. Independent audit: not yet performed.

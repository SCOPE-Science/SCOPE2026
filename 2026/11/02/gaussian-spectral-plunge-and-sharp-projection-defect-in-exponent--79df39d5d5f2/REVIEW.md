# Scientific review

## Correctness — PASS

The exact eigenvalue law follows from radial monomial orthogonality and the degree multiplicity. The phase \(U(y)=c(1-e^{-y})^{-\gamma}\) has positive curvature, and its Taylor expansion at the exact cutoff center produces the normal distribution for every bounded scaled degree. Crucially, the two exponential-tilting comparisons in the proof control the entire unbounded degree tails, so the trace coefficient is not inferred from finite sampling. The Gaussian integral coefficient is computed exactly by a two-normal expectation, and the binomial identity supplies the counting function. A standalone script gives supplementary six-case quadrature checks. Risks: independent checking of the infinite-dimensional argument and possible hidden normalization conventions; the proof has spelled out its own normalization.

## Originality — PASS, subject to historical priority

Cho–Lee–Park (arXiv:2207.13937, §4.2) prove boundedness and compactness criteria on the specific exponentially weighted Bergman ball but not sharp spectral plunge data. Zelditch–Zhou (arXiv:1708.09267) and Hedenmalm–Wennman (arXiv:1805.00854) establish Gaussian interfaces in different semiclassical Bergman settings; those results do not directly imply the present fixed-singular-weight/shrinking-indicator defect trace or its dimensional coefficient. The 2026 work of Marceca and collaborators provides general spectral-deviation bounds, rather than the exact constant here. Comparisons against accessible historical mathematical claims and public mathematical-record searches found no statement or direct implication matching the fixed singular-weight formula. Search absence alone is not novelty proof; further historical overlap is possible, particularly through a general boundary-limit theorem adapted to singular weights.

## Mathematical value — PASS

The cutoff has effective rank of order \(\varepsilon^{-d(\gamma+1)}\), yet the sharply smaller defect has order \(\varepsilon^{-(\gamma+1)(d-1)-(\gamma+2)/2}\). The proof identifies the exact number of boundary modes, a universal Gaussian transition, the full weighted counting correction, and the dimension-dependent trace coefficient in one natural spectral family. This makes a quantitative reference case for sharply decaying Bergman weights and discontinuous Toeplitz localization; it is not a mere single-mode integral approximation. No unproved global nonradial consequence is claimed.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness — PASS

The partition polynomial follows by conditioning on the central spin. The explicit finite Blaschke product proves that all zeros are simple and on the unit circle; its strictly positive angular derivative handles roots at the circle's endpoints without a genericity assumption. The Cauchy logarithm argument proves an all-size, all-order exponential error bound with the stated quantifiers. Fourier uniqueness, uniform Poisson expansion, Hausdorff moment determinacy, and a uniform Taylor/derivative bound establish respectively the limiting density, inverse law, and edge spacing. Exact-rational and independent phase checks in `verify.py` reproduce crucial finite calculations. The infinite statements follow analytically, not from experiments.

## Originality — PASS (with residual risk)

Chio–He–Ji–Roeder, arXiv:1806.00403, Proposition 1.1, covers the homogeneous finite-star equation as a subcase of its Cayley-tree recursion, and the paper's main limit instead fixes branching and grows depth. Hou–Jiang–Newman, arXiv:2208.00917, considers motion of zeros as bonds change. Simon, arXiv:2111.00650, treats analytic zero-free consequences. Their results do not state, and without additional arguments do not imply, the coupled heterogeneous increasing-degree inverse theorem together with the quantified finite zero-moment relation. General finite-Blaschke and orthogonal-polynomial literature may nevertheless contain a broader theorem implying these particular conclusions; that is the principal remaining prior-art risk. Absence of a direct search match is not asserted as proof of originality.

## Value — PASS

This resolves an exact inverse thermodynamic question for a natural heterogeneous statistical-mechanical family: the asymptotic bond distribution is encoded uniquely by the Lee–Yang zero measure, while finite spectral information recovers its moments at an exponential error scale. The formula covers arbitrary deterministic variation of the bond strengths and supplies physical edge-zero scaling. This is a complete, motivated asymptotic classification for the stated geometry rather than a table of isolated numerical cases. It is not claimed to extend to all trees or to yield stable inversion of noisy high-order moments.

Self-review: passed. Independent audit: not yet performed.

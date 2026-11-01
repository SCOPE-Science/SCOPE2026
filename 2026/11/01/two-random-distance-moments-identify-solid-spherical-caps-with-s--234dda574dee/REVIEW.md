# Scientific review

## Correctness — PASS
The stated parameter domain \(R>0\), \(0<t\le2\) gives a genuine full-dimensional cap. The axial marginal and uniform-disk conditional moments yield exact finite polynomial integrals. Expanding the two independent-point distance moments, then substituting those integrals, produces the stated rational formulas. The derivative of the normalized ratio factors into polynomials with positive coefficients and a nonnegative quadratic endpoint factor. This proves strict identification on the entire open shape interval, includes the full-ball endpoint, and supplies both endpoint values. The cubic term at the ball and a uniform lower bound for the derivative divided by the squared distance to that endpoint prove the sharp inverse regularity. `cap_verify.py` independently checks algebra, quadrature and direct volume-pair simulation; Monte Carlo is corroboration, not a proof.

## Originality — PASS, subject to historical priority risk
Checked original literature concerns a different probability measure (surface spherical caps and angular distances), a different functional (mean ordinary distance per mean width), or general forward distance/moment identities without the exact two-even-moment spherical-cap inverse and sharp cubic-root endpoint. The most relevant inspected primary texts are arXiv:2007.07297, arXiv:2010.03351 and arXiv:math-ph/0201046. The closely related generic moments paper DOI:10.1063/1.3559719 was accessible at the abstract level but not in full; its general identity may reduce the novelty of forward moment evaluations, not demonstrably the global strict monotonicity and optimal inverse exponent. The historical claim remains provisional.

## Mathematical value — PASS
A solid spherical cap is a natural two-parameter convex body, while Euclidean distances between unlabeled uniform point pairs are natural stereological observations. The result gives the complete exact feasible range, an explicit constructive two-measurement inverse, a matching impossibility from one measurement, and a sharp stability boundary at spherical symmetry. The value rests on the complete inverse classification and precise conditioning, not on arithmetic formula evaluation alone.

## Limits and residual risks
The theorem does not estimate the moments from finitely many observations and makes no noise-robust statistical assertion. It is not an inverse result for a spherical surface, other rotational solids or caps in arbitrary dimension. General moment calculus predates the result, and an unlocated equivalent cap-specialization is still possible.

Self-review: passed. Independent audit: not yet performed.

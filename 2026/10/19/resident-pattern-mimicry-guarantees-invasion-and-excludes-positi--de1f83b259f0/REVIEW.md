# Mathematical assessment

## Correctness — PASS

The quantified domain is exactly the two-patch conservative migration model with positive \(P_1,P_2,d,e,m_1,m_2\), where \(Q\) is the resident-only positive equilibrium and \(Q_1/P_1\ne Q_2/P_2\). The scalar logistic equilibrium is unique by a scaling comparison and stable by an irreducible Metzler test. The invader-at-resident determinant is the strictly negative \(-a^2/(Q_1Q_2)\), independent of \(e>0\). At the invader-only equilibrium a strict ordering \(t_1>1>0\) and \(t_1>t_2\) yields a strictly positive resident-invasion determinant and negative trace. At coexistence, summing fluxes either forces proportional species and a contradiction, or forces a negative coefficient in \(m=\alpha P+\beta Q\). The witness is checked with exact rational arithmetic by `verify.py`. Positivity and all relevant boundary cases are accounted for; no global convergence assertion is made.

## Originality — PASS, with residual uncertainty

Braverman–Lawson (arXiv:2512.10898v1) raises exactly the question of whether matching a nonideal resident stationary profile ensures invasion with identical species resources, and explicitly identifies discrete analogues as a prospective research direction. Its Theorem 3.4 assumes a strict resource advantage and its numerical equal-resource example is not a quantified theorem. The two-patch resident-matching theorem derives a determinant identity valid for every positive invader dispersal rate and rules out interior equilibria.

Lou's earlier survey, especially its two-patch Theorem 2.3, is the closest structural result: it treats a different local logistic law with common intrinsic per-capita growth and patch-dependent carrying-capacity crowding, and is not claimed novel. Chen–Shi–Shuai–Wu (2022) give more general patch competition results under a common species dispersal matrix; that hypothesis does not hold here. The constant-intrinsic-rate subcase overlaps older ideal-free competition literature and is not independently novel. The claim is the all-parameter heterogeneous-rate, distinct-target classification, including the unequal-rate rational example. No inspected source or accessible mathematical-record hit provided the exact joint conclusion for that model. Qi–Su–Wang (2024) and Chen–Liu–Wu (2022) are additional plausible two-patch sources accessible only through abstracts; that limitation leaves a substantive residual equivalence risk.

## Mathematical value — PASS

This is a substantive finite-patch resolution of a recent published motivation, not a numerical example or a generic linearization exercise: it covers every positive invader movement intensity, identifies opposite transverse stability signs at the two boundary populations, and proves absence of positive coexistence equilibria. The determinant cancellation and conservation-based exclusion argument explain why stationary-profile targeting defeats a nonbalanced resident without any direct resource advantage. This gives a precise benchmark for directed dispersal and invasion modelling. The result does **not** imply global competitive exclusion for arbitrary positive initial populations, the original PDE conjecture, or conclusions for more than two patches.

## Closest literature, remaining limitations

Primary comparisons: Braverman and Lawson, arXiv:2512.10898v1, §§3.3 and 5; Y. Lou, *Ideal Free Distribution in Two Patches* (2019), §2 and Theorem 2.3; Chen, Shi, Shuai and Wu, *Global dynamics of a Lotka–Volterra competition patch model* (2022), equation (1.3) and assumptions (A1)–(A3). All are inspected for implication rather than just title matching. Further bibliographic verification may uncover a general theorem that subsumes this specialization. Only local dynamical stability and stationary exclusion are proved; independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.

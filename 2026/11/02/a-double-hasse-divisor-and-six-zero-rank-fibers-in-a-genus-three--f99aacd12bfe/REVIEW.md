# Self-review

## Correctness — PASS
The smoothness domain follows from the cubic discriminant of \(T^3+aT^2+bT+1\). The exact coefficient formula for the standard Hasse--Witt matrix yields determinant \(-2(ab+1)^2\); on its reduced divisor, the two-by-two block factors as a rank-one outer product. The twisted square is zero precisely at \(b^6=1\), and nonzero rank persists otherwise. All six roots are simple and avoid the discriminant. The marked Frobenius orbit and isomorphism analysis uses explicit changes of coordinates. The two packaged verifiers check exact polynomial identities and independently reproduce representative finite-field data. Risk: finite-field enumerations are corroborative only; the proof of the complete geometric locus depends on the displayed symbolic equalities and standard semilinear rank interpretation.

## Originality — PASS (best-knowledge; residual risk)
Novoselov 2019 (arXiv:1902.05992) treats the genus-three model \(y^2=x^7+A x^4+B x\), with a different monomial-support/autormorphism pattern; Ohashi--Kudo--Harashita 2021 (arXiv:2111.09777) treat nonhyperelliptic genus-three cyclic-order-six curves. Neither inspected treatment asserts the full rank stratification for the order-four hyperelliptic family here, and the latter's rank behavior does not imply the exceptional stable-rank-zero locus on a rank-one Hasse block. The exact and alias searches of mathematical research records, and claim-level comparison of accessible prior findings, located no dominating theorem. Risk: an unindexed earlier specialized hyperelliptic computation could cover all or part of this result, and the literature search is not a proof of novelty.

## Mathematical value — PASS
A complete two-parameter arithmetic stratification with a nonreduced Hasse divisor and a six-point deeper Frobenius-nilpotence locus gives structural geometry beyond an isolated curve or point count. It distinguishes Cartier rank from stable Frobenius rank and identifies precisely which smooth marked curves realize each possibility, including their Frobenius orbits and geometric isomorphisms. This is useful for studying automorphism subloci and nonordinary degeneration in positive-characteristic moduli. The result does not claim a new general Cartier algorithm or full Newton-polygon classification.

Self-review: passed. Independent audit: not yet performed.

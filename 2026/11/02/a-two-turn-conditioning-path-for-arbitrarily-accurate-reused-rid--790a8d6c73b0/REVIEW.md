# Independent mathematical audit

## correctness

PASS

From frozen RESULT.md: for G=diag(4,1), D=[[5,1/4],[1/4,2]], generalized Gram eigenvalues reduce K_t(lambda)^2 to the ratio (W+t sqrt(P)/2)/(W-t sqrt(P)/2). Independently verified P=37lambda^2-67lambda+40, negative discriminant -1431, positive denominator from D SPD, and exact derivative identity P'W-2PW'=-F_t. Descartes signs (+,-,-,+), F_t(1)=140>0, F_t(2)=-972-1431t<0 give exactly two simple positive roots, a min in (1,2), then max above 2; lambda infinity limit is 1. Explicit X realizes XA Gram H_t and distortion t||G^(-1/2)DG^(-1/2)||; continuity and full Gaussian support justify positive probability only. Independent sympy identity and roots for t=.01,.1,1,5 agree; not a quantitative high-probability claim.

## originality

PASS

Introduced partly exact reused-sketch Cholesky regularization and embedding conditioning bound; no two-turn specific spectral path implication found in relevant algorithm/bound sections. Numerical stability follow-up uses finite-precision objective rather than exact path-turn classification. Resultary semantic queries of published records performed with two tailored queries; no exact dominating result located, and this is not proof of priority. The listed primary sources were compared on mathematical implications; inaccessible relevant text retained as risk.

## value

PASS

An explicit rigorous counterexample to the tempting expectation that regularization makes the reused-sketch preconditioned condition number monotone/unimodal is a motivated structural boundary for iterative ridge solvers. Its arbitrarily small amplitude and merely positive Gaussian probability are explicitly bounded; not a practical instability guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Review of the sharp two-agent directed welfare interval

## Correctness — PASS

The hypotheses include positive cost coefficients, a positive unreciprocated payoff spillover satisfying \(g^2<\gamma_1\gamma_2\), and nonnegative nonzero incentives. Normalized private first-order conditions give the unique Nash profile; the planner's positive-definite Hessian gives a feasible unique optimum. Direct evaluation yields the welfare ratio and two nonnegative factorizations establishing a **complete sharp interval**, not just sampled upper or lower estimates. The separate boundary ray shows welfare becomes unbounded when \(g^2\ge\gamma_1\gamma_2\). The best-response matrix squares to zero. A standard-library exact-rational check was executed successfully on 945 positive-cost and incentive configurations. Universal quantifiers follow from the algebra, not the tests.

## Originality — PASS, with residual priority risk

Golub (arXiv:2502.12309, welfare discussion and open-questions passage) derives a price-of-anarchy bound after explicitly assuming homogeneous own effort costs and symmetric interactions. Iwanaga and Kobayashi (*Economics Letters* 260, 2026, Secs. 2–3) require undirected symmetric adjacency; neither result applies to a one-way response matrix. Rokade and collaborators (arXiv:2508.06619, Theorem 3.1, Remark 6 and Appendix 0.F) bound welfare of an \(\alpha\)-potential maximizer; for nonsymmetric graphs this need not be the actual Nash equilibrium. Chen, Chen and Lu (arXiv:1602.02527, abstract) address directed opinion formation rather than productive effort payoffs. Actual scientific searches included ``"nilpotent" "price of anarchy" "network game"``, ``"one-way" "price of anarchy" "quadratic" "welfare" network games`` and heterogeneous directed LQ welfare queries; no statement implying the sharp interval was located. The 2016 source was not inspected in full; the possibility of a subsuming more general asymmetric welfare theorem remains. Priority is provisional, not independently certified.

## Mathematical value — PASS

The finding addresses a specific highlighted welfare-theory gap for asymmetric response matrices and heterogeneous own costs. The result determines **every attainable inefficiency ratio** at fixed directed spillover strength; it is uniform over all nonnegative incentives, identifies both exact extremes and shows a failure of spectral-radius-only efficiency estimates even for two agents with positive production spillovers and strictly concave social welfare. It also gives a sharp feasibility boundary and minimal network order. An isolated counterexample would not provide these structural facts. No extension beyond the one-way two-person model is asserted.

## Verification and limits

`verify.py` reproduces exactly 945 rational parameter configurations and the stated \(t=3/5\) heterogeneous example. The proof is self-contained but uses only ordinary 2×2 quadratic analysis; finite tests are not exhaustive for continuous parameters. No historical-priority or scientific assessment independent of the present review has been carried out. There is no assertion about arbitrary directed networks, dynamic learning, negative incentives or other welfare functionals.

Self-review: passed. Independent audit: not yet performed.

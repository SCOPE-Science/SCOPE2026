# Review of optimal one-sided \(p\)-moment concentration

## Correctness — PASS
The pointwise optimal exponential-remainder inequality follows from a strictly decreasing elasticity, with derivative sign certified by \(2\cosh u>2+u^2\). The nonlinear moment-generating estimate follows from the published reverse-KL tensorization Proposition 3.4; its complete conditional-density/entropy-telescoping proof was inspected. Chernoff optimization yields the stated coefficient. For sharpness, additive Bernoulli deficits give exact binomial Cramér rates, and the special choice \(\kappa=e^{-u_p}\) forces the same coefficient. This argument handles \(p=2\) through a separate boundary limit. The 3,600 program checks supplement, rather than establish, these infinite statements.

## Originality — PASS, qualified
The closest motivating primary source, Eshima–Esposito–Paudice (arXiv:2610.21103v1), proves a weaker non-sharp coefficient; neither its theorem nor its detailed proof asserts optimality of the universal coefficient. The earlier Aminian inequality also uses the weaker coefficient and concerns empirical averages. Published record searches found related sharp binomial and moment inequalities but no same conditional-deficit nonlinear characterization. The result does not claim novelty of scalar differentiation or reverse-KL tensorization, only of the exact globally optimal concentration constant and sharp rare-event extremizers. The exact coverage of older one-sided probability literature remains a nonzero originality risk; the Aminian full text was not accessible in the attempted retrieval.

## Mathematical value — PASS
The constant is a natural minimax quantity needed to translate a conditional \(p\)-moment budget into a sharp uniform exponential confidence exponent. The bound is valid for nonlinear estimators and possibly infinite variance. The improvement is not uniformly small: for \(p=3/2\) the exponent constant rises from \(1/3\) to \(0.917935\ldots\), and the improvement factor diverges near \(p=1\). A binomial large-deviation obstruction proves no further universal coefficient improvement is possible under the same budget.

## Limitations and closest literature
The statement does not yield fixed-sample exact tail envelopes or two-sided concentration. The main nonlinear tensorization lemma is borrowed and attributed, not rediscovered. Closest works: arXiv:2610.21103v1, Aminian (PMLR 300, 2026), Pinelis (EJP 2016), Bakhshizadeh–Maleki–de la Peña (2023). Prior implicit equivalences remain possible. The scientific review is not independent replication.

Self-review: passed. Independent audit: not yet performed.

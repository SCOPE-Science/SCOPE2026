# Scientific review

## Correctness — PASS
The intervals of the reflected Zipf model have explicitly ordered branch and gap cells, so their conformal mass obeys the exact first-symbol decomposition (1). The two required Hurwitz-zeta tail expansions have controlled, uniform remainders for every fixed real \(q>1\) and \(qs>1\). Taylor expansion produces exactly \(c^s(Q_\lambda(a)-a)\), not only an order bound. At \(a=\lambda\) the coefficient is \(c^s(1-\lambda)>0\), proving sharpness. The quantitative Poisson claim follows by coupling with the independent first-symbol process: only one boundary cell can disagree, with probability \(O(m^{-1/(qs-1)})\), and the binomial approximation adds \(O(m^{-1})\). Finite numerical diagnostics in `verify_endpoint.py` check the formulas but are not substituted for the proofs.

## Originality — PASS under examined evidence
The shift coding, conformal measure, dimension equation, and exact Zipf branch arrangement are **known**, including in Cunha--Novaes--Ponce and the published Zipf alphabet-crossover record. The latter's complete scientific `RESULT.md` was compared: it addresses the limit \(q\downarrow1\) and finite-alphabet Hausdorff dimensions, not the fixed-parameter two-term conformal endpoint distribution or its nonconstant profile. Reeve's target-set dimension theorem and Freitas--Freitas--Todd's Poisson laws cover different conclusions; neither supplies this model's exact singular profile or rate. Generic Poissonity is not itself considered novel. Priority risk remains from other specialized countable-IFS local-scaling literature; the 1996 Mauldin--Urbański article was compared using abstract and citations but not its complete text.

## Value — PASS
The origin is the natural limit point of infinitely many geometric branches in the source problem. The sharp local dimension \(d<s\) quantitatively distinguishes accumulation-point mass from global fractal size; the next correction is nonconstant and reflects the entire Cantor distribution rather than an arbitrary scalar coefficient. Its exponent cannot be improved and controls the explicit finite-time rare-return approximation. This is a natural local geometric/dynamical invariant of the already-published Zipf family, not a relabeling of a generic pressure equation or a claim that Poisson laws are new.

## Scope and risks
All asymptotic constants fix \(q>1\) and \(0<\lambda<1\). Nonlinear return maps and other invariant measures are outside scope; the Poisson convergence-rate exponent need not be optimal. General recurrence/renewal literature may encode an equivalent form. No independent mathematical or bibliographic audit has been conducted.

Self-review: passed. Independent audit: not yet performed.

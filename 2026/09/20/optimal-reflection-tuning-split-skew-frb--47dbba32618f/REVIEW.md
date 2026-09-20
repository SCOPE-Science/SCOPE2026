# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** On the family \(A=\gamma LJ\), \(B=LJ\), the iteration reduces exactly to a scalar complex two-step recurrence.  The quadratic Schur--Cohn criterion gives a necessary-and-sufficient inequality, whose numerator factors into the displayed linear expression in \(\tau^2\).  The other Schur condition is either automatic or strictly weaker.  The resulting threshold specializes exactly to Shehu's published \(\theta=1\) formula.

The robust max--min calculation was checked adversarially at the endpoint cases \(\gamma=0\), \(\gamma=1/2\), the unconditional region \(\gamma\ge2\theta+1\), and the coefficient boundary \(\theta=1/2\).  Differentiating the exact threshold function identifies the two stationary points at the proposed optimizer; separate monotonicity bounds on \(h_\theta(0)\) and \(h_\theta(1/2)\) prove global optimality over \(\theta\), rather than only local optimality.  The public verification script independently computes characteristic roots, checks the phase classification on representative points, confirms the \(\theta=1\) reduction, and numerically scans the robust ceiling.

The interpretation is deliberately limited: the result is a sharp phase diagram for the split-skew linear test family and a necessary obstruction for universal guarantees.  It is not presented as a sufficient universal convergence theorem for all monotone inclusions.

## Originality

**PASS, to the best of our knowledge, with a material access caveat.** Shehu, arXiv:2609.18373, establishes the sharp universal constant for standard FRB and gives the exact \(\theta=1\) skew--rotation family.  Those results are explicitly treated as prior work and recovered as a consistency check, not claimed as new.

Ou, Themelis, and Latafat, arXiv:2609.15936, directly study constant reflection coefficients for FRB and state in the abstract that the tight admissible coefficient range consists of all coefficients greater than one half for sufficiently small step size.  Therefore the parameterized method itself and the threshold \(\theta>1/2\) are excluded from the novelty claim.  Only the abstract was available for inspection.  This is the most important unresolved originality risk: its full theorem/proof sections could contain a split-skew or sharp constant-step formula not exposed by the abstract.  The abstract does not state the two-parameter split-skew phase diagram or the robust optimizer \((1+\sqrt3)/4\), but if the full text contains an equivalent result, this record's originality claim would need correction or withdrawal.

The \(A=0\) slice overlaps generalized optimistic-gradient analysis for bilinear zero-sum games, including Zhang and Yu, arXiv:1908.05699, which gives exact convergence conditions and parameter tuning for generalized gradient methods.  No novelty is claimed for that slice alone.  Soe--Vetrivel--Yao, arXiv:2509.02005, studies a distinct generalized FRB that uses an additional older operator value; it does not supply the checked two-parameter formula.

Searches included the source identifiers, constant-reflection FRB terminology, split-skew/skew-rotation formulations, the exact algebraic optimizer, and the distinctive numerical ceiling.  No checked source stated the combination of the nonzero split-skew phase diagram and the exact robust max--min tuning.  Older Popov/optimistic-gradient/operator-splitting literature remains a residual historical risk, particularly through equivalent parameterizations.

## Value

**PASS.** The result changes the interpretation of the matched-skew obstruction behind the sharp standard-FRB constant.  Once the reflection coefficient is tunable, the matched-skew case \(\gamma=1\) ceases to be the robust bottleneck.  The optimal fixed coefficient instead balances two different skew placements, \(\gamma=0\) and \(\gamma=1/2\), and raises the exact split-skew ceiling by about 15.17%.  This provides a concrete target for future universal analyses: either a convergence theorem can exploit the larger window, or a different non-skew/nonlinear obstruction must explain why it cannot.

## Limitations

The theorem is exact only for the planar split-skew linear family and exact arithmetic.  It does not establish that the optimized coefficient improves worst-case convergence over all maximally monotone plus monotone-Lipschitz inclusions.  The full text of arXiv:2609.15936 was not inspected, so source-specific originality remains less certain than correctness.  No independent audit has been performed.

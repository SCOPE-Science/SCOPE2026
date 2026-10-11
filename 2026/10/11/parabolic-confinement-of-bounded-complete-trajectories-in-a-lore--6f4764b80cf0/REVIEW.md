# Same-model review

## Correctness
PASS. The transformed variable \(W=z-gx^2/(2a)\) satisfies \(\dot W=-bW+\kappa x^2\) exactly. Bounded completeness and \(b>0\) give the backward convolution formula; strictness follows because equality would force the entire bounded complete trajectory to be the origin. `verify.py` checks the cleared polynomial identity coefficient by coefficient.

## Originality
PASS. The primary 2021 paper was inspected, as was the complete 2011 parent-system paper. The latter's strongest nearby global theorem assumes \(bg>2a(f+g)\), equivalent to \(\kappa<0\), while the 2018 follow-up highlights \(bg=2a(f+g)\), equivalent to \(\kappa=0\). Targeted formula, alias, title, and DOI searches did not find the present \(\kappa>0\) pointwise confinement statement. Residual risk remains that an equivalent identity appears elsewhere under different notation.

## Value
PASS. A pointwise parabolic constraint on every bounded complete non-equilibrium trajectory is structurally stronger than a mean-balance calculation and is directly usable to delimit or validate compact recurrent sets of the model.

## Closest literature and limitations
The closest same-family results are the Li–Ou 2011 convergence theorem in the opposite-sign regime and the Wang–Li 2018 boundary heteroclinic result. The present theorem is only a necessary confinement statement for \(b>0\), \(\kappa>0\); it does not prove recurrence or classify \(\kappa\le0\).

Same-model review: passed. Independent audit: not yet performed.

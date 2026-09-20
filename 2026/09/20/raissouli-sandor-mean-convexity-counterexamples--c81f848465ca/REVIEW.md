# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The construction was rechecked directly from the defining profile
\[
q_c(t)=ct^2(2-t^2),\qquad 0<c\le1/8.
\]
For \(0<|t|<1\), the bound \(0<q_c(t)<|t|\) puts the two proposed maps
strictly between the endpoint values \(\min(x,y)\) and \(\max(x,y)\),
with the arithmetic mean strictly between them.

The coordinate derivatives are
\[
\partial_x M_c^\pm
=\frac12\{f_\pm+(1-t)f_\pm'\},\qquad
\partial_y M_c^\pm
=\frac12\{f_\pm-(1+t)f_\pm'\}.
\]
Here \(f_\pm\ge7/8\) and
\[
|f_\pm'|\le\frac1{3\sqrt3}<\frac15,
\]
so both derivatives are \(>19/80\). This is a uniform strict
monotonicity certificate on the whole positive quadrant.

The curvature calculation was also rederived independently:
\[
\frac{d^2}{dx^2}M_c^+(x,1)
=-\frac{16c(x^2-4x+1)}{(x+1)^5},
\qquad
\frac{d^2}{dx^2}M_c^-(x,1)
=\frac{16c(x^2-4x+1)}{(x+1)^5}.
\]
The polynomial \(x^2-4x+1\) changes sign at \(2+\sqrt3\) on \(x>1\).
Thus each section has both curvature signs, which rules out both
convexity and concavity of the corresponding bivariate mean. This
argument is stronger than merely refuting the source paper's strict
convexity/concavity conclusion, because it fails even the non-strict
properties.

## Originality

PASS, to the best of our knowledge.

The 2016 source was inspected at Problem 4(ii), where the authors
explicitly ask whether a symmetric homogeneous strictly monotone mean
below \(A\) must be strictly concave and whether one above \(A\) must be
strictly convex. The same paper's nonmonotone counterexample does not
meet the hypothesis addressed here.

Searches covered the exact problem wording, source title and DOI,
“symmetric homogeneous strictly monotone mean,” “neither convex nor
concave,” and algebraically equivalent quartic-profile expressions. The
same-year characterization paper by Raïssouli and Rezgui was also
inspected as a plausible stronger framework; its characterization of
strict monotone homogeneous symmetric means does not state the claimed
order-curvature implication or these counterexamples. No located later
source gave an equivalent solution of Problem 4(ii).

The main residual risk is an equivalent example expressed through a
different mean representation, such as an intrinsic generating function
rather than the normalized profile \((x-y)/(x+y)\), in literature not
well indexed by the problem's terminology. No specific inaccessible
paper was found with concrete evidence of containing the present result.

## Value

PASS.

The result resolves both directions of an explicit published open
problem negatively. It supplies continua of \(C^\infty\) counterexamples,
not isolated numerical witnesses, and gives a reusable mechanism:
pointwise order relative to \(A\) is controlled by a profile's value,
whereas convexity is controlled by its second derivative. The
construction simultaneously preserves the nontrivial strict-monotonicity
hypothesis that the source paper identified as essential.

## Limitations

- Problem 4(i) is not addressed.
- No classification is given of additional assumptions that restore the
  proposed order-curvature relation.
- Equivalent prior coverage under substantially different mean
  parametrizations cannot be excluded exhaustively.

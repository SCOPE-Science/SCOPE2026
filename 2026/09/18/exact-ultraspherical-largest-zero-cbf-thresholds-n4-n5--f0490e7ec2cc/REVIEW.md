# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The degree-\(4\) and degree-\(5\) Gegenbauer polynomials reduce exactly to quadratic
equations in \(y=x^2\), yielding the displayed formulas for \(Y_4=z_{4,1}^2\) and
\(Y_5=z_{5,1}^2\). Their normalized inner square roots have the standard
upper-boundary sign change: after both branch points they are negative real. This
makes \(Y_4>0\) on \((-3,-2)\) and \(Y_5>0\) on \((-4,-3)\), so the largest-zero
continuation remains positive there.

At the next pole,
\[
Y_4(\lambda)\sim 3/(\lambda+3),\qquad
Y_5(\lambda)\sim 5/(\lambda+4).
\]
Upper-half-plane continuation therefore gives
\(z_{4,1}\sim\sqrt3(\lambda+3)^{-1/2}\) and
\(z_{5,1}\sim\sqrt5(\lambda+4)^{-1/2}\), with negative-imaginary boundary values
immediately to the left. For \(d\) beyond \(3\) or \(4\), respectively, those
points can be chosen to the right of the scale branch point \(-d\), so the scale
factor is positive real and the Pick property fails.

For sufficiency, the source paper's positive-real-part lemma for the continued
positive zero handles the boundary below the scale branch point, while its
previous boundary argument plus the explicit intervals above handle the boundary
above it. The source paper's boundary minimum principle applies because the
singularities are algebraic of order below one. Its infinity expansion has
strictly negative \(1/\lambda\) coefficient throughout the proposed ranges:
at the two new endpoints the decisive quantities are \(2-\sqrt6<0\) and
\(2-\sqrt{10}<0\). This yields the Pick property and hence the complete-Bernstein
conclusion. The endpoint cancellation of the half-order pole is consistent with
the same argument.

The proof is analytic; no numerical experiment is used as evidence.

## Originality

**PASS, to the best of our knowledge, with an explicit version-access caveat.**

The inspected full text of arXiv:2609.19186v1 gives, for the largest zero and
\(n\ge4\), the sufficient range \(1/2\le d\le\lceil n/2\rceil\) and explicitly
does not claim that its upper endpoint is optimal. It gives exact low-degree
thresholds only in degrees \(2\) and \(3\). The present result determines the next
two degrees exactly and proves that the source's sufficient endpoint is already
nonoptimal for \(n=4,5\).

Searches using the arXiv identifier and combinations of
"complete Bernstein", "ultraspherical", "Gegenbauer", "largest zero", "degree 4",
"degree 5", "d=3", "d=4", and "n-1" found no other source stating these exact
thresholds. The current SCOPE repository was also searched by the source identifier,
object, and claim family; no overlapping record was found.

A metadata index reports that arXiv:2609.19186 was updated on 2026-09-18, but the
updated full text was not available for inspection during this review. Its current
abstract is unchanged and does not state the exact degree-\(4,5\) thresholds.
Because an updated version of the source itself is the most plausible place where
the same calculation could appear, this is the principal residual originality
risk. If that version contains the same result, this originality verdict should
be revised. No claim of exhaustive literature coverage is made.

The Pick characterization of complete Bernstein functions, the Gegenbauer
identities, and the source paper's continuation/minimum-principle machinery are
prior results and are not claimed as new.

## Value

**PASS.**

The result closes the first two low-degree cases left open by the source paper's
nonoptimal sufficient bound and shows concretely that its first degree-loss barrier
is methodological rather than sharp. It identifies the next pole as the exact
complex-analytic obstruction in degrees \(4\) and \(5\), enlarging the admissible
scale interval by a full unit in each case. Together with the source paper's
degree-\(2,3\) calculations, it gives the exact low-degree law
\(d_{\max}(n)=n-1\) through degree five, while clearly separating that observed
pattern from any unproved all-degree conjecture.

## Scope and limitations

The result does not determine the optimal threshold for \(n\ge6\), does not prove
failure of the weaker Bernstein property outside the stated range, and does not
claim independent validation, formal verification, or peer review.

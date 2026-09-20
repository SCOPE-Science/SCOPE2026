# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. Direct substitution into
\[
\dot H=\dot y-m\dot x,\qquad H=y-mx,
\]
gives
\[
\dot H|_{y=mx}
=
x(-1-am-m^2)-m(\alpha-m+\beta m^2)x^3.
\]
Thus \(\beta m^2-m+\alpha=0\) and \(a=-(m+m^{-1})\) make \(y=mx\) invariant exactly. For \(0<\alpha\beta<1/4\), the quadratic has two positive real roots.

The system has exactly one finite equilibrium, the origin. A planar periodic orbit has index \(+1\) and therefore contains an equilibrium in its interior; hence any periodic orbit here would surround the origin. Every complete line through an interior point of a Jordan curve meets the curve. Since the invariant line through the origin cannot be crossed by another trajectory of this smooth vector field, a periodic orbit is impossible.

Elimination of \(m\) from
\[
m^2+am+1=0,\qquad \beta m^2-m+\alpha=0
\]
gives
\[
\alpha\beta a^2+(\alpha+\beta)a+(\alpha-\beta)^2+1=0.
\]
For \(\alpha=\beta=1/10\), the two slopes are \(5\pm2\sqrt6\), both give \(a=-10\), and \(0<\alpha\beta=1/100<1/4\). This is an exact counterexample to the literal statement of Conjecture 5.1.

Adversarial checks included whether a periodic orbit could avoid the origin, whether the invariant set is a full line rather than only an asymptotic direction at infinity, whether the explicit parameter point is strictly within the conjectured regime, and whether the two algebraic conditions really eliminate to the stated surface. All checks pass.

## Originality

PASS, to the best of our knowledge, with a significant prior-literature boundary stated explicitly.

The Lu–Zhang 2026 article was inspected at the model definition, Theorem 1.1, the unresolved-region discussion, and Conjecture 5.1. It states that the origin is the only finite equilibrium, proves at most one limit cycle, proves a unique stable limit cycle only for sufficiently small negative \(a\), and then conjectures exactly one stable hyperbolic limit cycle for every \(a<0\) with \(0<\alpha\beta<1/4\).

Searches used the exact source title, DOI, “Conjecture 5.1,” “invariant line,” “invariant algebraic curve,” the explicit parameter relation, the equivalent general Rayleigh–Liénard coefficients, and counterexample/no-periodic-orbit formulations. No correction, comment, or later paper explicitly recording this counterexample to Conjecture 5.1 was found.

The most relevant prior work is Chen–Fang–Zhang, Advances in Mathematics 483 (2025), 110667, DOI 10.1016/j.aim.2025.110667. Its accessible abstract states that it completes the classification of invariant algebraic curves for the full four-parameter Rayleigh–Liénard family with nonzero mixed coefficient, which contains the present system. The complete article text was not inspected. Therefore existence/classification of the invariant straight line is not claimed as novel. The originality claim is restricted to the no-periodic-orbit consequence in the Lu–Zhang conjectured region and the resulting explicit refutation of Conjecture 5.1. Because the 2025 paper studies exactly the ambient family, it remains the principal residual originality risk.

## Value

PASS. The result falsifies a concrete conjecture stated in a 2026 differential-equations paper and replaces a universal existence claim by an explicit codimension-one obstruction family. The counterexample is exact, requires no numerical evidence, and sharply identifies a class of parameters that any corrected global limit-cycle classification must exclude.

## Limitations retained

The result does not classify dynamics away from the invariant-line sheets, does not determine the corrected maximal region of existence of a limit cycle, and does not claim novelty for the general classification of invariant algebraic curves. The accessible abstract, but not the complete text, of the 2025 Advances in Mathematics paper was inspected; its exact overlap beyond invariant-curve classification therefore remains unresolved.

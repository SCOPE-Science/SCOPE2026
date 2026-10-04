# A time-varying weight destroys the claimed constant cobweb equilibrium
## Finding
Consider the generalized weighted fractional cobweb equation of Madani et al.,
\[
{}^{C}\mathfrak D p(t)=\lambda p(t)+\delta,
\]
with the paper's generalized weighted Caputo operator. Definition 4 differentiates \(\omega p\), while Proposition 1 states, under its stated parameter restrictions including \(\gamma=\alpha_2\),
\[
\mathfrak I\bigl({}^{C}\mathfrak D p\bigr)(t)
=
\frac{(\omega p)(t)-(\omega p)(0)}{\omega(t)}.
\]
Theorem 5 claims that \(p(t)\equiv p^*=-\delta/\lambda\) is a constant equilibrium whenever \(\lambda\ne0\). For a nonzero \(p^*\), this is compatible with Proposition 1 only when \(\omega\) is constant. If the claimed equilibrium equation held, then \({}^{C}\mathfrak D p^*=0\), so applying \(\mathfrak I\) would give
\[
0=
\frac{p^*\bigl(\omega(t)-\omega(0)\bigr)}{\omega(t)}
\quad\text{for every }t.
\]
Because \(\omega(t)>0\) and \(p^*\ne0\), one must have \(\omega(t)=\omega(0)\) for every \(t\). Thus a genuinely time-varying weight destroys the paper's declared nonzero constant equilibrium.

An exact admissible witness uses the source's baseline economic parameters
\[
a=10,\qquad a_1=5,\qquad b=-\frac12,\qquad b_1=\frac12,\qquad c=1,
\]
so that \(\lambda=-1\), \(\delta=5\), and \(p^*=5\). On \([0,1]\), take the positive nonconstant weight \(\omega(t)=1+t\), together with parameters satisfying Proposition 1. Then at \(t=1\),
\[
\frac{(\omega p^*)(1)-(\omega p^*)(0)}{\omega(1)}
=
\frac{10-5}{2}
=
\frac52,
\]
whereas the claimed equilibrium equation requires \({}^{C}\mathfrak D 5=0\), whose fractional integral would be zero. The two statements are incompatible.

## Assumptions and scope
The claim uses the operator and inverse identity printed in the source paper. It assumes the conditions of Proposition 1, including \(\gamma=\alpha_2\), and a positive weight \(\omega\) in the paper's admissible class. The universal part concerns the particular constant candidate \(p^*=-\delta/\lambda\), for which the right-hand side of the model equation is exactly zero. It does not assert that every time-varying weighted cobweb equation lacks all bounded or asymptotically stationary solutions.

The explicit witness is on the finite interval \([0,1]\) with \(\omega(t)=1+t\), which is positive, continuous, and bounded above and below there. The source itself treats nonconstant weights as a central modeling feature and numerically considers a periodic time-varying weight.

## Proof
Let \(p(t)\equiv p^*=-\delta/\lambda\) with \(\lambda\ne0\). Substitution into the right-hand side gives
\[
\lambda p^*+\delta=0.
\]
Therefore, if \(p^*\) were an equilibrium of the stated model, it would satisfy
\[
{}^{C}\mathfrak D p^*=0.
\]
Apply the source's Proposition 1 to this identity. By linearity of the fractional integral,
\[
0=
\mathfrak I(0)(t)
=
\mathfrak I\bigl({}^{C}\mathfrak D p^*\bigr)(t)
=
\frac{(\omega p^*)(t)-(\omega p^*)(0)}{\omega(t)}.
\]
Since \(p^*\) is constant,
\[
0=
\frac{p^*\bigl(\omega(t)-\omega(0)\bigr)}{\omega(t)}.
\]
For \(p^*\ne0\) and \(\omega(t)>0\), this forces \(\omega(t)=\omega(0)\) for every \(t\). Hence a nonconstant weight is incompatible with the claimed nonzero constant equilibrium.

The source proof contains the algebraic step "for a constant function ... \((\omega p)'=0\)." In fact,
\[
(\omega p^*)'=p^*\omega',
\]
which vanishes for nonzero \(p^*\) only when the weight is constant. The inverse identity above converts that local algebraic error into a complete contradiction with the claimed equilibrium.

The subsequent perturbation reduction also changes. If \(x=p-p^*\), then linearity gives
\[
{}^{C}\mathfrak D x
=
\lambda x-{}^{C}\mathfrak D p^*,
\]
not the homogeneous equation \({}^{C}\mathfrak D x=\lambda x\) unless \({}^{C}\mathfrak D p^*=0\). Thus the source's stability theorem is valid as written for the constant-weight subclass, but not for a genuinely time-varying weight without an additional reformulation.

## Verification
The bundled `verifier.py` checks the baseline economic parameters exactly with rational arithmetic, reconstructs \(\lambda=-1\), \(\delta=5\), and \(p^*=5\), and evaluates the Proposition 1 defect for \(\omega(t)=1+t\) at \(t=1\) as exactly \(5/2\). It also verifies that the model right-hand side at \(p^*\) is exactly zero. The universal argument is symbolic and follows directly from Proposition 1; the witness is a replay check, not a finite experiment used to infer the universal statement.

## Relationship to prior work
The motivating 2026 article introduces a generalized weighted Caputo-type operator specifically to allow time-dependent weighting and then states a unique constant equilibrium independent of the weight. In the same article, Definition 4 places the derivative on \(\omega p\), and Proposition 1 recovers the weighted increment \(((\omega p)(t)-(\omega p)(0))/\omega(t)\). Those two displayed formulas already imply the correction above. Searches for the article title, DOI, constant-equilibrium wording, and weighted-operator equivalents located no published erratum or source-specific correction of this point. Earlier generalized weighted fractional-calculus work develops the operator framework but does not establish the cobweb equilibrium claim corrected here.

## Limitations
This result corrects the constant-equilibrium and local-stability reduction for nonconstant weights. It does not classify the actual long-time dynamics for arbitrary \(\omega\), prove or disprove positivity of every solution, or assess the source's constant-weight ABC special case, where the displayed obstruction disappears. No claim is made about numerical figures beyond the fact that a genuinely time-varying weight cannot share the stated nonzero constant equilibrium under the printed operator and inverse identity.

## References
1. Y. A. Madani et al., "A Generalized Weighted Fractional Cobweb Model for Dynamic Market Adjustment," *Fractal and Fractional* 10 (2026), 159. DOI: 10.3390/fractalfract10030159.
2. H. Zine, E. M. Lotfi, D. F. M. Torres, and N. Yousfi, "Taylor's Formula for Generalized Weighted Fractional Derivatives with Nonsingular Kernels," *Axioms* 11 (2022), 231. DOI: 10.3390/axioms11050231.

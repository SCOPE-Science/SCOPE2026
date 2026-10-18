# A sharp eventual-sign barrier for a quadratic-binomial stopping semigroup

## Finding
Put \(h(z)=(2z+z^2)/3\), and for every \(0<\theta<1\) define the analytic germ
\[
G_\theta(z)=h^{-1}\!\left(\frac{\theta h(z)}{1-(1-\theta)h(z)}\right)
=\sqrt{\frac{1+(4\theta-1)h(z)}{1-(1-\theta)h(z)}}-1
=\sum_{n\ge1}a_n(\theta)z^n,
\]
using the square-root branch positive at the origin. Let \(R_*\) be the unique real root greater than one of
\[
R^3+2R^2-5R-2=0,
\]
and let \(\theta_*=(1+3/R_*^2)/4=0.5153108472877\ldots\).

**Theorem.** The following statements hold.

1. For every \(0<\theta\le2/5\), all \(a_n(\theta)\) are strictly positive and sum to one. Consequently \(\{G_\theta:0<\theta\le2/5\}\) is a composition-closed family of probability generating functions of positive-integer laws, with
\[
G_{\theta_1}\circ G_{\theta_2}=G_{\theta_1\theta_2}.
\]
2. For every fixed \(0<\theta\le\theta_*\), the coefficients have the sharp positive asymptotic
\[
a_n(\theta)\sim
\frac{\sqrt{\theta}}{d_\theta\sqrt{2\pi r_\theta(r_\theta+1)}}
\frac{r_\theta^{-n}}{\sqrt n},\qquad
 d_\theta=\frac{1-\theta}{3},\qquad
 r_\theta=\sqrt{\frac{4-\theta}{1-\theta}}-1.
\]
In particular, only finitely many coefficients could be nonpositive at any fixed parameter in this interval.
3. For every \(\theta_*<\theta<1\), infinitely many \(a_n(\theta)\) are strictly negative and infinitely many are strictly positive. None of these germs is a probability generating function.

Thus \(\theta_*\) is the **exact eventual coefficient-positivity cutoff** for \(0<\theta<1\). If \(\theta_{\mathrm{pgf}}\) denotes the supremum of the admissible parameters strictly below one, then
\[
\frac25\le\theta_{\mathrm{pgf}}\le\theta_*.
\]
The theorem does **not** claim that the second inequality is an equality. The isolated endpoint \(\theta=1\) instead gives \(G_1(z)=z\).

## Assumptions and scope
The variable \(z\) is complex, with a Taylor expansion at \(z=0\); the parameter is real in \((0,1)\). A positive-integer probability generating function means a power series \(\sum_{n\ge1}a_n z^n\) with all \(a_n\ge0\) and \(\sum a_n=1\). The inverse branch of \(h\) is \(h^{-1}(w)=\sqrt{1+3w}-1\); it maps \([0,1]\) into \([0,1]\). All asymptotics are for integer \(n\to\infty\) at **fixed** \(\theta\); no uniformity in \(\theta\) is asserted.

This particular \(h\) is the probability generating function of a zero-truncated binomial random variable with two trials of success probability one half. The recent study of composition-closed stopping models explicitly gives the corresponding family on \(0<\theta\le1/4\). The new lower admissibility endpoint \(2/5\) and exact eventual-sign threshold are properties of this same family, not of arbitrary conjugacies.

## Proof
**Algebra and normalization.** Put \(t(z)=z^2+2z\), \(c=(4\theta-1)/3\), and \(d=(1-\theta)/3\). The defining identity is
\[
1+G_\theta(z)=\sqrt{\frac{1+c\,t(z)}{1-d\,t(z)}}.
\]
Here \(c+d=\theta\), \(d>0\), and differentiation yields
\[
G_\theta'(z)=\theta(1+z)(1+c\,t(z))^{-1/2}(1-d\,t(z))^{-3/2}.
\tag{1}
\]
The function satisfies \(G_\theta(0)=0\), \(G_\theta'(0)=\theta\), and \(G_\theta(1)=1\). Every radical zero or pole is outside the closed unit disk for \(0<\theta<1\), as is confirmed by the root locations below; hence its Taylor series converges absolutely at one.

**Coefficient positivity on a genuinely enlarged parameter interval.** If \(0<\theta\le1/4\), then \(c\le0\) and \((1+c t)^{-1/2}\), \((1-dt)^{-3/2}\) have power series with nonnegative coefficients in \(t\). If \(1/4<\theta\le2/5\), then \(0<c\le d\), and
\[
(1+c t)^{-1/2}(1-dt)^{-3/2}
=(1-dt)^{-1}\bigl(1-(d-c)t-cd\,t^2\bigr)^{-1/2}.
\tag{2}
\]
Both factors in (2) have nonnegative Taylor coefficients in \(t\), by the positive binomial expansion of \((1-u)^{-1/2}\) and the fact that \((d-c)t+cd\,t^2\) has nonnegative coefficients and vanishing constant term. Substituting \(t=z^2+2z\) preserves nonnegativity. Moreover \((1-dt)^{-1}\) has strictly positive coefficients of every degree in \(z\). Equation (1) thus shows \(a_n(\theta)>0\) for every \(n\ge1\). Together with \(G_\theta(1)=1\), this proves the pgf assertion. Writing \(M_\theta(w)=\theta w/[1-(1-\theta)w]\), direct simplification gives \(M_\alpha\circ M_\beta=M_{\alpha\beta}\); conjugating by \(h\) proves the composition identity.

**Competing singularities.** The denominator has a positive simple zero at
\[
r_\theta=\sqrt{1+1/d}-1
=\sqrt{\frac{4-\theta}{1-\theta}}-1>1,
\]
and a negative zero with modulus \(r_\theta+2\). If \(\theta<1/4\), the numerator has a positive zero at \(\sqrt{1+1/|c|}-1>r_\theta\), and a negative zero of still larger modulus. At \(\theta=1/4\), the numerator is constant. If \(1/4<\theta<1\), its two simple conjugate zeros are
\[
-1\pm i\sqrt{1/c-1},
\]
each of modulus \(\rho_\theta=1/\sqrt c=\sqrt{3/(4\theta-1)}\). The function \(r_\theta\) is strictly increasing in \(\theta\), while \(\rho_\theta\) is strictly decreasing. Their unique intersection has common value \(R_*\). Substituting \(1-\theta=3/[R_*(R_*+2)]\) and \(4\theta-1=3/R_*^2\) gives the stated cubic. The cubic is strictly increasing for real \(R\ge1\) and changes sign between one and two, proving uniqueness of \(R_*\). Thus the positive denominator singularity is uniquely dominant before \(\theta_*\), ties the numerator conjugate branchpoints at \(\theta_*\), and loses dominance afterward.

**Sharp asymptotic and eventual positivity.** At the denominator root \(r=r_\theta\), the numerator has value \(1+c/d=\theta/d>0\). Locally,
\[
G_\theta(z)
=\frac{\sqrt{\theta}}{d\sqrt{2r(r+1)}}
(1-z/r)^{-1/2}+O(1)
\]
with a full analytic Puiseux expansion. Standard algebraic singularity transfer gives its coefficient contribution
\[
\frac{\sqrt\theta}{d\sqrt{2\pi r(r+1)}}r^{-n}n^{-1/2}(1+O(n^{-1})).
\]
For \(\theta<\theta_*\), all other singularities have strictly larger modulus, so this is the full leading term. At \(\theta=\theta_*\), the two equally distant numerator zeros are simple square-root *zeros* rather than inverse-square-root poles: their total coefficient contribution is only \(O(r^{-n}n^{-3/2})\), and the positive leading term is unchanged. Consequently \(a_n(\theta)>0\) for all sufficiently large \(n\) whenever \(0<\theta\le\theta_*\).

**Infinitely many sign changes beyond the barrier.** For \(\theta_*<\theta<1\), the radius of the Taylor expansion is \(\rho_\theta<r_\theta\), set by the two simple nonreal numerator zeros. The germ extends analytically across the *positive* real point \(z=\rho_\theta\), which is smaller than its first positive denominator zero. Suppose its coefficients were eventually nonnegative. Removing a finite initial polynomial would produce a nonnegative-coefficient series of finite radius \(\rho_\theta\) analytic through its positive radius, contradicting the Vivanti–Pringsheim theorem. Apply the same argument to the negative of the series to rule out eventual nonpositivity. Infinitely many strictly positive and infinitely many strictly negative coefficients therefore occur. This also proves non-admissibility in that parameter region.

## Verification
The standalone program `check_coefficients.py` generates exact rational Taylor coefficients by expanding the independent algebraic relation
\[
(1-d(z^2+2z))(1+G_\theta(z))^2=1+c(z^2+2z).
\]
It independently rechecks that relation coefficient by coefficient. In the supplied execution the program completed 704 exact finite assertions: positive first 120 coefficients for each of \(\theta=1/10,1/4,1/3,2/5,1/2\); 100 coefficients at \(\theta=11/20\), with the first negative at index 39; and decimal root bracketing of the defining cubic. These calculations are **not** the proof of universal positivity or infinite sign changes; those are established analytically above. Run with `python3 check_coefficients.py` using Python 3 standard library only.

## Relationship to prior work
Valero and Ginebra (2026, arXiv:2609.30106, Sections 3, 5, 6.2, 7 and Example 7) develop general composition-closed positive-integer stopping models, and explicitly give the zero-truncated-binomial family at two trials with the parameter range \(0<\theta\le1/4\). Their earlier paper (arXiv:2412.15997, Section 6.2, Example 6.5) constructs the same family on that range. These are foundational prior results. Neither inspected text asserts the new \(2/5\) admissibility endpoint, the exact critical cubic, or the coefficient-sign phase transition for this quadratic family. The general Koenigs-parametrization theorem does not by itself decide coefficient signs at parameters beyond the exhibited interval. Classical algebraic singularity transfer and Vivanti–Pringsheim are used as known tools, not claimed as new results. The closest known published result on dispersion of composition-closed stopping models computes a moment curve under already-admissible models, rather than deciding admissibility from coefficients.

## Limitations
The **exact** supremum of pgf-admissible nonidentity parameters remains undetermined inside \([2/5,\theta_*]\). Eventual coefficient positivity is weaker than nonnegativity of every coefficient; no equality between the two thresholds is claimed. All conclusions use this single quadratic conditioning polynomial, and do not classify general zero-truncated binomial degrees. The singularity analysis is pointwise in \(\theta\) and does not give a uniform positive-coefficient index. Published literature outside the inspected comparisons could contain a reformulation of the cutoff. No independent mathematical audit has been performed.

## References
- J. Valero and J. Ginebra, *Stopping models closed under pgf composition, and the stability of randomly stopped model extensions*, arXiv:2609.30106, first submitted 2026-09-24, especially Sections 3, 6.2 and 7. https://arxiv.org/abs/2609.30106
- J. Valero and J. Ginebra, *On statistical model extensions based on randomly stopped extremes*, arXiv:2412.15997, first submitted 2024-12-20, Section 6.2, Example 6.5. https://arxiv.org/abs/2412.15997
- P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, Chapters IV and VI (Pringsheim theorem and algebraic singularity transfer).

# Localized Blaschke max-laws and the absence of strongly extreme points in Garsia-norm balls

## Finding

**Theorem (boundary-localized max-law).** Write \(\mathbb D\) for the open unit disk and \(\mathbb T\) for the unit circle, with normalized arc measure. For a complex \(L^2(\mathbb T)\) function \(f\), let \(\mathcal P f\) denote its Poisson extension and define
\[
\Phi_f(z)=\mathcal P(|f|^2)(z)-|\mathcal P f(z)|^2,\qquad
\|f\|_G=\sup_{z\in\mathbb D}\sqrt{\Phi_f(z)}.
\]
For every \(f\) of bounded mean oscillation (equivalently \(\|f\|_G<\infty\)), there is a measurable set \(E_f\subset\mathbb T\) of full arc measure with the following property. Fix any \(\zeta\in E_f\), any \(c\in\mathbb C\), and put
\[
a=r\zeta,\qquad b_a(z)=\frac{a-z}{1-\overline a z},\qquad h_a(z)=b_a(z)-a,\qquad 0<r<1.
\]
Then
\[
\boxed{\|h_a\|_G=1\quad\text{and}\quad
\lim_{r\uparrow1}\|f+c h_{r\zeta}\|_G=\max\{\|f\|_G,|c|\}.}
\]
The same choice of full-measure set works for all fixed complex scalars \(c\); it may depend on \(f\).

**Corollary (complete strongly extreme classification).** In the Garsia norm, none of the closed unit balls of \(\mathrm{BMO}(\mathbb T)/\mathbb C\), \(\mathrm{BMOA}/\mathbb C\), \(\mathrm{VMO}(\mathbb T)/\mathbb C\), and \(\mathrm{VMOA}/\mathbb C\) has a strongly extreme point. Equivalently one may realize the analytic quotients by the canonical representatives satisfying \(f(0)=0\).

The corollary is compatible with the previously established fact that every norm-one element of \(\mathrm{VMO}\) is an *ordinary* extreme point for this norm: ordinary and strongly extreme geometry are different here.

## Assumptions and scope

All boundary functions are complex-valued, modulo additive constants. The variance \(\Phi_f(z)\) is the variance of \(f\) under the probability measure \(d\omega_z(\xi)=(1-|z|^2)|\xi-z|^{-2}dm(\xi)\). The Garsia seminorm becomes a norm on the indicated constant quotients. \(\mathrm{BMOA}\) and \(\mathrm{VMOA}\) are the analytic subspaces, with analytic polynomials dense in the latter. The \(\mathrm{VMO}\) space is understood as the subspace whose Poisson variance tends uniformly to zero as the base point approaches the boundary; this agrees with the standard vanishing-mean-oscillation space.

A point \(f\) of a closed unit ball is **strongly extreme** if, for every \(\epsilon>0\), there is \(\delta>0\) such that \(\|f+g\|_G\le1+\delta\) and \(\|f-g\|_G\le1+\delta\) imply \(\|g\|_G<\epsilon\). The result addresses this exact local uniform-midpoint property; no claim is made about all ordinary extreme points of \(\mathrm{BMO}\) or \(\mathrm{BMOA}\).

## Proof

**1. Boundary localization of the original oscillation.** A \(\mathrm{BMO}\) function is in \(L^2(\mathbb T)\). Consequently both \(f\) and \(|f|^2\) are integrable. By the non-tangential boundary-value theorem for Poisson integrals, on a common full-measure set \(E_f\) one has, whenever \(z\to\zeta\in E_f\) inside any fixed Stolz cone,
\[
\mathcal Pf(z)\longrightarrow f(\zeta),\qquad
\mathcal P|f|^2(z)\longrightarrow|f(\zeta)|^2.
\]
Thus \(\Phi_f(z)\to0\) non-tangentially at each such \(\zeta\). In particular \(\Phi_f(r\zeta)\to0\).

**2. The exact norm and pointwise escape of the perturbation.** The disk automorphism \(b_a\) has unimodular boundary values and a zero at \(a\). Addition of constants does not change Poisson variance, so
\[
\Phi_{h_a}(z)=\Phi_{b_a}(z)=1-|b_a(z)|^2.
\]
At \(z=a\) this equals one, while it never exceeds one; therefore \(\|h_a\|_G=1\). For any fixed \(z\in\mathbb D\), as \(r\uparrow1\) with \(a=r\zeta\), the automorphism \(b_a(z)\to\zeta\) and \(\Phi_{h_a}(z)\to0\). Moreover \(h_{r\zeta}(z)\to0\) locally uniformly in \(z\). Each \(h_a\) is a rational analytic function with its only pole outside the closed disk and \(h_a(0)=0\); in particular it belongs to \(\mathrm{VMOA}\) (and hence to all four spaces).

**3. Localization of the large perturbation variance.** Fix \(t\in(0,1)\) and write
\[
E_{a,t}=\{z\in\mathbb D:|b_a(z)|<t\}.
\]
These pseudohyperbolic disks converge *non-tangentially* to \(\zeta\) as \(a=r\zeta\to\zeta\). For completeness, rotate \(\zeta\) to \(1\). If \(w=b_r(z)\) and \(|w|<t\), then
\[
z=\frac{r-w}{1-rw},\qquad
|1-z|=\frac{(1-r)|1+w|}{|1-rw|},\qquad
1-|z|^2=\frac{(1-r^2)(1-|w|^2)}{|1-rw|^2}.
\]
In particular \(|1-z|\le(1-r)(1+t)/(1-t)\), and
\[
\frac{|1-z|}{1-|z|}
=\frac{(1+|z|)|1+w||1-rw|}{(1+r)(1-|w|^2)}
\le\frac{2(1+t)^2}{1-t^2}.
\]
Hence every \(E_{r\zeta,t}\) lies in a common non-tangential cone and shrinks to \(\zeta\). Step 1 implies
\[
\lim_{r\uparrow1}\sup_{z\in E_{r\zeta,t}}\sqrt{\Phi_f(z)}=0.
\]

**4. Upper bound for the global mixed norm.** For each base point \(z\), the square root of \(\Phi_f(z)\) is an \(L^2(d\omega_z)\) norm after subtracting the mean, and so obeys the triangle inequality:
\[
\sqrt{\Phi_{f+c h_a}(z)}\le
\sqrt{\Phi_f(z)}+|c|\sqrt{1-|b_a(z)|^2}.
\]
For \(z\in E_{a,t}\), the right side is bounded by \(|c|+o(1)\), uniformly by Step 3. For \(z\notin E_{a,t}\), it is bounded by \(\|f\|_G+|c|\sqrt{1-t^2}\). Therefore
\[
\limsup_{r\uparrow1}\|f+c h_{r\zeta}\|_G\le
\max\bigl\{|c|,\ \|f\|_G+|c|\sqrt{1-t^2}\bigr\}.
\]
Letting \(t\uparrow1\) yields the desired upper bound \(\max\{\|f\|_G,|c|\}\).

**5. Two matching lower bounds.** For each fixed \(z\), the reverse triangle inequality for the centered \(L^2(d\omega_z)\) norm and Step 2 show
\[
\liminf_{r\uparrow1}\|f+c h_{r\zeta}\|_G\ge\sqrt{\Phi_f(z)}.
\]
Taking the supremum over \(z\) gives the first lower bound \(\|f\|_G\). Evaluating instead at \(z=a=r\zeta\), where \(\sqrt{\Phi_{h_a}(a)}=1\), gives
\[
\|f+c h_a\|_G\ge |c|-\sqrt{\Phi_f(a)}\longrightarrow |c|.
\]
The upper and lower bounds prove the max-law for every fixed \(c\in\mathbb C\).

**6. Failure of strongly extreme geometry in all four spaces.** Take any norm-one \(f\) in one of the four specified spaces and choose \(\zeta\in E_f\). The sequence \(g_r=h_{r\zeta}\) belongs to that same space, satisfies \(\|g_r\|_G=1\), and, by the max-law with \(c=1\) and \(c=-1\),
\[
\lim_{r\uparrow1}\|f\pm g_r\|_G=1.
\]
This contradicts strong extremality for \(\epsilon=1/2\). Interior points cannot be strongly extreme either: a fixed nonzero sufficiently small direction produces two points still inside the unit ball. Thus there are no strongly extreme points, as asserted. \(\square\)

## Verification

Every step above is an exact analytical identity or limit. Critical checks are: the Poisson variance is a centered \(L^2\) norm; boundary limits apply simultaneously to \(f\) and \(|f|^2\); the automorphism has unit boundary modulus and vanishes at \(a\); its pseudohyperbolic peak set remains in a fixed non-tangential cone; the triangle bound is uniform inside and outside that set; and the two lower-bound tests use distinct base points. No finite calculation, probabilistic test, or computational certificate is needed for the infinite-dimensional assertion.

The formula is invariant under replacement of \(f\) by \(f+\mathrm{constant}\). It includes \(f=0\), arbitrary (fixed) complex \(c\), and all four indicated function spaces. It does **not** assert the convergence uniformly over all \(f\), all boundary points, or scalar parameters varying with \(r\).

## Relationship to prior work

Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm* (arXiv:2609.33242, first submitted 2026-09-27), explicitly asks about strongly extreme points of the Garsia-norm unit ball of \(\mathrm{BMO}\), with the analytic counterpart. The present max-law supplies a complete negative answer in the four stated spaces. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm* (arXiv:2404.05565), develops the variance definition and establishes that norm-attaining unit vectors are ordinary extreme points, including all unit vectors in \(\mathrm{VMO}\). This is distinct from strong extremality and highlights the force of the present conclusion. Dyakonov, *Inner functions as strongly extreme points: stability properties* (arXiv:2301.11162), concerns the \(H^\infty\) supremum norm and its finite-codimensional modifications, not the Garsia norm; inner functions' strong extremality there does not transfer to this geometry.

## Limitations

The result concerns the **specific Garsia norm**, not arbitrary equivalent \(\mathrm{BMO}\) norms or the usual \(H^\infty\) supremum norm. The full-measure good-boundary set depends on the fixed function. Strong extremality is ruled out, but the theorem does not provide a classification of the ordinary extreme points in the full \(\mathrm{BMO}\) or \(\mathrm{BMOA}\) unit ball. Published-work priority remains subject to further specialist and independent review, especially because related boundary-localization principles may be implicit in earlier oscillation theory. No independent scientific audit has been performed.

## References

1. K. M. Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm*, arXiv:2609.33242, first public 2026-09-27, https://arxiv.org/abs/2609.33242.
2. K. M. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm*, arXiv:2404.05565 (2024/2025), https://arxiv.org/html/2404.05565v2.
3. K. M. Dyakonov, *Inner functions as strongly extreme points: stability properties*, arXiv:2301.11162 (2023), https://arxiv.org/abs/2301.11162.
4. Standard Fatou theorem for Poisson integrals of \(L^1\) boundary data, as presented in the classical theory of Hardy spaces and harmonic analysis.

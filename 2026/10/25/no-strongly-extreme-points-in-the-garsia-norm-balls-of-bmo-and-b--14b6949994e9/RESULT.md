# No strongly extreme points in the Garsia-norm balls of BMO and BMOA

## Finding

The closed Garsia-norm unit balls of each of the following four complex Banach spaces have **no strongly extreme points**:
\[
\mathrm{BMO}(\mathbb T)/\mathbb C,\quad
\mathrm{BMOA}/\mathbb C,\quad
\mathrm{VMO}(\mathbb T)/\mathbb C,\quad
\mathrm{VMOA}/\mathbb C.
\]
More explicitly, for every element \(f\) of Garsia norm one in any one of these spaces there is a sequence \((g_n)\) in the same space such that
\[
\|g_n\|_G=1,\qquad
\max\{\|f+g_n\|_G,\|f-g_n\|_G\}\longrightarrow1.
\]
The perturbations can always be chosen from the disk algebra, even when \(f\) is merely in BMO. This settles the *strongly extreme* variant of the Garsia-norm geometry problem suggested in [1]; it does not characterize ordinary extreme points. In particular, it contrasts with the previously known result [2] that every Garsia-unit VMO function is an ordinary extreme point.

## Assumptions and scope

Write \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(\mathbb T=\partial\mathbb D\), and let \(dm\) be normalized arc measure. For \(u\in L^2(\mathbb T)\), its Poisson extension and *Poisson variance* are
\[
Pu(z)=\int_{\mathbb T}u(\xi)\frac{1-|z|^2}{|\xi-z|^2}\,dm(\xi),\qquad
V_u(z)=P(|u|^2)(z)-|Pu(z)|^2.
\]
Define \(\|u\|_G=\sup_{z\in\mathbb D}\sqrt{V_u(z)}\). Constants have seminorm zero; throughout, elements of each space are understood modulo constants. BMO consists of the \(L^2\) functions with finite Garsia norm; BMOA is its analytic Hardy subspace. VMO is the subspace characterized by \(V_u(z)\to0\) as \(|z|\to1\), and VMOA is its analytic subspace. (The standard definitions agree with [2].)

For a normed space \(X\), a point \(f\) of its closed unit ball is *strongly extreme* if every sequence \((g_n)\) satisfying \(\|f\pm g_n\|\to1\) has \(\|g_n\|\to0\). Equivalently, for each \(\varepsilon>0\) there is \(\delta>0\) such that both \(\|f\pm g\|<1+\delta\) imply \(\|g\|<\varepsilon\). The displayed theorem supplies a countersequence of norm exactly one at every point of the unit sphere. Points of norm less than one are not extreme and therefore not strongly extreme.

## Proof

**1. Variance vanishes at a Lebesgue point along Stolz regions.** Fix a unit Garsia-norm element \(f\), represented by a function in \(L^2(\mathbb T)\). Almost every \(\zeta\in\mathbb T\) is simultaneously a Lebesgue point of \(f\) and \(|f|^2\). Choose such a \(\zeta\). The nontangential boundary convergence theorem for Poisson integrals, applied to these two \(L^1\) data, yields
\[
V_f(z)\longrightarrow |f(\zeta)|^2-|f(\zeta)|^2=0
\quad\text{as }z\to\zeta\text{ within any fixed Stolz region.}
\]
This assertion does not require \(f\) to be bounded or analytic.

**2. Moving analytic perturbations have fixed norm.** For \(0<r<1\), put \(a=r\zeta\) and set
\[
b_a(z)=\frac{z-a}{1-\overline a z},\qquad g_a(z)=b_a(z)+a.
\]
Both functions extend analytically across \(\mathbb T\), and \(g_a(0)=0\). In particular \(g_a\) lies in each of BMO, BMOA, VMO and VMOA. As \(|b_a|=1\) on \(\mathbb T\), constant-invariance of variance implies
\[
V_{g_a}(z)=1-|b_a(z)|^2
=\frac{(1-r^2)(1-|z|^2)}{|1-\overline a z|^2}.
\]
Thus \(0\le V_{g_a}\le1\), and \(V_{g_a}(a)=1\). Consequently \(\|g_a\|_G=1\) for every \(r\).

**3. The two variance peaks become disjoint.** Define
\[
\Delta_r=\sup_{z\in\mathbb D}\min\big\{V_f(z),V_{g_{r\zeta}}(z)\big\}.
\]
We prove \(\Delta_r\to0\) as \(r\uparrow1\). Let \(\varepsilon\in(0,1)\) and put \(\rho=\sqrt{1-\varepsilon}<1\). If \(V_{g_{r\zeta}}(z)\ge\varepsilon\), then \(|b_{r\zeta}(z)|\le\rho\). Write \(b_{r\zeta}(z)=\zeta u\), \(|u|\le\rho\). Inverting the automorphism gives
\[
z=\zeta\frac{r+u}{1+ru},\qquad
|\zeta-z|=\frac{(1-r)|1-u|}{|1+ru|},\qquad
1-|z|^2=\frac{(1-r^2)(1-|u|^2)}{|1+ru|^2}.
\]
For every fixed \(\rho<1\), these formulas show uniformly in \(|u|\le\rho\) that \(z\to\zeta\) while
\[
\frac{|z-\zeta|}{1-|z|}\le
\frac{2(1+\rho)^2}{1-\rho^2}.
\]
Indeed \(1-|z|\ge(1-|z|^2)/2\), and the above relations give the stated bound (in fact a smaller \(r\)-dependent bound). Therefore, by step 1,
\[
\sup_{\{z:\,V_{g_{r\zeta}}(z)\ge\varepsilon\}}V_f(z)\longrightarrow0.
\]
On the complementary region \(V_{g_{r\zeta}}<\varepsilon\). It follows that
\[
\limsup_{r\uparrow1}\Delta_r\le\varepsilon.
\]
As \(\varepsilon>0\) is arbitrary, \(\Delta_r\to0\).

**4. The strong-extremity modulus vanishes.** At each \(z\), the centered Poisson \(L^2\) triangle inequality gives
\[
\sqrt{V_{f\pm g_a}(z)}\le\sqrt{V_f(z)}+\sqrt{V_{g_a}(z)}.
\]
Because \(\max\{V_f(z),V_{g_a}(z)\}\le1\) and \(\min\{V_f(z),V_{g_a}(z)\}\le\Delta_r\), we obtain for both signs
\[
\|f\pm g_{r\zeta}\|_G\le1+\sqrt{\Delta_r}\longrightarrow1.
\]
The reverse asymptotic inequality follows from
\[
2\|f\|_G=\|(f+g_{r\zeta})+(f-g_{r\zeta})\|_G
\le\|f+g_{r\zeta}\|_G+\|f-g_{r\zeta}\|_G,
\]
so the maximum tends to one. Meanwhile \(\|g_{r\zeta}\|_G=1\). This contradicts strong extremity of \(f\). Since the perturbations lie in all four spaces, the proof applies to each. Finally, a point strictly inside a norm unit ball cannot be strongly extreme (a sufficiently small fixed nonzero perturbation stays inside for both signs). The classification follows.

## Verification

The proof's critical ingredients are the stated nontangential Poisson boundary theorem, the exact Blaschke variance identity, uniform localization of its level sets inside a Stolz cone, and the centered \(L^2\) triangle inequality. The standalone script `checks/check_geometry.py` checks the Möbius inversion, the variance formula, the displayed Stolz estimate, and a concrete analytic benchmark using floating-point arithmetic. Those checks are supplementary: the proof of the result for all functions is analytic, not numerical.

## Relationship to prior work

Dyakonov [1, Section 2, Problem 2 and its concluding strongly extreme variant] asks for the geometry of the Garsia-norm balls of BMO and BMOA, specifically suggesting the strongly extreme variant. That paper does not classify strongly extreme points: its addendum addresses a different Hankel-operator problem. The earlier paper [2, Theorem 2.7 and Corollary 2.8] identifies many *ordinary* extreme points and all ordinary extreme points of the VMO unit ball, but does not imply strong extremity. The present empty-set result is compatible with those ordinary-extremity statements.

Classical strongly extreme results for \(H^\infty\) [3] concern the supremum norm, not the Garsia norm. Axler–Shields [4] studied BMO/VMO balls under norms defined using arc averages rather than the present Poisson-variance norm (as [2, Section 2] notes); a same-space label is not a same-norm theorem.

## Limitations

This establishes *absence of strongly extreme points* under the explicitly defined Garsia norm only. It does not settle the ordinary-extreme classification for arbitrary non-norm-attaining BMO or BMOA functions, nor does it address different equivalent BMO norms (strong extremity depends on the particular norm). The construction gives qualitative convergence with a rate depending on the Lebesgue-point behavior of \(f\); no uniform rate over the unit sphere is claimed. Independent review and exhaustive historical-priority verification have not been performed.

## References

[1] K. M. Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm*, arXiv:2609.33242, first posted 2026-09-27; inspected version 3 (2026-10-18), Section 2 and Addendum.

[2] K. M. Dyakonov, *Extremal Problems in BMO and VMO Involving the Garsia Norm*, arXiv:2404.05565, first posted 2024-04-08; inspected version 2 (2025-02-11), especially Theorem 2.7 and Corollary 2.8.

[3] K. M. Dyakonov, *Inner Functions as Strongly Extreme Points: Stability Properties*, arXiv:2301.11162 (2023).

[4] S. Axler and A. Shields, *Extreme Points in VMO and BMO*, Indiana Univ. Math. J. 31 (1982), 1–6. Its norm comparison is recorded in [2].

# A sharp four-site monotonicity breakdown for the Dudley norm on a metric path

## Finding
Let \(S=\{0,1,2,3\}\) with \(d(i,j)=|i-j|\), and let \(0<t<1\). Define the zero-total-mass signed measure
\[
\mu_t=-\delta_0+(1-t)\delta_1-(1-t)\delta_2+\delta_3.
\]
For the **sum-normalized bounded-Lipschitz norm** \(\|f\|_{\mathrm{BL}}=\|f\|_\infty+\operatorname{Lip}(f)\), its exact dual (Dudley) norm is
\[
\boxed{\|\mu_t\|_{\mathrm{BL}}^*=\max\!\left\{\frac{4-2t}{3},\frac{4+2t}{5}\right\}.}
\]
Equivalently, the first branch is strictly dominant for \(0<t<\tfrac12\), both branches agree at \(t=\tfrac12\), and the second is strictly dominant for \(\tfrac12<t<1\).

Every cumulative transport flux across the three successive edges equals, respectively, \(1,t,1\), so each flux is strictly positive. Nevertheless, **when \(0<t<\tfrac12\), no nondecreasing Lipschitz test function norms \(\mu_t\)**. The exact supremum among nondecreasing test functions of bounded-Lipschitz norm at most one is
\[
\boxed{\sup_{f(0)\le f(1)\le f(2)\le f(3),\,\|f\|_{\mathrm{BL}}\le1}\langle\mu_t,f\rangle
=\max\!\left\{1,\frac{4+2t}{5}\right\}.}
\]
At \(t=\tfrac12\) and beyond, a nondecreasing norming potential exists. Four sites are minimal for this monotonicity breakdown among finite path metrics with strictly positive cumulative edge flux: for any two- or three-site path, some nondecreasing potential attains the dual norm.

## Assumptions and scope
Everything is real, finite-dimensional, and uses the **sum** norm, not the maximum-based Fortet–Mourier norm. Points are successive unit-spaced vertices on the line; \(\delta_i\) denotes evaluation at point \(i\). The parameter has \(0<t<1\). The dual norm is the supremum of \(\langle\mu_t,f\rangle\) over all \(f:S\to\mathbb R\) with \(\|f\|_\infty+\max_{0\le i<3}|f(i+1)-f(i)|\le1\). The last equality for the Lipschitz constant follows from the unit path metric.

The statement is also valid for measures supported on these four points when bounded Lipschitz test functions are defined on all of \(\mathbb R\): piecewise-linear interpolation between sites, followed by constant extension outside \([0,3]\), does not change either the supremum norm or the Lipschitz constant.

A positive cumulative flux means \(-\sum_{i=0}^{j}\mu_t(\{i\})>0\) for every proper initial segment of the path. This convention matches the representation of the measure pairing as a positive weighted sum of successive test-function increments.

## Proof
**1. Symmetry reduction.** Since \(\mu_t(S)=0\), adding constants to \(f\) does not change the objective. Reflection with sign reversal, \((Rf)(i)=-f(3-i)\), preserves \(\|f\|_{\mathrm{BL}}\) and satisfies \(\langle\mu_t,Rf\rangle=\langle\mu_t,f\rangle\). Convexity of the norm therefore permits averaging \(f\) with \(Rf\) without changing its pairing or increasing its norm. Every optimum has a reflection-antisymmetric representative
\[
(f(0),f(1),f(2),f(3))=(-a,-b,b,a),\qquad a,b\in\mathbb R.
\]
On this plane, the objective equals \(2[a+(t-1)b]\) and the bounded-Lipschitz norm becomes
\[
N(a,b)=\max\{|a|,|b|\}+\max\{|a-b|,2|b|\}.
\]

**2. The exact symmetric unit ball.** The inequality \(N(a,b)\le1\) is the intersection of sixteen halfplanes \(u(a,b)+v(a,b)\le1\), where
\[
u\in\{a,-a,b,-b\},\qquad v\in\{a-b,b-a,2b,-2b\}.
\]
Solving their pairwise boundary intersections and retaining exactly those satisfying all halfplanes gives the six vertices
\[
\pm\left(\tfrac35,\tfrac15\right),\quad
\pm\left(\tfrac13,-\tfrac13\right),\quad
\pm\left(\tfrac13,\tfrac13\right).
\]
This enumeration can also be checked using the accompanying exact rational script. Evaluating the linear objective at these six vertices gives candidates \(\pm(4+2t)/5\), \(\pm(4-2t)/3\), and \(\pm2t/3\). For \(0<t<1\), the last candidate is smaller than the maximum of the first two. Thus the displayed Dudley norm formula holds for every real \(t\) in the asserted range, without relying on numerical sampling. The first branch is attained at \((a,b)=(1/3,-1/3)\), producing the sawtooth test \((-1/3,1/3,-1/3,1/3)\); the second is attained at \((3/5,1/5)\), producing the monotone test \((-3/5,-1/5,1/5,3/5)\). Their intersection is exactly \(t=1/2\).

**3. Restriction to monotone potentials.** Reflection with sign reversal preserves nondecreasing functions. Therefore a nondecreasing maximizer, if one exists, has a symmetric nondecreasing representative, equivalent to \(a\ge b\ge0\). For \(a>0\), write \(u=b/a\in[0,1]\); homogeneity reduces the monotone supremum to
\[
\max_{0\le u\le1}\frac{2[1-(1-t)u]}{1+\max\{1-u,2u\}}.
\]
On \([0,1/3]\), the derivative has the sign of \(2t-1\); on \([1/3,1]\), the expression strictly decreases. Therefore the maximum occurs at \(u=0\) or \(u=1/3\), with values \(1\) and \((4+2t)/5\). At \(a=0\), the only nondecreasing symmetric potential is zero, so no other candidate appears. For \(0<t<1/2\), this monotone supremum is \(1\), whereas the unrestricted norm is \((4-2t)/3>1\). Consequently no monotone potential norms the measure, despite all three positive fluxes. For \(t\ge1/2\), the second displayed extremizer is monotone and optimal.

**4. Minimum cardinality within paths.** For a path with at most three sites and any positive edge lengths, let \(A_j=-\sum_{i=0}^j\mu(\{i\})>0\) be the positive fluxes. Summation by parts gives \(\langle\mu,f\rangle=\sum_j A_j(f(j+1)-f(j))\). On a three-site path, if its first increment is negative, replace the first endpoint value by the middle value; if its last increment is negative, replace the last endpoint value by the middle value. Each replacement makes that increment zero, strictly raises the objective, and cannot increase either \(\|f\|_\infty\) (the replacement value already occurs) or the Lipschitz constant (the latter is the maximum of absolute adjacent slopes). After these replacements all increments are nonnegative. The two-site case is immediate. Thus a monotone optimizer always exists on paths of at most three sites. The four-site family above is a minimal counterexample.

## Verification
The accompanying `verify.py` derives all sixteen inequalities from the norm definition, enumerates all their pairwise intersections using exact rational arithmetic, and confirms that precisely the six stated points are feasible vertices. It evaluates the two formulas and the witness potentials at 39 rational parameters, checks flux/objective identities, and checks the stated monotonicity threshold. A separate numerical six-variable linear-program test on 98 parameter values agreed with the global formula; this numerical test is corroborative and is not the proof for all parameters. The analytic polytope and monotone-supremum arguments above establish the full real parameter interval.

## Relationship to prior work
Hille–Theewis (2023, arXiv:2305.08500v1) study extreme and norming bounded-Lipschitz test functions, explicitly defining the sum-norm Dudley dual. Their finite four-point examples demonstrate difficulties with naive extreme-point criteria but do not identify the positive-flux/monotone-optimizer failure or this exact one-parameter norm phase transition. Hille–Theewis (2022, arXiv:2206.12234v1), §6, give a general finite-dimensional linear-program description for Dudley norms; the present closed two-branch answer and minimal monotonicity counterexample require additional symmetry reduction and an analysis of the monotone subproblem, and are not stated there. Jabłoński–Marciniak-Czochra (2013, arXiv:1304.3501v1) compute the distinct maximum-normalized flat/Fortet–Mourier metric, not the sum-normalized Dudley norm used here. Related finite-star Dudley norm formulas concern non-isometric spaces and do not imply the path transition.

## Limitations
The exact formulas concern a symmetric one-parameter family on a four-site unit path; no universal monotonicity criterion for arbitrary signed measures, non-path metrics, or unequal edge spacings is claimed. Existing general LP formulations already compute finite cases algorithmically, and the contribution is the explicit analytic boundary and minimal positive-flux obstruction, not a new general computational algorithm. An equivalent closed formula in unindexed literature cannot be completely excluded. Independent scientific validation has not been performed.

## References
1. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500v1 (first public 2023-05-15), §§1, 6.
2. S. C. Hille and E. S. Theewis, *Explicit expressions and computational methods for the Fortet–Mourier distance to finite weighted sums of Dirac measures*, arXiv:2206.12234v1 (2022), §6.
3. J. Jabłoński and A. Marciniak-Czochra, *Efficient algorithms computing distances between Radon measures on R*, arXiv:1304.3501v1 (2013), §§2–3.

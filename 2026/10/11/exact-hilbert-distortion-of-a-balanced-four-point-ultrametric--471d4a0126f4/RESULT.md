# Exact Hilbert distortion of a balanced four-point ultrametric

## Finding
For every real parameter \(0<t\leq1\), let \(M_t=\{a_+,a_-,b_+,b_-\}\) carry the two-level ultrametric with
\[
 d(a_+,a_-)=d(b_+,b_-)=t,\qquad
 d(a_\sigma,b_\tau)=1\quad(\sigma,\tau\in\{+,-\}).
\]
Its three-dimensional real Lipschitz-free space has exact Euclidean Banach--Mazur distance
\[
 \boxed{d_{\mathrm{BM}}\!\left(\mathcal F_{\mathbb R}(M_t),\ell_2^3(\mathbb R)\right)^2
 =2+\frac{(1-t)^2}{1-t^2/2}.}
\]
The squared distance decreases strictly from the limiting value \(3\) as \(t\downarrow0\) to \(2\) at \(t=1\). An optimal Euclidean quadratic form on the dual Lipschitz space is explicitly identified below.

## Assumptions and scope
The metric has four distinct points and \(0<t\leq1\). Lipschitz-free spaces and all linear isomorphisms are over the real scalars. The Banach--Mazur distance \(d_{\mathrm{BM}}(X,Y)\) is the infimum of \(\|T\|\|T^{-1}\|\) over invertible linear maps \(T:X\to Y\). The dual of \(\mathcal F_{\mathbb R}(M_t)\) is the three-dimensional space of real Lipschitz functions modulo constants, with norm \(\|f\|_{\mathrm{Lip}}=\max_{i\ne j}|f(i)-f(j)|/d(i,j)\). Finite-dimensional duality preserves distance to a Hilbert space.

Write a function modulo its additive constant as
\[
 (f(a_+),f(a_-),f(b_+),f(b_-))=(u+v,u-v,-u+w,-u-w).
\]
Then direct maximization over cross-pair signs gives
\[
 \|f\|_{\mathrm{Lip}}=\max\left\{\frac{2|v|}{t},\frac{2|w|}{t},2|u|+|v|+|w|\right\}.
\]
Put \(s=t/2\), so \(0<s\leq1/2\). The dual unit ball is
\[
 B_s=\{(u,v,w): |v|\leq s,\ |w|\leq s,\ 2|u|+|v|+|w|\leq1\}.
\]

## Proof
**1. Reduction to invariant Hilbert forms.** Any positive definite quadratic form \(Q\) defines a Euclidean norm \(\sqrt{Q}\). Its squared multiplicative distortion relative to \(\|\cdot\|_{\mathrm{Lip}}\) is
\[
 \frac{\displaystyle\max_{z\in B_s}Q(z)}{\displaystyle\min_{z\in\partial B_s}Q(z)}.
\]
The Lipschitz ball is invariant under independent sign changes of \(v\) and \(w\), and under the interchange \((u,v,w)\mapsto(-u,w,v)\). Averaging \(Q\) over this finite symmetry group retains each of its two-sided comparison inequalities with \(\|\cdot\|_{\mathrm{Lip}}^2\). Thus an optimal form exists of the form \(Q_a(u,v,w)=a u^2+v^2+w^2\) for some \(a>0\), after harmless scalar normalization. This averaging proves optimality among *all* invertible linear Euclidean changes of coordinates, not just diagonal maps.

**2. Exact maximum and minimum for every relevant form.** Since \(Q_a\) increases with \(|u|\) when \((v,w)\) are fixed, its maximum occurs at \(|u|=(1-|v|-|w|)/2\). On the square \((|v|,|w|)\in[0,s]^2\) the resulting quadratic is convex, so its maximum occurs at a corner. Therefore
\[
 \max_{B_s}Q_a=M_s(a):=\max\left\{\frac a4,\frac{a(1-s)^2}{4}+s^2,\frac{a(1-2s)^2}{4}+2s^2\right\}.
\]
The boundary consists of the faces \(|v|=s\), \(|w|=s\), and \(2|u|+|v|+|w|=1\). On either coordinate face, the minimum of \(Q_a\) equals \(s^2\), achieved with the other two coordinates zero. On the remaining faces, with \(|u|=(1-|v|-|w|)/2\), weighted Cauchy--Schwarz gives
\[
 \frac{a(1-|v|-|w|)^2}{4}+v^2+w^2\ \geq\ \frac{a}{2(a+2)}.
\]
Equality requires \(|u|=1/(a+2)\), \(|v|=|w|=a/[2(a+2)]\); the last two values are feasible when \(a\leq4s/(1-2s)\), with the right side understood as infinite at \(s=1/2\). Define the transition
\[
 a_0=\frac{4s^2}{1-2s^2}.
\]
Since \(a_0\leq4s/(1-2s)\), the Cauchy equality is feasible for \(a\leq a_0\). For \(a\geq a_0\), the Cauchy bound itself is at least \(s^2\). Hence the *exact* boundary minimum, for all \(a>0\), is
\[
 m_s(a)=\min\left\{s^2,\frac{a}{2(a+2)}\right\},
\]
and the transition occurs precisely at \(a=a_0\).

**3. Global minimization in the quadratic parameter.** For \(0<a\leq a_0\), the third candidate in \(M_s(a)\) dominates each of the other two. Indeed the comparisons are equivalent to
\[
 a\leq\frac{4s}{2-3s},\qquad a\leq\frac{2s}{1-s},
\]
both valid because \(a\leq a_0\) and \(0<s\leq1/2\). Consequently the distortion squared is
\[
 R_s(a)=\frac{M_s(a)}{m_s(a)}
 =\frac{(1-2s)^2}{2}(a+2)+4s^2\left(1+\frac2a\right).
\]
Its derivative is \((1-2s)^2/2-8s^2/a^2<0\) throughout \(0<a\leq a_0\): for \(s<1/2\), use \(a_0<4s/(1-2s)\), and at \(s=1/2\) negativity is immediate. For \(a\geq a_0\), the denominator \(m_s(a)=s^2\) is fixed and the maximum \(M_s(a)\) of affine functions with nonnegative slopes is nondecreasing. Thus \(a_0\) is a global minimizer. Direct substitution yields
\[
 R_s(a_0)=2+\frac{(1-2s)^2}{1-2s^2}.
\]
Replacing \(2s\) by \(t\) proves the boxed formula. The explicitly optimal dual Hilbert quadratic form is
\[
 Q_*(u,v,w)=\frac{t^2}{1-t^2/2}\,u^2+v^2+w^2.
\]
Finally, the derivative of \((1-t)^2/(1-t^2/2)\) is \((1-t)(t-2)/(1-t^2/2)^2\), which is strictly negative for \(0<t<1\). The stated limiting and endpoint values follow.

## Verification
The proof is analytic, covers the complete continuum of \(t\), and requires no numerical optimization assumption. The standalone standard-library script `verify_ultrametric.py` exactly evaluates the three candidate maxima, transition minimum and optimal formula for 1,800 rational parameter/perturbation tests, using Python rational fractions exclusively. Run `python3 verify_ultrametric.py`; its expected output is `FOUR_POINT_ULTRAMETRIC_EXACT_RATIONAL_OK 1800`. These finite tests supplement but cannot establish the universal result.

## Relationship to prior work
Godard identifies the structure of Lipschitz-free spaces over tree metrics and gives the essential Lipschitz/transport framework [1]. Cúth and Doucha establish an \(\ell_1\)-isomorphic structure for separable ultrametric free spaces and a monotone basis [2], but the inspected theorems do not give this optimal Euclidean distance. Dalet, Kaufmann and Procházka address the isometric-\(\ell_1\) question [3], while Dilworth, Kutzarova and Ostrovskii supply an \(8\)-isomorphism estimate for ultrametrics [4]; neither inspected result specifies this sharp three-dimensional Hilbertian distortion. The formula here is a finer invariant of the smallest two-level symmetric ultrametric, with the exact optimal ellipsoid. The absence of a covering result from the inspected works is not proof of universal novelty.

## Limitations
Only four-point, balanced, two-level ultrametrics with real scalars are classified. The assertion is not an exact Banach--Mazur distance to \(\ell_1\), and no extension to asymmetric clusters, more levels, or arbitrary cardinalities is proved. At \(t=0\) points coalesce, changing the dimension; the value \(3\) is a limit and is not assigned to the collapsed metric. A mathematically equivalent historical convex-body calculation may exist despite targeted literature comparisons.

## References
[1] A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178 (first public version 2009-04-21), https://arxiv.org/abs/0904.3178.

[2] M. Cúth and M. Doucha, *Lipschitz-free spaces over ultrametric spaces*, arXiv:1411.2434 (first public version 2014-11-10), https://arxiv.org/abs/1411.2434.

[3] A. Dalet, P. Kaufmann and A. Procházka, *Characterization of metric spaces whose free space is isometric to \(\ell_1\)*, arXiv:1502.02719 (first public version 2015-02-09), https://arxiv.org/abs/1502.02719.

[4] S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz-free spaces on finite metric spaces*, arXiv:1807.03814, https://arxiv.org/abs/1807.03814.

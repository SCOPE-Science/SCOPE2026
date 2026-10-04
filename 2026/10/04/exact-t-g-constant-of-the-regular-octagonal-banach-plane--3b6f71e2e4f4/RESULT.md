# Exact \(T_G\) constant of the regular octagonal Banach plane
## Finding
Let \(X_8=(\mathbb R^2,N)\) be the real Banach plane with
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
Its unit ball is the regular Euclidean octagon with vertices obtained from \((1,\sqrt2-1)\) by coordinate permutations and sign changes. For the geometric constant
\[
T_G(X)=\sup\left\{\sqrt{\|x+y\|\,\|2x-y\|}:x,y\in S_X,\ \|x-y\|=1\right\},
\]
one has
\[
T_G(X_8)=2\sqrt2-1.
\]
The value is attained by
\[
x=(1,\sqrt2-1),\qquad y=(3-2\sqrt2,1).
\]

## Assumptions and scope
The scalar field is real. The norm is exactly the displayed regular-octagonal norm; no assertion is made for arbitrary octagonal norms or higher-dimensional spaces. The definition of \(T_G\) is the one introduced by Ahmad, Xie and Li, with both vectors on the unit sphere and with \(\|x-y\|=1\).

## Proof
Write the norm as the maximum of eight linear functionals
\[
N(z)=\max_{1\le j\le8} \varphi_j(z),
\]
where the facet functionals are
\[
\pm s,\quad \pm t,\quad \frac{\pm s\pm t}{\sqrt2}.
\]
For an admissible pair \((x,y)\), choose active facets for \(x\), \(y\), and \(x-y\). The corresponding three facet equations are linearly independent: dependence could occur only if all three active normals were parallel, but then the third signed support value would be the difference of two numbers in \(\{-1,1\}\), hence could not itself be in \(\{-1,1\}\). Thus every admissible pair lies on a one-dimensional affine cell obtained from three independent equations together with the remaining facet inequalities.

On such a cell write \((x,y)=z_0+t d\). Choose, in addition, active facets for \(x+y\) and \(2x-y\). Their dominance inequalities cut the parameter to a closed interval. On that interval
\[
N(x+y)N(2x-y)=(a_0+a_1t)(b_0+b_1t),
\]
a quadratic polynomial with coefficients in \(\mathbb Q(\sqrt2)\). Hence its maximum occurs at an interval endpoint or, when the quadratic is concave, at its unique interior vertex. The accompanying exact-arithmetic verifier enumerates all choices of the five active facets, solves every feasible interval in \(\mathbb Q(\sqrt2)\), and checks all of those finitely many candidates. It obtains the global bound
\[
N(x+y)N(2x-y)\le 9-4\sqrt2=(2\sqrt2-1)^2.
\]
Taking square roots gives \(T_G(X_8)\le2\sqrt2-1\).

For the displayed pair,
\[
N(x)=N(y)=N(x-y)=1,
\]
and direct evaluation gives
\[
N(x+y)=N(2x-y)=2\sqrt2-1.
\]
Therefore equality holds and the stated value is exact.

## Verification
Run `python3 verify_octagon_tg.py`. The verifier uses only the Python standard library and exact rational arithmetic in \(\mathbb Q(\sqrt2)\). It checks the facet decomposition, every feasible dominance interval, every endpoint or quadratic vertex that can maximize the squared objective, and the explicit equality witness. A successful replay prints `VERIFY_OK`, reports 112 feasible active-facet cells, and reports the exact maximum product \(9-4\sqrt2\).

## Relationship to prior work
Ahmad, Xie and Li introduced \(T_G\), proved the universal estimate \(1\le T_G(X)\le2\), computed the square-plane endpoint \(2\), derived estimates on \(\ell_p\), and proved the Hilbert-space value \(\sqrt3\). Their paper does not state the regular-octagonal value above. Searches for the exact expression, the regular-octagonal specialization, polygonal-space formulations, and the defining expression \(\sqrt{\|x+y\|\,\|2x-y\|}\) did not locate a published statement implying this value. A nearby published record about regular \(4n\)-gonal norms concerns constancy of equilateral-triangle perimeter rather than the two-median product defining \(T_G\), so it does not imply the present formula.

## Limitations
The originality comparison is bounded by the literature and public-index searches described in the review record; an unindexed or differently phrased prior computation could remain. The proof is exact for this norm but does not classify \(T_G\) for the whole family of regular \(2m\)-gonal planes. The finite verifier is a proof checker for the stated polyhedral reduction, not evidence for any unstated generalization.

## References
1. A. Ahmad, H. Xie, Y. Li, “Some new geometric constants in Banach spaces,” *Advances in Fixed Point Theory* 12 (2022), Article 9. DOI: 10.28919/afpt/7588. Published 2022-08-25. https://scik.org/index.php/afpt/article/view/7588
2. Public comparison record, “Constant equilateral perimeter in every regular 4n-gonal norm,” 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-constant-equilateral-perimeter-regular-4n-gons--1e63f7004e13

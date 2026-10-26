# Optimal symmetric four-node cubic interpolation for monotone range control

## Finding
For each \(0<a<1\), let \(P_{a,y}\) be the unique polynomial of degree at most three that takes the data \(0\le y_0\le y_1\le y_2\le y_3\le1\) at the ordered nodes \((-1,-a,a,1)\). Define the worst excursion outside the prescribed data bounds by
\[
\Delta(a)=\max_{y,\,-1\le x\le1}\max\{ -P_{a,y}(x),\ P_{a,y}(x)-1,\ 0\}.
\]
Set \(s(a)=\sqrt{1+3a^2}\) and \(q(a)=1+a+a^2\). The **exact global monotone-data defect** is
\[
\boxed{\Delta(a)=\max\{E(a),H(a)\}},\qquad
E(a)=\frac{(s(a)-1)(s(a)+2)}{9(2-s(a))},\qquad
H(a)=\frac{q(a)^{3/2}}{3\sqrt3\,a(1+a)}-\frac12.
\]
The first branch comes from a terminal step in the data, while the second comes from a central step. Both are attained at explicitly specified interior evaluation points. There is a **unique** \(a_*\in(0,1)\) minimizing \(\Delta(a)\), characterized exactly by \(E(a_*)=H(a_*)\). Certified rational bounds give
\[
\boxed{0.4458209224<a_*<0.4458209226,\qquad
\Delta(a_*)=0.1296867734\ldots.}
\]
Thus among all symmetric four-node grids with fixed endpoints, this and only this node placement minimizes the largest possible range violation for bounded nondecreasing observations. It is strictly better for this objective than the four Chebyshev–Lobatto nodes \(a=1/2\), where
\[
\Delta(1/2)=\frac{10+7\sqrt7}{162}=0.1760509825\ldots,
\]
and equally spaced nodes \(a=1/3\), where
\[
\Delta(1/3)=\frac{13\sqrt{39}}{108}-\frac12=0.2517127220\ldots.
\]

## Assumptions and scope
The nodes \((-1,-a,a,1)\) are strictly ordered and symmetric. The optimization runs over **all** four scalar, nondecreasing sample vectors in \([0,1]^4\), including step vectors, and the entire closed interpolation interval \([-1,1]\). The claim is an exact worst-case range estimate, not a claim that the cubic interpolant itself is nondecreasing. By affine scaling, the same dimensionless constant applies to any segment with two equally placed interior nodes relative to its midpoint and endpoints, and to any data interval of positive length after rescaling.

No optimization over asymmetric grids or higher degrees is asserted. The result concerns unmodified global four-point Lagrange interpolation, not a Hermite interpolant, a rational interpolant, a spline with chosen derivatives, or interpolation restricted to the middle cell.

## Proof
Let \(L_j\), \(0\le j\le3\), denote the four cardinal polynomials. Each admissible data vector is a convex combination of the zero vector, the all-one vector, and the three step vectors \(v^{(k)}_j=\mathbf1_{j\ge k}\) for \(k=1,2,3\): explicitly the nonnegative coefficients are \(1-y_3\), \(y_0\), and \(y_k-y_{k-1}\). Hence for any fixed evaluation point the extremal interpolated value occurs on one of these five vectors.

For the last step \(v^{(3)}\), the interpolant is
\[
T_a(x)=L_3(x)=\frac{(x+1)(x^2-a^2)}{2(1-a^2)}.
\]
It is nonnegative on \([-1,-a]\cup[a,1]\), nonpositive on \([-a,a]\), and never exceeds one: the inequalities \(0\le x+1\le2\) and \(0\le x^2-a^2\le1-a^2\) suffice on its nonnegative region. Its derivative is
\[
T_a'(x)=\frac{3x^2+2x-a^2}{2(1-a^2)},
\]
whose unique root in \((-a,a)\) is
\[
r_a=\frac{\sqrt{1+3a^2}-1}{3}\in(0,a).
\]
(The other root lies to the left of \(-a\).) This root gives the global minimum of \(T_a\) over \([-1,1]\); using \(a^2=3r_a^2+2r_a\),
\[
-T_a(r_a)=\frac{r_a(1+r_a)^2}{1-a^2}=E(a).
\]
By reflection, the first step has interpolant \(1-T_a(-x)\), with the corresponding sharp excess \(E(a)\).

For the middle step \(v^{(2)}=(0,0,1,1)\), symmetry gives
\[
U_a(x)=L_2(x)+L_3(x)
=\frac12+\frac{x(q(a)-x^2)}{2a(1+a)},\qquad U_a(-x)=1-U_a(x).
\]
Its derivative vanishes at \(x=\pm t_a\), where \(t_a=\sqrt{q(a)/3}\) satisfies \(a<t_a<1\). Therefore the exact largest value is
\[
U_a(t_a)=\frac12+\frac{q(a)^{3/2}}{3\sqrt3\,a(1+a)}=1+H(a),
\]
and the exact minimum is \(U_a(-t_a)=-H(a)\). Taking the convex hull of the five step interpolants proves the formula for \(\Delta(a)\), with both branch values sharp.

To minimize the envelope, note that \(s(a)\) strictly increases from one to two and the positive expression \((s-1)(s+2)/(9(2-s))\) strictly increases with \(s\), so \(E(a)\) strictly increases from zero to infinity. For \(H(a)+1/2>0\), logarithmic differentiation gives
\[
\frac{d}{da}\log\bigl(H(a)+\tfrac12\bigr)
=\frac{(1+2a)(a^2+a-2)}{2a(1+a)(1+a+a^2)}<0
\]
on \((0,1)\). Thus \(H(a)\) strictly decreases from infinity to zero. Consequently their graphs cross exactly once; to the left of the crossing \(\Delta=H\) strictly decreases, and to the right \(\Delta=E\) strictly increases. The unique crossing is the unique global minimizer. The rational enclosure and quoted approximations are reproducible from the accompanying `verify.py`, whose rational square-root intervals certify the crossing signs without floating-point assumptions. The two special-grid expressions follow by substitution.

## Verification
Running `python verify.py` (Python 3.10+ with SymPy) reconstructs all four Lagrange cardinal polynomials symbolically; verifies partition of unity, the step-reflection identities, and derivative formulas; and certifies with rational interval arithmetic that the crossing lies in \((0.4458209224,0.4458209226)\). It separately compares equally spaced, Chebyshev–Lobatto, and other rational choices, and performs a deterministic supplementary sampling test. The proof of universality and uniqueness above is analytic and **does not** rely on the finite sampling.

## Relationship to prior work
Berrut and Trefethen (2004) establish the classical Lagrange/barycentric representations, describe Chebyshev node sets, and discuss the Lebesgue norm as a measure of unrestricted interpolation stability. Their analysis does not optimize the **monotone-cone range excursion**; minimizing that restricted defect is a distinct objective from choosing a grid for ordinary Lebesgue-constant control. Fritsch and Carlson (1980) develop shape-preserving piecewise cubic Hermite methods rather than determining the worst range defect of an unmodified global cubic.

A published result on four uniformly spaced nodes derives a sharp defect only over the **middle cell**, and explicitly excludes nonuniform nodes. Consequently its \(\sqrt3/27\) local constant is neither the full-interval defect at the uniform grid nor a minimax result across symmetric nonuniform grids. A previously recorded four-node Chebyshev–Lobatto constant is the single-grid case \(a=1/2\) of the formula here, not a determination of the function \(\Delta(a)\) or its unique optimizing parameter. Searches did not identify a stronger statement covering this full parameter family and minimax objective; small-degree equivalent calculations may exist outside indexed sources.

## Limitations
The result establishes exact range excursions for the symmetric four-node family only. It does not prove asymmetry cannot improve the best defect, preservation of monotonicity between nodes, accuracy for smooth input functions, or optimality under an unrestricted Lebesgue norm. The data step witnesses are admissible nondecreasing arrays; strictly increasing arrays can approximate their sharp values but need not attain equality. General interpolation surveys and numerical-stability work may contain unindexed, algebraically equivalent special cases that remain an originality risk.

## References
1. J.-P. Berrut and L. N. Trefethen, *Barycentric Lagrange Interpolation*, SIAM Review **46** (2004), 501–517, DOI: 10.1137/S0036144502417715. Public full text: https://people.maths.ox.ac.uk/trefethen/barycentric.pdf (published electronically 2004-07-30).
2. F. N. Fritsch and R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM Journal on Numerical Analysis **17** (1980), 238–246, DOI: 10.1137/0717021.
3. *Sharp monotone range defect of uniform four-point cubic Lagrange interpolation*, publicly searchable research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-monotone-range-defect-of-uniform-four-point-cubic-lagrange--1fad48a6c445 (uniform, middle-cell result only).

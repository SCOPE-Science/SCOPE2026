# Sharp monotone range of four-node Chebyshev–Lobatto cubic interpolation

## Finding
For the four ordered Chebyshev–Lobatto nodes \(-1,-1/2,1/2,1\), let \(P_y\) be the unique polynomial of degree at most three taking prescribed values \(0\le y_0\le y_1\le y_2\le y_3\le 1\). The smallest possible uniform bound valid for every such data vector and every evaluation point \(x\in[-1,1]\) is
\[
-\delta\le P_y(x)\le1+\delta,
\qquad \delta=\frac{10+7\sqrt7}{162}=0.176050982576865\ldots.
\]
The lower equality occurs only for the step \(y=(0,0,0,1)\) and the location \(x_*=-1/3+\sqrt7/6\). The upper equality occurs only for the reflected complementary step \(y=(0,1,1,1)\) at \(-x_*\). Strictly increasing data with values in \([0,1]\) can approach both bounds arbitrarily closely.

For the comparably scaled equally spaced nodes \(-1,-1/3,1/3,1\), the analogous **global** optimal defect is
\[
\delta_{\mathrm{eq}}=\frac{13\sqrt{39}}{108}-\frac12
=0.251712722029436\ldots >\delta.
\]
Thus the standard endpoint-clustered cubic node set has a strictly smaller worst-case range excursion than the equally spaced cubic node set, although neither interpolant preserves the data range.

## Assumptions and scope
All functions and data are real. Interpolation is the ordinary degree-at-most-three Lagrange polynomial on the whole closed interval \([-1,1]\), **not** a local spline or a shape-preserving nonlinear rule. The data satisfy only the stated monotonicity and amplitude inequalities; continuity or differentiability of any generating function is unnecessary. The endpoint cluster is the degree-three Chebyshev–Lobatto grid (Chebyshev extrema). Affine changes of the interval preserve the dimensionless constants.

## Proof
Let \(L_0,L_1,L_2,L_3\) be the cardinal polynomials. Write the data through nonnegative increments
\[
a=y_0,\quad d_1=y_1-y_0,\quad d_2=y_2-y_1,\quad d_3=y_3-y_2,
\qquad a+d_1+d_2+d_3\le1.
\]
The Lagrange partition of unity yields
\[
P_y(x)=a+d_1 S_1(x)+d_2 S_2(x)+d_3 S_3(x),
\qquad S_j(x)=\sum_{i=j}^{3}L_i(x).
\]
For each fixed \(x\), all possible values therefore lie in the convex hull of \(0,1,S_1(x),S_2(x),S_3(x)\); the extrema for all bounded monotone data are consequently attained at a step vector. Direct cardinal-polynomial calculation gives
\[
S_1(x)=\frac{(x+1)(4x^2-8x+7)}6,
\quad S_2(x)=-\frac{(x+1)(2x-3)(2x+1)}6,
\quad S_3(x)=\frac{(x+1)(2x-1)(2x+1)}6.
\]
The symmetries are \(S_1(x)=1-S_3(-x)\) and \(S_2(x)=1-S_2(-x)\). Also \(S_1\ge0\) on the interval because \(4x^2-8x+7=4(x-1)^2+3>0\).

Differentiation gives the only two interior stationary points of \(S_2\) as \(\pm\sqrt{21}/6\). Its exact minimum and maximum are
\[
\min S_2=\frac12-\frac{7\sqrt{21}}{54},
\qquad \max S_2=\frac12+\frac{7\sqrt{21}}{54}.
\]
For \(S_3\), the only interior stationary points are \(-1/3\pm\sqrt7/6\). At the positive one,
\[
S_3(-1/3+\sqrt7/6)=-\frac{10+7\sqrt7}{162}=-\delta;
\]
at the negative one \(S_3=(-10+7\sqrt7)/162\), which lies between zero and one. The endpoint values of \(S_3\) are zero and one. Hence \(\min S_3=-\delta\) and \(\max S_3=1\), with the minimum unique. The other possible negative excursion, from \(S_2\), has magnitude \(\delta_2=7\sqrt{21}/54-1/2\), strictly less than \(\delta\). For an exact comparison, \(\sqrt{21}<5\) gives \(\delta_2<4/27\), whereas \(\sqrt7>2\) gives \(\delta>4/27\). Reflection gives \(\max S_1=1+\delta\) uniquely at \(-x_*\). This proves the global bounds. Strict inequality against every other vertex of the monotone-data simplex at the extremizing point gives uniqueness of the data vector and evaluation location.

On the equispaced four-node grid, the middle step polynomial is
\[
S_2^{\mathrm{eq}}(x)=-\frac{(x+1)(3x-4)(3x+1)}8.
\]
Its minimum is \(1/2-13\sqrt{39}/108\) at \(-\sqrt{39}/9\), and its maximum is the reflected positive counterpart. The other two step polynomials have extremal excursions only \(\sqrt3/27\), strictly smaller than \(\delta_{\mathrm{eq}}\). The identical convex-simplex argument yields the stated equal-grid comparison.

## Verification
The standalone `verify.py` reconstructs both four-node Lagrange bases with exact rational coefficients, checks all displayed polynomial identities, computes every stationary point and endpoint value symbolically, verifies the unique sharpness witnesses, and verifies the comparison of the two exact global constants. Execute with `python verify.py` after installing SymPy. The script returned `PASS` during this analysis. Finite sampling is not used in the proof of any universal statement; the analytic reduction to the data simplex and complete cubic critical-point analysis are exhaustive.

## Relationship to prior work
Berrut and Trefethen (2004) develop barycentric interpolation and specifically identify the second-kind Chebyshev grid as a standard well-conditioned interpolation grid; their relevant discussion gives no evaluated sharp monotone-data range constant. Fritsch and Carlson (1980) formulate conditions and procedures for monotone **piecewise Hermite interpolation**; their shape-preserving nonlinear construction is not the unmodified four-node Lagrange polynomial. An accessible 2026 result determines the exact range on the **central cell only** of the equispaced four-node cubic; it does not cover nonuniform Chebyshev–Lobatto nodes or the entire interval. The equal-grid global defect computed here is used as a comparison, not as an asserted separate discovery. The central-cell value is \(\sqrt3/27\), whereas the global equal-grid value is larger.

## Limitations
This is an exact finite four-node calculation, not an asymptotic theorem, not a bound uniform in interpolation degree, and not proof that Chebyshev–Lobatto nodes are optimal among all possible four-node configurations. It does not establish monotonicity of the interpolant. Classical interpolation sources or tabulations might implicitly contain the same algebraic values without using this range formulation; the novelty assessment is not independent certification. The bibliographic search checked pertinent accessible results and did not exhaust every historical monograph.

## References
1. J.-P. Berrut and L. N. Trefethen, *Barycentric Lagrange Interpolation*, SIAM Review 46 (2004), 501–517, DOI: 10.1137/S0036144502417715; first electronic publication 2004-07-30. Open full text: https://people.maths.ox.ac.uk/trefethen/barycentric.pdf.
2. F. N. Fritsch and R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM Journal on Numerical Analysis 17 (1980), 238–246, DOI: 10.1137/0717021.
3. *Sharp monotone range defect of uniform four-point cubic Lagrange interpolation*, publicly accessible result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-monotone-range-defect-of-uniform-four-point-cubic-lagrange--1fad48a6c445, specifically restricted to the central cell.

# Sharp range envelope for bivariate quadratic interpolation of monotone \(3\times3\) data

## Finding
Let \(f=(f_{ij})_{0\le i,j\le 2}\) be a real array such that \(0\le f_{ij}\le1\), \(f_{ij}\le f_{i+1,j}\), and \(f_{ij}\le f_{i,j+1}\) wherever indices are defined. Let \(P_f\) be its tensor-product degree-two Lagrange interpolant at the nine nodes \((i/2,j/2)\). The **exact** complete-square range enclosure is
\[
-\frac{17}{64}\;\le\; P_f(x,y)\;\le\;\frac{81}{64},\qquad (x,y)\in[0,1]^2.
\]
The constants are attained. In particular, monotonicity of every row and column does not preclude overshoot by \(17/64\) of the observed data range.

For a general nondegenerate sample range \([m,M]\), affine normalization yields the sharp enclosure \([m-17(M-m)/64,\ M+17(M-m)/64]\). The same numerical constant is a sharp supremum under *strict* coordinatewise increase, by approximation of the weakly increasing extremizer.

## Assumptions and scope
The domain is the **entire** closed unit square, the nine interpolation nodes are the Cartesian product of \(\{0,1/2,1\}\) with itself, interpolation is global tensor-product Lagrange interpolation (not piecewise interpolation), and monotonicity is the usual coordinatewise partial order on the nodal array. Data need not satisfy nonnegative mixed second differences. This is a two-dimensional theorem only; no higher-dimensional bound is asserted.

## Proof
The three univariate cardinal functions are
\[
\ell_0(t)=(1-t)(1-2t),\qquad \ell_1(t)=4t(1-t),\qquad \ell_2(t)=t(2t-1),
\]
with \(\ell_0+\ell_1+\ell_2=1\), and
\[
P_f(x,y)=\sum_{i=0}^2\sum_{j=0}^2\ell_i(x)\ell_j(y)f_{ij}.
\]
For \(0\le t\le1/2\), the only possibly negative cardinal coefficient is \(\ell_2(t)=-a(t)\), where \(a(t)=t(1-2t)\in[0,1/8]\). The other coefficients are nonnegative and sum to \(1+a(t)\). For \(1/2\le t\le1\), the only possibly negative coefficient is \(\ell_0(t)=-b(t)\), where \(b(t)=(1-t)(2t-1)\in[0,1/8]\). The other coefficients are nonnegative and sum to \(1+b(t)\). These bounds follow by completing squares (the maxima occur at \(t=1/4\) and \(t=3/4\), respectively).

**One-dimensional fact.** If \(0\le v_0\le v_1\le v_2\le1\) and \(t\ge1/2\), then
\[
0\le\sum_j\ell_j(t)v_j=v_0+\ell_1(t)(v_1-v_0)+\ell_2(t)(v_2-v_0)\le1+b(t).
\]
The first inequality uses \(\ell_1,\ell_2\ge0\); the second discards the nonpositive \(\ell_0v_0\) term and bounds the two positive terms by their coefficient sum.

**If \(y\ge1/2\).** Apply the one-dimensional fact to each monotone row to get \(0\le g_i=\sum_j\ell_j(y)f_{ij}\le1+b(y)\). In the remaining \(x\)-interpolation, at most one coefficient is negative, of magnitude at most \(1/8\). Consequently \(P_f(x,y)\ge-(1/8)(1+1/8)=-9/64\), regardless of which half of the interval contains \(x\). By symmetry, if \(x\ge1/2\) and \(y<1/2\), the same bound holds after interpolating along the columns first.

**If \(x,y\le1/2\).** Put \(a=a(x)\), \(b=a(y)\), \(p_i=\ell_i(x)\ge0\), \(q_j=\ell_j(y)\ge0\) for \(i,j\in\{0,1\}\). Then \(\sum_{i<2}p_i=1+a\), \(\sum_{j<2}q_j=1+b\), and
\[
P_f=\sum_{i,j<2}p_iq_j f_{ij}-b\sum_{i<2}p_i f_{i2}-a\sum_{j<2}q_j f_{2j}+ab f_{22}.
\]
The first sum is nonnegative. Isotonicity gives \(f_{i2}\le f_{22}\) and \(f_{2j}\le f_{22}\), so
\[
P_f\ge\bigl[-b(1+a)-a(1+b)+ab\bigr]f_{22}=-(a+b+ab)f_{22}\ge-(a+b+ab)\ge-\frac{17}{64}.
\]
The preceding cases cover all \((x,y)\in[0,1]^2\).

To obtain the upper bound, define \(h_{ij}=1-f_{2-i,2-j}\). Then \(h\) is again coordinatewise nondecreasing with entries in \([0,1]\), and \(\ell_i(1-t)=\ell_{2-i}(t)\) gives \(P_h(x,y)=1-P_f(1-x,1-y)\). Applying the lower bound to \(h\) yields \(P_f\le1+17/64=81/64\).

For sharpness, set \(f_{ij}=1\) exactly when \(i=2\) or \(j=2\), and \(f_{ij}=0\) otherwise. At \(x=y=1/4\), \((\ell_0,\ell_1,\ell_2)=(3/8,3/4,-1/8)\) and hence
\[
P_f(1/4,1/4)=1-\bigl(\ell_0(1/4)+\ell_1(1/4)\bigr)^2=1-(9/8)^2=-17/64.
\]
The reflected complement \(h\) attains the upper bound at \((3/4,3/4)\). The strictly increasing arrays \(f^{(\varepsilon)}_{ij}=(1-\varepsilon)f_{ij}+\varepsilon(i+j)/4\) for \(0<\varepsilon<1\) converge to the lower witness and have strictly increasing rows and columns, proving sharpness in the limiting sense for strict monotonicity. This completes the proof.

## Verification
The standalone `check_q2.py` uses exact rational arithmetic for all twenty upper-ideal zero-one arrays (the vertices of the order-polytope of the \(3\times3\) grid), checks all mesh points whose coordinates are integer multiples of \(1/16\), and evaluates the two sharpness witnesses exactly. These finite checks support the implementation and arithmetic; the proof above, not the finite enumeration, establishes the bound on the continuum.

## Relationship to prior work
The classical Lagrange basis and unconstrained Lebesgue-constant framework are described in Berrut–Trefethen [1], especially §§2 and 9.1. For unconstrained data the tensor-product Lebesgue constant of the uniform quadratic interpolant is \((5/4)^2=25/16\), allowing a lower excursion \(-9/32\). The restriction to isotone data improves this to the exact \(-17/64\); it is a different extremal problem from the unrestricted norm. Floater–Peña [2] study monotonicity preservation for tensor-product bases such as Bernstein polynomials and B-splines; their accessible abstract does not establish the present sharp range envelope for the global biquadratic Lagrange operator. Published one-dimensional sharp range-defect results for cubic Lagrange and rational interpolation likewise do not imply this two-dimensional constant. This comparison is based on inspected material, not a claim that unexamined literature is absent.

## Limitations
The theorem is confined to three uniform nodes in each of two variables and separately monotone bounded data. It does not characterize arbitrary node placement, higher degrees, dimensions above two, or monotonicity of the interpolating surface itself. The full Floater–Peña [2] paper was not accessible during the comparison, so a prior equivalent quantitative result cannot be excluded categorically. No independent mathematical audit has been performed.

## References
[1] Jean-Paul Berrut and Lloyd N. Trefethen, *Barycentric Lagrange Interpolation*, SIAM Review 46 (2004), 501–517, DOI 10.1137/S0036144502417715; author-hosted full text https://people.maths.ox.ac.uk/trefethen/barycentric.pdf; electronically published 2004-07-30.

[2] Michael S. Floater and Juan Manuel Peña, *Tensor-product monotonicity preservation*, Advances in Computational Mathematics 9 (1998), 353–362, DOI 10.1023/A:1018906027191; accessible abstract https://www.sciweavers.org/publications/tensor-product-monotonicity-preservation, full text not inspected.

[3] Timbwaoga A. J. Ouermi, Robert M. Kirby, Martin Berzins, *ENO-Based High-Order Data-Bounded and Constrained Positivity-Preserving Interpolation*, arXiv:2204.06168 (2022); relevant motivation on positivity and bounds in two-dimensional gridded interpolation, abstract inspected.

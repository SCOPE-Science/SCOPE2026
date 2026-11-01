# Sharp coordinatewise Lipschitz transition for Euclidean Lorentz-cone projection

## Finding
For every integer \(d\ge1\), let \(Q_d\) be the Euclidean nearest-point projection from \(\mathbb R^{d+1}\) onto the Lorentz cone \(K_d=\{(t,x):t\ge\|x\|_2\}\). Measure the errors of this **Euclidean** projector in the coordinate maximum norm, and write
\[
L_d=\sup_{z\ne z'}\frac{\|Q_d(z)-Q_d(z')\|_\infty}{\|z-z'\|_\infty}.
\]
Then \(L_1=1\). For each \(d\in\{2,3,4\}\), let \(a_d\in(0,1)\) be the unique zero of
\[
1-2a+\sqrt{d-1}\frac{1-2a^2}{\sqrt{1-a^2}}=0.
\]
The sharp constants are
\[
L_d=1+\frac{a_d-a_d^2+\sqrt{d-1}a_d\sqrt{1-a_d^2}}2\quad(2\le d\le4),
\qquad L_d=\frac{1+\sqrt d}{2}\quad(d\ge5).
\]
Thus the largest derivative row switches from a spatial output coordinate to the axial output at the exact threshold \(d=5\). The sequence grows like \(\sqrt d/2\), although the same Euclidean metric projection is one-Lipschitz in the Euclidean norm. Numerical values are \(L_2\approx1.361179\), \(L_3\approx1.463036\), \(L_4\approx1.541623\), and \(L_5=(1+\sqrt5)/2\).

## Assumptions and scope
All spaces, vectors, norms and derivatives are real. The integer \(d\) counts the **spatial** coordinates, so the full ambient dimension is \(d+1\). The source and target map is always Euclidean nearest-point projection, not an arbitrary metric projection for the maximum norm. The Lipschitz constant is a supremum of quotients at distinct inputs; sharpness follows from local derivatives, without requiring one finite pair to attain the supremum. In the formula for \(a_d\), uniqueness is proved below.

## Proof
**1. Projection and derivatives.** Write \(r=\|x\|_2\). The standard Euclidean Lorentz-cone projection, also verified directly by the Hilbert projection optimality inequality, is
\[
Q_d(t,x)=\begin{cases}
(t,x),&t\ge r,\\
(0,0),&t\le-r,\\
((t+r)/2,(t+r)x/(2r)),&-r<t<r.
\end{cases}
\]
In the open middle region let \(\lambda=t/r\in(-1,1)\) and \(u=x/r\), so \(\|u\|_2=1\). Differentiation yields
\[
DQ_d(t,x)=\frac12\begin{pmatrix}1&u^{\mathsf T}\\u&(1+\lambda)I_d-\lambda uu^{\mathsf T}\end{pmatrix}.
\]
The other open regions have Jacobian \(I\) and \(0\). Since \(Q_d\) is globally Euclidean-Lipschitz and is piecewise smooth, its restriction to any segment is absolutely continuous. The chain rule applies almost everywhere, and integrating its derivative bounds the maximum-norm Lipschitz constant by the supremum of absolute Jacobian row sums. Conversely, the derivative at each open middle-region point bounds the global Lipschitz quotient from below by local perturbations in a row-sign direction. The full sharp constant therefore equals the maximum of \(1\) and the suprema of these row sums.

**2. Axial and spatial rows.** The axial row sum is \((1+\|u\|_1)/2\), with sharp maximum \(A_d=(1+\sqrt d)/2\), realized as a derivative row when all spatial coordinates have equal magnitude. For spatial row \(i\), put \(a=|u_i|\), \(R=\sum_{j\ne i}|u_j|\); then its absolute sum is
\[
S_i(\lambda)=\frac12\bigl(a+1+\lambda-\lambda a^2+|\lambda|aR\bigr).
\]
For \(-1\le\lambda\le0\) and \(0\le\lambda\le1\) this is affine. The value at \(\lambda=1\) is at least that at \(\lambda=0\) and exceeds or equals that at \(\lambda=-1\) by \(1-a^2\); hence the supremum over \(\lambda\in(-1,1)\) is its limiting value at \(1\). Cauchy--Schwarz gives \(R\le\sqrt{(d-1)(1-a^2)}\), with equality possible when the other coordinate magnitudes are equal. Consequently, the sharp spatial row constant is
\[
F_d=1+\frac12\max_{0\le a\le1}g_d(a),\qquad
 g_d(a)=a-a^2+\sqrt{d-1}a\sqrt{1-a^2}.
\]
For \(d=1\), \(g_1(a)=a-a^2\), but there are no 'other' spatial coordinates, so necessarily \(a=1\), giving the correct value \(L_1=1\). For \(d\ge2\), direct differentiation gives
\[
g_d'(a)=1-2a+\sqrt{d-1}\frac{1-2a^2}{\sqrt{1-a^2}},\quad
g_d''(a)=-2+\sqrt{d-1}\frac{a(2a^2-3)}{(1-a^2)^{3/2}}<-2
\]
for \(0<a<1\). The derivative begins positive and tends to negative infinity at the right endpoint, yielding a unique maximizer \(a_d\in(0,1)\).

**3. Exact phase transition.** For \(d=2,3,4\), the trial \(a=2/3\) gives \(F_d\ge(10+\sqrt{5(d-1)})/9>(1+\sqrt d)/2=A_d\), so spatial rows strictly dominate. For \(d\ge5\), define \(h_d(a)=\sqrt d-1-g_d(a)\). Its derivative with respect to the real parameter \(d\) satisfies
\[
\partial_d h_d(a)=\frac1{2\sqrt d}-\frac{a\sqrt{1-a^2}}{2\sqrt{d-1}}>0 \quad(d\ge5),
\]
since \(a\sqrt{1-a^2}\le1/2\). Therefore it is enough to establish \(h_5(a)>0\) uniformly. Since \(g_5''\le-2\), Taylor's strong-concavity bound around \(a_0=2/3\) gives
\[
\max_{0\le a\le1}g_5(a)\le g_5(2/3)+\frac{g_5'(2/3)^2}{4}.
\]
The residual is strictly positive:
\[
\sqrt5-1-g_5(2/3)-\frac{g_5'(2/3)^2}{4}
=\frac{26\sqrt5}{45}-\frac{229}{180}>0.
\]
Thus \(F_d<A_d\) for every \(d\ge5\). Combining the row calculations proves all formulas and the asserted phase switch. \(\square\)

## Verification
The standalone standard-library script `verify.py` evaluates the exact projection map, middle-region Jacobians, limiting sign directions, and global sampled perturbation ratios, with tests over all integers \(1\le d\le20\). It reports 8,020 successful numerical assertions. Run `python3 verify.py` in a directory containing this document and the script. These tests are corroboration, not substitutes for the all-dimensional inequalities above.

## Relationship to prior work
Németh (2012) studies Euclidean metric projections onto cones in Hilbert geometry, particularly cone-order and duality properties, rather than sharp coordinate-maximum Lipschitz moduli. Németh and Zhang (2014) address extended Lorentz-cone isotonicity. A published calculation of nearest-point projections *in an \(\ell_p\) ambient metric* onto Lorentz cones is not a result about the same projector measured in the \(\ell_\infty\) norm. An exact sensitivity formula for Euclidean-ball clipping concerns a different convex target; it neither gives the spatial-row branch nor implies the dimension-five transition found here. These comparisons do not exclude an older equivalent calculation in conic-programming sensitivity literature.

## Limitations
The result applies to Euclidean metric projection onto the standard unweighted real Lorentz cone. It does not cover non-Euclidean metric projections, weighted coordinate norms, general second-order-cone linear images, or arbitrary convex cones. The norm is a global supremum; no assertion about attained distinct-input pairs is made. The historical novelty assessment is conditional on the inspected sources and may be revised after broader specialist comparison.

## References
1. S. Z. Németh, *A duality between metric projection onto a convex cone and its dual in Hilbert spaces*, arXiv:1212.5438 (first public version 2012-12-21), https://arxiv.org/abs/1212.5438 .
2. S. Z. Németh and G. Zhang, *Extended Lorentz cones and mixed complementarity problems*, arXiv:1405.7835 (first posted 2014-05-30), https://arxiv.org/abs/1405.7835 .
3. *Exact planar stability and nonexpansivity rigidity for \(\ell_p\) projections onto scaled Lorentz cones*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-planar-stability-and-nonexpansivity-rigidity-for-ell-p-pro--fbfc40872e9c .
4. *Sharp weighted coordinate sensitivity of Euclidean-ball clipping*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-weighted-coordinate-sensitivity-of-euclidean-ball-clipping--78696bf157c3 .

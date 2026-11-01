# Sharp squeezing transition for three rotated Gaussian ambiguity windows

## Finding

For three unit-norm Gaussian short-time Fourier windows whose covariance ellipses are rotated by angles \(0,\pi/3,2\pi/3\), consider the smallest sum of their positive symmetric ambiguity functions on the closed time-frequency disk of radius \(R>0\). Allow the common squeezing parameter \(a\ge1\), and put \(T=\pi R^2/2\). There is a sharp transition at \(T=2\), equivalently at \(R=2/\sqrt\pi\): the uniquely optimal squeezing is \(a=1\) for \(0<T\le2\), whereas for \(T>2\) a unique optimizer \(a_T>1\) improves the uniform ambiguity denominator strictly. It satisfies an explicit scalar equation and \(a_T\to\sqrt3\) as \(T\to\infty\).

More precisely, set
\[
 h(y)=\frac{1-e^{-3y/2}}{2+e^{-3y/2}},\qquad
 \mathcal T(y)=\frac{y\sqrt{1-h(y)^2}}{h(y)}\quad(y>0).
\]
The function \(\mathcal T\) is strictly increasing from \(2\) to \(+\infty\). For \(T>2\), the unique \(y_T>0\) satisfying \(\mathcal T(y_T)=T\) determines
\[
 a_T=\sqrt{1+(y_T/T)^2}+y_T/T.
\]
The exact maximized uniform denominator is \(3e^{-T}\) if \(T\le2\), and otherwise
\[
 \exp[-\sqrt{T^2+y_T^2}]\bigl(e^{-y_T}+2e^{y_T/2}\bigr).
\]

## Assumptions and scope

For \(a>0\), let \(g_a(t)=(2a)^{1/4}\exp(-\pi a t^2)\) on \(\mathbb R\), so \(\|g_a\|_2=1\). Use the symmetric ambiguity convention
\[
 \mathcal A_g(x,\xi)=\int_{\mathbb R}g(t+x/2)\overline{g(t-x/2)}e^{-2\pi i\xi t}\,dt.
\]
Let \(g_{a,j}\) be the fractional Fourier rotations of \(g_a\) by \(j\pi/3\), for \(j=0,1,2\). With a consistent rotation orientation their ambiguity functions are the positive functions
\[
 \mathcal A_{g_{a,j}}(r\cos\theta,r\sin\theta)
 =\exp\!\left[-\frac{\pi r^2}{2}
 \left(a\cos^2(\theta-j\pi/3)+a^{-1}\sin^2(\theta-j\pi/3)\right)\right].
\]
The relevant design functional is
\[
 W_R(a)=\min_{x^2+\xi^2\le R^2}\sum_{j=0}^2\mathcal A_{g_{a,j}}(x,\xi),\qquad a\in[1,\infty).
\]
Restricting to \(a\ge1\) removes the reciprocal squeezing symmetry: replacing \(a\) by \(a^{-1}\) rotates every ellipse by \(\pi/2\) and leaves \(W_R\) unchanged. The three angle gaps are fixed at \(\pi/3\); no claim optimizes arbitrary angle triples or a different weighting of the three windows.

## Proof

**Gaussian normalization and radial boundary.** The Gaussian integral gives the stated ambiguity formula. Every summand is positive and nonincreasing in the radial coordinate \(r\ge0\), strictly decreasing for \(r>0\). Consequently the minimum on the closed disk occurs on its boundary \(r=R\).

Put \(u=(a+a^{-1})/2\), \(v=(a-a^{-1})/2\), and \(y=Tv\), so \(u^2-v^2=1\). At \(r=R\) the sum equals
\[
 e^{-Tu}\sum_{j=0}^2e^{-y\cos(2\theta-2\pi j/3)}.
\]

**Exact angular minimum.** Define \(S_y(t)=\sum_{j=0}^2 e^{y\cos(t-2\pi j/3)}\). Periodicity and reflection reduce the angular minimization to \(0\le t\le\pi/3\). Write \(x=\cos t\in[1/2,1]\), \(z=(\sqrt3y/2)\sqrt{1-x^2}\) and \(k=\sqrt3x/\sqrt{1-x^2}\). Then
\[
 S_y(t)=e^{yx}+2e^{-yx/2}\cosh z
\]
and its derivative with respect to \(x\) has the sign of
\[
 e^{kz}-\cosh z-k\sinh z.
\]
For \(k\ge1\) and \(z\ge0\), this expression is nonnegative, since
\[
 \cosh(kz)\ge\cosh z,\qquad \sinh(kz)\ge k\sinh z.
\]
The inequalities are strict for \(k>1,z>0\). Hence for \(y>0\), \(S_y\) has its unique minimum modulo \(2\pi/3\) at \(t=\pi/3\). Replacing \(t\) by \(t+\pi\) switches the sign of \(y\). It follows that the original angular minimum, for \(a>1\), occurs at \(\theta=j\pi/3\) modulo \(\pi\), and equals \(e^{-y}+2e^{y/2}\). At \(a=1\) all directions tie. Thus
\[
 W_R(a)=e^{-Tu}(e^{-y}+2e^{y/2})
 =e^{-\sqrt{T^2+y^2}}(e^{-y}+2e^{y/2}),\qquad y=T(a-a^{-1})/2.
\]

**The unique squeezing transition.** Differentiate its logarithm with respect to \(y>0\):
\[
 \frac{d}{dy}\log W_R=h(y)-\frac{y}{\sqrt{T^2+y^2}}.
\]
The sign is positive precisely when \(T>\mathcal T(y)\) and negative precisely when \(T<\mathcal T(y)\). By elementary expansion \(h(y)\sim y/2\) at zero, so \(\mathcal T(0+)=2\); at infinity \(h(y)\to1/2\) and \(\mathcal T(y)\sim\sqrt3y\).

It remains to verify strict monotonicity. Direct differentiation yields
\[
 \frac{d}{dy}\mathcal T(y)^2
 =\frac{2y}{h(y)^3}\bigl(h(y)(1-h(y)^2)-yh'(y)\bigr).
\]
Let \(t=3y/2\) and \(w=e^{-t}\). The expression in parentheses has the same strict positive sign as
\[
 (1-w)(1+2w)-tw(2+w)
 =w\bigl(e^t+1-2e^{-t}-t(2+e^{-t})\bigr).
\]
Call the last parenthesis \(P(t)\). One has \(P(0)=P'(0)=0\), and \(P''(t)=e^t-te^{-t}>0\) for \(t>0\), since \(e^{2t}>t\). Therefore \(\mathcal T'(y)>0\) on \((0,\infty)\).

For \(T\le2\), the logarithmic derivative of \(W_R\) is strictly negative for all \(y>0\), making \(a=1\) the unique maximizer. For \(T>2\), there is a unique crossing \(y_T\) of \(\mathcal T(y)=T\), and \(W_R\) first increases then decreases, giving a unique global maximizer \(a_T>1\). Since \(\mathcal T(y)\sim\sqrt3y\), one has \(y_T/T\to1/\sqrt3\), hence \(a_T\to\sqrt3\). Finally, \(\mathcal T(y)=2+y/2+O(y^2)\) also gives \(y_T=2(T-2)+O((T-2)^2)\) as \(T\downarrow2\), showing continuous onset of squeezing.

## Verification

The standalone file `check.py` evaluates both the three-angle ambiguity sum and the closed angular-minimum formula, tests the exact special direction, samples other angles, checks optimality against comparison squeezes and verifies strict growth of the scalar threshold function on finite grids. It passes 8,823 finite assertions with Python, NumPy-independent standard mathematics and SciPy root finding. These checks are diagnostics only; the global angular minimum, strict monotonicity and optimization are proved analytically above.

## Relationship to prior work

Alaifari and Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval* (arXiv:2410.05486, first public version October 7, 2024), give the rotated-dilated Gaussian construction, formulae for its ambiguity functions, and reconstruction stability estimates using their sum. Their Section 2.1 evaluates the geometric disk covered by a union of threshold ellipses for arbitrary fixed dilation and number of windows. The present claim instead optimizes the **smallest aggregate ambiguity denominator over the whole disk** for exactly three equally spaced orientations as the common squeezing is varied. It obtains a sharp change from isotropic to anisotropic optimality at \(R=2/\sqrt\pi\), uniqueness and a large-radius limiting squeeze. The threshold-ellipse covering radius and the aggregate-denominator maximin functional are different objectives.

Hardin, Kendall and Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials* (arXiv:1208.5261), prove angular polarization results under convexity conditions. Those results concern variation of point locations rather than optimizing Gaussian squeezing; moreover \(d\mapsto e^{y\cos d}\) is concave near \(d=0\) and does not satisfy the paper's global strict-convexity assumption. Neither angular symmetry alone nor the primary Gaussian ambiguity formula implies the stated scalar transition without the separate monotonicity argument.

## Limitations

The conclusion concerns the aggregate positive symmetric ambiguity denominator of exactly three equiangular, equally weighted, unit-norm Gaussian windows, not full nonlinear signal reconstruction error or minimax design over arbitrary angles and weights. The optimal squeeze is implicit above threshold, but uniquely specified. The phase transition is a mathematical statement about a particular inversion denominator; independent experimental or mathematical validation has not been performed. Historical priority beyond the inspected sources is not guaranteed.

## References

1. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486 (public version of October 7, 2024); subsequently SIAM J. Appl. Math. 85 (2025), 2376–2398, DOI:10.1137/24M1701332.
2. D. P. Hardin, A. P. Kendall and E. B. Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials*, arXiv:1208.5261 (2012).

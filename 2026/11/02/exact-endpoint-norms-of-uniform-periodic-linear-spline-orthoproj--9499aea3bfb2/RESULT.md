# Exact endpoint norms of uniform periodic linear-spline orthoprojectors

## Finding

For each integer \(n\geq3\), let \(S_n\) be the space of real, continuous, piecewise-affine functions on the circle \(\mathbb R/n\mathbb Z\) with knots at the integers. Let \(P_n:L^2\to S_n\) be the orthogonal projector for Lebesgue measure, also acting on \(L^\infty\). Define
\[
r=2-\sqrt3,\qquad
 a_j=\frac{\sqrt3\bigl((-r)^j+(-r)^{n-j}\bigr)}{1-(-r)^n}
\quad(0\leq j<n),\qquad a_n=a_0.
\]
For real \(a,b\), set
\[
F(a,b)=\begin{cases}
 (|a|+|b|)/2,&ab\geq0,\\[2pt]
 (a^2+b^2)/(2(|a|+|b|)),&ab<0.
\end{cases}
\]
Then **the exact attained norm** is
\[
\boxed{\|P_n\|_{L^\infty\to L^\infty}=
L_n:=\sum_{j=0}^{n-1}F(a_j,a_{j+1}).}
\]
Every \(L_n\) is rational. More importantly, for every finite \(n\ge3\),
\[
\boxed{1<L_n<2,\qquad\sup_{n\ge3}L_n=2,\qquad
0<2-L_n\leq\frac{4\sqrt3}{1-r}\,r^{\lfloor n/2\rfloor}.}
\]
Thus \(2\) is the sharp knot-count-independent constant for this equally spaced *periodic* degree-one spline family, but no individual finite mesh attains \(2\). At any knot, the sign of the evaluation kernel is an attaining bounded input. The exact largest negative value possible at a knot for an input \(0\le f\le1\) is \((L_n-1)/2\).

For illustration, \(L_3=16/9\), \(L_4=17/9\), \(L_5=257/132\), and \(L_6=2923/1485\).

## Assumptions and scope

The circle is given arc length, and the knots \(0,1,\ldots,n-1\) are equally spaced. The domain consists of equivalence classes of real essentially bounded measurable inputs. The target is the continuous periodic piecewise-linear spline space. The operator is orthogonal for the continuous \(L^2\) inner product; it is *not* the discrete least-squares fit from samples. Rescaling the circumference does not change the norms. The assertion begins at \(n=3\), so the two cyclic neighbors of every knot are distinct.

## Proof

Let \(\phi_j\) be the nonnegative periodic hat basis, equal to one at knot \(j\), zero at other knots, and linear on each interval. The Gram matrix \(G=(\langle\phi_i,\phi_j\rangle)\) has \(6G=4I+S+S^{-1}\), with \(S\) the cyclic shift. Its eigenvalues are \((4+2\cos(2\pi k/n))/6>0\), hence it is invertible.

On the integer line put \(b_j=\sqrt3(-r)^{|j|}\). The algebraic relation \(r+r^{-1}=4\) gives
\[
4b_j+b_{j-1}+b_{j+1}=6\mathbf1_{\{j=0\}}.
\]
Periodize by \(a_j=\sum_{\ell\in\mathbb Z}b_{j+\ell n}\). The series converges absolutely and satisfies \(4a_j+a_{j-1}+a_{j+1}=6\mathbf1_{\{j\equiv0\;(\mathrm{mod}\;n)\}}\). By invertibility this is precisely row zero of \(G^{-1}\). Summing the two geometric tails gives the displayed closed expression for \(a_j\). In particular all coefficients \(a_j\) are rational, because \(G\) has rational entries.

The integral kernel is \(K_n(x,y)=\sum_{i,j}\phi_i(x)(G^{-1})_{ij}\phi_j(y)\). At knot zero this reduces to \(K_n(0,y)=\sum_{j=0}^{n-1}a_j\phi_j(y)\). On \([j,j+1]\), the kernel is the affine interpolant of \(a_j\) and \(a_{j+1}\). Directly integrating its absolute value gives
\[
\int_0^1|(1-t)a+tb|\,dt=F(a,b),
\]
including the case when the interpolant crosses zero. Thus the row norm is exactly the displayed sum \(L_n\). On an interval between two knots, \(K_n(x,\cdot)\) is a convex combination of the kernels of its endpoint knots. Convexity of the \(L^1\) norm and translation invariance show that no intermediate evaluation point has a larger kernel norm. Taking \(f(y)=\operatorname{sgn}K_n(0,y)\) attains \(L_n\) at zero. Rationality of \(L_n\) follows from rationality of the coefficients and the rational operations in \(F\).

For the strict uniform bound, use the infinite-line hats \(\psi_j\) and put
\[
k_\infty(x)=\sum_{j\in\mathbb Z}b_j\psi_j(x).
\]
For \(j\ge0\), the adjacent coefficients have opposite signs and magnitudes \(\sqrt3r^j\) and \(\sqrt3r^{j+1}\); the negative half-line is symmetric. Consequently
\[
\|k_\infty\|_{L^1(\mathbb R)}
=2\sum_{j=0}^{\infty}\frac{3r^{2j}(1+r^2)}{2\sqrt3r^j(1+r)}
=\frac{\sqrt3(1+r^2)}{1-r^2}=2.
\]
Here \(r^2-4r+1=0\). The finite cyclic kernel is the exact periodization
\[
K_n(0,x)=\sum_{\ell\in\mathbb Z}k_\infty(x+\ell n).
\]
The triangle inequality on one period immediately gives \(L_n\le2\).

The inequality is strict for every finite \(n\). If \(n=2m+1\), on a short interval to the right of \(x=m\), the two nonzero functions \(k_\infty(x)\) and \(k_\infty(x-n)\) have opposite signs: their initial signs are respectively \((-1)^m\) and \((-1)^{m+1}\). If \(n=2m\), consider \(x=m-1+t\) with \(r/(1+r)<t<1/(1+r)\): the zeros of \(k_\infty(x-n)\) and \(k_\infty(x)\) in this interval occur at the two respective endpoints, and their signs are opposite between them. Each case forces strict cancellation in the periodization on positive measure, so \(L_n<2\). Since each \(P_n\) fixes the constant function, \(L_n\ge1\), and its kernel changes sign at an interior point of some interval, giving \(L_n>1\).

For the limit, integrate over \(I_n=[-n/2,n/2]\) and use the reverse triangle inequality:
\[
L_n\ge\int_{I_n}|k_\infty(x)|\,dx-
\int_{\mathbb R\setminus I_n}|k_\infty(x)|\,dx
=2-2\int_{\mathbb R\setminus I_n}|k_\infty(x)|\,dx.
\]
On each unit interval at distance \(\lfloor|x|\rfloor\) from the origin, \(|k_\infty(x)|\le\sqrt3 r^{\lfloor|x|\rfloor}\). Summing geometric tails bounds the last integral by \(2\sqrt3r^{\lfloor n/2\rfloor}/(1-r)\), which yields the asserted exponential estimate and \(L_n\to2\).

Finally, \(\int K_n(0,y)\,dy=1\) because constants are reproduced. Its negative mass is \((L_n-1)/2\). Choosing the input indicator of the negative kernel region gives the most negative possible projected knot value for \(0\le f\le1\), and proves sharpness of the positivity defect.

## Verification

The companion `verify.py` solves the cyclic Gram systems over exact rational numbers for every \(3\le n\le25\), independently checks all linear equations and the algebraic coefficient expression at high precision, compares two implementations of the interval absolute-value integral, and checks explicit rational small-size values. It reported 1,041 successful checks. Finite tests are corroboration, **not** proof of the all-\(n\) inequality or limit: those follow from the preceding periodization argument.

## Relationship to prior work

Shadrin (2001) proved the knot-independent boundedness conjecture for spline orthoprojectors on intervals. Kayumov's 2004 preprint reports the sharp mesh-independent bound \(3\) for unrestricted polynomial linear splines. Foucart (2008) surveys stronger finite-interval and variable-knot problems, noting the settled degree-one case. Passenbrunner's 2016 preprint establishes knot-independent \(L^\infty\) boundedness for arbitrary periodic spline spaces. These cover *boundedness* or an extremum over substantially different classes, but the inspected relevant arguments do not give the finite \(L_n\) formula, strict universal constant \(2\), or its exponential knot-count gap for equispaced periodic continuous linear splines. A general inverse-Gram decay theorem supplies a bound, not the exact local absolute-kernel integral.

## Limitations

The result applies to continuous periodic linear splines with uniform knots and Lebesgue \(L^2\) fitting. It does not determine the sharp constant for nonuniform periodic knots, higher-degree splines, weighted least squares, or nonperiodic boundary conditions. Although no directly implying theorem was found in the inspected primary material and available indexed statements, equivalence with an older uniform-spline calculation remains a residual literature risk. The finite-size rational checks alone do not justify originality or the infinite theorem.

## References

1. A. Yu. Shadrin, *The L-infinity norm of the L2-spline projector is bounded independently of the knot sequence: A proof of de Boor's conjecture*, Acta Mathematica 187 (2001), 59–137. DOI: 10.1007/BF02392832. Author-hosted text: https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/spn0.pdf.
2. A. Kayumov, *Least-squares approximation by second-order L-splines*, first arXiv posting 2004-08-30, arXiv:math/0408418. https://arxiv.org/abs/math/0408418.
3. S. Foucart, *Open questions around the spline orthoprojector*, East Journal on Approximations 14 (2008), 241–253. Author-hosted text: https://foucart.github.io/publi/OpenPb.pdf.
4. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The L-infinity Norm of the L2 Projector*, arXiv:1005.2424, 2010-05-13. https://arxiv.org/abs/1005.2424.
5. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, first arXiv posting 2016-08-24, arXiv:1608.06720. https://arxiv.org/abs/1608.06720.

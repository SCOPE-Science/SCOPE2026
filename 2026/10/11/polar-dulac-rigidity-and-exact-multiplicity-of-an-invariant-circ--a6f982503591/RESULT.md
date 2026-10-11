# Polar Dulac rigidity and exact multiplicity of an invariant circle

## Finding
Let \(U,V\in C^2(\mathbb R/2\pi\mathbb Z;\mathbb R)\), \(U\not\equiv0\), and consider the annular polar dynamical system
\[
\dot s=2s(1-s)U(\theta),\qquad \dot\theta=sU(\theta)-V(\theta),\qquad s=r^2>0.
\]
Suppose an open interval \(I=(s_-,s_+)\subset(0,\infty)\) contains \(s=1\) and the function \(sU(\theta)-V(\theta)\) has one fixed, strict sign \(\sigma\in\{-1,+1\}\) for every \(s\in I\) and every \(\theta\). All periodic orbits discussed below are wholly contained in this annulus. Then:

1. The invariant circle \(s=1\) is a genuine periodic orbit. On each side \(I\cap(0,1)\) and \(I\cap(1,\infty)\) there is **at most one** additional periodic orbit. Any such orbit has a transverse Floquet multiplier different from one.
2. Write \(W(\theta)=U(\theta)-V(\theta)\), \(A(\theta)=-2U(\theta)/W(\theta)\), \(\theta_f=2\pi\sigma\), and \(h(\theta)=\exp(\int_0^\theta A(\phi)\,d\phi)\). The circle multiplier is \(M=h(\theta_f)\). If \(M=1\), the circle has **exactly multiplicity two**, with first return in \(q=s-1\) given by
\[
q_{\mathrm{next}}=q+Kq^2+O(q^3),\qquad
K=\frac12\int_0^{\theta_f} A(\theta)^2h(\theta)\,d\theta,\qquad \operatorname{sign}K=\sigma.
\]
At neutrality the circle is the **only** periodic orbit in the entire annulus; on the attracting side (\(Kq<0\)) the intersections \(q_n\) with the ray \(\theta=0\) satisfy \(\lim_{n\to\infty}nq_n=-1/K\).
3. Both phenomena are realized in elementary trigonometric cases. Setting \(V=2\) and \(U=2-\sqrt5+\cos\theta\) gives \(M=1\) and strict clockwise angular motion throughout \(0<s<2\), so the circle is the unique periodic orbit there and has multiplicity two. Setting \(V=2\) and \(U=-1/10+(3/2)\cos\theta\) gives strict clockwise angular motion on \(0<s<11/10\) and **exactly one** off-circle periodic orbit in \(0<s<1\); that orbit is repelling.

## Assumptions and scope
The vector field is defined on a polar annulus; smoothness at the origin and polynomiality in Cartesian coordinates are **not** assumed. The angular velocity must stay uniformly away from zero on each closed subannulus relevant to a claimed orbit. The functions \(U,V\) are periodic and have the indicated differentiability. For statements about a first return map at \(s=1\), it suffices that the angular velocity be nonzero on a neighborhood of that circle. A periodic orbit in an angularly regular annulus has angular winding number \(\sigma\) and is represented by a one-revolution periodic solution of the scalar radial equation.

## Proof
**Radial-coordinate Dulac identity.** Angular regularity permits the scalar equation
\[
\frac{ds}{d\theta}=\frac{2s(1-s)U(\theta)}{sU(\theta)-V(\theta)}.
\]
On either side of the invariant circle put \(z=\log\left|s/(1-s)\right|\). Since \(dz/ds=1/[s(1-s)]\),
\[
\frac{dz}{d\theta}=\frac{2U}{sU-V},\qquad
\frac{\partial}{\partial z}\left(\frac{dz}{d\theta}\right)
=-\frac{2s(1-s)U^2}{(sU-V)^2}.
\]
Here \(s\) is the monotone inverse function of \(z\) on the chosen radial side. Along any entire revolution the variational multiplier in \(z\) is strictly less than one for \(\sigma=1\) and \(s<1\), or for \(\sigma=-1\) and \(s>1\), and strictly greater than one in the two complementary cases. Strictness follows from \(U\not\equiv0\). Between any two hypothetical periodic radial graphs, solutions are trapped by those graphs and the return map is defined throughout the intervening set of initial radii. On that set the one-revolution displacement \(P_z(z)-z\) is strictly monotone, hence it has at most one zero. Every off-circle periodic solution is hyperbolic. Equivalently, with the integrating factor \(D=[s(1-s)(sU-V)]^{-1}\), the weighted divergence in \((s,\theta)\) coordinates equals \(-2U^2/(sU-V)^2\), a definite-sign Dulac certificate away from the circle.

**Neutral rigidity.** The invariant circle \(s=1\) has \(z\to+\infty\) when approached from either side. At its neutral multiplier the return map in \(q=s-1\) has \(q_{\mathrm{next}}/q\to1\), so \(P_z(z)-z\to0\) as \(z\to+\infty\). Any hypothetical off-circle periodic graph and the neutral circle also trap every intermediate trajectory, so the return displacement is defined and strictly monotone all the way up to the circle. A finite zero there is impossible: a strictly monotone function tending to zero at the endpoint cannot vanish at a finite point. Thus neutral \(s=1\) is the only periodic orbit in \(I\).

**Exact quadratic displacement.** Writing \(s=1+q\) and \(W=U-V\) gives
\[
\frac{dq}{d\theta}
=\frac{-2q(1+q)U}{W+qU}
=Aq+\left(A+\frac{A^2}{2}\right)q^2+O(q^3).
\]
Variation of constants gives \(q(\theta)=h(\theta)q_0+h(\theta)q_0^2\int_0^\theta [A+A^2/2]h\,d\phi+O(q_0^3)\). At neutrality \(h(\theta_f)=1\), and \(\int_0^{\theta_f}Ah\,d\theta=h(\theta_f)-1=0\). Consequently the quadratic coefficient is \(K=\frac12\int_0^{\theta_f}A^2h\,d\theta\). Its sign is exactly the orientation \(\sigma\), since \(h>0\) and \(U\not\equiv0\). Hence it cannot vanish: the multiplicity is exactly two, not three or greater. The scalar recurrence \(q_{n+1}=q_n+Kq_n^2+O(q_n^3)\) on the attracting side yields \((1/q_{n+1})-(1/q_n)\to-K\), proving \(nq_n\to-1/K\). No universal pointwise-in-time coefficient is asserted away from the fixed ray.

**Neutral explicit example.** Let \(U=a+\cos\theta\), \(V=2\), \(a=2-\sqrt5\). Since \(s(a+1)-2\le2(3-\sqrt5)-2<0\) for \(0<s<2\), the angular velocity is negative there. For any \(a\) with \(2-a>1\), the standard trigonometric integral yields
\[
\int_0^{2\pi}\frac{U}{U-2}\,d\theta
=2\pi\left(1-\frac{2}{\sqrt{(2-a)^2-1}}\right).
\]
At \(a=2-\sqrt5\), the square root equals \(2\), and the integral vanishes. Thus \(M=1\), and the preceding conclusions apply to the entire annulus \(0<s<2\).

**Sharp off-circle example.** Let \(U=-1/10+(3/2)\cos\theta\), \(V=2\). On \(0<s<11/10\), \(sU-2\le(11/10)(7/5)-2=-23/50<0\). The logarithm of the return multiplier at the limiting origin \(s=0\) (used only as a comparison boundary) is \(-\pi/5<0\); hence the return map moves sufficiently small positive \(s\) downward. The logarithm of the circle multiplier is
\[
\Lambda_1=4\pi\left(1-\frac{10}{3\sqrt6}\right)<0.
\]
Thus points just inside \(s=1\) move upward on the first return. Continuous dependence supplies at least one fixed radius in \(0<s<1\); the strict monotonicity established above makes it unique and hyperbolic. Since angular motion is clockwise and \(s<1\), its logarithmic-radial return derivative exceeds one: the off-circle orbit is repelling.

## Verification
All identities follow by differentiating the displayed scalar equations. A standalone exact-algebra checker, \(\texttt{verify.py}\), confirms the radial Taylor coefficients and the strict rational inequalities for both examples. The trigonometric integrals follow from \(\int_0^{2\pi}(c+\cos\theta)^{-1}d\theta=2\pi/\sqrt{c^2-1}\) for \(c>1\); their signs are exact, not floating-point evidence. The existence result relies on the intermediate value theorem for the return map, not numerical trajectory plots. Running \(\texttt{python verify.py}\) with SymPy produces \(\texttt{CHECK_OK}\).

## Relationship to prior work
Gasull and Giacomini (first public preprint 27 October 2022, arXiv:2210.15803v1; journal article 2023), Section 7.1, analyze a cubic planar system with an invariant unit circle, including the already-known double limit cycle at its critical parameter. The earlier Gasull–Llibre–Sotomayor (1987) paper establishes multiplicity and cycle-count information for vector fields of the form \(X(v)=Av+f(v)Bv\). **Neither the multiplicity-two status of that particular cubic system nor the generic parabolic-return asymptotic is claimed as novel.** The present result supplies a sign-definite Dulac identity and a complete annular periodic-orbit and neutral-multiplicity rigidity theorem for two *arbitrary independent periodic angular profiles* \(U,V\); the entire class is not restricted to the cited Cartesian matrix form. The proof also supplies exact neutral and nonneutral trigonometric realizations. Classical Abel-equation limit-cycle bounds concern different scalar normal forms and do not immediately imply this particular sign-definite variation formula.

## Limitations
The theorem does not cover angular stalls, orbits outside the specified annular interval, or arbitrary planar vector fields having an invariant circle. It does not assert a globally sharp total cycle count across annuli with different angular signs. Nonneutral circles need not have any additional cycle. Independent external mathematical verification has not been performed. Full text of the 1987 directly related paper was not available for comparison, although its stated class and the 2023 full-text discussion were compared; a residual risk of stronger older statements remains.

## References
1. A. Gasull and H. Giacomini, *Number of Limit Cycles for Planar Systems with Invariant Algebraic Curves*, arXiv:2210.15803v1 (public 27 October 2022), https://arxiv.org/abs/2210.15803 ; *Qualitative Theory of Dynamical Systems* 22, 44 (2023), https://doi.org/10.1007/s12346-023-00746-7, especially Section 7.1.
2. A. Gasull, J. Llibre and J. Sotomayor, *Limit Cycles of Vector Fields of the Form \(X(v)=Av+f(v)Bv\)*, *Journal of Differential Equations* 67 (1987), 90–110.
3. M. J. Álvarez, A. Gasull and H. Giacomini, *A New Uniqueness Criterion for the Number of Periodic Orbits of Abel Equations*, arXiv:math/0602468 (2006), https://arxiv.org/abs/math/0602468.
4. J.-L. Bravo and M. Fernández, *Limit Cycles of Non-Autonomous Scalar ODEs with Two Summands*, *Communications on Pure and Applied Analysis* 12 (2013), 1091–1102, https://doi.org/10.3934/cpaa.2013.12.1091.

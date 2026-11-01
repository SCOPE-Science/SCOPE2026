# Unique nonspherical maximizer of random planar-section diameters for balanced four-ellipsoids

## Finding
For \(t\geq0\), consider the volume-preserving balanced ellipsoid
\[
E_t=\{x\in\mathbb R^4:e^{-2t}(x_1^2+x_2^2)+e^{2t}(x_3^2+x_4^2)\leq1\}.
\]
All these bodies have four-dimensional volume \(\pi^2/2\), and semiaxes \(e^t,e^t,e^{-t},e^{-t}\). If \(L\) is a Haar-uniform two-dimensional linear subspace and \(R_t(L)=\tfrac12\operatorname{diam}(E_t\cap L)\), then its expected circumradius has the exact one-dimensional integral
\[
\Phi(t):=\mathbb E R_t(L)=\frac14\int_0^\pi\frac{\sin u+(\pi-u)\cos u}{\sqrt{\cosh(2t)-\cos u\sinh(2t)}}\,du.
\]
The integral on the right extends to a **strictly log-concave positive function of every real** \(t\), tending to zero as \(t\to\pm\infty\). On the geometrically relevant half-line \(t\geq0\), \(\Phi\) has a unique maximizer \(t_*>0\), characterized as the unique positive solution of
\[
\int_0^\pi\!\frac{[\sin u+(\pi-u)\cos u][\cos u\cosh(2t_*)-\sinh(2t_*)]}{[\cosh(2t_*)-\cos u\sinh(2t_*)]^{3/2}}\,du=0.
\]
The ratio of the two distinct semiaxis lengths at this unique optimum is \(e^{2t_*}\). Numerical quadrature gives \(t_*\approx0.7888103975\), ratio \(\approx4.843418606\), \(\Phi(t_*)\approx1.273260599\), and optimal expected section diameter \(\approx2.546521197\). The ball at \(t=0\) has expected section diameter exactly \(2\); the strictly positive optimal improvement is therefore geometric, not a volume change.

## Assumptions and scope
The parameter is \(t\geq0\); \(L\) has normalized invariant (Haar) measure on the unoriented Grassmannian \(\operatorname{Gr}(2,4)\). The diameter of an origin-centered planar ellipse is twice its largest radial semiaxis. No unrestricted assertion about arbitrary four-dimensional ellipsoids or convex bodies is made. For negative \(t\), the same integral defines an analytic continuation but **does not** give the geometric expected radius (for negative \(t\) the smaller projected eigenvalue comes from the other principal-angle branch). The geometric family is unchanged up to congruence under \(t\mapsto-t\).

## Proof
**1. Reduction to the principal-angle maximum.** Let \(B=\operatorname{span}(e_1,e_2)\). For \(L\in\operatorname{Gr}(2,4)\), let \(\lambda_1\geq\lambda_2\) be the two eigenvalues of the compression to \(L\) of the orthogonal projection onto \(B\). Restricting the defining quadratic form of \(E_t\) to \(L\) gives its two eigenvalues \(e^{2t}-(e^{2t}-e^{-2t})\lambda_j\). For \(t\geq0\), the smallest occurs at \(\lambda_1\), so
\[
R_t(L)=[\cosh(2t)-(2\lambda_1-1)\sinh(2t)]^{-1/2}.
\]

**2. Exact Grassmannian law.** Temporarily orient \(L\). The unit simple bivector of \(L\) has equal-norm self-dual and anti-self-dual parts. Their normalized directions are independent uniform unit vectors of two copies of \(\mathbb S^2\): the identification of the oriented Grassmannian with \(\mathbb S^2\times\mathbb S^2\) sends invariant measure to the product of round probability measures. Denote one chosen coordinate of each sphere point by \(X,Y\). They are independent and uniform on \([-1,1]\). In the basis adapted to \(B\), the two complementary projected oriented areas are \((X+Y)/2\) and \((X-Y)/2\). Thus the compressed projection has trace \(1+XY\) and discriminant \((1-X^2)(1-Y^2)\), whence
\[
2\lambda_1-1=XY+\sqrt{(1-X^2)(1-Y^2)}.
\]
Put \(\alpha=\arccos X\), \(\beta=\arccos Y\), independent with density \(\tfrac12\sin\alpha\) on \([0,\pi]\). Then \(2\lambda_1-1=\cos(\alpha-\beta)\). A direct convolution of these densities gives the density of \(U=|\alpha-\beta|\):
\[
f_U(u)=\tfrac14[\sin u+(\pi-u)\cos u],\quad0<u<\pi.
\]
Indeed, \(f_U(u)=\tfrac12\int_0^{\pi-u}\sin\alpha\sin(\alpha+u)\,d\alpha\), which evaluates as displayed. Integrating the radius in Step 1 establishes the exact formula. The normalization \(\int_0^\pi f_U=1\) is immediate.

**3. Strict log-concavity of the exact integral.** Let \(z=\cos U\) and \(v=\tfrac12\operatorname{arctanh}z\); write \(q=\pi-U\in(0,\pi)\). Note that \(z=-\cos q\) and \(dq/dv=2\sin q\). The integral can be rewritten on the whole real line as the ordinary convolution
\[
\Phi(t)=\int_{-\infty}^{\infty}h(v)k(t-v)\,dv,\qquad
h(v)=\tfrac12\sqrt{\sin q}\,(\sin q-q\cos q),\quad
k(w)=(\cosh 2w)^{-1/2}.
\]
This follows from \(\cosh(2t)-z\sinh(2t)=\sqrt{1-z^2}\cosh(2(t-v))\) and \(dz/dv=2(1-z^2)\). The function \(j(q)=\sin q-q\cos q\) is positive for \(q\in(0,\pi)\), because \(j(0)=0\) and \(j'(q)=q\sin q>0\).

A direct differentiation using \(dq/dv=2\sin q\) yields
\[
\frac{d^2}{dv^2}\log h(v)=
-\frac{2\sin^2q}{j(q)^2}\big[2j(q)^2+q^2(2+\cos^2q)-3\sin^2q\big].
\]
The bracket is strictly positive. To see this, the elementary strict Cusa--Huygens inequality
\[
3\sin q<q(2+\cos q),\qquad0<q<\pi,
\]
follows on differentiating \(q(2+\cos q)-3\sin q\): its derivative equals \(2\sin(q/2)[2\sin(q/2)-q\cos(q/2)]>0\), by \(\tan(q/2)>q/2\). Therefore
\[
q^2(2+\cos^2q)-3\sin^2q>
\frac{2q^2}{3}(1-\cos q)^2>0.
\]
Thus \(h\) is strictly log-concave. Likewise \((\log k)''(w)=-2\operatorname{sech}^2(2w)<0\). Both functions are positive and integrable. The strict convolution form of the Prékopa log-concavity theorem (or its elementary strict equality criterion in one dimension) now gives strict log-concavity of \(\Phi=h*k\). Since both \(h\) and \(k\) are integrable, their continuous convolution tends to zero at both infinities.

**4. Unique nonspherical optimizer.** At \(t=0\), \(\Phi(0)=1\). Differentiation under the integral is justified locally by the strictly positive denominator. Using the independent angles,
\[
\Phi'(0)=\mathbb E\cos(\alpha-\beta)
=\mathbb E\sin\alpha\,\mathbb E\sin\beta
=(\pi/4)^2=\pi^2/16>0.
\]
A positive strictly log-concave function vanishing at both infinities has one and only one global maximum. Its derivative at zero is positive, so this maximizer lies strictly in \((0,\infty)\). Differentiating the exact integral yields the stationary equation in the finding. Any numerical values quoted above are approximations to this uniquely specified exact root, not exact constants and not prerequisites for the proof.

## Verification
A standalone standard-library script `verify.py` implements deterministic Simpson quadrature of the exact integral and its derivative. It checks normalization, \(\Phi(0)=1\), \(\Phi'(0)=\pi^2/16\), the root bracket \((0.7887,0.7889)\), the displayed numerical estimates, sampled strict log-concavity, and finite samples of the elementary trigonometric lemma. Running the script reports `PASS`. The analytic proof in the previous section, rather than these finite tests, establishes the continuum strictness, existence, uniqueness and equality classification.

## Relationship to prior work
Guedon, Litvak, Tatarko and Vritsiou, *On random diameters of convex bodies* (first public version 2026-09-21, arXiv:2609.24131), establish probabilistic bounds for random-section diameters. Their Section 6.3 explicitly examines two-valued ellipsoid axis sequences and Remark 6.15 identifies a balanced regime where their estimates are not sharp. These results motivate the present exact four-dimensional mean-value optimization, but do not imply its numerical profile or strict logarithmic concavity. This theorem is not a solution of their general high-probability bound question. Hinrichs, Krieg, Novak, Prochno and Ullrich, *Random sections of ellipsoids and the power of random information* (arXiv:1901.06639, first public 2019), establish probabilistic and asymptotic random-section-radius bounds, not the present fixed-volume four-dimensional optimization. Classical principal-angle probability and the Grassmannian \(\mathbb S^2\times\mathbb S^2\) parametrization are used as known mathematical tools, not asserted to be new.

## Limitations
The optimum is unique only within the balanced two-large/two-small-axis family. No extremum is asserted over general four-ellipsoids. Strict logarithmic concavity applies to the analytic integral on all real parameters, but the geometric formula applies on the stated half-line. Approximate numerical values are not certified interval enclosures. Available literature and mathematical-record searches do not prove absolute historical novelty; unindexed exact finite-dimensional analyses remain possible. Independent verification by another researcher has not been performed.

## References
1. O. Guedon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, first public 2026-09-21, especially §§1, 6.3 and Remark 6.15. https://arxiv.org/abs/2609.24131
2. A. Hinrichs, D. Krieg, E. Novak, J. Prochno, M. Ullrich, *Random sections of ellipsoids and the power of random information*, arXiv:1901.06639, especially §2. https://arxiv.org/abs/1901.06639
3. A. Hinrichs, J. Prochno, M. Sonnleitner, *Random sections of \(\ell_p\)-ellipsoids, optimal recovery and Gelfand numbers of diagonal operators*, arXiv:2109.14504, first public 2021-09-29. https://arxiv.org/abs/2109.14504
4. Classical Grassmannian principal-angle distributions and the Prékopa convolution theorem are invoked in the elementary special forms explicitly proved or stated above.

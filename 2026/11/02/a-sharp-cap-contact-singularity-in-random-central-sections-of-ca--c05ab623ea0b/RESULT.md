# A sharp cap-contact singularity in random central sections of capsules

## Finding
Let \(a,r>0\) and let the three-dimensional Euclidean capsule be
\[
K_{a,r}=[-a,a]e_3+rB_2^3.
\]
For a Haar-uniform unoriented plane \(U^\perp\) through its center, let \(X=\operatorname{area}_2(K_{a,r}\cap U^\perp)\). This theorem determines the complete distribution of \(X\), its two endpoint laws, and a genuine interior nonanalyticity caused by the first contact with the spherical caps.

Put \(L=\sqrt{a^2+r^2}\), \(\theta_*=\arctan(a/r)\), and write \(s=\sin\theta\), \(c=\cos\theta\). The section-area profile \(A(\theta)\), where \(\theta\in[0,\pi/2]\) is the acute angle of the plane normal with the capsule axis, is strictly increasing. For \(0\le\theta\le\theta_*\),
\[
A(\theta)=\frac{\pi r^2}{c}.
\]
For \(\theta_*<\theta<\pi/2\), define \(q=\sqrt{r^2-a^2c^2}\), \(x_0=a/s\), and
\[
J_c(x)=\frac12\left[x\sqrt{r^2-c^2x^2}+\frac{r^2}{c}\arcsin\left(\frac{cx}{r}\right)\right],\quad
H_q(v)=\frac12\left[v\sqrt{q^2-v^2}+q^2\arcsin\left(\frac vq\right)\right].
\]
Then
\[
A(\theta)=4\left[J_c(x_0)+H_q(q)-H_q(x_0-as)\right].
\]
The endpoint values are \(A(0)=\pi r^2\) and \(A(\pi/2)=\pi r^2+4ar\), using limits at \(c=0\).

If \(F(z)=\Pr(X\le z)\), the exact cumulative distribution is
\[
F(z)=\begin{cases}
0,&z<\pi r^2,\\
1-\pi r^2/z,&\pi r^2\le z\le\pi rL,\\
1-\cos(A^{-1}(z)),&\pi rL<z<\pi r^2+4ar,\\
1,&z\ge\pi r^2+4ar.
\end{cases}
\]
The inverse on the third branch exists uniquely because \(A\) is strictly increasing. Thus this is an exact evaluable law without an unspecified integration over orientations.

At the cap-contact angle, the correction to the analytic ellipse continuation has the sharp one-sided law
\[
\frac{\pi r^2}{\cos\theta}-A(\theta)
=\frac{16\sqrt2}{15}\frac{L^6}{\sqrt a\,r^{7/2}}
(\theta-\theta_*)^{5/2}+o\bigl((\theta-\theta_*)^{5/2}\bigr)
\quad (\theta\downarrow\theta_*\text{ from above}).
\]
Equivalently, setting \(z_*=\pi rL\),
\[
F(z)=1-\frac{\pi r^2}{z}
+\frac{16\sqrt2\,L^{3/2}}{15\pi^{7/2}a^3r^{7/2}}
(z-z_*)^{5/2}+o\bigl((z-z_*)^{5/2}\bigr)
\quad(z\downarrow z_*\text{ from above}).
\]
The two distributions agree with the reciprocal branch to second derivative at the join but not to third derivative. The (scale-free) probability at the nonanalytic transition is \(p_*=F(z_*)=1-r/L\), so the cylinder half-length-to-radius ratio is determined by
\[
\frac{a}{r}=\sqrt{(1-p_*)^{-2}-1}.
\]

Finally, with \(z_{\max}=\pi r^2+4ar\) and
\[
B_{a,r}=\frac{2a^3}{3r}+\pi a^2+2ar>0,
\]
the sharp upper-tail law is
\[
\Pr(X>z_{\max}-\varepsilon)
\sim\sqrt{\frac{\varepsilon}{B_{a,r}}}\quad(\varepsilon\downarrow0).
\]

## Assumptions and scope
The capsule radius and segment half-length are strictly positive and fixed. Planes pass through the capsule's center and have uniformly random normal directions, modulo sign, under spherical Haar probability. All areas are intrinsic two-dimensional Euclidean areas. The random affine-plane measure and offset-distributed sections are different sampling schemes and are not covered. The degenerate ball limit \(a=0\) has a point-mass area distribution and must be excluded from the singularity and tail statements.

## Proof
Choose orthonormal coordinates \((x,y)\) in a section plane such that a point in three-space has axial coordinate \(sx\) and squared distance \(c^2x^2+y^2\) from the capsule's axis. The squared distance from the point to the axis segment is therefore
\[
\Phi_s(x,y)=(1-s^2)x^2+y^2+(s|x|-a)_+^2,
\]
where \(t_+=\max(t,0)\). Consequently, the section satisfies \(\Phi_s(x,y)\le r^2\). Its area is four times the integral of
\[
y_s(x)=\sqrt{\bigl[r^2-(1-s^2)x^2-(sx-a)_+^2\bigr]_+}
\]
over positive \(x\).

When \(r/c\le a/s\), equivalently \(\theta\le\theta_*\), the entire section stays on the cylindrical region and has area \(\pi r^2/c\). Otherwise, the cylindrical arc runs from \(0\) to \(x_0=a/s\), while the spherical cap is a circular arc of radius \(q=\sqrt{r^2-a^2c^2}\), centered at \(x=as\), running from \(x_0\) to \(as+q\). Integrating these two arcs gives the stated formula. At \(c=0\) the planar section is the usual stadium of area \(\pi r^2+4ar\).

For fixed \(x>0\), write the part of \(\Phi_s\) independent of \(y\) as \(g_s(x)\). On the branch \(sx<a\), its derivative with respect to \(s\) is \(-2sx^2\). On \(sx>a\), it is \(-2ax\). Both are strictly negative for \(0<s<1\); the derivatives agree at the branch point. Hence section domains are strictly nested as \(s\) increases, and their positive areas increase strictly. Since \(|U\cdot e_3|=\cos\theta\) is uniform on \([0,1]\), the cumulative-distribution formula follows, including its exact reciprocal first branch.

For the interior singularity, let \(x_E=r/c\), and for \(\theta>\theta_*\) put \(\Delta=x_E-x_0\). The squared ordinate of the cap is exactly the squared ordinate of the *virtual* cylinder ellipse minus \(s^2(x-x_0)^2\). In particular its ordinate cannot exceed the ellipse ordinate, and
\[
\frac{\pi r^2}{c}-A(\theta)=4\int_{x_0}^{x_E}
\left[\sqrt{r^2-c^2x^2}-\sqrt{\bigl(r^2-c^2x^2-s^2(x-x_0)^2\bigr)_+}\right]dx.
\]
At the critical angle, \(c_*=r/L\), \(s_*=a/L\), and differentiating \(x_E-x_0\) gives
\[
\Delta=\frac{L^3}{ar}(\theta-\theta_*)+O\bigl((\theta-\theta_*)^2\bigr).
\]
Rescale \(x=x_0+\Delta u\). The quotient of the displayed deficit by \(\Delta^{5/2}\) converges by dominated convergence to
\[
\frac{2s_*^2}{\sqrt{2rc_*}}\int_0^1u^2(1-u)^{-1/2}du
=\frac{32s_*^2}{15\sqrt{2rc_*}}.
\]
For domination, use \(0\le\sqrt v-\sqrt{(v-w)_+}\le w/\sqrt v\), and \(v=r^2-c^2x^2\asymp\Delta(1-u)\) uniformly close to the threshold. Substituting the expansion of \(\Delta\) gives the claimed coefficient. Inverting the strictly increasing analytic ellipse branch, whose derivative at contact is \(\pi aL\), and differentiating the Haar CDF \(1-\cos\theta\) gives the displayed \((z-z_*)^{5/2}\) coefficient.

For the upper endpoint, put \(\eta=c^2\) and differentiate the direct ordinate integral at \(\eta=0\), where its positive support is \(0\le x\le a+r\). On \(0<x<a\), the derivative of the squared distance from the axis segment is \(x^2\); on \(a<x<a+r\) it is \(ax\). Differentiation under the integral is justified by the integrable square-root boundary singularity. Thus
\[
-\frac{dA}{d\eta}\bigg|_{\eta=0^+}
=2\left[\int_0^a\frac{x^2}{r}\,dx+
\int_a^{a+r}\frac{ax}{\sqrt{r^2-(x-a)^2}}\,dx\right]
=B_{a,r}.
\]
It follows that \(z_{\max}-A(\arccos c)=B_{a,r}c^2+o(c^2)\). Since \(c\) is uniform, the claimed square-root upper tail follows.

## Verification
The standalone standard-library script `verify.py` computes the closed profile and independently integrates the point-to-segment distance inequality by numerical quadrature. It checks 18 section configurations, monotonicity, the exact reciprocal branch, critical \(5/2\) scaling and upper-endpoint scaling. All assertions passed. The maximum relative difference between formula and direct quadrature over the 18 configurations was \(4.11\times10^{-13}\). These finite checks corroborate the exact analytical proof and do not certify all parameter values by enumeration.

## Relationship to prior work
Kim, Yaskin and Zvavitch (2015) establish the general framework of *unlabeled distributions* of convex-body central sections, as well as nonuniqueness and comparison theorems. Their general results do not give the capsule profile, its reciprocal first branch, the cap-contact \(5/2\) singularity, or the sharp upper tail. Portal and collaborators (2011) treat the segment-distance geometry of spherocylinders in the distinct problem of Voronoi boundaries between particles. Baule and collaborators (2013) investigate random packings of spherocylinders, not centered section-area distributions. These antecedents motivate the body and observable but do not imply the stated special-family calculation. No claim is made that the concept of random section distributions, the point-to-segment distance formula, or the elementary circular primitive is new.

## Limitations
The result treats centered planes in \(\mathbb R^3\), not offset planes, arbitrary capsules, higher-dimensional sections, or other sampling distributions. The second branch is an explicit strictly invertible analytic profile rather than a closed elementary formula for the inverse. Searches and inspection of the most closely relevant available works do not establish absolute historical novelty; older stereological literature may contain equivalent formulas under alternate terminology.

## References
- L. Portal, M. Danisch, A. Baule, R. Mari and H. A. Makse, *Jamming of hard rods I: From Onsager to Edwards*, arXiv:1102.0608v1, publicly submitted 2011-02-03; later versions/title concern Voronoi boundaries of spherocylinders. https://arxiv.org/abs/1102.0608
- A. Baule, R. Mari, L. Bo, L. Portal and H. A. Makse, *Mean-field theory of random close packings of axisymmetric particles*, Nature Communications **4**, 2194 (first online 2013-07-23), DOI: 10.1038/ncomms3194.
- J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1 (publicly submitted 2015-12-22), https://arxiv.org/abs/1512.07289.

# Orthogonal-width copulas and a universal angular covariance transition for regular polygons

## Finding
For every integer \(n\ge3\), let \(P_n\) be a regular Euclidean \(n\)-gon with circumradius \(R>0\). Let \(\Theta\) be uniform on \([0,2\pi)\), and write \(W(\theta)\) for its orthogonal projection width onto the line of angle \(\theta\). Define
\[
 m=\begin{cases}n,&n\text{ even},\\2n,&n\text{ odd},\end{cases}
 \quad a=\pi/m,\quad
 C=\begin{cases}2R,&n\text{ even},\\2R\cos a,&n\text{ odd}.\end{cases}
\]
For any angular shift \(\phi\), put \(t=\operatorname{dist}(\phi,2a\mathbb Z)\in[0,a]\). All two-direction distributions are the pushforwards of normalized uniform measure on \([-a,a]\) under
\[
 x\longmapsto\bigl(C\cos x,\ C\cos d_{2a}(x+t)\bigr),
 \qquad d_{2a}(u)=\operatorname{dist}(u,2a\mathbb Z).
\]
Their exact covariance is \(C^2K_a(t)\), where
\[
 K_a(t)=\frac{(2a-t)\cos t+t\cos(2a-t)+\sin(2a-t)+\sin t}{4a}
 -\left(\frac{\sin a}{a}\right)^2.
 \tag{1}
\]
The function \(K_a\) is strictly decreasing on \([0,a]\), with \(K_a(0)>0>K_a(a)\); hence there is a unique zero \(t_a\in(0,a)\). Furthermore,
\[
 \sup_{0\le u\le1}\left|\frac{K_a(au)}{K_a(0)}-Q(u)\right|=O(a^2),
 \quad Q(u)=1-\frac{15}{2}u^2+\frac{15}{2}u^3-\frac{15}{8}u^4,
 \tag{2}
\]
as \(n\to\infty\), and \(t_a/a\to u_*\), the unique zero of \(Q\) on \((0,1)\), approximately \(0.480670377640771857\). The normalized covariance at maximal folded separation converges to \(-7/8\).

In particular, the **orthogonal pair** \((W(\Theta),W(\Theta+\pi/2))\) has a sharp arithmetic dichotomy. If \(4\mid n\), the two widths are almost surely equal (the upper Fréchet copula). Otherwise, writing \(X\sim\operatorname{Unif}[0,a]\),
\[
 (W(\Theta),W(\Theta+\pi/2))\ \overset{\mathrm d}=\ (C\cos X,C\cos(a-X)),
 \tag{3}
\]
which has the lower Fréchet copula (strict countermonotonicity); its Pearson correlation tends to \(-7/8\) along \(4\nmid n\), and both rank correlations equal \(-1\). For \(4\mid n\), all three correlations equal \(+1\).

Let \(A=W(\Theta)W(\Theta+\pi/2)\) be the area of the smallest enclosing rectangle with sides in these two specified perpendicular directions. Its **complete distribution** is as follows (the formulas below apply only between their respective support endpoints; the CDF equals zero to the left and one to the right):
\[
 \Pr(A\le z)=
 \begin{cases}
 1-\dfrac1a\arccos(\sqrt z/C),&4\mid n,
 \quad C^2\cos^2a\le z\le C^2,\\[5pt]
 1-\dfrac1a\arccos(2z/C^2-\cos a),&4\nmid n,
 \quad C^2\cos a\le z\le C^2\cos^2(a/2).
 \end{cases}
 \tag{4}
\]
The two branches are nondegenerate for each fixed \(n\ge3\).

## Assumptions and scope
The polygon is deterministic, convex, regular, and inscribed in a radius-\(R\) circle; angular randomness means planar Haar-uniform rotation, not independent sampling of the two normals. The width \(W(\theta)\) is the distance between supporting lines perpendicular to \((\cos\theta,\sin\theta)\). The enclosing rectangle in (4) is minimal **among rectangles with prescribed orientation**, not among rectangles of freely chosen orientation. The covariance phase depends on the folded separation \(t\), rather than the raw angle. The correlation in the circle limit is undefined because the unscaled widths become constant: (2) concerns the well-defined nonzero finite-polygon correlations before taking the limit.

## Proof
**Width profile.** Let \(D=(P_n-P_n)/2\) denote the central symmetral. The width equals \(2h_D\). If \(n\) is even, \(D=P_n\), a regular \(m=n\) polygon of radius \(R\). If \(n\) is odd, \(D\) is a regular \(m=2n\) polygon of radius \(R\cos(\pi/(2n))\). For a regular \(m\)-gon, the support in any direction is its circumradius times the cosine of the angular distance to the closest vertex direction. Therefore, up to a harmless angular origin shift,
\[
 W(\theta)=C\cos d_{2a}(\theta).
 \tag{5}
\]
Because \(\Theta\) is uniform, folding one period gives exactly the pushforward representation in the finding. In particular \(X=d_{2a}(\Theta)\) is uniform on \([0,a]\), so \(\mathbb EW=C\sin a/a\).

**Two-angle integral.** Folding \([-a,a]\) after an angular translation \(t\in[0,a]\), the product expectation is obtained by splitting the integral at \(a-t\):
\[
 \frac{\mathbb E[W(\Theta)W(\Theta+t)]}{C^2}
 =\frac1{2a}\left(\int_{-a}^{a-t}\cos x\cos(x+t)\,dx+
 \int_{a-t}^{a}\cos x\cos(x+t-2a)\,dx\right).
\]
Product-to-sum integration yields the first term on the right of (1); subtracting the squared mean gives (1). Differentiating yields
\[
 K_a'(t)=\frac{t\sin(2a-t)-(2a-t)\sin t}{4a}.
 \tag{6}
\]
For \(0<t<a\), since \(0<t<2a-t<\pi\) and \(\sin x/x\) decreases strictly on \((0,\pi)\), (6) is negative. The variance \(K_a(0)>0\) since \(\cos X\) is nonconstant. At \(t=a\), (3) follows directly from folding, and \(\operatorname{Cov}(\cos X,\cos(a-X))<0\) by the strict opposite-monotonicity covariance inequality. Thus the unique zero exists.

**Orthogonal coupling and rectangle law.** If \(4\mid n\), then \(m=n\) is divisible by four and \(\pi/2\) is an integer multiple of the fundamental width period \(2a\). Hence the two widths agree and \(A=C^2\cos^2X\). Otherwise \(m\equiv2\pmod4\), so \(\pi/2\equiv a\pmod{2a}\) and (3) holds. In that case
\[
 A=C^2\cos X\cos(a-X)
 =\frac{C^2}{2}\bigl(\cos a+\cos(2X-a)\bigr).
\]
Inverting these strictly monotone formulas on their half-intervals proves both support ranges and the CDFs (4). Formula (3) also gives the lower Fréchet copula, while equality of the widths gives the upper one. Every width is nonconstant for finite \(n\), so these copula and correlation assertions are well-defined.

**Universal high-side-count law.** Represent a folded angular coordinate by \(aY\) with \(Y\) uniform on \([-1,1]\). For \(0\le u\le1\), the second folded coordinate is \(aT_u(Y)\), where
\[
 T_u(y)=\begin{cases}y+u,&-1\le y\le1-u,\\y+u-2,&1-u<y\le1.\end{cases}
\]
The variables \(Y\) and \(T_u(Y)\) are both uniform on \([-1,1]\). Expanding \(\cos(ay)=1-a^2y^2/2+O(a^4)\) uniformly in \(y\in[-1,1]\) and \(u\in[0,1]\), the covariance is
\[
 K_a(au)=\frac{a^4}{4}\operatorname{Cov}(Y^2,T_u(Y)^2)+O(a^6).
\]
Direct polynomial integration on the two pieces above gives
\[
 \mathbb E[Y^2T_u(Y)^2]=\frac{-5u^4+20u^3-20u^2+6}{30},
 \quad \operatorname{Var}(Y^2)=\frac4{45}.
\]
Dividing by \(K_a(0)=a^4/45+O(a^6)\) proves (2), uniformly, with \(Q\) as stated. Since \(Q'(u)=-(15/2)u(1-u)(2-u)<0\) for \(0<u<1\), \(Q\) has one zero there. The exact strict decrease of \(K_a\) and uniform convergence give \(t_a/a\to u_*\). The endpoint value is \(Q(1)=-7/8\).

## Verification
The self-contained program `verification/verify.py` reconstructs widths directly from all vertices rather than using (5) in its geometric side. It compares \(11{,}564\) vertex/support, independent numerical angular-quadrature, and empirical rectangle-area distribution checks against formulas (1) and (4) for every \(3\le n\le30\) at circumradius \(1.6\). It then checks high-precision opposite-width Pearson correlations for effective orders \(6,10,18,30,100,300,1000\) and computes the unique universal root of (2). The program executed successfully on Python 3 with `mpmath` installed. These are finite diagnostic checks, not the proof of assertions for all \(n\), which is the analytic argument above.

## Relationship to prior work
The single-direction width distribution, variance, and minimization questions are a classical subject: Akiyama and Kamae explicitly analyze polygonal width deviations and regular-polygon examples [1]. Kim, Yaskin and Zvavitch study the distribution of projection sizes of convex bodies [2], which supplies important tomography context but not the deterministic dependence induced by rotating *one* polygon and measuring two directions. Horváth and Lángi [3] analyze translative convex-hull area using the **maximum chord length times perpendicular width**, not the random product of two perpendicular widths. A published exact regular-polygon specialization of their invariant [4] has a modulo-four split, but its operands and optimization differ from (1)--(4). The known minimum-area enclosing parallelogram [5] is an optimization over admissible orientations, not the present complete orientation distribution.

The present precise contribution is the bivariate orthogonal-width copula, complete random enclosing-rectangle-area CDF, the strict angular covariance zero, and its uniform quartic limit. All follow from elementary support geometry and short exact integrations; this dependence on classical ingredients is explicitly acknowledged rather than called a new general convex-body theorem. Targeted exact and equivalent-formulation searches did not locate the combined assertion. Unindexed preexisting regular-polygon projection calculations remain a historical priority risk.

## Limitations
No analogous assertion is made for nonregular polygons, arbitrary convex bodies, or angles chosen independently rather than as a fixed shift. No sampling-noise or inverse-stability result follows from these exact distributions. The square and regular triangles are covered, but the circle itself has constant width and hence no Pearson correlation. The theorem is an exact fixed-family statistic, not a solution to a general extremal conjecture.

## References
1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1, first submitted 2022-01-18, https://arxiv.org/abs/2201.06736.
2. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first submitted 2015-12-22, https://arxiv.org/abs/1512.07289.
3. Á. G. Horváth and Z. Lángi, *On the volume of the convex hull of two convex bodies*, arXiv:1302.6164v1, first submitted 2013-02-25, https://arxiv.org/abs/1302.6164.
4. *Exact translative convex-hull profile of every regular polygon*, published research record https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-translative-convex-hull-profile-of-every-regular-polygon--79b005afe9c0.
5. *Exact minimum-area enclosing parallelograms for regular polygons*, published research record https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-minimum-area-enclosing-parallelograms-for-regular-polygons--827c68cd7bad.
6. *Inverse classification of projection-width distributions for tangential symmetric polygons*, published research record https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-inverse-classification-of-projection-width-distributions-for-tan--2ee871113939.

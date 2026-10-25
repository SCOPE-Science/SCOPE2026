# Six-or-eight-vertex equality structure for three-dimensional quotient covering

## Finding
For any origin-symmetric three-dimensional convex body \(K\), lattice \(\Lambda\), and first successive-minimum vector \(v\), let \(L=\mathbb Rv\), \(B=\pi_{L^\perp}K\), \(\Sigma=\pi_{L^\perp}\Lambda\), and \(\rho=\mu(B,\Sigma)\). The mixed inequality of Williams [1] reads
\[
\lambda_1(K,\Lambda)\,\rho^2\operatorname{vol}_3(K)\ge\tfrac23\det\Lambda.
\]
**Exact equality structure:** equality holds precisely when \(\rho B+\Sigma\) is a one-fold lattice tiling and the length of the fiber over every \(y\in B\) equals \(2a(1-p_B(y))\), where \(K\cap L=[-a,a]e\), \(e=v/|v|\), and \(p_B\) is the gauge of \(B\). Then \(K\) is a polytope with **exactly six or eight vertices**: two axial vertices and four or six projected equatorial vertices. In the six-vertex case the equatorial vertices lie in one plane; in the eight-vertex case they can be noncoplanar.

**Sharp hexagonal twist classification:** write \(y=(u,w)\) and set
\[
q(y)=\max\{|2u+w|,|u+2w|,|u-w|\},\qquad H=\{y:q(y)\le1\}.
\]
The cyclic vertices of \(H\) are
\[
h_0=(2,-1)/3,\quad h_1=(1,1)/3,\quad h_2=(-1,2)/3,\quad
h_3=-h_0,\quad h_4=-h_1,\quad h_5=-h_2.
\]
Let \(f\) be the unique continuous function that is linear on each cone \(\operatorname{pos}\{h_i,h_{i+1}\}\), is odd, and has \(f(h_0)=f(h_1)=0\), \(f(h_2)=1\). Its remaining values are \(0,0,-1\). The bodies
\[
K_{\tau,\ell}=\{(s,y):y\in H,\ |s-\ell(y)-\tau f(y)|\le1-q(y)\}
\]
are convex exactly for \(|\tau|\le1\), for arbitrary linear \(\ell:\mathbb R^2\to\mathbb R\). Each has \(\lambda_1(K_{\tau,\ell},\mathbb Z^3)=\rho=1\), volume \(2/3\), and eight vertices, so saturates the inequality. Conversely, every equality body with \(\Lambda=\mathbb Z^3\), axial section \([-1,1]\times\{0\}\), and projection \(H\) is of this form for unique \(\tau\) and \(\ell\). Its equatorial vertices are noncoplanar exactly when \(\tau\ne0\).

## Assumptions and scope
All norms, volumes and projections are Euclidean. Bodies are compact, convex, origin symmetric and full dimensional. Lattices are full rank. The selected \(v\) attains the first successive minimum and generates \(\Lambda\cap L\); this primitivity follows from minimality. The central interval has half-length \(a>0\). The gauge \(p_B(y)=\inf\{t>0:y\in tB\}\) is evaluated only for \(y\in B\). The classification concerns dimension three and the mixed theorem's \(r=1\) case, not other dimensions or other values of \(r\).

## Proof
**1. Exact equality criterion.** The fiber over \(y\in B\) is an interval with lower and upper endpoints \(d(y)\), \(u(y)\), and length \(g(y)=u(y)-d(y)\). Convexity makes \(u\) concave and \(d\) convex on \(B\), hence \(g\) concave. Symmetry gives \(g(0)=2a\) and \(g(y)=g(-y)\); therefore \(g(0)\) is maximal. For any boundary point \(z\in\partial B\) and \(0\le t\le1\), concavity gives
\[
g(tz)\ge(1-t)g(0)+tg(z)\ge2a(1-t).
\]
Because \(p_B(tz)=t\), one has \(g(y)\ge2a(1-p_B(y))\). The areas of sublevel sets of the gauge in the planar body are \(\operatorname{area}\{p_B\le t\}=t^2\operatorname{area}(B)\), so
\[
\operatorname{vol}_3(K)=\int_Bg(y)\,dy\ge2a\int_B(1-p_B(y))\,dy
=\tfrac{2a}{3}\operatorname{area}(B).
\]
The primitive lattice generator of \(\Lambda\cap L\) is \(v\), and \(\lambda_1=|v|/a\), because \(v\in\lambda_1 K\). The determinant factors as \(\det\Lambda=|v|\det\Sigma\). Covering density gives \(\rho^2\operatorname{area}(B)\ge\det\Sigma\), hence
\[
\lambda_1\rho^2\operatorname{vol}_3(K)
\ge\tfrac23|v|\rho^2\operatorname{area}(B)
\ge\tfrac23\det\Lambda.
\]
Equality occurs precisely when both inequalities are equalities. For the volume inequality, continuity of the interior fiber-length function, followed by radial concavity at the boundary, gives \(g(y)=2a(1-p_B(y))\) **for every** \(y\in B\). For covering density, a covering with density one has no positive-volume overlaps, so \(\rho B+\Sigma\) is a one-fold lattice tiling. Both conditions suffice.

**2. Vertex classification.** By Fedorov's planar lattice-tiling theorem [3], \(B\) is a parallelogram or a centrally symmetric hexagon. Fix an adjacent pair of vertices \(w_i,w_{i+1}\) of \(B\). On the triangle \(\operatorname{conv}(0,w_i,w_{i+1})\), the gauge \(p_B\) is affine. Since \(u\) is concave, \(d\) convex, and \(u-d=2a(1-p_B)\) affine there, both \(u\) and \(d\) must be affine there. The intersection of \(K\) above this triangle is consequently the convex hull of the two axial points \((\pm a,0)\) and the unique fiber points above \(w_i,w_{i+1}\). Thus \(K\) is exactly the convex hull of those two points and the four or six points above the vertices of \(B\). Each projected vertex has a singleton fiber and is an extreme point of \(K\); each axial endpoint is also extreme, because any nontrivial chord of \(K\) with projected midpoint zero has midpoint fiber height strictly between \(-a\) and \(a\) (apply the strict radial fiber-length deficit). Hence the number of vertices is exactly \(6\) or \(8\).

Write the fiber center as \(c(y)=(u(y)+d(y))/2\). It is odd, continuous and linear on each radial triangle. For a parallelogram, its values on one pair of linearly independent vertices determine a unique linear functional, agreeing with \(c\) on all four vertices and therefore throughout \(B\). Hence the equatorial vertices in the six-vertex case lie in a plane.

**3. Exact hexagonal family.** The six rays and the gradients of \(q\) and \(f\) on their intervening cones, in cyclic order, are:

| Cone | \(\nabla q\) | \(\nabla f\) |
|---|---|---|
| \(h_0,h_1\) | \((2,1)\) | \((0,0)\) |
| \(h_1,h_2\) | \((1,2)\) | \((-1,1)\) |
| \(h_2,h_3\) | \((-1,1)\) | \((1,2)\) |
| \(h_3,h_4\) | \((-2,-1)\) | \((0,0)\) |
| \(h_4,h_5\) | \((-1,-2)\) | \((-1,1)\) |
| \(h_5,h_0\) | \((1,-1)\) | \((1,2)\) |

Across consecutive rays, the jump in the gradient of \(f\) is alternately the positive and the negative of the corresponding jump for \(q\). Consequently both piecewise-linear functions \(q+\tau f\) and \(q-\tau f\) are convex if and only if \(1+\tau\ge0\) and \(1-\tau\ge0\). The upper endpoint of a fiber in \(K_{\tau,\ell}\) is \(1+\ell+\tau f-q\), while the lower endpoint is \(-1+\ell+\tau f+q\). Both have the required concavity/convexity precisely for \(|\tau|\le1\), proving the sharp threshold. An arbitrary odd continuous function linear on these cones is specified by its values on \(h_0,h_1,h_2\); subtract the unique linear functional matching the first two values. The residual vanishes at \(h_0,h_1\) and equals \(\tau\) at \(h_2\), hence is \(\tau f\). This proves completeness of the center parameterization.

The hexagon has area one by the shoelace formula. Moreover, every nonzero \(z\in\mathbb Z^2\) satisfies \(q(z)\ge2\): if \(q(z)<2\), the integers \(2u+w\), \(u+2w\), and \(u-w\) would all have absolute value at most one; the only integral solution is \(u=w=0\). Thus distinct interiors of \(H+\mathbb Z^2\) do not overlap because \(H-H=2H\); density one implies the translates tile, giving \(\rho=1\). Any nonzero lattice point with nonzero planar projection has gauge at least two in \(K_{\tau,\ell}\), while the axial primitive vector \((1,0,0)\) first enters at dilation one, so \(\lambda_1=1\). Finally,
\[
\operatorname{vol}_3(K_{\tau,\ell})=2\int_H(1-q(y))\,dy
=2\int_0^1 t^2\,dt=\tfrac23.
\]
This proves equality. All six lifted projected vertices and both axial vertices are extreme, giving eight vertices. An affine plane containing the six equatorial lifts, which come in opposite pairs, must be the graph of a linear functional. But \(f(h_0)=f(h_1)=0\) for independent vectors and \(f(h_2)=1\), so no such graph exists when \(\tau\ne0\). For \(\tau=0\) the equator is the graph of \(\ell\), so it is planar. At \(\tau=1/2,\ell=0\), this yields an explicit noncoplanar eight-vertex extremizer. Its eight vertices distinguish it under affine maps from the six-vertex source family.

## Verification
The standalone standard-library script `verify_hexagon.py` recomputes all six rational vertices, area, gradients, vertex values, nonnegative convexity certificates for the sharp endpoints, failure just outside the sharp interval, and the integer lattice obstruction. Run `python3 verify_hexagon.py`. The all-dimensional coverage assertions and the full equality classification are proved analytically above; the script is a check of finite exact certificates, not a substitute for these proofs.

## Relationship to prior work
Williams [1], Theorem 1, proves the mixed quotient-covering inequality in every dimension and constructs a sharp family with cubical quotient projections; its displayed three-dimensional, one-minimum instance has six vertices. The present result classifies the equality geometry in that dimension and exhibits a second eight-vertex hexagonal branch with a sharp extra center-warp parameter. Rogers and Shephard's classical equality criterion, reproduced in [2], supplies the underlying section-projection geometry. Fedorov's planar lattice-tile classification, discussed in [3], supplies the two possible projected polygon types. Neither [2] nor [3] addresses the mixed lattice inequality, and [1] does not give this dimension-three equality/moduli classification. The conceptual ingredients are classical, so literature overlap remains possible.

## Limitations
Only three dimensions and the first successive minimum are classified. The construction is an exact equality family, not a claim about ordinary covering-radius equality or all higher-dimensional extremizers. This result does not claim that the ingredients of the equality proof are new. Independent mathematical audit has not been performed.

## References
1. A. Williams, *Mixed Minkowski-Covering Inequalities for Convex Bodies and Lattices*, arXiv:2606.06291v1 (first public 2026-06-04), especially Theorem 1 and Sections 3–4.2. https://arxiv.org/html/2606.06291v1
2. D. Alonso-Gutiérrez, S. Artstein-Avidan, B. González Merino, C. H. Jiménez, R. Villa, *Rogers-Shephard and local Loomis-Whitney type inequalities*, arXiv:1706.01499v2, especially Section 1's classical section-projection equality criterion. https://arxiv.org/html/1706.01499v2
3. Q. Yang and C. Zong, *Multiple Translative Tilings in Euclidean Spaces*, arXiv:1711.02514, Introduction (Fedorov's theorem). https://arxiv.org/abs/1711.02514

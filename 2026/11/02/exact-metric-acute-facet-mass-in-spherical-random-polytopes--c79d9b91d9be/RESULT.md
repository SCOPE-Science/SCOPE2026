# Exact metric acute-facet mass in spherical random polytopes

## Finding
Let \(P_n\) be the Euclidean convex hull of \(n\ge4\) independent area-uniform points on the unit sphere \(S^2\subset\mathbb R^3\). For each triangular facet \(F\), let \(A_F\) be its ordinary Euclidean area and let \(\mathbf1_{\mathrm{ac}}(F)\) indicate that all three Euclidean interior angles of \(F\) are strictly less than \(\pi/2\). Define
\[
M_j(n)=\mathbb E\!\sum_{F\in\mathcal F_2(P_n)}A_F^j,
\qquad
M_j^{\mathrm{ac}}(n)=\mathbb E\!\sum_{F\in\mathcal F_2(P_n)}A_F^j\mathbf1_{\mathrm{ac}}(F),
\quad j=0,1,2.
\]
Then the *annealed* acute metric mass fractions are independent of the number of sampled points:
\[
\boxed{\frac{M_0^{\mathrm{ac}}(n)}{M_0(n)}=\frac12,\quad
\frac{M_1^{\mathrm{ac}}(n)}{M_1(n)}=\frac14+\frac4{\pi^2},\quad
\frac{M_2^{\mathrm{ac}}(n)}{M_2(n)}=\frac{53}{70}.}
\]
The first, count-weighted fraction is previously known. The evaluated area- and squared-area-weighted fractions and their finite-sample totals are the contributions here. Precisely,
\[
\begin{aligned}
M_0(n)&=2n-4,& M_0^{\mathrm{ac}}(n)&=n-2,\\
M_1(n)&=\frac{4\pi(n-1)(n-2)}{(n+1)(n+2)},&
M_1^{\mathrm{ac}}(n)&=\frac{(\pi^2+16)(n-1)(n-2)}{\pi(n+1)(n+2)},\\
M_2(n)&=\frac{140n(n-1)(n-2)}{(n+1)(n+2)(n+3)(n+4)},&
M_2^{\mathrm{ac}}(n)&=\frac{106n(n-1)(n-2)}{(n+1)(n+2)(n+3)(n+4)}.
\end{aligned}
\]
Here \(A_F^0=1\). In particular, although only half of the facets are acute on average by count, acute facets carry approximately \(65.528\%\) of expected total facet area and \(75.714\%\) of expected total squared facet area.

## Assumptions and scope
The vertices are independent and sampled according to normalized area measure on the unit *two*-sphere. For \(n\ge4\), with probability one their hull is three-dimensional, simplicial, and has exactly \(2n-4\) facets. Triangles and their angles are Euclidean, with chord edges; this is not a statement about intrinsic spherical triangle angles. A right triangle has probability zero. The ratios are quotients of expectations, not the expectations of ratios taken separately for each realization. The area has squared-length units, and the sphere radius is one; on a sphere of radius \(R>0\), \(M_j\) and \(M_j^{\mathrm{ac}}\) acquire a factor of \(R^{2j}\), leaving the ratios unchanged.

## Proof
**1. A typical facet splits into independent height and shape.** Uniformly select one of the \(2n-4\) facets after sampling. Write its outward supporting plane as \(\langle u,z\rangle=h\), where \(u\in S^2\) and \(-1<h<1\). Its circumcircle radius is \(r=\sqrt{1-h^2}\). The spherical Blaschke–Petkantschin measure for three points in a plane at signed height \(h\) has a product density proportional to \((1-h^2)\,W(v_1,v_2,v_3)\) times the uniform plane-orientation and circle-coordinate measures; \(W\) is the area of the triangle with circumradius one. The remaining \(n-3\) points must be on the inner side of the outward plane. The corresponding spherical cap has area fraction \((1+h)/2\), producing the additional factor \(((1+h)/2)^{n-3}\). Since the height and shape factors separate, \(h\) and the normalized circle triangle are independent.

Put \(U=(1+h)/2\). The height density is proportional to \((1-h^2)((1+h)/2)^{n-3}\,dh\), hence
\[
U\sim\operatorname{Beta}(n-1,2),
\qquad
\mathbb E[(1-h^2)^j]=4^j\frac{(n-1)_j(2)_j}{(n+1)_{2j}},\quad j\ge0,
\]
with rising factorial \((a)_j=\prod_{k=0}^{j-1}(a+k)\). In particular,
\[
\mathbb E[1-h^2]=\frac{8(n-1)}{(n+1)(n+2)},\quad
\mathbb E[(1-h^2)^2]=\frac{96n(n-1)}{(n+1)(n+2)(n+3)(n+4)}.
\]
This product decomposition is a specialization of the known spherical Blaschke–Petkantschin formula, not a claimed new measure theorem.

**2. Evaluate the weighted circular-triangle shape moments.** Denote the three interior angles of the unit-circumradius triangle by \(x,y,z>0\), \(x+y+z=\pi\). In the angular coordinate triangle \(\mathcal T=\{x>0,y>0,x+y<\pi\}\), the density of \((x,y)\) is proportional to \(s(x,y)=\sin x\sin y\sin(x+y)\); this is the circular-triangle area factor from step 1. Its unit-circumradius Euclidean area is \(W=2s\). The acute region is
\[
\mathcal T_{\mathrm{ac}}=\{0<x<\pi/2,\ \pi/2-x<y<\pi/2\}.
\]
For positive integer \(p\), put \(J_p=\int_{\mathcal T}s^p\,dx\,dy\), and \(J_p^{\mathrm{ac}}=\int_{\mathcal T_{\mathrm{ac}}}s^p\,dx\,dy\). Direct trigonometric integration gives the exact table
\[
\begin{array}{c|cc}
p&J_p&J_p^{\mathrm{ac}}\\\hline
1&3\pi/8&3\pi/16\\
2&3\pi^2/64&3\pi^2/256+3/16\\
3&35\pi/512&53\pi/1024
\end{array}
\]
For reproducibility, use \(t=x+y\), so that \(\sin x\sin(t-x)=(\cos(2x-t)-\cos t)/2\). The entries follow by expanding powers \(p=1,2,3\) and integrating
\[
J_p=2^{-p}\int_0^\pi\sin^p t\int_0^t(\cos(2x-t)-\cos t)^p\,dx\,dt,
\]
\[
J_p^{\mathrm{ac}}=2^{-p}\int_{\pi/2}^\pi\sin^p t\int_{t-\pi/2}^{\pi/2}(\cos(2x-t)-\cos t)^p\,dx\,dt.
\]
These are elementary finite trigonometric integrals. The attached checker evaluates all six symbolically and independently by high-precision quadrature.

Consequently,
\[
\begin{array}{c|cc}
j&\mathbb E[W^j]&\mathbb E[W^j\mathbf1_{\mathrm{ac}}]\\\hline
0&1&1/2\\
1&\pi/4&\pi/16+1/\pi\\
2&35/48&53/96
\end{array}
\]
because \(\mathbb E[W^j\mathbf1_{\mathrm{ac}}]=2^jJ_{j+1}^{\mathrm{ac}}/J_1\), with the unrestricted version obtained by replacing \(J_{j+1}^{\mathrm{ac}}\) with \(J_{j+1}\).

**3. Multiply independent moments and count facets.** Each facet area equals \(A_F=(1-h^2)W\). With the deterministic facet count, for \(j=0,1,2\),
\[
M_j^{\mathrm{ac}}(n)=(2n-4)\,\mathbb E[(1-h^2)^j] \frac{2^jJ_{j+1}^{\mathrm{ac}}}{J_1},\qquad
M_j(n)=(2n-4)\,\mathbb E[(1-h^2)^j] \frac{2^jJ_{j+1}}{J_1}.
\]
Substituting the explicit height moments and table yields the six finite-sample expressions in the Finding section. Cancelling the common height factor proves the three size-independent ratios. This argument treats every \(n\ge4\) and does not extrapolate from a finite enumeration.

## Verification
The included files `verify.py` and `requirements.txt` reproduce all six exact angular integrals using symbolic antiderivatives, verify the beta-moment substitutions at several sample sizes, and independently evaluate all six angular integrals using high-precision numerical quadrature. Running `python verify.py` after installing the listed dependencies ends with `ALL_SYMBOLIC_AND_QUADRATURE_CHECKS_PASSED`. As additional diagnostics, independent direct simulations of random tetrahedra and numerical convex-hull sampling at larger sample sizes gave area fractions near \(0.6553\) and squared-area fractions near \(0.7571\); these finite tests are corroboration and not the proof.

## Relationship to prior work
Akopyan, Edelsbrunner and Nikitenko proved that an unweighted uniformly chosen facet is acute with probability \(1/2\), and established the shape-size decomposition and an exact expected-total-area formula. Thus the unweighted result and \(M_1(n)\) are prior results. Their general facet-intensity formula makes weighted integrations possible but does not evaluate the above acute area fractions or squared-area total in the inspected full text. Bonnet and O'Reilly's facet-height analysis supplies another route to the height factor but does not provide the acute shape moments. Finch documents the same angle-density factor for a planar typical Poisson–Delaunay triangle, with the classical unweighted acute fraction, but not the evaluated acute area moment constants used here. The new content is the evaluated *metric* conditional moments and resulting exact finite-sample identities, not the underlying Blaschke–Petkantschin technique or the classical counting result.

## Limitations
The statements are expectations and expectation ratios; they do not establish concentration, variances of the total acute area, or the expectation of a realization-wise area fraction. Historical priority of the explicit constants is not conclusively established, especially among older Poisson–Delaunay moment tables. The derivation relies on independent uniform sampling and spherical symmetry; it does not assert the same fractions for arbitrary sampling laws on smooth surfaces or for intrinsic spherical angles. Independent mathematical verification has not been performed.

## References
1. A. Akopyan, H. Edelsbrunner, A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-Sphere*, arXiv:2007.07783 (first public posting 2020-07-15), especially Sections 4.1–4.3 and the expected surface-area result. https://arxiv.org/abs/2007.07783
2. G. Bonnet, E. O'Reilly, *Facets of spherical random polytopes*, arXiv:1908.04033 (first public posting 2019-08-12), especially the exact facet-height density. https://arxiv.org/abs/1908.04033
3. S. R. Finch, *Random Triangles V*, dated 2010-12-22, especially the angular density and moments of a planar typical Poisson–Delaunay triangle. https://oeis.org/A261710/a261710.pdf
4. B. Leroux et al., *Expected extremal area of facets of random polytopes*, arXiv:2501.08614 (2025), for distinct extremal-area questions. https://arxiv.org/abs/2501.08614

# Exact area-weighted silhouette law and reverse area–complexity ordering for the regular icosahedron

## Finding
Let \(I\) be a regular icosahedron of edge length \(2\), with \(U\) Haar-uniform on the unit sphere \(S^2\). Let \(N\) be the number of vertices of the orthogonal projection of \(I\) onto \(U^\perp\), let \(B\) be that projection's area, and normalize by the area \(F=\sqrt3\) of one triangular facet: \(W=B/F\).

Put
\[
\begin{gathered}
\alpha=\arccos(1/3),\qquad \beta=\arccos(\sqrt5/3),\\
 h=\arccos\!\left(\frac{3+\sqrt5}{4\sqrt2}\right),\qquad
 p=\arccos\!\left(\frac{1+3\sqrt5}{8}\right).
\end{gathered}
\]
Then \(N\in\{6,8,10\}\) almost surely. Its **area-weighted silhouette law** is
\[
\boxed{\begin{aligned}
\mathbb E[W\mathbf1_{\{N=6\}}]&=\frac{5(3+\sqrt5)h}{\pi},\\
\mathbb E[W\mathbf1_{\{N=8\}}]&=\frac5{2\pi}\bigl((1+\sqrt5)p+2(3-\sqrt5)h\bigr),\\
\mathbb E[W\mathbf1_{\{N=10\}}]&=\frac{5(5-\sqrt5)p}{2\pi}.
\end{aligned}}
\]
For clarity, the already-known unweighted marginals, recovered independently in the same chamber calculation, are
\[
\begin{aligned}
P_6&=\frac5\pi(2\pi-3\alpha-3\beta),\\
P_8&=\frac{15}\pi(2\alpha+\beta-\pi),\\
P_{10}&=\frac3\pi(2\pi-5\alpha).
\end{aligned}
\]
Their numerical values are approximately \(0.638408811559\), \(0.238989468900\), and \(0.122601719541\), respectively. The exact mixed moments yield a strict **reverse ordering**:
\[
\boxed{\mathbb E[W\mid N=6]>\mathbb E[W\mid N=8]>\mathbb E[W\mid N=10].}
\]
The three conditional means are approximately \(5.066574049654\), \(4.893847762291\), and \(4.860261397053\). In particular,
\[
\boxed{\operatorname{Cov}(N,W)=\sum_{k\in\{6,8,10\}}k\,\mathbb E[W\mathbf1_{\{N=k\}}]-5\sum_{k\in\{6,8,10\}}kP_k<0,}
\]
with value approximately \(-0.119267305855\). Thus the more vertex-rich generic silhouettes have **smaller average area**.

## Assumptions and scope
The vertex model is
\[
I=\operatorname{conv}\{(0,s,t\varphi),(s,t\varphi,0),(s\varphi,0,t):s,t\in\{-1,1\}\},\quad \varphi=(1+\sqrt5)/2.
\]
There are twelve distinct vertices, thirty edges of length \(2\), twenty equilateral triangular faces of area \(F=\sqrt3\), and outward face-unit normals in ten antipodal pairs. Viewing directions lying on any face-normal great circle have spherical measure zero; the assertion about \(N\) and its conditional means concerns their complement. The object, Euclidean measure and uniform angular measure are fixed; no perspective projection or affine deformation is included.

## Proof
**Face normals and silhouette count.** Put \(r=1/\varphi\). Choose ten unnormalized face-normal representatives
\[
\mathcal A=\{(1,s,t),(0,\varphi,tr),(\varphi,tr,0),(r,0,t\varphi):s,t\in\{-1,1\}\},
\]
where the last three displayed families each use only \(t\in\{-1,1\}\). Every \(a\in\mathcal A\) has squared length \(3\), and \(\pm a/\sqrt3\) are precisely the twenty face-unit normals. Each supporting face contains exactly three of the twelve listed icosahedron vertices, and each of its three edges has length \(2\). Two of these facets share an edge precisely when their unnormalized normals have scalar product \(\sqrt5\). Thus the thirty adjacent-facet pairs give the projected silhouette vertices exactly as the edges whose adjacent face-normal dot products with \(U\) have opposite signs.

**Exact chamber classification.** Ten great circles \(a\cdot u=0\), \(a\in\mathcal A\), partition the viewing sphere. Their forty-five pairs have ninety distinct signed intersection vertices and no triple intersections. Hence they form \(92\) open spherical polygon chambers. Each chamber is a convex intersection of hemispheres indexed by the signs of its ten face-normal scalar products. Exhaustive exact arithmetic in \(\mathbb Q(\sqrt5)\) identifies the chambers and silhouette count as follows:

| Number of projected vertices | Number of spherical chambers | Spherical chamber sides | Interior-angle multiset |
|---|---:|---:|---|
| \(6\) | 20 | 6 | three \(\pi-\alpha\), three \(\pi-\beta\) |
| \(8\) | 60 | 3 | two \(\alpha\), one \(\beta\) |
| \(10\) | 12 | 5 | five \(\pi-\alpha\) |

For completeness, this finite enumeration is reproduced and checked in `ico_weighted_check.py`: its field arithmetic has exact rational coefficients in the basis \(1,\sqrt5\), and every chamber is generated from all four infinitesimal sectors at every circle intersection. It checks every facet and edge from the twelve input vertices, all thirty facet adjacencies, all **ninety** signed circle-intersection vertices, all ninety-two sign chambers, each chamber's complete boundary, exact angle type and silhouette size. Exact exhaustiveness follows from the no-triple-intersection assertion and the great-circle arrangement formula. Applying Girard's area formula gives chamber areas \(2\pi-3(\alpha+\beta)\), \(2\alpha+\beta-\pi\), and \(2\pi-5\alpha\), and dividing total type-areas by \(4\pi\) gives the three displayed unweighted marginals.

**Linear projection area and spherical flux.** By Cauchy's polytope projection-area identity,
\[
W(u)=\sum_{a\in\mathcal A}\left|\frac{a\cdot u}{\sqrt3}\right|.
\]
Within a sign chamber \(C_s=\{u\in S^2:s_a a\cdot u>0\}\), with \(s_a\in\{-1,1\}\), the function is \(W(u)=v_s\cdot u\) for \(v_s=\sum_a s_a a/\sqrt3\). Since \(\Delta_{S^2}(v\cdot u)=-2(v\cdot u)\), the spherical divergence theorem and the fact that each edge on \(a\cdot u=0\) has outward spherical conormal \(-s_a a/\sqrt3\) give
\[
\int_{C_s}W(u)\,d\omega(u)
=\frac12\sum_{e\subset\partial C_s}\ell(e)\frac{s_{a(e)}v_s\cdot a(e)}{\sqrt3}.
\]
Every boundary arc length belongs to exactly two classes,
\[
\ell_H=h=\arccos\!\left(\frac{3+\sqrt5}{4\sqrt2}\right),\quad
\ell_P=p=\arccos\!\left(\frac{1+3\sqrt5}{8}\right).
\]
The same exact chamber enumeration checks the cosine-squares of the boundary arcs and every edge's flux coefficient. After summing coefficients over all chambers of one silhouette class, one obtains
\[
\begin{array}{c|cc}
N&\text{coefficient of }h&\text{coefficient of }p\\\hline
6&120+40\sqrt5&0\\
8&120-40\sqrt5&20+20\sqrt5\\
10&0&100-20\sqrt5
\end{array}
\]
Thus \(\mathbb E[W\mathbf1_{\{N=k\}}]\) is exactly one eighth of the corresponding linear combination divided by \(\pi\), proving the three mixed-moment formulas.

**Strict order and covariance.** The all-direction mean \(\mathbb E[W]=5\) follows independently from Cauchy's surface-area identity: the solid has twenty congruent faces. This is also the sum of the displayed exact mixed moments. The rational interval checker `ico_shadow_signs.py` brackets all four inverse-cosine angles by monotonicity of cosine and a rigorous finite Taylor remainder; it brackets \(\pi\) using Machin's identity and alternating arctangent series. It proves exact positivity of the two cross-products \(M_6P_8-M_8P_6\) and \(M_8P_{10}-M_{10}P_8\), where \(M_k=\mathbb E[W\mathbf1_{\{N=k\}}]\). It also proves the covariance lies strictly between \(-0.119267327\) and \(-0.119267284\). All interval endpoints and arithmetic are rational; no floating-point comparison is used for the strict inequalities.

## Verification
Execute `python3 ico_weighted_check.py` to reproduce the exact ninety-two-chamber and boundary-flux certificate. It needs only Python's standard library. Execute `python3 ico_shadow_signs.py` for the rigorous strict-inequality certificates, likewise standard-library-only. Optionally execute `python3 ico_shadow_numeric.py` (requires NumPy and SciPy) for an independent reconstruction of 1,800 two-dimensional convex hulls, face-normal silhouette checks and 300,000 Haar viewing-direction simulations. The exact scripts establish the finite certificates used in the analytic proof; the numerical simulation is an independent diagnostic, not proof of an infinite assertion.

## Relationship to prior work
The unweighted silhouette distribution for this Platonic solid is not claimed as new; the polar regular-dodecahedron central-section law already gives it. The unconditional expected projected area \(\mathbb E[W]=5\) is classical, and the unconditional orientation variance has also been evaluated. The present claim is their previously non-implied **partition into all three area-weighted silhouette classes**, and its strict inverse ordering/covariance. The prior exact area-weighted silhouette formulas for tetrahedra do not instantiate to the regular icosahedron. Glisse–Lazard's geometric silhouette estimates and Black–Criado's random-shadow bounds concern expectation/size bounds, not the area-conditioned law computed here. Historical priority remains provisional pending broader archival verification.

## Limitations
Only first area-weighted moments conditioned on the three generic silhouette types are evaluated; the complete conditional area distributions and conditional second moments are not claimed. The proof does not extend these values to affine icosahedra or perspective projections. Search-based priority assessment is not a uniqueness or historical-priority certificate; archival sources could contain an equivalent law. The exact algebraic enumeration uses a standalone computer-checked finite certificate, not a formal proof-assistant verification or independent audit.

## References
1. M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087v1 (public 14 February 2007), especially the definitions and principal silhouette bounds. https://arxiv.org/abs/cs/0702087
2. M. Glisse, S. Lazard, J. Michel, and M. Pouget, *Silhouette of a random polytope*, Journal of Computational Geometry 7 (2016), 86–99, DOI:10.20382/jocg.v7i1a5. https://jocg.org/index.php/jocg/article/view/3009
3. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1 (2024), especially Theorem 1.1 on expected shadow-vertex bounds. https://arxiv.org/abs/2406.06936
4. H. Alt, M. Glisse, and X. Goaoc, *On the worst-case complexity of the silhouette of a polytope*, CCCG 2003, pp. 51–55. https://www.cccg.ca/proceedings/2003/12.pdf
5. Published geometric results on the exact Haar polygon-type law for central icosahedral sections, the unconditional Platonic brightness-variance spectrum, and the tetrahedral area-weighted silhouette law (bibliographic identifiers and implication comparisons in `AUDIT.json`).

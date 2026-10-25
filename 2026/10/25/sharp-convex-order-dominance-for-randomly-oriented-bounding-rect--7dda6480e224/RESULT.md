# Sharp convex-order dominance for randomly oriented bounding-rectangle perimeters

## Finding

Let \(K\subset\mathbb R^2\) be any compact convex body with nonempty interior and perimeter \(P(K)>0\). Rotate \(K\) through a uniformly random angle \(\Theta\), and let \(B_K(\Theta)\) be the perimeter of the tight axis-parallel enclosing rectangle. Put \(Z_K=B_K(\Theta)/P(K)\). If \(U\) is uniform on \([0,\pi/2]\), set \(Q=\cos U+\sin U\). Then
\[
\boxed{Z_K\preceq_{\rm cx}Q,\qquad \mathbb EZ_K=\mathbb EQ=4/\pi.}
\]
Precisely, \(\mathbb E\Phi(Z_K)\le\mathbb E\Phi(Q)\) for every real-valued convex function \(\Phi:[1,\sqrt2]\to\mathbb R\). Equality for **any strictly convex** such \(\Phi\) holds if and only if \(K\) is a rectangle, up to rigid motion; all nondegenerate rectangles, irrespective of aspect ratio, share the law \(Q\).

Consequently, the sharp normalized variance bound is
\[
\boxed{\operatorname{Var}(Z_K)\le 1+\frac2\pi-\frac{16}{\pi^2}=0.015480834090177\ldots,}
\]
with equality exactly for rectangles. For those extremizers, the entire survival law is
\[
\mathbb P(Z_K>t)=\frac4\pi\arccos\frac{t}{\sqrt2}\quad(1\le t\le\sqrt2),
\]
with survival probability one below \(1\), zero above \(\sqrt2\), and density \(4/(\pi\sqrt{2-t^2})\) in the open support interval.

There is a quantitative rigidity identity. Let \(\nu_K\) denote arclength on \(\partial K\), normalized by \(P(K)\), pushed forward by the unoriented tangent angle \(\varphi\in\mathbb R/\pi\mathbb Z\). Let \(c_m=\int e^{4im\varphi}\,d\nu_K(\varphi)\). Then
\[
\boxed{\operatorname{Var}(Z_K)=\frac{32}{\pi^2}\sum_{m=1}^\infty\frac{|c_m|^2}{(16m^2-1)^2}.}
\]
In particular, with \(V_*=1+2/\pi-16/\pi^2\),
\[
\boxed{V_*-\operatorname{Var}(Z_K)\ge\frac{64}{225\pi^2}\iint\sin^2(2(\varphi-\psi))\,d\nu_K(\varphi)d\nu_K(\psi).}
\]
The right-hand side is zero precisely for rectangles, and its universal coefficient follows exactly from the first nonconstant Fourier mode.

## Assumptions and scope

The shape is a fixed full-dimensional compact Euclidean convex body, with arbitrary nonsmooth boundary permitted. Tangent angles exist at arclength-almost-every boundary point; the normalized arclength distribution \(\nu_K\) is a probability measure. The axis-parallel bounding rectangle is **tight**, with widths equal to the two orthogonal projection lengths; its orientation is randomized by one common uniform angle, not separately for each width. Convex order compares **normalized** perimeters, not rectangle areas, one-direction widths, or minimum-over-orientations enclosing rectangles. Strict convexity of \(\Phi\) is required only for rigidity, not the inequality.

## Proof

**1. Exact integral-geometric representation.** Parametrize the boundary by arclength \(s\), with almost-everywhere unit tangent \(t(s)=(\cos\varphi(s),\sin\varphi(s))\). Its orthogonal projection onto a line has length one-half the total variation of projected boundary traversal, a classical Cauchy projection identity valid for all convex curves. Thus the width in direction \(u_\theta\) is
\[
w_K(\theta)=\tfrac12\int_{\partial K}|u_\theta\cdot t(s)|\,ds.
\]
The bounding rectangle has perimeter \(B_K(\theta)=2[w_K(\theta)+w_K(\theta+\pi/2)]\). Therefore, with \(q(t)=|\cos t|+|\sin t|\),
\[
Z_K(\theta)=\int q(\theta-\varphi)\,d\nu_K(\varphi).
\]
Since \(1\le q\le\sqrt2\), the same bounds hold for \(Z_K\), and averaging gives \(\mathbb EZ_K=\mathbb E q(\Theta)=4/\pi\). The law of \(q(\Theta)\) is exactly that of \(Q\).

**2. Sharp simultaneous convex inequalities.** By Jensen at each orientation,
\[
\Phi(Z_K(\theta))\le\int\Phi(q(\theta-\varphi))\,d\nu_K(\varphi).
\]
Integrate uniformly in \(\theta\) and use rotation invariance: the right-hand side has expectation \(\mathbb E\Phi(Q)\). This proves the convex order for every stated \(\Phi\). For a rectangle, all nonzero arclength tangents have angles in \(\{\varphi_0,\varphi_0+\pi/2\}\bmod\pi\), and \(q\) is \(\pi/2\)-periodic, so \(Z_K(\theta)=q(\theta-\varphi_0)\). Hence every rectangle attains equality for every convex \(\Phi\).

**3. Exact Fourier variance.** The elementary absolutely uniformly convergent cosine series is
\[
q(t)=\frac4\pi-\frac8\pi\sum_{m=1}^\infty\frac{\cos(4mt)}{16m^2-1}.
\]
Convolution with \(\nu_K\) and Parseval give
\[
\operatorname{Var}(Z_K)=\frac{32}{\pi^2}\sum_{m=1}^\infty\frac{|c_m|^2}{(16m^2-1)^2}.
\]
The triangle inequality \(|c_m|\le1\) shows that the variance is at most the corresponding sum with every \(|c_m|=1\). That sum equals \(\operatorname{Var}(Q)\), where \(\mathbb EQ^2=1+2/\pi\). Subtracting gives the **exact nonnegative defect**
\[
V_*-\operatorname{Var}(Z_K)=\frac{32}{\pi^2}\sum_{m=1}^\infty\frac{1-|c_m|^2}{(16m^2-1)^2}.
\]
Since \(1-|c_1|^2=\iint[1-\cos(4(\varphi-\psi))]\,d\nu_K(\varphi)d\nu_K(\psi)=2\iint\sin^2(2(\varphi-\psi))\,d\nu_K(\varphi)d\nu_K(\psi)\), retaining the first term proves the quantitative inequality.

**4. Equality, rigid geometry, and strict convex losses.** If the variance equals \(V_*\), then \(|c_1|=1\). Equality in the triangle inequality for the integral of unit complex numbers implies \(e^{4i\varphi}\) is constant \(\nu_K\)-almost surely. Thus tangent directions belong to exactly two perpendicular unoriented axes. A convex closed curve with tangent directions only in two perpendicular lines is a rectangle: its support measure consists of two opposite pairs of facet normals, and convexity yields their four supporting facets (collinear segments merge). Conversely rectangles attain equality. For any strictly convex \(\Phi\), equality in the Jensen inequality for almost every \(\theta\) forces \(q(\theta-\varphi)\) to be \(\nu_K\)-almost surely constant; that implies vanishing variance defect by taking the strictly convex choice \(\Phi(t)=t^2\), or directly by integrating the two-point squared discrepancies. Hence equality for such \(\Phi\) likewise forces a rectangle.

**5. Exact extremal distribution.** Write \(q(\theta)=\sqrt2\cos(\theta-\pi/4)\) for \(\theta\in[0,\pi/2]\). This function increases from \(1\) to \(\sqrt2\) and decreases symmetrically. A uniform \(U\) therefore satisfies \(\Pr(Q>t)=4\pi^{-1}\arccos(t/\sqrt2)\) for \(t\in[1,\sqrt2]\); differentiate to obtain the density. The equality of laws is independent of the two side lengths because the two perpendicular tangent families contribute the same periodic kernel.

## Verification

Execute `python3 verify.py` using Python's standard library. It checks 81,920 direct pairs of independently computed bounding-rectangle-perimeter formulas from rotated polygon vertices and tangent angles for five shapes; Fourier variance against numerical orientation integration; the strict rectangular extremum and angular-dispersion lower bound; several nonquadratic convex losses; the full rectangular survival function at sampled thresholds; and the triangular symmetry-restricted spectrum. The numerical checks do not replace the general proof or assert uniqueness from finite samples.

## Relationship to prior work

Cauchy's perimeter projection formula and the total-variation identity for convex boundaries provide the classical starting point. Audet, Hansen and Messine (2008) optimize **minimum directional width** among fixed-perimeter polygons, not the random pair of perpendicular widths. Akiyama and Kamae (2022) optimize normalized variation of **a single random-direction width** and prove a degenerate segment maximizes that different statistic; it does not imply rectangle equality or convex-order domination for the sum of perpendicular widths. The published sharp positive-direction Cauchy quadrature result (2026) concerns the **supremum over convex bodies of deterministic discrete quadrature error**, not the distribution over uniformly random orientations of each body's tight bounding-rectangle perimeter. The current claim combines the random box observable, a sharp extremal law, all convex losses, rigidity, and a spectral quantitative defect. Searches of the named works and related mathematical records did not establish an equivalent full claim; unindexed historical priority is a residual risk.

## Limitations

The theorem concerns **perimeter**, not **area**, of the tight rectangular enclosure, and Euclidean dimension two only. The rotation is common to the two perpendicular directions. The theorem does not address arbitrary nonconvex shapes, stochastic orientation bias, minimum-area oriented enclosures, or independent rotations of coordinate axes. The proof is a mathematical derivation with reproducibility checks; it has not undergone independent verification or definitive historical-priority determination.

## References

1. C. Audet, P. Hansen, F. Messine, *Isoperimetric Polygons of Maximum Width*, *Discrete & Computational Geometry* 41 (2009), 45–60, DOI 10.1007/s00454-008-9103-9; first published online 2008-08-22.
2. S. Akiyama, T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1, posted 2022-01-18, especially its introduction and polygon-edge decomposition.
3. *Sharp positive \(N\)-direction Cauchy quadrature and angular rigidity*, publicly accessible mathematical research record (2026), identifier `33b1062b46ae`, especially the finding and proof of worst-case directional quadrature error.
4. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second expanded edition, Cambridge University Press, 2014 (Cauchy projection identities and curvature/surface-area measures).

# Second-order curvature gap for the regular-simplex sharpness family in spherical Grünbaum
## Finding
Let \(n\ge 3\), set \(m=n-1\), and let \(T\subset\mathbb R^m\) be the centered regular simplex with vertices \(v_0,\ldots,v_m\) satisfying \(\lVert v_i\rVert=m\), \(\langle v_i,v_j\rangle=-m\) for \(i\ne j\), and \(v_0=m e_1\). Define the gnomonic inverse
\[
G(x)=\frac{(x,1)}{\sqrt{1+\lVert x\rVert^2}}
\]
into the northern hemisphere of \(S^{n-1}\). For \(0<\rho<\pi/2\), put \(\varepsilon=\tan\rho/m\) and \(K_\rho=G(\varepsilon T)\). Then \(K_\rho\) is a spherical regular simplex with spherical centroid \(\theta=e_n\), and each vertex has spherical distance \(\rho\) from \(\theta\). If \(u=e_1\), then \(u\perp\theta\) and
\[
\frac{\sigma(K_\rho\cap u^+)}{\sigma(K_\rho)}
=\left(1-\frac1n\right)^{n-1}\left[1+\frac{n-2}{2n(n+1)}\tan^2\rho+O(\tan^4\rho)\right]
\]
as \(\rho\downarrow0\). In particular,
\[
\lim_{\rho\downarrow0}\frac{1}{\rho^2}\left(\frac{\sigma(K_\rho\cap u^+)}{(1-1/n)^{n-1}\sigma(K_\rho)}-1\right)=\frac{n-2}{2n(n+1)}.
\]
The coefficient is positive for every dimension covered by the spherical Grünbaum theorem.

## Assumptions and scope
The spherical centroid is the radial projection of the Euclidean centroid of the cone over the spherical body, equivalently the direction of \(\int_K \xi\,d\sigma(\xi)\). The spherical measure \(\sigma\) may be normalized or unnormalized because only a ratio is used. The parameter \(\rho\) is the common spherical distance from the centroid \(\theta\) to the vertices of \(K_\rho\). The result is an asymptotic statement for this canonical regular-simplex family; it does not claim a stability estimate for arbitrary spherical convex bodies.

## Proof
The symmetry group of the centered regular simplex \(T\) acts orthogonally on \(\mathbb R^m\), permutes its vertices, and has no nonzero fixed vector. The induced rotations \(\operatorname{diag}(Q,1)\) preserve \(K_\rho\). Hence the horizontal component of \(\int_{K_\rho}\xi\,d\sigma(\xi)\) is fixed by the simplex symmetry group and must vanish, while its last component is positive. Thus the spherical centroid is exactly \(\theta=e_n\). Also \(\lVert \varepsilon v_i\rVert=\tan\rho\), so each vertex has angular distance \(\rho\) from \(\theta\); equal pairwise dot products of the \(v_i\) imply equal spherical edge lengths.

The gnomonic area formula is
\[
d\sigma(G(x))=(1+\lVert x\rVert^2)^{-n/2}\,dx.
\]
Because \(v_0=m e_1\) and \(\langle v_0,v_j\rangle=-m\) for \(j>0\), the facet opposite \(v_0\) lies in \(x_1=-1\). Therefore
\[
T_+:=T\cap\{x_1\ge0\}=v_0+\lambda(T-v_0),\qquad \lambda=\frac{m}{m+1},
\]
so \(\operatorname{vol}(T_+)/\operatorname{vol}(T)=\lambda^m=(m/(m+1))^m=(1-1/n)^{n-1}\).

For a uniform random point \(X\) in \(T\), the Dirichlet barycentric-coordinate identities give
\[
\mathbb E\lVert X\rVert^2=\frac{m^2}{m+2}.
\]
The centroid of \(T_+\) is \(v_0/(m+1)\), while its centered covariance is \(\lambda^2\) times that of \(T\). Hence, for a uniform random point \(X_+\) in \(T_+\),
\[
\mathbb E\lVert X_+\rVert^2
=\frac{m^2}{(m+1)^2}+\frac{m^2}{(m+1)^2}\frac{m^2}{m+2},
\]
and therefore
\[
\mathbb E\lVert X_+\rVert^2-\mathbb E\lVert X\rVert^2
=-\frac{m^2(m-1)}{(m+1)^2(m+2)}.
\]

Uniformly for \(y\) in the fixed compact simplex \(T\),
\[
(1+\varepsilon^2\lVert y\rVert^2)^{-n/2}
=1-\frac n2\varepsilon^2\lVert y\rVert^2+O(\varepsilon^4).
\]
Applying this expansion to the numerator and denominator gnomonic integrals and taking their quotient yields
\[
\frac{\sigma(K_\rho\cap u^+)}{\sigma(K_\rho)}
=\left(\frac{m}{m+1}\right)^m
\left[1+\frac{m^2(m-1)}{2(m+1)(m+2)}\varepsilon^2+O(\varepsilon^4)\right].
\]
Since \(m\varepsilon=\tan\rho\) and \(m=n-1\), this becomes the stated formula. Finally \(\tan^2\rho=\rho^2+O(\rho^4)\), giving the limit.

## Verification
The accompanying `verify.py` checks, with exact rational arithmetic for \(3\le n\le 80\), the simplex second-moment identity, the cap homothety moment identity, the moment difference, and the conversion of the quadratic coefficient from \(\varepsilon\) to \(\tan\rho\). The proof itself establishes the identities for every \(n\ge3\); the finite replay is an arithmetic sanity check, not an exhaustive proof over the infinite dimension range.

## Relationship to prior work
Myroshnychenko, Ryabogin, Tatarko, and Yaskin prove the sharp spherical Grünbaum inequality and, in their optimality Step 7, use spherical simplices converging to a point. Their displayed argument records only an \(O(\varepsilon_i^2)\) discrepancy between the spherical and Euclidean ratios before taking the limit. The present calculation specializes to the symmetry-canonical regular-simplex sharpness family and resolves that hidden quadratic term exactly. It does not change the sharp constant and is not implied by the Euclidean stability theorem for Grünbaum's inequality, which controls geometric closeness to cones rather than the curvature correction of a spherical sharpness family.

## Limitations
No claim is made about the smallest possible quadratic deficit among all shrinking spherical simplices, about a global spherical stability modulus, or about higher-order terms. The originality search found no statement with this coefficient, but an unindexed calculation in private notes or other literature remains a residual risk.

## References
1. S. Myroshnychenko, D. Ryabogin, K. Tatarko, V. Yaskin, *The Spherical Grünbaum Inequality*, arXiv:2607.16924v1, first public 2026-07-18.
2. L. Tanganelli Castrillón, *An improved stability result for Grünbaum's inequality*, arXiv:2410.12072, later published in Journal of Geometric Analysis 35 (2025).
3. M. Fradelizi, D. Langharst, J. Liu, F. Marín Sola, S. Tang, *Grünbaum's inequality for Gaussian and convex probability measures*, arXiv:2507.06759.

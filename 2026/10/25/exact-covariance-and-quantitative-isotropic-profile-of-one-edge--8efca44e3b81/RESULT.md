# Exact covariance and quantitative isotropic profile of one-edge-weighted cycle zonotopes

## Finding
Let \(d\ge2\) be an integer, \(t\ge0\), and
\[
K_{d,t}=[-1/2,1/2]^d+[-t\mathbf1/2,t\mathbf1/2]\subset\mathbb R^d.
\]
For \(t>0\), this is an affine model for the centered graphical zonotope of a \((d+1)\)-cycle whose distinguished edge has weight \(t\) and whose other edges have weight one. Write \(P=I_d-\mathbf1\mathbf1^T/d\) and \(Q=\mathbf1\mathbf1^T/d\). For \(X\) uniformly sampled from \(K_{d,t}\), the following **entire covariance profile** holds:
\[
\operatorname{vol}_d(K_{d,t})=1+dt,\qquad
\operatorname{Cov}(X)=
\frac{1+(d+2)t}{12(1+dt)}P+
\frac{1+2t+dt^2}{12}Q.
\]
Thus the covariance eigenvalue on \(\mathbf1^\perp\) has multiplicity \(d-1\); the eigenvalue along \(\mathbf1\) is simple, and exceeds the transverse eigenvalue by
\[
\frac{dt^2(3+dt)}{12(1+dt)}>0\quad(t>0).
\]
With \(L(K)^{2d}=\det\operatorname{Cov}(X)/(\operatorname{vol}_d K)^2\), this yields the exact normalized profile
\[
R_d(t):=12^d L(K_{d,t})^{2d}=
\frac{[1+(d+2)t]^{d-1}(1+2t+dt^2)}{(1+dt)^{d+1}}.
\]
Its logarithmic derivative and sharp second-order response at the symmetric point are
\[
\frac{d}{dt}\log R_d(t)=
\frac{2d(d-1)t(t-1)}{(1+dt)[1+(d+2)t](1+2t+dt^2)},
\qquad
\left.\frac{d^2}{dt^2}\log R_d(t)\right|_{t=1}=
\frac{2d(d-1)}{(d+1)(d+3)^2}.
\]
Consequently \(R_d\) decreases strictly for \(0<t<1\), increases strictly for \(t>1\), and has exact minimum \((d+3)^d/(d+1)^{d+1}\) at \(t=1\). **The minimizing shape and its uniqueness are already known** from Kipp's more general theorem; the result here is the complete finite-parameter covariance, determinant profile, anisotropy, and sharp response coefficient.

## Assumptions and scope
All bodies use the stated coordinate normalization and ordinary Euclidean Lebesgue volume. The statement is valid for every integer \(d\ge2\) and real \(t\ge0\), including the cube at \(t=0\). For a cycle of \(d+1\) vertices, delete the distinguished edge to obtain a path. Its \(d\) oriented incidence vectors form a basis of the zero-sum hyperplane; the remaining edge vector is, up to sign, their sum. This linear isomorphism carries the centered cycle graphical zonotope to \(K_{d,t}\). The scalar \(L\) is affine invariant, whereas the displayed Euclidean covariance eigenvalues refer specifically to \(K_{d,t}\), not to the original graph-vertex coordinates.

## Proof
1. **Slice and measure.** Put \(v=x-\overline x\mathbf1\in\mathbf1^\perp\), where \(\overline x=d^{-1}\sum_i x_i\). Let \(a=\min_i v_i\), \(b=\max_i v_i\), \(\ell=1-b+a\), and \(c=-(a+b)/2\). The projection of \(K_{d,t}\) to \(\mathbf1^\perp\) is \(D=\{v:b-a\le1\}\). Over \(v\in D\), the permitted \(\overline x\) form an interval of length \(\ell+t\) and midpoint \(c\). Use the translation-invariant measure \(d\nu=\sqrt d\,dH_{d-1}\) on \(\mathbf1^\perp\), so that \(dx=d\nu(v)\,d\overline x\). Ordering the \(d\) coordinates of \(v\), its \(d-1\) successive nonnegative gaps together with \(\ell\) form a \(d\)-coordinate simplex. On each of the \(d!\) order chambers, \(d\nu\) is constant in these gaps. Therefore their normalized law under flat \(d\nu\) is \(\operatorname{Dirichlet}(1,\ldots,1)\). The elementary simplex integrals give
\[
\int_D 1\,d\nu=d,\qquad \int_D\ell\,d\nu=1,
\qquad \int_D\ell^2\,d\nu=\frac2{d+1}.
\]
It follows directly that \(\operatorname{vol}(K_{d,t})=\int_D(\ell+t)d\nu=1+dt\).

2. **Transverse covariance.** By coordinate permutation symmetry, \(\int_Dvv^T\,d\nu\) and \(\int_D\ell vv^T\,d\nu\) are multiples of \(P\). The measure \(\ell d\nu\) is the projection to \(\mathbf1^\perp\) of uniform Lebesgue measure on the unit cube, hence
\[
\int_D\ell vv^T\,d\nu=P/12.
\]
Under flat \(d\nu\), write the ordered point as \(v=\sum_{j=1}^{d-1}g_jP(\mathbf1_{\{j+1,\ldots,d\}})\). Dirichlet second moments \(\mathbb E(g_ig_j)=(1+\delta_{ij})/[d(d+1)]\) together with
\[
\sum_{j=1}^{d-1}\left\|P\mathbf1_{\{j+1,\ldots,d\}}\right\|^2=\frac{d^2-1}{6},
\qquad \left\|\sum_{j=1}^{d-1}P\mathbf1_{\{j+1,\ldots,d\}}\right\|^2=\frac{d(d^2-1)}{12}
\]
give \(\operatorname{tr}(\int_Dvv^Td\nu)=(d-1)(d+2)/12\), whence \(\int_Dvv^Td\nu=(d+2)P/12\). Dividing the sum of the two weighted contributions by \(1+dt\) proves the asserted transverse covariance.

3. **Longitudinal covariance.** Given \(v\), the conditional \(\overline x\) has mean \(c\) and second moment \(c^2+(\ell+t)^2/12\). For ordered gaps \(g_j\),
\[
c=-\frac1{2d}\sum_{j=1}^{d-1}(2j-d)g_j.
\]
Because \(\sum_j(2j-d)=0\) and \(\sum_j(2j-d)^2=d(d-1)(d-2)/3\), Dirichlet moments yield
\[
\int_Dc^2\,d\nu=\frac{(d-1)(d-2)}{12d(d+1)}.
\]
The original unit cube's coordinate mean has variance \(1/(12d)\), so
\[
\int_D\left(\ell c^2+\frac{\ell^3}{12}\right)d\nu=\frac1{12d}.
\]
Expand \((\ell+t)c^2+(\ell+t)^3/12\), use the preceding integrals and \(\int_D\ell d\nu=1\), \(\int_D1d\nu=d\), to obtain
\[
\mathbb E\overline X^{\,2}=
\frac{1+(d+2)t+3dt^2+d^2t^3}{12d(1+dt)}=
\frac{1+2t+dt^2}{12d}.
\]
Permutation symmetry forces \(\mathbb E[(X-\overline X\mathbf1)\overline X]=0\); central symmetry gives \(\mathbb EX=0\). Therefore the eigenvalue in the unit direction \(\mathbf1/\sqrt d\) is \(d\mathbb E\overline X^2=(1+2t+dt^2)/12\), as asserted.

4. **Determinant and sharp response.** The determinant is \(\lambda_\perp^{d-1}\lambda_\parallel\). Divide by \((1+dt)^2\) to obtain \(R_d(t)\). A direct logarithmic derivative simplifies to the displayed factored rational expression. For \(d\ge2\) its denominator is positive on \(t\ge0\), and its numerator has the sign of \(t-1\) when \(t>0\). Differentiating at \(t=1\) gives the exact positive curvature. The eigenvalue difference follows by subtracting the displayed formulas. No asymptotic or finite-dimensional extrapolation is used to prove these identities.

## Verification
A reproducible checker, `verify.py`, evaluates exact rational covariance and volume identities using independent polytope-hull triangulations for dimensions \(2,3,4\) and rational weights \(1/4,1,3\), and symbolically checks the logarithmic derivative and curvature for arbitrary formal dimension. The finite checks corroborate, but are not a substitute for, the preceding all-dimensional Dirichlet proof. Run `python verify.py`; it uses NumPy, SciPy, and SymPy.

## Relationship to prior work
Padrol, Pilaud, and Poullot develop deformation theory of graphical zonotopes [1], motivating the weighted-cycle family. Kipp [2, Proposition 6.5], in a stronger statement for **all** zonotopes with at most \(d+1\) generators, already proves that the symmetric \(t=1\) body is the unique affine-isomorphism class minimizing the isotropic constant. Thus the optimal parameter and qualitative uniqueness are **not claimed as discoveries**. Conway and Sloane [3] also compute the normalized second moments of the type-\(A\) root-lattice Voronoi cells, corresponding to the symmetric case after changing coordinates. The contribution established here is an exact **parameterwise** covariance operator, rational isotropic determinant function, anisotropy gap, and local curvature. Neither [1] nor the full proof of [2, Sections 5–6] supplies that parameterwise information.

## Limitations
The two eigenvalue formulas concern the diagonal-segment coordinate model; a nonorthogonal graph-incidence change of coordinates changes the Euclidean spectrum, though not the affine-invariant isotropic constant. No assertion is made about arbitrary independent weights on every cycle edge or about any zonotope with more than \(d+1\) generators. The optimality statement is previously known; independent review of the new exact formulas has not been performed. Equivalent formulas in older box-spline or multivariate-moment literature cannot be ruled out solely by title searches.

## References
[1] A. Padrol, V. Pilaud, and J. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first posted 2021-11-24. https://arxiv.org/abs/2111.12422

[2] C. Kipp, *Isotropic constants and regular polytopes*, arXiv:2407.01353, first posted 2024-07-01, especially Proposition 6.5. https://arxiv.org/pdf/2407.01353

[3] J. H. Conway and N. J. A. Sloane, *Voronoi Regions of Lattices, Second Moments of Polytopes, and Quantization*, IEEE Transactions on Information Theory 28 (1982), 211–226. https://neilsloane.com/doc/Me82.pdf

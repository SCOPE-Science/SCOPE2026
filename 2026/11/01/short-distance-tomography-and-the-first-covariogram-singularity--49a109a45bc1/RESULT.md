# Short-distance tomography and the first covariogram singularity of orthotopes

## Finding

For an axis-aligned Euclidean orthotope in dimension \(d\ge2\), the distribution of the normalized distance between two independent uniform points has an exact short-range polynomial whose \(d-1\) nontrivial coefficients determine **all unordered side-length ratios**. Any \(d-1\) distinct normalized distance thresholds, provided they lie strictly before the shortest-side threshold for every candidate box, suffice for this reconstruction. For generically distinct side lengths, \(d-2\) or fewer such thresholds never suffice locally. The first departure from the polynomial at the shortest-side threshold has an exact positive leading coefficient and exponent \((d+3)/2\), detecting the multiplicity of the shortest side.

More explicitly, let \(Q=\prod_{i=1}^d[0,\ell_i]\), where \(\ell_i>0\), and let \(X,Y\) be independent uniform random points in \(Q\). Put \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\), \(V=\prod_i\ell_i\), \(R=(V/\kappa_d)^{1/d}\), \(c_i=R/\ell_i\), \(\rho_*=\min_i(\ell_i/R)\), and
\[
F_Q(\rho)=\Pr\bigl(\|X-Y\|_2\le \rho R\bigr).
\]
With \(e_k(c)\) the elementary symmetric function of degree \(k\) in \((c_1,\ldots,c_d)\), define
\[
 b_{d,k}=\frac{\Gamma(1+d/2)}{\pi^{k/2}\Gamma(1+(d+k)/2)},\quad
 P_Q(\rho)=\rho^d\sum_{k=0}^d(-1)^k b_{d,k}e_k(c)\rho^k.
\]
Then
\[
\boxed{F_Q(\rho)=P_Q(\rho)\quad (0\le\rho\le\rho_*).}
\]
Both endpoint coefficients are shape-independent: \(e_0(c)=1\) and \(e_d(c)=1/\kappa_d\). The intervening coefficients \(e_1(c),\ldots,e_{d-1}(c)\) determine the multiset \(\{c_1,\ldots,c_d\}\), hence the unordered side-length ratios \(\{\ell_i/R\}\), by the positive roots of
\[
\boxed{T^d-e_1(c)T^{d-1}+e_2(c)T^{d-2}-\cdots+(-1)^d/\kappa_d=0.}
\]
In particular, the germ of \(F_Q\) at zero determines \(Q\) up to translation, orthogonal coordinate changes, and positive scaling. Known volume removes scaling ambiguity.

For any \(d-1\) distinct thresholds \(0<\rho_1<\cdots<\rho_{d-1}\) satisfying \(\rho_{d-1}<\rho_*\), the values \(F_Q(\rho_j)\) determine those \(d-1\) intermediate coefficients via one nonsingular Vandermonde system. This identification is among boxes whose thresholds all belong to their short-range polynomial windows. Conversely, given at most \(d-2\) fixed such thresholds and a box with pairwise distinct side lengths, there is a positive-dimensional local family of non-similar boxes of the same dimension having identical measured values at those thresholds. Thus \(d-1\) is generically minimal for this finite, short-range experiment.

Let \(m=\#\{i:\ell_i=\min_j\ell_j\}\). As \(\rho\downarrow\rho_*\) from above,
\[
\boxed{F_Q(\rho)-P_Q(\rho)
= C_{d,m}(\rho_*)\,(\rho-\rho_*)^{(d+3)/2}
+o\bigl((\rho-\rho_*)^{(d+3)/2}\bigr),}
\]
where
\[
\boxed{C_{d,m}(s)=\frac{8m\,\kappa_{d-1}\,2^{(d-1)/2}}{\kappa_d(d+1)(d+3)}s^{(d-3)/2}>0.}
\]
Consequently \(\rho_*\) is exactly the right endpoint of the initial polynomial window. In dimension three the coefficient simplifies to \(m/2\), independently of the side-length ratios.

## Assumptions and scope

The dimension \(d\ge2\) is fixed. All side lengths are strictly positive; equal side lengths are allowed. Boundaries have zero probability under the uniform distributions, so \(<\) and \(\le\) give the same values. The polynomial identity and reconstruction from its germ hold for **every** orthotope. The local minimality assertion assumes pairwise distinct side lengths, while the first-transition asymptotic allows ties and explicitly includes their multiplicity. The finite-measurement uniqueness assertion is restricted to the common known polynomial regime of the compared boxes; it does **not** assert global uniqueness from arbitrary large-radius samples.

## Proof

**1. Exact polynomial.** The difference vector \(Z=X-Y\) has probability density
\[
 f_Z(z)=\frac1V\prod_{i=1}^d\left(1-\frac{|z_i|}{\ell_i}\right)_+.
\]
For \(\rho R\le\min_i\ell_i\), the positive-part truncations are inactive on the Euclidean ball \(\|z\|_2\le\rho R\). Rescale \(z=\rho Ru\), expand the product, and integrate over the unit ball. Rotational/permutation symmetry makes all subsets of cardinality \(k\) have the same integral. Repeated beta integration (equivalently, the Dirichlet integral) gives
\[
 \frac1{\kappa_d}\int_{\|u\|_2\le1}\prod_{i=1}^k|u_i|\,du
 =\frac{\Gamma(1+d/2)}{\pi^{k/2}\Gamma(1+(d+k)/2)}=b_{d,k}.
\]
Since \(R^d/V=1/\kappa_d\), substitution proves the displayed expression for \(P_Q\). Multiplication yields \(\prod_i c_i=R^d/V=1/\kappa_d\).

**2. Reconstruction and sharp sample count.** Reading coefficients of the polynomial germ recovers \(e_1,\ldots,e_{d-1}\) because all \(b_{d,k}\) are strictly positive. Together with \(e_d=1/\kappa_d\), Vieta's formulas give the monic polynomial whose positive root multiset is precisely the \(c_i\). Its roots determine the unordered ratios \(\ell_i/R=1/c_i\). This proves global identifiability from the germ, including repeated lengths. If the volume is separately supplied, \(R\) is known and so are the actual \(\ell_i\).

For finite sampling, subtract the known first and last terms from \(F_Q(\rho_j)/\rho_j^d\) and divide by \(\rho_j\). The resulting values are
\[
 \sum_{k=1}^{d-1}(-1)^k b_{d,k}e_k(c)\rho_j^{k-1},
 \qquad j=1,\ldots,d-1.
\]
The coefficient matrix is the ordinary Vandermonde matrix \((\rho_j^{k-1})\), with determinant \(\prod_{i<j}(\rho_j-\rho_i)\ne0\). All \(d-1\) unknowns are therefore uniquely recovered, and so is the box's shape. This comparison requires all considered boxes to have these nodes strictly inside their polynomial windows.

For sharpness, restrict to boxes with pairwise distinct positive \(c_i\), normalized by \(\prod c_i=1/\kappa_d\). This is a smooth \((d-1)\)-dimensional manifold (up to permutation). The map to \((e_1,\ldots,e_{d-1})\) is locally invertible there: the full elementary-symmetric map has Jacobian determinant equal, up to sign, to \(\prod_{i<j}(c_i-c_j)\ne0\), and fixing \(e_d\) restricts it to corresponding local coordinate hypersurfaces. At \(q\le d-2\) distinct positive nodes the map from these coordinates to sampled probabilities has differential rank \(q\), because its first \(q\) nonzero coefficient columns form a scaled Vandermonde matrix. The implicit function theorem then produces a smooth local fiber of dimension \(d-1-q\ge1\). Shrinking the neighborhood maintains positivity, pairwise distinctness, and the short-range inequalities. This proves the claimed generic minimality.

**3. First singularity.** Write \(a=\min_i\ell_i=R\rho_*\) and \(r=a+\varepsilon\), where \(\varepsilon>0\) is small enough that \(r\) is below every strictly larger side length and also \(r<\sqrt2 a\). Within \(\|z\|_2\le r\), at most one coordinate can exceed its side length. Hence the difference between the actual radial integral and the untruncated polynomial continuation is the sum of exactly \(2m\) positive cap integrals, one for each sign of each shortest coordinate.

On the cap \(z_i>a\), writing \(z_i=t\), the missing untruncated integrand equals
\[
 \frac1V\left(\frac{t}{a}-1\right)
 \prod_{j\ne i}\left(1-\frac{|z_j|}{\ell_j}\right).
\]
Uniformly on these caps, the product over \(j\ne i\) is \(1+O(\sqrt\varepsilon)\), because \(\sum_{j\ne i}z_j^2\le r^2-a^2=O(\varepsilon)\). Thus the total difference has leading term
\[
 \frac{2m\kappa_{d-1}}{Va}
 \int_a^{a+\varepsilon}(t-a)(r^2-t^2)^{(d-1)/2}\,dt.
\]
With \(u=t-a\), uniformly on \(0\le u\le\varepsilon\),
\[
 r^2-t^2=2a(\varepsilon-u)+O(\varepsilon^2).
\]
Rescale \(u=\varepsilon v\), apply dominated convergence, and use
\[
 \int_0^1v(1-v)^{(d-1)/2}\,dv
 =\frac4{(d+1)(d+3)}.
\]
The leading coefficient in powers of \(\varepsilon\) is \(8m\kappa_{d-1}(2a)^{(d-1)/2}/[Va(d+1)(d+3)]\). Finally put \(\varepsilon=R(\rho-\rho_*)\), \(a=R\rho_*\), \(V=\kappa_dR^d\). This yields \(C_{d,m}(\rho_*)\), with strictly positive sign. The polynomial identity cannot extend to any interval above \(\rho_*\), and in dimension three the coefficient simplifies to \(m/2\).

## Verification

The included standalone `verify.py` runs with the Python standard library. It checks the normalization and shape-independent leading coefficient in dimensions two through five; independently evaluates the two-dimensional polar integral; solves the finite Vandermonde inverse problem for multiple boxes and dimensions; checks the first-cap asymptotic by quadrature; and verifies the dimension-three coefficient simplification. The program is diagnostic only. The algebraic and asymptotic proofs above establish the all-dimensional assertions.

Run from the extracted package directory using `python3 verify.py`.

## Relationship to prior work

Wang (2026, arXiv:2610.01916) studies the volume-normalized pair-distance profile \(F_Q\) for general convex bodies, its Brunn--Minkowski behavior, variation, and uniqueness for an associated Minkowski measure, while emphasizing that the radial pair-distance profile is coarser than the full covariogram. The present result gives **explicit finite-data shape rigidity within orthotopes** and the first singular departure from the local polynomial; it is not an instance of Wang's global Minkowski-measure uniqueness theorem.

Lellouche and Souris (2019/2020) derive convolution formulas for pair distances, including planar rectangles and higher-dimensional cubes. Those are the core known ingredients for the forward distribution, and their planar/cube cases are **not** claimed as new. The new claimed content is the sharp, all-dimensional finite-sample inverse classification for anisotropic orthotopes and the universal first-transition exponent and coefficient.

Mémoli and Needham (2022, arXiv:1810.09646) formulate inverse problems for global distance distributions and prove rigidity/nonrigidity results for manifolds and metric graphs, but do not formulate this finite-sample orthotope classification. Other indexed projection-tomography results concern moments of random projection volumes or widths, which are distinct observables and do not imply this short-range pair-distance theorem.

## Limitations

Originality is assessed from the literature available for this study, not certified against every unindexed source. Previously published planar-rectangle and cube distance-distribution formulas are acknowledged. There is no claim of arbitrary-convex-body shape reconstruction, no unconditional uniqueness from just \(d-1\) radii outside the shared short-range regime, no statistical-noise stability theorem, and no complete description beyond the **first** non-polynomial threshold. All proof and computational review here is non-independent; independent audit is not performed.

## References

1. S. Wang, *A Brunn--Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916, first posted 2026-10-01. https://arxiv.org/abs/2610.01916
2. S. Lellouche and M. Souris, *Distribution of Distances between Elements in a Compact Set*, Stats 3 (2020), 1--15, first published 2019-12-26, DOI 10.3390/stats3010001. https://doi.org/10.3390/stats3010001
3. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, arXiv:1810.09646, first posted 2018-10-23. https://arxiv.org/abs/1810.09646
4. V. K. Ohanyan and V. H. Khalatyan, *Relation between the covariogram and distribution function of the distance between two uniform and independent points*, Proc. Yerevan State Univ. Phys. Math. Sci. 56 (2022), 33--42, DOI 10.46991/PYSU:A/2022.56.1.033.
5. B. Galerne, *Computation of the perimeter of measurable sets via their covariogram*, Image Analysis & Stereology 30 (2011), 39--51, DOI 10.5566/ias.v30.p39-51.

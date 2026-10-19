# Sharp orientation-dependent level repulsion for a diagonally perturbed two-dimensional null space

## Finding

Let \(a=(a_1,a_2,a_3)^{\mathsf T}\) be any real unit vector. Let \(D=\operatorname{diag}(d_1,d_2,d_3)\) have independent \(\operatorname{Unif}[0,1]\) entries, and let \(U\) be any real \(3\times2\) matrix with orthonormal columns spanning \(a^\perp\). Write \(\Delta\) for the difference between the larger and smaller eigenvalues of \(C=U^{\mathsf T}DU\), and put \(p_i=a_i^2\), so \(p_1+p_2+p_3=1\).

**Exact orientation-dependent small-gap law.** If every \(p_i>0\), put
\[
 t_0=\frac{2\sqrt{p_1p_2p_3}}{1-\min_i p_i}.
\]
Then, for every \(0\le t\le t_0\),
\[
 \boxed{\Pr(\Delta\le t)=\frac{\pi t^2}{2\sqrt{p_1p_2p_3}}-\frac{t^3}{3p_1p_2p_3}.}
\]
The interval is sharp: for every \(t>t_0\), the cubic polynomial on the right is strictly smaller than the true cumulative probability.

If exactly one \(p_i\) is zero and the other two equal \(u,v>0\), \(u+v=1\), then for \(0\le t\le\min(u,v)\),
\[
 \boxed{\Pr(\Delta\le t)=2t-\frac{t^3}{3uv}.}
\]
If two \(p_i\) vanish, then, for \(0\le t\le1\),
\[
 \boxed{\Pr(\Delta\le t)=2t-t^2.}
\]
Consequently, for every \(s>0\), the inverse gap moment \(\mathbb E[\Delta^{-s}]\) is finite exactly when \(s<2\) if \(p_1p_2p_3>0\), and exactly when \(s<1\) if \(p_1p_2p_3=0\). The exponent changes discontinuously when the kernel acquires a coordinate-aligned direction.

**Connection to actual diagonal perturbation.** Let \(A=aa^{\mathsf T}\), a symmetric \(3\times3\) rank-one projection with a two-dimensional null space. For \(0<\eta<1\) define \(B_\eta=A^{\mathsf T}A+\eta D=aa^{\mathsf T}+\eta D\), and denote its ordered eigenvalues by \(\lambda_1(\eta)\le\lambda_2(\eta)\le\lambda_3(\eta)\). If \(\mu_1\le\mu_2\) are the eigenvalues of \(C\), then for \(j=1,2\), samplewise,
\[
 \eta\mu_j-\frac{\eta^2}{1-\eta}\le\lambda_j(\eta)\le\eta\mu_j.
\]
In particular,
\[
 \left|\frac{\lambda_2(\eta)-\lambda_1(\eta)}{\eta}-\Delta\right|\le\frac{2\eta}{1-\eta},
\]
so the normalized separation of the two formerly zero eigenvalues converges uniformly over all diagonal draws to \(\Delta\) as \(\eta\downarrow0\). This statement concerns the perturbative first-order limit; the displayed exact probability polynomials do not purport to be exact for fixed positive \(\eta\).

## Assumptions and scope

All matrices are real and finite-dimensional, calculations are in exact arithmetic, and the three diagonal perturbations are independent and continuously uniform on \([0,1]\). A choice of signs for \(a\), or of orthonormal basis \(U\), does not change the law. No generic-position hypothesis is imposed: the coordinate-aligned boundary cases are classified. The inverse moments concern the limiting two-dimensional compression gap, not unbounded dimension or a finite-precision eigensolver. The ordering of limits for the original perturbed matrix is first \(\eta\downarrow0\), then the small-gap threshold \(t\downarrow0\).

## Proof

**1. Reduction to an ellipse.** Write \(p=p_1\), \(q=p_2\), \(r=p_3\) and \(x=d_1-d_3\), \(y=d_2-d_3\). Since \(UU^{\mathsf T}=I-aa^{\mathsf T}\), one has
\[
 \operatorname{tr}C=\sum_i(1-p_i)d_i,
 \qquad \operatorname{tr}(C^2)=\sum_i(1-p_i)^2d_i^2+\sum_{i\ne j}p_ip_jd_id_j.
\]
For any symmetric \(2\times2\) matrix, the squared eigenvalue gap equals \(2\operatorname{tr}(C^2)-(\operatorname{tr}C)^2\). Translation of all \(d_i\) by a common scalar does not change the gap, whence
\[
 \Delta^2=(x,y)M(x,y)^{\mathsf T},\quad
 M=\begin{pmatrix}(1-p)^2&pq-r\\pq-r&(1-q)^2\end{pmatrix},
 \qquad \det M=4pqr.
\]

**2. Exact density in difference coordinates.** For \(d_i\) independent uniform on \([0,1]\), the joint density of \((x,y)\) is
\[
 h(x,y)=\bigl(1-w(x,y)\bigr)_+,\qquad
 w(x,y)=\max(0,x,y)-\min(0,x,y)
 =\frac{|x|+|y|+|x-y|}{2}.
\]
Indeed, after fixing \((x,y)\), the allowed interval of \(d_3\) has precisely that length. Assume \(pqr>0\), so \(M\) is positive definite. The dual norms of the three linear forms \(x\), \(y\), and \(x-y\) on the ellipsoid \((x,y)M(x,y)^{\mathsf T}\le t^2\) are, respectively,
\[
 \frac{t(1-q)}{2\sqrt{pqr}},\qquad
 \frac{t(1-p)}{2\sqrt{pqr}},\qquad
 \frac{t(1-r)}{2\sqrt{pqr}}.
\]
Since \(w=\max\{|x|,|y|,|x-y|\}\), the whole ellipsoid lies in \(w\le1\) exactly when \(t\le t_0\). Above that threshold, an open positive-area subset lies in \(w>1\), establishing sharpness of the polynomial interval.

**3. Ellipse integration.** The area of this ellipsoid equals \(\pi t^2/\sqrt{\det M}\). For every real two-vector \(\ell\), the change of variables \((x,y)^{\mathsf T}=tM^{-1/2}z\), \(\|z\|\le1\), gives
\[
 \int_{(x,y)M(x,y)^{\mathsf T}\le t^2}|\ell_1x+\ell_2y|\,dx\,dy
 =\frac{4t^3}{3\sqrt{\det M}}\sqrt{\ell^{\mathsf T}M^{-1}\ell}.
\]
The factor \(4/3\) is the integral of the absolute first coordinate over the unit disk. For \(\ell=(1,0),(0,1),(1,-1)\), the square roots on the right are \((1-q)/(2\sqrt{pqr})\), \((1-p)/(2\sqrt{pqr})\), and \((1-r)/(2\sqrt{pqr})\). Their sum is \(1/\sqrt{pqr}\). Integrating \(1-w\) thus gives exactly
\[
 \frac{\pi t^2}{2\sqrt{pqr}}-\frac{t^3}{3pqr}.
\]

**4. Coordinate-aligned boundary.** If, without loss of generality, \(p_1=0\), an orthonormal basis of \(a^\perp\) consists of \(e_1\) and a vector supported on coordinates \(2,3\). Thus the two eigenvalues of \(C\) are \(d_1\) and \(Z=p_3d_2+p_2d_3\). If \(p_2p_3>0\), the density of \(Z\) on \([0,\min(p_2,p_3)]\) is \(z/(p_2p_3)\), and by reflection it has the same behavior near \(1\). Conditioning on \(Z\), for \(t\le\min(p_2,p_3)\), yields
\[
 \Pr(|d_1-Z|\le t)
 =2t-2\int_0^t\frac{(t-z)z}{p_2p_3}\,dz
 =2t-\frac{t^3}{3p_2p_3}.
\]
If two squared coordinates vanish, the compression eigenvalues are two independent uniform variables, giving \(2t-t^2\) for \(0\le t\le1\).

**5. Inverse moments.** Since \(0\le\Delta\le1\) and the gap has no atom at zero, for \(s>0\) the layer-cake identity gives
\[
 \mathbb E[\Delta^{-s}]=1+s\int_0^1t^{-s-1}\Pr(\Delta<t)\,dt.
\]
The exactly established leading powers \(t^2\) and \(t\), each with positive coefficient, make the integral finite precisely for \(s<2\) and \(s<1\), respectively.

**6. Perturbation transfer.** In the orthonormal basis \([U,a]\), the original perturbed matrix has block form
\[
 \begin{pmatrix}\eta C&\eta h\\\eta h^{\mathsf T}&1+\eta\alpha\end{pmatrix},\qquad
 h=U^{\mathsf T}Da,\quad\alpha=a^{\mathsf T}Da,
\]
with \(\|h\|\le1\) and \(0\le\alpha\le1\). Its two smallest eigenvalues belong to \([0,\eta]\) by Weyl's inequality. For \(\lambda\in[0,\eta]\), the Schur complement of the lower-right block is
\[
 K(\lambda)-\lambda I_2,
 \qquad K(\lambda)=\eta C-\frac{\eta^2hh^{\mathsf T}}{1+\eta\alpha-\lambda}.
\]
The ordered eigenvalue functions of \(K(\lambda)\) are nonincreasing in \(\lambda\). Each crosses \(\lambda\) exactly once on this interval, with the crossings giving the two smallest eigenvalues of the full matrix (by Schur-complement inertia). Weyl's inequality applied to \(K(\lambda)\) and \(\eta C\) bounds the \(j\)-th crossing between \(\eta\mu_j-\eta^2/(1-\eta)\) and \(\eta\mu_j\). Subtracting proves the uniform gap bound.

## Verification

The accompanying `verify_gap.py` checks the symbolic quadratic-form determinant and three dual-norm identities; numerically integrates the ellipsoid density for four orientations at three radii each; compares direct uniform sampling with the interior and boundary cumulative distributions; and verifies the perturbative matrix eigenvalue bounds. The fixed-seed numerical sampling is evidence for implemented formulas, not a substitute for the preceding exact continuum proof. Run `python verify_gap.py` after installing `requirements.txt`.

## Relationship to prior work

Kressner and Shao, *On a randomized small-block Lanczos method for large-scale null space computations* (arXiv:2407.04634, initially public July 5, 2024), introduce iid uniform diagonal perturbations to separate a multiple zero-eigenvalue cluster. Their Theorem 4 provides a general high-probability linear upper bound on the probability of an unusually small finite-perturbation eigenvalue gap. The present result instead classifies the **exact first-order compressed gap distribution** for the minimal rank-one, nullity-two model, including its orientation-dependent order of repulsion, sharp local polynomial interval, and inverse-moment cutoff. Their general theorem does not determine those quantities.

Kumar and Ahmed, *New Spectral Statistics for Ensembles of \(2\times2\) Real Symmetric Random Matrices* (Acta Polytechnica 57, 2017, DOI:10.14311/AP.2017.57.0418), analyze eigenvalue-spacing distributions of other two-dimensional random-matrix ensembles and obtain linear small-gap densities. Their ensembles use distinct unconstrained matrix-entry laws; the present compression has a specific correlated traceless part inherited from three independent diagonal entries and a prescribed null-space orientation. Standard two-level repulsion ideas provide context but not the stated orientation-dependent constants or boundary classification.

## Limitations

The probabilities are exact for the first-order compressed gap, not for every fixed positive perturbation strength. Three ambient coordinates and a two-dimensional null space are essential to the calculated coefficients; no formula is claimed for larger matrices, alternative diagonal noise distributions, restarted Lanczos iterations, or floating-point effects. The result provides exact small-gap distribution and moment thresholds, but not an iteration-count estimate for a practical eigensolver. Independent mathematical validation and a comprehensive historical novelty review have not been performed.

## References

1. D. Kressner and N. Shao, *On a randomized small-block Lanczos method for large-scale null space computations*, arXiv:2407.04634, v1 July 5, 2024; Theorem 4 and Section 2.1. https://arxiv.org/abs/2407.04634
2. S. Kumar and Z. Ahmed, *New Spectral Statistics for Ensembles of \(2\times2\) Real Symmetric Random Matrices*, Acta Polytechnica **57** (2017), 418–423, DOI:10.14311/AP.2017.57.0418. https://doi.org/10.14311/AP.2017.57.0418

# Sharp finite-moment reconstruction of ellipsoid axes from unoriented central sections

## Finding
For every integer \(d\ge2\), the first \(d\) population moments of the **reciprocal squared volume** of a Haar-random central hyperplane section of a centered \(d\)-dimensional Euclidean ellipsoid determine all its semiaxes, up to permutation. No direction-to-section correspondence, additional volume measurement, or noncentral section is needed. The number \(d\) is optimal uniformly over ellipsoids: near **every** ellipsoid with pairwise distinct semiaxes, there are noncongruent ellipsoids with the same first \(d-1\) moments.

If the full \(d\)-dimensional volume is also known, exactly \(d-1\) reciprocal-square section moments suffice; \(d-2\) are again insufficient locally at every ellipsoid with distinct semiaxes. The recovery is given by extracting the roots of one explicit degree-\(d\) polynomial.

## Assumptions and scope
Let \(E=\{x\in\mathbb R^d:\sum_{i=1}^d x_i^2/a_i^2\le1\}\), where all \(a_i>0\). A rotation of \(E\) is immaterial. Put \(A=\operatorname{diag}(a_1,\ldots,a_d)\), \(P=\det A\), and let \(\kappa_j\) denote the volume of the unit ball in \(\mathbb R^j\). Let \(U\) be uniform on the Euclidean unit sphere and define the section volume and transformed measurement by
\[
S(U)=\operatorname{Vol}_{d-1}(E\cap U^\perp),\qquad X(U)=\left(\frac{\kappa_{d-1}}{S(U)}\right)^2.
\]
The available data are the exact population moments \(m_k=\mathbb E[X(U)^k]\), for \(1\le k\le d\), together with the known dimension. Thus these are negative even moments of section volume, normalized by \(\kappa_{d-1}\), rather than the ordinary positive area moments. The sample normal is Euclidean Haar-uniform, not affine-uniform or area-biased.

Define \(b_i=a_i^2/P^2\), and the rising factorial \((c)_k=c(c+1)\cdots(c+k-1)\), with \((c)_0=1\). For \(m_0=1\), form the truncated series
\[
G_d(z)=\sum_{k=0}^d\frac{(d/2)_k}{k!}m_kz^k.
\]
Then the coefficients through degree \(d\) of \(G_d(z)^{-2}\), interpreted as a formal series, are exactly those of
\[
H(z)=\prod_{i=1}^d(1-b_i z).
\]
The \(d\) positive roots of \(t^dH(1/t)\), counted with multiplicity, are \(b_1,\ldots,b_d\). The semiaxes are consequently
\[
a_i=\sqrt{b_i}\left(\prod_{j=1}^db_j\right)^{-1/(2(d-1))}.
\]
If \(\operatorname{Vol}_d(E)=\kappa_dP\) is known, then \(\prod_i b_i=P^{-2(d-1)}\) fixes the final coefficient of \(H\) in advance, so only \(m_1,\ldots,m_{d-1}\) are needed.

## Proof
**1. Section-volume identity.** The ellipsoid equals \(AB_d\). Under \(x=Ay\), its section by \(U^\perp\) becomes the unit-ball section with normal \(A^{\mathsf T}U\). Let \(n=A^{\mathsf T}U/\|A^{\mathsf T}U\|\) be the unit normal in the source. The \((d-1)\)-Jacobian of \(A\) restricted to \(n^\perp\) is
\[
|\det A|\,\|A^{-\mathsf T}n\|=P/\|A^{\mathsf T}U\|.
\]
Therefore \(S(U)=\kappa_{d-1}P/\sqrt{\sum_i a_i^2U_i^2}\), including in dimension \(2\), where sections are chord lengths. Consequently \(X(U)=\sum_i b_iU_i^2\).

**2. Moment identity.** Write \(U=Z/\|Z\|\) with independent standard Gaussian coordinates. Then \((U_1^2,\ldots,U_d^2)\) has the Dirichlet law with \(d\) parameters equal to \(1/2\). Its multinomial moments give, for every \(k\ge0\),
\[
\frac{(d/2)_k}{k!}m_k
=\sum_{\alpha_1+\cdots+\alpha_d=k}\prod_{i=1}^d
\frac{(1/2)_{\alpha_i}}{\alpha_i!}b_i^{\alpha_i}.
\]
Summing as formal power series and using the generalized binomial theorem yields
\[
G(z)=\sum_{k\ge0}\frac{(d/2)_k}{k!}m_kz^k
=\prod_{i=1}^d(1-b_i z)^{-1/2}.
\]
Hence \(G(z)^{-2}=H(z)\), a polynomial of degree exactly \(d\). Coefficients through degree \(d\) depend only on \(m_0,\ldots,m_d\), proving reconstruction. For explicit recurrence, write \(g_k=(d/2)_km_k/k!\) and \(c_j=\sum_{r=0}^jg_rg_{j-r}\). Set \(h_0=1\), and for \(1\le k\le d\) set
\[
h_k=-\sum_{j=1}^k c_jh_{k-j}.
\]
Then \(H(z)=\sum_{k=0}^dh_kz^k\). The formula for \(a_i\) follows from \(\prod_i b_i=P^{-2(d-1)}\).

**3. Optimal number of moments.** The mapping from the first \(r\) moments to the first \(r\) elementary symmetric functions of the positive numbers \(b_i\) is triangular with nonzero diagonal: the coefficient of \(m_k\) in the degree-\(k\) coefficient of \(G(z)^{-2}\) is \(-2(d/2)_k/k!\). Let \(b_1,\ldots,b_d\) be pairwise distinct and positive. Vary only the constant term of the monic polynomial \(\prod_i(t-b_i)\) by a sufficiently small nonzero real amount. Its simple positive roots persist continuously as distinct positive real roots. All elementary symmetric functions through order \(d-1\), hence the first \(d-1\) moments, remain fixed, but the root multiset changes. The resulting axes differ, so the ellipsoids are not congruent.

If volume is fixed, the final elementary symmetric function \(\prod_i b_i=P^{-2(d-1)}\) is fixed. Instead vary only the coefficient of \(t\) in \(\prod_i(t-b_i)\); the first \(d-2\) elementary symmetric functions and the final one are unchanged. The same simple-positive-root argument supplies distinct equal-volume ellipsoids with identical first \(d-2\) moments. This argument applies also when \(d=2\), for which zero moment observations and known volume plainly do not determine an ellipse. Optimality is asserted generically, not at repeated-axis bodies.

## Verification
The accompanying self-contained `verify.py` performs exact rational reconstruction in dimensions \(2,3,4,5\), checks a two-dimensional pair of different spectra having the same first moment, and independently computes three-dimensional section areas from the restricted quadratic form on the section plane rather than from the Jacobian formula. Run `python3 verify.py` with Python 3.10 or later; it prints `VERIFY_OK` on success. The infinite-dimensional quantifiers and local optimality statements are established by the preceding proof, not by finite computations.

## Relationship to prior work
Kim, Yaskin and Zvavitch (first public preprint 22 December 2015) defined distributions of unlabeled central section volumes and proved comparison results, including their ellipsoid volume comparison theorem; they also constructed nonellipsoidal counterexamples to general reconstruction from full section distributions. The present statement is specifically about the **exact optimal finite number of negative even section-volume moments** for recovering all axes within the ellipsoid class. Their comparison theorem does not supply this finite cutoff or its two local lower bounds. Hillier (2001) studied forward densities of random spherical quadratic forms; the present finite-data recovery uses the associated Dirichlet structure and an additional polynomial inversion/optimality argument. Møller (1988) studied an inverse problem using three parallel hyperplane sections, a different, direction-correlated observation model. None of these statements should be interpreted as providing uniqueness for arbitrary nonellipsoidal convex bodies.

## Limitations
Results concern ideal population moments, not a finite random sample or statistically stable estimation. Axis recovery is up to orthogonal congruence; the absolute orientation cannot be determined from Haar-unoriented section volumes. The generic lower bounds do not exclude faster identification for special repeated-axis families. Root reconstruction may be ill-conditioned near multiple axes. Published work on spherical quadratic-form distributions may contain historically related formulas; no claim of full historical exhaustiveness or independent audit is made. The construction is not a general solution to distributional geometric tomography outside ellipsoids.

## References
1. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289 (first posted 22 December 2015), later *J. London Math. Soc.* **95** (2017), 52–72. https://arxiv.org/abs/1512.07289
2. G. Hillier, *The density of a quadratic form in a vector uniformly distributed on the n-sphere*, *Econometric Theory* **17** (2001), 1–28. https://doi.org/10.1017/S026646660117101X
3. J. Møller, *Stereological analysis of particles of varying ellipsoidal shape*, *Journal of Applied Probability* (1988). https://doi.org/10.2307/3214440
4. M. Arelio and L. Montejano, *Convex bodies with many elliptic sections*, arXiv:1408.5647 (2014). https://arxiv.org/abs/1408.5647

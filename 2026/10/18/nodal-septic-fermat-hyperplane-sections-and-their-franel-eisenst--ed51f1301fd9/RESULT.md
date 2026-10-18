# Nodal septic Fermat hyperplane sections and their Franel–Eisenstein arithmetic

## Finding

For every integer \(N\geq5\), define the projective hypersurface \(X_N\subset\mathbb P^{N-2}_{\mathbb Q}\) by the equations
\[
\sum_{i=1}^{N}x_i=0,\qquad \sum_{i=1}^{N}x_i^7=0
\]
in \(\mathbb P^{N-1}_{\mathbb Q}\). It is geometrically integral and normal. All its geometric singular points are ordinary double points, with the exact number
\[
\boxed{\nu_N=\frac16\sum_{k=0}^{N}\binom Nk(-2)^{N-k}\sum_{j=0}^{k}\binom kj^3.}
\]
The first values, in order \(N=5,6,7,8,9,10\), are \(60,340,1680,9135,48440,264726\).

More precisely, put \(F_k=\sum_{j=0}^{k}\binom kj^3\), the order-three Franel numbers. Then \(6\nu_N\) is the number of length-\(N\) closed walks on the triangular (Eisenstein) lattice with six unit directions, and is the binomial transform \(\sum_k\binom Nk(-2)^{N-k}F_k\).

The entire **reduced singular scheme over \(\mathbb Q\)** has the explicit arithmetic decomposition
\[
\operatorname{Sing}(X_N)_{\mathrm{red}}\simeq
\coprod_{i=1}^{\rho_N}\operatorname{Spec}\mathbb Q
\;\sqcup\;
\coprod_{i=1}^{(\nu_N-\rho_N)/2}\operatorname{Spec}\mathbb Q(\sqrt{-3}),
\qquad
\rho_N=\begin{cases}\frac12\binom{N}{N/2},&N\ \mathrm{even},\\0,&N\ \mathrm{odd}.\end{cases}
\]
In particular, at \(N=5\) there are 30 quadratic closed singular points and no rational ones; at \(N=6\) there are 10 rational and 165 quadratic closed singular points.

## Assumptions and scope

All geometry is over characteristic zero; ordinary double point means a hypersurface germ with a nondegenerate quadratic leading term over an algebraic closure. The hypersurface has dimension \(N-3\). The order-three Franel number \(F_k\) is defined by the displayed finite binomial sum. No assertion is made in positive characteristic. The count \(\nu_N\) counts geometric points, not closed points over \(\mathbb Q\). The arithmetic decomposition is only for the reduced singular scheme.

## Proof

**Step 1: Determine every geometric singular point.** Over an algebraically closed characteristic-zero field, the Jacobian criterion for the complete intersection in \(\mathbb P^{N-1}\) gives a singular point precisely when the gradient of the seventh-power equation is proportional to the gradient of the linear equation. Thus there is \(c\) with \(7x_i^6=c\) for all \(i\). Necessarily \(c\ne0\), since otherwise every coordinate is zero. After rescaling the projective representative, \(x_i^6=1\) for every \(i\); in this normalization the seventh-power sum equals the ordinary sum. Writing \(\mu_6\) for the sixth roots of unity, we obtain the exact parametrization
\[
\operatorname{Sing}(X_N)(\overline{\mathbb Q})
=\{(\xi_1,\ldots,\xi_N)\in\mu_6^N:\sum_i\xi_i=0\}/\mu_6,
\]
where the final \(\mu_6\) acts by common scalar multiplication. This action is free on nonzero ordered tuples, so the geometric point count is the ordered zero-sum count divided by six.

**Step 2: All singularities are ordinary double points.** Normalize \(x_N=1\). On the affine chart of the linear hyperplane, take coordinates \(y_i=x_i\) for \(1\le i\le N-2\), eliminate \(x_{N-1}=-1-\sum_{i=1}^{N-2}y_i\), and write
\[
G(y)=\sum_{i=1}^{N-2}y_i^7+\left(-1-\sum_{i=1}^{N-2}y_i\right)^7+1.
\]
At a singular point, the Hessian of \(G\) is
\[
42\left(\operatorname{diag}(x_1^5,\ldots,x_{N-2}^5)+x_{N-1}^5\mathbf1\mathbf1^{\mathsf T}\right).
\]
Since \(x_i^6=1\), the matrix determinant lemma and \(\sum_i x_i=0\) give
\[
\det(\operatorname{Hess}G)
=-\frac{42^{N-2}}{\prod_{i=1}^{N-1}x_i}\ne0.
\]
The local quadratic term is therefore nondegenerate, so every geometric singularity is an ordinary double point. In particular, the singular scheme is geometrically reduced and zero-dimensional; there are no other singularities.

**Step 3: Geometric integrality and normality.** For \(N\ge5\), the ambient space of the degree-seven hypersurface is \(\mathbb P^{N-2}\), of dimension at least three. If its equation had two positive-degree factors, their projective zero sets would intersect in dimension at least \(N-4\ge1\), giving a positive-dimensional subset of the singular locus, contrary to Step 2. Repeated factors likewise force a positive-dimensional singular locus. Thus the equation is absolutely irreducible. A hypersurface is Cohen–Macaulay (Serre \(S_2\)); isolated singularities on a hypersurface of dimension at least two give regularity in codimension one (\(R_1\)). Serre's criterion implies normality.

**Step 4: Count all nodes by an Eisenstein lattice constant term.** Write a primitive sixth root \(\zeta\) satisfying \(\zeta^2=\zeta-1\). The six complex sixth roots correspond to the six unit vectors of the Eisenstein lattice \(\mathbb Z[\zeta]\). After an integral unimodular change of lattice coordinates, the six steps are recorded by
\[
S(U,V)=U+U^{-1}+V+V^{-1}+UV+(UV)^{-1}.
\]
The number of ordered zero-sum \(N\)-tuples is exactly \(\operatorname{CT}_{U,V}S(U,V)^N\), the coefficient of \(U^0V^0\). Crucially,
\[
S(U,V)+2=(1+U)(1+V)(1+U^{-1}V^{-1}).
\]
Expand the right side to power \(k\). Its constant term requires the same binomial index in each factor, hence
\[
\operatorname{CT}_{U,V}(S+2)^k
=\sum_{j=0}^k\binom kj^3=F_k.
\]
Expanding \(S^N=((S+2)-2)^N\) and dividing by the six choices of projective representative proves the boxed formula for \(\nu_N\).

**Step 5: Rational and quadratic residue fields.** Normalize every singular projective point by \(x_N=1\). Its coordinates now lie in \(\mu_6\subset\mathbb Q(\zeta)=\mathbb Q(\sqrt{-3})\). The point is rational over \(\mathbb Q\) if and only if all normalized coordinates lie in \(\mu_6\cap\mathbb Q=\{1,-1\}\). A zero sum of \(N\) signs exists only for even \(N\), with \(N/2\) plus signs and \(N/2\) minus signs, and complementary sign assignments represent the same projective point. Hence their number is \(\rho_N\). Every other singular point has residue field exactly the indicated quadratic field, and complex conjugation interchanges the remaining geometric singular points in pairs. Nondegeneracy of the Hessian (Step 2) ensures that this describes the full reduced singular subscheme rather than merely its set of closed points.

## Verification

Run \(\texttt{python3 check\_septic.py}\), requiring only the Python standard library. The script performs independent dynamic programming on the six-direction Eisenstein lattice for \(3\le N\le12\), compares its return-walk totals with the Franel-binomial formula, independently enumerates multinomial root histograms for \(3\le N\le7\), compares rational and quadratic splitting counts, and checks exact normalized Hessian determinants at sample nodes for \(5\le N\le7\). Its successful exit prints \(\texttt{VERIFY\_OK}\). These are finite checks; Steps 1–5 give the proof for all integers \(N\ge5\).

## Relationship to prior work

Lam and Leung [1] classify **which lengths** admit vanishing sums of roots of unity. Their length-spectrum theorem is compatible with Step 1, but it does not count ordered zero sums or establish the singular-scheme geometry of the seventh-power hyperplane family. Looijenga [2] develops the cohomology and period theory of Fermat varieties, rather than this singular hyperplane-section node census. Chen and Xia [3] study the pre-existing Franel numbers as combinatorial sequences; no originality is claimed for those numbers themselves. The earlier cubic linear-section geometry (the Segre cubic) exhibits ten nodes for six coordinates, but it does not imply the sixth-root-of-unity Franel transform or the arithmetic splitting established here. This contribution is the combined all-dimensional geometric, enumerative, and arithmetic classification, not the elementary Jacobian criterion or the separate pre-existing combinatorial objects.

## Limitations

The theorem applies only in characteristic zero and to the specifically displayed symmetric septic family, not to arbitrary Fermat hyperplane sections or general degree-seven hypersurfaces. The node counts are not claimed extremal among degree-seven hypersurfaces, and no characteristic-\(p\) classification is asserted. Possible equivalent presentations under the language of diagonal hyperplane sections or root-of-unity configurations remain an originality risk. Computational checks cover finite ranges only and are not substitutes for the proof.

## References

1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1 (1995-11-13), https://arxiv.org/abs/math/9511209.
2. Eduard Looijenga, *Fermat varieties and the periods of some hypersurfaces*, arXiv:1005.1733v1 (2010-05-11), https://arxiv.org/abs/1005.1733.
3. William Y. C. Chen and Ernest X. W. Xia, *The 2-log-convexity of the Apéry Numbers*, arXiv:0912.0795v1 (2009-12-04), https://arxiv.org/abs/0912.0795.

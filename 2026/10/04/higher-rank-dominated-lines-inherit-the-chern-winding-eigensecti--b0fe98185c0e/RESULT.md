# Higher-rank dominated lines inherit the Chern–winding eigensection criterion
## Finding
Let \(n\ge 3\), let \(S(w)=w+\tau\) be a Diophantine translation of \(\mathbb T^2\), and let \( (U_1,U_2,A)\) be strip-admissible analytic \(U(n)\)-sewn, \(GL(n,\mathbb C)\)-valued cocycle data. Suppose the bundle has a continuous invariant splitting
\[
V=L\oplus H,\qquad \dim_{\mathbb C}L=1,
\]
which is dominated in one of the two orders: either \(L\) is dominated by \(H\), or \(H\) is dominated by \(L\).

Then \(L\) carries a nonzero measurable eigensection if and only if
\[
c_1(L)=0\qquad\text{and}\qquad k(L)=0,
\]
where \(k(L)\in\mathbb Z^2\) is the winding vector of the normalized periodic multiplier phase in the charge gauge. When both invariants vanish, the eigenvalues carried by \(L\) are exactly
\[
\Lambda_L=\lambda_0\left\{e^{{-2\pi i\nu\cdot\tau}}:\nu\in\mathbb Z^2\right\},
\]
a dense coset on the circle \( |\lambda|=e^{{\lambda_L}}\). Each carried eigenspace is one-dimensional, and every measurable eigensection carried by \(L\) agrees almost everywhere with a real-analytic nowhere-vanishing eigensection.

This removes the rank-two restriction from the exact line-resolved criterion whenever the chosen invariant line is an extremal one-dimensional block of a two-block dominated splitting.

## Assumptions and scope
Strip-admissibility means that the sewing maps and cocycle matrix extend holomorphically and boundedly to a fixed complex tube around \(\mathbb R^2\), are unitary on the real slice for the sewing maps, are invertible on the real slice for the cocycle, and satisfy the sewing and equivariance identities. The Diophantine hypothesis is the usual lower bound
\[
\|\nu\cdot\tau\|_{{\mathbb R/\mathbb Z}}\ge c|\nu|_1^{{-\eta}}
\]
for all nonzero \(\nu\in\mathbb Z^2\), for some \(c>0\) and finite \(\eta\).

For the forward order \(L\prec H\), domination means that for some block length \(N\) and \(0<\kappa<1\),
\[
\frac{{\|A^{{(N)}}(w)|_{{L(w)}}\|}}{{\mathfrak m(A^{{(N)}}(w)|_{{H(w)}})}}\le \kappa
\]
for every real base point. The reverse order is reduced to this one by the inverse cocycle over translation by \(-\tau\), which is Diophantine with the same constants.

The conclusion is line-resolved. It does not assert that every measurable eigensection of a higher-rank cocycle is carried by \(L\), nor that the complementary block \(H\) splits further into invariant lines.

## Proof
Assume first that \(L\prec H\). Replace the domination block by a sufficiently large iterate so that its ratio is as small as required below.

**1. The lifted dominated line is uniformly continuous.** Put \(M_r(w)=A^{{(rN)}}(w)\),
\[
a_r(w)=\|M_r(w)|_{{L(w)}}\|,
\qquad
b_r(w)=\mathfrak m(M_r(w)|_{{H(w)}}).
\]
Then \(a_r/b_r\le\kappa^r\). By the min-max characterization of singular values,
\[
\sigma_{{n-1}}(M_r(w))\ge b_r(w),\qquad
\sigma_n(M_r(w))\le a_r(w),
\]
so \(\sigma_n/\sigma_{{n-1}}\le\kappa^r\). Hence the least right-singular line \(v_r(w)\) is uniquely defined for large \(r\). If \(\ell\) is a unit vector in \(L(w)\), its component orthogonal to \(v_r(w)\) has norm at most
\[
\frac{{\|M_r(w)\ell\|}}{{\sigma_{{n-1}}(M_r(w))}}\le\frac{{a_r(w)}}{{b_r(w)}}\le\kappa^r.
\]
Thus \(v_r\to L\) uniformly on the real lift. For each fixed \(r\), strip holomorphy and the unitary sewing give uniform real-slice Lipschitz bounds for \(M_r\); the spectral projection of \(M_r^*M_r\) onto its simple least eigenvalue is therefore uniformly continuous. Hence \(v_r\) is uniformly continuous, and its uniform limit \(L\) is uniformly continuous on \(\mathbb R^2\).

**2. Domination gives a holomorphic extension of the line in every rank.** Fix a large block \(M=A^{{(rN)}}\). At a real point, relative to the invariant splitting at source and target, \(M\) is block diagonal. In the affine chart of projective space consisting of graphs from the line \(L\) into \(H\), the backward projective graph transform has linear slope bound
\[
\|M|_L\|\,\|(M|_H)^{{-1}}\|
=\frac{{\|M|_L\|}}{{\mathfrak m(M|_H)}}\le\kappa^r.
\]
The angle between \(L\) and \(H\) is uniformly bounded away from zero on the compact base. Because \(M(w)\) is uniformly close to \(M(\operatorname{Re}w)\) on a sufficiently thin strip, the same fractional-linear graph transform maps a fixed graph ball into itself and is a strict contraction there, uniformly in \(w\). Banach's fixed-point theorem gives a continuous invariant line on the strip extending the real line field.

To prove holomorphy, fix a complex neighborhood of \(w_0\). For every nonnegative integer \(j\), take the constant line
\[
c_j=L(\operatorname{Re}(S^{{jrN}}w_0)).
\]
Uniform continuity of the lifted line makes every \(c_j\) lie in the appropriate graph ball for all points in a sufficiently small neighborhood of \(w_0\), uniformly in \(j\). The maps
\[
\psi_j(w)=A^{{(jrN)}}(w)^{{-1}}c_j
\]
are holomorphic maps into \(\mathbb{CP}^{{n-1}}\), and uniform graph contraction makes \(\psi_j\) converge uniformly to the fixed line. All values lie in one affine chart after shrinking the neighborhood. Weierstrass convergence therefore makes the fixed line holomorphic. Uniqueness of the fixed graph and the sewing identities give the required sewing equivariance. This is the higher-rank version of the rank-two strip-extension step; the proof uses only a one-dimensional dominated block and not a one-dimensional complement.

**3. The analytic charge gauge is dimension-free.** Pull back the tautological line bundle over \(\mathbb{CP}^{{n-1}}\) by the holomorphic line map. The complex tube is contractible and Stein, so the pullback line is holomorphically trivial there. On the quotient strip torus, the same factor-system argument as for the rank-two line produces a real-analytic normalized unit section with automorphy charge equal to \(c_1(L)[\mathbb T^2]\). Nothing in this step depends on the ambient rank; only the tautological **line** is used.

**4. The two scalar cohomological equations are analytic.** In that normalized gauge the invariant multiplier \(q\) is real analytic and zero free. Therefore \(\log|q|\) and the zero-winding part \(g\) of the normalized periodic phase are real analytic. The Diophantine Fourier estimate solves
\[
v-v\circ S=h-\langle h\rangle
\]
real-analytically for \(h=\log|q|\) and for \(h=g\).

**5. Apply the line-resolved obstruction and rederive the exact carried spectrum.** The source's Chern obstruction, charge-zero winding obstruction, and abstract existence theorem are formulated for an invariant line in arbitrary ambient rank. Steps 1--4 supply the analytic cohomology hypotheses that the source proves automatically only in rank two. Thus \(c_1(L)\ne0\) excludes carried eigensections; when \(c_1(L)=0\) but \(k(L)\ne0\), winding excludes them; and when both vanish, the analytic scalar equations construct a nowhere-zero analytic eigensection \(F_0\) with eigenvalue \(\lambda_0\).

For completeness, the exact coset and simplicity are derived directly rather than imported from the source's rank-two classification theorem. If \(F\) is any other nonzero measurable eigensection carried by the same line, write \(F=rF_0\). Then
\[
r\circ S=(\lambda/\lambda_0)r.
\]
Poincaré recurrence on a positive-measure level band of \(|r|\) forces \(|\lambda|=|\lambda_0|\); hence \(|r|\) is invariant and therefore constant almost everywhere by ergodicity. After normalization, \(r/|r|\) is an \(L^2\) eigenfunction of the torus translation. Its Fourier coefficients satisfy the translation eigenvalue equation, so irrationality of the Diophantine translation leaves exactly one character \(e^{{2\pi i\nu\cdot w}}\). Consequently
\[
\lambda=\lambda_0 e^{{-2\pi i\nu\cdot\tau}},\qquad \nu\in\mathbb Z^2,
\]
and each carried eigenspace is one-dimensional. Multiplying \(F_0\) by a character also shows that every element of this coset is realized by a real-analytic nowhere-vanishing eigensection.

If instead \(H\prec L\), apply the previous argument to the inverse cocycle over \(-\tau\). The same line \(L\) becomes the dominated one-dimensional block; the inverse-data normalization transfers back to the forward multiplier exactly as in the rank-two inverse argument. This proves the stated two-sided version.

## Verification
The proof was checked at the level of the critical implications. The min-max inequalities give the required smallest-singular-value gap without an experiment. The graph transform is performed in \(\operatorname{{Hom}}(L,H)\) coordinates, where the real backward slope multiplier is exactly bounded by the domination ratio; sufficiently small complex perturbations preserve a uniform contraction. Uniform convergence of fixed-center holomorphic projective iterates supplies holomorphy without treating singular-vector fields as holomorphic. The Stein normalization uses only a holomorphic line bundle, so replacing \(\mathbb{CP}^1\) by \(\mathbb{CP}^{{n-1}}\) changes no cohomological step. The source's arbitrary-rank line-resolved obstruction and existence theorems supply necessity and existence after the analytic hypotheses are discharged; the exact eigenvalue coset and one-dimensional carried eigenspaces are then rederived from the ratio of two sections using recurrence, ergodicity, and Fourier characters of the torus translation.

No finite computation is used, and no statement is made about point spectrum supported in \(H\) or about measurable invariant directions not equal to \(L\).

## Relationship to prior work
Azimifard proves the Chern obstruction in arbitrary rank under a measurable phase-coboundary hypothesis, but proves automatic analytic discharge and the exact Chern–winding criterion only in rank two. The paper explicitly states that no higher-rank analogue is asserted and lists rank \(n>2\) outside its proved scope. Its strip-extension and Stein-normalization sections identify precisely the step where rank two was imposed.

Bochi and Gourmelon prove in arbitrary dimension that domination is equivalent to a uniform exponential singular-value gap and develop the projective-hyperbolic viewpoint. Their theorem supplies background for the higher-rank graph transform, but does not discuss sewn analytic torus bundles, Chern classes, multiplier winding, or measurable eigensections.

Duarte and Klein construct topological obstructions to the **existence** of dominated splittings for analytic quasi-periodic cocycles on higher-dimensional tori. Their conclusion is about homotopy classes and domination, not about eigensections carried by a dominated line. Thus it neither implies nor contradicts the present line-resolved criterion.

Targeted searches for the conjunction of higher-rank domination, Chern class, multiplier winding, and measurable eigensections did not locate an equivalent or stronger statement. A residual risk remains that the analytic higher-rank graph-transform extension is known as folklore or follows from a general analytic invariant-bundle theorem not indexed in this terminology; such a result would cover the regularity lemma, but the searched sources did not combine it with the exact Chern–winding eigensection criterion.

## Limitations
The theorem requires a one-dimensional **extremal dominated block**. It does not treat a line embedded inside a higher-dimensional center block, equal-exponent regimes, nonuniform domination, noninvertible cocycles, Liouville translations, or arbitrary measurable invariant lines. It does not classify eigensections carried by the complementary block \(H\). The Diophantine hypothesis remains essential for the sufficiency direction because the modulus cohomological equation can fail over Liouville translations even when the topological invariants vanish.

The originality comparison cannot exclude unindexed folklore about analytic regularity of dominated line bundles. The scientific novelty claimed here is therefore the explicit arbitrary-rank discharge for an extremal one-dimensional dominated block and the resulting exact carried-eigensection criterion, not a general new theory of dominated splittings.

## References
1. Ahmadreza Azimifard, *A Chern-Class Obstruction to Measurable Eigensections of Analytic Quasi-Periodic Bundle Cocycles*, arXiv:2609.29577v1, 2026.
2. Jairo Bochi and Nicolas Gourmelon, *Some Characterizations of Domination*, arXiv:0808.3811v2; Math. Z. 263 (2009), 221–231.
3. Pedro Duarte and Silvius Klein, *Topological obstructions to dominated splitting for ergodic translations on the higher dimensional torus*, arXiv:1704.03036v1; Discrete Contin. Dyn. Syst. 38 (2018), 5379–5387.

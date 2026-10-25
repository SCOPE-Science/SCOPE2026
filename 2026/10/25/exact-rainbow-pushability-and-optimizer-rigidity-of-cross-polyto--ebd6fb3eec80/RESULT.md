# Exact rainbow pushability and optimizer rigidity of cross-polytopes

## Finding

For integers \(d\ge2\) and \(r\ge1\), let
\[
P_d=\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}\subset\mathbb R^d.
\]
The rainbow pushability \(\pi_r(P_d)\) is the maximum probability that \(r\) independent random vertices lie in one facet, when their expectations sum to zero. Then
\[
\boxed{\pi_r(P_d)=\min\{1,2^{d-r}\}.}
\]
For \(r\ge d\), a maximizing family of laws is characterized *if and only if* by the following two conditions: each law assigns equal probabilities to \(+e_j\) and \(-e_j\) for every \(j\), and for each \(j\) some law is supported entirely on the antipodal pair \(\{+e_j,-e_j\}\). In particular, when \(r=d\), the optimizing laws are, up to permutation, exactly the fair antipodal laws on the \(d\) separate axes. The smallest \(r\) for which \(\pi_r(P_d)<1\) is \(d+1\).

## Assumptions and scope

All variables are independent and take values in \(V(P_d)=\{\pm e_1,\ldots,\pm e_d\}\), with possibly different distributions. They satisfy the *collective* balance constraint
\[
\sum_{i=1}^{r}\mathbb E X_i=0.
\]
No assumption of individual mean zero is made in the definition: this property will follow for optimizers in the nontrivial regime. A common facet is any of the \(2^d\) facets
\[
F_\sigma=\operatorname{conv}\{\sigma_1e_1,\ldots,\sigma_de_d\},\qquad \sigma\in\{\pm1\}^d.
\]

## Proof

**Upper bound.** Write \(a_{ij}^{+}=\Pr(X_i=e_j)\) and \(a_{ij}^{-}=\Pr(X_i=-e_j)\). For a fixed facet \(F_\sigma\), let
\[
q_{i,\sigma}=\Pr(X_i\in F_\sigma)=\sum_{j=1}^{d}a_{ij}^{\sigma_j}.
\]
Since each vertex lies in exactly one of \(F_\sigma,F_{-\sigma}\), and the row masses sum to one,
\[
q_{i,\sigma}=\tfrac12\left(1+\sum_{j=1}^{d}\sigma_j(a_{ij}^{+}-a_{ij}^{-})\right).
\]
Collective balance gives \(\sum_i(a_{ij}^{+}-a_{ij}^{-})=0\) separately for each \(j\), whence
\[
\sum_{i=1}^{r}q_{i,\sigma}=r/2.
\]
Independence and arithmetic-geometric mean imply
\[
\Pr(X_1,\ldots,X_r\in F_\sigma)=\prod_iq_{i,\sigma}\le2^{-r}.
\]
Taking the union over the \(2^d\) facets, and also using the trivial upper bound one, yields \(\pi_r(P_d)\le\min\{1,2^{d-r}\}\).

**Sharp constructions.** If \(r\le d\), choose independent fair signs on \(r\) *distinct* coordinate axes. Every realization uses distinct axes, so its observed signs extend to some \(\sigma\), meaning all chosen vertices lie in \(F_\sigma\), with probability one.

If \(r\ge d\), take one independent fair antipodal vertex on *each* axis \(1,\ldots,d\); assign to any additional variables arbitrary independent antipodally symmetric vertex laws. Every law has zero expectation. After the first \(d\) draws, exactly one facet \(F_\sigma\) contains them. Every additional antipodally symmetric law assigns probability exactly \(1/2\) to that fixed facet, independently of previous draws. Therefore the common-facet probability is \(2^{-(r-d)}=2^{d-r}\), proving the formula.

**Necessity and sufficiency of the maximizing structure when \(r\ge d\).** Equality in the formula requires equality both in the facet union bound and in the arithmetic-geometric mean bound for **each** of the \(2^d\) facets, because the sum of the latter upper bounds equals the achieved probability. Thus \(q_{i,\sigma}=1/2\) for every \(i,\sigma\). Comparing \(\sigma\) with the sign vector obtained by flipping only coordinate \(j\), we get \(a_{ij}^{+}=a_{ij}^{-}\) for all \(i,j\). Therefore every individual vertex distribution is antipodally symmetric.

With this symmetry, condition on the random axis choices \(J_i\), where \(X_i\in\{\pm e_{J_i}\}\). Given these axes, the signs are independent and fair. If \(K\) distinct axes occur, then the probability of sign consistency on every repeated axis is \(2^{K-r}\). A consistent outcome is in exactly \(2^{d-K}\) different facets. It follows that the conditional union probability is \(2^{K-r}\), so
\[
\Pr(\exists\sigma:\ X_1,\ldots,X_r\in F_\sigma)=\mathbb E\,2^{K-r}\le2^{d-r},
\]
with equality precisely when \(K=d\) almost surely.

The axis selections are independent and take finitely many values. For a fixed \(j\), every positive-probability axis tuple contains \(j\) if and only if at least one row chooses \(j\) with probability one: in the absence of such a row, each row has a positive-probability axis choice other than \(j\), and independence yields a positive-probability tuple missing \(j\). Thus \(K=d\) almost surely if and only if every coordinate axis has an axis-exclusive row. This proves both necessity and sufficiency, and the \(r=d\) characterization follows because \(d\) distinct axes require \(d\) distinct exclusive rows.

## Verification

The independent exact-rational script `verify_crosspolytope.py` enumerates all supported signed-axis outcomes for 21 distinct \((d,r)\) construction cases with \(2\le d\le5\), including additional *nonuniform* antipodally symmetric rows, and checks collective balance plus the displayed formula. It also tests one balanced but nonoptimal family that lacks a mandatory axis. All tests passed. The arbitrary-dimensional theorem and equality classification are proved analytically above; numerical or finite enumeration is not used to infer them.

## Relationship to prior work

Martínez-Sandoval and Olvera-Sampieri (2026) introduce rainbow pushability and prove a general centrally symmetric facet-depth bound \(\pi_r(P)\le\min\{1,f_{d-1}(P)/2^r\}\). The upper bound here is its specialization since \(P_d\) has \(2^d\) facets. Their exact cubical calculation is instead \(\pi_r([-1,1]^d)=\min\{1,d/2^{r-1}\}\). The new content is the **matching lower bound in the polar-dual cross-polytope** and the complete equality classification; neither follows from the one-sided generic estimate or from the distinct cube calculation. Their Section 7 explicitly poses exact evaluation for additional centered polytopes and sharpness of the facet bound as open directions.

## Limitations

The equality classification is asserted only for \(r\ge d\); for \(r<d\) the argument gives the exact value and examples, but not every maximizing distribution. No extension to all centrally symmetric polytopes is claimed. The comparison with indexed literature does not exclude earlier equivalent calculations in unindexed sources. An independent scientific audit has not been performed.

## References

Martínez-Sandoval, L., and Olvera-Sampieri, A., *Pushed colorful polytopal KKMS Theorem and orthogonal star transversals*, arXiv:2610.17157 (first public version October 12, 2026), especially Definition 3.1, Sections 4.1–4.2, and Section 7. https://arxiv.org/abs/2610.17157

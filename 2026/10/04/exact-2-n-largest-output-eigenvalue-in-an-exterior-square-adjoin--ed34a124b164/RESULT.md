# Exact \(2/n\) largest-output eigenvalue in an exterior-square adjoint channel family
## Finding
Let \(V=\mathbb C^n\) with \(n\ge5\), let \(W=\wedge^2V\), and let \(V_\lambda=\wedge^{n-2}V\), so \(\lambda=(1^{n-2},0,0)\). In the multiplicity-one Pieri summand
\[
V_\mu\subset \wedge^{n-2}V\otimes\wedge^2V,\qquad \mu=(2,1^{n-2},0),
\]
consider the two complementary channels obtained from the isometric inclusion of \(V_\mu\) by tracing out either tensor factor. For either channel,
\[
\max_\rho \lambda_\max\!\left(\Phi(\rho)\right)=\frac2n.
\]
A coherent highest-weight input has largest output eigenvalue \(1/(n-2)\). Hence coherent-state majorization fails throughout this natural family, with exact largest-eigenvalue gap
\[
\frac2n-\frac1{n-2}=\frac{n-4}{n(n-2)}>0.
\]
For \(n\ge5\), every pure maximizer is, up to phase and the natural \(U(n)\)-action, the vector corresponding to
\[
X=P-\frac2n I,
\]
where \(P\) is a rank-two orthogonal projection. In particular, for \(n=5\) the noncoherent value \(2/5\) exhibited in arXiv:2609.33498v1 is not merely a counterexample to coherent optimality: it is the global optimum.

## Assumptions and scope
All spaces carry their standard \(U(n)\)-invariant Hilbert structures, and \(\wedge^kV\) is normalized so that wedges of orthonormal basis vectors are orthonormal. The claim concerns the largest output eigenvalue only; it does not assert a full output-majorization order or determine the minimum von Neumann entropy for these exterior-square channels. The maximum over mixed inputs equals the maximum over pure inputs because \(\rho\mapsto\lambda_\max(\Phi(\rho))\) is convex.

Hodge duality gives a unitary identification
\[
\wedge^{n-2}V\cong (\wedge^2V)^*\otimes\det V.
\]
After removing the harmless determinant twist, the summand \(V_\mu\) is the adjoint representation inside \(\operatorname{End}(\wedge^2V)\). Thus a vector in this summand is represented by
\[
L(X)(u\wedge v)=Xu\wedge v+u\wedge Xv,\qquad X\in\mathfrak{sl}_n.
\]
Schmidt coefficients of the bipartite vector are the singular values of \(L(X)\), after Frobenius normalization.

## Proof
First, for every traceless \(X\),
\[
\|L(X)\|_{\mathrm{HS}}^2=(n-2)\|X\|_{\mathrm{HS}}^2.
\]
For diagonal traceless \(X=\operatorname{diag}(x_1,\ldots,x_n)\), this is
\[
\sum_{i<j}|x_i+x_j|^2=(n-2)\sum_i|x_i|^2.
\]
For an off-diagonal matrix unit \(E_{pq}\), the induced map moves exactly \(n-2\) orthonormal wedge-basis vectors isometrically. By unitary equivariance, these identities give the displayed Hilbert--Schmidt scaling on all of \(\mathfrak{sl}_n\).

Let \(S=L(\mathfrak{sl}_n)\subset\operatorname{End}(\wedge^2V)\). For any subspace of a bipartite Hilbert space, the maximum squared Schmidt coefficient of unit vectors in the subspace equals the maximum squared norm of the orthogonal projection of a unit product vector onto that subspace. A unit product vector in \((\wedge^2V)^*\otimes\wedge^2V\) is a rank-one operator \(|a\rangle\langle b|\) with unit two-forms \(a,b\). From \(L^*L=(n-2)I\),
\[
\|P_S(|a\rangle\langle b|)\|_{\mathrm{HS}}^2
=\frac1{n-2}\|\Gamma_0(a,b)\|_{\mathrm{HS}}^2,
\]
where \(\Gamma_0\) is the traceless part of the one-body transition matrix.

Write \(a,b\) as skew matrices \(A,B\) with \(\|A\|_{\mathrm{HS}}^2=\|B\|_{\mathrm{HS}}^2=2\). Up to adjoint, which does not affect Frobenius norm, the transition matrix is
\[
\Gamma=BA^*,\qquad \operatorname{Tr}\Gamma=2c,\qquad c=\langle a,b\rangle.
\]
The key estimate is
\[
\|BA^*\|_{\mathrm{HS}}^2\le1+|c|^2.
\]
To prove it, put \(A\) by unitary congruence into skew-normal form with blocks \(\alpha_rJ\), where \(\alpha_r\ge0\), \(\sum_r\alpha_r^2=1\), and \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\). Let \(u_r\) be the coefficient of \(B\) on the matching block pair. Every nonmatching matrix entry has weight at most one in \(\|BA^*\|_{\mathrm{HS}}^2\), so
\[
\|BA^*\|_{\mathrm{HS}}^2
\le1+\sum_r(2\alpha_r^2-1)|u_r|^2.
\]
Since \(c=\sum_r\alpha_ru_r\),
\[
|c|^2-\sum_r(2\alpha_r^2-1)|u_r|^2
=\sum_{r<s}|\alpha_su_r+\alpha_ru_s|^2\ge0,
\]
which proves the estimate.

Therefore
\[
\|\Gamma_0\|_{\mathrm{HS}}^2
=\|\Gamma\|_{\mathrm{HS}}^2-\frac{|\operatorname{Tr}\Gamma|^2}{n}
\le1+\left(1-\frac4n\right)|c|^2
\le2-\frac4n.
\]
It follows that every squared Schmidt coefficient is at most
\[
\frac1{n-2}\left(2-\frac4n\right)=\frac2n.
\]
Equality is attained by taking \(a=b=u\wedge v\) to be a Slater two-form. Then \(\Gamma=P\) is the rank-two projection onto \(\operatorname{span}\{u,v\}\), and \(\Gamma_0=P-(2/n)I\). The projected vector is therefore the adjoint direction \(L(P-(2/n)I)\), proving sharpness.

When \(n>4\), equality in the final bound forces \(|c|=1\), hence \(b\) is a phase multiple of \(a\). Equality in the transition estimate then forces the skew-normal form of \(a\) to have a single nonzero block, so \(a\) is Slater. This gives the stated maximizer classification.

Finally, a coherent highest-weight vector of the adjoint summand corresponds to \(X=E_{1n}\). The map \(L(E_{1n})\) is a rank-\((n-2)\) partial isometry: it maps \(e_n\wedge e_j\) to \(e_1\wedge e_j\) for \(2\le j\le n-1\). Hence its normalized nonzero squared singular values are all \(1/(n-2)\), establishing the coherent value and the strict gap.

## Verification
The proof is analytic and covers every integer \(n\ge5\). The bundled `artifacts/verify.py` performs exact-rational checks for \(5\le n\le12\): it verifies the Hilbert--Schmidt scaling on the sharp diagonal family, the ratio \(2/n\), the coherent partial-isometry ratio \(1/(n-2)\), the positive gap, the Slater transition-matrix projection norm, and representative exact instances of the sum-of-squares identity used in the transition estimate. It prints `VERIFY_OK` on success. These finite checks corroborate the formulas but are not used as an infinite proof.

## Relationship to prior work
Reuvers, arXiv:2609.33498v1, proves coherent-state majorization for the channels obtained when the tensor factor is the defining representation, then asks what happens for other tensor factors such as \(\wedge^h\mathbb C^d\). Its open-problem discussion gives exactly the \(n=5\), \(h=2\), \(\lambda=(1,1,1,0,0)\), \(\mu=(2,1,1,1,0)\) example: the coherent largest eigenvalue is \(1/3\), while another state reaches \(2/5\). The present result proves that \(2/5\) is globally optimal and extends the phenomenon, with exact optimum and maximizers, to every \(n\ge5\).

Reuvers, arXiv:1805.00364v2, gives exact one-particle Schmidt bounds for Young-diagram subspaces and develops the projection reformulation of largest Schmidt coefficients. Its main theorem concerns the cut \((\mathbb C^d)^{\otimes(N-1)}\otimes\mathbb C^d\); its larger-cut discussion constrains Schmidt-vector symmetry but does not give the exterior-square \((n-2)\)-versus-two optimum proved here. The present proof uses the same general variational idea but requires the adjoint realization and the sharp two-form transition inequality above.

## Limitations
No claim is made about the complete output spectrum, full majorization, minimum von Neumann entropy, or other Pieri summands. The proof is specific to the adjoint-twist summand arising from \(\wedge^{n-2}V\otimes\wedge^2V\). Although targeted searches found no equivalent published formula, representation-theoretic or geometric-entanglement literature could contain the same subspace-overlap constant under different terminology; this is the main residual originality risk.

## References
1. R. Reuvers, *Minimal output entropy for the channels that add or remove a box of a Young diagram, and a Pauli principle for every permutation symmetry*, arXiv:2609.33498v1 (2026).
2. R. Reuvers, *Lower bound on entanglement in subspaces defined by Young diagrams*, arXiv:1805.00364v2 (2019).

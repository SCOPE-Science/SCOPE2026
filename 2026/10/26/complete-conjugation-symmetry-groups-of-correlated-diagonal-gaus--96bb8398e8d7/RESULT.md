# Complete conjugation-symmetry groups of correlated-diagonal Gaussian Hermitian matrices

## Finding

**Theorem.** Fix an integer \(M\geq 2\) and a real symmetric positive-semidefinite matrix \(\Sigma\in\mathbb R^{M\times M}\). Let \(H\) be the centered Gaussian Hermitian matrix with independent upper off-diagonal entries distributed as circular complex Gaussians of second absolute moment one, and with an independent real diagonal vector of covariance \(\Sigma\). Define its unitary conjugation symmetry group by
\[
G_\Sigma=\{U\in U(M):UHU^*\stackrel{d}{=}H\}.
\]
Put \(A=\Sigma-I_M\), and partition \(\{1,\ldots,M\}\) into maximal classes \(C_1,\ldots,C_r\) under the exact relation
\[
i\sim j\quad\Longleftrightarrow\quad A(e_i-e_j)=0
\quad\Longleftrightarrow\quad \Sigma(e_i-e_j)=e_i-e_j.
\]
Thus members of one class have identical columns, equivalently identical rows, in \(A\). Set \(V_\alpha=\operatorname{span}\{e_i:i\in C_\alpha\}\). Then
\[
\boxed{G_\Sigma=\left(\prod_{\alpha=1}^r U(V_\alpha)\right)
\operatorname{Aut}_{\rm perm}(\Sigma),\qquad
G_\Sigma^0=\prod_{\alpha=1}^r U(V_\alpha),}
\]
where the second factor in the first formula consists of permutation matrices \(P\) with \(P\Sigma P^T=\Sigma\); the product is a set-product, and \(G_\Sigma^0\) denotes the identity component. In particular,
\[
\dim_{\mathbb R}G_\Sigma=\sum_{\alpha=1}^r|C_\alpha|^2,
\]
and the finite component group is naturally isomorphic to
\[
\operatorname{Aut}_{\rm perm}(\Sigma)\big/\prod_{\alpha=1}^r\mathfrak S(C_\alpha).
\]
Consequently the continuous symmetry exceeds the diagonal torus exactly when some two distinct coordinate rows of \(\Sigma-I_M\) agree. Full unitary invariance holds exactly when \(\Sigma=I_M+b\mathbf1\mathbf1^T\), with \(b\geq-1/M\) (the weak inequality allows singular covariance).

## Assumptions and scope

We use the normalization \(\mathbb E|H_{ij}|^2=1\) for \(i<j\); hence the real and imaginary parts of each off-diagonal entry independently have variance \(1/2\). All entries are jointly Gaussian; the real diagonal vector is independent of the off-diagonal family, and each off-diagonal upper-triangular entry is independent of the others. The covariance \(\Sigma\) need only be positive semidefinite, not invertible. The group concerns invariance in distribution under conjugation by deterministic complex-unitary matrices; it does not describe invariance under antiunitary operators or equality merely of spectral laws. Products \(U(V_\alpha)\) act as the identity on the orthogonal complement of their coordinate blocks.

## Proof

**1. Gaussian covariance reduction.** On the real Hilbert space \(\mathcal H_M\) of Hermitian matrices with inner product \(\langle X,Y\rangle=\operatorname{Tr}(XY)\), write \(D(X)=(X_{11},\ldots,X_{MM})\) and \(D^*(x)=\operatorname{diag}(x)\). For standard GUE with the normalization above, the covariance operator is the identity on \(\mathcal H_M\); indeed the Hilbert–Schmidt normalized off-diagonal real and imaginary coordinates have variance one, just as the diagonal coordinates. Replacing the diagonal covariance \(I_M\) by \(\Sigma\) gives the exact covariance operator
\[
T=I_{\mathcal H_M}+D^* A D,\qquad A=\Sigma-I_M.
\]
Equality in law of centered real Gaussian vectors, including degenerate ones, is equivalent to equality of covariance operators. Conjugation \(\operatorname{Ad}_U:X\mapsto UXU^*\) is orthogonal on \(\mathcal H_M\). Thus \(U\in G_\Sigma\) if and only if \(\operatorname{Ad}_U T=T\operatorname{Ad}_U\), equivalently it commutes with \(S=D^*AD\). This formulation requires no covariance inverse.

**2. Determine every infinitesimal symmetry.** The set \(G_\Sigma\) is a closed subgroup of compact \(U(M)\), hence a compact Lie group. If \(K^*=-K\) belongs to its real Lie algebra, differentiating the identity \(\operatorname{Ad}_{\exp(tK)}S=S\operatorname{Ad}_{\exp(tK)}\) gives
\[
[K,S(X)]=S([K,X])\quad\text{for all }X\in\mathcal H_M.
\]
Substitute the coordinate projection \(X=E_{ii}=e_ie_i^*\). Since the Hermitian commutator \([K,E_{ii}]\) has zero diagonal, its image under \(S\) is zero, while \(S(E_{ii})=\operatorname{diag}(Ae_i)\). Its off-diagonal \((a,b)\) entry yields
\[
K_{ab}(A_{bi}-A_{ai})=0\quad\text{for all }i,\ a\ne b.
\]
Consequently \(K_{ab}\ne0\) forces equality of rows \(a,b\) in \(A\), precisely \(a\sim b\). Every infinitesimal symmetry is therefore block diagonal with respect to the partition \(C_\alpha\).

**3. Every unitary within a class is a symmetry.** Identical rows and symmetry of \(A\) imply that \(A_{ij}=a_{\alpha\beta}\) whenever \(i\in C_\alpha\), \(j\in C_\beta\). Write \(P_\alpha\) for the coordinate projection onto \(V_\alpha\). For any \(X\in\mathcal H_M\),
\[
S(X)=\sum_{\alpha,\beta} a_{\alpha\beta}\,
\operatorname{Tr}(P_\beta X)P_\alpha.
\]
Every block-diagonal \(B\in\prod_\alpha U(V_\alpha)\) preserves these block traces, commutes with each \(P_\alpha\), and so satisfies \(S(BXB^*)=BS(X)B^*\). Thus the entire connected group \(B_0=\prod_\alpha U(V_\alpha)\) lies in \(G_\Sigma\). By Step 2 its Lie algebra equals the full Lie algebra of \(G_\Sigma\). The connected subgroup \(B_0\) must therefore be exactly \(G_\Sigma^0\), proving the identity-component formula and its real dimension.

**4. No other disconnected symmetries.** Every \(U\in G_\Sigma\) normalizes the identity component \(G_\Sigma^0=B_0\). The commutant in the complex full matrix algebra of \(B_0\) consists exactly of \(\sum_\alpha z_\alpha P_\alpha\). Its minimal nonzero projections are \(P_1,\ldots,P_r\). Normalization therefore forces \(UP_\alpha U^*\) to be one of these projections: \(U\) permutes the coordinate blocks, necessarily preserving each block dimension. Choose a permutation matrix \(P\) implementing exactly that block permutation, by bijections between equal-sized classes, and put \(B=UP^*\). Then \(B\) is block diagonal and belongs to \(B_0\subseteq G_\Sigma\); hence \(P=B^*U\in G_\Sigma\). A coordinate permutation preserves the Gaussian law exactly when it preserves the diagonal covariance, i.e. \(P\Sigma P^T=\Sigma\), because the independent off-diagonal distribution is already permutation-invariant. Thus \(U=BP\) with both factors as asserted. Conversely, every such product preserves the law. Intersecting the permutation subgroup with \(B_0\) leaves precisely the permutations within each class, yielding the component quotient formula.

**5. Sharp criteria and edge cases.** The identity-component dimension exceeds \(M\) exactly if a class has size at least two, equivalently \(\Sigma(e_i-e_j)=e_i-e_j\) for some distinct indices. All coordinates belong to one class exactly when \(A\) has every row identical. Since \(A\) is symmetric, this forces \(A=b\mathbf1\mathbf1^T\). Positivity of \(\Sigma\) is then equivalent to \(b\geq-1/M\), proving the full-unitary criterion even at the singular boundary. In particular, merely having \(1\) as an eigenvalue of \(\Sigma\) is insufficient for symmetry enlargement: the required unit eigenvector must be one of the coordinate differences \(e_i-e_j\).

## Verification

The self-contained script `check_correlated_gaussian_symmetries.py` uses exact rational arithmetic to test \(S(UHU^*)=US(H)U^*\) on a spanning set of real symmetric test matrices. It exercises block rotations, rotations joining distinct classes, all coordinate permutations in small examples, a covariance with repeated blocks, a covariance with eigenvalue one but all row classes singleton, and a singular covariance. Running `python3 check_correlated_gaussian_symmetries.py` reported **102 passing exact-rational assertions**. Those finite checks support the normalization and combinatorial implications; the universal classification, complex-unitary sufficiency, and all dimensions follow from Steps 1–5, not from enumeration.

For a concrete distinction, let \(\Sigma=I_3+vv^T\) with \(v=(1,2,3)^T\). Although \(1\) is an eigenvalue of multiplicity two, all rows of \(\Sigma-I_3\) differ, so \(G_\Sigma^0=U(1)^3\), and no nonidentity coordinate permutation preserves \(\Sigma\). By contrast, for \(\Sigma=I_4+b\mathbf1_{\{1,2\}}\mathbf1_{\{1,2\}}^T+c\mathbf1_{\{3,4\}}\mathbf1_{\{3,4\}}^T\) with distinct positive \(b,c\), the connected group is \(U(2)\times U(2)\).

## Relationship to prior work

Houdré and Kidonakis (2026, Proposition 2.2) define this same Gaussian Hermitian ensemble and prove that the unitary symmetry group is monomial, subject to covariance-preserving permutations, under positive definiteness and the additional assumption \(1\notin\operatorname{spec}(\Sigma)\). Their Remark 2.3(ii) expressly identifies the eigenvalue-one case as needing separate analysis. They also give examples of full unitary symmetry for \(\Sigma=I_M+b\mathbf1\mathbf1^T\) with positive \(b\). The theorem here instead settles all positive-semidefinite covariances, classifies every intermediate continuous block-unitary group and every disconnected component, and determines the exact condition needed for enhanced continuous invariance. The generic monomial formula and previously exhibited full-unitary examples are recovered and are not claimed independently new. The reduction to a Gaussian covariance stabilizer and standard Lie-group normalizer facts are classical ingredients.

## Limitations

The result is confined to the specified centered Gaussian Hermitian law with independent circular complex-Gaussian off-diagonal entries of common second absolute moment one. Different off-diagonal variances, non-Gaussian entries, antiunitary maps, and transformations preserving only the eigenvalue distribution are not classified. A broad theorem on Gaussian covariance stabilizers might imply the classification through additional work; the primary-paper comparison supports, but cannot certify, novelty beyond the examined sources. No independent mathematical audit has been performed.

## References

1. Christian Houdré and Dorian Kidonakis, *Markovian Random Words, a Gaussian Random Matrix Model and Beyond*, arXiv:2610.12950v1, first publicly submitted October 9, 2026; especially Section 2, Proposition 2.2 and Remark 2.3(ii). https://arxiv.org/html/2610.12950v1
2. Standard finite-dimensional centered Gaussian covariance uniqueness and compact unitary Lie-group normalizer principles (used in proof, with all specialized calculations given above).

# Exact inverse-bias law for ordered sparse Schur-clique trees

## Finding

**Theorem (an exact inverse-moment law for one-tree clique elimination).** Let \(n\ge 2\) be an integer and \(P=I_n-\frac1n\mathbf 1\mathbf 1^{\mathsf T}\). Consider elimination of the center of an unweighted star with \(n\) leaves. Its exact Schur-complement update on the leaves is \(P\), the weighted complete-graph Laplacian with conductance \(1/n\) on every unordered pair.

Run the one-tree `SampleClique` rule with a fixed tie order \(1,\ldots,n\): independently for each \(i=1,\ldots,n-1\), choose \(J_i\) uniformly from \(\{i+1,\ldots,n\}\) and insert the undirected edge \(\{i,J_i\}\) with conductance \(c_i=(n-i)/n\). Write \(T\) for the resulting random tree Laplacian and \(T^\dagger\) for its Moore–Penrose pseudoinverse. Then, for every distinct \(a,b\in\{1,\ldots,n\}\),

\[
\mathbb E\big[(e_a-e_b)^{\mathsf T}T^\dagger(e_a-e_b)\big]=n,
\qquad
\mathbb E[T^\dagger]=\frac n2P^\dagger=\frac n2P,
\qquad \mathbb E[T]=P.
\]

Since \((e_a-e_b)^{\mathsf T}P^\dagger(e_a-e_b)=2\), every pair's **expected** resistance is inflated by exactly \(n/2\) relative to the exact clique. Moreover the final two leaves satisfy the deterministic identity

\[
(e_{n-1}-e_n)^{\mathsf T}T^\dagger(e_{n-1}-e_n)=n
\]

in every outcome, and hence every outcome obeys

\[
\lambda_{\min}\big(T\vert_{\mathbf 1^\perp}\big)\le\frac2n,
\]

where the minimum is over the strictly positive eigenvalues. This is a one-local-update obstruction: unbiasedness and connectedness of a single sparse clique replacement do not imply inverse unbiasedness or a dimension-independent lower spectral approximation.

## Assumptions and scope

All arithmetic is exact, all star-edge conductances equal one, and the star center is eliminated before any leaf. The fixed order on the equally weighted leaves resolves arbitrary sorting ties. The one-tree rule is Algorithm 3 (`SampleClique`) of Chen–Liang–Biros [1], or the corresponding single-tree `CliqueTreeSample` specialization of Gao–Kyng–Spielman [2]. The draws for different \(i\) are independent. Edge conductance means a positive coefficient multiplying \((e_i-e_j)(e_i-e_j)^{\mathsf T}\); edge resistance is its reciprocal. The update \(T\) is a Laplacian on **only the surviving \(n\) leaves**, not the entire approximate Cholesky factorization or the original star Laplacian.

The nullspaces of \(P\), \(T\) and their pseudoinverses are \(\operatorname{span}\{\mathbf1\}\); all inverse and spectral claims are interpreted on \(\mathbf1^\perp\). The full probability space has \((n-1)!\) equiprobable parent maps. There is no asymptotic approximation in the theorem.

## Proof

**1. Exact and sampled conductances.** The star Laplacian in the basis (center, leaves) is

\[
L_\star=\begin{pmatrix}n&-\mathbf1^{\mathsf T}\\-\mathbf1&I_n\end{pmatrix}.
\]

Eliminating the center gives \(I_n-\mathbf1\mathbf1^{\mathsf T}/n=P\). The star-edge coefficients supplied to `SampleClique` are all one. Immediately before processing \(i\), the unprocessed incident weight sum equals \(n-i\), so its rule produces a parent chosen uniformly among the \(n-i\) later labels and a sampled-edge conductance \((n-i)/n\). The parent map is strictly increasing and every non-root vertex has one parent, so it forms a tree rooted at \(n\).

For every \(i<j\), the edge \(\{i,j\}\) occurs with probability \(1/(n-i)\) and, when it occurs, has conductance \((n-i)/n\). Its expected coefficient is \(1/n\); summing over all unordered pairs yields \(\mathbb E T=P\). Unbiasedness is also explicitly established in [1,2], and is included here to fix the comparison normalization.

**2. Exact expected electrical distances by backward induction.** Let \(T_k\) denote the tree on the remaining vertices \(\{k,\ldots,n\}\) formed by edges with lower endpoint at least \(k\), and let \(R_k(a,b)\) be its effective resistance. As \(T_k\) is a tree, \(R_k(a,b)\) is the sum of the edge resistances on its unique \(a\)-to-\(b\) path. The last edge \(\{n-1,n\}\) is deterministic, has conductance \(1/n\), and therefore \(R_{n-1}(n-1,n)=n\).

Assume that for some \(k\le n-2\), every two distinct vertices in \(\{k+1,\ldots,n\}\) have expected resistance \(n\) in \(T_{k+1}\). The next sampled edge joins the new pendant vertex \(k\) to independent uniform \(J_k\in\{k+1,\ldots,n\}\), with resistance \(n/(n-k)\). Existing pairwise resistances in \(T_{k+1}\) are unchanged. For fixed \(j>k\), series addition gives

\[
R_k(k,j)=\frac{n}{n-k}+R_{k+1}(J_k,j).
\]

Exactly one of the \(n-k\) possible values of \(J_k\) equals \(j\), giving resistance zero; each other value has expectation \(n\) by induction. Independence of the new parent and the older tree therefore yields

\[
\mathbb E R_k(k,j)=\frac{n}{n-k}+\frac{n-k-1}{n-k}n=n.
\]

This proves, simultaneously for every \(2\le n<\infty\) and every distinct pair, that \(\mathbb E R_T(a,b)=n\).

**3. Recovering the entire inverse moment.** For any connected Laplacian \(Q\), with centered pseudoinverse \(M=Q^\dagger\), its resistance matrix \(D\) obeys \(D_{ab}=M_{aa}+M_{bb}-2M_{ab}\). Multiplication on both sides by \(P\) gives \(PDP=-2M\), because \(M\mathbf1=0\). Consequently \(M=-PDP/2\). Applying this identity to \(T\) and taking expectations is justified by the finite probability space. The expected resistance matrix has zero diagonal and constant off-diagonal entries \(n\), so \(\mathbb ED=n(\mathbf1\mathbf1^{\mathsf T}-I_n)\). It follows that

\[
\mathbb E[T^\dagger]=-\tfrac12P(\mathbb ED)P=\tfrac n2P.
\]

Since \(P\) is an orthogonal projector, \(P^\dagger=P\). Thus the mean pseudoinverse is the **same scalar multiple in every centered direction**, not merely on average over selected pairs.

**4. Deterministic spectral obstruction.** For each outcome, the final two leaves are linked directly by the deterministic conductance \(1/n\) edge, so their resistance is exactly \(n\). Let \(b=e_{n-1}-e_n\), so \(b\perp\mathbf1\) and \(\|b\|_2^2=2\). The Rayleigh quotient of \(T^\dagger\) on \(b\) is \(n/2\). Therefore \(\lambda_{\max}(T^\dagger\vert_{\mathbf1^\perp})\ge n/2\), and reciprocating its positive eigenvalues yields the claimed bound \(\lambda_{\min}(T\vert_{\mathbf1^\perp})\le2/n\). The conclusion concerns every realized one-tree update, without a probability qualifier. \(\square\)

## Verification

`verify.py` needs only Python 3 standard-library modules `fractions`, `itertools` and `math`. Run `python3 verify.py` from the directory holding this document and the script. It exhaustively enumerates all \((n-1)!\) parent maps for each \(2\le n\le8\) (5,913 trees in total). Exact rational arithmetic checks every expected edge conductance, every expected pair resistance, the deterministic last-pair resistance and every entry of the inverse matrix obtained by double-centering. It does **not** prove the claim for \(n>8\); the preceding induction and linear-algebra argument do.

## Relationship to prior work

Chen, Liang and Biros [1, Algorithm 3; Theorems 7 and 10] introduce the actual ordered clique-tree sampling law, prove connectedness/unbiasedness and use it in a sparse solver. Gao, Kyng and Spielman [2, Algorithm 3; Corollary 4.4 and Claim 4.5] give a closely related, algorithmically equivalent tree sampling formulation, an elementary tree induction and a broader approximate-Cholesky framework. Those statements imply neither the precise average inverse nor a dimension-uniform spectral lower bound without additional analysis; the exact all-pairs inverse-moment identity here is the new claim.

Kyng and Sachdeva [3] obtain spectral approximation using a different algorithm with controlled sampling, splitting and elimination; their higher-sampling guarantees do not assert strong local approximation by a single unsplit tree. CAST [4] studies a *different*, order-independent weighted spanning-tree sampler with leverage-optimal edge marginals; even on the equal-weight clique its random-tree law and reweighted conductances differ from the ordered `SampleClique` rule. The present identity therefore does not apply to CAST without separate calculation. Generic matrix-convexity/Jensen principles predict the direction of inverse bias but not this exact \(n/2\) scalar, and standard electrical-network identities alone do not identify the expectation without the sampling-law induction.

## Limitations

The exact factor concerns one local elimination of an equal-weight star **with its center processed first**, fixed leaf tie order, and one connected tree replacement. It does not characterize typical fill-reducing elimination order, multi-edge sampling, aggregate factorization error, solution accuracy of preconditioned conjugate gradients, or all stochastic spanning-tree laws. The deterministic small-eigenvalue bound is a **one-sided** bound, not an assertion of equality or a complete spectrum. Mathematically equivalent results could exist in literature not inspected.

## References

[1] C. Chen, T. Liang, and G. Biros, *RCHOL: Randomized Cholesky Factorization for Solving SDD Linear Systems*, arXiv:2011.07769v1 (first public version 2020-11-16), especially Section 2 and Algorithm 3. https://arxiv.org/abs/2011.07769

[2] Y. Gao, R. Kyng, and D. A. Spielman, *Robust and Practical Solution of Laplacian Equations by Approximate Elimination*, arXiv:2303.00709v1 (2023-03-01), especially Section 4.2, Algorithm 3, Corollary 4.4, Claim 4.5. https://arxiv.org/abs/2303.00709

[3] R. Kyng and S. Sachdeva, *Approximate Gaussian Elimination for Laplacians: Fast, Sparse, and Simple*, arXiv:1605.02353 (2016), algorithm and approximation hypotheses. https://arxiv.org/abs/1605.02353

[4] *CAST: Canonical Approximate Schur Tree for Approximate Cholesky on Graphs*, arXiv:2609.09255v1 (2026), Sections 2–4 and 6, especially the distinct weighted-tree distribution and inverse-marginal reweighting. https://arxiv.org/abs/2609.09255

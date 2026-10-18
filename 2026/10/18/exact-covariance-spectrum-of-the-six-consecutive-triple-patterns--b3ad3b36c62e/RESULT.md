# Exact covariance spectrum of the six consecutive triple patterns in uniform permutations

## Finding
Let \(n\ge4\), and let \(\Pi\) be a uniform permutation of \(\{1,\ldots,n\}\). For each \(\tau\in S_3\), let \(N_\tau\) be the number of indices \(1\le i\le n-2\) for which \((\Pi_i,\Pi_{i+1},\Pi_{i+2})\) has relative order \(\tau\). Order the six counts as \((N_{123},N_{132},N_{213},N_{231},N_{312},N_{321})\), and let \(\Sigma_n\) denote their covariance matrix.

The **complete, finite-sample covariance spectrum**, including multiplicities, is
\[
\operatorname{spec}(\Sigma_n)=\left\{0,\ \frac18,\ \frac{12n-13}{120},\ \frac{16n-29}{120},\ \frac{8n-13-\sqrt{32n^2-224n+393}}{48},\ \frac{8n-13+\sqrt{32n^2-224n+393}}{48}\right\}.
\]
For \(n=4\), the two middle linear eigenvalues coincide; each listed eigenvalue is otherwise simple. The nullspace is spanned by the all-ones vector. The eigenvalue \(1/8\) is the unique smallest positive eigenvalue for every \(n\ge4\), and its fixed eigenvector is
\[
 v=(0,-1,1,-1,1,0)^\mathsf T.
\]
The associated random variable is exactly a boundary statistic:
\[
 v^\mathsf TN=\mathbf1\{\Pi_{n-1}<\Pi_n\}-\mathbf1\{\Pi_1<\Pi_2\}.
\]
Its distribution is \(\Pr(v^\mathsf TN=1)=\Pr(v^\mathsf TN=-1)=1/4\) and \(\Pr(v^\mathsf TN=0)=1/2\). Thus its variance remains exactly \(1/2\), whereas the variances of all four remaining orthogonal nonconstant modes grow linearly with \(n\).

The largest eigenvalue is
\[
 \Lambda_n=\frac{8n-13+\sqrt{32n^2-224n+393}}{48},
\]
so the covariance condition number on the five-dimensional space orthogonal to the constant vector is exactly
\[
\kappa_n=8\Lambda_n=\frac{8n-13+\sqrt{32n^2-224n+393}}6\sim\frac{4+2\sqrt2}{3}\,n.
\]
The result is a covariance statement, not an assertion of independence or of a joint central limit theorem.

## Assumptions and scope
The permutation is uniform over all \(n!\) linear permutations, with no circular wrap-around, ties, or pattern avoidance. Consecutive triples start at positions \(1\) through \(n-2\). All formulas hold for every integer \(n\ge4\), with no asymptotic assumptions; the asymptotic condition-number assertion takes \(n\to\infty\). The convention for eigenvalues is the ordinary Euclidean covariance spectrum of the **unstandardized count vector**, not the Pearson-correlation spectrum of the six marginal counts.

## Proof
**Step 1 (independent order patterns on disjoint sets).** Realize the uniform permutation as the ranks of independent continuous observations \(U_1,\ldots,U_n\). The relative orders on disjoint index sets are independent. The six possible orders of one triple are equiprobable. For \(h=1,2\), define the \(6\times6\) rational matrix
\[
 Q_h(\alpha,\beta)=\frac1{(3+h)!}\#\left\{\sigma\in S_{3+h}:\operatorname{std}(\sigma_1,\sigma_2,\sigma_3)=\alpha,\ \operatorname{std}(\sigma_{1+h},\sigma_{2+h},\sigma_{3+h})=\beta\right\}.
\]
This is a finite enumeration over \(S_4\) and \(S_5\), respectively; it does not depend on \(n\). If \(I_6\) and \(J_6\) are the identity and all-ones matrices, respectively, the ordered-pair covariance count gives
\[
\Sigma_n=(n-2)(I_6/6-J_6/36)
 +(n-3)(Q_1+Q_1^\mathsf T-2J_6/36)
 +(n-4)(Q_2+Q_2^\mathsf T-2J_6/36).
\]
The terms with shifts greater than two vanish through independence. The coefficients count, respectively, identical triple locations, pairs at distance one, and pairs at distance two. This identity includes \(n=4\), when the distance-two coefficient is zero.

**Step 2 (the exact covariance matrix).** Evaluation of these \(4!+5!\) finite orderings yields \(\Sigma_n=M_n/360\), where
\[
M_n=\begin{pmatrix}
46n-74&67-23n&67-23n&7n-38&7n-38&16-14n\\
67-23n&28n-32&10n-35&40-20n&-2n-2&7n-38\\
67-23n&10n-35&28n-32&-2n-2&40-20n&7n-38\\
7n-38&40-20n&-2n-2&28n-32&10n-35&67-23n\\
7n-38&-2n-2&40-20n&10n-35&28n-32&67-23n\\
16-14n&7n-38&7n-38&67-23n&67-23n&46n-74
\end{pmatrix}.
\]
Direct multiplication verifies that the vectors \((1,1,1,1,1,1)^\mathsf T\), \((0,-1,1,-1,1,0)^\mathsf T\), \((0,1,-1,-1,1,0)^\mathsf T\), and \((2,-1,-1,-1,-1,2)^\mathsf T\) are mutually orthogonal eigenvectors, with respective eigenvalues \(0,1/8,(12n-13)/120,(16n-29)/120\). The two-dimensional orthogonal complement is invariant. Evaluating the remaining characteristic polynomial (or restricting \(M_n\) to this complement) yields
\[
\det(zI_6-\Sigma_n)=
\frac{z(8z-1)(120z-12n+13)(120z-16n+29)
(144z^2+(78-48n)z+2n^2+n-14)}{16588800}.
\]
Its quadratic roots are the two stated radical eigenvalues. The identity is exact symbolic arithmetic; the accompanying program reproduces both the matrix and factorization from permutations of length at most five.

**Step 3 (bounded mode and extremal eigenvalues).** Each interior triple is either a peak \(132,231\), a valley \(213,312\), or monotone \(123,321\). Write \(A_i=\mathbf1\{\Pi_i<\Pi_{i+1}\}\). For every \(i\le n-2\), the valley indicator minus the peak indicator equals \(A_{i+1}-A_i\). Summing telescopes to \(A_{n-1}-A_1\). Because \(n\ge4\), the first and final comparisons depend on disjoint sets of independent observations; each is Bernoulli\((1/2)\). This proves the stated three-point distribution and variance. Since \(v^\mathsf Tv=4\), the covariance eigenvalue is \((1/2)/4=1/8\).

For \(n\ge4\), the linear eigenvalues \((12n-13)/120\) and \((16n-29)/120\) both exceed \(1/8\). The smaller radical root also exceeds \(1/8\): its difference from \(1/8\) is \((8n-19-\sqrt{32n^2-224n+393})/48\), and \(8n-19>0\) with
\[
(8n-19)^2-(32n^2-224n+393)=16(2n^2-5n-2)>0.
\]
The larger radical root exceeds the two linear eigenvalues by direct subtraction (for example, relative to \((16n-29)/120\), the difference is \(n/30-7/240+\sqrt{32n^2-224n+393}/48>0\)). Thus all five nonzero eigenvalues are positive, the largest and smallest are as asserted, and \(\kappa_n\) follows. The leading term of its numerator gives the displayed asymptotic constant.

## Verification
Run `python verify.py` with Python 3 and SymPy. The code reconstructs the two overlap tables by enumerating all \(4!\) and \(5!\) local rank orders, exactly derives \(M_n\), symbolically factors the characteristic polynomial, checks fixed eigenvectors, enumerates all \(4!+5!+6!+7!+8!\) uniform permutations for exact covariance/boundary assertions, and checks spectral inequalities numerically for integers \(4\le n\le300\). The local exact combinatorial derivation and characteristic-polynomial identity—not the finite sample enumeration—prove the theorem for all \(n\ge4\).

## Relationship to prior work
Borga's 2020 work (arXiv:2003.08426) proves central-limit theorems for consecutive patterns in **pattern-avoiding classes** represented by generating trees, not an exact six-pattern covariance spectrum for unrestricted uniform permutations. Borga and Penaguiao (arXiv:1910.02233) determine the limiting feasible polytope and its overlap-flow equations; notably, the limiting polytope has dimension four for size-three patterns. Those equations explain the existence of boundary corrections, but they do not specify the covariance matrix or any of its five finite-sample eigenvalues. Crane, DeSalvo, and Elizalde (arXiv:1609.01370, Theorem 8.1, equations (33)–(34)) establish weak dissociation and consecutive homogeneity and an exact finite-\(n\) **variance formula for each individual pattern count**, covering the diagonal entries of this covariance matrix and ingredients of Step 1. The diagonal variances are therefore **not** claimed to be new; their treatment does not give the cross-pattern covariances, the six-dimensional eigenspaces, or the exact sharp condition number. Crane and DeSalvo (arXiv:1509.07941) study pattern avoidance and Poisson approximation; its methods also differ from the explicit joint covariance diagonalization here. The boundary telescoping identity is elementary and is not claimed independently as a novel fact; its exact position in the covariance spectrum, together with the complete finite-dimensional eigenvalues and sharp condition number, constitutes the assessed result.

## Limitations
Historical priority is assessed from the cited full-text inspections and targeted searches, not independently certified; a multivariate generating-function treatment of consecutive patterns might implicitly yield this spectrum. The law is for the **uniform unrestricted** model and cannot be transferred without new work to Mallows distributions with nonuniform parameters or to avoidance classes. The eigenvalues concern unstandardized counts. The four growing eigenscores are pairwise uncorrelated by construction, but need not be independent; this theorem alone does not supply a multivariate normal approximation, hypothesis test, independence decomposition, or distributional convergence for the bounded mode beyond its exact law. Independent audit and external validation have not been performed.

## References
1. J. Borga, *Asymptotic normality of consecutive patterns in permutations encoded by generating trees with one-dimensional labels*, arXiv:2003.08426, first public version 18 March 2020, https://arxiv.org/abs/2003.08426.
2. J. Borga and R. Penaguiao, *The feasible region for consecutive patterns of permutations is a cycle polytope*, arXiv:1910.02233, first public version 5 October 2019, https://arxiv.org/abs/1910.02233.
3. H. Crane, S. DeSalvo and S. Elizalde, *The probability of avoiding consecutive patterns in the Mallows distribution*, arXiv:1609.01370, first public version 6 September 2016, https://arxiv.org/abs/1609.01370.
4. H. Crane and S. DeSalvo, *Pattern avoidance for random permutations*, arXiv:1509.07941, first public version 26 September 2015, https://arxiv.org/abs/1509.07941.

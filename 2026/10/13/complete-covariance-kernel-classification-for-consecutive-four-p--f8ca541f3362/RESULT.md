# Complete covariance-kernel classification for consecutive four-pattern counts

## Finding

Let \(\pi\) be uniformly distributed on the permutations of \(\{1,\ldots,n\}\), \(n\ge4\). For each \(\tau\in S_4\), let \(N_\tau\) count indices \(i\in\{1,\ldots,n-3\}\) whose consecutive four entries have relative order \(\tau\). Let \(Z_n=(N_\tau-(n-3)/24)_{\tau\in S_4}\). Define \(\Gamma=\lim_{n\to\infty}n^{-1}\operatorname{Cov}(Z_n)\), with coordinates in lexicographic order \(1234,1243,\ldots,4321\). Then \(\Gamma\) exists, is positive semidefinite, and has **rank exactly \(18\)** (nullity \(6\)). Its entire nullspace is

\[
\ker\Gamma=\left\{c:\ c_\tau=a+g(\operatorname{ord}(\tau_1,\tau_2,\tau_3))-g(\operatorname{ord}(\tau_2,\tau_3,\tau_4)),\quad a\in\mathbb R,\ g:S_3\to\mathbb R\right\}.
\]

Here \(\operatorname{ord}\) means the relative-order permutation, and the representation has one redundant parameter because adding a constant to \(g\) has no effect. Thus the nonconstant kernel is exactly the five-dimensional space of endpoint coboundaries; no other nonconstant linear combination has sublinear variance.

More precisely, for every such \(c\) and every \(n\ge4\),
\[
\sum_{\tau\in S_4} c_\tau N_\tau=a(n-3)+g(\operatorname{ord}(\pi_1,\pi_2,\pi_3))-g(\operatorname{ord}(\pi_{n-2},\pi_{n-1},\pi_n)).
\]
For \(n\ge6\), the two endpoint patterns are independent and each is uniform on \(S_3\); consequently the exact variance of this contrast is \(2\operatorname{Var}(g(U))\) with \(U\) uniform on \(S_3\). For every real coefficient vector \(c\notin\ker\Gamma\),
\[
\operatorname{Var}\bigl(\textstyle\sum_\tau c_\tau N_\tau\bigr)=n\,c^{\mathsf T}\Gamma c+O(1),\qquad c^{\mathsf T}\Gamma c>0.
\]
Finally, \(Z_n/\sqrt n\) converges in distribution to a centered Gaussian vector with covariance \(\Gamma\), supported on an exactly 18-dimensional linear subspace.

## Assumptions and scope

The permutation is uniform, all entries are distinct, windows are consecutive of length exactly four, and \(n\ge4\). Equivalently, let \(X_1,\ldots,X_n\) be independent atomless identically distributed real random variables and take their overall ranking; each window pattern depends only on its four \(X\)'s. This representation supplies independence when window index gaps are at least four. The limit is at fixed pattern length four as \(n\to\infty\). No analogous rank assertion for longer patterns, dependent data, or nonuniform permutations is made.

## Proof

Write \(\mathcal P=S_4\), let \(H_i(\tau)=\mathbf 1\{\operatorname{ord}(X_i,\ldots,X_{i+3})=\tau\}\), and \(m=n-3\). The twenty-four-dimensional process \((H_i)\) is stationary and 3-dependent, with mean \(\mathbf1/24\). For \(d=0,1,2,3\), form the **explicit finite joint-probability matrix**
\[
Q_d(\tau,\sigma)=\frac{1}{(4+d)!}\#\left\{\rho\in S_{4+d}:\operatorname{ord}(\rho_1,\ldots,\rho_4)=\tau,\ \operatorname{ord}(\rho_{d+1},\ldots,\rho_{d+4})=\sigma\right\}-\frac1{576}.
\]
In particular, \(Q_0(\tau,\sigma)=\mathbf1_{\tau=\sigma}/24-1/576\). Distinct windows at lag \(d\ge4\) are independent. Hence for every \(n\ge4\) the **exact covariance matrix** satisfies
\[
\operatorname{Cov}(Z_n)=mQ_0+\sum_{d=1}^{\min(3,m-1)}(m-d)(Q_d+Q_d^{\mathsf T}).
\]
Taking \(n\to\infty\) yields \(\Gamma=Q_0+\sum_{d=1}^{3}(Q_d+Q_d^{\mathsf T})\), which is positive semidefinite because it is a limit of covariance matrices divided by \(n\).

The full integer matrix \(A=20160\Gamma\), in lexicographic pattern order, is included in `COVARIANCE_MATRIX.json`. The self-contained `verify.py` reconstructs all four \(Q_d\) by exhausting \(S_4,S_5,S_6,S_7\), confirms each of the 576 matrix entries against the stored integers, and proves the following exact finite certificate using modular arithmetic at prime \(1000003\):
\[
\det A[0{:}18,0{:}18]\equiv897856\pmod{1000003}\ne0.
\]
Thus \(\operatorname{rank}_{\mathbb R}\Gamma\ge18\). The checker constructs seven integer vectors: the all-ones vector plus six vectors with entries \(\mathbf1\{\operatorname{ord}(\tau_1,\tau_2,\tau_3)=q\}-\mathbf1\{\operatorname{ord}(\tau_2,\tau_3,\tau_4)=q\}\), one for every \(q\in S_3\). Exact integer multiplication verifies \(A v=0\) for all seven. Their rank over the same prime field is exactly six, hence their real span has dimension at least six. Since the sum of the six coboundary vectors is identically zero, this span has real dimension at most six. Therefore \(\dim\ker\Gamma\ge6\). Combining \(\operatorname{rank}\Gamma\ge18\) with \(\dim\ker\Gamma\ge6\) in dimension 24 proves rank 18 and exhausts the nullspace. The modular determinant proves a nonzero **integer** minor in characteristic zero; no floating-point rank threshold is used.

For a kernel vector, summing its consecutive three-pattern differences telescopes to the first and last length-three windows, proving the exact identity. If \(n\ge6\), those endpoint patterns are independent as functions of disjoint sets of independent \(X\)'s, yielding the stated variance. A vector outside the kernel has strictly positive quadratic form because \(\Gamma\) is positive semidefinite. The finite covariance identity then yields its \(n\)-linear variance with bounded remainder. Finally, the multivariate central limit theorem for bounded stationary 3-dependent vectors (by applying the scalar theorem to every coefficient vector) and Cramér–Wold show \(Z_n/\sqrt n\Rightarrow N_{24}(0,\Gamma)\), with exactly 18 nonzero covariance directions.

## Verification

The exact reconstruction of the \(24\times24\) rational covariance limit and the modular minor and kernel certificates is independently replayable with `python3 verify.py`. The program also exhaustively enumerates all permutations of sizes \(4,5,6,7\) and verifies every entry of the finite-sample covariance matrix by exact integer cross-multiplication (\(4\times576=2304\) checks). Its only dependencies are Python standard-library modules and the bundled `COVARIANCE_MATRIX.json`; no external data or computer algebra package is required. The checker returns `VERIFY_OK` on success. These finite computations certify exactly specified rational and integer identities; the asymptotic statements additionally use the explicit 3-dependence argument and its standard central limit theorem.

## Relationship to prior work

Bandt and Shiha (2007) establish foundational ordinal-pattern probabilities in time series. Janson, Nakamura, and Zeilberger (2013) examine joint statistics for **ordinary nonconsecutive subsequence patterns**; the covariance degeneracy mechanisms for their normalization do not directly determine the kernel for length-four **consecutive** windows. Crane and DeSalvo (2015) analyze occurrence and avoidance probabilities, including consecutive patterns, but not the complete 24-category covariance nullspace. Janson (2021/2022), §14 and Remark 14.2, proves constrained-pattern central limit theorems and explicitly proposes characterization of degenerate linear combinations as an open problem; its general theorem does not supply this length-four kernel. Bandt (2023) computes the complete six-category length-three picture and discusses two selected length-four contrasts, while explicitly identifying full length-four analysis as a next step. Weiß and collaborators (2022) study ordinal-pattern serial-independence tests; the available comparative source discusses selected length-four contrasts, not the full kernel, but the complete primary text was not inspected. The distinct earlier result for length-three consecutive patterns does not settle the present length-four statement. Known universal balance relations imply some kernel directions; the exact rank certificate proves there are **no additional** asymptotically degenerate directions under the independent uniform null.

## Limitations

The proof does not claim that the 18 positive eigenvalues are equal, provide an explicit closed form for them, or establish chi-square calibration in finite samples. The Gaussian law is asymptotic; fixed-size exhaustive verification does not alone prove it. The priority comparison is based on the listed inspected work and searches, and does not exclude an implicit equivalent in older order-pattern test literature, especially sources not fully available for inspection. This is not an independent audit or external mathematical certification.

## References

1. C. Bandt and F. Shiha, "Order Patterns in Time Series," *Journal of Time Series Analysis* 28 (2007), 646–665, doi:10.1111/j.1467-9892.2007.00528.x (first published 19 February 2007).
2. S. Janson, B. Nakamura, and D. Zeilberger, "On the Asymptotic Statistics of the Number of Occurrences of Multiple Permutation Patterns," arXiv:1312.3955 (2013).
3. H. Crane and S. DeSalvo, "Pattern Avoidance for Random Permutations," arXiv:1509.07941 (2015).
4. S. Janson, "Asymptotic normality for m-dependent and constrained U-statistics, with applications to pattern matching in random strings and permutations," arXiv:2106.09401, §14 and Remark 14.2 (2021–2022).
5. C. Bandt, "Statistics and contrasts of order patterns in univariate time series," *Chaos* 33 (2023), 033124, doi:10.1063/5.0132602.
6. C. H. Weiß, M. Ruiz Marín, K. Keller, and M. Matilla-García, "Non-parametric analysis of serial dependence in time series using ordinal patterns," *Computational Statistics & Data Analysis* 168 (2022), doi:10.1016/j.csda.2021.107381.

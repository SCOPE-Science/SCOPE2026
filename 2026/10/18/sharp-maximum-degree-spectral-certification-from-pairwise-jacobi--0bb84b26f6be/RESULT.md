# Sharp maximum-degree spectral certification from pairwise Jacobi scores

## Finding

The pairwise perturbation-aware Jacobi score certifies an **optimal, dimension-free eigenvalue error** when the residual off-diagonal support is sparse. Let \(A=(a_{ij})\) be Hermitian of order \(n\). Put \(d_i=a_{ii}\), and let \(\Delta\) denote the maximum degree of the undirected graph having an edge \(\{i,j\}\) precisely when \(a_{ij}\ne0\). Define
\[
s_{ij}(A)=\frac{\sqrt{(d_i-d_j)^2+4|a_{ij}|^2}-|d_i-d_j|}{2}.
\]
If \(s_{ij}(A)\le\varepsilon\) for every pair and \(\varepsilon>0\), then the eigenvalues and diagonal entries, both ordered nonincreasingly, obey
\[
\boxed{\ \max_{1\le k\le n}|\lambda_k(A)-d_{(k)}|\le\Delta^2\varepsilon.\ }
\]
When \(\Delta=0\), the two ordered lists agree exactly. For every fixed integer \(\Delta\ge1\), no uniformly smaller multiplier can replace \(\Delta^2\), even for positive-definite matrices.

The improvement is structural: in a banded example with maximum off-diagonal degree at most two, the certified absolute eigenvalue error is at most \(4\varepsilon\) regardless of the matrix size. No individual spectral gaps or bounds on the sizes of its diagonal entries are required.

## Assumptions and scope

The matrix is an arbitrary finite Hermitian matrix, including matrices with repeated diagonal entries, mixed signs, disconnected support, or positive definiteness. Scores are computed on the **present** matrix in exact arithmetic. A zero off-diagonal entry has score zero, including when its two diagonal entries coincide. There are no assumptions on how this matrix was generated. The theorem also applies to real symmetric matrices and is invariant under adding a scalar multiple of the identity.

Here \(\varepsilon>0\). The zero-tolerance case follows directly: all pair scores then vanish, so all off-diagonal entries are zero. The proof relies on the **maximum degree of the current support graph**, not that of an initial matrix before any rotations.

## Proof

**Step 1: translate the local impact bound.** Write \(g_{ij}=|d_i-d_j|\) and \(b_{ij}=|a_{ij}|\). Squaring two nonnegative quantities gives the exact equivalence
\[
s_{ij}\le\varepsilon\quad\Longleftrightarrow\quad
b_{ij}^2\le\varepsilon(g_{ij}+\varepsilon).
\tag{1}
\]
This holds also when \(g_{ij}=0\) and includes vanishing entries.

**Step 2: control the largest eigenvalue using edgewise positive-semidefinite matrices.** Suppose \(\Delta\ge1\). Set \(t=\max_i d_i\), \(u_i=t-d_i\ge0\), and \(C=\Delta^2\varepsilon\). We show \(Q=(t+C)I-A\succeq0\). For every edge \(\{i,j\}\), form a Hermitian matrix supported on coordinates \(i,j\), with its nonzero block equal to
\[
Q^{(ij)}=\begin{pmatrix}
(C+u_i)/\Delta&-a_{ij}\\
-\overline{a_{ij}}&(C+u_j)/\Delta
\end{pmatrix}.
\]
Let \(h=|u_i-u_j|\) and \(v=\min(u_i,u_j)\). The product of the diagonal entries satisfies
\[
\frac{(C+u_i)(C+u_j)}{\Delta^2}
=\frac{(C+v)(C+v+h)}{\Delta^2}
\ge\frac{C(C+h)}{\Delta^2}
=\Delta^2\varepsilon^2+\varepsilon h
\ge\varepsilon(\varepsilon+h)
\ge |a_{ij}|^2,
\]
where the final inequality is (1). Hence every \(Q^{(ij)}\) is positive semidefinite, including its zero determinant boundary.

The off-diagonal entries of their sum equal those of \(Q\). At vertex \(i\), their diagonal sum is \(\deg(i)(C+u_i)/\Delta\), which does not exceed the target \(C+u_i\). Therefore
\[
Q=\sum_{\{i,j\}\in E(G)}Q^{(ij)}+
\operatorname{diag}\!\left((1-\deg(i)/\Delta)(C+u_i)\right)\succeq0.
\]
Consequently \(\lambda_{\max}(A)\le\max_i d_i+C\). Applying the same argument to \(-A\) gives \(\lambda_{\min}(A)\ge\min_i d_i-C\). Both arguments persist under passing to any principal submatrix, because its maximum degree is at most \(\Delta\).

**Step 3: match every ordered eigenvalue.** Sort the diagonal entries \(d_{(1)}\ge\cdots\ge d_{(n)}\), keeping any fixed permutation among ties. For each \(k\), the principal submatrix on the \(n-k+1\) lowest-diagonal coordinates has largest eigenvalue at most \(d_{(k)}+C\). Cauchy interlacing places \(\lambda_k(A)\) below this largest eigenvalue. The principal submatrix on the \(k\) highest-diagonal coordinates has smallest eigenvalue at least \(d_{(k)}-C\); interlacing places \(\lambda_k(A)\) above it. Combining these two inequalities gives the asserted error for every \(k\).

**Step 4: show the degree-squared multiplier is sharp.** Fix any integer \(\Delta\ge1\), \(\varepsilon>0\), and \(H>0\). Let \(J\) be the \(\Delta\)-by-\(\Delta\) all-ones matrix, and put
\[
A_H=\begin{pmatrix}
H I_\Delta&z_H J\\ z_H J&0_\Delta
\end{pmatrix},\qquad z_H=\sqrt{\varepsilon(H+\varepsilon)}.
\]
Its support graph is the complete bipartite graph \(K_{\Delta,\Delta}\), hence has maximum degree exactly \(\Delta\). Every nonzero edge joins diagonals differing by \(H\), and its score equals \(\varepsilon\) exactly, since \(\sqrt{H^2+4z_H^2}=H+2\varepsilon\). The top eigenvalue is
\[
\lambda_{\max}(A_H)=\frac{H+\sqrt{H^2+4\Delta^2\varepsilon(H+\varepsilon)}}{2}.
\]
The largest diagonal is \(H\), and direct rationalization yields
\[
\lim_{H\to\infty}\frac{\lambda_{\max}(A_H)-H}{\varepsilon}=\Delta^2.
\]
For \(\Delta=1\) equality holds for every \(H>0\); for larger degrees the limit suffices to rule out a smaller uniform constant. Adding a sufficiently large scalar identity matrix makes \(A_H\) positive definite without changing the scores or eigenvalue-minus-diagonal differences. This proves optimality also within the positive-definite class.

## Verification

The companion `verify.py` checks the edge-score implication, all ordered eigenvalue bounds on 5,693 reproducibly sampled finite instances, and the complete-bipartite near-extremizers. It uses deterministic pseudorandom sampling and requires NumPy. Executing it is a **finite sanity check**, not an exhaustive or infinite-dimensional proof. The proof above is independent of computational sampling.

## Relationship to prior work

Shao and Nakatsukasa, *Accelerating preconditioned Jacobi methods via perturbation-inspired pivoting* (first publicly available July 25, 2026), define the same local impact score for real symmetric Jacobi pivoting. Their Theorem 1 proves a general accuracy estimate of \(2n(n-1)\varepsilon\) for ordered diagonal/eigenvalue differences. The present result instead gives a **sharp degree-dependent bound** \(\Delta^2\varepsilon\), for every Hermitian matrix, with a complete extremal family. The earlier dimension-dependent bound does not imply this claim when \(n\) grows but \(\Delta\) remains bounded.

The score derives from the classical Li–Li off-diagonal block perturbation estimate. Li and Li's matrix block theorem controls eigenvalue changes in terms of a block-coupling operator norm and a spectral gap; the score alone is their two-coordinate specialization. The 2012 work of Li, Nakatsukasa, Truhar and Wang refines sensitivity for a specified multiple eigenvalue under graded block perturbations. Neither of these formulations, as inspected, supplies the universal all-index maximum-degree certification and its optimality construction. The new argument is an edgewise positive-semidefinite decomposition plus interlacing, not an appeal to a stochastic or approximate Jacobi execution.

## Limitations

The statement is deterministic and exact-arithmetic. A practical computed score requires suitable rounding-error safeguards; none are analyzed here. Jacobi rotations ordinarily modify matrix sparsity, so a sparsity assumption on an **input** matrix does not license using its original degree at a later iterate. The theorem does not imply fewer Jacobi pivots, faster wall-clock execution, eigenvector accuracy, or a relative eigenvalue guarantee. Earlier equivalent estimates under another matrix-localization terminology cannot be ruled out conclusively by a finite bibliographic search; independent literature verification remains warranted.

## References

1. N. Shao and Y. Nakatsukasa, *Accelerating preconditioned Jacobi methods via perturbation-inspired pivoting*, arXiv:2607.23187v1 (July 25, 2026), especially Section 3.1, Theorem 1. https://arxiv.org/abs/2607.23187
2. C.-K. Li and R.-C. Li, *A note on eigenvalues of perturbed Hermitian matrices*, Linear Algebra and its Applications **395** (2005), 183–190. doi:10.1016/j.laa.2004.08.026. Corrected author preprint arXiv:2508.08203. https://arxiv.org/abs/2508.08203
3. R.-C. Li, Y. Nakatsukasa, N. Truhar and W.-G. Wang, *Perturbation of multiple eigenvalues of Hermitian matrices*, MIMS EPrint 2012.17 (2012), https://eprints.maths.manchester.ac.uk/1765/
4. N. J. Higham, *A Survey of Componentwise Perturbation Theory*, Proceedings of Symposia in Applied Mathematics **48** (1994), 49–77, https://eprints.maths.manchester.ac.uk/651/ .

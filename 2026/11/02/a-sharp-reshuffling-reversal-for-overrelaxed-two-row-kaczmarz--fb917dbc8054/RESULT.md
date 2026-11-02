# A sharp reshuffling reversal for overrelaxed two-row Kaczmarz

## Finding
Let \(u,v\in\mathbb R^2\) be linearly independent unit row normals with \(\rho=|u^\top v|\in(0,1)\). On any consistent two-equation linear system having these normals, start from a deterministic solution-error vector \(e\in\mathbb R^2\) and use the same relaxation \(\alpha\in(0,2)\) on every Kaczmarz update. Compare two consecutive row updates sampled independently and uniformly **with replacement** (IID) against a uniformly random order of the two distinct rows **without replacement** (RR).

Write \(E_{\mathrm I}(e)\) and \(E_{\mathrm R}(e)\) for the respective expected squared Euclidean error after these two updates. Orient \(v\) so that \(u^\top v=\rho>0\), and set \(w_+=u+v\), \(w_-=u-v\). There is an exact self-adjoint comparison operator \(D\), defined by
\[
E_{\mathrm I}(e)-E_{\mathrm R}(e)=e^\top D e,
\]
whose orthogonal eigenvectors are \(w_+\) and \(w_-\), with eigenvalues
\[
\lambda_+=\frac{\alpha^2(2-\alpha)}4(1-\rho^2)[2-\alpha(1+\rho)],\qquad
\lambda_-=\frac{\alpha^2(2-\alpha)}4(1-\rho^2)[2-\alpha(1-\rho)].
\]
Therefore RR has no larger two-update expected squared error **for every deterministic initial error** precisely when
\[
0<\alpha\le\frac{2}{1+\rho}.
\]
The comparison is strict for every nonzero error below this threshold; at equality, the tie directions are exactly the multiples of \(u+v\). Above this threshold and below \(2\), the advantage reverses on \(u+v\) but still favors RR on \(u-v\). In particular, neither sampling scheme dominates the other on all initial directions.

A rational witness takes \(u=(1,0)^\top\), \(v=(3/5,4/5)^\top\), \(\alpha=3/2\), and \(e=(2,1)^\top\). It has \(\rho=3/5\), and the exact expectations are
\[
E_{\mathrm I}(e)=\frac{161}{100},\qquad E_{\mathrm R}(e)=\frac{197}{100},
\]
so reshuffling is worse by \(9/25\) after one epoch, although both values are below the initial squared error \(5\). For every \(\rho\in(0,1)\) and \(0<\alpha<2\), **both** methods converge geometrically on continued use: IID per-step in mean square, and RR by a deterministic per-epoch contraction. The reversal is therefore a performance separation between convergent methods, not an instability artifact.

## Assumptions and scope
Rows are real, normalized, nonparallel, and there are exactly two unknowns and exactly two consistent equations. An update is
\[
x\longmapsto x-\alpha(u_i^\top x-b_i)u_i.
\]
For IID, each of the two selections is independent and uniform on the two rows. For RR, one of the orders \((u,v)\) or \((v,u)\) is chosen with probability \(1/2\); subsequent epochs may use fresh independent permutations. Initial error is deterministic and arbitrary. The criterion concerns the squared **solution-error norm** after exactly two sequential updates, not the residual norm or a stationary noise floor. The strict interval \(0<\alpha<2\) is essential to the geometric convergence assertion.

## Proof
Let \(P=uu^\top\), \(Q=vv^\top\) be rank-one orthogonal projections, and set \(B=I-\alpha P\) and \(C=I-\alpha Q\). These symmetric matrices propagate the error after one row action. With-replacement sampling produces the four ordered products with equal probability. Therefore its two-step expected-error matrix is
\[
M_{\mathrm I}=\frac14\bigl(B^4+C^4+BC^2B+CB^2C\bigr),
\]
whereas the random permutation has expected-error matrix
\[
M_{\mathrm R}=\frac12\bigl(BC^2B+CB^2C\bigr).
\]
In each case the expected squared norm is the quadratic form of that matrix in \(e\). Thus \(D=M_{\mathrm I}-M_{\mathrm R}\) equals
\[
D=\frac14\bigl(B^4+C^4-BC^2B-CB^2C\bigr).
\]
Put \(\beta=\alpha(2-\alpha)\). Since \(P^2=P\), \(Q^2=Q\), we have \(B^2=I-\beta P\) and \(C^2=I-\beta Q\). Moreover \(PQP=\rho^2P\) and \(QPQ=\rho^2Q\). Multiplication, without any commutativity assumption on \(P,Q\), now gives
\[
\boxed{D=\frac\beta4\left[(\beta+\alpha^2\rho^2)(P+Q)-2\alpha(PQ+QP)\right].}
\]
For clarity, the cross terms follow from
\[
BC^2B=B^2-\beta BQB
=B^2-\beta\bigl(Q-\alpha(PQ+QP)+\alpha^2\rho^2P\bigr),
\]
and the analogous formula with \(P\) and \(Q\) exchanged.

Set \(S=P+Q\). The relation \(PQ+QP=S^2-S\) holds because \(P,Q\) are projections. With \(u^\top v=\rho\), direct application gives
\[
S(u+v)=(1+\rho)(u+v),\qquad
S(u-v)=(1-\rho)(u-v).
\]
These two vectors are nonzero, orthogonal, and span \(\mathbb R^2\). Substituting the eigenvalues of \(S\) into the boxed expression for \(D\) and factoring yields exactly \(\lambda_+\) and \(\lambda_-\) in the finding.

For \(0<\alpha<2\), the prefactor \(\alpha^2(2-\alpha)(1-\rho^2)/4\) is positive. Also \(2-\alpha(1-\rho)>0\), hence \(\lambda_->0\). The other eigenvalue has the sign of \(2-\alpha(1+\rho)\). This proves the necessary-and-sufficient universal comparison, both equality classifications, and the direction-dependent reversal. The rational example is direct multiplication of the four two-step maps; its exact arithmetic is also checked by the accompanying script.

For completeness, geometric convergence is independent of the comparison. A single relaxed projection obeys
\[
\|(I-\alpha P)e\|^2=\|e\|^2-\beta(u^\top e)^2.
\]
IID selection therefore satisfies the conditional bound
\[
\mathbb E[\|e_{k+1}\|^2\mid e_k]\le
\left(1-\frac{\beta(1-\rho)}2\right)\|e_k\|^2,
\]
because the smallest eigenvalue of \(S\) is \(1-\rho\). The factor is strictly below one.

For RR, either two-row sweep \(CB\) or \(BC\) has operator norm strictly less than one. Indeed, each update is nonexpansive for \(0<\alpha<2\), and equality in \(\|CB e\|\le\|Be\|\le\|e\|\) for nonzero \(e\) would force \(u^\top e=0\) and \(v^\top Be=0\). The first equality gives \(Be=e\), hence \(v^\top e=0\) as well, contradicting linear independence. Compactness of the unit circle upgrades strictness to \(\|CB\|_2<1\). The reverse order is identical by swapping rows. A fixed maximum of their norms bounds every epoch, proving uniform geometric decay along every reshuffling realization.

## Verification
Running `python3 verify.py` uses only Python's standard library and checks 202 exact rational matrix, eigendirection, boundary-sign, and witness identities. The test sets contain six rational row angles and eight rational relaxation values, with explicit inspection of the reflection endpoint. Its output is `VERIFY_OK 202 exact rational matrix/eigenmode/witness checks`.

The finite tests are not an exhaustive proof for arbitrary real \(\rho\) or \(\alpha\); the proof above establishes the universally quantified identities and signs algebraically. In the independently reproducible rational witness, both comparison matrices are formed by averaging **all** four IID row sequences or both RR orders, not Monte Carlo samples.

## Relationship to prior work
Han and Xie establish linear convergence and a tight worst-order bound for standard, unrelaxed reshuffling Kaczmarz. Those results do not compare two-query expected squared errors at adjustable overrelaxation, nor do they yield the sign-changing eigendirection criterion. Recht and Ré formulated the matrix-product comparison motivating the general preference for reshuffling; Lai and Lim discuss its two-factor positive-semidefinite case and more general limitations. The elementary unrelaxed part of the present comparison is consistent with this established principle; the contribution is the **sharp extension into relaxed, potentially indefinite update operators**, including exact reversal inside the stable parameter interval. Ying and collaborators analyze constant-step reshuffling and steady-state stochastic gradients, while Safran and Shamir emphasize finite-epoch limitations under commuting quadratic terms. Neither result gives the present angle-dependent, noncommuting two-projection classification. A separate published two-row cyclic-overrelaxation calculation concerns deterministic sweep norms and asymptotic relaxation rather than IID-versus-permutation expectation matrices.

## Limitations
This is a two-row, two-update exact comparison for the Euclidean **solution-error norm**. It does not claim that IID becomes better at all later epochs, or for other initial-error orientations; above the threshold, advantage depends on the initial direction. It does not imply failure of reshuffling convergence, address inconsistent systems, more than two equations, other normalization choices, or noisy updates. Earlier specialized matrix-product inequalities could contain a differently phrased equivalent of the sharp threshold, so independent priority verification remains necessary.

## References
1. D. Han and J. Xie, *A simple linear convergence analysis of the randomized reshuffling Kaczmarz method*, arXiv:2410.01140, first submitted 2 October 2024. https://arxiv.org/abs/2410.01140
2. B. Recht and C. Ré, *Beneath the valley of the noncommutative arithmetic-geometric mean inequality: conjectures, case-studies, and consequences*, arXiv:1202.4184 (2012). https://arxiv.org/abs/1202.4184
3. Z. Lai and L.-H. Lim, *Recht–Ré Noncommutative Arithmetic-Geometric Mean Conjecture is False*, arXiv:2006.01510 (2020). https://arxiv.org/abs/2006.01510
4. B. Ying, K. Yuan, S. Vlaski, and A. H. Sayed, *Stochastic Learning under Random Reshuffling with Constant Step-sizes*, arXiv:1803.07964 (2018). https://arxiv.org/abs/1803.07964
5. I. Safran and O. Shamir, *Random Shuffling Beats SGD Only After Many Epochs on Ill-Conditioned Problems*, arXiv:2106.06880 (2021). https://arxiv.org/abs/2106.06880
6. *Exact finite-horizon cost of asymptotically optimal two-row Kaczmarz overrelaxation*, publicly available result, 2026. https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-exact-finite-horizon-cost-of-asymptotically-optimal-two-row-kacz--d549f7251aa1/RESULT.md

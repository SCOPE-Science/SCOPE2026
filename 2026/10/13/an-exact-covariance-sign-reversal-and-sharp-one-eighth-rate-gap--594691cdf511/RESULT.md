# An exact covariance-sign reversal and sharp one-eighth rate gap in two-coordinate randomized least squares

## Finding

For independent exact single-coordinate least-squares updates with two normalized, nonorthogonal columns, unequal sampling probabilities make the **population covariance between the preceding batch's restricted curvature and the current squared error eventually negative**. The exact long-run expected squared-error factor is slower than the factor obtained by naively substituting the mean restricted curvature, and their discrepancy has the sharp global supremum \(1/8\), even among matrices with condition number approaching one.

Specifically, let \(p\in(0,1)\), \(r\in(-1,0)\cup(0,1)\), and write
\[
\lambda_+(p,r)=\frac{1+\sqrt{(2p-1)^2+4p(1-p)r^4}}2,
\quad \rho_{\mathrm{av}}(p,r)=1-2p(1-p)(1-r^2).
\]
For every nonoptimal deterministic initial point, the ratio of consecutive expected squared errors tends to \(\lambda_+\). The curvature–error covariance is eventually strictly negative exactly when \(p\ne1/2\); when \(p=1/2\) it is zero at every step. Moreover,
\[
0\le \Delta(p,r):=\lambda_+(p,r)-\rho_{\mathrm{av}}(p,r)<\frac18,
\qquad\sup_{p,r}\Delta(p,r)=\frac18.
\]
Equality in the supremum is approached by \(p=1/4\), \(r\to0\) (or \(p=3/4\)). In this limit the two columns become orthogonal and the spectral condition number tends to one.

## Assumptions and scope

Let \(m\ge2\) and \(A=[a_1\ a_2]\in\mathbb R^{m\times2}\) have unit Euclidean-norm columns with \(r=a_1^{\mathsf T}a_2\) satisfying \(0<|r|<1\). For arbitrary \(b\in\mathbb R^m\), let \(x_{LS}\) be the unique least-squares minimizer. Start at any deterministic \(x^{(0)}\ne x_{LS}\). At each time \(k=0,1,\ldots\), independently choose index \(J_k=1\) with probability \(p\in(0,1)\) and \(J_k=2\) otherwise, and perform the **exact** one-coordinate least-squares minimization
\[
x^{(k+1)}=x^{(k)}-e_{J_k}a_{J_k}^{\mathsf T}A(x^{(k)}-x_{LS}).
\]
Define the error residual \(z_k=A(x^{(k)}-x_{LS})\) and \(f_k=\|z_k\|_2^2\). Its expectation is \(F_k=\mathbb E f_k\). These are squared *error residuals*, not the full (possibly nonzero) least-squares residual norm \(\|Ax^{(k)}-b\|^2\).

For the one-coordinate case of the restricted-subspace curvature of Xie and Yang, choose any invertible diagonal auxiliary scaling \(S\). As both columns are unit normalized, their definition reduces to \(M^2=\operatorname{diag}(p,1-p)\), independently of \(S\). The curvature associated with the previously sampled coordinate is
\[
\xi_1=(1-p)(1-r^2),\qquad \xi_2=p(1-r^2),\qquad
\bar\xi=\mathbb E\xi_{J_{k-1}}=2p(1-p)(1-r^2).
\]
All covariance claims below use the **population** covariance over independent trajectories at fixed iteration \(k\ge1\); sample covariance over finitely many trajectories is a separate random quantity.

## Proof

**1. Restricted curvature is exact in dimension two.**  For any diagonal \(S=\operatorname{diag}(s_1,s_2)\) with nonzero entries, the one-coordinate batch norm bound gives \(R_{S;1}=\operatorname{diag}(s_1^2,s_2^2)\) for normalized columns. Thus \(M^2=S^{\mathsf T}R_{S;1}^{-1}\operatorname{diag}(p,1-p)S=\operatorname{diag}(p,1-p)\), independent of \(S\). Define \(P_i=I-a_ia_i^{\mathsf T}\) on \(\operatorname{range}(A)\). The update is \(z_{k+1}=P_{J_k}z_k\); for \(k\ge1\), \(z_k\perp a_{J_{k-1}}\). The orthogonal complement of each column in the two-dimensional range is one-dimensional, so its restricted curvature equals the squared length of the other column's projection multiplied by its sampling probability. That length squared is \(1-r^2\). Thus the claimed formulas for \(\xi_1\) and \(\xi_2\) are exact; there is no hidden strict inequality in the restricted-subspace step.

Repeating the same index leaves \(f_k\) unchanged, whereas switching indices multiplies \(f_k\) by \(r^2\). Therefore, conditionally on the trajectory through iteration \(k-1\),
\[
\mathbb E[f_{k+1}\mid J_0,\ldots,J_{k-1}]
=(1-\xi_{J_{k-1}})f_k.
\]
Consequently,
\[
F_{k+1}=(1-\bar\xi)F_k-
\operatorname{Cov}(\xi_{J_{k-1}},f_k)
=\rho_{\mathrm{av}}F_k-
\operatorname{Cov}(\xi_{J_{k-1}},f_k).
\tag{1}
\]

**2. Exact two-state second-moment evolution.** Set
\[
u_{k,i}=\mathbb E\bigl[f_k\mathbf 1_{\{J_{k-1}=i\}}\bigr],\qquad k\ge1.
\]
Condition on the new index and the previous index. The preceding repetition/switching rule yields
\[
\begin{pmatrix}u_{k+1,1}\\u_{k+1,2}\end{pmatrix}
=T\begin{pmatrix}u_{k,1}\\u_{k,2}\end{pmatrix},\qquad
T=\begin{pmatrix}p&pr^2\\(1-p)r^2&1-p\end{pmatrix}.
\tag{2}
\]
The trace of \(T\) equals one, and its determinant is \(p(1-p)(1-r^4)\). Its two real eigenvalues are
\[
\lambda_{\pm}=\frac{1\pm\sqrt{(2p-1)^2+4p(1-p)r^4}}2.
\]
Because \(p\in(0,1)\) and \(0<r^2<1\), the matrix \(T\) has strictly positive entries. The initial two-state vector \(u_1\) is nonzero and nonnegative for every \(z_0\ne0\): otherwise both independent orthogonal projections would annihilate \(z_0\), which is impossible when \(a_1,a_2\) are linearly independent. Perron–Frobenius therefore gives
\[
\lim_{k\to\infty}\frac{F_{k+1}}{F_k}=\lambda_+,
\qquad F_k=u_{k,1}+u_{k,2}>0.
\tag{3}
\]

**3. The covariance's sharp sign.** Combine (1) and (3) to obtain
\[
\lim_{k\to\infty}
\frac{\operatorname{Cov}(\xi_{J_{k-1}},f_k)}{F_k}
=\rho_{\mathrm{av}}-\lambda_+.
\tag{4}
\]
Put \(t=4p(1-p)\in(0,1]\) and \(v=r^2\in(0,1)\). Then
\[
2\Delta=\sqrt{1-t+tv^2}-(1-t+tv).
\]
Both expressions being compared are nonnegative, and their squared difference is the identity
\[
1-t+tv^2-(1-t+tv)^2=t(1-t)(1-v)^2.
\]
Thus \(\Delta>0\) for \(t<1\), equivalently \(p\ne1/2\), and \(\Delta=0\) for \(p=1/2\). Equation (4) proves eventual strict covariance negativity in the first case. In the second case \(\xi_1=\xi_2\), so the covariance vanishes for every \(k\ge1\).

**4. Sharp maximal gap.** For fixed \(t\in(0,1]\),
\[
\frac{\partial(2\Delta)}{\partial v}
=t\left(\frac{v}{\sqrt{1-t+tv^2}}-1\right)\le0,
\]
since \(1-t+tv^2\ge v^2\). Hence the maximum over the open correlation interval is approached as \(v\downarrow0\). Let \(z=\sqrt{1-t}\). Then
\[
\sup_{0<v<1}\Delta=\frac{z-z^2}{2}\le\frac18,
\]
and \(z=1/2\) gives equality for the limiting problem, i.e. \(t=3/4\), \(p=1/4\) or \(3/4\). For every admissible \(v>0\), the strict inequality \(\Delta<1/8\) holds. The two singular values of \(A\) are \(\sqrt{1\pm|r|}\), so its condition number \(\sqrt{(1+|r|)/(1-|r|)}\to1\) as \(r\to0\). This completes the theorem.

## Verification

The standalone standard-library file `verify.py` enumerates actual sequences of independently sampled coordinate projections using exact rational arithmetic, tests the two-state recurrence against exact enumeration, checks the conditional covariance identity, and compares its Perron eigenvalue and the sharp bound with a 19,900-point numerical parameter grid. It uses rational two-column matrices based on Pythagorean triples. To replay, run `python verify.py` with Python 3.10 or newer. An expected success marker is `VERIFY_OK`. Enumeration checks finitely many instances and does not prove the all-parameter theorem, which follows from the algebra above.

## Relationship to prior work

Xie and Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685v1 (public 2026-10-03), introduce the motivating arbitrary-distribution RBSCD method and a restricted-subspace curvature \(\xi_\tau\). Their Theorem 4.3 requires a **nonnegative covariance** between that curvature and the current squared error before replacing an iterate-dependent contraction by an average-curvature factor. Their Remark 4.4 reports predominantly positive sampled covariances on selected larger numerical problems. The present result does **not** challenge their conditional theorem: it determines exactly the opposite population sign for all asymptotically late steps in the particular two-coordinate, biased-sampling class, and supplies a sharp quantitative consequence.

Classical randomized Gauss–Seidel/coordinate-descent analyses, including Ma–Needell–Ramdas (arXiv:1503.08235) and Qu–Richtárik (arXiv:1412.8063), establish global expected-error or arbitrary-sampling bounds, rather than the exact two-state covariance and sharp 1/8 gap for the new restricted curvature. An independently published study of delayed, **uniformly sampled** two-coordinate Gauss–Seidel gives a different diagonally scaled second-moment recurrence and explicitly excludes biased coordinate sampling. Separate optimal-coordinate-sampling work gives the best **worst-case one-step** energy contraction, rather than the present long-time covariance comparison. The exact biased two-state reduction follows from elementary projection geometry and Perron–Frobenius theory; no claim is made that these standard tools are new.

## Limitations

The theorem covers exactly two normalized, linearly independent columns with nonzero correlation, positive fixed iid coordinate probabilities, and exact single-coordinate projections. It concerns asymptotic **expected squared error**, not typical pathwise contraction, a finite-step sign guarantee, a general block-sampling theorem, or computation time. At exactly zero correlation the positive-matrix Perron argument can fail for special initial conditions, which is why the supremum is stated as an unattained limit. The sign result concerns population covariance; finite-sample covariance may fluctuate. An equivalent two-state reduction may appear under different terminology in older Markovian projection or iterative-linear-solver literature; independent literature review is warranted.

## References

1. D.-Y. Xie and X. Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685v1, first public 2026-10-03. https://arxiv.org/html/2610.04685v1
2. A. Ma, D. Needell and A. Ramdas, *Convergence properties of randomized extended Gauss–Seidel and Kaczmarz methods*, arXiv:1503.08235. https://arxiv.org/abs/1503.08235
3. Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling II: Expected Separable Overapproximation*, arXiv:1412.8063. https://arxiv.org/abs/1412.8063
4. *Exact delay-distribution law for two-coordinate randomized Gauss–Seidel*, published mathematical finding (2026-09-20). https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-exact-stochastic-delay-law-randomized-gauss-seidel--9ae0040f2dac
5. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, published mathematical finding (2026-09-20). https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995

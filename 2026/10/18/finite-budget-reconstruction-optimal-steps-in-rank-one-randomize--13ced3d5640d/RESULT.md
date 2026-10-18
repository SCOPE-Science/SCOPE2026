# Finite-budget reconstruction-optimal steps in rank-one randomized block descent

## Finding
For a single observation measuring the sum of \(b\ge 2\) unknown scalar blocks, randomized block-coordinate descent has an exactly solvable reconstruction-versus-residual tradeoff. With \(N\ge1\) independent, uniformly sampled updates and deterministic steps, the unique schedule minimizing squared distance to the minimum-norm solution is
\[
\eta_k=\frac1{N+b-1-k},\qquad k=0,\ldots,N-1,
\]
and its minimum expected squared distance is
\[
\min_{\eta_0,\ldots,\eta_{N-1}}\mathbb E\|x_N-x^\dagger\|_2^2
=\frac{y^2(b-1)}{b(N+b-1)}.
\]
**The optimal schedule does not interpolate the noiseless observation at the allotted stopping time**: the final residual is \(y(b-1)/(N+b-1)\). Exact interpolation at the same horizon instead incurs the larger sharp risk \(y^2(b-1)/(bN)\), attained by \(\eta_k=1/(N-k)\).

For every constant \(0<\eta<2\), the observation residual decays geometrically, but the mean squared reconstruction error approaches a strictly positive floor. Its exact one-step change has the sign of \(b\eta-2\), revealing a sharp reconstruction-monotonicity boundary at \(\eta=2/b\).

## Assumptions and scope
Fix an integer \(b\ge2\), a nonzero real observation \(y\), and the row operator \(A=(1,\ldots,1)\in\mathbb R^{1\times b}\). Let the independent indices \(I_0,I_1,\ldots\) be uniform on \(\{1,\ldots,b\}\), and initialize \(x_0=0\). For a deterministic real step sequence \(\eta_k\), make the coordinate update
\[
x_{k+1}=x_k+\eta_k(y-Ax_k)e_{I_k}.
\]
The unique minimum-Euclidean-norm solution of \(Ax=y\) is \(x^\dagger=(y/b)\mathbf 1\). Reconstruction risk means \(\mathbb E\|x_N-x^\dagger\|_2^2\), **not** residual error or optimization objective. The claimed finite-budget optimum ranges over all real deterministic step schedules, including schedules with intermediate zero residuals or sign-changing residuals. Independent uniform coordinate sampling is essential. Optimization occurs over schedules, not selection distributions, adaptive policies, or estimators using the known closed-form pseudoinverse.

## Proof
Write \(r_k=y-Ax_k\). Summing the chosen coordinate update gives the deterministic recursion
\[
r_{k+1}=(1-\eta_k)r_k,\qquad r_0=y.
\]
Define the effective update weights \(w_k=\eta_k\prod_{j=0}^{k-1}(1-\eta_j)\) and total weight \(W=\sum_{k=0}^{N-1}w_k=1-r_N/y\), with empty products equal to one. Then
\[
x_N=y\sum_{k=0}^{N-1}w_ke_{I_k},\qquad
\mathbb E x_N=\frac{yW}{b}\mathbf 1.
\]
Independence of the coordinates yields the **exact** covariance
\[
\operatorname{Cov}(x_N)=y^2\left(\sum_{k=0}^{N-1}w_k^2\right)
\left(\frac1bI_b-\frac1{b^2}\mathbf 1\mathbf 1^{\mathsf T}\right).
\]
Consequently, the bias-variance decomposition is an identity for every deterministic schedule:
\[
\boxed{\frac{\mathbb E\|x_N-x^\dagger\|_2^2}{y^2}
=\frac{(1-W)^2}{b}+\frac{b-1}{b}\sum_{k=0}^{N-1}w_k^2.}
\tag{1}
\]
Cauchy–Schwarz gives \(\sum_kw_k^2\ge W^2/N\), with equality precisely when all weights equal \(W/N\). Minimizing the resulting strictly convex scalar quadratic
\[
\frac{(1-W)^2}{b}+\frac{b-1}{bN}W^2
\]
over all real \(W\) gives the unique optimum \(W=N/(N+b-1)\), with every \(w_k=1/(N+b-1)\), and minimum \((b-1)/[b(N+b-1)]\). For these weights the residual before update \(k\) is \(r_k/y=1-k/(N+b-1)>0\), so \(\eta_k=w_k/(r_k/y)=1/(N+b-1-k)\). This proves attainment and uniqueness of the **actual step schedule**, not just uniqueness of the effective weights. In particular \(0<\eta_k\le1/b\), while \(r_N=y(b-1)/(N+b-1)\ne0\).

If interpolation is demanded for every index sequence, it is equivalent to \(r_N=0\), hence \(W=1\). Identity (1) and Cauchy–Schwarz show that the least possible risk is \(y^2(b-1)/(bN)\). Equality forces \(w_k=1/N\) and, by the same residual recovery, the unique steps \(\eta_k=1/(N-k)\), whose last step equals one. This includes schedules that otherwise have an earlier zero residual: those assign subsequent zero weights and cannot attain equality for \(N>1\).

For constant \(0<\eta<2\), put \(q=1-\eta\). Then \(w_k=\eta q^k\) and \(1-W=q^N\). Substituting the geometric sum in (1) proves
\[
\mathbb E\|x_N-x^\dagger\|_2^2
=\frac{y^2}{b}q^{2N}
+\frac{y^2(b-1)\eta}{b(2-\eta)}(1-q^{2N}).
\tag{2}
\]
Because \(|q|<1\), the terminal risk is \(y^2(b-1)\eta/[b(2-\eta)]>0\), even though \(r_N=yq^N\to0\). Subtraction of (2) at successive horizons gives
\[
\mathbb E\|x_{N+1}-x^\dagger\|_2^2-\mathbb E\|x_N-x^\dagger\|_2^2
=-\frac{y^2\eta(2-b\eta)}b q^{2N}.
\tag{3}
\]
Thus reconstruction risk decreases whenever \(\eta<2/b\) and the residual has not already reached zero, is constant at \(\eta=2/b\), and increases whenever \(\eta>2/b\) and the residual is nonzero. For \(\eta=1\), residual zero after the first update explains the permitted subsequent equality. All boundaries are included explicitly.

## Verification
A standalone standard-library Python checker (`verify.py`) exhaustively enumerates coordinate sequences for \(b\in\{2,3,4\}\) and short horizons, using exact rational arithmetic. It compares the empirical enumeration (which is exact, not Monte Carlo) against the optimal-schedule identity, the exact-interpolation schedule, and formula (2) for several rational constant steps. It also independently checks the one-step sign identity (3) and that the proposed optimal schedule has strictly positive residual. The code checks finite instances; the proofs of the statements for every \(b,N\) are the algebraic arguments above.

## Relationship to prior work
Jin and Liu (2024) introduce the randomized block-coordinate algorithm for ill-posed inverse problems, including noisy-data stability estimates, weak convergence and a stronger theorem under a full-column-rank structural assumption. Their Algorithm 1 supplies the update here. The present result concerns a rank-deficient one-row example, the exact expected Euclidean distance to the minimum-norm solution, and the finite-budget choice of a **nonconstant** deterministic step schedule. Neither their residual-oriented convergence result nor their step-size bound gives this sharp schedule or its noninterpolation property.

Ma, Needell and Ramdas (2015), especially Section 3.3, explain why ordinary randomized Gauss–Seidel on underdetermined systems may reach a feasible solution without reaching the least-norm solution, motivating an extended method. That known qualitative nonuniqueness phenomenon is **not claimed as new**. The new finite-budget equality, unique schedule, terminal residual and sharp mean-square monotonicity formula do not follow from the inspected statements. The related stochastic-optimization literature can contain equivalent risk/weight optimizations under other terminology; no search establishes absolute novelty.

## Limitations
The theorem requires a single identical-entry measurement, exact arithmetic, a fixed horizon, deterministic steps and independent uniformly sampled coordinates. It does not extend the optimal schedule to a general inverse operator, nonuniform sampling, adaptive steps, arbitrary stochastic gradient noise, or unknown minimum-norm target. The optimal expected **reconstruction** criterion presumes the minimum-norm solution as the target; reducing the measured residual alone is a different objective. The zero-residual exception in the monotonicity assertion must not be ignored. Finite enumeration is a reproducibility aid, not an infinite proof. The historical lower bound that ordinary coordinate descent need not approach the minimum-norm solution is acknowledged; the precise finite-budget risk-optimal schedule is the proposed contribution.

## References
1. Q. Jin and D. Liu, “Randomized block coordinate descent method for linear ill-posed problems,” arXiv:2405.13340v1, first posted 2024-05-22, Algorithm 1 and Section 2. `https://arxiv.org/html/2405.13340v1`.
2. A. Ma, D. Needell and A. Ramdas, “Convergence Properties of the Randomized Extended Gauss–Seidel and Kaczmarz Methods,” arXiv:1503.08235, 2015, Sections 3.3–4. `https://arxiv.org/pdf/1503.08235`.

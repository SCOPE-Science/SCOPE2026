# Sharp error–residual stability separation and near-doubling transients in doubly sampled block gradient descent

## Finding
For the uniform independent row-and-coordinate stochastic block-gradient update of Xia and Zhou, orthogonality of the columns does **not** make Euclidean solution-error monotonicity and physical-residual monotonicity equivalent. On real flat orthogonal-column systems, the two sharp universal one-step step-size ceilings are respectively
\[
\eta_{\rm err}=\frac{2m}{S_2},\qquad
\eta_{\rm res}=\frac{2m\sigma_{\min}^{2}}{S_4},\qquad
S_2=\sum_{j=1}^{n}\sigma_j^2,\quad S_4=\sum_{j=1}^{n}\sigma_j^4.
\]
The second ceiling is strictly smaller if the singular values are unequal. The unique step minimizing the worst-case one-step expected squared solution-error factor is \(\eta_*=m/S_2\). In the two-mode case, its physical squared-residual expectation already increases from the weak singular direction exactly when \(\kappa>\sqrt{1+\sqrt2}\), where \(\kappa\) is the singular-value ratio.

More strongly, for the two-by-two normalized Hadamard family and initial error in the weak singular direction, every iterate at this error-optimal step has expected squared physical residual less than twice its initial value, and this upper bound **two is sharp jointly over singular-value ratio and iteration index**. In fact, as \(\kappa\to\infty\), with \(k=\lfloor\kappa\rfloor\), the residual ratio tends to \(2\) while the expected squared solution error is nonincreasing at every iteration.

## Assumptions and scope
Let \(m\ge n\ge1\) be integers and let \(H\in\{-1,1\}^{m\times n}\) have pairwise orthogonal columns: \(H^{\mathsf T}H=mI_n\). For example, select columns of a Sylvester Hadamard matrix. Fix arbitrary \(\sigma_j>0\), set \(A=m^{-1/2}H\operatorname{diag}(\sigma_1,\ldots,\sigma_n)\), and take a consistent real system \(Ax=b\) with unique solution \(x^\dagger\). At each iteration independently choose \(i\) uniformly from \(\{1,\ldots,m\}\) and \(j\) uniformly from \(\{1,\ldots,n\}\), and perform precisely the unnormalized coordinate update
\[
x^+=x-\eta\,e_j A_{ij}(Ax-b)_i,\qquad \eta>0.
\]
Here \(e_j\) is a coordinate basis vector, unrelated to the error \(e=x-x^\dagger\). All sampling and expectations are over the indicated independent uniform choices; the matrix and step size are deterministic. Define \(r=Ae\), \(G=A^{\mathsf T}A=\operatorname{diag}(\sigma_j^2)\), \(\sigma_{\min}=\min_j\sigma_j\), and \(S_2,S_4\) as above. “One-step universal decrease” means conditional nonincrease for *every* deterministic starting error. “Mean-square convergence” means \(\mathbb E\|x_k-x^\dagger\|^2\to0\) for every fixed initial error. Statements concern exact arithmetic, exact consistent data, fixed positive step and fresh independent samples.

## Proof
**1. Exact conditional identities.** Since each \(A_{ij}^2=\sigma_j^2/m\) and \(A^{\mathsf T}A=G\), expanding \(e^+=e-\eta e_jA_{ij}r_i\) and averaging gives, for every deterministic \(e\),
\[
\mathbb E[\|e^+\|^2\mid e]
=\|e\|^2-\frac{\eta}{mn}\left(2-\frac{\eta S_2}{m}\right)e^{\mathsf T}Ge.\tag{1}
\]
Likewise \(r^+=r-\eta A_{\cdot j}A_{ij}r_i\). In its squared norm the negative cross term averages to \(-2\eta e^{\mathsf T}G^2e/(mn)\); the positive square term uses \(\|A_{\cdot j}\|^2=\sigma_j^2\) and averages to \(\eta^2S_4\|r\|^2/(m^2n)\). Thus
\[
\mathbb E[\|r^+\|^2\mid e]
=\|r\|^2-\frac{\eta}{mn}\left(2e^{\mathsf T}G^2e-\frac{\eta S_4}{m}e^{\mathsf T}Ge\right).\tag{2}
\]
No independence of components of the error is used.

**2. Exact sharp frontiers.** Since \(G\) is positive definite, (1) is strictly decreasing for each nonzero error exactly if \(0<\eta<2m/S_2\). At equality all conditional expected squared errors are unchanged. Above it they strictly increase for every nonzero error. Below the ceiling,
\[
\mathbb E\|e_{k+1}\|^2\le q_{\rm err}(\eta)\mathbb E\|e_k\|^2,
\quad q_{\rm err}(\eta)
=1-\frac{\eta(2-\eta S_2/m)\sigma_{\min}^2}{mn}<1.
\]
The factor is attained at one step by a smallest-singular-direction error. Hence the ceiling is also the exact global mean-square convergence frontier; at the ceiling the mean square is constant, and above it grows geometrically at least at a positive rate. Minimizing \(q_{\rm err}\) uniquely gives \(\eta_*=m/S_2\) and \(q_{\rm err}(\eta_*)=1-\sigma_{\min}^2/(nS_2)\).

Equation (2) is nonincreasing for all errors precisely when \(2G^2-(\eta S_4/m)G\succeq0\), equivalently \(0<\eta\le2m\sigma_{\min}^2/S_4\). At the strict interior it decreases for every nonzero error. Above this ceiling, an error aligned with any smallest-singular coordinate gives a strict physical-residual increase. Furthermore \(S_4-\sigma_{\min}^2 S_2=\sum_j\sigma_j^2(\sigma_j^2-\sigma_{\min}^2)\), so the two ceilings agree exactly in the equal-singular-value case. For an unequal spectrum there is a nonempty open interval of steps where mean-square solution error strictly decreases universally but the expected squared physical residual increases for some errors.

**3. Sharp two-mode threshold.** Take
\[
A_\kappa=2^{-1/2}\begin{pmatrix}\kappa&1\\\kappa&-1\end{pmatrix},
\quad e_0=(0,1)^{\mathsf T},\quad \kappa\ge1,
\quad \rho=\kappa^2,
\quad \eta_*=\frac{2}{\rho+1}.
\]
Equation (1) gives \(\mathbb E\|e_1\|^2/\|e_0\|^2=1-1/[2(\rho+1)]<1\). Equation (2) gives
\[
\frac{\mathbb E\|Ae_1\|^2}{\|Ae_0\|^2}
=1+\frac{\rho^2-2\rho-1}{2(\rho+1)^2}.\tag{3}
\]
The residual increase is strict exactly for \(\rho>1+\sqrt2\), equivalently \(\kappa>\sqrt{1+\sqrt2}\). For \(\kappa=2\) the error factor is \(9/10\), but the residual factor is \(57/50\).

**4. The sharp long transient.** For the same two-mode system, put \(u_k=\mathbb E[e_{k,1}^2]\) and \(y_k=\mathbb E[e_{k,2}^2]\); the row-sign cancellation and the same entrywise expansion yield the *exact* closed second-moment recursion
\[
\begin{pmatrix}u_{k+1}\\y_{k+1}\end{pmatrix}=
\begin{pmatrix}
1-\frac{\rho}{\rho+1}+\frac{\rho^2}{2(\rho+1)^2}&\frac{\rho}{2(\rho+1)^2}\\
\frac{\rho}{2(\rho+1)^2}&1-\frac1{\rho+1}+\frac1{2(\rho+1)^2}
\end{pmatrix}
\begin{pmatrix}u_k\\y_k\end{pmatrix},\quad(u_0,y_0)=(0,1).\tag{4}
\]
Write \(v_k=\rho u_k\), \(a_\rho=1-\rho/(\rho+1)+\rho^2/[2(\rho+1)^2]\), \(c_\rho=\rho^2/[2(\rho+1)^2]\), \(d_\rho=1-1/(\rho+1)+1/[2(\rho+1)^2]\). Then
\[
v_{k+1}=a_\rho v_k+c_\rho y_k,\qquad
y_{k+1}=\frac{v_k}{2(\rho+1)^2}+d_\rho y_k.\tag{5}
\]
For \(\rho\ge1\), all coefficients are nonnegative. The already proved mean-square monotonicity implies \(0\le y_k\le u_k+y_k\le1\). Also \(a_\rho+c_\rho=1-\rho/(\rho+1)^2<1\), so induction in (5), starting with \(v_0=0\), gives \(0\le v_k<1\) for every finite \(k\ge0\). The squared-residual expectation ratio is exactly \(v_k+y_k\), hence it is always strictly less than \(2\).

For the converse sharpness set \(k=\lfloor\sqrt\rho\rfloor\) and let \(\rho\to\infty\). The second recurrence and \(d_\rho\ge1-1/(\rho+1)\) give, for all \(0\le j\le k\),
\[
1\ge y_j\ge d_\rho^j\ge1-\frac{k}{\rho+1}\longrightarrow1.
\]
The first recurrence implies
\[
1>v_k\ge c_\rho\left(1-\frac{k}{\rho+1}\right)
\frac{1-a_\rho^k}{1-a_\rho}
=\frac{\rho}{\rho+2}\left(1-\frac{k}{\rho+1}\right)(1-a_\rho^k)\longrightarrow1,
\]
because \(a_\rho\to1/2\) and \(k\to\infty\). Thus \(v_k+y_k\to2\). This proves the joint sharp supremum. For each *fixed* positive integer \(k\), the recurrences additionally yield \(v_k+y_k\to2-2^{-k}\) as \(\rho\to\infty\).

## Verification
The supplementary standalone file `verify.py` enumerates every sampled row-coordinate pair with exact rational arithmetic and checks (1) and (2) on 370 configurations, including Sylvester and partial Sylvester matrices of sizes \(2,4,8\). It checks the exact two-mode factors \(9/10\) and \(57/50\), and separately compares (4) with exact all-path iteration through three steps for three rational singular-value contrasts. A floating-point check at \(\rho=10^6\) and \(k=1000\) tests the asymptotic trend; it is not used in the proof. Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work
Xia and Zhou's 2026 DSBGD method supplies the uniform independent row/coordinate update (their equation (1.2), Algorithm 1); their work analyzes regularization, convergence rates and discrepancy stopping under more general Hilbert-space assumptions. Their introduction explicitly notes loss of residual-related monotonicity due to the additional sampling. The present statement is **not** a claim to have invented the update, the general error-moment expansion, or the qualitative possibility of residual nonmonotonicity. It gives exact *sharp* paired step-size ceilings in a natural flat-frame family and a sharp multistep near-doubling law.

Du and Sun's earlier doubly stochastic block Gauss–Seidel analysis treats a different probability and scaling normalization: entry blocks are selected with probability proportional to their squared Frobenius norm and corrected by the selected-block norm. In the present family, nonuniform singular values make this different from uniform independent row-and-coordinate draws with one fixed unnormalized step. Their Theorems 8 and 11 provide sufficient convergence bounds, not the paired exact thresholds or the near-doubling limit stated here. The earlier Razaviyayn–Hong–Reyhanian–Luo doubly stochastic Gauss–Seidel algorithm likewise uses designed nonuniform sampling and step rules. These distinctions concern the actual update law, not paper titles.

## Limitations
The sharp claims require exact uniform independent row/coordinate draws, full column rank, a flat real orthogonal-column design, constant step size, consistent noiseless data, and exact arithmetic. For general matrices the entry-squared identities no longer collapse to \(S_2,S_4\), so no universal extension is asserted. The near-doubling limit concerns **expected squared** physical residual, not the expected unsquared residual, almost-sure paths, or a twofold solution-error increase. No general noisy-data regularization result or universal inference about adaptive stopping is established. The available material from the 2026 motivating article included its introduction and algorithm but not all of its later sections, leaving some historical-priority uncertainty; the independently available older block Gauss–Seidel article was inspected at its update law and convergence theorems.

## References
- Yuxin Xia and Zehui Zhou, *On the convergence of doubly stochastic block gradient descent method for linear inverse problems*, arXiv:2610.15399v1, first public October 11, 2026, https://arxiv.org/abs/2610.15399.
- Kui Du and Xiao-Hui Sun, *A doubly stochastic block Gauss–Seidel algorithm for solving linear equations*, arXiv:1912.13291 (first public December 31, 2019; inspected version 3), https://arxiv.org/pdf/1912.13291.
- Meisam Razaviyayn, Mingyi Hong, Navid Reyhanian and Zhi-Quan Luo, *A linearly convergent doubly stochastic Gauss–Seidel algorithm for solving linear equations and a certain class of over-parameterized optimization problems*, Mathematical Programming 176 (2019), 465–496, https://doi.org/10.1007/s10107-019-01404-0.

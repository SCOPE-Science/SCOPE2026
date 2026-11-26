# Optimal probe allocation for a power-law log spectrum under ideal deflation

## Finding

Fix a probe cost \(c\in\mathbb N\), an exponent \(p>1\), and an amplitude \(L>0\). Suppose the log-eigenvalues of a positive diagonal trace-class input are \(a_j=L j^{-p}\), \(j\ge1\). Within the ideal estimator family below, let \((k_B,N_B)\) be any exact mean-square-error minimizer at integer budget \(B\), with \(k_B+cN_B=B\). Then, as \(B\to\infty\),
\[
\frac{k_B}{B}\longrightarrow\frac{2p-1}{2p},\qquad
\frac{N_B}{B}\longrightarrow\frac{1}{2pc},\qquad
\min_N\mathcal V_N\sim
\frac{4pcL^2}{2p-1}\left(\frac{2p}{2p-1}\right)^{2p-1}B^{-2p}.
\]
In particular, the optimal number of probes is linear in the budget, and the probes consume asymptotically the fraction \(1/(2p)\) of the cost. Keeping any fixed positive number of probes instead gives risk of order \(B^{1-2p}\).

## Assumptions and scope

The eigenvalues of the input are \(\lambda_j=e^{a_j}-1\). They are summable, since \(\lambda_j\le e^L a_j\) and \(p>1\). The target is \(\log\det(I+A)=\sum_j a_j\). Deflating one eigenpair exactly costs one unit; one exact Gaussian residual quadratic form costs \(c\) units. For \(B\ge c\) the admissible integers are \(1\le N\le\lfloor B/c\rfloor\) and \(k=B-cN\). No finite deflation rank exhausts the residual. The estimator is
\[
\widehat L_{k,N}=\sum_{j\le k}a_j+\frac1N\sum_{i=1}^N\sum_{j>k}a_j Z_{ij}^2,
\]
with independent standard real normal variables \(Z_{ij}\). The nonnegative sums are finite almost surely by their finite expectations; no Gaussian random vector in the underlying infinite-dimensional Hilbert space is assumed. The unit cost of exact deflation and the fixed cost of an exact quadratic form are model assumptions, not algorithmic complexity bounds.

## Proof

The estimator is unbiased. The centered residual series converge in \(L^2\) since \(\sum_j a_j^2<\infty\), and \(\operatorname{Var}(Z_{ij}^2)=2\), so
\[
\mathcal V_N=\frac{2L^2}{N}\sum_{j>k}j^{-2p}.
\]
The integral comparison gives, for \(k\ge1\),
\[
\frac{(k+1)^{1-2p}}{2p-1}\le\sum_{j>k}j^{-2p}\le\frac{k^{1-2p}}{2p-1};
\]
the lower bound holds also at \(k=0\). Let \(x=k/B\) and note that \(N=B(1-x)/c\). On any compact subinterval of \((0,1)\), these bounds imply uniformly at the admissible points that
\[
B^{2p}\mathcal V_N=f(x)+o(1),\qquad
f(x)=\frac{2cL^2}{2p-1}\frac{x^{1-2p}}{1-x}.
\]
The same lower bound yields
\[
B^{2p}\mathcal V_N\ge\frac{2cL^2}{2p-1}\frac{((k+1)/B)^{1-2p}}{1-x}.
\]
This diverges along any sequence with \(x\to0\) or \(x\to1\). A sequence of feasible allocations with \(k/B\to1/2\) has bounded scaled risk (the grid spacing is \(c/B\)), so the minimizing allocations stay away from both endpoints. The logarithmic derivative of \(f\) is \(-(2p-1)/x+1/(1-x)\), which changes sign from negative to positive precisely at \(x_*=(2p-1)/(2p)\). A feasible sequence approaching \(x_*\), uniform convergence on compact interior sets and uniqueness of the minimum imply that every minimizing sequence has \(k_B/B\to x_*\) and scaled risk converging to \(f(x_*)\). Evaluation gives the displayed constant. For fixed \(N\) one has \(k\sim B\), and the same tail comparison gives \(\mathcal V_N\sim 2L^2 B^{1-2p}/(N(2p-1))\).

## Relationship to prior work

Cortinovis and Toni, [*Preconditioned Log-Determinant Approximation: One Gaussian Probe Vector Is Almost Always Enough*](https://arxiv.org/abs/2601.05778v1), Section 2, analyze the ideal Gaussian residual risk and compare allocations. [*Single-crossing optimality of Gaussian probe allocation after ideal spectral deflation*](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-single-crossing-optimality-of-gaussian-probe-allocation-after-id--63138f0a4092/RESULT.md) gives a global one-versus-two probe criterion in the finite model and an exact geometric allocation law. Those results are not claimed here. The contribution here is the limiting cost split and the leading optimized risk for the trace-class power-law model. The risk identity alone does not guarantee that an integer minimizer stays away from the extremes of the budget split; the endpoint lower bounds and compact-interior comparison supply this step.

## Limitations and reproducibility

The result concerns exact spectral deflation, exact residual quadratic forms and the specified cost model; it is not a guarantee for randomly estimated deflation subspaces, approximate Lanczos probes, arbitrary estimators, or a fixed finite spectrum as the budget diverges. The proof is analytic and its estimates are given above. No numerical output or formal proof certificate is needed for the claim.

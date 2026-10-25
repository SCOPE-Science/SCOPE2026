# An exact mean-square stability frontier for two-component random reshuffling

## Finding

Consider two quadratic component losses on \(\mathbb R^2\):
\[
f_1(z)=\frac{\alpha}{2}(u_1^Tz)^2,\qquad f_2(z)=\frac{\beta}{2}(u_2^Tz)^2,
\]
where \(\alpha,\beta>0\), the vectors \(u_1,u_2\) are unit vectors, and
\[
x=\langle u_1,u_2\rangle^2\in(0,1).
\]
The nonparallel directions make the sum objective strongly convex. At every epoch, apply both component-gradient steps with the same constant step size \(\eta>0\), in a uniformly random order, independently across epochs.

Let
\[
F_1(\eta)=2\alpha\beta\eta-2(\alpha+\beta)-\alpha^2\beta^2x(1-x)\eta^3,
\]
\[
F_2(\eta)=\alpha^2\beta^2x\eta^4-\alpha\beta(\alpha+\beta)x\eta^3-2\alpha\beta\eta^2+4(\alpha+\beta)\eta-8.
\]
Define \(\eta_*\) to be the smallest positive real root of either \(F_1\) or \(F_2\). Then the epoch-start iterates converge to the minimizer in mean square for every deterministic initial state exactly throughout the initial stable interval \(0<\eta<\eta_*\); at \(\eta=\eta_*\), convergence for every deterministic initial state fails because some initial state has a nondecaying second moment.

A concrete case is \(\alpha=2\), \(\beta=1\), and \(x=1/2\). Here \(F_1(\eta)=-\eta^3+4\eta-6<0\) for every \(\eta>0\), while
\[
F_2(\eta)=2\eta^4-3\eta^3-4\eta^2+12\eta-8.
\]
This quartic has exactly one positive root, \(\eta_*\approx1.3096734019\), lying in \( (1,3/2)\). Thus a step size such as \(\eta=1.2\) is mean-square stable at epoch boundaries even though the active multiplier of the larger-curvature component alone is \(1-2\eta=-1.4\), whose magnitude exceeds one.

## Assumptions and scope

The component Hessians are \(H_1=\alpha u_1u_1^T\) and \(H_2=\beta u_2u_2^T\). Each epoch visits both components exactly once; the two possible orders have probability \(1/2\), independently from epoch to epoch. The step size is constant within and across epochs. Mean-square stability means \(\mathbb E\|z_k\|^2\to0\) for every deterministic epoch-start state \(z_0\). The result concerns epoch-start states, not every intermediate state within an epoch.

The theorem is limited to two rank-one positive-semidefinite component Hessians in dimension two, with nonparallel component directions and zero component gradients at the common minimizer. It does not cover additive gradient noise, momentum, more than two components, nonquadratic losses, variable step sizes, or general shuffling rules.

## Proof

Set \(u_1=(1,0)^T\) and \(u_2=(\sqrt{x},\sqrt{1-x})^T\), without loss of generality. Write \(B_i=I-\eta H_i\) for the two component-step matrices and \(M=B_2B_1\). Because each \(B_i\) is symmetric, the reverse-order epoch matrix is \(B_1B_2=M^T\). If \(\Sigma_k=\mathbb E[z_kz_k^T]\), independence of the order selected at each epoch gives
\[
\Sigma_{k+1}=\mathcal T_\eta(\Sigma_k),\qquad
\mathcal T_\eta(X)=\frac12\big(MXM^T+M^TXM\big).
\]
The map \(\mathcal T_\eta\) preserves positive-semidefinite matrices and is self-adjoint for the Frobenius inner product. Its spectral radius is therefore a nonnegative eigenvalue with a positive-semidefinite eigenmatrix. Consequently mean-square stability is equivalent to \(\rho(\mathcal T_\eta)<1\).

Since \(H_1+H_2\) is positive definite for \(x\in(0,1)\), the small-step expansion
\[
\mathcal T_\eta(X)=X-\eta\big((H_1+H_2)X+X(H_1+H_2)\big)+O(\eta^2)
\]
shows that \(\rho(\mathcal T_\eta)<1\) for all sufficiently small positive \(\eta\). By continuity and positivity, the first loss of stability occurs when the Perron eigenvalue reaches \(1\); hence it is the first positive root of \(\det(I-\mathcal T_\eta)\).

Representing a symmetric matrix \(X\) by its coordinates \( (X_{11},X_{22},X_{12})\) and expanding the resulting three-dimensional covariance map gives the exact factorization
\[
\det(I-\mathcal T_\eta)=\frac{\alpha\beta\eta^3(1-x)}{4}\,F_1(\eta)F_2(\eta).
\]
For \(\eta>0\), the prefactor is strictly positive, so the first positive root of \(F_1F_2\) is exactly the first stability boundary. Also \(F_2(0)=-8\) and its leading coefficient is positive, so at least one positive root exists.

At the boundary, the positive covariance map has a nonzero positive-semidefinite fixed matrix. Decomposing it into rank-one positive-semidefinite matrices shows that at least one deterministic initial vector has a nondecaying second moment.

For the stated example, \(F_1(\eta)=-\eta^3+4\eta-6\) attains its global maximum over \(\eta>0\) at \(\eta=2/\sqrt3\), where its value is \(16/(3\sqrt3)-6<0\). The quartic \(p(\eta)=2\eta^4-3\eta^3-4\eta^2+12\eta-8\) has exactly one positive real root: a Sturm sequence gives two sign variations at \(0\) and one at \( +\infty\). Since \(p(1)=-1\) and \(p(3/2)=1\), that root lies in \( (1,3/2)\); numerical approximation gives \(1.3096734019\). These exact checks establish the claimed example and the extension beyond \(2/\alpha=1\).

## Verification

The included `verify.py` reconstructs the covariance map symbolically, verifies the determinant factorization exactly, proves that the example's cubic factor has no positive root, and applies Sturm's theorem to count exactly one positive root of the quartic. The script reports the numerical root only after the exact factorization and root-count checks pass. The proof uses the analytic covariance recursion; no finite simulation is treated as an infinite-time proof.

## Relationship to prior work

Ying, Yuan, Vlaski, and Sayed study random reshuffling with constant step sizes and establish a sufficient small-step stability condition and steady-state mean-square performance bounds. Ahn, Yun, and Sra analyze convergence rates for random reshuffling, including constant-step lower-bound settings. Neither inspected statement gives the necessary-and-sufficient mean-square threshold for the two-component, noiseless, noncommuting rank-one quadratic model above.

Mulayoff and Michaeli derive an exact mean-square stability threshold for SGD when minibatches are sampled independently across iterations. That sampling assumption differs from random reshuffling, where both components are used once per epoch and the order dependence persists across the two-step product. Nguyen, Phan, and Kalagnanam analyze paired-reversal averaging of epoch maps and its order-sensitivity reduction; averaging the two state maps is not the same covariance recursion as independently choosing one order each epoch. These results are close conceptual relatives but do not imply the displayed polynomial threshold.

## Limitations

This is a sharp, finite-dimensional stability result for a deliberately narrow model, not a general stability theorem for random reshuffling. The exact threshold is the first positive root among two explicit low-degree polynomials; for arbitrary parameters the root ordering may require further analysis. The result does not claim that the process is unstable for every step size above the first boundary, only that the connected stable interval starting at zero ends there. The literature search cannot prove exhaustive novelty, and a broader matrix-product treatment may contain an equivalent specialization not located in the inspected sources.

## References

1. B. Ying, K. Yuan, S. Vlaski, and A. H. Sayed, “Stochastic Learning under Random Reshuffling with Constant Step-sizes,” arXiv:1803.07964 (first public version 2018-03-21); IEEE Transactions on Signal Processing, DOI 10.1109/TSP.2018.2878551.
2. K. Ahn, C. Yun, and S. Sra, “SGD with shuffling: optimal rates without component convexity and large epoch requirements,” arXiv:2006.06946 (2020).
3. R. Mulayoff and T. Michaeli, “Exact Mean Square Linear Stability Analysis for SGD,” arXiv:2306.07850 (2023).
4. L. M. Nguyen, D. T. Phan, and J. Kalagnanam, “Learning to Shuffle: Block Reshuffling and Reversal Schemes for Stochastic Optimization,” arXiv:2604.00260 (2026).
5. M. Gürbüzbalaban, A. Ozdaglar, and P. Parrilo, “Why Random Reshuffling Beats Stochastic Gradient Descent,” arXiv:1510.08560; cited as background on random-reshuffling convergence, not as a source of the exact threshold.

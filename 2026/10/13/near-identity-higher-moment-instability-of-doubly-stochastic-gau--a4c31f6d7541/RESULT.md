# Near-identity higher-moment instability of doubly stochastic Gauss–Seidel

## Finding

**Theorem (mean-square decay together with arbitrarily rapid higher-moment growth).**
Fix a relaxation parameter \(0<\alpha<1\). For \(0<\rho<1\), consider the consistent linear system \(A_\rho x=0\), where
\[
A_\rho=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.
\]
From any deterministic \(X_0=x_0\in\mathbb R^2\setminus\{0\}\), independently at each iteration choose an equation index \(i\in\{1,2\}\) and a coordinate index \(j\in\{1,2\}\) with probability
\[
\Pr\{(i,j)\}=\frac{(A_\rho)_{ij}^{2}}{\|A_\rho\|_{\mathrm F}^{2}},
\qquad
(X_{k+1})_j=(X_k)_j-\alpha\frac{(A_\rho)_{i,:}X_k}{(A_\rho)_{ij}},
\]
leaving the other coordinate unchanged. This is the entry-weighted doubly stochastic Gauss–Seidel update of Razaviyayn, Hong, Reyhanian and Luo [1] on a homogeneous system.

Define
\[
\theta(\alpha,\rho)=1-\frac{\alpha(1-\alpha)(1-\rho)^2}{1+\rho^2}\in(0,1).
\]
For every integer \(k\ge0\),
\[
\mathbb E\|X_k\|_2^2\le\theta(\alpha,\rho)^k\|x_0\|_2^2,
\qquad
X_k\longrightarrow0\quad\text{almost surely}.
\]
More generally, for every \(0<p\le2\),
\[
\mathbb E\|X_k\|_2^p\le\theta(\alpha,\rho)^{kp/2}\|x_0\|_2^p.
\]
In contrast, for every fixed real \(p>2\) and every prescribed \(R>1\) and \(\varepsilon>0\), **there exists** \(\rho\in(0,1)\) for which \(\kappa_2(A_\rho)<1+\varepsilon\) yet
\[
\mathbb E\|X_k\|_2^p\ge R^k\|x_0\|_2^p
\qquad\text{for every integer }k\ge0.
\]
Indeed, whenever \(\rho<\alpha/(1-\alpha)\), the explicit uniform lower factor is
\[
L_p(\alpha,\rho)=
\frac{[\alpha-(1-\alpha)\rho]^p}
{2^{p/2}\rho^{p-2}(1+\rho^2)},
\quad
\mathbb E\|X_k\|_2^p\ge L_p(\alpha,\rho)^k\|x_0\|_2^p,
\]
and \(L_p(\alpha,\rho)\to+\infty\) as \(\rho\downarrow0\) for each \(p>2\).

The rational instance \(\alpha=\tfrac12\), \(\rho=\tfrac1{10}\) has condition number \(11/9\) and simultaneously
\[
\mathbb E\|X_k\|_2^2\le\left(\frac{323}{404}\right)^k\|x_0\|_2^2,
\qquad
\mathbb E\|X_k\|_2^4\ge\left(\frac{6561}{6464}\right)^k\|x_0\|_2^4.
\]
The quantifier is **for each** \(p>2\) one may select a sufficiently small \(\rho\); no single \(\rho\) is claimed to make all moments of order strictly greater than two unstable.

## Assumptions and scope

The scheme uses independent identically distributed ordered index pairs, exact arithmetic, exact residuals and division by the selected nonzero matrix entry. Its relaxation is fixed in \((0,1)\), which includes the source's recommended \(\alpha=1/2\) for two columns. The matrix is symmetric positive definite and nonsingular, with eigenvalues \(1\pm\rho\). Thus \(\kappa_2(A_\rho)=(1+\rho)/(1-\rho)\to1\). The target is the unique solution \(0\); the theorem concerns errors from deterministic nonzero initial vectors. Every moment at every finite time is finite.

## Proof

Write \(A=A_\rho\), \(S=\|A\|_{\mathrm F}^2=2(1+\rho^2)\), and let \(e_j\) be the standard basis vector. Conditioned on \(X_k=x\), the transition indexed by \((i,j)\) is
\[
x'=x-\alpha\frac{a_i^\top x}{a_{ij}}e_j.
\]
Its squared Euclidean norm is
\[
\|x'\|_2^2=\|x\|_2^2-2\alpha\frac{(a_i^\top x)x_j}{a_{ij}}
+\alpha^2\frac{(a_i^\top x)^2}{a_{ij}^2}.
\]
Since every entry of \(A\) is nonzero, average over all four pairs with weights \(a_{ij}^2/S\). The cross term contributes \(-2\alpha\|Ax\|_2^2/S\): for each row \(i\), \(\sum_j a_{ij}x_j=a_i^\top x\). The quadratic term contributes \(2\alpha^2\|Ax\|_2^2/S\), because there are precisely two coordinate choices per row. Consequently the **exact conditional identity** is
\[
\mathbb E[\|X_{k+1}\|_2^2\mid X_k=x]
=\|x\|_2^2-\frac{\alpha(1-\alpha)}{1+\rho^2}\|Ax\|_2^2.
\]
The smallest singular value of \(A\) is \(1-\rho\), proving the conditional \(\theta\) inequality. The tower property gives the asserted bounds for the second moment and, by concavity of \(t\mapsto t^{p/2}\) for \(0<p\le2\), for each lower-order moment. For each fixed \(\delta>0\), Markov's inequality bounds \(\Pr\{\|X_k\|_2>\delta\}\) by \(\theta^k\|x_0\|_2^2/\delta^2\); the probabilities are summable. Borel–Cantelli for rational positive \(\delta\) proves almost-sure convergence.

For the higher-order lower bound, retain **only** the two off-diagonal choices. Each has probability \(\rho^2/S\). The choice \((i,j)=(2,1)\) changes coordinate one to
\[
w_1=(1-\alpha)x_1-\frac\alpha\rho x_2,
\]
and \((i,j)=(1,2)\) changes coordinate two to
\[
w_2=(1-\alpha)x_2-\frac\alpha\rho x_1.
\]
In either outcome the output norm is at least the absolute value of its just-updated coordinate. Therefore, for \(p\ge2\),
\[
\mathbb E[\|X_{k+1}\|_2^p\mid X_k=x]
\ge\frac{\rho^2}{S}(|w_1|^p+|w_2|^p)
\ge\frac{\rho^2}{S}2^{1-p/2}(w_1^2+w_2^2)^{p/2}.
\]
The second inequality is the elementary two-coordinate power-mean inequality. The map \(x\mapsto w\) is represented by
\[
W=\begin{pmatrix}1-\alpha&-\alpha/\rho\\-\alpha/\rho&1-\alpha\end{pmatrix}.
\]
Its two singular values are \(|1-\alpha-\alpha/\rho|\) and \(1-\alpha+\alpha/\rho\). Under the stated restriction \(\rho<\alpha/(1-\alpha)\), the smaller one is \(\alpha/\rho-(1-\alpha)\). Thus
\[
\mathbb E[\|X_{k+1}\|_2^p\mid X_k=x]
\ge \frac{\rho^2}{2(1+\rho^2)}2^{1-p/2}
\left(\frac\alpha\rho-(1-\alpha)\right)^p\|x\|_2^p
=L_p(\alpha,\rho)\|x\|_2^p.
\]
Independence of the fresh pair from the current state, followed by the tower property, gives the iterated lower bound for **all** nonzero \(x_0\) and **all** \(k\ge0\). For fixed \(p>2\), its factor is asymptotic to \(\alpha^p/[2^{p/2}\rho^{p-2}]\) as \(\rho\downarrow0\); therefore it exceeds any specified \(R\). Meanwhile \(\kappa_2(A_\rho)\to1\), allowing both inequalities to hold simultaneously. This proves all quantified assertions.

For the rational example, substituting \(\alpha=1/2\) and \(\rho=1/10\) yields the exact fractions \(\theta=323/404\) and \(L_4=6561/6464\). Note \(323/404<1<6561/6464\).

## Verification

Run `python3 verify.py` with the standard Python library. The verifier constructs all four random update matrices using exact fractions, confirms the exact quadratic-error identity as a matrix equality, checks the stated rational constants, checks the conditional second- and fourth-moment inequalities for 360 nonzero rational state vectors, and exhaustively enumerates 18 finite-horizon expectations at three initial states for horizons one through six. It prints `VERIFY_OK` on success. Finite testing does **not** prove the infinite-horizon or real-order assertions; the power-mean and singular-value arguments above do.

## Relationship to prior work

Razaviyayn, Hong, Reyhanian and Luo [1, Algorithm 1 and Theorem 1] introduce this very entry-weighted selection rule and prove geometric **mean-square** convergence under their stepsize condition. The present theorem is consistent with, and uses exactly the same type of update as, that result; its new target is the behavior of orders strictly greater than two near the identity. Du and Sun [2, §2 and the mean-square convergence analysis] include the entrywise scheme as a limiting block choice and derive lower-order convergence results, without the specific higher-moment separation in the inspected sections. Gower and Richtárik [3] present broader expected-norm randomized iterative-solvers, which likewise do not imply higher-order moment decay. Heavy-tail results for stochastic optimization [4,5] motivate caution with multiplicative amplification but study different recurrences or stationary regimes, rather than this exact homogeneous, near-identity linear solver. This comparison does not establish exhaustive worldwide priority.

## Limitations

The theorem is about expectations of homogeneous random matrix products in exact arithmetic. The higher-order moments are **finite for each finite iteration** but diverge as the iteration index grows; no heavy-tailed stationary distribution is asserted. Almost-sure convergence remains true and is not contradicted by the diverging higher moments. Exponential higher-moment growth is established for each requested \(p>2\) with a sufficiently small matrix parameter, not uniformly in \(p\) for a single matrix. The lower factor need not be the exact moment spectral radius. The result does not assess running time, finite-precision overflow, or the effect of imposing a safeguard on small selected entries.

## References

[1] M. Razaviyayn, M. Hong, N. Reyhanian, Z.-Q. Luo, *A Linearly Convergent Doubly Stochastic Gauss-Seidel Algorithm for Solving Linear Equations and A Certain Class of Over-Parameterized Optimization Problems*, arXiv:1810.05251, first public version 2018-10-11. Algorithm 1, Theorem 1. https://arxiv.org/abs/1810.05251

[2] K. Du, X. Sun, *A doubly stochastic block Gauss-Seidel algorithm for solving linear equations*, arXiv:1912.13291, first public version 2019-12-31, §2 and moment convergence results. https://arxiv.org/abs/1912.13291

[3] R. M. Gower, P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM J. Matrix Anal. Appl. 36 (2015), 1660–1690, arXiv:1506.03296. https://arxiv.org/abs/1506.03296

[4] *The Heavy-Tail Phenomenon in SGD*, arXiv:2006.04740, introduction and moment discussion. https://arxiv.org/abs/2006.04740

[5] *Multiplicative noise and heavy tails in stochastic optimization*, arXiv:2006.06293, introductory and stationary-tail sections. https://arxiv.org/abs/2006.06293

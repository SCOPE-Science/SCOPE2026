# Exact finite-budget laws for adjoint-free stochastic Rayleigh–Ritz search on one-spike spectra

## Finding

**Theorem (exact laws and optimal batching).** Let \(d\ge3\), let \(e\in\mathbb R^d\) have unit norm, and suppose the real linear map \(A:\mathbb R^d\to\mathbb R^q\) satisfies
\[
 A^{\mathsf T}A=\lambda_-I_d+(\lambda_+-\lambda_-)ee^{\mathsf T},
 \qquad 0\le\lambda_-<\lambda_+.
\]
Start from a deterministic unit vector \(v_0\) with \(0<|e^{\mathsf T}v_0|<1\). On each iteration choose independently, conditional on the current vector, a Haar-uniform \(s\)-dimensional subspace \(W_k\subset v_k^\perp\), where \(1\le s\le d-1\). Set \(v_{k+1}\) to any unit maximizer of \(\|Az\|^2\) in \(\operatorname{span}(v_k,W_k)\). This operation uses forward products with \(A\), without applying its adjoint.

Write \(m=d-1\) and \(\Delta_k=\lambda_+-\|Av_k\|^2\). For \(1\le s<m\), the variables
\[
 B_k=\frac{\Delta_{k+1}}{\Delta_k}
\]
are independent and identically distributed with the exact law
\[
 \boxed{B_k\sim\operatorname{Beta}\!\left(\frac{m-s}{2},\frac{s}{2}\right).}
\]
Consequently \(\Delta_n/\Delta_0\) is a product of \(n\) such beta variables; for every real \(p>-(m-s)/2\),
\[
 \boxed{\mathbb E\left[\left(\frac{\Delta_n}{\Delta_0}\right)^p\right]
 =\left[\frac{\Gamma((m-s)/2+p)\Gamma(m/2)}{\Gamma((m-s)/2)\Gamma(m/2+p)}\right]^n.}
\]
In particular \(\mathbb E\Delta_n=\Delta_0(1-s/m)^n\) and, almost surely,
\[
 \boxed{\lim_{n\to\infty}-\frac1n\log\frac{\Delta_n}{\Delta_0}
 =\psi(m/2)-\psi((m-s)/2)>0,}
\]
where \(\psi\) is the logarithmic derivative of the gamma function. If \(s=m\), the first iteration reaches a top singular vector and \(\Delta_1=0\).

The assertion extends to deterministic variable block sizes \(1\le s_j\le m\): until any full-dimensional block terminates the iteration, the successive ratios are independent beta variables with the corresponding parameters; a size-\(m\) block has a zero gap ratio deterministically. Given a fixed total budget \(B=\sum_{j=1}^t s_j\le m\) of *new forward applications of* \(A\), and counting the initial \(Av_0\) as cached, the expected remaining gap is exactly
\[
 \boxed{\mathbb E\Delta_t=\Delta_0\prod_{j=1}^t(1-s_j/m).}
\]
Among all such partitions of \(B\), one block of size \(B\) minimizes the expected gap, uniquely except for the single-block triviality; every genuine split is strictly worse. In particular, for \(2\le B\le m\), one \(B\)-dimensional block has normalized expected gap \(1-B/m\), strictly below the \(B\) successive single-direction updates' \((1-1/m)^B\). At \(B=m-1\), the factors are \(1/m\) and \((1-1/m)^{m-1}\), respectively; their ratio is asymptotically \(e/m\) as \(m\to\infty\).

The high-dimensional separation also holds in distribution: if \(s/m\to\theta\in(0,1)\), the one-block ratio converges in probability to \(1-\theta\), whereas \(s\) one-direction updates yield a ratio converging in probability to \(e^{-\theta}\). At \(s=m-1\), \(m\Delta_1/\Delta_0\) converges in distribution to a chi-square variable with one degree of freedom, while the \(m-1\) successive one-direction updates have normalized gap converging in probability to \(e^{-1}\).

## Assumptions and scope

All vectors and operators are real, sampling is exactly Haar-uniform within the current Euclidean tangent hyperplane, and the subspace minimax problem is solved exactly. The two distinct squared singular values have multiplicities \(1\) and \(d-1\). The initial overlap assumption avoids stationary singular vectors and ensures strictly positive finite gaps for every finite iteration when \(s<m\). No stochastic noise is added to the evaluations of \(A\). For the budget comparison, the already evaluated forward image of each current vector is reused; only new tangent-vector forward evaluations are counted. Larger blocks require extra working memory, orthogonalization, inner products and a reduced eigenproblem: this is **not** a claim of better wall-clock time or total arithmetic complexity.

## Proof

**1. Exact optimizing vector.** For any unit \(z\),
\[
 \|Az\|^2=\lambda_-+(\lambda_+-\lambda_-)|\langle e,z\rangle|^2.
\]
If \(K=\operatorname{span}(v,W)\), maximizing over the unit sphere in \(K\) is equivalent by Cauchy–Schwarz to maximizing \(|\langle P_Ke,z\rangle|\); an optimizer is \(P_Ke/\|P_Ke\|\), up to sign. Because \(\langle e,v\rangle\ne0\), the projection is nonzero. For this optimizer,
\[
 \Delta_{\mathrm{new}}=(\lambda_+-\lambda_-)(1-\|P_Ke\|^2).
\]
Write \(c=\langle e,v\rangle\) and \(w=(e-cv)/\sqrt{1-c^2}\), so \(w\perp v\), \(\|w\|=1\), and
\[
 \|P_Ke\|^2=c^2+(1-c^2)\|P_Ww\|^2.
\]
Since \(\Delta_{\mathrm{old}}=(\lambda_+-\lambda_-)(1-c^2)\), division gives the exact, normalization-independent identity
\[
 \frac{\Delta_{\mathrm{new}}}{\Delta_{\mathrm{old}}}=1-\|P_Ww\|^2.
\]

**2. Conditional beta law and independence.** The tangent space has dimension \(m=d-1\). Rotational invariance implies the squared norm of the projection of a fixed unit tangent vector onto a Haar-uniform \(s\)-plane has distribution \(U=X/(X+Y)\), where \(X\sim\chi_s^2\) and \(Y\sim\chi_{m-s}^2\) are independent. Thus \(1-U\sim\operatorname{Beta}((m-s)/2,s/2)\). For \(s<m\) this value is strictly between zero and one almost surely. It depends on the current state only through a **fixed** conditional distribution. Because the newly sampled plane is conditionally independent of the past, the conditional expectation of any bounded measurable function of the next ratio is the same constant given the entire past. Induction proves independence of all successive ratios and their displayed marginal laws. Also \(P_Ke\) has nonzero \(e\)-overlap at each finite step, validating all subsequent iterations. If \(s=m\), \(W=v^\perp\) and \(K=\mathbb R^d\).

**3. Product moments and pathwise rate.** The beta density gives, whenever \(p>-(m-s)/2\),
\[
 \mathbb EB^p=\frac{\Gamma((m-s)/2+p)\Gamma(m/2)}{\Gamma((m-s)/2)\Gamma(m/2+p)}.
\]
Multiplication yields all finite-horizon moments. Its derivative at \(p=0\) yields \(\mathbb E\log B=\psi((m-s)/2)-\psi(m/2)\), which is finite and strictly negative. The strong law of large numbers applied to the independent logarithms proves the almost-sure exponential rate. The stated expectation follows by taking \(p=1\).

**4. Sharp allocation over a finite forward-product budget.** The same conditional argument allows nonconstant deterministic block sizes. For positive integers \(a,b\) with \(a+b\le m\),
\[
 (1-a/m)(1-b/m)=1-(a+b)/m+ab/m^2>1-(a+b)/m.
\]
Merging adjacent blocks therefore strictly decreases the expected gap, and repeated merging produces the one-block optimum for every partition. With \(B=m\), that block reaches the optimum exactly. The single-direction comparison and its near-full-budget asymptotics follow immediately. This comparison is exclusively in the forward-evaluation metric, not a wall-clock statement.

**5. Distributional high-dimensional limits.** The beta distribution in step 2 has mean \(1-s/m\) and variance \(2s(m-s)/(m^2(m+2))\), so the one-block ratio concentrates at \(1-\theta\) when \(s/m\to\theta\). For one-direction steps, \(\mathbb E\log B=\psi((m-1)/2)-\psi(m/2)=-1/m+O(m^{-2})\), and \(\operatorname{Var}(\log B)=\psi_1((m-1)/2)-\psi_1(m/2)=O(m^{-2})\). For \(s=O(m)\), their independent logarithmic sum converges in probability to \(-\theta\). Finally, \(s=m-1\) gives \(B=X/(X+Y)\) with \(X\sim\chi_1^2\) and \(Y\sim\chi_{m-1}^2\); because \(Y/m\to1\) in probability, \(mB\) converges in law to \(\chi_1^2\). This completes the classification.

## Verification

The standalone `verify.py` checks reduced Rayleigh–Ritz eigenvector updates directly against the predicted tangent projection identity for dimensions \(3,4,6,11\), all admissible block sizes and random initial states. It also checks beta moments, strict finite-budget inequalities, and seeded Monte Carlo beta means. The actual saved script passed 837 deterministic assertions. The algebraic derivation above establishes the universal statements independently of those finite tests. Run using `python verify.py` with NumPy and SciPy installed.

## Relationship to prior work

Bresch, Lorenz, Schneppe and Winkler (arXiv:2410.08297, first posted October 10, 2024) introduced the adjoint-free random tangent exact line search, proved almost-sure convergence and general sublinear stationarity estimates, and studied numerical behavior. Their one-direction update corresponds to \(s=1\) here. A later paper by Bresch, Melnyk, Schoen and Steidl (arXiv:2512.05520, first posted December 5, 2025), **already describes the multi-vector Rayleigh–Ritz construction** in Section 8.6 and compares its numerical performance with averaged-gradient sampling; neither that construction nor the Haar projection's beta distribution is claimed as new. The present narrow claim is the complete *adaptive finite-horizon beta product law and exact all-partitions forward-evaluation budget comparison* for two-level one-spike maps. Stich, Müller and Gärtner's random-pursuit theory provides broader background on randomized exact line optimization; Saibaba's subspace-iteration analysis supplies distinct randomized singular-vector error bounds. The exact one-spike random-section projection law is independently classical and appears in related geometric work, but it is not an adaptive repeated Rayleigh–Ritz workload theorem. These comparisons do not establish exhaustive publication priority.

## Limitations

The exact independent beta factors generally fail for spectra with three or more distinct eigenvalues, nonuniform tangent sampling, approximate inner maximization, finite-precision arithmetic or noisy forward evaluations. The per-forward-call gap comparison does **not** include the growing reduced eigenproblem and orthogonalization costs for large blocks, and the 2025 publication already proposed that block procedure. Search records cannot rule out equivalent calculations in older specialized literature. The mathematical statements are subject to the stated exact-arithmetic and one-spike restrictions.

## References

1. J. Bresch, D. A. Lorenz, F. Schneppe and M. Winkler, *Matrix-free stochastic calculation of operator norms without using adjoints*, arXiv:2410.08297, first public version 2024-10-10. https://arxiv.org/html/2410.08297v3
2. J. Bresch, O. Melnyk, M. Schoen and G. Steidl, *Stochastic Zeroth-Order Method for Computing Generalized Rayleigh Quotients*, arXiv:2512.05520, section 8.6, first public version 2025-12-05. https://arxiv.org/html/2512.05520v2
3. S. U. Stich, C. L. Müller and B. Gärtner, *Optimization of Convex Functions with Random Pursuit*, arXiv:1111.0194. https://arxiv.org/html/1111.0194
4. A. K. Saibaba, *Randomized subspace iteration: Analysis of canonical angles and unitarily invariant norms*, arXiv:1804.02614. https://arxiv.org/abs/1804.02614

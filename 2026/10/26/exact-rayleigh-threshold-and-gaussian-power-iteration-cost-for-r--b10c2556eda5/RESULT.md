# Exact Rayleigh threshold and Gaussian power-iteration cost for rank-one spectral preconditioning

## Finding
For every integer \(n\ge2\), \(\kappa>1\), and unit vector \(e\in\mathbb R^n\), let \(A=I+(\kappa-1)ee^{\mathsf T}\), and consider the strongly convex quadratic \(f(x)=\frac12 x^{\mathsf T}Ax\). For a proposed unit top-eigenvector approximation \(u\), write its Rayleigh score \(\gamma=u^{\mathsf T}Au\in[1,\kappa]\). Consider **all** positive rank-one inverse-spectral scalings of the form
\[
B_r=I-(1-r)uu^{\mathsf T},\qquad 0<r\le1,
\]
where \(r=1\) means omitting the correction, and then the optimally tuned constant-gain iteration \(x^+=x-\eta B_rAx\). Define \(q(r)\) as the best worst-case one-step contraction in the objective-energy norm \(\|x\|_A=(x^{\mathsf T}Ax)^{1/2}\), minimized over \(\eta>0\).

**Exact phase boundary.** The unique best rank-one strength and its optimal contraction factor are
\[
r_\star=\min\left\{1,\frac{\kappa+1-\gamma}{\gamma}\right\},\qquad
q_\star=\begin{cases}
\sqrt{\dfrac{(\kappa-\gamma)(\gamma-1)}{\gamma(\kappa+1-\gamma)}},&\gamma>(\kappa+1)/2,\\
\dfrac{\kappa-1}{\kappa+1},&1\le\gamma\le(\kappa+1)/2.
\end{cases}
\]
Thus **strict improvement over optimally tuned ordinary gradient descent is possible in this family if and only if** \(\gamma>(\kappa+1)/2\), equivalently \(|e^{\mathsf T}u|^2>1/2\) or the principal angle is less than \(\pi/4\). At and below the Rayleigh threshold, every nontrivial rank-one correction is strictly worse; its optimal safeguard is to apply no correction. At exact eigenvector alignment, the best iteration solves the quadratic in one step. The criterion is valid in all dimensions, not only in a two-by-two example.

**Gaussian power initialization.** If \(u=A^k g/\|A^k g\|_2\) for \(g\sim N(0,I_n)\) and integer \(k\ge0\), the exact probability that a strictly useful rank-one correction exists is
\[
\Pr(\gamma>(\kappa+1)/2)
=1-I_{1/(1+\kappa^{2k})}\left(\tfrac12,\tfrac{n-1}2\right),
\]
where \(I_z(a,b)\) is the regularized incomplete beta function. For \(n=2\), this probability is \((2/\pi)\arctan(\kappa^k)\). For fixed \(\kappa>1\) and \(n\to\infty\), if \(\kappa^{2k_n}/(n-1)\to c\in(0,\infty)\), the success probability tends to \(2[1-\Phi(c^{-1/2})]\), with limits zero and one when the ratio tends respectively to zero and infinity. Here \(\Phi\) is the standard normal CDF. Thus the transition in useful Gaussian power-iteration initialization occurs at order \((\log n)/(2\log\kappa)\) steps.

## Assumptions and scope
The setting is exact real arithmetic; \(n\ge2\) is an integer, \(\kappa>1\) is fixed, the spike direction \(e\) and candidate \(u\) are unit vectors, and the eigenvalues of \(A\) are exactly one (multiplicity \(n-1\)) and \(\kappa\) (multiplicity one). The scalar gain \(\eta\) is free and selected optimally. This is a *fixed preconditioner* result, not a theorem about nonlinear or varying-Hessian methods. For \(0<r<1\), the scaling \(B_r\) is, up to an irrelevant positive scalar factor, the inverse of the spectral-preconditioning template \(H+\alpha I\), with \(H=\gamma uu^{\mathsf T}\) and \(\alpha=\gamma r/(1-r)\). The optimal \(r_\star\) is implementable from the Rayleigh score \(\gamma\) when the spike spectrum is known. The scalar gain and regularizer are jointly tuned; the algorithm and parameters are not asserted to equal any separately prescribed published stepsize rule. The case \(r=1\) is the no-correction limit.

## Proof
Let \(C_r=A^{1/2}B_rA^{1/2}\), which is symmetric positive definite and similar to \(B_rA\). Put \(\gamma=u^{\mathsf T}Au=1+(\kappa-1)|e^{\mathsf T}u|^2\). The span of \(e\) and the component of \(u\) perpendicular to \(e\) is invariant. On that at-most-two-dimensional active plane the two eigenvalues \(\lambda_-\le\lambda_+\) have
\[
T(r)=\lambda_-+\lambda_+=\kappa+1-(1-r)\gamma,
\qquad\lambda_-\lambda_+=\kappa r.
\]
The remaining \(n-2\) eigenvalues (when present) equal one. For \(0<r\le1\), \((1-\lambda_-)(1-\lambda_+)=-(\kappa-1)(1-r)(1-|e^{\mathsf T}u|^2)\le0\); by continuity this also covers the aligned endpoints. Hence \(\lambda_-\le1\le\lambda_+\), so the two displayed eigenvalues are the full spectral extremes.

The error map \(I-\eta B_rA\) is similar under the \(A\)-norm to the self-adjoint map \(I-\eta C_r\). The optimal gain is \(\eta_\star(r)=2/T(r)\), and the exact worst-case energy contraction is
\[
q(r)^2=\left(\frac{\lambda_+-\lambda_-}{\lambda_++\lambda_-}\right)^2
=1-\frac{4\kappa r}{[\kappa+1-\gamma+\gamma r]^2}.
\]
Minimizing \(q(r)\) is equivalent to minimizing \([\kappa+1-\gamma+\gamma r]/\sqrt r\). Its derivative has the sign of \(\gamma r-(\kappa+1-\gamma)\). Therefore the unique minimizer over \(0<r\le1\) is \(r_\star=\min\{1,(\kappa+1-\gamma)/\gamma\}\). Substitution yields the stated piecewise formula. Strict comparison with \(q(1)=(\kappa-1)/(\kappa+1)\) gives the if-and-only-if cutoff. The squared objective contracts by the sharp worst-case factor \(q_\star^2\) at every fixed-preconditioner step, and an extreme eigenvector attains equality. No finite computation is used to justify this universal conclusion.

For the probabilistic statement, let \(g=(G_1,\ldots,G_n)\) in an orthonormal basis with first vector \(e\). The strict-usefulness event becomes \(\kappa^{2k}G_1^2>\sum_{j=2}^nG_j^2\). Since \(G_1^2\) and the sum on the right are independent chi-square variables with degrees of freedom one and \(n-1\), their normalized ratio is beta with parameters \((1/2,(n-1)/2)\). This yields the incomplete-beta formula. The two-dimensional formula follows from the Cauchy law of \(G_2/G_1\). For the high-dimensional limit, the normalized sum of \(n-1\) Gaussian squares converges in probability to one; conditioning on the independent \(G_1^2\) and applying continuity of its distribution gives the stated \(\Phi\) formula and two endpoint limits. This is an exact finite-dimensional distribution plus a proved asymptotic, not a simulation-based extrapolation.

## Verification
Run `python3 verify.py` using only the Python standard library. The script checks the rational Gram/trace and optimality identities over 3,088 finite exact cases and compares sampled Gaussian power-selection frequencies to exact formulas in four reproducible finite scenarios. Those tests provide algebraic corroboration; the proof above establishes the universal formulas and their strict boundaries.

## Relationship to prior work
Doikov, Stich and Jaggi (2024, arXiv:2402.04843, especially Sections 3, 6 and 7) introduce low-rank spectral Hessian preconditioning, describe top-eigenvector estimation via the power method, and prove global convergence bounds based on spectral approximation error. Those guarantees motivate the present rank-one, spiked-Hessian model. They do not provide the exact optimal-scalar gain and Rayleigh-based *usefulness/no-correction* cutoff, nor the finite-sample Gaussian power-init probability or logarithmic dimension transition established here. The present statement is not a contradiction of their results, since it optimizes a separately specified gain and regularization on a special quadratic.

Kahl and Rittich (arXiv:1209.1963, Sections 3--4) analyze approximate deflation subspaces and effective condition-number estimates for deflated conjugate gradients. Their operator is a projection-based deflated system rather than the positive rank-one inverse-Hessian scaling here; the exact Rayleigh midpoint criterion and power-iteration selection law do not follow from their reported bounds. Qu and collaborators (arXiv:2209.00809) optimize *diagonal* preconditioners via convex/quasiconvex formulations; an arbitrary rotated rank-one correction is a different feasible family. These comparisons distinguish objects and implications, not only titles.

## Limitations
The spectrum has one spike and an exactly flat bulk; the claimed cutoff need not remain at the same location for a general multilevel Hessian. The optimal parameters assume knowledge of the two spectral levels and a Rayleigh score. The probability calculation assumes independent isotropic Gaussian initialization, a frozen Hessian and exact power iterates; it does not include roundoff, approximate Hessian-vector products, warm starts or nonlinear changes of curvature. The sharp one-step factor is in the objective-energy norm, not a guarantee of one-step Euclidean error contraction under an arbitrary nonsymmetric similarity. General preconditioner-optimization and deflation literature could contain an equivalent special case under other notation; priority still requires independent assessment.

## References
1. N. Doikov, S. U. Stich, M. Jaggi, *Spectral Preconditioning for Gradient Methods on Graded Non-convex Functions*, arXiv:2402.04843 (first publicly submitted 2024-02-07), Sections 3, 6--7; ICML/PMLR 235 (2024), 11227--11252. https://arxiv.org/abs/2402.04843
2. K. Kahl, H. Rittich, *The Deflated Conjugate Gradient Method: Convergence, Perturbation and Accuracy*, arXiv:1209.1963 (first publicly submitted 2012-09-10), Sections 3--4. https://arxiv.org/abs/1209.1963
3. Z. Qu, W. Gao, O. Hinder, Y. Ye, Z. Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809 (first publicly submitted 2022-09-02). https://arxiv.org/abs/2209.00809

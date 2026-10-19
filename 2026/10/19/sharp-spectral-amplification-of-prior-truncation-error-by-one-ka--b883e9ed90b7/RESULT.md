# Sharp spectral amplification of prior truncation error by one Kalman observation

## Finding

Let \(P\in\mathbb R^{n\times n}\) be positive definite with ordered eigenvalues \(\lambda_1\ge\cdots\ge\lambda_n>0\). Let \(1\le r<n\) and \(P_r\) be a rank-\(r\) spectral truncation of \(P\), retaining the first \(r\) eigenpairs. For an observation matrix \(H\) and positive definite observation-noise covariance \(R\), define the covariance conditioning map
\[
\mathcal K_{H,R}(M)=M-MH^{\mathsf T}(HMH^{\mathsf T}+R)^{-1}HM,\qquad M\succeq0.
\]
Its difference after rank truncation satisfies the exact, dimension-independent worst-case law
\[
\boxed{\sup_{m\ge1,\ H\in\mathbb R^{m\times n},\ R\succ0}
\frac{\|\mathcal K_{H,R}(P)-\mathcal K_{H,R}(P_r)\|_2}{\|P-P_r\|_2}
=\frac{\lambda_1}{\lambda_{r+1}}.}
\]
The same supremum already holds with one scalar observation (\(m=1\)) and fixed noise variance \(R=1\). It is a supremum, not necessarily a maximum at finite sensor coefficients.

By contrast, if the observation information matrix \(H^{\mathsf T}R^{-1}H\) preserves the retained spectral subspace, the ratio is at most \(1\). Thus a non-block-diagonal observation direction can turn a small neglected prior eigenvalue into a posterior covariance discrepancy on the scale of the largest prior eigenvalue; an aligned observation cannot.

For the minimal two-dimensional model \(P=\operatorname{diag}(L,\varepsilon)\), \(P_1=\operatorname{diag}(L,0)\), \(L>\varepsilon>0\), and scalar measurement row \(h=(a,b)\) with noise variance \(1\), the exact amplification factor is
\[
\rho=\frac{(1+x)^2+\kappa xy}{(1+x)(1+x+y)},\qquad
x=La^2,\quad y=\varepsilon b^2,\quad\kappa=L/\varepsilon.
\]
In particular, amplification occurs precisely when \(b\ne0\) and \(x>1/(\kappa-1)\). For \(\kappa=1\), no amplification occurs.

## Assumptions and scope

All statements concern one **exact Gaussian conditioning step**, not prediction, approximate gains, Kalman mean errors, or multiple filter updates. Every covariance is real symmetric; \(P\) is positive definite, \(P_r\) is its positive-semidefinite rank-\(r\) spectral truncation, and \(R\) is strictly positive definite. Repeated eigenvalues are allowed; any fixed orthonormal eigenbasis used for truncation is admissible. The norm \(\|\cdot\|_2\) is the operator norm. The observation dimension is any positive integer; the sharp construction only needs one real row. "Information-aligned" means the orthogonal projector \(\Pi_r\) onto the selected retained eigenvectors satisfies
\[
[H^{\mathsf T}R^{-1}H,\Pi_r]=0.
\]
No assumption of scalar-coordinate independence of the measurement is made in the worst-case theorem. The spectral-truncation discrepancy is exactly \(\|P-P_r\|_2=\lambda_{r+1}\).

## Proof

**1. Order bound.** For \(M\succeq0\), completing a square in the observation coefficient \(z\in\mathbb R^m\) gives, for every \(v\in\mathbb R^n\),
\[
v^{\mathsf T}\mathcal K_{H,R}(M)v
=\min_z\{(v-H^{\mathsf T}z)^{\mathsf T}M(v-H^{\mathsf T}z)+z^{\mathsf T}Rz\}.
\]
Consequently, \(0\preceq M_0\preceq M_1\) implies \(\mathcal K(M_0)\preceq\mathcal K(M_1)\), and taking \(z=0\) shows \(0\preceq\mathcal K(M)\preceq M\). As \(P_r\preceq P\),
\[
0\preceq D:=\mathcal K(P)-\mathcal K(P_r)\preceq\mathcal K(P)\preceq P.
\]
Thus \(\|D\|_2\le\lambda_1\), and the claimed supremum is bounded above by \(\lambda_1/\lambda_{r+1}\). This argument is valid for singular \(P_r\) and arbitrary observation dimension.

**2. Sharp scalar sensor.** In an orthonormal eigenbasis of \(P\), choose a scalar observation with noise variance \(1\) and row
\[
h_t^{\mathsf T}=t e_1^{\mathsf T}+t^2 e_{r+1}^{\mathsf T},\qquad t>0.
\]
Only coordinates \(1\) and \(r+1\) enter the innovation. The posterior \(\mathcal K(P_r)\) has first diagonal entry \(\lambda_1/(1+\lambda_1t^2)\to0\). Meanwhile, the posterior of \(P\) has first diagonal entry
\[
\lambda_1-\frac{\lambda_1^2t^2}{1+\lambda_1t^2+\lambda_{r+1}t^4}
\longrightarrow\lambda_1.
\]
The cross entry tends to zero, and the \((r+1)\)-diagonal of \(\mathcal K(P)\) tends to zero. Other retained coordinates have matching posteriors and cancel; other omitted coordinates contribute unchanged eigenvalues \(\lambda_{r+2},\ldots,\lambda_n\). Hence
\[
D_t\longrightarrow \lambda_1 e_1e_1^{\mathsf T}+
\sum_{j=r+2}^n\lambda_je_je_j^{\mathsf T}
\]
in operator norm. Its norm is \(\lambda_1\), proving sharpness, including every dimension and retained rank. For \(r=n-1\), the sum is empty.

**3. No amplification by an aligned information matrix.** Assume \([H^{\mathsf T}R^{-1}H,\Pi_r]=0\). The positive information matrix \(S=H^{\mathsf T}R^{-1}H\) is block diagonal relative to the retained/omitted decomposition. On the retained block, \(P\) and \(P_r\) coincide, so their conditioned covariances coincide. On the omitted block, \(P_r\) is zero and \(\mathcal K(P)\) is positive semidefinite and bounded above by the corresponding omitted prior block. Therefore
\[
0\preceq D\preceq P-P_r,
\qquad \|D\|_2\le\lambda_{r+1}.
\]
The aligned bound is sharp: measuring only a retained eigenvector leaves the discarded prior block unchanged.

**4. Exact two-dimensional threshold.** Set \(d=1+La^2\) and \(v=(-Lab/d,\,1)^{\mathsf T}\). Direct substitution into the conditioning formula yields the rank-one factorization
\[
\mathcal K_{h,1}(P)-\mathcal K_{h,1}(P_1)
=\frac{\varepsilon d}{d+\varepsilon b^2}vv^{\mathsf T}.
\]
Its sole nonzero eigenvalue equals its trace, giving the displayed formula for \(\rho\). Subtracting one produces
\[
\rho-1=\frac{y((\kappa-1)x-1)}{(1+x)(1+x+y)}.
\]
For \(\kappa>1\) and \(b\ne0\), this is positive exactly when \(x>1/(\kappa-1)\). Also
\[
\kappa-\rho=\frac{(\kappa-1)(1+x)^2+\kappa y}{(1+x)(1+x+y)}\ge0.
\]
Taking \(a=t\), \(b=t^2\), and then \(t\to\infty\) yields \(\rho\to\kappa\), agreeing with the general construction. No finite enumeration is used to justify the all-dimensional theorem.

**5. Exact witness.** With \(P=\operatorname{diag}(1,1/100)\), \(h=(10,100)\), \(R=1\), and \(P_1=\operatorname{diag}(1,0)\), one has
\[
\boxed{\|\mathcal K(P)-\mathcal K(P_1)\|_2
=\frac{1010201}{2030100}>\frac{49}{100}},
\qquad\|P-P_1\|_2=\frac1{100}.
\]
The exact error amplification factor is \(1010201/20301\), exceeding \(49\). Every prior, approximate prior and observation variance here is nonnegative, and the observation noise is strictly positive.

## Verification

Run \(\texttt{python verify_covariance.py}\) using Python 3 with SymPy and NumPy. The verifier reconstructs the two-dimensional covariance updates symbolically, checks the rank-one factorization and scalar identities, tests the exact rational witness, and checks numerical high-dimensional instances for order, upper bounds, alignment and approach to sharpness. It has 385 deterministic assertions. The proof above, rather than the finite tests, establishes the universal quantifiers and the limiting supremum.

## Relationship to prior work

Schmidt, Hennig, Nick and Tronarp (2023), *The Rank-Reduced Kalman Filter*, derive low-rank prediction and correction formulas and note that conditioning a given low-rank forecast introduces no additional approximation inside the update. Their statement concerns exact implementation of the reduced-model correction, not an upper bound on the discrepancy between reduced and full posteriors. The present result isolates that separate discrepancy and computes its sharp operator-norm worst case over observation designs.

Spantini et al. (2014/2015), *Optimal Low-rank Approximations of Bayesian Linear Inverse Problems*, explicitly distinguish truncating a prior covariance from approximating the prior-to-posterior information update, and observe that prior-based dimension reduction ignores the likelihood. That qualitative warning is established prior work. Their principal approximation class retains the full prior and applies a low-rank negative update; it is different from replacing the prior by \(P_r\) before conditioning. Their results do not give the spectral minimax amplification \(\lambda_1/\lambda_{r+1}\) or the exact two-mode amplification threshold established here.

Al Ghattas and Sanz-Alonso (2024), *Non-asymptotic Analysis of Ensemble Kalman Updates: Effective Dimension and Localization*, bound ensemble approximation error, including small-noise deterioration; their perturbation model is random finite-ensemble covariance estimation rather than deterministic spectral-prior truncation with worst-case observation choice. Recent work on optimal low-rank posterior updates likewise uses different approximation classes and loss functions.

## Limitations

The supremum permits arbitrarily large observation coefficients while holding the noise variance fixed; it does not assert that typical normalized sensors attain the worst case. The result concerns covariance operator norm, not Kalman mean error, posterior distribution divergences, mean-square filter accuracy, or the stability of multiple prediction/correction cycles. It neither states nor assumes that a particular reduced-rank filtering algorithm explicitly computes the best rank-\(r\) eigenvalue truncation at every step. Prior literature already discusses qualitative shortcomings of prior truncation. An equivalent exact spectral bound in less searchable perturbation literature cannot be excluded; independent publication-priority examination remains outstanding.

## References

1. J. Schmidt, P. Hennig, J. Nick and F. Tronarp, *The Rank-Reduced Kalman Filter: Approximate Dynamical-Low-Rank Filtering In High Dimensions*, arXiv:2306.07774 (first public 2023-06-13). https://arxiv.org/abs/2306.07774
2. A. Spantini, A. Solonen, T. Cui, J. Martin, L. Tenorio and Y. Marzouk, *Optimal Low-rank Approximations of Bayesian Linear Inverse Problems*, arXiv:1407.3463 (2014); SIAM J. Sci. Comput. 37 (2015). https://arxiv.org/abs/1407.3463
3. O. Al Ghattas and D. Sanz-Alonso, *Non-asymptotic Analysis of Ensemble Kalman Updates: Effective Dimension and Localization*, Information and Inference 13 (2024), article iaad043. https://doi.org/10.1093/imaiai/iaad043
4. G. Carere and H. C. Lie, *Optimal low-rank approximations for linear Gaussian inverse problems on Hilbert spaces, Part I: posterior covariance approximation*, arXiv:2503.24020 (2025). https://arxiv.org/abs/2503.24020

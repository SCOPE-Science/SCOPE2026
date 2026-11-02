# A hub-induced one-step Lanczos bias and an exact chi-square two-step error law

## Finding

Let \(L_n\) be the combinatorial Laplacian of the unweighted star \(K_{1,n-1}\), and let \(t>0\) be fixed. For a single iid Rademacher vector \(s\in\{-1,1\}^n\), start Lanczos from \(v=s/\sqrt n\), and set
\[
\tau_n(t)=\operatorname{tr}(tI+L_n)^{-1}
=\frac1t+\frac{n-2}{t+1}+\frac1{t+n}.
\]
Write \(\widehat\tau_{n,j}(t)=n e_1^{\mathsf T}(tI_j+J_j)^{-1}e_1\) for the corresponding \(j\)-node Lanczos–Gauss trace approximation; if the Krylov subspace terminates early, the last available exact quadrature is used. All quantities refer to exact arithmetic.

**Theorem.** For each integer \(n\ge3\) and every \(t>0\), \(\widehat\tau_{n,2}\) is strictly negatively biased, and its error relative to the single-probe exact quadratic form is nonpositive on every outcome. Moreover, as \(n\to\infty\),
\[
\frac{\widehat\tau_{n,1}(t)-\tau_n(t)}n
\xrightarrow{\mathsf P}
-\frac1{(t+1)(t+2)},
\qquad
\widehat\tau_{n,2}(t)-\tau_n(t)
\xrightarrow{\mathsf d}
\frac{Z^2}{(t+1)^2}-\frac1{t(t+1)},
\]
where \(Z\sim N(0,1)\). The second convergence also holds in every fixed absolute moment. In particular,
\[
\lim_{n\to\infty}\bigl(\mathbb E\widehat\tau_{n,2}-\tau_n\bigr)
=-\frac1{t(t+1)^2},
\qquad
\lim_{n\to\infty}\operatorname{Var}(\widehat\tau_{n,2})
=\frac2{(t+1)^4}.
\]
Thus two Lanczos nodes suppress a linear-scale one-node underestimation, but leave a nondegenerate shifted chi-square error of constant size.

## Assumptions and scope

The graph is the **unweighted combinatorial star** with one distinguished center, \(n-1\) leaves, and spectrum \(\{0,1,n\}\) with multiplicities \(1,n-2,1\). The random vector has independent equiprobable \(\pm1\) coordinates. The parameter \(t\in(0,\infty)\) is held fixed as \(n\to\infty\). There is one probe and at most two Lanczos steps, with exact inner products and exact evaluation of the rational matrix function. The theorem does not concern averaging over multiple probes or a numerical floating-point implementation.

## Proof

**1. Exact random spectral measure.** Flip the entire sign vector if necessary so its center entry is positive, and let \(K\) count leaves of opposite sign. Then \(K\sim\operatorname{Bin}(n-1,1/2)\). The unit-start spectral weights at eigenvalues \(0,1,n\) are
\[
 w_0=\frac{(n-2K)^2}{n^2},\qquad
 w_1=\frac{4K(n-1-K)}{n(n-1)},\qquad
 w_n=\frac{4K^2}{n^2(n-1)}.
\]
Indeed, the constant eigenvector gives \(w_0\), the unit center-versus-leaves eigenvector gives \(w_n\), and orthogonal complementarity gives \(w_1\). They are nonnegative and sum to one. Put \(k=K\); the exact single-probe quadratic-form trace is
\[
 Q_n(k)=n\left(\frac{w_0}t+\frac{w_1}{t+1}+\frac{w_n}{t+n}\right).
\]
Unbiasedness \(\mathbb E Q_n=\tau_n\) follows independently from \(\mathbb E ss^{\mathsf T}=I\).

**2. Exact two-node residual.** The first three normalized moments of the spectral measure are
\[
 m_1=\frac{4k}n,\qquad
 m_2=\frac{4k(k+1)}n,\qquad
 m_3=\frac{4k[1+(n+1)k]}n.
\]
For \(k>0\), let \(H=n+(n-4)k\) and set
\[
 \beta^2=m_2-m_1^2=\frac{4kH}{n^2}>0,
 \qquad
 \alpha_1=\frac{m_3-2m_1m_2+m_1^3}{\beta^2}
 =\frac Hn+\frac{nk(n-1-k)}H.
\]
These are precisely the coefficients in the two-by-two Lanczos Jacobi matrix \(J_2=\bigl(\begin{smallmatrix}m_1&\beta\\ \beta&\alpha_1\end{smallmatrix}\bigr)\). Define
\[
 d_0=m_1\alpha_1-\beta^2
 =\frac{4k^2(n-1-k)}H\ge0,
 \qquad
 d_t=(t+m_1)(t+\alpha_1)-\beta^2>0.
\]
Since \(J_2\) is positive semidefinite, \(0\le d_0\le d_t\). The one- and two-node estimates are
\[
 \widehat\tau_{n,1}(k)=\frac n{t+m_1},\qquad
 \widehat\tau_{n,2}(k)=\frac{n(t+\alpha_1)}{d_t}.
\]
For \(k=0\) the start vector is constant, Lanczos stops after one step, and \(Q_n=\widehat\tau_{n,1}=\widehat\tau_{n,2}=n/t\).

For \(k>0\), the exact error identity is
\[
 \boxed{\quad
 Q_n(k)-\widehat\tau_{n,2}(k)
 =\frac{(n-2k)^2d_0}{t(t+1)(t+n)d_t}\ge0.\quad}
\]
To verify the identity without assuming it, write \(F(t)=Q_n(k)/n\) and \(G(t)=(t+\alpha_1)/d_t\). Both have matching Laurent expansions through \(t^{-4}\) at infinity because two-node Gaussian quadrature matches moments of degrees zero through three. After placing them over the common denominator \(t(t+1)(t+n)d_t\), the resulting numerator is therefore constant. When \(d_0>0\), comparing residues at \(t=0\) gives this constant as \(nw_0d_0=(n-2k)^2d_0/n\); multiplying by \(n\) yields the boxed identity. When \(d_0=0\), the spectral measure has only two atoms, and both sides are identically zero. The identity is strict for exactly those outcomes with \(k\ne n-1\) and \(2k\ne n\). Since \(\Pr(K=1)>0\) and \(n\ge3\), its expectation is positive, proving \(\mathbb E\widehat\tau_{n,2}<\tau_n\).

**3. Outlier-induced one-step error.** The weak law gives \(K/n\to1/2\) in probability, hence \(m_1\to2\), \(\widehat\tau_{n,1}/n\to1/(t+2)\), and \(\tau_n/n\to1/(t+1)\). This proves the first limit. The discrepancy between \(m_1\to2\) and the limiting bulk eigenvalue \(1\) is the influence of the vanishing-weight but growing eigenvalue \(n\).

**4. Two-step chi-square limit.** Define \(X_n=(n-2K)/\sqrt n\). Since \(n-2K\) has the law of one plus a sum of \(n-1\) independent symmetric signs, \(X_n\Rightarrow Z\sim N(0,1)\). We have \(nw_0=X_n^2\), \(nw_n\to1\), \(d_0/n\to1\), and \(d_t/n\to t+1\) in probability. From the spectral measure,
\[
 Q_n-\tau_n
 =(nw_0-1)\left(\frac1t-\frac1{t+1}\right)
 +(nw_n-1)\left(\frac1{t+n}-\frac1{t+1}\right)
 \Rightarrow\frac{Z^2-1}{t(t+1)}.
\]
The exact residual from step 2 converges in distribution to \(Z^2/[t(t+1)^2]\). Subtraction proves
\[
 \widehat\tau_{n,2}-\tau_n
 \Rightarrow
 \frac{Z^2-1}{t(t+1)}-\frac{Z^2}{t(t+1)^2}
 =\frac{Z^2}{(t+1)^2}-\frac1{t(t+1)}.
\]
For fixed \(t>0\), \(nw_n\) is bounded by \(4\), and the residual lies between zero and \(X_n^2/[t(t+1)]\). Consequently the absolute error is bounded by a constant depending only on \(t\) times \(1+X_n^2\). Standard Hoeffding sub-Gaussian bounds on the centered sign sum show \(\sup_n\mathbb E|X_n|^p<\infty\) for each finite \(p\). This supplies uniform integrability of every fixed power of the error, establishing absolute-moment convergence, the claimed limiting bias, and the variance \(2/(t+1)^4\).

## Verification

The bundled `verify.py` requires only Python 3 and uses exact rational arithmetic for the finite checks. It independently constructs the star Laplacian action, solves the shifted linear system by substitution, computes the first three moments from repeated sparse matrix-vector operations, checks both Lanczos coefficients and the full residual formula for all \(3\le n\le20\), all \(0\le k\le n-1\), and six positive rational shifts; it also verifies binomially averaged unbiasedness and strictly positive two-step bias. Additional asymptotic diagnostic tests compare the formula with the predicted scaling at dimensions \(400,2500,10000\). Its output was `VERIFY_OK exact_and_asymptotic_diagnostic_groups=1410`. These **finite tests are not proofs** of the theorem's universal or asymptotic assertions, which rely on the analytic argument above.

## Relationship to prior work

Ubaru, Chen and Saad (2017) establish the stochastic Lanczos quadrature method and general error estimates for matrix-function traces, including inverse traces. Chen, Trogdon and Ubaru (2021; 2022) analyze stochastic Lanczos spectral approximation and randomized matrix-free quadrature, including moment matching and analytic-function bounds. Chen and Hallman (2022) develop Krylov-aware stochastic trace estimators. Those facts provide the method and comparison framework; the finding here is the explicit **star-Laplacian finite-binomial residual identity and contrasting one-/two-step limits**, not the method or general Gaussian-quadrature error sign. The inspected literature did not establish the stated star-specific chi-square limit. Standard three-atom Gaussian quadrature and the central limit theorem are the principal classical ingredients.

## Limitations

The results require one **iid Rademacher** starting probe, the unweighted combinatorial star, fixed positive shift \(t\), and exact arithmetic. The mean-square error is not asserted to vanish at two steps; its asymptotic variance remains positive. General graph families, floating-point Lanczos loss of orthogonality, non-Rademacher probes, changes of the shift with dimension, and multiple-probe averaging are outside the theorem. General finite spectral Gaussian-quadrature theory and specialized earlier work could imply the finite identity in a different form; publication priority remains subject to independent verification. No independent scientific audit has been performed.

## References

1. S. Ubaru, J. Chen and Y. Saad, *Fast Estimation of \(\operatorname{tr}(f(A))\) via Stochastic Lanczos Quadrature*, SIAM Journal on Matrix Analysis and Applications **38** (2017), DOI: `10.1137/16M1104974`.
2. T. Chen, T. Trogdon and S. Ubaru, *Analysis of stochastic Lanczos quadrature for spectrum approximation*, `arxiv:2105.06595`, first posted 2021-05-13, https://arxiv.org/abs/2105.06595.
3. T. Chen, T. Trogdon and S. Ubaru, *Randomized matrix-free quadrature: unified and uniform bounds for stochastic Lanczos quadrature and the kernel polynomial method*, `arxiv:2204.01941v1`, first posted 2022-04-05, https://arxiv.org/abs/2204.01941.
4. T. Chen and E. Hallman, *Krylov-aware stochastic trace estimation*, `arxiv:2205.01736`, first posted 2022-05-03, https://arxiv.org/abs/2205.01736.

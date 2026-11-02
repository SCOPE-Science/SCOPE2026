# Gaussian commutator fluctuations and a finite Krylov silence test for paired implicit splitting

## Finding
Let \(d\geq2\), \(S,T\in\mathbb R^{d\times d}\) be real symmetric positive-semidefinite matrices, \(L>0\), and \(x_0\in\mathbb R^d\). In each pair of implicit-Euler microsteps use each of \(S\) and \(T\) once, choosing the pair's order fairly and independently from other pairs. Put \(h=L/(2n)\) and denote the random result after \(n\) pairs by \(X_n^{(h)}\). Let \(m_n^{(h)}=\mathbb E[X_n^{(h)}]\), \(H=(S+T)/2\), and \(C=(TS-ST)/2\). Then
\[
 h^{-3/2}(X_n^{(h)}-m_n^{(h)})\ \xrightarrow{\mathrm d}\ \mathcal N(0,\Sigma_L(x_0)),
 \qquad h^{-3}\operatorname{Cov}(X_n^{(h)})\longrightarrow\Sigma_L(x_0),
\]
where the possibly singular covariance is exactly
\[
 \Sigma_L(x_0)=\frac12\int_0^L v(t)v(t)^{\mathsf T}\,dt,\qquad
 v(t)=e^{-(L-t)H}C e^{-tH}x_0.
\]
Moreover \(m_n^{(h)}=e^{-LH}x_0+O(h)\). The leading stochastic error is silent **if and only if**
\[
 \Sigma_L(x_0)=0\quad\Longleftrightarrow\quad C H^k x_0=0\quad(k=0,1,\ldots,d-1).
\]
For every initial vector simultaneously, silence holds if and only if \(S\) and \(T\) commute. Thus the finite Krylov condition decides the exact initial-state-dependent cancellation of the leading random-order error.

The order is sharp: with \(H=\operatorname{diag}(2,1)\), \(S=H+B\), \(T=H-B\), \(B=\left(\begin{smallmatrix}0&1/2\\1/2&0\end{smallmatrix}\right)\), and \(x_0=(1,0)^{\mathsf T}\), both generators are positive definite but
\[
 \Sigma_L(x_0)=\operatorname{diag}\!\left(0,\frac1{16}e^{-2L}(1-e^{-2L})\right)\neq0
\]
in the second coordinate. (The matrix is nonzero positive semidefinite, not positive definite.)

## Assumptions and scope
Fix the dimension, the generators, the deterministic initial vector, and the positive physical horizon while \(n\to\infty\); only \(h=L/(2n)\) changes. Set \(R_S=(I+hS)^{-1}\) and \(R_T=(I+hT)^{-1}\). Each chronological pair applies either \(R_T R_S\) or \(R_S R_T\), with probability \(1/2\), independently between pairs. No random forcing or floating-point errors are included. Covariances and expectations refer solely to the independent random choices of pair order. Zero matrices and degenerate Gaussian limits are permitted.

## Proof
**1. Exact pair decomposition.** Let \(Q_+=R_TR_S\), \(Q_-=R_SR_T\), \(P_h=(Q_++Q_-)/2\), and \(D_h=(Q_+-Q_-)/2\). For independent symmetric signs \(\varepsilon_j\), the entire scheme is
\[
 X_j=(P_h+\varepsilon_jD_h)X_{j-1},\qquad m_j=P_h^j x_0.
\]
Because the generators are symmetric positive semidefinite, \(\|R_S\|_2,\|R_T\|_2\leq1\). Consequently \(\|P_h\|_2\leq1\), \(\|X_j\|_2\leq\|x_0\|_2\) on every sample path. Uniform Taylor expansion at zero gives
\[
 P_h=I-h(S+T)+O(h^2)=I-2hH+O(h^2),\qquad D_h=h^2C+O(h^3).
\]
Since \(n=L/(2h)\), the standard telescoping comparison of stable products with the matrix exponential gives \(P_h^n=e^{-LH}+O(h)\), and uniformly for \(0\leq j\leq n\), \(P_h^j=e^{-2jhH}+O(h)\) in operator norm.

**2. Exact martingale decomposition and remainder.** Iterating the centered recursion yields
\[
 X_n-m_n=\sum_{j=1}^nP_h^{n-j}\varepsilon_jD_hX_{j-1}.
\]
Each term is a martingale difference, so orthogonality and contraction imply \(\mathbb E\|X_j-m_j\|_2^2\leq j\|D_h\|_2^2\|x_0\|_2^2=O(jh^4)\). Replace \(X_{j-1}\) by its deterministic mean \(m_{j-1}\) in the exact decomposition. The replacement remainder \(R_n\) is again a martingale sum, and
\[
 \mathbb E\|R_n\|_2^2\leq\|D_h\|_2^2\sum_{j=1}^n\mathbb E\|X_{j-1}-m_{j-1}\|_2^2=O(n^2h^8)=O(h^6).
\]
Thus \(h^{-3/2}R_n\to0\) in \(L^2\), and \(R_n\) does not affect the limiting covariance after division by \(h^3\).

**3. Weighted-sign central limit theorem.** The remaining triangular array is the sum of independent centered Rademacher vectors
\[
 Z_h=h^{-3/2}\sum_{j=1}^n\varepsilon_jP_h^{n-j}D_hP_h^{j-1}x_0.
\]
Set \(t_j=2h(j-1)\). The coefficient of \(\varepsilon_j\) is \(\sqrt h\,v(t_j)+O(h^{3/2})\), uniformly in \(j\), because \(P_h^j=e^{-2jhH}+O(h)\) and \(D_h=h^2C+O(h^3)\). Every coefficient tends uniformly to zero, while their covariance matrix tends to
\[
 \lim_{h\downarrow0}h\sum_{j=1}^{L/(2h)}v(t_j)v(t_j)^{\mathsf T}
 =\frac12\int_0^L v(t)v(t)^{\mathsf T}\,dt.
\]
The Lindeberg condition holds automatically by bounded summands. Cramér–Wold proves the displayed Gaussian weak limit, including degenerate directions. The \(L^2\) remainder estimate and Cauchy–Schwarz transfer the same limit to the exact covariance.

**4. Sharp silence criterion.** Because the integrand is positive semidefinite, \(\Sigma_L(x_0)=0\) if and only if \(v(t)=0\) throughout \([0,L]\). Matrix exponentials are invertible; hence this is equivalent to \(Ce^{-tH}x_0=0\) for all such \(t\). Analyticity, differentiation at zero, and Cayley–Hamilton give the equivalent finite list \(CH^kx_0=0\) for \(k=0,\ldots,d-1\). If this holds for every \(x_0\), then \(C=0\) and \(ST=TS\). Conversely commutation gives \(C=0\) and even \(Q_+=Q_-\) at every positive step, since the resolvents commute. For a single initial vector the finite Krylov test is strictly finer than matrix commutation.

**5. Explicit nonzero witness.** With the displayed \(S,T\), the matrix \(C=[H,B]=\left(\begin{smallmatrix}0&1/2\\-1/2&0\end{smallmatrix}\right)\). Therefore \(v(t)=(0,-\tfrac12e^{-L-t})^{\mathsf T}\). Integrating its square yields \(\Sigma_{22}=\tfrac1{16}e^{-2L}(1-e^{-2L})>0\), proving the nontrivial root-mean-square fluctuation order \(h^{3/2}\) is attained. Both matrices are positive definite because their smallest eigenvalue is \((3-\sqrt2)/2>0\).

## Verification
The supplied `verify.py` recomputes exact rational matrix products for the witness, evaluates the limiting integral independently, and iterates the exact finite-step covariance recursion
\[
 V_{j+1}=P_hV_jP_h^{\mathsf T}+D_hV_jD_h^{\mathsf T}
 +(D_hm_j)(D_hm_j)^{\mathsf T},\quad V_0=0,
\]
for five step sizes. Scaled covariances converge monotonically to the independent integral value in those tests. It also checks the commuting boundary and a three-dimensional noncommuting example where a selected initial vector lies in the silent Krylov subspace. These finite calculations corroborate rather than replace the proof. Run `python verify.py` after installing the packages in `requirements.txt`.

## Relationship to prior work
Eisenmann and Stillfjord (2022 first preprint; 2024 journal publication) introduce independently sampled implicit randomized operator splitting and establish strong convergence-rate bounds. The present paired **without-replacement ordering variant** uses both suboperators in every pair; its asserted new statement is the explicit weak-noise Gaussian covariance and complete finite-dimensional initial-state-dependent silence classification, not the standard backward-Euler scheme or generic mean convergence.

Berger (1984) develops a foundational random-matrix-product central limit theorem using Chernoff semigroups, including stochastic product formulas. His fixed-diffusive-noise product limits are essential context; the present assertion concerns fluctuations vanishing at the faster \(h^{3/2}\) scale about a nontrivial deterministic implicit-splitting mean, along with its exact commutator/Krylov zero criterion. The result is not claimed as a new general product central limit theorem. Li and Wang (2025) already prove order-\(3/2\) expected single-run error for random splitting of an Allen–Cahn PDE; the **rate alone** is therefore not claimed as new. Childs and collaborators develop commutator-based deterministic Trotter error estimates. No new claim is made about the basic commutator expansion itself.

## Limitations
This is a finite-dimensional fixed-horizon theorem for real symmetric positive-semidefinite constant matrices and independent fair within-pair order choices. The root-mean-square rate concerns random-order fluctuations around the exact scheme mean, **not** total error relative to the continuum solution, which has a generally larger deterministic \(O(h)\) bias. A zero leading covariance for a particular \(x_0\) need not eliminate every higher-order fluctuation. The theorem does not cover unbounded generators, nonlinear evolutions, dependent orders across pairs, or finite-precision noise. Earlier general stochastic-product results may admit reformulations implying some components; independent priority assessment is outstanding.

## References
1. M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, arXiv:2210.05375 (initial public preprint 11 October 2022); *Numerische Mathematik* 156 (2024), 435–461, doi:10.1007/s00211-024-01396-w.
2. M. A. Berger, *Central Limit Theorem for Products of Random Matrices*, *Transactions of the American Mathematical Society* 285 (1984), 777–803, doi:10.1090/S0002-9947-1984-0752503-3.
3. L. Li and C. Wang, *Convergence of Random Splitting Method for the Allen–Cahn Equation in a Background Flow*, *Numerical Methods for Partial Differential Equations* 41 (2025), e70040, doi:10.1002/num.70040.
4. A. Childs, Y. Su, M. Tran, N. Wiebe and S. Zhu, *Theory of Trotter Error with Commutator Scaling*, *Physical Review X* 11 (2021), 011020, doi:10.1103/PhysRevX.11.011020.

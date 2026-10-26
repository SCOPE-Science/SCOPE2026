# A sharp fourth-moment barrier for a balanced stochastic-delay Euler step

## Finding
For independent standard Gaussian sequences \((\xi_n)\), \((\eta_n)\), the balanced one-grid stochastic Euler recurrence
\[
X_{n+1}=\frac13X_n+\left(\frac13+\sqrt u\,\xi_n\right)X_{n-1}+\eta_n,
\qquad u\ge0,
\]
has a unique causal centered strictly stationary solution with finite second moment precisely when \(u<2/3\). Here *unique* refers to causal \(L^2\)-stationarity. Let
\[
Q(u)=14008-45261u-10935u^2+78003u^3-19683u^4,
\quad R(u)=7004-4212u-7209u^2+2187u^3.
\]
There is a **unique** root \(u_4\in(0,2/3)\) of \(Q\), with \(u_4=0.345556005763941\ldots\). For the causal stationary solution its fourth moment is finite if and only if \(0\le u<u_4\). In this range,
\[
\operatorname{Var}(X)=\frac1{2/3-u},\qquad
\mathbb E[X^4]=\frac{27R(u)}{(2-3u)Q(u)}.
\]
For \(u_4\le u<2/3\), the variance is finite but the fourth moment is infinite. At the transition the latter diverges as
\[
\mathbb E[X^4]\sim
\frac{27R(u_4)}{(2-3u_4)[-Q'(u_4)]}\frac1{u_4-u},
\qquad u\uparrow u_4.
\]

## Assumptions and scope
The recursion is the step-\(h=1\), one-grid-delay explicit Euler–Maruyama discretization of the linear stochastic delay equation
\[
dX_t=\left(-\frac23X_t+\frac13X_{t-1}\right)dt
+\sqrt u\,X_{t-1}\,dW_t+dB_t,
\]
where \(B\) and \(W\) are independent Brownian motions. The balance \(p=q=1/3\) makes current and delayed deterministic weights equal while their sum remains contractive. The stochastic update, not an exact continuous-delay invariant distribution, is the theorem's object. No limit in step size is asserted. Gaussianity, independence and positive deterministic weights are used essentially. The fourth moment is an unconditional stationary moment, not a conditional Gaussian fourth moment.

## Proof
**Second moments and causal solution.** Write \(p=q=1/3\), \(Z_n=(X_n,X_{n-1})\), and \(u=\sigma^2\). The deterministic companion matrix is
\[
A=\begin{pmatrix}1/3&1/3\\1&0\end{pmatrix}.
\]
It is strictly Schur stable. For \(S_n=\mathbb EX_n^2\), \(T_n=\mathbb E(X_nX_{n-1})\), the homogeneous second-moment map in coordinates \((S_n,T_n,S_{n-1})\) is
\[
L_2(u)=\begin{pmatrix}1/9&2/9&1/9+u\\1/3&1/3&0\\1&0&0\end{pmatrix}.
\]
With additive noise, the stationary equations imply \(T=S/2\) and \((2/3-u)S=1\). Entrywise monotonicity and irreducibility of \(L_2(u)\) yield \(\rho(L_2(u))<1\) exactly for \(0\le u<2/3\); this can also be checked by the exact deterministic Gramian identity. Hence the independent-noise backward series converges in \(L^2\) and defines the unique causal \(L^2\)-stationary solution. At and beyond the boundary no causal stationary solution can have finite nonzero variance.

**Fourth-moment operator.** Order degree-four monomials as \(x^i y^{4-i}\), for \(i=0,1,2,3,4\). Gaussian moments \(\mathbb E\xi^2=1\), \(\mathbb E\xi^4=3\) yield the exact nonnegative matrix
\[
K_4(u)=\begin{pmatrix}
0&0&0&0&1\\
0&0&0&1/3&1/3\\
0&0&u+1/9&2/9&1/9\\
0&u+1/27&u+1/9&1/9&1/27\\
3u^2+2u/3+1/81&4u/3+4/81&2u/3+2/27&4/81&1/81
\end{pmatrix}.
\]
The entries are the coefficients of the conditional expectation of \((p x+(q+\sqrt u\xi)y)^i x^{4-i}\). It is irreducible and has strictly increasing Perron spectral radius as \(u\) increases. At \(u=0\) the spectral radius is less than one, since the deterministic companion matrix is Schur stable. Moreover,
\[
\det(I-K_4(u))=\frac{Q(u)}{19683}.
\]
Set \(u=2t/[3(1+t)]\) for \(t>0\). Then
\[
(1+t)^4Q\left(\frac{2t}{3(1+t)}\right)
=-2(901t^4+10549t^3+5667t^2-12929t-7004).
\]
The right polynomial has exactly one positive real root by Descartes' rule and the intermediate value theorem. Since \(Q(1/3)>0\) and \(Q(7/20)<0\), that root lies in \((1/3,7/20)\). Perron monotonicity implies \(\rho(K_4(u))<1\) exactly for \(u<u_4\) within \([0,2/3)\).

**Fourth moments and necessity.** For \(u<2/3\), write \(S=(2/3-u)^{-1}\) and \(m_i=\mathbb E[X_n^iX_{n-1}^{4-i}]\). Gaussian integration in the independent additive increment gives exactly
\[
m=K_4(u)m+\begin{pmatrix}0\\0\\S\\3S/2\\6S-3\end{pmatrix}.
\]
The forcing vector is nonnegative and nonzero. For \(u<u_4\) the positive resolvent converges, and exact elimination gives
\[
m_4=\frac{27R(u)}{(2-3u)Q(u)}.
\]
For completeness, necessity is not inferred merely from failure of matrix inversion: consider finite-past solutions initialized at zero. Iterating the fourth-moment recurrence gives nonnegative mixed moment vectors, because the finite-past solutions are polynomials in independent centered Gaussian inputs with nonnegative algebraic coefficients, and each even-total-degree expectation is a sum of nonnegative Wick contributions. The positive forcing approaches the displayed stationary forcing. The positive left Perron eigenvector of \(K_4\) shows that their fourth moments diverge when \(\rho(K_4)\ge1\). The finite-past solutions at a common terminal time are conditional expectations, given successive blocks of past driving noises, of the causal stationary solution. Were its fourth moment finite, their fourth moments would be uniformly bounded by conditional Jensen. This contradiction proves necessity, including equality. Finally, simplicity of the positive Perron crossing makes \(Q'(u_4)<0\), establishing the displayed simple-pole constant.

## Verification
The standalone `verify.py` rebuilds both moment operators from the independent Gaussian moments, checks the determinant identity and rational fourth-moment formula symbolically, certifies the unique root in \((0,2/3)\) by exact polynomial transformation and rational sign checks, and performs ancillary numerical Perron tests. Execute `python verify.py` using Python 3 with SymPy and NumPy. The analytical argument, not sampled eigenvalues, establishes the infinite-horizon claims.

## Relationship to prior work
Lan and Liu's 2023 study develops mean-square stability criteria for stochastic-delay Euler–Maruyama schemes; these are acknowledged as prior contributions, not independently rediscovered here. Shaikhet (1997), Example 2, already establishes the sharp second-moment stability condition for stochastic scalar difference equations with one lag. General random-coefficient autoregression theory already provides moment-spectral criteria; the degree-four operator method itself is not claimed as novel. The narrow assessed result is the explicit exact algebraic fourth-moment cutoff, rational fourth-moment law, and strict second-versus-fourth-moment gap for this balanced delayed Euler benchmark. Available closely related literature does not establish this specific combined exact cutoff, although incomplete access to some random-coefficient time-series publications leaves priority uncertainty.

## Limitations
The result is an exact special-case benchmark, not a universal fourth-moment criterion for all stochastic delay equations. Its fourth-moment boundary is specific to Gaussian independent noises, additive noise intensity one, unit delay/step, and equal deterministic coefficients one third. The existence of a stationary law with infinite fourth moment does not itself imply divergence of individual sample paths or incorrect finite-time strong convergence. Numerical root verification cannot replace the algebraic uniqueness argument. Independent verification and comprehensive publication-priority certification remain outstanding.

## References
1. G. Lan and Q. Liu, *Mean square exponential stability of numerical methods for stochastic differential delay equations*, arXiv:2306.12116v1, first public 2023-06-21, https://arxiv.org/html/2306.12116v1 .
2. L. Shaikhet, *Necessary and Sufficient Conditions of Asymptotic Mean Square Stability for Stochastic Linear Difference Equations*, Applied Mathematics Letters **10** (1997), 111–115, https://www.math.cmu.edu/~shaikhet/leonid/_docs/AML1997.pdf .
3. L. Truquet and J. Yao, *On the quasi-likelihood estimation for random coefficient autoregressions*, Statistics **46** (2012), 505–521, DOI: 10.1080/02331888.2010.541557 (full text not inspected).

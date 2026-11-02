# Joint Gaussian arrivals and discoveries in Poisson-grown complete graphs

## Finding

Let \(m_0\ge3\) be a fixed integer, and let \(\beta,\lambda>0\). Begin with a complete graph on \(m_0\) labeled vertices and one walker on an initial vertex. New vertices arrive independently at Poisson rate \(\beta\), each joining all extant vertices. Independently, at rate \(\lambda\), the walker jumps uniformly to one of the *other* extant vertices. A birth does not move the walker. Let \(N_t\) be the number of available vertices and \(X_t\) the number of different vertices visited through time \(t\), including the starting vertex.

Put
\[
k=\frac{\lambda}{\beta},\qquad
\alpha=\frac{\lambda}{\beta+\lambda},\qquad
a=\frac{\beta\lambda}{\beta+\lambda}.
\]
Then \(X_t/t\to a\) in probability and in \(L^2\). More precisely, as \(t\to\infty\),
\[
\frac1{\sqrt t}
\begin{pmatrix}N_t-m_0-\beta t\\X_t-a t\end{pmatrix}
\ \Longrightarrow\ \mathcal N_2(0,\Sigma_{\beta,\lambda}),
\]
with explicit covariance matrix
\[
\boxed{
\Sigma_{\beta,\lambda}=
\begin{pmatrix}
\beta&\displaystyle\frac{\beta k^2}{(1+k)^2}\\[3pt]
\displaystyle\frac{\beta k^2}{(1+k)^2}&
\displaystyle\frac{\beta k(k^2+1)}{(1+k)^3}
\end{pmatrix}.
}
\]
In particular, for unit rates, \(\beta=\lambda=1\), the limiting variance coefficient of the discovered-vertex count is \(1/4\), and its covariance coefficient with the number of births is also \(1/4\). These coefficients quantify the additional randomness due to Poisson vertex arrivals; deterministic vertex creation is a different model.

## Assumptions and scope

The two Poisson mechanisms are independent, with constant strictly positive rates. Every arrival supplies exactly one new vertex, attached to every existing vertex; there are no departures. At each walk event the target is uniform among the \(N_t-1\) vertices other than the current one; the graph has at least three vertices throughout. At birth times, the walker stays put. The statistic \(X_t\) records visits at all times, not merely at integer sampling times. All limits keep \(m_0\), \(\beta\), and \(\lambda\) fixed. Convergence of the centered two-dimensional vector concerns a single large observation time; no convergence rate is asserted.

## Proof

**1. Exact Markov reduction.** Let \(B_t=N_t-m_0\) be the birth count and \(D_t=X_t-1\) the count of newly discovered vertices. Write \(A_t=N_t-1=m_0-1+B_t\). Given \((A_t,D_t)\), the walker occupies a visited vertex. There are \(A_t-D_t\) unvisited targets among the \(A_t\) eligible jump targets. Thus, independent of its precise position, \(B\) jumps by \(+1\) at rate \(\beta\), and \(D\) jumps by \(+1\) at rate
\[
q_t=\lambda\frac{A_t-D_t}{A_t}.
\]
Walk events that do not discover a vertex leave \((A,D)\) unchanged. The resulting reduced state chain is exact, with no independence-of-visits assumption.

**2. An exact contracting martingale equation.** Define \(\alpha=\lambda/(\lambda+\beta)\), \(R_t=D_t-\alpha A_t\), and compensated martingales
\[
M^B_t=B_t-\beta t,\qquad
M^D_t=D_t-\int_0^t q_s\,ds.
\]
Since \(\lambda(1-\alpha)=\alpha\beta\), the conditional drift of \(R\) is \(-\lambda R_t/A_t\). Exactly,
\[
\boxed{dR_t=-\frac{\lambda R_{t-}}{A_{t-}}\,dt+dM^D_t-\alpha\,dM^B_t.}
\]
The predictable brackets are
\[
\langle M^B\rangle_t=\beta t,\qquad
\langle M^D\rangle_t=\int_0^t q_s\,ds,\qquad
\langle M^B,M^D\rangle_t=0.
\]
There are no simultaneous birth and discovery jumps. Applying the jump version of the square identity and discarding the nonpositive drift term gives
\[
\frac d{dt}\mathbb E[R_t^2]
\le\lambda+\alpha^2\beta,
\quad\text{hence}\quad
\mathbb E[R_t^2]\le\alpha^2(m_0-1)^2+(\lambda+\alpha^2\beta)t.
\tag{1}
\]
The birth process obeys \(B_t/t\to\beta\) almost surely and in \(L^2\). Since \(D_t=\alpha A_t+R_t\), bound (1) implies \(D_t/t\to\alpha\beta=a\) in \(L^2\). It also implies \(R_t/A_t\to0\) in probability, because \(A_t/t\to\beta>0\). Therefore \(q_t=\lambda(1-\alpha-R_t/A_t)\to a\) in probability. Its boundedness \(0\le q_t\le\lambda\), together with time integration and the same argument uniformly on rescaled intervals bounded away from zero, yields
\[
t^{-1}\langle M^D\rangle_{ts}\longrightarrow as
\]
uniformly on \(s\in[0,1]\) in probability.

**3. Gaussian martingale limit.** The two-dimensional martingale functional central limit theorem applies to \((M^B,M^D)\): jumps are bounded by one, the off-diagonal bracket is zero, and the rescaled predictable brackets converge to \(\beta s\) and \(as\). Consequently,
\[
\left(t^{-1/2}M^B_{ts},t^{-1/2}M^D_{ts}\right)_{0\le s\le1}
\Longrightarrow\left(\sqrt\beta W_1(s),\sqrt a W_2(s)\right)_{0\le s\le1},
\tag{2}
\]
where \(W_1,W_2\) are independent standard Brownian motions.

Set \(Z_t(s)=t^{-1/2}R_{ts}\). For any fixed \(\varepsilon\in(0,1)\), the exact equation from step 2 becomes, on \([\varepsilon,1]\),
\[
dZ_t(s)=-\frac{t\lambda}{A_{ts}}Z_t(s)\,ds
+d(t^{-1/2}M^D_{ts})-\alpha\,d(t^{-1/2}M^B_{ts}).
\]
Uniformly for \(s\in[\varepsilon,1]\), the coefficient \(t\lambda/A_{ts}\) converges in probability to \(k/s\), since \(A_{ts}/t\to\beta s\) uniformly on that interval. Solve the linear integral equation (or apply its elementary variation-of-constants/Gronwall stability formula) and use (2): any subsequential limit on \([\varepsilon,1]\) satisfies
\[
dZ(s)=-\frac ks Z(s)\,ds+\sqrt a\,dW_2(s)-\alpha\sqrt\beta\,dW_1(s).
\]
The influence of the random initial value at \(\varepsilon\) on \(Z_t(1)\) is at most \(|Z_t(\varepsilon)|\), because the drift coefficient is nonnegative. By (1), its second moment is at most \(C\varepsilon+O(t^{-1})\). Letting first \(t\to\infty\) and then \(\varepsilon\downarrow0\), we therefore obtain the unique entrance solution
\[
\boxed{
\frac{R_t}{\sqrt t}\Longrightarrow
\sqrt a\int_0^1s^k\,dW_2(s)
-\alpha\sqrt\beta\int_0^1s^k\,dW_1(s),
}
\tag{3}
\]
jointly with (2) at time one. The cutoff argument is valid even if \(k\le1/2\): the entrance integral has finite variance because \(k>0\).

**4. Identification of the covariance.** The exact identity
\[
X_t-a t=1+\alpha(m_0-1)+\alpha M^B_t+R_t
\]
combines with (2)–(3) to give the joint Gaussian representation
\[
\left(\sqrt\beta W_1(1),\ 
\alpha\sqrt\beta\int_0^1(1-s^k)\,dW_1(s)
+\sqrt a\int_0^1s^k\,dW_2(s)\right).
\]
By Itô isometry, the birth/discovery covariance is
\[
\alpha\beta\int_0^1(1-s^k)\,ds
=\frac{\beta k^2}{(1+k)^2},
\]
while the discovery variance is
\[
\alpha^2\beta\int_0^1(1-s^k)^2\,ds
+a\int_0^1s^{2k}\,ds
=\frac{\beta k(k^2+1)}{(1+k)^3}.
\]
The birth variance is \(\beta\). These prove the displayed joint limit. The determinant is strictly positive for every \(\beta,\lambda>0\), since the \(W_2\) component of the second coordinate is nondegenerate.

## Verification

`verify.py` is a standalone Python standard-library checker. It reconstructs the detailed embedded jump/birth process for all event sequences of length at most seven from two initial graph sizes and three pairs of integer rates, aggregating over exact rational probabilities. These are compared to the proposed reduced-state Markov chain. It then checks the exact drift of \(R\), its quadratic drift identity, the closed covariance simplifications, and positive definiteness for finite grids of states and integer rates. In the packaged replay it completed **9,369 exact rational checks** successfully. These finite tests independently stress the reduction and algebra but do not substitute for the martingale central limit proof.

## Relationship to prior work

Demirci, Işlak and Yıldız, *On a cover time problem on a dynamic graph with steps at random times*, arXiv:2110.01083, first publicly submitted October 3, 2021, study one-vertex-per-integer-time growth with Poisson walk steps and give a Gaussian limit for the number of visited vertices (Theorem 2.5); the introduction and Remark 2.2 mention random vertex arrival as a possible variant but do not present the above bivariate Poisson-birth covariance law in the inspected version 2. That model's deterministic arrival process has no birth-count fluctuation to couple to discoveries. Videla's *Out-of-equilibrium random walks* (2020) develops growing-graph knowledge processes, but only its abstract and bibliographic description were accessible during the comparison. Kijima, Shimizu and Shiraga (2025) investigate discretely timed, deterministically prescribed growth and unvisited-vertex counts, a different scaling/setup. The present result addresses explicitly stochastic **Poisson** graph growth and the joint Gaussian fluctuations of births and discoveries. Its novelty assessment is necessarily conditional on the uninspected full Videla paper and unavailable early preprint text; the statement should not be treated as a certified historical-priority claim.

## Limitations

The proof treats fixed positive constant rates, independent Poisson births and Poisson walker events, and complete graphs. Non-Poisson renewal births, state-dependent jump rates, sparse growing graphs, quantitative normal-approximation errors, and variable rate regimes are not covered. Numerical or exact finite tests are not proofs of convergence. Independent external mathematical review has not been performed; broader historical-priority checking remains warranted, particularly for Videla (2020) and early versions of arXiv:2110.01083.

## References

1. Y. E. Demirci, Ü. Işlak and M. A. Yıldız, *On a cover time problem on a dynamic graph with steps at random times*, arXiv:2110.01083 (initial submission 2021-10-03; version 2 dated 2023-02-28), https://arxiv.org/abs/2110.01083.
2. L. A. Videla, *Out-of-equilibrium random walks*, Advances in Applied Probability **52** (2020), 772–797, https://doi.org/10.1017/apr.2020.23.
3. S. Kijima, N. Shimizu and T. Shiraga, *How Many Vertices Does a Random Walk Miss in a Network with a Moderately Increasing Number of Vertices?*, Mathematics of Operations Research (online 2025-04-04), https://doi.org/10.1287/moor.2023.0060.

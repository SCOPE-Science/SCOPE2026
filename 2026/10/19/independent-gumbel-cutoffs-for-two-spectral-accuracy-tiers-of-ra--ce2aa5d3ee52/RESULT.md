# Independent Gumbel cutoffs for two spectral-accuracy tiers of randomly pivoted Cholesky

## Finding
For randomly pivoted Cholesky (RPCholesky) on repeated correlated positive-definite blocks and a diffuse diagonal background, the **two distinct spectral-norm accuracy thresholds have asymptotically independent standard-Gumbel fluctuations**, although both thresholds arise along the very same adaptive pivot trajectory. The result also gives an exact finite-size integral for the rank at which the tighter threshold is reached.

Fix \(0<\rho<1\), \(w=1-\rho^2\), and \(\beta>0\). For positive integers \(r,s\), put \(\delta=\beta r/s<w\) and
\[
 A_{r,s}=\operatorname{diag}(\underbrace{B_\rho,\ldots,B_\rho}_{r\text{ blocks}},\delta I_s),\qquad
 B_\rho=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.
\]
Run exact-arithmetic RPCholesky: at each step, choose an uneliminated index with probability proportional to its nonnegative Schur-complement diagonal and perform its rank-one Schur-complement update. Write \(R^{(k)}\) for the positive-semidefinite residual after \(k\) pivots. Define stopping indices
\[
 \tau_1=\min\{k:\|R^{(k)}\|_2\le w\},\qquad
 \tau_2=\min\{k:\|R^{(k)}\|_2<w\}.
\]
For any fixed tolerance \(\mu\) with \(w\le\mu<1+\rho\), the first index with \(\|R^{(k)}\|_2\le\mu\) is exactly \(\tau_1\); for any \(\delta<\mu<w\) it is exactly \(\tau_2\). This holds for every finite admissible \(r,s\).

Let \(U_i\) and \(V_i\) be mutually independent variables with \(U_i\sim\operatorname{Exp}(2)\), \(V_i\sim\operatorname{Exp}(w)\), \(1\le i\le r\), and let \(Z_j\sim\operatorname{Exp}(\delta)\), \(1\le j\le s\), independently. Set
\[
 H_r=\max_i U_i,\quad M_r=\max_i(U_i+V_i),\quad
 J(t)=\sum_{j=1}^s\mathbf1\{Z_j\le t\},\quad
 L_r=\sum_{i=1}^r\mathbf1\{U_i+V_i>H_r\}.
\]
Then the **joint finite-sample law** is
\[
 (\tau_1,\tau_2)\ \overset{d}=\ (2r-L_r+J(H_r),\ 2r+J(M_r)). \tag{1}
\]
In particular, with \(F(t)=1-[2e^{-wt}-we^{-2t}]/(2-w)\) and \(f(t)=2w(e^{-wt}-e^{-2t})/(2-w)\), the finite-sample CDF of the stricter stopping rank, for every integer \(k\), is
\[
 \Pr\{\tau_2\le k\}=\int_0^\infty rF(t)^{r-1}f(t)
 \sum_{j=0}^{\min(s,k-2r)}{s\choose j}(1-e^{-\delta t})^j e^{-\delta t(s-j)}\,dt, \tag{2}
\]
where the sum is zero if its upper limit is negative.

Suppose \(s=s_r\ge c r\log r\) for every sufficiently large \(r\), with fixed \(c>0\). Put
\[
 q_{1,r}=\tfrac12\log r,\qquad q_{2,r}=(\log r+\log(2/(2-w)))/w,
\]
\[
 a_{j,r}=2r+s_r(1-e^{-\delta_rq_{j,r}}),\qquad
 b_{1,r}=\tfrac{\beta r}{2}e^{-\delta_rq_{1,r}},\qquad
 b_{2,r}=\tfrac{\beta r}{w}e^{-\delta_rq_{2,r}},\quad \delta_r=\beta r/s_r.
\]
Then, **jointly**,
\[
 \left(\frac{\tau_1-a_{1,r}}{b_{1,r}},\frac{\tau_2-a_{2,r}}{b_{2,r}}\right)
 \ \xrightarrow{d}\ (G_1,G_2), \tag{3}
\]
where \(G_1,G_2\) are **independent** standard Gumbel variables, each with \(\Pr(G_j\le x)=\exp(-e^{-x})\). Thus the same pivot sequence has two independent limiting spectral-accuracy fluctuations at distinct resolution thresholds. The centers retain their nonlinear background-occupancy correction when \(s_r\) is only of order \(r\log r\).

## Assumptions and scope
All matrices are real symmetric positive definite; the identical statements hold for complex Hermitian matrices with these real blocks. The pivot law is the **exact residual-diagonal sampling rule**, not greedy Cholesky, stale-weight sampling, or approximate probabilities. The tolerances and numerical ranks refer to **operator norm**, not trace or Frobenius norm. For the finite statement require \(r,s\ge1\), \(\rho\in(0,1)\), \(\beta>0\), and \(\delta<w\). The limit holds for any integer sequence \(s_r\ge c r\log r\), with fixed \(\rho,\beta,c\), without requiring a limit for \(s_r/(r\log r)\). At \(\mu=w\) the weak inequality places the tolerance in the first tier; for \(\mu< w\) it is in the second tier as soon as \(\delta<\mu\).

## Proof
**(1) Spectral states and exponential embedding.** A fresh \(B_\rho\) has eigenvalues \(1+\rho\) and \(1-\rho\); after one pivot its remaining Schur diagonal and sole nonzero eigenvalue are \(w=1-\rho^2\); after two pivots it is zero. An unvisited background singleton has eigenvalue \(\delta<w\). Hence the spectral error is above \(w\) exactly while some block has zero pivots, and it equals \(w\) exactly while none is unvisited but at least one has one pivot. This proves the threshold characterization, including the equality case.

In every untouched correlated block, the two possible pivots have combined diagonal weight \(2\); after the first, the remaining pivot has weight \(w\). Each surviving background singleton contributes \(\delta\). Independent exponential waiting clocks of those rates generate exactly the same conditional next-event probabilities as residual-diagonal sampling, by the memoryless-race identity. Each block's first and second event times are \(U_i\) and \(U_i+V_i\), with independent inter-event intervals. The background events occur at \(Z_j\). At time \(H_r\), every block has first contact, exactly \(L_r\) second contacts are outstanding, and \(J(H_r)\) background events have occurred. At time \(M_r\) every block is fully eliminated. Almost-sure absence of ties yields (1).

**(2) Exact finite stopping distribution.** Convolution of independent exponentials of rates \(2,w\) gives the stated \(F,f\). The largest of \(r\) independent completion times has density \(rF^{r-1}f\). Independently, \(J(t)\sim\operatorname{Binomial}(s,1-e^{-\delta t})\). Conditioning (1) on \(M_r=t\) gives (2), with no asymptotic approximation.

**(3) The two continuous-time maxima are asymptotically independent.** For any fixed real \(x,y\), let \(u=q_{1,r}+x/2\), \(v=q_{2,r}+y/w\). Marginally, \(r\Pr(U_1>u)\to e^{-x}\) and \(r\Pr(U_1+V_1>v)\to e^{-y}\). Since \(w<1\), eventually \(v>u\) and direct integration over the first-event time gives
\[
 \Pr(U_1>u,U_1+V_1>v)
 \le \frac{2}{2-w}e^{-wv-(2-w)u}+e^{-2v}.
\]
The right side is \(O(r^{-2+w/2})+O(r^{-2/w})=o(r^{-1})\). Therefore, with \(p_r\) the single-block probability that neither exceedance occurs,
\[
 \Pr(H_r\le u,M_r\le v)=p_r^r\longrightarrow
 \exp(-e^{-x}-e^{-y}),
\]
which proves joint convergence of \(2(H_r-q_{1,r})\) and \(w(M_r-q_{2,r})\) to **independent** standard Gumbels, not merely marginal Gumbels.

**(4) Transfer from continuous time to discrete pivots.** First \(L_r=o_p(r)\): choose any fixed \(\varepsilon\in(0,1/2)\). With probability tending to one, \(H_r>(1/2-\varepsilon)\log r\); on that event,
\[
 L_r\le\sum_{i=1}^r\mathbf1\{U_i+V_i>(1/2-\varepsilon)\log r\}.
\]
The mean of the right side is \(O(r^{1-w(1/2-\varepsilon)})=o(r)\), by the above hypoexponential tail; Markov's inequality suffices. Second, conditional on any \(t\), the variance of \(J(t)\) is at most \(s\delta t=\beta rt\). Since \(H_r,M_r=O_p(\log r)\), the differences \(J(H_r)-s(1-e^{-\delta H_r})\) and \(J(M_r)-s(1-e^{-\delta M_r})\) are \(O_p(\sqrt{r\log r})=o_p(r)\). This conditional estimate does not require independence of \(J(H_r)\) and \(J(M_r)\).

Third, the centering assumption implies \(\delta_r=O(1/\log r)\) and \(e^{-\delta_r q_{j,r}}\) is bounded away from zero. As the fluctuations of \(H_r-q_{1,r}\) and \(M_r-q_{2,r}\) are tight, Taylor's theorem gives, jointly for \(j=1,2\),
\[
 s(1-e^{-\delta T_j})-s(1-e^{-\delta q_{j,r}})
 =\beta r e^{-\delta q_{j,r}}(T_j-q_{j,r})+o_p(r),
\]
where \(T_1=H_r\), \(T_2=M_r\). Divide (1) by the declared \(b_{j,r}=\Theta(r)\) and combine with step (3). The \(L_r\) and binomial fluctuation terms vanish, proving (3).

## Verification
Run `python CHECK.py` after installing `numpy` and `scipy` listed in `requirements.txt`. The checker compares finite-state recursions for the exact pivot process against the integral (2) at every attainable strict-tier rank in nine small configurations; all passed with absolute error below \(4\cdot10^{-9}\). It also directly reconstructs Schur complements from the matrix and confirms the three-valued block spectral-norm profile. Seeded high-dimensional simulations probe (3), but only the analytical proof above justifies the infinite-dimensional and asymptotic assertions. The local checker output reports its checks; it is not an independent certificate.

## Relationship to prior work
Epperly (2026, first public 2026-08-21) proves expected-error and high-probability trace/operator-norm bounds for RPCholesky and discusses a diagonal coupon-collection lower-bound illustration. The present block model has a second intermediate Schur eigenvalue \(w\), giving *two distinct* stopping rules, their exact linked distributions, and asymptotic **independence** of the critical fluctuations. Neither the cited broad error bounds nor the diagonal coupon example imply that joint law. Chen, Epperly, Tropp, and Webber establish the actual RPCholesky rule and general approximation bounds; Epperly, Tropp, and Webber establish accelerated implementations retaining this pivot law. The general convergence-rate bounds of Divan and Gilles (2026) are relevant, but their full manuscript was not available for material comparison, leaving a bibliographic risk. The proof also uses classical exponential races, binomial thinning, hypoexponential distributions, and extreme-value convergence as standard ingredients. A precise joint two-threshold RPCholesky theorem is the asserted contribution, not these ingredients.

## Limitations
The construction uses identical \(2\times2\) blocks and a diffuse diagonal background whose size grows at least as \(r\log r\). It does not establish independent fluctuations for general matrices, other pivot selection rules, or arbitrary growth of \(s_r\). The Gumbel law is asymptotic and makes no finite-sample tail-error guarantee. Numerical experiments alone do not certify asymptotic conclusions. Some related recently posted manuscripts or appendices could not be fully compared, and novelty is subject to that residual coverage uncertainty. No independent audit has been performed.

## References
1. Ethan N. W. Epperly, *A new analysis of the randomly pivoted Cholesky algorithm* (arXiv:2608.20633v1, first public 2026-08-21). https://arxiv.org/html/2608.20633v1
2. Yifan Chen, Ethan N. Epperly, Joel A. Tropp, Robert J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations* (arXiv:2207.06503). https://arxiv.org/html/2207.06503
3. Ethan N. Epperly, Joel A. Tropp, Robert J. Webber, *Embrace rejection: Kernel matrix approximation by accelerated randomly pivoted Cholesky* (arXiv:2410.03969). https://arxiv.org/html/2410.03969
4. Ryan Divan and Marc Aurèle Gilles, *Convergence rates of randomly pivoted methods for low-rank approximation* (arXiv:2609.06287, first public 2026-09-05; abstract inspected, full text not inspected). https://arxiv.org/abs/2609.06287

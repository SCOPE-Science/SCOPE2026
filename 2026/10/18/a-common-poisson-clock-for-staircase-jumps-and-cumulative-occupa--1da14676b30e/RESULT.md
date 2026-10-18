# A common Poisson clock for staircase jumps and cumulative occupation

## Finding

Consider the discrete Poisson-hyperbolic staircase with parameter \(p\in(0,1]\), starting at \(X_0=1\). At a step from state \(x\), it jumps to \(xU\) with probability \(px\) (with independent \(U\sim\operatorname{Uniform}(0,1)\)) and otherwise stays at \(x\). Let \(N_n\) count strict downward jumps in the first \(n\) steps and let \(A_n=\sum_{m=0}^{n-1}X_m\) be cumulative occupation.

**Quantitative marked-Poisson coupling.** There is a coupling with a standard rate-one Poisson process \(\Pi\) and independent unit-exponential marks \((E_j)_{j\ge0}\), independent of \(\Pi\), on which for **every deterministic triangular choice** \(p=p_n\in(0,1]\) satisfying \(np_n\to\infty\), with \(t_n=\log(np_n)\),
\[
\left|N_n-\Pi(t_n)\right|+
\left|p_nA_n-\sum_{j=0}^{\Pi(t_n)-1}E_j\right|
=O_{\mathbb P}(\log t_n).
\]
An empty marked sum is zero. In particular, the joint central limit theorem is
\[
\boxed{\quad
\frac{(N_n-t_n,\ p_n A_n-t_n)}{\sqrt{t_n}}
\ \Longrightarrow\ \mathcal N_2\!\left(0,
\begin{pmatrix}1&1\\1&2\end{pmatrix}\right).
\quad}
\]
The limiting correlation is \(1/\sqrt2\). This includes fixed \(p\), vanishing \(p_n\), and all other sequences with \(np_n\to\infty\), without a rate condition. The quantitative coupling controls *both* observables by the *same* marked Poisson clock, not just their separate marginal distributions.

As a finite-time calibration (not a new marginal theorem), conditional jump probabilities give \(\mathbb EN_n=p\mathbb EA_n\). The known exact survival law yields
\[
\mathbb EN_n=p\mathbb EA_n
=\sum_{j=1}^n\frac{1-(1-p)^j}{j}
=\log(np)+\gamma+o(1)
\]
for every triangular sequence with \(np\to\infty\), where \(\gamma\) is Euler's constant. This independently confirms the centering.

For \(p=1\), there is also a finite-sample check: writing \(H_j=\sum_{r=1}^j1/r\), one has
\[
\operatorname{Cov}(N_n,A_n)=\sum_{j=2}^n\frac{j-H_j}{j(j+1)}=\log n+O(1),
\]
\[
\operatorname{Var}(N_n)=\sum_{j=1}^n\left(\frac1j-\frac1{j^2}\right)
=\log n+O(1),\qquad
\operatorname{Var}(A_n)=2\log n+O(1).
\]
These agree with the covariance matrix in the limit theorem; they are not substitutes for its joint distributional proof.

## Assumptions and scope

The jump probability is exactly \(px\) and each jump multiplier is an independent continuous uniform random variable, independent of the past and of the decision to jump. The stochastic arrays may use any deterministic \(p_n\in(0,1]\); only \(np_n\to\infty\) is required. The estimates concern the joint distribution under the explicit coupling described below. The initial height is one, time is discrete, and the occupation sum includes time zero but excludes time \(n\). The difference from the convention \(\sum_{m=1}^nX_m\) is bounded by one before multiplication by \(p_n\).

## Proof

**1. Exact record-level renewal representation.** Let \((U_k)_{k\ge1}\) and \((E_k)_{k\ge0}\) be mutually independent iid uniform and mean-one exponential sequences. Put \(a_0=1\), \(a_k=\prod_{r=1}^kU_r\), \(S_0=0\), and \(S_k=-\log a_k\). The increments \(L_k=S_k-S_{k-1}=-\log U_k\) are iid unit exponentials. Consequently \(\Pi(t)=\#\{k\ge1:S_k\le t\}\) is a rate-one Poisson process, independent of the marks \(E_j\).

At level \(a_k\), define \(\lambda_k=pa_k\) and \(h_k=-\log(1-\lambda_k)\). For \(\lambda_k<1\), set \(G_k=\lceil E_k/h_k\rceil\); if \(\lambda_k=1\), set \(G_k=1\). Conditional on the levels, the \(G_k\) are independent geometric waiting times on positive integers with success parameter \(\lambda_k\), independent of the next multiplier \(U_{k+1}\). Thus with \(T_k=\sum_{j=0}^{k-1}G_j\) and \(K_n=\max\{k:T_k\le n\}\), the process \(X_m=a_{K_m}\) has exactly the stated transition kernel, while \(N_n=K_n\). Its occupation satisfies the *exact* identity
\[
 pA_n=\sum_{j=0}^{K_n-1}\lambda_jG_j
   +\lambda_{K_n}(n-T_{K_n}).
\]

**2. Uniform control of discrete waiting-time rewards.** For \(0<\lambda<1\) and \(h=-\log(1-\lambda)\), the elementary inequalities \(\lambda\le h\le\lambda/(1-\lambda)\) imply
\[
\left|\lambda\left\lceil E/h\right\rceil-E\right|
\le (1-\lambda/h)E+\lambda\le\lambda(E+1).
\]
The same inequality holds at \(\lambda=1\) by the stated convention. Thus
\[
D:=\sum_{k\ge0}|\lambda_kG_k-E_k|
\le\sum_{k\ge0}pa_k(E_k+1),\qquad
\mathbb ED\le\sum_{k\ge0}2p\,(1/2)^k=4p\le4.
\]
In particular, \(D=O_{\mathbb P}(1)\) uniformly in \(p\). Also \(G_k\le E_k/\lambda_k+1\); whenever \(\lambda_k\le1/2\), \(h_k\le2\lambda_k\) and hence \(G_k\ge E_k/(2\lambda_k)\).

**3. Comparison of physical and Poisson logarithmic times.** Write \(t=\log(np)\to\infty\), \(q=\lceil3t\rceil\), and \(b=10\log t\). With probability tending to one, all of the following hold simultaneously: \(S_q\ge2t\); for \(j\le q\), \(t^{-3}\le E_j\le3\log t\); for \(1\le j\le q\), \(L_j\le3\log t\); and \(\sum_{j<q}E_j\le6t\). Exponential tails, a union bound over \(O(t)\) variables, and a gamma Chernoff bound prove this event has probability \(1-o(1)\), with constants not depending on \(p\).

For \(k\le q\), monotonicity of \(S_j\) and the upper waiting-time bound give
\[
T_k\le\frac{e^{S_k}}p\sum_{j<k}E_j+k
\le\frac{6t}{p}e^{S_k}+q.
\]
Consequently, every \(k\le q\) with \(S_k\le t-b\) has \(T_k<n\) for sufficiently large \(t\), because \(n=e^t/p\ge e^t\). In the other direction, if \(S_k\ge t+b\), then \(S_{k-1}\ge S_k-3\log t\); the preceding level has \(\lambda_{k-1}\le1/2\), and
\[
T_k\ge G_{k-1}\ge\frac{e^{S_{k-1}}E_{k-1}}{2p}
\ge\frac{e^{S_k}}{2p\,t^6}>n.
\]
The same lower bound at \(k=q\) excludes all larger indices. Since \(\Pi(2t)<q\) with probability tending to one, the two comparisons yield
\[
\Pi(t-b)\le K_n\le\Pi(t+b)
\]
with probability \(1-o(1)\). As \(\Pi(t+b)-\Pi(t-b)\) is Poisson with mean \(2b=20\log t\),
\[
|K_n-\Pi(t)|=O_{\mathbb P}(\log t).
\]

**4. Marked rewards at the random cutoff.** The difference between \(\sum_{j<K_n}E_j\) and \(\sum_{j<\Pi(t)}E_j\) is at most the sum of the marks with indices between \(\Pi(t-b)\) and \(\Pi(t+b)\). These marks are independent of \(\Pi\), and their total has mean \(2b\), hence is \(O_{\mathbb P}(\log t)\). Moreover, \(K_n\le q\) with high probability, so \(E_{K_n}=O_{\mathbb P}(\log t)\). Because \(0\le n-T_{K_n}<G_{K_n}\), step 2 gives
\[
0\le\lambda_{K_n}(n-T_{K_n})
\le\lambda_{K_n}G_{K_n}\le2E_{K_n}+1=O_{\mathbb P}(\log t).
\]
Combining these bounds with \(D=O_{\mathbb P}(1)\) proves the quantitative joint coupling. Every bound above is uniform over deterministic \(p\in(0,1]\) as \(np\to\infty\).

**5. Joint Gaussian limit.** Since the marks are independent of \(\Pi\), the pair
\(
(\Pi(t),\sum_{j<\Pi(t)}E_j)
\) is a compound-Poisson vector with rate one and jump vector \((1,E)\). Its mean is \(t(1,1)\) and its covariance is \(t\begin{psmallmatrix}1&1\\1&2\end{psmallmatrix}\). Expansion of its joint characteristic exponent at arguments of order \(t^{-1/2}\) proves the stated bivariate Gaussian limit. The coupling error \(O_{\mathbb P}(\log t)\) is \(o_{\mathbb P}(\sqrt t)\), so Slutsky's theorem completes the proof.

**6. Exact mean and fixed-parameter covariance checks.** For each integer \(m\ge0\), the conditional transition law yields \(\mathbb EX_m=\int_0^1(1-px)^m\,dx=[1-(1-p)^{m+1}]/[p(m+1)]\). The jump compensator gives \(\mathbb EN_n=p\mathbb EA_n\). Summing the expectations and comparing the geometric-harmonic series with \(\sum_{j\ge1}(1-p)^j/j=-\log p\) proves the exact mean formula above. Its remainder after \(\log(np)+\gamma\) is bounded by a multiple of \(n^{-1}+e^{-np}/(np)\), uniformly for \(p\in(0,1]\) with \(np\to\infty\).

At \(p=1\), the states after positive times are running minima \(M_i=\min(U_1,\dots,U_i)\). For \(1\le i\le j\), a split of the joint-survival integral at the diagonal gives
\[
\operatorname{Cov}(M_i,M_j)
=\frac{i}{(i+1)(j+1)(j+2)}.
\]
If \(I_j\) indicates that \(U_j\) is a new lower record, permutation ranks are independent of order statistics, so \(\operatorname{Cov}(I_j,M_i)=0\) when \(j\le i\); conditioning on \(U_j\) and requiring all earlier observations to exceed it gives for \(i<j\),
\[
\operatorname{Cov}(I_j,M_i)=\frac{i}{(i+1)j(j+1)}.
\]
Summing these two exact identities, and using \(\sum_{i<j}i/(i+1)=j-H_j\), proves the stated covariance asymptotics. The independent classical lower-record indicators give \(\operatorname{Var}(N_n)=\sum_{j\le n}(1/j-1/j^2)\).

## Verification

Run the standalone exact-and-simulation checker with `python3 verify_staircase.py`. It verifies the finite jump-count generating-function recurrence against its independent closed form for several rational parameters, exact running-minimum mixed moments and covariance identities over a range of indices, and two seeded finite coupling sanity checks. All computations are finite evidence only. The theorem for unbounded time and triangular \(p_n\) is established by proof steps 1–5, not by testing.

## Relationship to prior work

Yoshida, *Poisson Hyperbolic Staircase in Discrete Time* (arXiv:2604.22637v1, April 24, 2026), introduces the chain and obtains its marginal and joint-survival functions, a jump-count PGF, a transform for the accumulated states, and martingales. We use the same chain and do not claim these results. The record-minimum realization is an elementary equivalence of the transition kernels. Our assessed contribution is the *joint*, quantitative marked-Poisson coupling, its shared covariance, and uniform validity for triangular \(p_n\) with \(np_n\to\infty\).

The marginal central limit law for sums of iid running minima is classical: Gouet (1989), Berkes–Horváth (2001), and Fahrner (2001) establish limit and stronger invariance results in that setting. We **do not claim** the scalar occupation CLT at fixed \(p\) as new. The separate classical record-count CLT is also standard. Neither set of marginal statements, alone, determines the cross-covariance or an explicit simultaneous logarithmic-rate coupling. Priority comparisons with inaccessible full texts remain incomplete; see limitations.

## Limitations

The theorem requires uniform jump multipliers and a jump probability exactly proportional to height. No statement is proved for other jump kernels, nonuniform record distributions, or \(np_n\) bounded. The error \(O_{\mathbb P}(\log\log(np_n))\) is a valid uniform upper order, not asserted optimal. The Gaussian limit describes weak convergence, not a uniform Berry–Esseen bound. The proof does not establish independent external validation. Earlier literature on joint extremes and record-value times, particularly older works without accessible full text, could contain an equivalent joint representation; priority remains subject to that risk.

## References

1. N. Yoshida, *Poisson Hyperbolic Staircase in Discrete Time*, arXiv:2604.22637v1 (2026), https://arxiv.org/pdf/2604.22637 .
2. R. Gouet, *Embedding in extremal processes and the asymptotic behavior of sums of minima*, Statistics & Probability Letters 8 (1989), 219–223, DOI:10.1016/0167-7152(89)90125-9.
3. I. Berkes and L. Horváth, *The logarithmic average of sample extremes is asymptotically normal*, Stochastic Processes and their Applications 91 (2001), 77–98, DOI:10.1016/S0304-4149(00)00056-9.
4. I. Fahrner, *A strong invariance principle for the logarithmic average of sample maxima*, Stochastic Processes and their Applications 93 (2001), 317–337, DOI:10.1016/S0304-4149(00)00103-4.
5. S. I. Resnick, *Extremal processes and record value times*, Journal of Applied Probability (1973), https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/extremal-processes-and-record-value-times/FC35E651968DB7E28E55865057B3FB17 .

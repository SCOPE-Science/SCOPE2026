# Second-order covariance fluctuations in a fair Pascal bootstrap scenery

## Finding

Consider the inclusion-induced, subset-cardinality-invariant bootstrap transformation with independent fair Bernoulli coefficients. The first-order martingale brackets vanish after division by the number of steps, but their next-order fluctuations distinguish the conditional and averaged probability laws.

Let \(A_n\) be the (unscaled) predictable cross-bracket of its two simple-walk coordinates and define the environment-dependent centering \(C_n=2\sum_{m=0}^{\lfloor n/2\rfloor-1}f_m\), where the signs \(f_m\) are defined below. For almost every coefficient environment, under the conditional walk law, on every bounded interval \([0,T]\),

\[
\left(\frac{A_{\lfloor nt\rfloor}-C_{\lfloor nt\rfloor}}{\sqrt n}\right)_{0\le t\le T}\Longrightarrow(B_t)_{0\le t\le T}
\]

in the Skorokhod \(J_1\) topology, with \(B\) a standard Brownian motion. For almost every fixed environment, the **uncentered** laws of \(A_n/\sqrt n\) are not tight as \(n\to\infty\). In contrast, after averaging over the fair coefficient environment, the uncentered process has the functional limit

\[
\left(\frac{A_{\lfloor nt\rfloor}}{\sqrt n}\right)_{0\le t\le T}\Longrightarrow\left(\sqrt3\,\widetilde B_t\right)_{0\le t\le T},
\]

with \(\widetilde B\) a standard Brownian motion. The annealed variance factor \(3\) decomposes exactly into environmental variance \(2\) and conditional renewal variance \(1\) at leading order. The initial-step convention changes \(A_n\) by at most two and does not affect these limits.

## Assumptions and scope

Let \((\xi_j)_{j\ge1}\) be independent uniform signs taking values \(\{-1,+1\}\), and let \((\beta_k)_{k\ge0}\) be independent fair Bernoulli variables, independent of the walk. Put \(M_0=0\) and \(M_j=\sum_{i=1}^j\mathbf1_{\{\xi_i=-1\}}\). For each integer \(m\ge0\), set

\[
f_m=(-1)^{\sum_{k=0}^{m}\left(\binom{m}{k}\bmod2\right)\beta_k}.
\]

The predictable signs of the inclusion-induced bootstrap are \(\zeta_0=1\) and \(\zeta_j=f_{M_j}\) for \(j\ge1\). Define \(\eta_j=\xi_j\zeta_{j-1}\), \(X_n=\sum_{j=1}^n\xi_j\), \(Y_n=\sum_{j=1}^n\eta_j\), and

\[
A_n=\langle X,Y\rangle_n=\sum_{j=1}^{n}\zeta_{j-1}.
\]

Here the predictable bracket refers to the discrete-time martingale bracket. Conditional (quenched) probability freezes the entire sequence \(\beta\); averaged (annealed) probability samples both \(\beta\) and \(\xi\). All limits hold simultaneously for integer \(T\ge1\), hence on every fixed finite interval.

## Proof

**1. The Pascal scenery is independent and fair.** Lucas's parity theorem identifies the odd entries of row \(m\) as precisely the binary submasks of \(m\). In particular, the exponent defining \(f_m\), reduced modulo two, contains \(\beta_m\) with coefficient one and otherwise depends only on \(\beta_0,\ldots,\beta_{m-1}\). The map from \((\beta_0,\ldots,\beta_r)\) to \((f_0,\ldots,f_r)\) is therefore an invertible triangular affine map over \(\mathbb F_2\). Hence \((f_m)_{m\ge0}\) is an i.i.d. sequence of fair signs under the environment law. Its sums \(F_m=\sum_{j=0}^{m-1}f_j\) satisfy the ordinary strong law, functional central limit theorem and law of the iterated logarithm.

**2. A holding-time representation.** Fix an environment. Each negative input sign advances \(M\) by one; positive signs leave it unchanged. Let \(H_m\) be the number of input draws spent in level \(m\) before the next negative sign, including that terminating draw. Then \((H_m)\) are i.i.d. geometric variables with parameter \(1/2\), independent of the environment, satisfying

\[
\mathbb EH_m=2,\qquad\operatorname{Var}(H_m)=2,\qquad \mathbb EH_m^2=6.
\]

Write \(T_m=\sum_{j=0}^{m-1}H_j\) and \(M_n=\max\{m:T_m\le n\}\). For the bracket with the harmless alternative initial convention \(\zeta_0=f_0\), the exact renewal identity is

\[
A_n=\sum_{m<M_n}H_mf_m+(n-T_{M_n})f_{M_n}.
\]

Returning to the original convention \(\zeta_0=1\) changes the bracket by \(1-f_0\), at most two.

**3. Uniform control of random-index scenery errors.** Fix an integer \(T\ge1\). For every \(\delta>0\), Hoeffding's inequality and a union bound over at most \(O_T(n^2)\) pairs \(0\le i,j\le 2Tn\) separated by at most \(n^{2/3}\) imply

\[
\mathbb P_\beta\!\left(\max_{\substack{0\le i,j\le2Tn\\|i-j|\le n^{2/3}}}|F_i-F_j|>\delta\sqrt n\right)\le O_T(n^2)e^{-\delta^2 n^{1/3}/2}.
\]

The right side is summable. Borel--Cantelli, first over positive rational \(\delta\), then over integers \(T\), gives an environment-full-measure event on which the corresponding maximum is \(o(\sqrt n)\). By the ordinary maximal inequality for the input simple random walk,

\[
\max_{0\le t\le T}\left|M_{\lfloor nt\rfloor}-\lfloor nt/2\rfloor\right|=O_{P^\beta}(\sqrt n),
\]

so \(\max_{t\le T}|F_{M_{\lfloor nt\rfloor}}-F_{\lfloor nt/2\rfloor}|/\sqrt n\to0\) in conditional probability. The largest \(H_m\) with \(m\le Tn+1\), divided by \(\sqrt n\), likewise tends to zero in probability by the geometric tail bound.

**4. Conditional functional central limit theorem.** With \(W_m=\sum_{j=0}^{m-1}f_j(H_j-2)\), the renewal identity and step 3 show, uniformly on \([0,T]\),

\[
\frac{A_{\lfloor nt\rfloor}-2F_{\lfloor nt/2\rfloor}}{\sqrt n}
=\frac{W_{M_{\lfloor nt\rfloor}}}{\sqrt n}+o_{P^\beta}(1).
\]

For each fixed environment, the variables \(f_j(H_j-2)\) are independent, centered, have variance exactly two and possess a uniform exponential-moment neighborhood. The independent-array functional Lindeberg theorem yields \(W_{\lfloor nt/2\rfloor}/\sqrt n\Rightarrow B_t\). Since \(M_{\lfloor nt\rfloor}/n\to t/2\) uniformly on compacts in probability, the random time change preserves this limit. This proves the asserted conditional functional convergence.

**5. Annealed limit and loss of quenched tightness without centering.** The iid scenery functional CLT gives \(2F_{\lfloor nt/2\rfloor}/\sqrt n\Rightarrow\sqrt2\,B_t^{(e)}\) under the environment law. Since the conditional law of the centered process converges for almost every environment to the same fixed standard Brownian law, bounded-continuous test-function factorization and dominated convergence show joint asymptotic independence of the scenery and centered conditional fluctuations. Therefore their sum converges to a Brownian motion with variance rate \(2+1=3\).

Finally, the law of the iterated logarithm for the i.i.d. scenery implies \(\limsup_{m\to\infty}F_m/\sqrt m=+\infty\) and \(\liminf_{m\to\infty}F_m/\sqrt m=-\infty\) for almost every environment. Thus the deterministic centers \(2F_{\lfloor n/2\rfloor}/\sqrt n\) are unbounded along subsequences. The centered conditional family is tight by step 4; translating it by an unbounded deterministic sequence prevents tightness of the uncentered conditional family. This proves all assertions.

## Verification

Run the provided standalone `second_order_checker.py` with Python 3 and no dependencies. Its recorded output is in `second_order_checker_output.txt`. The program checks the invertibility of finite Pascal transforms, renewal-reward identities for all short input histories and environments, and exact variance decompositions; it does not certify an infinite-dimensional functional limit. The infinite results depend on the explicit probabilistic inequalities, Borel--Cantelli and the independent-array invariance principle in the proof.

## Relationship to prior work

Hamza and Tournier, *Are random random walks normal?* (2026), §4.3, Proposition 11 and Corollary 12, establish annealed independent-Brownian convergence of the two-coordinate walk in the entire elliptic cardinality-invariant model. The martingale limit criterion in Collevecchio--Hamza--Shi--Williams (2022) concerns the first-order scaled two-coordinate walk, not the next-order cross-bracket law. Existing first-order quenched results for this specific Pascal-sign scenery yield only the vanishing normalized bracket; they do not supply its environment-dependent central limit centering or the non-tightness phenomenon. The present result is restricted to **fair** coefficient bits, for which the Pascal transform becomes independent fair scenery. Classical iid-sign invariance principles and renewal-reward facts are used as established tools.

## Limitations

The theorem treats exactly one-sided negative-count scenery with independent fair coefficient bits. It does not establish this second-order limit for biased elliptic coefficient sequences, general cardinality-by-time arrays, or arbitrary predictable sign mechanisms. The normal limit for the bracket does not assert independent finite-sample brackets, nonasymptotic error rates, or an independent validation. A general previously published theorem on quenched renewal-reward processes in one-sided random scenery could subsume part of the proof; this historical-coverage risk is not eliminated by keyword searches alone.

## References

1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (first publicly submitted 2026-10-01), especially §4.3, https://arxiv.org/html/2610.01658v1.
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, Electron. J. Probab. 27 (2022), article 92; preprint arXiv:2010.16000, https://arxiv.org/abs/2010.16000.
3. Classical Lucas parity theorem, Hoeffding maximal inequalities, the strong law, law of the iterated logarithm, Borel--Cantelli lemma, and the independent-array functional central limit theorem (standard results used with the hypotheses stated in the proof).

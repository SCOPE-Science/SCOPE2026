# Exact high-start mixing windows and Pareto collapse in a Zipf-disaster chain

## Finding

Fix a real parameter \(\beta>1\). Consider the Markov chain on \(\mathbb N_0\) that, from state \(k\), advances to \(k+1\) with probability \(((k+1)/(k+2))^\beta\) and otherwise resets to zero. Let \(P_i\) denote its law when started at \(X_0=i\), and let \(\pi\) be its stationary distribution. Write \(d_i(n)=d_{\mathrm{TV}}(\mathcal L_i(X_n),\pi)\), with total variation defined as \(\sup_A|P_i(X_n\in A)-\pi(A)|\).

**Exact macroscopic-window theorem.** For every finite \(T>0\), there exists \(I(\beta,T)\) such that for every integer \(i\ge I(\beta,T)\) and every integer \(0\le n\le\lfloor Ti\rfloor\),

\[
 d_i(n)=\left(\frac{i+1}{i+n+1}\right)^\beta
       -\frac{1}{\zeta(\beta)(i+n+1)^\beta}
       =\frac{(i+1)^\beta-\zeta(\beta)^{-1}}{(i+n+1)^\beta}.
\]

The singleton \(\{i+n\}\), representing the path with no reset, uniquely maximizes the **signed positive** discrepancy \(P_i(X_n\in A)-\pi(A)\); its complement uniquely maximizes the opposite signed discrepancy. These are the two absolute-total-variation optimizers. The following explicit finite criterion suffices for the displayed identity to hold simultaneously through any prescribed integer horizon \(N\ge1\):

\[
 \frac{\beta}{(\beta-1)(i+1)}
 \sum_{r=1}^{N}r^{1-\beta}
 <\left(\frac{i+1}{i+N+1}\right)^\beta.
 \tag{1}
\]

For any fixed \(\delta\in(0,1)\), let \(t_{\mathrm{mix}}(i,\delta)=\min\{n\ge0:d_i(n)\le\delta\}\). Then, for all sufficiently large \(i\), its *exact integer value* is

\[
 t_{\mathrm{mix}}(i,\delta)=\left\lceil
 \left(\frac{(i+1)^\beta-\zeta(\beta)^{-1}}{\delta}\right)^{1/\beta}-i-1
 \right\rceil,
 \quad
 t_{\mathrm{mix}}(i,\delta)=(i+1)(\delta^{-1/\beta}-1)+O_{\beta,\delta}(1).
\]

In particular \(d_i(\lfloor it\rfloor)\to(1+t)^{-\beta}\) uniformly for \(t\) on any compact interval of \([0,\infty)\).

**Path-level counterpart.** If \(X^{(i)}\) starts at \(i\) and \(Y_i(t)=X^{(i)}_{\lfloor it\rfloor}/i\), then in \(D([0,T])\) with its Skorokhod \(J_1\) topology, for every fixed \(T<\infty\),

\[
  Y_i\ \Longrightarrow\ Y,\qquad
  Y(t)=(1+t)\mathbf 1_{\{t<\tau\}},\quad
  \Pr(\tau>t)=(1+t)^{-\beta}\quad(t\ge0).
\]

Thus a high initial state grows linearly until one Pareto-time collapse; subsequent excursions are asymptotically invisible on the initial-height scale. This and the exact singleton total-variation event are parts of one finding about the nonuniform relaxation from high initial states.

## Assumptions and scope

The parameter \(\beta>1\) is fixed as \(i\to\infty\); \(\pi_k=(k+1)^{-\beta}/\zeta(\beta)\) for every \(k\ge0\), where \(\zeta(\beta)=\sum_{j\ge1}j^{-\beta}<\infty\). The initial state \(i\) is a positive integer. The criterion (1) also applies at finite \(i\) and \(N\). The process limit is on each fixed finite time horizon, not on horizons growing with \(i\). No statement is asserted for \(\beta\le1\), when the stationary probability law does not exist.

## Proof

**1. The renewal law and a monotonicity lemma.** Put \(a_k=(k+1)^{-\beta}\), \(k\ge0\). A run starting at zero survives at least \(k\) advances with probability \(a_k\). Its first return time has mass \(f_j=a_{j-1}-a_j\), \(j\ge1\). Write \(u_m=P_0(X_m=0)\), so \(u_0=1\) and \(u_m=\sum_{j=1}^m f_j u_{m-j}\).

We verify the needed nonstandard renewal monotonicity, rather than assume it. Let \(A(z)=\sum_{k\ge0}a_kz^k\). The ratios \(a_k/a_{k-1}=(k/(k+1))^\beta\) increase strictly. Define numbers \(c_n\) by \(a_n=\sum_{j=1}^n c_j a_{n-j}\) (\(n\ge1\)). Then \(c_1=a_1>0\); if \(c_j\ge0\) through \(n-1\), the monotonicity of the ratios gives

\[
 \sum_{j=1}^{n-1}c_j a_{n-j}
 \le\frac{a_n}{a_{n-1}}\sum_{j=1}^{n-1}c_j a_{n-1-j}=a_n,
\]

so \(c_n\ge0\). Formal power-series identities now give \(1/A(z)=1-\sum_{n\ge1}c_nz^n\). As \(F(z)=\sum_{j\ge1}f_jz^j=1-(1-z)A(z)\), the renewal generating function obeys

\[
 U(z)=\sum_{m\ge0}u_mz^m=\frac{1}{(1-z)A(z)},
 \qquad u_m-u_{m-1}=-c_m\le0.
\]

Hence \(u_m\) decreases to some limit. Since \(A(1)=\zeta(\beta)\), taking the Abel limit of \((1-z)U(z)=1/A(z)\) shows

\[u_m\downarrow\zeta(\beta)^{-1}=:\pi_0.\]

Stationarity follows directly from \(\pi_kp_k=\pi_{k+1}\) and \(\sum_k\pi_k(1-p_k)=\pi_0\). The last-renewal decomposition gives

\[
 P_0(X_m=k)=a_ku_{m-k}\quad(0\le k\le m),
 \qquad P_0(X_m=k)=0\quad(k>m).
\]

Because \(u_{m-k}\ge\pi_0\), the probability excess over stationarity lies entirely on \(\{0,\ldots,m\}\). Consequently the exact distance from zero is the *known renewal comparison*

\[
 d_0(m)=\sum_{k=m+1}^\infty\pi_k
 =\pi_0\sum_{j=m+2}^\infty j^{-\beta}
 \le\frac{(m+1)^{1-\beta}}{(\beta-1)\zeta(\beta)}.
 \tag{2}
\]

This comparison is used as an auxiliary lemma, not claimed as new; it is consistent with the decreasing-failure-rate renewal theorem of Chevyrev and Korepanov.

**2. Delayed renewal from a high initial state.** Let \(\tau_i=\inf\{n\ge1:X_n=0\}\). Telescoping the advance probabilities yields, for all integers \(m\ge0\),

\[
 s_i(m):=P_i(\tau_i>m)
 =\left(\frac{i+1}{i+m+1}\right)^\beta.
\]

Set \(f_i(j)=s_i(j-1)-s_i(j)\) for \(j\ge1\), and \(v_m^{(i)}=P_i(X_m=0)\) for \(m\ge1\). Conditioning on the first reset gives

\[
 v_m^{(i)}=\sum_{j=1}^m f_i(j)u_{m-j},\qquad
 v_m^{(i)}-\pi_0=-\pi_0s_i(m)
   +\sum_{j=1}^m f_i(j)(u_{m-j}-\pi_0).
 \tag{3}
\]

The mean-value inequality yields \(0<f_i(j)\le\beta/(i+1)\). By (2), \(0\le u_r-\pi_0\le d_0(r)\le\pi_0(r+1)^{1-\beta}/(\beta-1)\). Thus, for every \(1\le m\le N\),

\[
 v_m^{(i)}-\pi_0
 \le -\pi_0s_i(N)
 +\frac{\beta\pi_0}{(\beta-1)(i+1)}
       \sum_{r=1}^N r^{1-\beta}.
 \tag{4}
\]

Under criterion (1), every right-hand side in (4) is strictly negative, hence \(v_m^{(i)}<\pi_0\) for all \(1\le m\le N\). For \(N=\lfloor Ti\rfloor\), the left side of (1) tends to zero as \(i\to\infty\) because \(\beta>1\): it is \(O(i^{1-\beta})\) when \(1<\beta<2\), \(O(\log i/i)\) when \(\beta=2\), and \(O(i^{-1})\) when \(\beta>2\). The right side tends to \((1+T)^{-\beta}>0\). This proves eventual validity of (1) for every fixed \(T\).

**3. Exact sign decomposition and mixing threshold.** At time \(n\) from \(i\ge1\), the probability of the no-reset state \(i+n\) is \(s_i(n)\). If at least one reset has occurred, the state is at most \(n-1\), with

\[
 P_i(X_n=k)=a_kv_{n-k}^{(i)}\quad(0\le k\le n-1).
\]

When (1) holds with \(n\le N\), these probabilities are all strictly below \(a_k\pi_0=\pi_k\); every other state except \(i+n\) has probability zero and thus also lies below stationarity. At \(i+n\), the excess is strictly positive because

\[
 \frac{s_i(n)}{\pi_{i+n}}=\zeta(\beta)(i+1)^\beta>1.
\]

The unique positive-support event of the signed measure \(P_i(X_n\in\cdot)-\pi\) is therefore \(\{i+n\}\); its complement uniquely maximizes the negative direction. This proves the exact total-variation formula and identifies both optimizers for absolute total variation. It also covers \(n=0\) directly. Total-variation contraction makes \(d_i(n)\) nonincreasing in time. Given fixed \(\delta\in(0,1)\), choose \(T>\delta^{-1/\beta}-1\); the exact formula applies through \(\lfloor Ti\rfloor\) for all large \(i\), and its first crossing of \(\delta\) occurs there. Solving the exact inequality and taking a ceiling proves the mixing-time formula. The fixed-\(\delta\) additive \(O(1)\) bound follows by expanding \(((i+1)^\beta-\pi_0)^{1/\beta}=(i+1)+O(i^{1-\beta})\).

**4. The one-shot path limit.** The first-reset survival identity gives \(\tau_i/i\Rightarrow\tau\) with \(P(\tau>t)=(1+t)^{-\beta}\). Before \(\tau_i\), the rescaled chain follows \(1+\lfloor it\rfloor/i\). After this reset, it evolves as a fresh chain started at zero. On a time interval containing at most \(\lfloor Ti\rfloor+1\) excursions, the event that any post-reset excursion reaches height \(r\) is bounded, by the union bound on the independent excursion lengths, by

\[
 (\lfloor Ti\rfloor+1)(r+1)^{-\beta}.
\]

Taking \(r=\lfloor\varepsilon i\rfloor\) makes this probability \(O_{\beta,T,\varepsilon}(i^{1-\beta})\to0\). Thus, on \([0,T]\), the sup-norm distance between \(Y_i\) and the single-jump path \((1+t)\mathbf1_{\{t<\tau_i/i\}}\) vanishes in probability. As the limiting \(\tau\) has a continuous law, the corresponding mapping to the Skorokhod space is almost surely continuous, giving the claimed \(J_1\) convergence.

## Verification

The standalone Python 3 program `check.py` computes all finite-step transition probabilities and delayed renewal masses from **exact rational transition kernels**, and checks the sign of every finite-state discrepancy against exact rational integral-test bounds for stationary zeta values. It also verifies the explicit finite criterion, renewal monotonicity, the singleton-Hahn event, the total-variation identity and two integer mixing thresholds. `check_output.txt` records 10,523 passed finite assertions. These finite computations are supplemental consistency checks; the all-parameter and functional-limit results follow from the four analytic steps above.

## Relationship to prior work

Huillet, *On Divisibility Properties of Zipf Law and Relatives* (arXiv:2610.29974v1, first public October 21, 2026), Section 3, supplies the exactly telescoping total-disaster transition probabilities, excursion tail and invariant Zipf distribution, but does not analyze high-initial-state total-variation maximizing events, integer mixing thresholds or the one-shot path limit. Chevyrev and Korepanov, *Rates of memory loss for null recurrent Markov chains* (arXiv:2501.10169v1), Theorem 2.8 and Lemma 2.9, supply general renewal comparison and temporal-shift memory-loss results from the zero state; the exact distance (2) is consistent with their stronger zero-state renewal theory. Their statements do not provide the new sign comparison for a chain started at an *arbitrarily high state*, nor its sharp state-dependent mixing quantile. Goncalves and Huillet, *Scaling features of two special Markov chains involving total disasters* (arXiv:2101.03853v1), develop general growth-collapse chains and excursions, with a different transition family. Fontes and Schinazi, *Metastability of a random walk with catastrophes* (arXiv:1907.05357v1), prove path limits for a different, absorbing binomial-catastrophe model with scaling parameters; it is not the same recurrent Zipf-disaster process or the singleton total-variation assertion. The proof here makes no novelty claim for the renewal monotonicity lemma or ordinary stationary Zipf law.

## Limitations

The finite-window exact singleton test is proved for each fixed linear-time window \(0\le n\le Ti\) once \(i\) is sufficiently large, and for any explicit finite pair \((i,N)\) satisfying (1). It is **not** asserted for all times at fixed \(i\), nor for \(\beta\le1\). The path limit does not quantify convergence in Skorokhod metric beyond the supplied excursion bound, and does not classify near-critical varying \(\beta\). Earlier work on delayed renewals or catastrophe-chain metastability could contain equivalent formulations not revealed by the inspected texts.

## References

1. T. E. Huillet, *On Divisibility Properties of Zipf Law and Relatives*, arXiv:2610.29974v1 (first public October 21, 2026), https://arxiv.org/abs/2610.29974.
2. I. Chevyrev and A. Korepanov, *Rates of memory loss for null recurrent Markov chains*, arXiv:2501.10169v1 (January 17, 2025), https://arxiv.org/abs/2501.10169.
3. B. Goncalves and T. Huillet, *Scaling features of two special Markov chains involving total disasters*, arXiv:2101.03853v1 (January 11, 2021), https://arxiv.org/abs/2101.03853.
4. L. R. Fontes and R. B. Schinazi, *Metastability of a random walk with catastrophes*, arXiv:1907.05357v1 (July 11, 2019), https://arxiv.org/abs/1907.05357.

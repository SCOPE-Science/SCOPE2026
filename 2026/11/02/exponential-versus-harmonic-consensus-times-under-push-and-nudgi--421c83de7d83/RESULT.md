# Finite harmonic consensus-time bounds for the complete-graph nudging rule

## Finding

Fix a complete graph without loops on \(N\ge2\) vertices. At each update attempt select a vertex independently and uniformly. Use the symmetric external-influence rule (nudging) of Van Santen, Ryckebusch and Rocha [1, Eq. (3)], with trust \(0<\alpha\le1\), field \(0<E<1\) in favor of opinion \(A\), and \(c=1-\alpha\), \(h=\alpha E\). A selected \(B\)-vertex flips with probability \(c f_A+h\), where \(f_A\) is its fraction of \(A\)-neighbors; a selected \(A\)-vertex flips with probability \(\max\{0,c f_B-h\}\), where \(f_B\) is its fraction of \(B\)-neighbors.

**Theorem.** From every initial configuration with \(i<N\) vertices holding \(A\), unanimous \(A\) is reached almost surely. The mean number of update attempts \(T_N^{\rm nudge}(i)\) satisfies
\[
N H_{N-i}\le T_N^{\rm nudge}(i)\le \frac{N}{\alpha E}H_{N-i},
\qquad H_b=\sum_{v=1}^b\frac1v,\quad H_0=0.
\]
The upper bound is exact for \(\alpha=1\). For fixed parameters these inequalities give \(\Theta(NH_{N-i})\) uniformly over nonconsensus starts, thus \(\Theta(N\log N)\) if the number of initial opponents is a positive fraction of \(N\), and \(\Theta(N)\) from one initial opponent.

This gives a quantitative comparison with the asymmetric external-influence rule (push) of the same authors [1, Eq. (2)]. For push, the rate of exponential growth of the mean is \(\int_E^1\log(x/(cx+h))\,dx>0\) uniformly over nonconsensus starts. We give this comparison below as a consequence of prior birth–death theory [2], not a new extinction-time theorem.

## Proof of the nudging bounds

The count \(X_t\) of \(A\)-vertices is a birth–death chain. At \(j<N\), with \(v=N-j\), its up and down probabilities per attempt are
\[
p_j=\frac{v}{N}\left(\frac{cj}{N-1}+h\right),\qquad
q_j=\frac{j}{N}\max\left\{0,\frac{cv}{N-1}-h\right\}.
\]
The endpoint \(N\) is absorbing and there is a positive-probability path of upward steps from every other count. For fixed \(N\) this gives a positive lower bound, over starts, on the chance of absorption within \(N\) steps; iterating this bound proves almost-sure absorption and finite mean time.

If \(q_j>0\), the social terms cancel in \(p_j-q_j\), leaving \(h\). If \(q_j=0\), the difference is at least \(hv/N\). Hence \(p_j-q_j\ge hv/N\) always. With \(V_t=N-X_t\), the harmonic potential obeys, at \(V_t=v>0\),
\[
\mathbb E[H_{V_t}-H_{V_{t+1}}\mid V_t=v]
=\frac{p_j}{v}-\frac{q_j}{v+1}
\ge\frac{p_j-q_j}{v}\ge\frac hN.
\]
It has zero drift at \(v=0\). Summing up to a deterministic time \(m\) gives \(H_{N-i}\ge(h/N)\sum_{t=0}^{m-1}\mathbb P(\tau>t)\) where \(\tau\) is the consensus time; take \(m\to\infty\) for the upper bound. For the lower bound, each of the initially \(B\)-vertices must be selected before consensus. With \(v\) of these vertices still unselected, the next previously unselected one arrives after a geometric wait of mean \(N/v\). Adding these means yields \(NH_{N-i}\). At \(\alpha=1\), \(q_j=0\) and \(p_j=Ev/N\), so the exact mean is \(NH_{N-i}/E\).

## Comparison: specialization of the push extinction-time law

For push the down probability is instead \(q_j^{\rm push}=j(N-j)/(N(N-1))\), with the same \(p_j\). Absorption and finite mean follow as above. The standard birth–death recurrence [2, Eqs. (10)–(14)], applied to the opponent count \(v=N-j\), gives the exact expression in attempts
\[
T_N^{\rm push}(i)=\sum_{k=i}^{N-1}\sum_{j=0}^k\frac{1}{p_j}
\prod_{\ell=j+1}^{k}\frac{\ell}{c\ell+(N-1)h},
\]
where an empty product is 1. In fact, with \(\Delta_j=T_N^{\rm push}(j)-T_N^{\rm push}(j+1)\), the recurrence is \(p_j\Delta_j=1+q_j^{\rm push}\Delta_{j-1}\), with the second summand zero at \(j=0\). Iterating and summing gives the expression.

To see how the prior superthreshold extinction-time law applies, run attempts at rate \(N\) in continuous time, so the actual birth and death rates of the opponent count are \(\lambda_v=Nq_{N-v}^{\rm push}\) and \(\mu_v=Np_{N-v}\). This divides each mean duration in attempts by \(N\). For \(x=v/N\), compare with fixed-profile rates \(\lambda_v^*=Nx(1-x)\) and \(\mu_v^*=Nx[c(1-x)+h]\). For \(1\le v\le N\), \(1\le\mu_v/\mu_v^*\le N/(N-1)\); for \(1\le v<N\), \(\lambda_v/\lambda_v^*=N/(N-1)\), and both births vanish at \(v=N\). Consequently every term of the nonnegative extinction-time sum [2, Eqs. (12)–(14)] changes by a factor between \((N-1)/N\) and \((N/(N-1))^{N-1}\le e\): a term consists of one inverse death rate and at most \(N-1\) birth-to-death ratios. This comparison is uniform over initial counts.

For the fixed profiles the ratio at zero, defined by its continuous limit, is \(1/(c+h)>1\). The positive crossing is \(x_e=1-E\); it is interior and simple, and the rate profiles and their extended ratio are smooth. The effective potential of [2, Eq. (16)] gives the superthreshold action of [2, Eqs. (19)–(20)] as
\[
-\Phi(x_e)=\int_0^{1-E}\log\!\frac{1-x}{c(1-x)+h}\,dx
=\mathcal I_{\alpha,E}:=\int_E^1\log\!\frac{u}{cu+h}\,du.
\]
The boundary-layer factor in Eq. (20) is \(1-(c+h)^v\), bounded below by \(1-(c+h)>0\) for all \(v\ge1\). At the reflecting endpoint \(v=N\) one additionally waits mean \(1/(Nh)\) in the fixed-profile chain before entering \(v=N-1\). Thus this law supplies the same logarithmic rate uniformly for the comparison chain and, by the termwise bounds, for push.

Equivalently, one can read off only the logarithmic rate directly from the exact product: put \(L_N=\sum_{\ell=1}^{N-1}\max\{0,\log[\ell/(c\ell+(N-1)h)]\}\). The product ending at \(k=N-1\) and beginning at \(j+1\) with \(j=\lfloor(N-1)E\rfloor\) realizes \(e^{L_N}\) and occurs for every \(i<N\); its coefficient is at least 1. No product exceeds it, and \(p_j\ge h/N\), so \(e^{L_N}\le T_N^{\rm push}(i)\le (N^3/h)e^{L_N}\). The positive part of the logarithm extends continuously by zero on \([0,E]\). Its Riemann sums give \(L_N/N\to\mathcal I_{\alpha,E}\), confirming the uniform limit in the update-attempt convention. The integral is positive since \(cu+h<u\) on \((E,1]\); for \(\alpha=1\) it is \(\log(1/E)-1+E\).

## Evidence and scope

The new contribution assessed here is the finite uniform harmonic sandwich for the specified nudging kernel, which supplies the fast side of the comparison for these two concrete rules. The exact product and asymptotic mechanism for push are applications of known birth–death results. The original model paper [1] studies simulated prevalence on sparse network ensembles, not the finite complete-graph nudging bounds. The literature comparison is bounded and does not certify priority.

The accompanying `verify_media.py` uses rational finite-state systems and direct configuration transitions to check the kernels, expected times and harmonic inequalities, and gives numerical consistency checks on the comparison rate. These finite checks do not supply the proof for all populations. Parameters are fixed for the population-size comparison. No result for simultaneous updates, sparse graphs, heterogeneous fields, parameter sequences approaching excluded endpoints, or concentration of the consensus time is claimed.

## References

1. N. Van Santen, J. Ryckebusch and L. E. C. Rocha, *Social clustering reinforces external influence on the majority opinion model*, Physica A 648 (2024), 129929, arXiv:2404.02689, DOI 10.1016/j.physa.2024.129929, §§2.2 and 3.1.
2. C. R. Doering, K. V. Sargsyan and L. M. Sander, *Extinction times for birth-death processes: exact results, continuum asymptotics, and the failure of the Fokker-Planck approximation*, arXiv:q-bio/0401016, §§2.1–2.2, Eqs. (10)–(20).

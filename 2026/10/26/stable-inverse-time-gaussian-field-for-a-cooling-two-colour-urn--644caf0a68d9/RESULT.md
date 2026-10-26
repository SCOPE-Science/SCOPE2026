# Stable inverse-time Gaussian field for a cooling two-colour urn

## Finding
Let \(w_0,b_0\geq1\) be integers and let \(p_n\in[0,1]\) be deterministic with \(p_n\to0\). At each discrete time \(n\geq1\), uniformly sample one of the current urn balls, and add a ball of the sampled colour with probability \(1-p_n\), or of the opposite colour with probability \(p_n\), independently conditional on the past. Write \(m=w_0+b_0\), \(Q_n=(W_n-B_n)/(m+n)\), \(a_0=1\), and
\[
a_n=\prod_{k=1}^n\left(1-\frac{2p_k}{m+k}\right),\qquad M_n=Q_n/a_n.
\]
There is a bounded-in-\(L^2\) martingale limit \(M_\infty\) and a limiting imbalance \(Q_\infty=a_\infty M_\infty\), where \(a_\infty=\lim_n a_n\). For every \(0<r<T<\infty\), as \(n\to\infty\), in the Skorokhod space \(D([r,T])\), **stably with respect to the full urn history**,
\[
\left(\sqrt n\,[Q_{\lfloor nt\rfloor}-a_{\lfloor nt\rfloor}M_\infty]\right)_{t\in[r,T]}
\ \Longrightarrow_{\mathrm{st}}\
\left(\sqrt{1-Q_\infty^2}\,B(1/t)\right)_{t\in[r,T]},
\]
where \(B\) is standard Brownian motion independent of the full urn history. The conditional limiting covariance at \(s,t>0\) is exactly
\[
\frac{1-Q_\infty^2}{\max\{s,t\}}.
\]
In particular, \(\sqrt n\,(Q_n-a_nM_\infty)\) converges stably to \(\sqrt{1-Q_\infty^2}\,Z\), \(Z\) standard normal independent of the history. If \(\sum_n p_n/(m+n)=\infty\), then \(Q_\infty=0\), and the limiting process is the un-mixed \(B(1/t)\). If the series converges, \(a_\infty>0\) and the variance coefficient retains the random urn limit (in general nonconstant).

## Assumptions and scope
All urn draws and reinforcement coins are conditionally independent given the current urn configuration, according to the specified probabilities. The deterministic sequence may oscillate and need not be monotone; only \(p_n\to0\) is imposed. There are at least two initial balls, and both colours are initially represented, ensuring the normalizer is strictly positive and the martingale limit nondegenerate. Stable convergence means joint weak convergence with every bounded measurable random element of the underlying terminal sigma-field; the displayed Brownian process lives on an independent extension. For a path claim, \(r>0\) is essential; no convergence at \(t=0\) is claimed.

## Proof
Set \(V_k=+1\) if the new ball is white and \(-1\) if blue, and \(\mathcal F_k\) the urn history through step \(k\). Then \(\mathbb E[V_k\mid\mathcal F_{k-1}]=(1-2p_k)Q_{k-1}\) and, using \(Q_k=[(m+k-1)Q_{k-1}+V_k]/(m+k)\),
\[
\mathbb E[Q_k\mid\mathcal F_{k-1}]=\left(1-\frac{2p_k}{m+k}\right)Q_{k-1}.
\]
Thus \(M_k=Q_k/a_k\) is a martingale with increments
\[
D_k=M_k-M_{k-1}=\frac{V_k-(1-2p_k)Q_{k-1}}{(m+k)a_k},
\quad \mathbb E[D_k^2\mid\mathcal F_{k-1}]=
\frac{1-(1-2p_k)^2 Q_{k-1}^2}{(m+k)^2a_k^2}.
\]
Since \(p_k\to0\), logarithmic product comparison gives \(a_{\lfloor nt\rfloor}/a_n\to1\) uniformly on any compact \(t\)-interval in \((0,\infty)\); equivalently \(a_n\) and \(a_n^{-1}\) are slowly varying. In particular \(a_n^{-1}=n^{o(1)}\) and \(\sum_k (k^2a_k^2)^{-1}<\infty\). The increments are orthogonal in \(L^2\), so \(M_k\to M_\infty\) almost surely and in \(L^2\). As \(a_k\downarrow a_\infty\), also \(Q_k\to Q_\infty=a_\infty M_\infty\) almost surely. Moreover the strictly positive first conditional variance implies \(\operatorname{Var}(M_\infty)>0\).

Fix \(0<r<T\). Define a forward martingale path
\[
H_n(t)=\sqrt n\,a_n\sum_{k=\lfloor nr\rfloor+1}^{\lfloor nt\rfloor}D_k,\quad r\le t\le T.
\]
Its predictable quadratic variation, uniformly in \(t\in[r,T]\), satisfies
\[
\langle H_n\rangle(t)
=n a_n^2\sum_{k=\lfloor nr\rfloor+1}^{\lfloor nt\rfloor}
\frac{1-(1-2p_k)^2 Q_{k-1}^2}{(m+k)^2a_k^2}
\xrightarrow{a.s.}(1-Q_\infty^2)\left(\frac1r-\frac1t\right).
\]
Indeed, on the block the slowly varying ratios approach one uniformly, while \(p_k\to0\) and \(Q_k\to Q_\infty\) almost surely; the remaining sum is a Riemann sum for \(\int_r^t u^{-2}\,du\). Jumps satisfy \(\sup_{r\le t\le T}|\Delta H_n(t)|\le C_{r,T}/\sqrt n\) since \(|V_k-(1-2p_k)Q_{k-1}|\le2\). The stable martingale functional central limit theorem therefore yields, jointly with every bounded \(\mathcal F_\infty\)-measurable variable,
\[
H_n(\cdot)\Longrightarrow_{\mathrm{st}}\sqrt{1-Q_\infty^2}\,\widetilde B(1/r-1/\cdot),
\]
where \(\widetilde B\) is independent Brownian motion. The stable independence can also be seen by first testing observables measurable with respect to a fixed \(\mathcal F_K\), taking \(n r>K\), and approximating arbitrary bounded terminal observables by their \(\mathcal F_K\)-conditional expectations.

To pass from finite blocks to future-tail fluctuations, let \(R>T\). The process \(\sqrt n a_n(M_{\lfloor nt\rfloor}-M_{\lfloor nR\rfloor})=H_n(t)-H_n(R)\) on \([r,T]\) has the corresponding Gaussian limit. The omitted tail \(\sqrt n a_n(M_{\lfloor nR\rfloor}-M_\infty)\) has second moment at most
\[
4n a_n^2\sum_{k>\lfloor nR\rfloor}\frac1{(m+k)^2a_k^2}.
\]
By the tail form of Karamata's theorem for \(a_k^{-2}\), this expression tends to \(4/R\). Hence the tail vanishes in \(L^2\), uniformly in \(t\in[r,T]\), as \(R\to\infty\). The Gaussian limit as \(R\to\infty\) is \(\sqrt{1-Q_\infty^2}B(1/t)\), with the asserted inverse-time covariance. Finally replace the multiplier \(a_n\) by \(a_{\lfloor nt\rfloor}\), uniformly on \([r,T]\): their ratio tends uniformly to one, and the tail process is tight. This gives exactly the stated limit for \(Q_{\lfloor nt\rfloor}-a_{\lfloor nt\rfloor}M_\infty\).

The product is positive because \(2p_k/(m+k)<1\), and \(\sum_k[2p_k/(m+k)]^2<\infty\). Thus \(a_\infty>0\) if and only if \(\sum_k p_k/(m+k)<\infty\). In the divergent case \(Q_\infty=0\) and the Gaussian field is independent of the urn history. In the summable case \(a_\infty>0\); the variance is genuinely random, for example when \(p_k\equiv0\), \(w_0=b_0=1\), the classical Pólya law makes \(Q_\infty\) uniform on \((-1,1)\).

## Verification
A standalone exact-rational verifier checks the urn distribution recursion, the martingale's expectation identity, and its conditional-variance-driven second moment recursion over 320 checks, using four positive initial compositions and two nonconstant probability schedules. Three additional slowly varying product diagnostics illustrate the logarithmic cooling regimes; these finite computations are not evidence of functional weak convergence. The infinite-dimensional result rests on the displayed martingale functional CLT and Karamata tail estimate, with hypotheses verified above.

## Relationship to prior work
Fan and Qi, arXiv:2610.16065v1 (public October 12, 2026), prove first-order martingale limits for general time-dependent-memory elephant walks; the present urn is the seeded two-colour formulation. The first-order limit and logarithmic product phenomena are **prior results, not asserted novel here**. James, James and Qi (2008) treat general time-dependent correlated Bernoulli sequences and establish laws of large numbers and first-order CLTs. González-Navarrete, Lambert and Vázquez Guevara (2024), Kubota and Takei (2019), and Tokumitsu (2026) obtain fluctuations and/or stable functional limits for constant memory; their fixed-parameter formulas do not imply the inhomogeneous cooling, random-versus-deterministic variance crossover in the present statement. The new target is the terminal-centered stable **functional** field for arbitrary vanishing reversal schedules. Gava and Rezende (2021) study Gaussian fluctuations of correlated Bernoulli processes; their full article could not be inspected, and whether a general result there subsumes part of the present functional statement remains a priority risk.

## Limitations
The theorem is specific to a deterministic cooling schedule and the two-colour single-addition urn. The random centering involves a future limit and need not be observable at finite times. No rate of weak convergence or uniform result down to time zero is proved. The Gaussian field may be degenerate on an event where \(|Q_\infty|=1\), though the zero-mutation positive-seed example has strictly positive variance almost surely. The inaccessible full text of Gava–Rezende (2021), and possible extensions of martingale functional CLTs under other terminology, are residual novelty risks. Independent validation has not been performed.

## References
1. X. Fan and Y. Qi, *A Generalized Elephant Random Walk with Time-Dependent Memory*, arXiv:2610.16065v1 (2026-10-12), Sections 2–3.
2. B. James, K. James and Y. Qi, *Limit theorems for correlated Bernoulli random variables*, Statistics & Probability Letters 78 (2008), 2339–2345, DOI 10.1016/j.spl.2008.01.104.
3. M. González-Navarrete, R. Lambert and V. H. Vázquez Guevara, *A complete characterization of a correlated Bernoulli process*, Electronic Communications in Probability 29 (2024), 69, DOI 10.1214/24-ECP637.
4. N. Kubota and M. Takei, *Gaussian Fluctuation for Superdiffusive Elephant Random Walks*, Journal of Statistical Physics 177 (2019), 1157–1171.
5. G. Tokumitsu, *Stable functional CLTs for scaled elephant random walks*, arXiv:2603.13690v1 (2026-03-14).
6. R. J. Gava and B. L. F. Rezende, *Some limit theorems for dependent Bernoulli random variables*, Statistics & Probability Letters 170 (2021), 109010, DOI 10.1016/j.spl.2020.109010; full text not available for comparison.

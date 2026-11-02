# A stationary immigration–death limit for critical expiring coupon windows

## Finding

At the critical sliding-window length \(M_n=\lfloor n(\log n+c)\rfloor\), the entire stationary missing-coupon count converges to an immigration–death process, not merely to a one-time Poisson variable. The resulting first stationary completion time has a nonexponential limit with an explicit transform:
\[
D_n\Rightarrow Y,\qquad
\mathbb E e^{-s\tau}=\left[s\int_0^1u^{s-1}e^{\lambda u}\,du\right]^{-1},
\quad \lambda=e^{-c},\quad s>0.
\]
Here \(Y\) has immigration rate \(\lambda\), death rate \(j\) in state \(j\), and equilibrium law \(\operatorname{Poisson}(\lambda)\). This is a statement about stationary windows; it does not describe the first completion time of a collector initially holding no coupons.

## Assumptions and scope

Fix any \(c\in\mathbb R\) and \(T>0\). For all sufficiently large integers \(n\), let \((X_k)_{k\in\mathbb Z}\) be independent and uniform on \(\{1,\ldots,n\}\) and let \(M_n=\lfloor n(\log n+c)\rfloor\). At integer index \(k\), define \(A_{n,k}\) as the set of labels missing from \((X_{k-M_n+1},\ldots,X_k)\). Set \(D_n(t)=|A_{n,\lfloor nt\rfloor}|\), a right-continuous piecewise-constant process. Define \(\tau_n=\inf\{t\ge0:D_n(t)=0\}\), including \(\tau_n=0\) if the initial window is complete. Write \(\lambda=e^{-c}>0\).

The claim is weak convergence in the usual Skorokhod \(J_1\) space \(D([0,T],\mathbb Z_{\ge0})\), for each fixed \(T\). Let \(Y\) be the stationary continuous-time Markov chain with generator
\[
(Qf)(j)=\lambda[f(j+1)-f(j)]+j[f(j-1)-f(j)],
\]
with the second term zero at \(j=0\). The stationary distribution is Poisson with mean \(\lambda\). Define \(\tau=\inf\{t\ge0:Y(t)=0\}\).

## Proof

**1. Rare marked gaps in the Poissonized sequence.** Start with a stationary Poisson process of total rate \(n\) on the real line and mark each point independently uniformly in \(\{1,\ldots,n\}\). Thinning produces independent stationary rate-one Poisson processes, one for each label. Write \(L_n=\log n+c\). A label is absent from a sliding time interval of length \(L_n\) precisely when its present-age exceeds \(L_n\). Each Poisson interarrival gap of length \(G>L_n\) produces one absence interval, beginning \(L_n\) after the earlier arrival, with duration \(G-L_n\). The memoryless property gives \(G-L_n\mid G>L_n\sim\operatorname{Exp}(1)\).

For a fixed bounded interval \(I\), each label has at most one such absence-interval starting point in \(I\) for all large \(n\): two successive starts must be separated by more than \(L_n>|I|\). Stationary Poisson Campbell counting gives its start probability exactly \(|I|e^{-L_n}=|I|\lambda/n\). Conditional on a start, its location is uniform in \(I\) and its duration has an independent unit exponential law. Independence across labels and the law of small numbers now imply convergence of the pooled marked starts on \(I\times(0,\infty)\) to a Poisson process of intensity \(\lambda\,dt\,e^{-v}dv\). This argument holds jointly on any fixed finite union of bounded intervals (or by their partition).

To recover the stationary population of active absence intervals, use starts in \([-B,T]\). Intervals started earlier than \(-B\) that survive into \([0,T]\) have expected number at most \(\lambda e^{-B}\), by stationarity and exponential overshoots. First let \(n\to\infty\), then \(B\to\infty\). Mapping finitely many marked points to their interval-overlap count is \(J_1\)-continuous whenever endpoints are distinct and avoid \(0,T\), properties holding almost surely for the limiting marked Poisson process. Thus the Poissonized absent-label process converges on \([0,T]\) to the stationary \(M/M/\infty\) occupancy process. Its generator is \(Q\), since starts arrive at rate \(\lambda\) and each active interval terminates independently at rate one.

**2. Return to the fixed-draw window.** Index the rate-\(n\) Poisson points in increasing order so that indices near calendar time zero match the centered iid mark sequence. By the maximal inequality for centered sums of independent exponential waiting times, on the index range \(|k|\le Cn\log n\) containing all relevant endpoints,
\[
\max |T_k-k/n|=O_{\mathbb P}\bigl(\sqrt{\log n/n}\bigr).
\]
Any fixed \(C>2\) sufficiently large for \(T\) and \(c\) works. Take \(\delta_n=n^{-1/3}\), so the above maximum is \(o_{\mathbb P}(\delta_n)\). An absence interval created by two consecutive draws of the same label, with indices \(i<j\), has discrete rescaled endpoints \(((i+M_n)/n,j/n)\) when \(j-i>M_n\); its continuous-time counterpart has endpoints \((T_i+L_n,T_j)\) when \(T_j-T_i>L_n\). Corresponding endpoints differ by \(O_{\mathbb P}(\delta_n)\) on the relevant index range.

It remains to prevent a near-threshold geometric gap from appearing in just one representation. Among the \(O(n\log n)\) potential starting indices, the next equal-label index has geometric waiting law of parameter \(1/n\). Uniformly, the probability of a gap in a band of width \(O(n\delta_n)\) about \(M_n\) is \(O(\delta_n/n)\), because \((1-1/n)^{M_n}\sim\lambda/n\). The expected number of threshold-straddling gaps is therefore \(O(\delta_n\log n)=o(1)\). With high probability the two processes have the same finite set of start/finish jumps on \([0,T]\), with corresponding times differing by \(o(1)\). A deterministic piecewise-linear time change between successive jumps proves \(J_1\) convergence of the original fixed-draw process to the same \(Y\).

**3. First stationary completion.** The chain \(Y\) is irreducible and positive recurrent, so \(\tau<\infty\) almost surely. Its visits to zero contain nondegenerate holding intervals: the first departure from zero has an exponential waiting time of rate \(\lambda\). For integer-valued cadlag paths, \(J_1\) convergence to a path whose first zero visit has a holding interval makes the first-zero functional continuous, after excluding a null set of jump times at fixed interval endpoints. Tightness of \(\tau_n\) follows from finite-horizon path convergence and \(\Pr(\tau>T)\to0\) as \(T\to\infty\). Hence \(\tau_n\Rightarrow\tau\).

**4. Hitting-time transform and its mean.** The equilibrium probability of state zero is \(\pi_0=e^{-\lambda}\). Starting the immigration–death process at zero, the probability of remaining at zero at time \(t\), allowing intermediate excursions, is
\[
p_{00}(t)=\exp[-\lambda(1-e^{-t})],
\]
because only immigrants surviving to time \(t\) matter. The strong Markov property at \(\tau\) gives the convolution identity \(\pi_0=\int_{[0,t]}p_{00}(t-u)\Pr(\tau\in du)\). Its Laplace transform is
\[
\frac{\pi_0}{s}=\mathbb E e^{-s\tau}\int_0^\infty e^{-st}p_{00}(t)\,dt.
\]
The substitution \(u=e^{-t}\) gives \(\int_0^\infty e^{-st}p_{00}(t)dt=e^{-\lambda}\int_0^1u^{s-1}e^{\lambda u}du\), and thus
\[
\mathbb E e^{-s\tau}=\frac{1}{s\int_0^1u^{s-1}e^{\lambda u}\,du}.
\]
Expanding \(s\int_0^1u^{s-1}e^{\lambda u}du=1+s\int_0^1u^{s-1}(e^{\lambda u}-1)du\) and taking \(s\downarrow0\) yields
\[
\mathbb E\tau=\int_0^1\frac{e^{\lambda u}-1}{u}\,du.
\]
The latter is the expectation of the limit \(\tau\); convergence of \(\mathbb E\tau_n\) is not asserted.

## Verification

The standalone script `verify.py` exhaustively enumerates small sliding-window words and checks finite one-time and two-time missing-label moments in exact fractions; it also checks the equilibrium detailed-balance relation, the predicted critical covariance, and independent quadratures for the Laplace transform. Its recorded execution passed 186 deterministic assertions. The exact finite-dimensional identities used are
\[
\mathbb E[(D_n(0))_r]=(n)_r(1-r/n)^{M_n},
\]
and, with \(p=(1-1/n)^M\) and \(0\le k\le M\),
\[
\mathbb E[D_n(0)D_n(k/n)]
=n(1-1/n)^{M+k}+n(n-1)(1-2/n)^{M-k}(1-1/n)^{2k}.
\]
In particular \(\mathbb E D_n(0)\to\lambda\) and \(\operatorname{Cov}(D_n(0),D_n(t))\to\lambda e^{-t}\) at each fixed \(t\ge0\), consistent with the limiting process. Finite tests do not prove process convergence.

## Relationship to prior work

Long [1, Sections 3 and 8.3] gives the exact finite sliding-window completion-entry flux and notes the ordinary stationary Poisson occupancy crossover at the critical window, but does not derive the stationary missing-label path law or its stationary first-zero hitting distribution. Attrill and Garoni [2, Lemma 4.9 and Theorem 4.10] already identify this same immigration–death process and its stationary zero-hitting transform for a **different, independently refreshed clumsy-coupon model**. Their formula is therefore not claimed as a new queueing identity here. The contribution is to prove a functional critical-window limit for deterministic sliding expiration and transfer the known first-zero law to its stationary completion process. Long [3] addresses reset, clumsy, careless and combined independent-loss mechanisms, not this functional critical-window result. Standard Poisson superposition, memorylessness, and \(M/M/\infty\) identities are known ingredients.

## Limitations

The starting windows are two-sided stationary, not initially empty. The convergence is on fixed time intervals and then for the first-zero distribution, without a rate or finite-size moment convergence. The source manuscript [1] explicitly distinguishes the initially empty first-completion problem at criticality; the present hitting limit must not be substituted for that problem. The proof assumes iid uniform coupons and deterministic common expiration, and gives no result for unequal weights or random expiration. Historical priority beyond the compared sources is not independently established; general Poisson-clumping or queueing limit theorems might offer an alternative implication.

## References

[1] C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1, first posted 2026-04-29, https://arxiv.org/abs/2604.26298.

[2] L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206v1, first posted 2026-05-14, https://arxiv.org/abs/2605.14206.

[3] C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1, first posted 2026-05-14, https://arxiv.org/abs/2605.14511.

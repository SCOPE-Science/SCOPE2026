# Studentized Gaussian fluctuations of the coupon collector's terminal singleton count

## Finding

For every integer \(n\ge2\), draw independent coupons uniformly from \(n\) types until every type has appeared. Let \(T_n\) be the number of draws through the first complete collection, and let \(U_n\) be the number of types appearing **exactly once** in those draws (equivalently, the unfilled slots of the first sibling's album). Put
\[
Y_n=\frac{T_n}{n}-\log n,\qquad B_n=(\log n)e^{-Y_n}=n(\log n)e^{-T_n/n}.
\]
Then the following **joint, studentized second-order limit** holds:
\[
\boxed{\left(\frac{U_n-B_n}{\sqrt{B_n}},Y_n\right)\ \Longrightarrow\ (Z,G),}
\]
where \(Z\) is standard normal, \(G\) has the standard Gumbel distribution \(\Pr(G\le y)=\exp(-e^{-y})\), and \(Z\) and \(G\) are independent. Equivalently, if \(E\) is mean-one exponential independent of \(Z\),
\[
\boxed{\left(\frac{U_n-B_n}{\sqrt{\log n}},Y_n\right)\ \Longrightarrow\ (\sqrt E\,Z,-\log E).}
\]
The random centering \(B_n\), computable from the observed completion time, removes the order-\(\log n\) fluctuations responsible for the previously known exponential limit and exposes independent, order-\(\sqrt{\log n}\) Gaussian residual noise.

A key exact finite-\(n\) identity under an independent exponential-clock embedding is as follows. Write \(M_n\) for the physical time at the last first arrival among \(n\) independent rate-one Poisson processes, with the coupon sequence obtained by ordering all their arrivals. The associated singleton count is the same \(U_n\). For every \(m>0\),
\[
\boxed{U_n\mid M_n=m\ \overset d=\ 1+\operatorname{Bin}\left(n-1,\frac{m}{e^m-1}\right).}
\]
In particular its joint law with \(M_n\) has density, for \(1\le u\le n\),
\[
\frac{\Pr(U_n=u,M_n\in dm)}{dm}=n\binom{n-1}{u-1}e^{-m}(me^{-m})^{u-1}
\big[1-(1+m)e^{-m}\big]^{n-u}.
\]
Moreover, for each fixed \(K>0\), there are finite constants \(C_K\) and \(n_K\) such that for \(n\ge n_K\), uniformly in \(m\in[\log n-K,\log n+K]\), the conditional distribution of
\[
\frac{U_n-(\log n)n e^{-m}}{\sqrt{(\log n)n e^{-m}}}\quad\text{given }M_n=m
\]
is within \(C_K/\sqrt{\log n}\) of the standard normal distribution in Kolmogorov distance.

## Assumptions and scope

The coupon labels are independent and uniform on a fixed collection of \(n\) distinct types. Collection ceases immediately after the final previously unseen coupon. Only the first sibling's missing count, namely the number of singleton types, is treated. The limit is as \(n\to\infty\), with no nonuniform weights, time-dependent sampling, or additional stopping rules. The exact conditional law conditions on the *physical completion time of the Poisson embedding* \(M_n\), not on the discrete draw count \(T_n\); those random variables are related asymptotically, but their finite conditional laws are not interchangeable.

## Proof

**1. Embedding and exact conditional law.** Let \(N_1,\ldots,N_n\) be independent rate-one Poisson processes, with independent first-jump times \(F_1,\ldots,F_n\), each \(\operatorname{Exp}(1)\). The merged jump labels form a uniform independent coupon sequence. Almost surely exactly one first jump is last, at \(M_n=\max_i F_i\). The maximum has density
\[
f_{M_n}(m)=ne^{-m}(1-e^{-m})^{n-1},\qquad m>0.
\]
Conditioned on the last index and \(M_n=m\), all remaining processes are independent Poisson processes conditioned to have a first arrival before \(m\); this follows directly by factorization of the independent process laws, or by conditioning on each event \(\{N_i(m)\ge1\}\). Each count at \(m\) is therefore an independent \(\operatorname{Poisson}(m)\) variable conditioned to be positive. The last-index process has count exactly one at \(m\). The chance a positive Poisson count equals one is
\[
p(m)=\frac{me^{-m}}{1-e^{-m}}=\frac{m}{e^m-1}.
\]
This proves the shifted-binomial identity. Multiplying its binomial mass function by \(f_{M_n}\) and cancelling the factors \(1-e^{-m}\) yields the displayed joint density. This derivation covers every \(n\ge2\), \(m>0\), and attainable \(u\).

**2. Conditional Gaussian fluctuations.** Put \(L=\log n\). For \(m=L+y\) with \(y\) in a fixed compact interval, uniformly in \(y\),
\[
(n-1)p(m)=Le^{-y}+ye^{-y}+O_K(L/n),\qquad
(n-1)p(m)(1-p(m))=Le^{-y}+O_K(1).
\]
Consequently the binomial mean differs from \(Le^{-y}\) by a bounded quantity, and its variance divided by \(Le^{-y}\) converges uniformly to one. Since the binomial conditional variance is bounded below by a positive multiple of \(L\), the elementary binomial Berry--Esseen inequality yields a Kolmogorov bound \(O_K(L^{-1/2})\) after normalization by its exact mean and variance. Replacing those normalizers with \(Le^{-y}\) and \(\sqrt{Le^{-y}}\) introduces another \(O_K(L^{-1/2})\) in Kolmogorov distance, using the bounded density of a standard normal and uniform control of the scale ratio. The constant last coupon contributes only \(O_K(L^{-1/2})\). This proves the asserted uniform conditional bound.

**3. Independence from the completion extreme.** As a maximum of \(n\) independent exponentials,
\[
\Pr(M_n-L\le y)=\left(1-\frac{e^{-y}}n\right)^n\longrightarrow e^{-e^{-y}}
\]
for fixed \(y\). This limit implies tightness of \(M_n-L\). Conditional on \(M_n=m\), Step 2 shows that the characteristic function of the normalized singleton count converges uniformly, on each compact interval in \(m-L\), to \(\exp(-t^2/2)\). Multiplying by any bounded continuous function of \(m-L\), integrating against the distribution of \(M_n\), and discarding arbitrarily small tails by tightness proves the joint convergence
\[
\left(\frac{U_n-Le^{-(M_n-L)}}{\sqrt{Le^{-(M_n-L)}}},M_n-L\right)
\Longrightarrow(Z,G),\qquad Z\ \text{independent of}\ G.
\]
Equivalently, this follows by bounded conditional characteristic functions plus the uniqueness theorem for joint characteristic functions. No independence claim is made at finite \(n\).

**4. De-Poissonization.** The inter-arrival durations of the merged Poisson process are independent \(\operatorname{Exp}(n)\) variables, independent of its coupon labels. Conditional on the discrete completion count \(T_n\), its continuous completion time \(M_n\) is a sum of \(T_n\) such durations. With \(H_n=\sum_{k=1}^n k^{-1}\), the classical elementary coupon-stage decomposition gives \(\mathbb E T_n=nH_n\), hence
\[
\mathbb E\left(M_n-\frac{T_n}{n}\right)^2=\frac{\mathbb E T_n}{n^2}=\frac{H_n}{n}=O\left(\frac{\log n}{n}\right).
\]
Therefore \(\sqrt{\log n}(M_n-T_n/n)\to0\) in probability. Since \(M_n-\log n\) is tight, both random centerings \(Le^{-(M_n-L)}\) and \(Le^{-(T_n/n-L)}=B_n\) are of order \(L\) in probability, and their difference is \(o_{\Pr}(\sqrt L)\): on an event with \(|M_n-L|\le K\) and \(|M_n-T_n/n|\le1\), the mean value theorem bounds it by \(L e^{K+1}|M_n-T_n/n|\). Their square-root ratio converges to one in probability. Slutsky's theorem applied to Step 3 proves the first displayed joint limit for the **original discrete stopping time** \(T_n\).

Finally, \(e^{-G}\) has the \(\operatorname{Exp}(1)\) distribution. Multiplying the first coordinate by \(\sqrt{B_n/L}=e^{-Y_n/2}\), a continuous function of the second coordinate, gives the mixed-normal representation, with \(Z\) independent of the exponential mixing variable.

## Verification

The standalone standard-library program `checker.py` evaluates the singleton law by two independent finite mechanisms for all \(2\le n\le10\): exact rational absorption probabilities of the unseen/singleton Markov chain and exact integration of the Poissonized joint density by finite alternating Gamma sums. It also checks the known harmonic mean and finite variance identity. Run `python3 checker.py`. The program makes 90 exact rational assertions. These checks confirm finite identities in the specified range; Steps 1--4, not the enumeration, establish the exact general identity and infinite limiting theorem.

## Relationship to prior work

Ilienko's extended collector analysis (first publicly posted February 3, 2020; later published in 2026) establishes joint *leading-scale* exponential limits for sibling deficits and joint Gumbel limits for collection times through point-process arguments. Papanicolaou and Doumas (first posted May 11, 2020) establish the first sibling's exponential limit \(U_n/\log n\Longrightarrow\operatorname{Exp}(1)\). Long's 2026 treatment obtains monotonicity, extremality, and fixed-album-index joint leading exponential laws, using exponential order statistics and conditional Bernoulli structure. The present assertion is the finer, random-time-centered \(\sqrt{\log n}\) Gaussian fluctuation law **jointly with the completion extreme**, including asymptotic independence and a uniform conditional normal bound; it is not an implication of leading-scale convergence alone. Classical Poissonization and binomial normal approximation are used rather than claimed as inventions. The first-order exponential limit is recovered but is not presented as novel.

## Limitations

The result does not cover nonuniform coupon weights, subsequent siblings, growing sibling indices, or a Gaussian approximation conditional on an exactly specified discrete stopping count. Historical priority outside the inspected literature, particularly general occupancy central-limit theory at random stopping times, is not exhaustively resolved. Independent validation has not been performed.

## References

1. A. Ilienko, *Limit theorems in the extended coupon collector's problem*, arXiv:2002.00650 (first posted February 3, 2020); later *Modern Stochastics: Theory and Applications* (2026), https://doi.org/10.15559/26-VMSTA306 ; https://www.vmsta.org/journal/VMSTA/article/358/text .
2. V. G. Papanicolaou and A. V. Doumas, *The Coupon Collector's Brother*, arXiv:2005.05270 (first posted May 11, 2020), https://arxiv.org/abs/2005.05270 .
3. A. V. Doumas and V. G. Papanicolaou, *The Siblings of the Coupon Collector*, arXiv:1412.4346 (first posted December 14, 2014), https://arxiv.org/abs/1412.4346 .
4. C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635 (first posted June 28, 2026), https://arxiv.org/abs/2606.29635 .
5. L. Holst, *On birthday, collectors', occupancy and other classical urn problems*, *International Statistical Review* **54** (1986), 15--27, https://doi.org/10.2307/1403255 .

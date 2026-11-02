# Marked-excursion coupling and the critical-drift crossover for random-walk sign changes

## Finding

The following is one joint theorem concerning returns and sign changes of a Bernoulli random walk. Its exact finite-horizon and critical-window statements hold for the same excursion marking mechanism.

**Exact conditional law.** Let \(S_0=0\) and \(S_j=\sum_{i=1}^j X_i\), with independent steps \(\Pr(X_i=1)=p\), \(\Pr(X_i=-1)=q=1-p\), where \(0<p<1\). Define
\[
K_{2m}=\sum_{j=1}^{2m}\mathbf 1_{\{S_j=0\}},\qquad C_{2m+1}=\sum_{j=1}^{2m}\mathbf 1_{\{S_{j-1}S_{j+1}<0\}}.
\]
For every integer \(m\ge0\), conditional on the **entire absolute-value path** \((|S_0|,\ldots,|S_{2m+1}|)\),
\[
C_{2m+1}\sim\operatorname{Bin}(K_{2m},1/2).
\]
In particular, if \(F_p(z)=1-\sqrt{1-4pqz}\), then, as a formal power-series identity in \(z\) (and analytically wherever its denominator series converges),
\[
\sum_{m\ge0}z^m\mathbb E[u^{K_{2m}}v^{C_{2m+1}}]
=\frac{\sqrt{1-4pqz}}{(1-z)\{1-u(1+v)F_p(z)/2\}}.
\]
For \(p=q=1/2\), its coefficient form is
\[
\Pr(K_{2m}=r,C_{2m+1}=s)=4^{-m}\binom{2m-r}{m}\binom rs,\quad 0\le s\le r\le m.
\]
For \(p\ne 1/2\), the eventual number \(C_\infty\) of sign changes is geometric on nonnegative integers with success parameter \(2|2p-1|/(1+|2p-1|)\).

**Critical-drift joint functional limit.** Fix \(a\in\mathbb R\). For each large integer \(n\), run a fresh walk with \(p_n=(1+a/\sqrt n)/2\). Put
\[
K_n(t)=\sum_{j=1}^{\lfloor nt\rfloor}\mathbf 1_{\{S_j=0\}},\qquad C_n(t)=\sum_{j=1}^{\lfloor nt\rfloor-1}\mathbf 1_{\{S_{j-1}S_{j+1}<0\}},\quad 0\le t\le 1.
\]
Then, in the Skorokhod \(J_1\) topology on càdlàg paths (with continuous limits),
\[
\left(n^{-1/2}K_n(t),\ n^{-1/4}\{2C_n(t)-K_n(t)\}\right)_{0\le t\le1}
\ \Longrightarrow\ \left(L_t^{(a)}, W_{L_t^{(a)}}\right)_{0\le t\le1},
\]
where \(L^{(a)}\) is standard semimartingale local time at zero of \(B_t+at\), with \(B\) standard Brownian motion, and \(W\) is a standard Brownian motion independent of \(B\). Thus the second-order fluctuations are Gaussian conditionally on local time but not generally Gaussian unconditionally. More explicitly, the right-continuous inverse of \(L^{(a)}\) is a possibly killed subordinator whose Laplace exponent is \(\sqrt{a^2+2\lambda}\). Hence for \(\lambda>0\), \(\theta\ge0\),
\[
\int_0^\infty e^{-\lambda t}\mathbb E e^{-\theta L_t^{(a)}}\,dt
=\frac{\sqrt{a^2+2\lambda}}{\lambda\{\theta+\sqrt{a^2+2\lambda}\}}.
\]

## Assumptions and scope

The walk is nearest-neighbour on \(\mathbb Z\), begins at zero, and has independent identically distributed steps with fixed \(p\in(0,1)\) for finite-horizon statements. The triangular near-critical array has fixed \(a\in\mathbb R\) and sufficiently large \(n\) so \(0<p_n<1\). No assumptions about a random environment, non-nearest-neighbour steps, or nonindependent steps are made. All convergence is in distribution, not an almost-sure coupling.

## Proof

**1. Conditional fair signs.** Fix any realizable path of the absolute values through an odd time \(2m+1\). Its zeros separate \(r=K_{2m}\) completed excursions followed by one nonempty incomplete excursion. For each completed excursion the numbers of \(+1\) and \(-1\) steps are equal. Reflecting any such excursion therefore leaves its probability unchanged, even for \(p\ne q\). Consequently its sign is an independent fair bit, conditional on the full absolute-value path; the terminal incomplete excursion's sign may be biased, but it is independent of the preceding fair bits. If \(E_1,\ldots,E_{r+1}\) denote excursion signs, the transformation from \((E_1,\ldots,E_r)\) to \((\mathbf1_{E_i\ne E_{i+1}})_{i=1}^r\), for any fixed terminal sign \(E_{r+1}\), is a bijection. The transition bits are therefore independent Bernoulli\((1/2)\), even conditional on the full absolute-value path. Exactly these sign transitions are counted by \(C_{2m+1}\).

**2. Exact renewal generating function.** The first return \(T\) to zero has
\[
\Pr(T=2\ell)=2\,\operatorname{Cat}_{\ell-1}(pq)^\ell,\qquad
\mathbb E[z^{T/2};T<\infty]=F_p(z)=1-\sqrt{1-4pqz}.
\]
The survival series \(Q_p(z)=\sum_{m\ge0}\Pr(T>2m)z^m\) equals \((1-F_p(z))/(1-z)\). Decomposing at the \(r\) completed return excursions, the coefficient generating function of \(K_{2m}=r\) is \(F_p(z)^rQ_p(z)\). By Step 1, the conditional generating factor for \(C\) is \(((1+v)/2)^r\). Summing the geometric series in \(r\) gives the stated bivariate transform. At \(p=1/2\), coefficient extraction using \(F=1-\sqrt{1-z}\) gives the displayed binomial product; it is also independently verified by exact path enumeration. For \(p\ne1/2\), \(F_p(1)=1-|2p-1|\), hence \(K_\infty\) is geometric with success probability \(|2p-1|\); Bernoulli thinning then yields the claimed geometric law for \(C_\infty\).

**3. Excursion-clock limit.** Let \(T_{n,i}\) be the successive iid first-return durations for the \(n\)-th walk, allowing \(\infty\) for escape. For fixed \(\lambda\ge0\), the preceding exact transform yields
\[
\sqrt n\bigl(1-\mathbb E[e^{-\lambda T_{n,1}/n};T_{n,1}<\infty]\bigr)
=\sqrt n\sqrt{1-4p_nq_ne^{-2\lambda/n}}\longrightarrow\sqrt{a^2+2\lambda}.
\]
It follows from the Laplace transforms of independent increments that the increasing partial-return-clock process \(n^{-1}\sum_{i\le\lfloor u\sqrt n\rfloor}T_{n,i}\) converges, up to killing, to the subordinator with exponent \(\sqrt{a^2+2\lambda}\). Its Lévy measure has a positive density proportional to \(t^{-3/2}e^{-a^2t/2}\), so the un-killed part is strictly increasing. The standard monotone inverse-continuity argument then gives uniform-on-compact-in-probability convergence in law of the inverse return counts \(K_n(t)/\sqrt n\) to the continuous inverse \(L_t^{(a)}\). The inverse identification follows from the Brownian first-hitting-time Laplace transform for local time, with local-time normalization \(\mathbb E L_1^{(0)}=\sqrt{2/\pi}\).

**4. Independent mark limit and composition.** The sign-transition bits from Step 1 can be sampled as iid fair coins independent of the entire return-time sequence and its terminal escape event. Write \(\eta_i=2\mathbf1_{E_i\ne E_{i+1}}-1\). Donsker's theorem yields \(n^{-1/4}\sum_{i\le\lfloor u\sqrt n\rfloor}\eta_i\Rightarrow W_u\), independently of the return clock, because these are independent factors. Composition with the inverse clock yields \(W_{L_t^{(a)}}\). The difference between \(2C_n(t)-K_n(t)\) and the completed-return mark sum is bounded by one uniformly in \(t\), due to a possible return at the final observed time for which the next excursion sign is not yet observed. This proves the claimed joint convergence. Integration of the identity \(\Pr(L_t^{(a)}>u)=\Pr(D_u^{(a)}\le t)\), with a one-sided Laplace transform in \(t\), proves the last formula.

## Verification

The accompanying `biased_crossing_verifier.py` exhaustively enumerates all \(2^{2m+1}\) walks for \(0\le m\le5\) at four exact step probabilities \(1/3,2/5,3/4,1/2\), compares every conditional absolute-path distribution with an exact binomial, and compares the complete joint law with a second derivation using formal-series coefficients. It reproduced 4,644 exact rational assertions. The separate `crossing_verifier.py` exhaustively checks the symmetric coefficient identity through \(m=8\) and various moment identities (922 assertions). These checks confirm finite cases only; the all-parameter and functional statements are analytically proved above.

## Relationship to prior work

Siripraparat and Jongpreechaharn (2026) obtain non-uniform half-normal approximation bounds for the marginal sign-change count of a symmetric walk and identify a joint treatment involving returns as a natural further question. Döbler (2013) derives separate return and sign-change marginal laws and sharp one-dimensional approximation rates. Neither inspected work states the conditional full-absolute-path binomial coupling for biased walks or the joint critical-drift second-order limit. De Vos and Vervaat (1988) derive generating functions of local times, a related but different observable; the available abstract does not decide whether the joint marking identity is implied by its full text. General marked-renewal invariance principles can supply an abstract time-change step, but the bias-uniform conditional thinning, exact parameter-dependent transform and explicit killed inverse clock still require identification here. No claim is made to invent general renewal-subordinator theory.

## Limitations

The result does not give a uniform rate in the functional limit, extend to dependent increments, or establish independence between \(L_t^{(a)}\) and the walk endpoint. Only the independent auxiliary noise \(W\) is independent of the Brownian path. The finite checker does not establish the infinite-dimensional theorem. Historical priority remains partly uncertain in older local-time, discrete excursion, and marked-renewal literature; in particular, the full 1988 local-time paper was not available in the inspected material. Independent mathematical audit has not been performed.

## References

- T. Siripraparat and S. Jongpreechaharn, *Distributional approximations for the number of sign changes and the maximum value of a symmetric random walk*, Journal of Inequalities and Applications 2026, article 62, published 2026-03-31. https://doi.org/10.1186/s13660-026-03463-2
- C. Döbler, *Stein's method for the half-normal distribution with applications to limit theorems related to the simple symmetric random walk* (2013). https://arxiv.org/abs/1303.4592
- J. C. de Vos and W. Vervaat, *Local Times of Bernoulli Walk*, Statistica Neerlandica 42 (1988), 1–16. https://doi.org/10.1111/j.1467-9574.1988.tb01516.x
- W. Feller, *An Introduction to Probability Theory and Its Applications*, Volume I, third edition (1968), simple random-walk returns and sign changes.

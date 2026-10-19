# Pressure staircases and two-scale renewal clocks for superlacunary gap shifts

## Finding
Let \(1=a_1<a_2<\cdots\) be increasing positive integers with \(a_{j+1}/a_j\to\infty\). In the two-sided binary shift \(X_a\), consecutive symbols \(1\) are separated by a distance belonging to \(\{a_j:j\ge1\}\) (equivalently, by \(a_j-1\) zero symbols). For a finite real penalty \(t\) per symbol \(1\), let \(P(t)\) be the pressure of the potential \(-t\mathbf1_{[1]}\), and \(\mu_t\) its equilibrium state.

For every finite \(t\), the equilibrium state is unique, its pressure is positive and is the unique solution of
\[
 e^{-t}\sum_{j\ge1}e^{-a_jP(t)}=1.
\]
Under \(\mu_t\), successive distances between markers are independent with probabilities \(q_j(t)=\exp(-t-a_jP(t))\), in their Palm (marker-conditioned) order.

Fix \(s\in(0,1)\) and put \(t_n(s)=\log(n-1+s)\), \(p_n=P(t_n(s))\). Write \(L_n=a_n\), and select a stationary configuration under \(\mu_{t_n(s)}\). Then, as \(n\to\infty\):

1. **Pressure staircase:** \(a_np_n\to-\log s\), locally uniformly for \(s\in(0,1)\).
2. **Gap condensation:** a marker-conditioned gap has length \(a_n\) with probability asymptotic to \(s/n\), yet the probability that a stationary observation time lies inside such a gap tends to \(1\). The mean marker-to-marker distance is asymptotic to \(s a_n/n\).
3. **Macroscopic clock:** if \(\Xi_n\) is the point measure of starting positions of length-\(a_n\) gaps, with positions divided by \(a_n\), then
\[
 \Xi_n\ \Longrightarrow\ \sum_{k\in\mathbb Z}\delta_{k-U},\qquad U\sim\operatorname{Uniform}[0,1].
\]
Convergence is in the vague topology of locally finite point measures on \(\mathbb R\).
4. **Microscopic correction:** if \(\Delta_n\) denotes the distance between consecutive starts of length-\(a_n\) gaps in marker-Palm order, then
\[
 \frac{\Delta_n-a_n}{a_{n-1}}\ \Longrightarrow\ G_s,
 \qquad \Pr(G_s=k)=\frac{s}{(s+1)^{k+1}},\quad k=0,1,2,\ldots.
\]
For any fixed finite number of successive macroscopic gaps, these corrections converge jointly to independent copies of \(G_s\); the stationary phase \(U\) is asymptotically independent of those corrections.

For the canonical factorial-distance shift \(a_j=j!\), the staircase and condensation have the sharper forms (uniformly for \(s\) in any compact subinterval of \((0,1)\))
\[
 n!p_n=A_s-\frac{A_s}{sn}+o(n^{-1}),\qquad
 \Pr_{\mu_{t_n(s)}}(0\text{ lies in an }n!\text{-gap})
 =1-\frac1{sn}+o(n^{-1}),
 \qquad A_s=-\log s.
\]
In that case \(n(\Delta_n/n!-1)\Longrightarrow G_s\), and the mean inter-marker distance is asymptotic to \(s(n-1)!\).

## Assumptions and scope
The permitted distances are strictly increasing positive integers, with \(a_1=1\) and divergent successive ratios. Each integer \(n\) indexes a *different penalty*, not a different shift. The pressure is natural-log pressure. The time-stationary law is the two-sided shift-invariant renewal measure; a "gap containing time zero" is the marker interval \([k,k+a_j)\) containing coordinate zero. In \(\Xi_n\), only starts of the distinguished *exact* distance \(a_n\) are counted, not all marker positions. Compact \(s\)-ranges exclude the singular boundaries \(s=0,1\). No theorem about arbitrary sparse gap sets, full unmarked-point-process convergence, or the crossover when \(s\) itself varies with \(n\) is claimed.

## Proof
**1. Pressure and equilibrium measure.** For \(p>0\), the sum \(F(p)=\sum_j e^{-pa_j}\) is finite, strictly decreasing, and tends from infinity to zero as \(p\) runs from zero to infinity. Hence there is exactly one \(p=P(t)>0\) satisfying \(F(p)=e^t\). Set \(q_j=e^{-t-pa_j}\), a probability distribution with finite mean \(m=\sum_j a_jq_j\). The stationary renewal process with independent gap lengths of law \(q\) defines an invariant probability \(\mu_t\).

For any *ergodic* invariant probability \(\nu\) with positive marker frequency \(\rho\), induce the shift at marker times. Its gap-symbol process has marginal law \(r\), mean gap \(\sum_j a_jr_j=1/\rho\) by Kac's formula, and entropy rate at most \(H(r)\). Abramov's formula and nonnegativity of relative entropy give
\[
 h_\nu(\sigma)-t\rho\le\rho(H(r)-t)
 =p-\rho D(r\Vert q)\le p.
\]
Equality requires \(r=q\) and independence of successive gaps. Any ergodic invariant measure without markers is the all-zero point mass, with pressure contribution zero, strictly below \(p\). By ergodic decomposition, \(p\) is the topological pressure and \(\mu_t\) its unique equilibrium state. This also verifies all normalization constants used below.

**2. Superlacunary estimates.** Put \(b_{j,n}=a_j/a_n\). Divergence of successive ratios implies
\[
 \sum_{j<n}b_{j,n}\longrightarrow0,
 \qquad \sum_{j>n}b_{j,n}e^{-c b_{j,n}}\longrightarrow0
 \quad\text{for each fixed }c>0.
\]
Indeed, eventually consecutive lengths more than double, so the first sum is bounded by twice \(a_{n-1}/a_n\) plus a vanishing finite prefix; the second is dominated by \(\sum_{k\ge0}2^k b_{n+1,n}e^{-c2^k b_{n+1,n}}\), which vanishes as \(b_{n+1,n}\to\infty\). These estimates also control the upper-tail probabilities without the factor \(b_{j,n}\).

Writing \(x_n=a_np_n\), its defining equation is
\[
 \sum_{j<n}e^{-x_nb_{j,n}}+e^{-x_n}
 +\sum_{j>n}e^{-x_nb_{j,n}}=n-1+s.
\]
For \(x\) in any fixed positive compact interval, the left side minus \(n-1\) converges uniformly to \(e^{-x}\). Monotonicity brackets the root to obtain \(x_n\to A_s=-\log s\), locally uniformly in \(s\in(0,1)\). Therefore
\[
 q_n=\frac{e^{-x_n}}{n-1+s}\sim\frac{s}{n},\quad
 q_{n-1}\sim\frac1n,\quad
 m=\frac{\sum_j a_j e^{-x_n b_{j,n}}}{n-1+s}
 \sim\frac{s a_n}{n}.
\]
The stationary time fraction in \(a_n\)-gaps is the exact size-biased probability
\[
 \pi_n=\frac{a_nq_n}{m}
 =\frac{e^{-x_n}}{e^{-x_n}+\sum_{j\ne n}b_{j,n}e^{-x_nb_{j,n}}}
 \longrightarrow1.
\]

**3. Two scales of the clock.** Starting from a length-\(a_n\) gap, continue through a geometrically distributed number of other gaps until the next length-\(a_n\) gap. Write the intervening total length as \(W_n\); then \(\Delta_n=a_n+W_n\). Independence of gaps gives the *exact* Laplace transform, for \(u\ge0\),
\[
 \mathbb E e^{-uW_n/a_{n-1}}=
 \frac{q_n}{q_n+\sum_{j\ne n}q_j(1-e^{-ua_j/a_{n-1}})}.
\]
Divide the denominator by \(q_n\). The contribution of \(j=n-1\) converges to \((1-e^{-u})/s\). The contribution of \(j<n-1\) is bounded by \(u\sum_{j<n-1}a_j/(a_{n-1}e^{-x_n})\to0\), and that of \(j>n\) tends to zero exponentially in \(a_{n+1}/a_n\). Thus the transform tends to \(s/(s+1-e^{-u})\), the transform of the asserted geometric law. Successive \(W_n\)'s are independent, proving finite-dimensional independence.

Moreover
\[
 \frac{\mathbb E W_n}{a_n}
 =\frac{\sum_{j\ne n}a_jq_j}{a_nq_n}
 =\frac{1-\pi_n}{\pi_n}\longrightarrow0.
\]
A stationary time lies in an \(a_n\)-gap with probability \(\pi_n\to1\). Conditional on that event, its integer offset within the gap is uniform on \(\{0,\ldots,a_n-1\}\), independent of the gaps on either side. The rescaled offset converges to \(U\sim\operatorname{Uniform}[0,1]\). By Markov's inequality and the preceding mean-delay bound, every fixed number of neighboring \(a_n\)-gap starts lies within \(o_{\Pr}(a_n)\) of the corresponding points \(\{k-U:k\in\mathbb Z\}\). Their separation is at least \(a_n\), so this finite-neighbor control implies vague convergence of the full locally finite start-point measures. It also yields independence of the limiting phase and the finite collection of microscopic corrections.

**4. Factorial refinement.** For \(a_j=j!\), the elementary identity
\[
 \sum_{j<n}\frac{j!}{n!}=\frac1n+O(n^{-2})
\]
and exponentially negligible tails above \(n\) (uniform for \(x\) in any positive compact interval) sharpen the root equation to
\[
 s=e^{-x_n}-\frac{x_n}{n}+o(n^{-1}).
\]
Taylor expansion at \(A_s=-\log s\) gives \(x_n=A_s-A_s/(sn)+o(n^{-1})\). The same factorial sum and time-size bias show
\[
 1-\pi_n=\frac1{sn}+o(n^{-1}),\qquad
 \frac{\mathbb E W_n}{n!}=\frac1{sn}+o(n^{-1}).
\]
Finally \(a_{n-1}=n!/n\), converting the universal microscopic limit into \(n(\Delta_n/n!-1)\Longrightarrow G_s\). Every asserted asymptotic has now been justified.

## Verification
The accompanying `verify.py` uses only Python's standard library. It independently solves the normalized pressure equation by bisection for factorial gaps, compares the pressure root and its first correction, computes the length-biased occupation fraction and exact renewal delay, and compares exact non-long-gap Laplace transforms with the geometric limit for several values of \(s\) and \(n\). It also checks small exact renewal-composition identities. Run `python3 verify.py` alongside this document. Finite tests support, but do not prove, the infinite-size limits, whose proofs are above.

## Relationship to prior work
Climenhaga and Thompson (arXiv:1011.2780, first public version 2010-11-11) prove intrinsic ergodicity for \(S\)-gap shifts and their factors at zero potential. Their Section 3.3 even uses gaps of factorial size, specifically \((2n)!\), to demonstrate failure of almost specification; neither the factorial example nor their uniqueness theorem gives the present parameter-dependent two-scale gap law. Baker and Ghenciu (arXiv:1411.7167, first public version 2014-11-26, especially their Proposition 2.1) record the classical entropy equation; its weighted renewal counterpart here is elementary and *not* claimed as a novel general thermodynamic formalism. Ramirez and Somers (arXiv:2501.08438) extend entropy formulas to \((S,w)\)-gap shifts and discuss mixing; their full text contains neither the parameter-window limit nor the geometric inter-clock correction.

Geometrically spaced gap shifts have separate log-periodic pressure/entropy phenomena, but their ratios of consecutive allowed distances remain bounded, whereas the hypotheses here force those ratios to diverge. The factorial (and broader superlacunary) clock and its microscopic geometric perturbations therefore are not consequences of a fixed-ratio geometric-gap result. General renewal Palm-size bias is a standard ingredient; the contribution is its joint, explicitly parameterized pressure-to-clock limit under the superlacunary scaling. A broader unidentified renewal limit theorem may still subsume this result; independent priority assessment remains open.

## Limitations
The theorem excludes the parameter boundary layers \(s\downarrow0\) and \(s\uparrow1\), which may have additional scales. It describes exact \(a_n\)-gap starts, not every marker in the growing observation window, and gives no finite-\(n\) total-variation rate for the whole point process. The weighted pressure equation, inducing, and size-bias identities are established tools; novelty is asserted only for the combined superlacunary two-scale limit and factorial refinement, subject to independent literature review.

## References
1. V. Climenhaga and D. J. Thompson, *Intrinsic ergodicity beyond specification: beta-shifts, S-gap shifts, and their factors*, arXiv:1011.2780v1 (2010-11-11), https://arxiv.org/abs/1011.2780.
2. S. Baker and A. E. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, arXiv:1411.7167v1 (2014-11-26), https://arxiv.org/abs/1411.7167.
3. C. Ramirez and A. Somers, *(S,w)-Gap Shifts and Their Entropy*, arXiv:2501.08438v2 (2025), https://arxiv.org/pdf/2501.08438.
4. Standard induced-map entropy and stationary-renewal facts: Abramov's entropy formula, Kac's return-time formula, and the elementary equilibrium length-bias identity; all uses are explicitly reduced to formulas above.

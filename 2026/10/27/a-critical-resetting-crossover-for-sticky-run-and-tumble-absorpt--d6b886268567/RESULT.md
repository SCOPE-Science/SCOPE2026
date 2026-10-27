# A critical resetting crossover for sticky run-and-tumble absorption

## Finding

A run-and-tumble particle moves on the half-line and attaches to the boundary at each collision. The boundary holds it for a random duration, then absorbs it with probability \(\theta\) or returns it to the bulk. When the holding-time Laplace transform satisfies \(1-\phi(s)=c\sqrt{s}+o(\sqrt{s})\), its long binding-time tail competes exactly with the intrinsic square-root return-time tail of unbiased run-and-tumble motion.

**Critical weak-absorption and weak-resetting law.** Fix \(\alpha,v,x_0,c>0\), a starting velocity \(k_0\in\{-,+\}\), a desorption protocol \(P\), and a nonnegative constant \(R\). Let the absorption probability at each completed binding period be \(\theta\in(0,1)\), and let the bulk resetting rate be \(r_\theta=R\theta^2\). If \(T_\theta\) is the time of final absorption, then

\[
\theta^2T_\theta\ \Longrightarrow\ Y_R^{(P)},\qquad
\mathbb E\big[e^{-zY_R^{(P)}}\big]
=\frac{1}{1+c\sqrt z+A_P z/\sqrt{z+R}},\quad z\geq0,
\]

where the coefficient \(A_P\) depends on desorption:

\[
A_{\mathrm{wall}}=\sqrt{\frac2\alpha},\qquad
A_{\mathrm{home},-}=\frac{x_0}{v}\sqrt{2\alpha},\qquad
A_{\mathrm{home},+}=\sqrt{\frac2\alpha}+\frac{x_0}{v}\sqrt{2\alpha}.
\]

Here *wall* means detachment into the right-moving state from \(x=0\), and *home* means immediate replacement by the original state \((x_0,k_0)\). The renewal duration \(T_\theta\) always begins at the original state \((x_0,k_0)\). Only bulk motion is subject to resetting; a bound particle is never reset.

For any fixed \(R>0\),

\[
\Pr(Y_R^{(P)}>t)\sim\frac{c}{\sqrt{\pi t}}\qquad(t\to\infty),
\]

whereas at exactly \(R=0\),

\[
\Pr(Y_0^{(P)}>t)\sim\frac{c+A_P}{\sqrt{\pi t}}.
\]

Thus \(Y_R^{(P)}\Rightarrow Y_0^{(P)}\) as \(R\downarrow0\), but the far-tail amplitude has a discontinuous zero-reset limit. The limit is ordered in the Laplace-transform sense as \(R\) increases; this is **not** asserted to be ordinary stochastic dominance. For left-moving initial orientation, the two protocols have identical limiting laws precisely at \(\alpha x_0/v=1\); home desorption has the larger Laplace transform when \(\alpha x_0/v<1\), and wall desorption has the larger one when \(\alpha x_0/v>1\). For right-moving initial orientation, wall desorption always has the larger limiting Laplace transform.

The limit has a constructive representation. Let \(E\) be exponential with mean one, independent of a stable subordinator \(S_c\) with exponent \(c\sqrt z\) and an independent subordinator \(Z_{A_P,R}\) with exponent \(A_Pz/\sqrt{z+R}\). Then

\[
Y_R^{(P)}\ \stackrel d=\ S_c(E)+Z_{A_P,R}(E).
\]

The second subordinator has the explicit Lévy density

\[
A_P e^{-Rt}\left(\frac1{2\sqrt\pi\,t^{3/2}}+\frac R{\sqrt\pi\,t^{1/2}}\right)\,dt\quad(t>0),
\]

which distinguishes a reset-tempered return mechanism from the untempered heavy-tailed binding mechanism. The exact fixed-time renewal transforms and the ordinary heavy-tail minimum-exponent principle are prior methodology, not claimed as new. The claim concerns the critical **joint** scaling, its explicit law, two desorption coefficients, subordinator decomposition, and noncommuting far-tail limits.

## Assumptions and scope

The particle occupies \(x\geq0\), moves at velocity \(+v\) or \(-v\), and flips velocity at an independent Poisson rate \(\alpha>0\). During bulk motion a separate Poisson clock of rate \(r_\theta\) instantaneously restores \((x_0,k_0)\), with \(x_0>0\). On its first encounter with \(x=0\) while moving left, it binds immediately. Every visit draws a fresh independent nonnegative bound duration \(W\) with transform \(\phi\), independent of a Bernoulli absorption decision of probability \(\theta\). Failure leads either to wall desorption \((0,+v)\) or to home desorption \((x_0,k_0)\). The process repeats until absorption, and no reset clock acts during binding. Assume

\[
1-\mathbb E[e^{-sW}]=c\sqrt s+o(\sqrt s),\qquad s\downarrow0,\quad c>0.
\]

For example \(\Pr(W>t)=(1+t/\tau)^{-1/2}\) with \(\tau>0\) gives \(c=\sqrt{\pi\tau}\). There is no finite mean bound duration. All statements hold for fixed positive \(\alpha,v,x_0,c\), each fixed \(R\geq0\), and \(\theta\downarrow0\); they do not assert uniformity when \(R\) grows with \(1/\theta\).

## Proof

**1. Bare first-passage transforms.** Let \(H_{x,k}\) be the first encounter with the wall for motion without resetting. The backward generator is \(vk\partial_x+\alpha(\mathcal S-I)\), where \(\mathcal S\) reverses velocity. For \(s>0\), the bounded solution with the left-moving boundary condition \(\mathbb E[e^{-sH_{0,-}}]=1\) gives

\[
a_-(s)=e^{-x_0\sqrt{s(s+2\alpha)}/v},\quad
a_+(s)=b(s)e^{-x_0\sqrt{s(s+2\alpha)}/v},\quad
b(s)=\frac{\alpha}{s+\alpha+\sqrt{s(s+2\alpha)}}.
\]

Here \(b(s)\) is the transform of the first return after starting at the wall moving right. The boundary-value calculation can be reconstructed by substituting the decaying exponential \(e^{-\sqrt{s(s+2\alpha)}x/v}\) into the two backward equations; it also agrees with the wall-return transform in the motivating source (its equation (2.23)). In particular,

\[
a_{k_0}(s)=1-A_{\mathrm{home},k_0}\sqrt s+O(s),\qquad
b(s)=1-A_{\mathrm{wall}}\sqrt s+O(s).
\]

The coefficients follow from \(\sqrt{s(s+2\alpha)}=\sqrt{2\alpha s}+O(s^{3/2})\).

**2. Exact resetting decomposition.** Write \(a=a_{k_0}(s+r)\). Conditioning on whether the first bulk reset precedes adsorption gives the transform from the original state,

\[
F_{r,\mathrm{home}}(s)=\frac{(s+r)a}{s+ra}.
\]

A bulk excursion starting from the wall in the right-moving state has transform

\[
F_{r,\mathrm{wall}}(s)=\frac{s b(s+r)+r a}{s+ra}.
\]

These formulas are valid also at \(r=0\), by continuity, and follow from independent exponential resetting rather than any waiting-time approximation. Let \(g_P\) be respectively \(a\) or \(b(s+r)\). Then for both desorption protocols the **exact** identity

\[
1-F_{r,P}(s)=\frac{s\big(1-g_P(s+r)\big)}{s+r a_{k_0}(s+r)}
\]

holds. The initial bulk adsorption transform is \(F_{r,\mathrm{home}}\) in either protocol.

**3. Geometric number of bound visits.** If \(N\) is the number of bound visits up to and including the successful one, then \(\Pr(N=n)=\theta(1-\theta)^{n-1}\) for integers \(n\geq1\). Conditional on \(N\), the absorption time is the initial adsorption time, plus \(N\) i.i.d. bound durations, plus \(N-1\) i.i.d. post-desorption bulk excursions. Therefore the exact transform is

\[
\mathcal L_\theta(s)
=\frac{\theta F_{r,\mathrm{home}}(s)\phi(s)}{1-(1-\theta)\phi(s)F_{r,P}(s)}.
\]

This is the first-renewal identity used in the motivating literature; it is stated here to specify precisely the probabilistic inputs to the new singular limit.

**4. Joint scaling.** Set \(s=\theta^2 z\) and \(r=R\theta^2\), for fixed \(z>0,R\geq0\). The bare expansions from step 1 yield

\[
a_{k_0}(s+r)=1-A_{\mathrm{home},k_0}\theta\sqrt{z+R}+O(\theta^2),\quad
g_P(s+r)=1-A_P\theta\sqrt{z+R}+O(\theta^2).
\]

In step 2 this gives

\[
F_{r,P}(\theta^2z)=1-\theta A_P\frac{z}{\sqrt{z+R}}+O(\theta^2),\qquad
F_{r,\mathrm{home}}(\theta^2z)\longrightarrow1.
\]

The bound-time hypothesis gives \(\phi(\theta^2z)=1-c\theta\sqrt z+o(\theta)\). Substitute in step 3, cancel \(\theta\), and obtain the asserted Laplace-transform limit. Its value tends to one as \(z\downarrow0\); the continuity theorem for Laplace transforms gives convergence in distribution to a proper nonnegative limit. This argument never uses a finite first moment.

**5. Positive subordinator representation.** The derivative of \(h_R(z)=z/\sqrt{z+R}\) is

\[
h_R'(z)=\frac{z+2R}{2(z+R)^{3/2}}.
\]

For \(z>0\) it equals the Laplace integral

\[
\int_0^\infty e^{-zt}e^{-Rt}\left(\frac1{2\sqrt{\pi t}}+\frac{R\sqrt t}{\sqrt\pi}\right)dt.
\]

Since \(h_R(0)=0\), the Lévy–Khintchine formula gives the stated nonnegative Lévy density. The classical \(1/2\)-stable subordinator has exponent \(c\sqrt z\). Conditional on independent unit-rate exponential \(E\), the Laplace transform of their sum at time \(E\) is \(\exp[-E(c\sqrt z+A_Ph_R(z))]\); averaging over \(E\) gives exactly \((1+c\sqrt z+A_Ph_R(z))^{-1}\).

**6. Long tails, noncommutation, and protocol threshold.** If \(R>0\) is fixed, \(h_R(z)=z/\sqrt R+O(z^2)\) as \(z\downarrow0\); hence \(1-\mathcal L_R(z)\sim c\sqrt z\). At \(R=0\), \(h_0(z)=\sqrt z\), giving \(1-\mathcal L_0(z)\sim(c+A_P)\sqrt z\). Karamata's Tauberian theorem for nonnegative random variables converts these expressions to the two stated survival asymptotics, since \(\Gamma(1/2)=\sqrt\pi\). Pointwise continuity of the transform in \(R\) proves \(Y_R^{(P)}\Rightarrow Y_0^{(P)}\), while the tail coefficients differ by \(A_P/\sqrt\pi>0\). Finally \(h_R(z)\) strictly decreases with \(R\) for each fixed \(z>0\), so the limiting Laplace transform increases with \(R\), and decreases with \(A_P\). The explicit formulas for \(A_P\) give the asserted protocol threshold and orientation ordering.

## Verification

The accompanying `verify.py` is a standalone deterministic verifier requiring Python 3 and `mpmath`. It checks the backward equations and wall boundary condition, independent first-reset renewal identities, joint-scaling convergence for both desorption protocols, the small-argument tail coefficients, strict Laplace ordering, the Lévy-kernel integral, and the orientation threshold. It passed 158 tests on extraction from the working package. These numerical checks complement, but do not replace, the analytical arguments above.

For the Pareto example, the complete binding-time transform used by the verifier is

\[
\phi(s)=1-\sqrt{\pi\tau s}\,e^{\tau s}\operatorname{erfc}(\sqrt{\tau s}),
\]

which has \(1-\phi(s)\sim\sqrt{\pi\tau}\sqrt s\). Substitution into step 3 provides the finite-parameter comparison without Monte Carlo truncation.

## Relationship to prior work

Bressloff and Linn (2026) provide the run-and-tumble sticky-boundary model, the transform for irreversible adsorption after starting at the wall, and exact first-renewal transforms for absorption under the two desorption protocols. All those facts are prior work. Their analysis of finite means uses finite moments of the bound duration; no weak-absorption/vanishing-reset scaling theorem or subordinator crossover is identified in the inspected original sections.

Bressloff (2025) analyzes a different, diffusing partially reactive target in a bounded domain and proves the **already-known** minimum-power tail classification for competing heavy-tailed adsorption and bound waiting, including the equal-exponent case (Section 3.3, equations (3.34)–(3.36)). Neither that general tail rule nor the finite-parameter geometric renewal transform is part of the asserted novelty. The proposed contribution isolates the critical rate \(r=R\theta^2\) for a bulk-reset run-and-tumble excursion on an unbounded half-line; the denominator \(z/\sqrt{z+R}\), its explicit positive Lévy kernel, and the noncommuting reset and survival-tail limits require the new joint asymptotic comparison.

Scher, Reuveni and Grebenkov (2023) study sticky escape for Brownian particles in bounded domains with Markovian surface kinetics. Their escape-time methodology is related, but the inspected model does not provide this weak-absorption, heavy-tailed, two-desorption-protocol, weak-bulk-reset limit. General geometric-renewal, Tauberian, and subordinator methods are standard and are used without asserting priority for them.

## Limitations

The result assumes independent classical Poisson velocity flips and bulk resets, a fixed half-line geometry, a single reactive wall, independent bound durations and absorption decisions, and a critical square-root Laplace asymptotic for the waiting time. The scaling \(r=R\theta^2\) holds with fixed \(R\); no estimate uniform across all resetting rates is claimed. The theorem establishes Laplace ordering, not ordinary stochastic dominance. It does not describe multiple interacting searchers, state-dependent resets, correlations between waiting duration and absorption outcome, or non-Poisson bulk clocks. Novelty relative to more general geometric-sum scaling literature remains a priority risk; an independent scientific audit has not been carried out.

## References

1. P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, arXiv:2602.02446v1, first public 2026-02-02, https://arxiv.org/abs/2602.02446 ; *Physical Review E* **113**, 054122 (2026), DOI:10.1103/dcnh-bhwc.
2. P. C. Bressloff, *Diffusion-mediated adsorption versus absorption at partially reactive targets: a renewal approach*, arXiv:2503.01308v1 (2025), https://arxiv.org/pdf/2503.01308 , Section 3.3.
3. Y. Scher, S. Reuveni and D. S. Grebenkov, *Escape of a sticky particle*, arXiv:2305.08701v1 (2023), https://arxiv.org/abs/2305.08701 , *Physical Review Research* **5**, 043196 (2023).
4. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle with stochastic resetting*, arXiv:2503.01304v1 (2025), https://arxiv.org/abs/2503.01304 .

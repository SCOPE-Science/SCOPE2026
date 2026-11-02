# A unique finite-hyperedge environment-bias threshold with logarithmic sensitivity scaling

## Finding

In a two-environment public-goods transition model with linear high-state persistence and power-law recovery, the finite-group stationary high-state frequency has a unique leading-bias crossover. Fix a real recovery sensitivity \(\beta\ge2\). For \(0\le c\le1\), the probability of a high state on the next update is \(c\) when the present state is high and \(c^\beta\) when it is low. The unique stationary high-state probability is
\[
h_\beta(c)=\frac{c^\beta}{1-c+c^\beta}.
\]
Suppose a group of integer size \(g\ge2\) draws its members' cooperation indicators independently with common probability \(p\in(0,1)\), *once*, then holds these strategies fixed while the environmental state is allowed to reach stationarity. Its expected stationary high-state frequency is
\[
F_{g,\beta}(p)=\sum_{k=0}^{g}\binom{g}{k}p^k(1-p)^{g-k}h_\beta(k/g).
\]
There is exactly one \(p_\beta\in(0,1)\) such that, for every fixed \(p\ne p_\beta\),
\[
\lim_{g\to\infty}g\big(F_{g,\beta}(p)-h_\beta(p)\big)
=\frac{p(1-p)}2h_\beta''(p),
\]
with strictly positive limit when \(p<p_\beta\) and strictly negative limit when \(p>p_\beta\). Thus, as group size increases, binomial composition variability eventually raises the stationary high-state frequency on one side of the *unique* threshold and lowers it on the other, relative to the homogeneous-composition benchmark. The sensitivity-dependent transition satisfies
\[
\beta(1-p_\beta)=\log\beta-\log\log\beta+o(1)
\qquad(\beta\to\infty).
\]
For quadratic recovery \(\beta=2\), the unique threshold is \(p_2=1-2\cos(4\pi/9)\approx0.6527036447\).

## Assumptions and scope

The two states are labeled high and low. Within each group composition \(c\), the high-to-high transition probability is \(c\), while low-to-high is \(c^\beta\); the complementary probabilities go to the low state. The group composition is random initially but subsequently frozen and is not redrawn on each state transition. At \(c=0\) and \(c=1\), the environmental chain has a unique absorbing low and high state, respectively. At \(0<c<1\), it is irreducible and aperiodic. The probability \(p\) concerns the initial independent strategy draw and is not an equilibrium cooperation rate of an adaptive game. No claim is made for endogenous strategy imitation, between-group correlations, or the fully coupled network process.

## Proof

**Stationary reduction.** Write \(v=c\) for the high-to-high probability and \(u=c^\beta\) for low-to-high. Stationary balance requires \(\pi(1-v)=(1-\pi)u\). Thus \(\pi=u/(1-v+u)=h_\beta(c)\), with the endpoint states obtained by direct inspection. Independently drawing the initial indicators gives \(K\sim\operatorname{Binomial}(g,p)\), and averaging their *conditional* stationary probabilities gives exactly \(F_{g,\beta}(p)\).

**One and only one curvature threshold.** Set \(d_\beta(p)=1-p+p^\beta\). Twice differentiating gives
\[
h_\beta''(p)=\frac{p^{\beta-2}N_\beta(p)}{d_\beta(p)^3},
\]
where
\[
\begin{aligned}
N_\beta(p)={}&\beta(\beta-1)(1-p)^2
 +2p\big(\beta-(\beta-1)p\big)\\
&-\beta\big(\beta+1-(\beta-1)p\big)p^\beta.
\end{aligned}
\]
The critical algebraic identity is
\[
N_\beta'(p)=2(\beta-2)\big((\beta-1)p-\beta\big)
 -\beta(\beta+1)p^{\beta-1}\big(\beta-(\beta-1)p\big).
\]
For \(\beta\ge2\) and \(p\in(0,1)\), the first summand is nonpositive and the second is strictly negative. Moreover, \(N_\beta(0)=\beta(\beta-1)>0\) and \(N_\beta(1)=-2(\beta-1)<0\). Continuity and strict decrease prove a unique zero \(p_\beta\), and the displayed second-derivative formula proves the claimed sign pattern.

**Finite-group correction.** Let \(Y_g=K/g\). For fixed \(p\in(0,1)\), \(\mathbb E(Y_g-p)=0\) and \(\mathbb E(Y_g-p)^2=p(1-p)/g\). Also \(\mathbb E(Y_g-p)^3=p(1-p)(1-2p)/g^2\) and \(\mathbb E(Y_g-p)^4=O_p(g^{-2})\). Choose a closed interval about \(p\) contained in \((0,1)\), where \(h_\beta\) has bounded fourth derivative. Fourth-order Taylor expansion on the event that \(Y_g\) lies in this interval, together with an exponentially small binomial tail bound on its complement, yields
\[
F_{g,\beta}(p)=h_\beta(p)
 +\frac{p(1-p)}{2g}h_\beta''(p)+O_{p,\beta}(g^{-2}).
\]
This is a *pointwise* interior estimate. Its leading coefficient is strictly signed whenever \(p\ne p_\beta\); it does not assert a fixed sign at the critical \(p\), nor a uniform estimate at moving endpoints.

**Sensitivity boundary layer.** Put \(t=\beta(1-p)\). For any fixed real \(a\), set \(t=\log\beta-\log\log\beta+a\) and \(p=1-t/\beta\). Substitution into the exact expression for \(N_\beta\) yields
\[
\frac{N_\beta(1-t/\beta)}{(\log\beta)^2}
 \longrightarrow 1-e^{-a}.
\]
Indeed, its two nonnegative summands contribute \((\log\beta)^2(1+o(1))\); its negative summand is \(\beta(2+t+o(1))(1-t/\beta)^\beta=e^{-a}(\log\beta)^2(1+o(1))\). For any \(\varepsilon>0\), the signs at \(a=-\varepsilon\) and \(a=+\varepsilon\) eventually bracket the unique root. Hence \(t_\beta=\beta(1-p_\beta)=\log\beta-\log\log\beta+o(1)\).

**Quadratic sensitivity.** For \(\beta=2\), \(N_2(p)=2(p^3-3p^2+1)\), whose unique root in \((0,1)\) is \(1-2\cos(4\pi/9)\). This proves the exact special value.

## Verification

The accompanying `VERIFY.py` symbolically differentiates the stationary response and checks the derivative and endpoint identities. It also verifies exact binomial formulae for two and three members, rational stationary-balance identities at many group compositions, and numerical root brackets for several sensitivities. The central uniqueness and logarithmic-limit claims are established by the algebraic and asymptotic proofs above; the finite checks are not treated as substitutes for those proofs.

For \(\beta=2\), the exact small-group checks give
\[
F_{2,2}(p)-h_2(p)=\frac{p(p-1)(p^2+2p-2)}{3(p^2-p+1)}
\]
and
\[
F_{3,2}(p)-h_2(p)=\frac{-p(p-3)(p-1)(2p^2-1)}{7(p^2-p+1)}.
\]
Their respective interior sign-switch points, \(\sqrt3-1\) and \(1/\sqrt2\), differ from the large-group limit; the asymptotic theorem does not claim that finite-group thresholds are identical.

## Relationship to prior work

Wei, Xiong, Li, Feng and Szolnoki (2026) specify the two-state high/low transition model with cooperator-fraction exponents in their equations (2.6)–(2.7), and study adaptive cooperation/environment coevolution with simulations. The theorem here isolates the exact *frozen-composition stationary environment*, applies binomial sampling, and proves a unique curvature crossover and its logarithmic sensitivity scale. Their reported dynamic high-state fractions are not interchangeable with this annealed stationary quantity. Su, McAvoy, Wang and Nowak (2019) investigate game transitions and cooperation thresholds on structured populations, not this fixed-composition hyperedge observable. The binomial approximation step is a standard Bernstein/Voronovskaya-type expansion, but that general principle does not itself determine the unique root or its \(\log\beta-\log\log\beta\) location.

## Limitations

This is a one-way environmental calculation under frozen independent strategies, not a theorem about evolutionary stability, payoff optimization, dynamic cooperation rates, or correlated hyperedge composition. Eventual bias signs hold for each fixed interior \(p\ne p_\beta\); their finite-group onset and the critical-point higher-order term are not classified here. Other, potentially unindexed literature may contain equivalent formulations of the special crossover, and no independent scientific review is claimed.

## References

1. N. Wei, X. Xiong, Q. Li, M. Feng, and A. Szolnoki, *Cooperation in Public Goods Games over Uniform Random Hypergraphs with Game Transitions*, arXiv:2603.22967 (first publicly posted 24 March 2026); *Journal of the Royal Society Interface* 23 (2026), article 20251319. https://arxiv.org/abs/2603.22967 ; https://doi.org/10.1098/rsif.2025.1319 .
2. Q. Su, A. McAvoy, L. Wang, and M. A. Nowak, *Evolutionary dynamics with game transitions*, *Proceedings of the National Academy of Sciences* 116 (2019), 25398–25404. https://arxiv.org/abs/1905.10269 ; https://doi.org/10.1073/pnas.1908936116 .
3. M. Feng, B. Pi, L.-J. Deng, and J. Kurths, *An Evolutionary Game With the Game Transitions Based on the Markov Process*, *IEEE Transactions on Systems, Man, and Cybernetics: Systems* 54 (2024), 609–621. https://doi.org/10.1109/TSMC.2023.3315963 .

# Finite mutation restores interior return-rate sensitivity in three-person public goods games

## Finding

A group-size-three public goods game with a general contributor-count return schedule can respond to changes in its *interior* return rates even under arbitrarily weak selection. This sensitivity is present at **every positive mutation probability**, disappears in the rare-mutation limit, and cannot occur to first order in any two-person public goods game under the same updating rule. It is already observable with four individuals.

**Theorem.** In the finite-population process defined below, for every integer \(N\ge4\), every \(0<\mu<1\), and every positive return triple \((r_1,r_2,r_3)\), the stationary cooperator fraction \(m_N(\delta)\) is differentiable at zero selection strength and satisfies \(m_N(0)=1/2\) and

\[
\boxed{\displaystyle
m_N'(0)=\frac{1-\mu}{12[3+(4N-7)\mu][1+(4N-5)\mu]}
\left[3(N-3)(1+(N-2)\mu)r_3+(N-3)(N-1)\mu(2r_2-r_1)-3(N-1)(3+(4N-7)\mu)\right].}
\]

In particular, the coefficient of \(r_2\) is strictly positive and that of \(r_1\) strictly negative for every \(N\ge4\) and \(0<\mu<1\). The first derivative in the two-person group model, for every \(N\ge3\), is independent of \(r_1\).

**Sharp finite example.** With \(N=4\), \(\mu=1/2\), unit contribution cost, and three-person groups, both strictly increasing return triples \((2,3,10)\) and \((2,7,10)\) have the same full-contribution return \(r_3=10\), yet their stationary cooperator-frequency derivatives at zero selection are respectively \(-1/780\) and \(7/780\). Therefore, for all sufficiently small positive selection strengths, the first game has fewer than half cooperators at stationarity, while the second has more than half.

For the first triple the derivative changes sign at the exact mutation probability \(\mu=1/3\): positive below it and negative above it. In the limit \(\mu\downarrow0\) the general formula reduces to \(\big[(N-3)r_3-3(N-1)\big]/12\), the full-contribution-only threshold appropriate to the rare-mutation, weak-selection comparison.

## Assumptions and scope

Fix an integer population \(N\), two strategies \(C,D\), group size \(g\in\{2,3\}\) with \(g<N\), and a positive return schedule \((r_1,\ldots,r_g)\). In a game with exactly \(j\) cooperators, each participant receives the equal share \(j r_j/g\) of the public return; each cooperator additionally pays unit cost and each defector pays no cost. A player's payoff is its **expectation** over a group formed by drawing the other \(g-1\) members uniformly without replacement from the remaining \(N-1\) individuals. The payoff difference \(\Delta_k\) is the expected cooperator payoff minus expected defector payoff when the population contains \(k\) cooperators. Only interior states \(1\le k\le N-1\) require this difference.

One discrete step chooses a uniformly random focal individual. With probability \(\mu\in(0,1)\), the focal *flips* its strategy. Otherwise it samples one of the other \(N-1\) individuals, uniformly, and adopts the sampled strategy with probability \(F(\delta(\pi_{\mathrm{sampled}}-\pi_{\mathrm{focal}}))\), where \(F(z)=(1+e^{-z})^{-1}\), \(\delta\ge0\), and payoffs are strategy averages at current state. The states \(k=0,\ldots,N\) form a finite irreducible birth-death Markov chain, with a self-loop allowed. The stationary distribution \(\pi_\delta\) and its cooperator mean \(m_N(\delta)=N^{-1}\sum_{k=0}^N k\pi_\delta(k)\) exist uniquely. These are properties of this stated mutation-before-imitation, *distinct-peer* process, not of every updating rule or every mutation convention.

For group size three, define \(C=\binom{N-1}{2}\). At interior state \(k\), the exact payoffs are

\[
\begin{aligned}
P_C(k)&=-1+\frac{r_1\binom{N-k}{2}+2r_2(k-1)(N-k)+3r_3\binom{k-1}{2}}{3C},\\
P_D(k)&=\frac{r_1 k(N-k-1)+2r_2\binom{k}{2}}{3C},\\
\Delta_k&=P_C(k)-P_D(k).
\end{aligned}
\]

The convention \(\binom ab=0\) for out-of-range \(b\) applies.

## Proof

**1. Exact transition probabilities.** At interior state \(k\), the birth and death probabilities are

\[
q_k^+=\frac{N-k}{N}\left[\mu+(1-\mu)\frac{k}{N-1}F(\delta\Delta_k)\right],\qquad
q_k^-=\frac{k}{N}\left[\mu+(1-\mu)\frac{N-k}{N-1}F(-\delta\Delta_k)\right].
\]

At the endpoints, the cross-strategy imitation terms vanish. Because \(\mu>0\), every neighboring transition is positive. Finite irreducibility and detailed balance give a unique stationary distribution, analytic in \(\delta\) near zero because all transition rates are analytic and nonzero where needed.

**2. Stationary drift response.** The identity \(2F(z)-1=\tanh(z/2)\) yields

\[
q_k^+-q_k^-=\mu(1-2k/N)+\frac{(1-\mu)k(N-k)}{N(N-1)}\tanh(\delta\Delta_k/2).
\]

At stationarity, the mean drift vanishes. Differentiating this identity at \(\delta=0\), where \(\tanh(0)=0\), proves

\[
m_N'(0)=\frac{1-\mu}{4\mu}\,\mathbb E_{\pi_0}\!\left[\frac{K(N-K)}{N(N-1)}\Delta_K\right].\tag{1}
\]

The unknown derivative of the stationary distribution cancels because the selection-dependent drift term is zero at \(\delta=0\). No weak-mutation approximation has been made.

**3. Exact neutral law and moments.** Set \(a=2\mu(N-1)/(1-\mu)\). Detailed balance at \(\delta=0\) gives the symmetric beta-binomial law

\[
\pi_0(k)=\binom Nk\frac{(a)_k(a)_{N-k}}{(2a)_N},\qquad k=0,\ldots,N,
\]

where \((u)_j=u(u+1)\cdots(u+j-1)\), \((u)_0=1\). In particular \(\mathbb E_{\pi_0}K=N/2\). Size-biasing by \(K(N-K)\) amounts to selecting an ordered cooperator–defector pair. If \(J=K-1\) is the cooperator count among the remaining \(N-2\) individuals under this size-biased law, then

\[
J\sim\mathrm{BetaBinomial}(N-2,a+1,a+1),\quad
\mathbb E J=\frac{N-2}{2},\quad
\mathbb E[J(J-1)]=\frac{(N-2)(N-3)(a+2)}{2(2a+3)}.
\]

Also, \(\mathbb E_{\pi_0}[K(N-K)/(N(N-1))]=a/[2(2a+1)]\). Each assertion follows either from the beta mixture representation or the displayed detailed-balance weights; in particular no large-population approximation is involved.

**4. Closed form.** The displayed three-person payoff difference is quadratic in \(k\). Substitute \(K=J+1\) into equation (1), evaluate its constant, linear, and quadratic terms using the preceding two factorial moments, and substitute \(a=2\mu(N-1)/(1-\mu)\). Collecting the coefficients of \(r_1,r_2,r_3\) and the unit cost gives the boxed rational formula. It is exact for every indicated integer \(N\) and positive \(\mu<1\). The coefficients of \(r_2\) and \(r_1\) are respectively

\[
\frac{(1-\mu)(N-3)(N-1)\mu}{6[3+(4N-7)\mu][1+(4N-5)\mu]},\quad
-\frac{(1-\mu)(N-3)(N-1)\mu}{12[3+(4N-7)\mu][1+(4N-5)\mu]},
\]

which are nonzero and of opposite signs.

**5. Exact counterexample and mutation threshold.** Substitution of \(N=4\), \(\mu=1/2\), \((r_1,r_2,r_3)=(2,3,10)\) and \((2,7,10)\) gives \(-1/780\) and \(7/780\). Stationary analyticity and \(m_4(0)=1/2\) imply the asserted strict inequalities for all sufficiently small positive \(\delta\). With the first triple, the bracket of the formula factors as a positive constant times \((1-3\mu)\); the denominator remains positive throughout \((0,1)\). Finally, letting \(\mu\downarrow0\) proves the stated endpoint-only limit.

**6. Sharp group-size boundary.** For two-person groups the cooperator-minus-defector payoff simplifies exactly to

\[
\Delta_k=-1+\frac{(k-1)r_2+(N-2k)r_1/2}{N-1}.
\]

The neutral weight \(\pi_0(k)k(N-k)\) is invariant under \(k\leftrightarrow N-k\), while its \(r_1\) coefficient \(N-2k\) is antisymmetric. Therefore equation (1) is independent of \(r_1\), for every \(N\ge3\) and every \(\mu\in(0,1)\). A genuine interior return rate needs group size at least three; the restriction \(g<N\) then requires \(N\ge4\). The four-person example attains both lower bounds.

## Verification

Run `python verify.py` using Python's standard library. It implements the payoffs by a direct hypergeometric sum, obtains the stationary neutral law by birth–death recursion, differentiates the complete stationary detailed-balance products independently of the drift argument, and compares them with the stated closed form using exact rational arithmetic. It checks 140 group-three parameter combinations (population sizes 4–10, four mutation probabilities, five return triples) and 32 independent two-person tests, for 172 exact equalities. It separately checks the two exact derivatives, the one-third mutation boundary, and the signs of stationary frequencies at selection strength 0.01. Finite tests support error detection; the analytical proof above establishes the universally quantified result.

## Relationship to prior work

Wang, Liu, Chen and Szolnoki (2026) study general contributor-count-dependent returns and show a full-contribution-rate-only selection condition in their weak-selection, rare-mutation regime. The present theorem holds the mutation probability strictly positive while taking the weak-selection derivative and identifies the exact previously suppressed interior-rate contributions. These two limiting regimes must not be interchanged without justification.

Hauert and McAvoy (2024) derive nonlinear-public-goods payoffs and finite-population mutation-selection processes, and calculate stationary distributions numerically for an exponential-fitness Moran process. This differs from the distinct-peer Fermi update studied here, but the underlying payoff and finite-state methodology provide relevant prior coverage. The boxed rational all-population formula, strict interior coefficient, sharp minimum size and pair of opposite-sign schedules sharing the same full-contribution value are not stated in the inspected article. McAvoy and Wakeley (2022) develop general weak-selection mutation-selection structure coefficients, and therefore provide a broad framework that may imply parts of the calculation after specialization; the specific group-size-three closed form and contrasting example are the asserted result, not the general technique.

## Limitations

The conclusion concerns the first-order stationary response at **zero** selection strength, not every positive selection strength. Mutation is symmetric strategy flipping at each step, peer imitation excludes self-sampling, and game groups are sampled without replacement. Other updating rules, multiplayer aggregation schemes or definitions of mutation can change the coefficients. The rare-mutation limit is taken *after* differentiating in selection and does not assert uniformity in the two small parameters. The result is a deterministic identity about stationary means of a finite stochastic game, not evidence of observed behavioral responses. Originality remains conditional on incomplete literature coverage; a sufficiently specialized application of a broader existing structure-coefficient theorem could subsume aspects of the derivation. The earliest precisely verified public arXiv date of the motivating source is 2026-07-18; metadata elsewhere lists a June 2026 journal issue without a verified earlier public day.

## References

1. Q. Wang, Y. Liu, X. Chen, and A. Szolnoki, *Evolutionary dynamics in public goods games with general frequency-dependent returns*, arXiv:2607.16809v1 (public preprint 2026-07-18); *Physica D* **495**, 135303 (2026), DOI: 10.1016/j.physd.2026.135303.
2. C. Hauert and A. McAvoy, *Frequency-dependent returns in nonlinear public goods games*, arXiv:2404.13728, *Journal of the Royal Society Interface* **21**, 20240334 (2024), DOI: 10.1098/rsif.2024.0334.
3. A. McAvoy and J. Wakeley, *Evaluating the structure-coefficient theorem of evolutionary game theory*, arXiv:2010.14566, *Proceedings of the National Academy of Sciences* (2022), DOI: 10.1073/pnas.2119656119.

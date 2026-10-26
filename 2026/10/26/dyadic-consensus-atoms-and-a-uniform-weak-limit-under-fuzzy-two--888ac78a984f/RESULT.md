# Dyadic consensus atoms and a uniform weak limit under fuzzy two-agent influence

## Finding

For the two-agent instance of the fuzzy-selection, unweighted synchronous opinion model described below, the terminal opinion is **purely atomic for every positive confidence width**, supported on all dyadic midpoints of the initial opinion interval. As the confidence width tends to zero at fixed positive steepness, this atomic distribution converges weakly to the **uniform distribution on the entire initial interval**, although its total-variation distance from uniform remains one. The exact waiting-time formula additionally implies the sharp asymptotic
\[
\lim_{\varepsilon\downarrow0} e^{-\beta d/\varepsilon}\,\mathbb E[T_\varepsilon]
=\frac{1}{2(1+e^\beta)}.
\]
Thus the rare-influence limit produces a maximally dispersed random consensus location on an exponentially long timescale, not convergence to the deterministic initial midpoint.

Precisely, let \(a<b\) and \(d=b-a\), with \(0\le a<b\le1\). For each integer \(k\ge0\), set
\[
q_k=\frac{1+e^{-\beta}}{1+e^{\beta(d/(2^k\varepsilon)-1)}},\quad
h_k=2q_k-q_k^2,\quad s_k=\frac{q_k}{2-q_k},\quad
S_0=1,\quad S_k=\prod_{j=0}^{k-1}(1-s_j).
\]
All these quantities are well-defined for \(\varepsilon,\beta>0\), with \(0<q_k\le1\). The exact law of the common eventual opinion \(C_\varepsilon\), at every integer \(k\ge0\) and \(0\le j<2^k\), is
\[
\Pr\!\left(C_\varepsilon=a+d\frac{2j+1}{2^{k+1}}\right)
=\frac{S_k s_k}{2^k}.
\]
These are all its atoms. In particular,
\[
\mathbb E[C_\varepsilon]=\frac{a+b}{2},\qquad
\operatorname{Var}(C_\varepsilon)=\frac{d^2}{12}\left(1-\sum_{k=0}^{\infty}S_k s_k4^{-k}\right),
\qquad \mathbb E[T_\varepsilon]=\sum_{k=0}^{\infty}\frac{S_k}{h_k}.
\]
Here \(T_\varepsilon\) is the **number of synchronous rounds until exact opinion equality**, including the successful round. It is almost surely finite and has finite expectation for each \(\varepsilon>0\).

## Assumptions and scope

We study exactly two agents linked by a single undirected edge, each retaining their own opinion in their averaging set. At each synchronous integer time, *each directed potential influence is selected independently* with probability
\[
q(z)=\frac{f(z)}{f(0)},\qquad f(z)=\frac{1}{1+e^{\beta(z/\varepsilon-1)}}.
\]
If a directed influence is selected, its recipient replaces their old opinion by the arithmetic mean of the two pre-update opinions; otherwise that recipient retains their old opinion. The two decisions use independent random draws conditional on the current opinions. The model is the unweighted fuzzy-selection variant, not the strictly selected, weighted-influence, or combined variants. The confidence width is \(\varepsilon>0\), the steepness is fixed \(\beta>0\), and the limiting statement is the singular regime \(\varepsilon\downarrow0\) with the nonzero initial distance \(d\) held fixed. The claim does not set \(\varepsilon=0\) in the original formula.

All probabilities and expectations are with respect to the independent directed selection decisions, with fixed initial opinions \(a,b\). No random replacement of opinions, exogenous bias, or further agents are present.

## Proof

**One accepted transition.** At distance \(z>0\), let \(q=q(z)\). In one round, no directed influence is selected with probability \((1-q)^2\); exactly one direction is selected with probability \(2q(1-q)\); both are selected with probability \(q^2\). The probability of a non-null round is \(h=2q-q^2\). Conditional on a non-null round, two-way selection has probability \(q^2/h=q/(2-q)=s\); otherwise a left-only or right-only selection occurs with equal probability \((1-s)/2\). No-selection rounds do not change the state, so the waiting time to the next accepted transition is geometric with mean \(1/h\).

**Dyadic tree.** If both directions are selected, both opinions become their common midpoint and equality is exact. If exactly one is selected, one endpoint moves to that midpoint while the other stays fixed. Thus the opinion interval is replaced by its left or right half, with each choice equally probable conditional on not stopping. After exactly \(k\) one-direction transitions, the interval is one of the \(2^k\) dyadic subintervals of \([a,b]\), each with conditional probability \(2^{-k}\), and its length is \(d/2^k\). The probability that no two-way selection occurred at preceding levels is \(S_k\). Stopping at level \(k\) consequently has probability \(S_k s_k\), giving each of the distinct dyadic midpoints the asserted mass.

**Finite absorption and moments.** As the interval contracts, \(q_k\) increases, hence \(s_k\ge s_0>0\). Therefore \(S_k\le(1-s_0)^k\), implying certain finite stopping and normalization \(\sum_{k\ge0}S_k s_k=1\). The conditional distribution at depth \(k\) is the uniform measure on the \(2^k\) dyadic midpoints, with mean \((a+b)/2\) and variance \(d^2(1-4^{-k})/12\). Mixture gives the exact mean and variance. Reaching stage \(k\) has probability \(S_k\), and its geometric holding time has mean \(1/h_k\); monotone convergence of nonnegative sums yields the stated exact calendar-time expectation. As \(h_k\ge h_0>0\), the expected number of stages and the expected calendar time are finite.

**Singular weak limit and total variation.** For each fixed \(k\), \(q_k\to0\) as \(\varepsilon\downarrow0\), so \(s_k\to0\) and the random stopping depth \(K_\varepsilon\to\infty\) in probability. Conditional on \(K_\varepsilon=k\), the stopping point has the distribution of the midpoint of a uniformly chosen dyadic interval of length \(d/2^k\). Couple it to an independent uniform sample from that same interval: the distance is at most \(d/2^{k+1}\), tending to zero in probability as \(K_\varepsilon\to\infty\). Therefore \(C_\varepsilon\) converges in distribution to \(\mathrm{Unif}[a,b]\). At every fixed positive \(\varepsilon\), its support is countable, while uniform measure assigns that countable set zero mass; the total-variation distance is consequently exactly one.

**Sharp expected-time scale.** Let \(L_\varepsilon=\lceil\log_2(d/\varepsilon)\rceil\) for \(0<\varepsilon<d\). For every \(k\ge L_\varepsilon\), \(d/2^k\le\varepsilon\), so \(q_k\ge(1+e^{-\beta})/2=:c_\beta>0\), hence \(s_k\ge c_\beta/(2-c_\beta)=:\sigma_\beta>0\). Consequently the expected stopping depth is at most \(L_\varepsilon+1/\sigma_\beta\). Moreover \(h_k\ge h_1\) for \(k\ge1\), so the contribution to \(\mathbb E[T_\varepsilon]\) from all stages after the first is at most \((L_\varepsilon+1/\sigma_\beta)/h_1\). Since \(q_0\sim(1+e^\beta)e^{-\beta d/\varepsilon}\) and \(q_1\sim(1+e^\beta)e^{-\beta d/(2\varepsilon)}\), this remainder is \(o(1/h_0)\). Finally \(1/h_0\sim[2(1+e^\beta)]^{-1}e^{\beta d/\varepsilon}\), proving the claimed exact prefactor.

## Verification

Run the included standard-library Python program `verify.py`. It independently enumerates accepted one-sided and simultaneous actions at prescribed rational conditional-selection probabilities, compares exact atomic masses and moments with the dyadic formula, checks normalization and stagewise expected round counts, and evaluates the logistic-model expectation against its analytic rare-selection asymptotic. Rational finite checks do not establish the infinite theorem; each infinite assertion is proved above.

## Relationship to prior work

Giaquinta, Hernández and Chavalarias (2026, arXiv:2610.07971v1, publicly posted October 6, 2026) define the logistic fuzzy-selection rule and self-normalized sampling in their equations (1)–(3), with the unweighted fuzzy model called HK2. Their numerical analysis acknowledges that rare distant interactions can restart ostensibly converged clusters, but does not provide this two-agent exact absorption distribution, atomic-to-uniform singular limit or sharp exponential waiting-time prefactor.

Mäs, Flache and Helbing (2016) already establish the qualitative importance of positive-probability cross-cluster contacts and illustrate eventual consensus in a related generalized bounded-confidence simulation model. Consequently, eventual consensus by itself is not claimed as new here. Elboim, Peres and Peretz (2024) study consensus times and variance under asynchronous DeGroot updates with fixed averaging kernels; their full-text theorems do not specialize to the state-dependent logistic inclusion mechanism or imply the stopped-dyadic atomic formula without additional analysis. Randomized gossip under unreliable communications is likewise related but does not supply the present model's distance-dependent stopping-depth law. The elementary dyadic subdivision is a proof technique, not a claim of new probability theory in isolation.

## Limitations

The result concerns exactly two agents and independent directional choices, not arbitrary connected networks or the weighted-influence variants. Its full outcome law is specific to midpoint averaging and synchronous independent selection. Exact equality need not occur in higher-agent models. The result's historical originality remains provisional: broader work on random affine recursions, stopped dyadic subdivisions or random consensus laws may contain mathematically equivalent formulas. The distributional result is mathematical and does not predict empirical social opinion distributions without assessing the model assumptions.

## References

1. C. Giaquinta, L. Hernández and D. Chavalarias, *Probabilistic neighbors' selection competes with confirmation bias in a bounded confidence model*, arXiv:2610.07971v1 (October 6, 2026), https://arxiv.org/html/2610.07971.
2. M. Mäs, A. Flache and D. Helbing, *Robust Clustering in Generalized Bounded Confidence Models*, Journal of Artificial Societies and Social Simulation **19**(4), 7 (2016), https://www.jasss.org/19/4/7.html.
3. D. Elboim, Y. Peres and R. Peretz, *The asynchronous DeGroot dynamics*, Random Structures & Algorithms **65** (2024), 857–895, https://doi.org/10.1002/rsa.21248.
4. G. Shi, M. Johansson and K. H. Johansson, *Randomized Gossip Algorithm with Unreliable Communication*, arXiv:1203.6028 (2012), https://arxiv.org/abs/1203.6028.

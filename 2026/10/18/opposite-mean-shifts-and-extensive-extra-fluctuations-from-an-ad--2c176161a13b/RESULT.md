# Opposite mean shifts and extensive extra fluctuations from an adsorption hub

## Finding

Consider irreversible random-order single-vertex deposition on a cycle with an additional site connected either to every cycle site (a wheel) or to alternate cycle sites (a gear). Although adding this site decreases the limiting mean occupied count in the wheel and increases it in the gear, **both** attachments increase the leading fluctuation variance. Let \(K_m\) be the number accepted on the unmodified cycle of \(2m\) sites, and \(J_m^{\mathrm W}\), \(J_m^{\mathrm G}\) the corresponding wheel and gear counts. For every fixed \(\lambda>0\), with an independent hub clock of rate \(\lambda\) and unit-rate cycle clocks,
\[
\begin{aligned}
\lim_{m\to\infty}(\mathbb E J_m^{\mathrm G}-\mathbb E K_m)&=\lambda e^{-2},\\
\lim_{m\to\infty}(\mathbb E J_m^{\mathrm W}-\mathbb E K_m)&=-\frac{\lambda}{2}(1-e^{-2}),\\
\lim_{m\to\infty}\frac{\operatorname{Var}(J_m^{\mathrm G})-\operatorname{Var}(K_m)}m&=\lambda e^{-4},\\
\lim_{m\to\infty}\frac{\operatorname{Var}(J_m^{\mathrm W})-\operatorname{Var}(K_m)}m&=\frac\lambda2(1-e^{-2})^2.
\end{aligned}
\]
In particular, the variance per cycle pair approaches \((2+\lambda)e^{-4}\) in the gear and \(2e^{-4}+\lambda(1-e^{-2})^2/2\) in the wheel, while the ordinary cycle value is \(2e^{-4}\). These are separate graph families, not competing adsorption rules on the same graph.

## Assumptions and scope

For each integer \(m\ge 3\), the rim is the simple cycle with sites labelled \(0,1,\ldots,2m-1\). The wheel hub is adjacent to all sites; the gear hub is adjacent only to even-labelled sites. Each rim site has an independent exponential clock of rate one; the hub clock is exponential of rate \(\lambda>0\), independent of all rim clocks. When a clock rings, its site is permanently occupied if and only if no occupied neighbor exists, and otherwise permanently rejected. Every site attempts exactly once. All three processes use the same rim clocks, with the hub deleted in the baseline. Counts refer to the terminal jammed state. Limits take \(m\to\infty\) at fixed \(\lambda\). The first archive source was publicly posted March 24, 2005; this is the archival date of the mathematical kinetic framework, not a publication date of the present claim.

## Proof

**Baseline cycle.** Let \(A_n\) be the occupied count on a path of \(n\) sites and \(a_n=\mathbb E A_n\). The first site attempted always deposits and excludes its at most two neighbors; conditioning on its uniformly random position gives, for \(n\ge1\),
\[
na_n=n+2\sum_{j=0}^{n-2}a_j,
\]
with empty sum zero and \(a_0=0\). Consequently the generating function is
\[
\sum_{n\ge0}a_n z^n=\frac{1-e^{-2z}}{2(1-z)^2}.
\]
The first attempted site on the cycle accepts and leaves a path of \(2m-3\) sites. Hence \(\mu_m:=\mathbb EK_m=1+a_{2m-3}=(1-e^{-2})m+O(1)\). We write \(r=1-e^{-2}\). The known one-dimensional blocking-adsorption variance theorem of Penrose–Sudbury [1, Theorem 11] gives \(\operatorname{Var}(K_m)/m\to 2e^{-4}\): cutting a single cycle edge changes occupation only within the two descending-priority causal clusters of its endpoints. Their sizes have uniform factorial tails, so the change in terminal count has bounded second moment. The covariance of this change with a baseline count of variance \(O(m)\) is \(O(\sqrt m)\) by Cauchy–Schwarz, and its variance is \(O(1)\); thus the path variance coefficient transfers to the cycle. An alternative exact cycle moment recursion is included in the reproducibility program.

**Wheel coupling.** Write \(A_m^{\mathrm W}\) for the event that the hub clock is earliest among all \(2m+1\) clocks. It occurs with probability \(q_m=\lambda/(2m+\lambda)\). On this event the hub is occupied and blocks the entire rim, so \(J_m^{\mathrm W}=1\); on its complement the hub is rejected and \(J_m^{\mathrm W}=K_m\). Because the earliest-clock identity and the relative order of the rim clocks are independent, \(A_m^{\mathrm W}\) is independent of \(K_m\). Thus, exactly for every \(m\),
\[
\begin{aligned}
\mathbb E J_m^{\mathrm W}&=(1-q_m)\mu_m+q_m,\\
\operatorname{Var}(J_m^{\mathrm W})&=(1-q_m)\operatorname{Var}(K_m)+q_m(1-q_m)(\mu_m-1)^2.
\end{aligned}
\]
Using \(q_m\sim\lambda/(2m)\), \(\mu_m\sim rm\) and \(\operatorname{Var}(K_m)=O(m)\) yields the two wheel limits.

**Gear pathwise identity.** Let \(A_m^{\mathrm G}\) mean the hub arrives before the first *accepted* even-labelled site in the baseline cycle process. If this occurs, no even site has been occupied and the hub deposits, blocks all even sites, and every odd site eventually deposits; the result is exactly \(m+1\) occupied sites. If it does not occur, an already occupied even site rejects the hub and the resulting count is exactly \(K_m\). Therefore, pathwise,
\[
J_m^{\mathrm G}=K_m+(m+1-K_m)\mathbf1_{A_m^{\mathrm G}}.
\]

**Rare early-deposition probability.** Let \(H_m(t)\) be the probability no even site is accepted before time \(t\) under the unmodified cycle process. Independence of the hub clock gives
\[
p_m:=\mathbb P(A_m^{\mathrm G})=\int_0^\infty\lambda e^{-\lambda t}H_m(t)\,dt.
\]
For fixed \(s\ge0\), the probability no even clock rings before \(s/m\) is \(e^{-s}\), while a rejected even clock by that time requires at least one odd neighboring clock also before that time. Hence
\[
0\le H_m(s/m)-e^{-s}\le2m(1-e^{-s/m})^2\longrightarrow0.
\]
Take \(\lfloor m/2\rfloor\) even sites spaced four rim steps apart. Their three-site neighborhoods are disjoint. Each event that the selected even clock rings by \(t\), but both adjacent odd clocks do not, forces an accepted even site; these events are independent and each has probability \((1-e^{-t})e^{-2t}\). It follows that
\[
H_m(t)\le[1-(1-e^{-t})e^{-2t}]^{\lfloor m/2\rfloor}.
\]
For \(0\le t\le1\) this is bounded by \(e^{-cmt}\), with absolute \(c>0\) for all large \(m\); for \(t\ge1\), monotonicity gives \(H_m(t)\le e^{-cm}\). Dominated convergence after the substitution \(s=mt\), with the remaining tail controlled by the preceding bounds, proves \(mp_m\to\lambda\).

**Conditioning on the rare event.** We require \(K_m/m\to r\) conditional on \(A_m^{\mathrm G}\), not merely unconditionally. For any fixed \(\varepsilon>0\), in fact
\[
\mathbb P(|K_m/m-r|>\varepsilon)=o(m^{-1}).
\]
A self-contained concentration argument uses the random-clock greedy process on the cycle. To determine a site's decision it suffices to inspect its descending-clock causal cluster. The probability that this cluster extends farther than \(R\) sites is at most \(2/(R+1)!\), since a decreasing path of \(R+1\) distinct continuous clock values is necessary. Radius-\(R\) truncated occupancy indicators depend only on clocks within that radius, are bounded by one, and have a dependency distance at most \(2R\). The fourth centered moment of their sum is \(O(m^2R^2+mR^3)\), because a nonzero mixed term has no isolated index in its dependency graph. With \(R=\lceil3\log m\rceil\), Markov's inequality gives a deviation probability \(O(R^2/m^2+R^3/m^3)\), while the probability any truncation disagrees is \(O(m/(R+1)!)\), both \(o(m^{-1})\). The expectation is \(rm+O(1)\), as established above, and the truncated expectations differ negligibly. Since \(p_m\sim\lambda/m\), conditioning on \(A_m^{\mathrm G}\) now gives \(K_m/m\to r\) in probability. Boundedness \(0\le K_m/m\le1\) also gives convergence of its first and second conditional moments.

It follows from the pathwise identity and \(mp_m\to\lambda\) that
\[
\mathbb E(J_m^{\mathrm G}-K_m)\to\lambda(1-r)=\lambda e^{-2}
\]
and
\[
\frac1m\mathbb E[(J_m^{\mathrm G})^2-K_m^2]\to\lambda(1-r^2).
\]
Subtracting the squared-mean difference divided by \(m\), whose limit is \(2r\lambda(1-r)\), proves \(\lim_m (\operatorname{Var}J_m^{\mathrm G}-\operatorname{Var}K_m)/m=\lambda(1-r)^2=\lambda e^{-4}\). This completes the proof.

## Verification

The standalone standard-library program `verify.py` implements an independent exact rational first-arrival recursion for occupied-count first and second moments on each finite graph, using only site masks and arrival rates. It verifies the pathwise wheel formula and the signs of both mean responses for several rim lengths, including nonunit hub rates. Direct enumeration over all clock orders on the smallest graphs checks the gear pathwise identity. Numerical finite-size comparisons are consistency checks only: the asymptotic statements follow from the proof above. The baseline variance constant is sourced to [1, Theorem 11]; it is not inferred from finite samples.

## Relationship to prior work

Penrose and Sudbury [1] treat exact one-dimensional blocking deposition, including limiting variance \(e^{-4}\) per line site, and establish general finite-degree fluctuation results. Here the new graph hub has unbounded degree and is present at only one vertex, so its order-one mean effect and order-\(m\) variance response are not consequences of their bounded-degree theorem. Brightwell, Janson and Łuczak [2] study greedy independent sets and degree dependence, including stars; the wheel/gear opposite-sign defect comparison is different. Prior work on random greedy maximal independent sets for complete multipartite [3], threshold [4] and chain [5] graphs describes different graph classes and does not imply the present cycle-spoke equations. An inaccessible older adsorption treatment [6] may contain related geometric comparisons; that bibliographic uncertainty is not eliminated by name searches.

## Limitations

The theorem is for exponential single-attempt clocks, a fixed positive hub rate, and the specified simple wheel/gear graphs. It gives terminal expected counts and leading variances, not relaxation-time laws, complete count distributions, a central limit theorem for these high-degree graph families, or uniform statements as the hub rate scales with rim length. Originality is assessed relative to accessible inspected sources, not guaranteed against all literature; independent audit has not been performed.

## References

[1] M. D. Penrose and A. Sudbury, “Exact and approximate results for deposition and annihilation processes on graphs,” arXiv:math/0503519 (first public 2005-03-24), *Annals of Applied Probability* 15 (2005), 853–889; Theorem 11.

[2] G. Brightwell, S. Janson and M. Łuczak, “The greedy independent set in a random graph with given degrees,” arXiv:1510.05560 (2015), introduction and discussion of examples.

[3] “Sharp variance of random greedy maximal independent sets on complete multipartite graphs,” published research record `2026/9/19/SCOPE-random-greedy-mis-variance-complete-multipartite--9cd73ef8690f`.

[4] “Exact random-greedy independent-set law on threshold graphs,” published research record `2026/10/4/SCOPE-exact-random-greedy-independent-set-law-on-threshold-graphs--13703984bf2d`.

[5] “Exact random-greedy maximal-independent-set law on chain graphs,” published research record `2026/10/4/SCOPE-exact-random-greedy-maximal-independent-set-law-on-chain-graphs--36fe61ce32de`.

[6] N. Pippenger, “Random Sequential Adsorption on Graphs” (1989), bibliographic abstract; relevant full text not inspected.

# A sharp hub-speed crossover between influence and consensus duration on a star

## Finding

Let \(n\ge 2\) be an integer and \(c>0\). In a continuous-time binary voter model on a star with one center and \(n\) leaves, every leaf updates at rate \(1\) by copying the center; the center updates at rate \(c\) by copying a uniformly selected leaf. All node clocks are independent. An update that copies the same opinion has no effect. Write \(H_j=\sum_{i=1}^{j}1/i\).

Starting from a single dissenting center or from a single dissenting leaf, the respective unconditional mean times to consensus are
\[
T_{\mathrm C}=\frac{nH_n}{n+c},
\qquad
T_{\mathrm L}=\frac{n+cH_{n-1}}{n+c}.
\]
The respective probabilities that the dissenter's opinion takes over are
\[
P_{\mathrm C}=\frac{1}{1+c},
\qquad
P_{\mathrm L}=\frac{c}{n(1+c)}.
\]
Define
\[
c_n=\frac{n(H_n-1)}{H_{n-1}}
=n-\frac{n-1}{H_{n-1}}.
\]
Then \(T_{\mathrm C}>T_{\mathrm L}\) exactly when \(0<c<c_n\), equality holds exactly at \(c=c_n\), and the inequality is reversed for \(c>c_n\). By contrast, \(P_{\mathrm C}>P_{\mathrm L}\) exactly when \(0<c<n\). Thus, on the nonempty interval \(c_n<c<n\), a dissenting center is *more likely* to impose its opinion yet has a *shorter* expected time until unanimity than a dissenting leaf.

A rate-invariance identity underlies the result: starting with exactly \(n-1\) leaves in disagreement with the center, expected consensus time equals \(H_{n-1}\), independently of \(c\). The interval width \(n-c_n=(n-1)/H_{n-1}\) grows asymptotically as \(n/\log n\).

## Assumptions and scope

The graph is the unweighted undirected star \(K_{1,n}\), not an arbitrary tree. The two opinions have equal intrinsic status. Each vertex has a fixed Poisson copying rate depending on its *position*, not its opinion, and rates remain unchanged as opinions change. Each center update samples one leaf uniformly. Time is physical continuous time; not the count of attempted updates. There are no zealots, spontaneous mutations, ties, or other transitions. The outcomes are eventual unanimity and its first hitting time.

For a binary configuration let \(k\in\{0,\ldots,n\}\) be the number of leaves currently disagreeing with the center. All configurations with the same \(k\) have the same conditional law of future \(k\), because of leaf symmetry and invariance under simultaneously exchanging the two opinion labels. State \(k=0\) is absorbing.

## Proof

**Exact discordance generator.** If \(k\ge1\), each of the \(k\) discordant leaves copies the center at rate one, and the resulting state has \(k-1\) discordant leaves. The center copies a discordant leaf at total rate \(ck/n\), flipping the center and leaving exactly \(n-k\) leaves discordant. Hence for \(\tau_k=\mathbb E_k[T]\), with \(\tau_0=0\),
\[
k(\tau_k-\tau_{k-1})
+\frac{ck}{n}(\tau_k-\tau_{n-k})=1
\qquad(1\le k\le n).
\tag{1}
\]
If \(k=n/2\), the second jump changes the center's opinion but not \(k\); its term is zero, as it should be. Since \(n\) is finite and \(c>0\), absorption is certain and the expected hitting time is finite: each discordant leaf has an independent positive-rate opportunity to copy the center, giving a uniformly positive probability of absorption within a bounded time from every transient state. Thus the finite generator equations characterize \(\tau\) uniquely.

**Telescoping the full system.** Dividing (1) by \(k\) and summing over \(k=1,\ldots,n\) gives
\[
\tau_n+\frac{c}{n}
\sum_{k=1}^{n}(\tau_k-\tau_{n-k})=H_n.
\]
The sum is \(\tau_n-\tau_0=\tau_n\), so
\[
\tau_n=\frac{nH_n}{n+c}.
\tag{2}
\]
The \(k=n\) equation gives
\[
\tau_{n-1}=
\left(1+\frac{c}{n}\right)\tau_n-\frac1n
=H_n-\frac1n=H_{n-1}.
\tag{3}
\]
Inserting (3) into the \(k=1\) equation yields
\[
\tau_1=\frac{n+cH_{n-1}}{n+c}.
\tag{4}
\]
One dissenting center means all \(n\) leaves disagree (\(k=n\)); one dissenting leaf means \(k=1\). Equations (2) and (4) are the asserted times, and (3) establishes the additional invariance.

**Fixation probabilities.** For each vertex \(v\) let \(r_v\) be its update rate and \(d_v\) its degree. The weighted opinion count
\[
M_t=\sum_{v}\frac{d_v}{r_v}\,\eta_v(t)
\]
is a martingale. Indeed, for every unoriented edge \(uv\), the expected increment contributed by copying \(u\) from \(v\) is \(\eta_v-\eta_u\), and the reverse-copy increment is \(\eta_u-\eta_v\); they cancel exactly because \(r_v(d_v/r_v)/d_v=1\). At the absorbing all-zero or all-one configuration, \(M_T\) is respectively \(0\) or \(\sum_vd_v/r_v\). Bounded optional stopping applies and gives the fixation probability as initial weight divided by total weight. The center has weight \(n/c\), each leaf weight \(1\), and their sum is \(n/c+n\). The formulas for \(P_{\mathrm C}\) and \(P_{\mathrm L}\) follow.

**Sharp ordering.** Subtraction yields
\[
T_{\mathrm C}-T_{\mathrm L}
=\frac{n(H_n-1)-cH_{n-1}}{n+c},
\quad
P_{\mathrm C}-P_{\mathrm L}
=\frac{n-c}{n(1+c)}.
\]
The first numerator is strictly decreasing in \(c\) with its sole zero \(c_n\); the second changes sign at \(c=n\). Since \(H_n>1\) and \(H_n-1=H_{n-1}-(n-1)/n\), one has \(0<c_n<n\). This proves all the sharp comparisons. The harmonic-number asymptotic \(H_{n-1}\sim\log n\) gives \(n-c_n\sim n/\log n\).

## Verification

`verify_star_voter.py` uses exact rational Gaussian elimination on the independent \(n\)-state discordance generator at 77 pairs \((n,c)\) for \(2\le n\le12\); it independently constructs the full binary-configuration generator for 28 pairs with \(2\le n\le5\). Both agree with the formulas. The program also checks threshold identities, the fixation-probability ordering, and the following exact example.

For \(n=4\) and \(c=3\), the threshold is \(c_4=26/11\), while
\[
T_{\mathrm C}=\frac{25}{21}<\frac{19}{14}=T_{\mathrm L},
\qquad
P_{\mathrm C}=\frac14>\frac3{16}=P_{\mathrm L}.
\]
The proof of all-size statements is (1)--(4) and the martingale calculation; finite computation is only a check.

## Relationship to prior work

Sood, Antal, and Redner (2008, preprint first public 2007) study the voter model on heterogeneous-degree networks and emphasize that a lone central mutant on a homogeneous-rate star has fixation probability \(1/2\). Their bipartite consensus-time calculation uses a large-population approximation; it does not include heterogeneous *position-dependent* center copying rates or the exact two-starting-location time crossover. Masuda, Gibert, and Redner (2010) introduce heterogeneous intrinsic flip rates and study conservation laws and asymptotic consensus times primarily on regular lattices and complete graphs, not this sharp star comparison. Hadjichrysanthou, Broom, and Rychtař (2011) give absorption-time formulae for evolutionary games on stars with selection through strategy fitness and several update rules; their transition mechanism is not fixed node-specific Poisson copying rates. Iwamasa and Masuda (2014) compare consensus times across homogeneous-update graph topologies, not variation in a center's update rate.

The contribution assessed here is specifically the exact joint probability/time ordering on a position-rate-heterogeneous star, including the nonempty gap between thresholds \(c_n\) and \(n\). Classical star fixation effects and standard voter-model generators are not claimed as new.

## Limitations

This is an exact result for the star with location-specific constant rates; other graphs, multiple dissenters of arbitrary configuration, type-dependent fitness, simultaneous updates, and non-Markovian update clocks are not covered. No assertion about real-world opinion systems or causal influence is made. An equivalent star-chain reduction could exist in less visible stochastic-process literature despite the targeted comparisons.

## References

1. Sood, V., Antal, T., and Redner, S., *Voter Models on Heterogeneous Networks*, arXiv:0712.4288 (first posted 2007-12-27); *Physical Review E* 77, 041121 (2008), https://arxiv.org/abs/0712.4288 .
2. Masuda, N., Gibert, N., and Redner, S., *Heterogeneous Voter Models*, arXiv:1003.0768 (first posted 2010-03-03); *Physical Review E* 82, 010103 (2010), https://arxiv.org/abs/1003.0768 .
3. Hadjichrysanthou, C., Broom, M., and Rychtař, J., *Evolutionary Games on Star Graphs Under Various Updating Rules*, *Dynamic Games and Applications* 1, 386–407 (2011), https://doi.org/10.1007/s13235-011-0022-7 .
4. Iwamasa, Y., and Masuda, N., *Networks Maximizing the Consensus Time of Voter Models*, *Physical Review E* 90, 012816 (2014), https://doi.org/10.1103/PhysRevE.90.012816 .

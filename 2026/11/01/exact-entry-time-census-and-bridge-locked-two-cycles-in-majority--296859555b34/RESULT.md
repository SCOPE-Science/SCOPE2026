# Exact entry-time census and bridge-locked two-cycles in majority barbells

## Finding

Let \(B_m\), \(m\ge2\), be the labelled graph consisting of two vertex-disjoint copies of \(K_m\) joined by one edge between distinguished vertices \(a\) and \(b\). Every vertex has a binary state. All vertices update simultaneously to the strict majority of their neighbors' states; in a tie, a vertex keeps its current state. Write \(F\) for one update and
\[
T(x)=\min\{t\ge0:F^{t+2}(x)=F^t(x)\}.
\]
Let \(s_t(m)\) count labelled initial states \(x\) with \(T(x)=t\). These numbers, together with every recurrent orbit, have the following exact description.

If \(m\ge3\) is odd, put \(H=\binom{m-1}{(m-1)/2}\). Then
\[
s_0(m)=4,\quad s_1(m)=4^m-4-2H(2^m-H),\quad s_2(m)=2H(2^m-H),
\]
with \(s_t(m)=0\) for \(t>2\). The only periodic orbits are four fixed configurations, one for each choice of a uniform color on each clique.

If \(m\ge4\) is even, put \(C=\binom{m}{m/2}\) and \(U=2^m-C\). Then
\[
\begin{aligned}
s_0(m)&=4+\tfrac12C^2,\\
s_1(m)&=U^2-4,\\
s_2(m)&=CU+\tfrac12C^2,\\
s_3(m)&=2^{m-1}C,\\
s_4(m)&=C(2^{m-1}-C),
\end{aligned}
\]
with \(s_t(m)=0\) for \(t>4\). There are four fixed configurations and exactly \(C^2/4\) distinct primitive two-cycle orbits. A state lies on a primitive two-cycle if and only if both cliques initially have exactly \(m/2\) ones and the two distinguished bridge endpoints initially have opposite colors. No state outside these periodic configurations can enter a primitive two-cycle.

For the small case \(m=2\), the graph is a four-vertex path: \((s_0,s_1,s_2)=(6,6,4)\), all later counts vanish, and there are four fixed configurations and exactly one primitive two-cycle orbit. Again, the two-cycle has no nonperiodic preimages.

Consequently the sharp worst-case first-entry time is \(2\) for odd \(m\ge3\), \(4\) for even \(m\ge4\), and \(2\) for \(m=2\). For uniformly random initial binary states, in the even case
\[
\Pr(\text{primitive period two})=\frac{C^2}{2\,4^m}\sim\frac1{\pi m},\qquad
\Pr(T=4)=\frac{C(2^{m-1}-C)}{4^m}\sim\frac1{\sqrt{2\pi m}}.
\]
Here the probability of primitive period two concerns initial states, whereas \(C^2/4\) counts two-point orbits.

## Assumptions and scope

The graph is simple and undirected, with no loops other than the implicit self-state tie rule. The bridge joins exactly one prescribed vertex of each labelled clique, not every corresponding pair. All \(2m\) spins are independently assignable at time zero, so there are \(4^m\) labelled configurations. No quotient by vertex permutations, color exchange, or clique exchange is taken. Primitive orbits are quotiented only by temporal cyclic rotation. The first-entry time is defined using the two-step test because all eventual periods are one or two; the proof below establishes this directly on this graph, without importing a general period theorem.

## Proof

**One-clique update identity.** Fix one clique. Let \(k\) be its current number of ones; let \(u\in\{0,1\}\) be its distinguished bridge vertex, and \(v\in\{0,1\}\) the bridge vertex in the other clique. A nonbridge vertex with old state \(z\) sees exactly \(k-z\) ones among its \(m-1\) neighbors. The bridge vertex sees \(k-u+v\) ones among its \(m\) neighbors. These two counts determine the entire update, including ties.

**Odd clique size.** Write \(m=2q+1\). For \(k\ge q+1\), every nonbridge vertex becomes one; for \(k\le q\), every nonbridge vertex becomes zero. Thus every clique's nonbridge vertices adopt its original strict internal majority \(c\) at the first update. Its bridge vertex also adopts \(c\), except in either of the following opposite-color, weakest-margin cases:
\[
(k,u,v)=(q+1,1,0)\quad\text{or}\quad(k,u,v)=(q,0,1).
\]
In either exceptional case, the bridge vertex adopts \(1-c\) while all nonbridge vertices adopt \(c\). At the next update it necessarily adopts \(c\), because at least two of its same-clique neighbors hold \(c\), and every nonbridge vertex retains \(c\). Hence both cliques are uniform, and permanently so, by time two. Exactly four states are periodic, namely the uniform-on-each-clique states.

Count the states requiring the second update. In one specified clique and for either majority color \(c\), the bridge bit must equal \(c\), the other bridge bit must equal \(1-c\), and exactly \(q\) of the remaining \(2q\) vertices must have color \(c\). Thus the number for which that specified clique is exceptional is \(2H2^{m-1}=H2^m\). Both cliques are simultaneously exceptional in exactly \(2H^2\) states (the two majorities are opposite). Inclusion-exclusion gives \(s_2=2H2^m-2H^2=2H(2^m-H)\). The four already periodic states give \(s_0=4\), and subtraction from \(4^m\) gives \(s_1\). For every odd \(m\ge3\), some states realize \(T=2\), proving sharpness.

**Even clique size.** Write \(m=2q\). If \(k<q\), the entire clique becomes zero in one update. If \(k>q\), the entire clique becomes one. If \(k=q\), each nonbridge vertex flips and the bridge vertex takes the old opposite bridge state \(v\). Call \(k=q\) *balanced*; otherwise call the clique *unbalanced*. A uniform clique remains uniform forever when \(m\ge2\), regardless of the opposite bridge color.

If both cliques are initially unbalanced, they become uniform and fixed after one update; only the four initially uniform pairs are fixed at time zero. If both are balanced and have opposite bridge bits, every vertex flips at each update, giving a primitive two-cycle from time zero. If both are balanced and their bridge bits agree, both become unbalanced after one update and uniform after a second. The latter first-entry time is exactly two for \(m\ge4\).

Suppose exactly one clique is balanced. Let \(u\) be its bridge bit, \(v\) the other clique's bridge bit, and \(c\) the strict initial majority color of the unbalanced clique. The other clique becomes permanently uniform \(c\) at time one. If \(v=u\), the balanced clique becomes unbalanced at time one and uniform at time two: \(T=2\). If \(v\ne u\) and \(c=v\), it remains balanced at time one, becomes unbalanced at time two, and uniform at time three: \(T=3\). If \(v\ne u\) and \(c=u\), it remains balanced through time two, becomes unbalanced at time three, and becomes uniform at time four: \(T=4\). For \(m\ge4\), every intermediate unbalanced clique in these cases has one dissenting bridge vertex and is not yet uniform; therefore these are exact first-entry times. These cases exhaust all configurations and prove there are no transients leading to the two-cycle class.

**Even-size enumeration.** There are \(C\) balanced colorings of one clique, exactly \(C/2\) for each specified bridge bit, and \(U=2^m-C\) unbalanced colorings. For a specified strict-majority color \(c\), the number of unbalanced colorings whose bridge bit agrees with \(c\) is
\[
I=\sum_{j=q}^{2q-1}\binom{2q-1}{j}=2^{m-2},
\]
whereas the number whose bridge bit disagrees with \(c\) is
\[
J=\sum_{j=q+1}^{2q-1}\binom{2q-1}{j}=2^{m-2}-C/2.
\]
Here \(2(I+J)=U\). Both-balanced, opposite-bridge assignments total \(C^2/2\) labelled period-two states, giving \(C^2/4\) temporal orbits. Both-balanced, same-bridge assignments total \(C^2/2\) states at \(T=2\). Among exactly-one-balanced assignments, the three cases \((v=u)\), \((v\ne u,c=v)\), and \((v\ne u,c=u)\) have respective counts \(CU\), \(2CI\), and \(2CJ\). Combining these with the both-unbalanced states gives the stated five entry-time counts. Their sum is \(4^m\), as required.

For \(m=2\), each unbalanced clique is *already* uniform. Both-balanced, same-bridge states enter a fixed configuration after one update; exactly-one-balanced states take one update if the bridge bits agree and two if they disagree. The four uniform pairs and the two period-two states have entry time zero, giving \((6,6,4)\).

**Sharpness and asymptotics.** For every \(m=2q\ge4\), one has \(J=2^{m-2}-C/2>0\), so a configuration attaining \(T=4\) exists. For odd \(m\ge3\), \(0<H<2^m\), so \(s_2>0\). The central-binomial estimate \(\binom{m}{m/2}/2^m\sim\sqrt{2/(\pi m)}\) yields both stated limiting probabilities. This completes the proof.

## Verification

The standalone script `verify.py` enumerates every labelled state on \(B_m\) for \(2\le m\le9\), updates from explicit bit-mask neighbor sets without using the proof's clique-level transition cases, and finds the exact first \(t\) for which \(F^{t+2}(x)=F^t(x)\). It compares the entire time histogram with the formulas above and independently counts primitive two-cycle orbits and nonperiodic states entering a two-cycle. There are exactly \(349520\) states across these sizes. The script also checks nonnegativity and total-count identities symbolically over integer sizes \(2\le m<300\). Its recorded output is supplied in `verification_output.txt`.

The exhaustive checks are finite diagnostics, not a proof for all \(m\); the general result follows from the local majority identities and the counting argument above.

## Relationship to prior work

Goles and Olivos established the eventual period-at-most-two property for symmetric binary threshold dynamics; this does not give a first-entry histogram or individual orbit populations on this graph. Kaaser, Mallmann-Trenn and Natale developed upper bounds on deterministic-majority convergence times using potential functions and graph modules; their 2015 preprint defines the same lazy-tie update and voting-time statistic but gives neither the present sharp constant nor a barbell-specific census. Benjamini and collaborators study general period-two behavior and probabilistic unanimity, not the exact two-clique finite census. Masuda's two-clique work treats a random sequential voter model, for which the dynamics and consensus times differ substantially from deterministic synchronous majority. Thus identical graph terminology does not imply the present statements. Relevant known censuses on complete multipartite, ladder, or matching-coupled clique graphs do not imply the effect of replacing all interclique matching edges by a single bridge.

## Limitations

The theorem concerns two cliques of equal size with exactly one bridge and binary strict-neighbor majority with tie retention. It does not establish the corresponding full census for unequal clique sizes, multiple bridges, stochastic voter models, or asynchronous schedules. Historical equivalence outside the inspected sources remains possible. Computational agreement over finite sizes cannot establish novelty or an infinite statement. No independent audit has been performed.

## References

1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. D. Kaaser, F. Mallmann-Trenn and E. Natale, “On the Voting Time of the Deterministic Majority Process,” arXiv:1508.03519v1, first submitted 14 August 2015, https://arxiv.org/html/1508.03519v1.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1, first submitted 11 May 2014, https://arxiv.org/abs/1405.2486.
4. N. Masuda, “Voter model on the two-clique graph,” arXiv:1403.4763v1, first submitted 19 March 2014, https://arxiv.org/abs/1403.4763; *Physical Review E* 90 (2014), 012802, DOI: 10.1103/PhysRevE.90.012802.

# A sharp nine-vertex onset of mixed sentinel placement in two-hub outbreak networks

## Finding
Consider a two-hub contact network with \(m\ge2\) peripheral individuals, with every peripheral individual connected to both hubs and no other connections. Independently retain each contact edge with common probability \(p\in(0,1)\). An outbreak begins at one uniformly random vertex (monitored vertices included), spreads over its entire retained-edge component, and is detected if the component contains at least one of two preselected passive sentinels.

**Theorem (sharp mixed-placement onset).** A pair containing one hub and one peripheral individual is strictly better for outbreak-detection probability than both a pair of hubs and a pair of peripheral individuals for some transmissibility \(p\in(0,1)\) **if and only if \(m\ge7\)**. Consequently, the first contact network supporting a strictly optimal mixed pair in this family has nine vertices. When \(m=7\), the strict improvement holds at \(p=11/20\); for every \(m\ge8\), it holds at \(p=1/2\). By continuity, the improvements persist on nonempty open intervals of transmission probabilities. For \(2\le m\le6\), no mixed pair is globally optimal at any interior transmissibility.

The three symmetry types of two-sentinel placements are denoted HH (two hubs), HL (one hub and one leaf), and LL (two leaves). For \(q=1-p\), \(r=1-p^2\), and \(b=1-q^2\), let \(U_X=(m+2)(1-D_X)\) be the expected number of unmonitored sources that cannot reach either sentinel, where \(D_X\) is detection probability for placement \(X\). For \(m\ge3\), the exact formulas are
\[
\begin{aligned}
U_{HH}&=m q^2,\\
U_{HL}&=q^2\big[(m-1)+(1+mp)r^{m-2}\big],\\
U_{LL}&=q^2\big[(m-2)+q^2(2+(m-2)b)+2bq(1+(m-1)p)r^{m-3}\big].
\end{aligned}
\]
For \(m=2\), \(U_{HH}=U_{LL}=2q^2\) and \(U_{HL}>U_{HH}\). Minimizing \(U_X\) is equivalent to maximizing \(D_X\).

## Assumptions and scope
The graph is the finite simple undirected complete bipartite graph \(K_{2,m}\); no temporal or directed transmission is asserted. Every edge is independently open with the same probability; the outbreak from a single uniformly selected source reaches its whole connected component. The two monitors are fixed and perfect, cannot prevent transmission, and count as possible sources. All statements quantify over every integer \(m\ge2\), every allowed interior \(p\), and all unordered two-vertex monitoring sets. The edge model is a specific connectivity model, not a claim that all stochastic SIR epidemics are exactly independent bond percolation.

## Proof
**1. Exact component probabilities.** For HH, only peripheral seeds can go undetected. Each must have both incident edges closed, independently with probability \(q^2\); hence \(U_{HH}=mq^2\).

For HL, denote the monitored leaf by \(z\) and the monitored hub by \(a\); let \(c\) be the unmonitored hub. Hub \(c\) fails to reach either monitor precisely when \(cz\) is closed and all \(m-1\) two-edge paths through the other leaves to \(a\) are blocked, with probability \(q r^{m-1}\). An unmonitored leaf \(x\) fails to reach a monitor with probability \(q^2[1+p r^{m-2}]\): its edge to \(a\) must be closed, and if its edge to \(c\) is open, the other edge-disjoint routes from \(c\) to a monitor must fail. Summing over \(m-1\) such leaves and using \(r=q(1+p)\) gives \(U_{HL}\) above.

For LL, the two monitored leaves are \(z_1,z_2\). A specified hub is not connected to a monitor with probability \(q^2[q^2+b r^{m-2}]\): its own two monitor edges are closed, and either the other hub has no direct monitored-leaf edge or there is no unmonitored two-edge bridge to it. For an unmonitored leaf \(x\), first remove its edges. Let \(A,B\) say whether the respective hubs reach a monitor without \(x\). Then \(x\)'s failure probability is \(\mathbb E[(1-p\mathbf1_A)(1-p\mathbf1_B)]\). Direct monitor incidences of the two hubs are independent, with success probability \(b\), and they are bridged through the remaining \(m-3\) unmonitored leaves with probability \(1-r^{m-3}\). Therefore the failure probability of \(x\) equals \((1-pb)^2-2p q^3b(1-r^{m-3})\). Summing two hub failures and \(m-2\) peripheral failures and simplifying gives \(U_{LL}\). For \(m=2\), the two sides of \(K_{2,2}\) are symmetric and the same HH/LL value follows directly.

**2. HH–HL crossing.** Subtracting yields
\[
U_{HL}-U_{HH}=q^2\big[(1+mp)(1-p^2)^{m-2}-1\big].
\]
For \(m=2\) this is \(2pq^2>0\). For every \(m\ge3\), the logarithmic derivative of \(F_m(p)=(1+mp)(1-p^2)^{m-2}\) is
\[
\frac{m}{1+mp}-\frac{2(m-2)p}{1-p^2},
\]
which decreases strictly from positive to negative. Thus \(F_m\) first increases from \(F_m(0)=1\), then decreases to \(F_m(1)=0\), crossing level one exactly once in the interior. In particular, to ensure HH is better than HL for every \(p\le a\), it is enough to verify \(F_m(a)>1\).

**3. Excluding mixed optima for \(m\le6\).** For \(m=3\),
\[
U_{LL}-U_{HL}=pq^2(3p^3-3p^2-1)<0.
\]
For \(m=4\),
\[
U_{LL}-U_{HL}=-p^3q^2(6p^3-12p^2+3p+4)<0,
\]
because the final cubic equals \(4(1-p)^3+15p(1-p)^2+6p^2(1-p)+p^3>0\).

For \(m=5\), \(U_{HL}-U_{HH}>0\) at \(p=1/2\), where it equals \(61/512\); the unique crossing from step 2 implies HH is strictly better for every \(p\le1/2\). On \([1/2,1]\), write
\[
U_{LL}-U_{HL}=p q^2 f_5(p),\quad
f_5(p)=8p^7-17p^6-5p^5+33p^4-18p^3-3p^2+1.
\]
After substituting \(p=(1+t)/2\), the degree-seven Bernstein coefficients of \(-f_5\) are exactly
\[
(1995,3855,5510,6708,7296,7360,7200,6720)/6720.
\]
All are positive, so LL is strictly better on \([1/2,1)\).

For \(m=6\), the same argument uses \(a=11/20\), where \(U_{HL}-U_{HH}=368267721723/102400000000000>0\). For
\[
f_6(p)=-10p^9+22p^8+15p^7-64p^6+16p^5+60p^4-42p^3+2,
\]
we have \(U_{LL}-U_{HL}=pq^2 f_6(p)\). On \([11/20,1]\), the degree-nine Bernstein coefficients of \(-f_6\), multiplied by \(358400000000\), are
\[
(34820250689,130840487848,215172026370,283058412200,332256472000,363573600000,379976000000,384160000000,376320000000,358400000000).
\]
These are all positive. Here a degree-\(d\) Bernstein expansion means \(\sum_{j=0}^{d} c_j\binom dj t^j(1-t)^{d-j}\); positive coefficients imply strict positivity for \(0\le t\le1\). Hence either HH or LL always strictly improves upon HL when \(m=5\) or \(6\).

**4. Existence for \(m\ge7\).** At \(m=7\) and \(p=11/20\), exact subtraction gives
\[
U_{HL}-U_{HH}=-\frac{3306362852256057}{81920000000000000}<0,
\qquad U_{LL}-U_{HL}=\frac{5900587445173509}{204800000000000000}>0.
\]
Thus the mixed pair strictly wins. For every \(m\ge8\), take \(p=1/2\). Then
\[
\frac{U_{HL}-U_{HH}}{q^2}=(1+m/2)(3/4)^{m-2}-1<0:
\]
this is negative at \(m=8\) and the positive first term is strictly decreasing as a function of integral \(m\ge8\). Moreover,
\[
\frac{U_{LL}-U_{HL}}{q^2}=
\frac{3m-14}{16}-\frac38(3/4)^{m-3}>0
\]
for every \(m\ge8\), using \((3m-14)/16\ge10/16>3/8\). Strict inequalities persist in a neighborhood of each stated \(p\), since every detection probability is continuous. This proves the sharp threshold and the entire stated scope.

## Verification
The standalone `verify.py` uses `fractions.Fraction`. It independently enumerates all \(2^{2m}\) edge states, their connected components, and all uniform outbreak origins for \(2\le m\le6\) at three exact rational probabilities. It checks 15 graph/parameter cases comprising 16,368 edge states, verifies the algebraic factor and Bernstein certificates for \(m=5,6\), checks the exact strict inequalities for \(m=7\), and checks values through \(m=100\) as a finite corroboration of the analytic large-\(m\) proof. Run `python verify.py`; the expected JSON output is embedded in `verification_output.json`. These finite experiments do not establish the infinite-parameter theorem without the proof above.

## Relationship to prior work
Leskovec and collaborators' 2007 outbreak-detection framework develops general submodularity and approximate sensor-selection algorithms. That framework motivates maximizing detection likelihood but does not give the exact three-orbit classification for uniformly seeded independent-edge outbreaks on \(K_{2,m}\), nor the nine-vertex mixed-placement onset. Kenah and Robins (2006) distinguish independent bond percolation from broader SIR transmission models, delimiting the precise modeling assumption here. The separate literature on two-terminal reliability is related to path existence between specified endpoints; the present objective averages over all possible outbreak sources and chooses a two-vertex target set. Discounted graph hitting domination and fragile power domination on multipartite graphs have different propagation/reliability objectives and do not directly imply the present threshold. Prior path-, cycle-, and star-network calculations concern different graph families and different parameter questions. The bibliography search does not establish absolute novelty; equivalent classical network-reliability formulations remain a residual risk.

## Limitations
All results are exact for a stylized independent-undirected-bond process with a single uniformly random source including monitor positions, perfect detection, and precisely two monitors. No claim concerns optimality for heterogeneous contacts, arbitrary bipartite graphs, directed or continuous-time SIR dynamics, external importation rates, observation delays, or generalized mixed monitoring costs. The theorem gives a sharp threshold for **existence** of some transmissibility favoring mixed placement, not a complete classification of every transition probability for every \(m\).

## References
1. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057, first arXiv posting 2006-10-30, https://arxiv.org/abs/q-bio/0610057.
2. J. Leskovec, A. Krause, C. Guestrin, C. Faloutsos, J. VanBriesen and N. Glance, *Cost-effective Outbreak Detection in Networks*, CMU-ML-07-111 (June 2007), https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf; KDD 2007, doi:10.1145/1281192.1281239.
3. I. Brown, C. Graves, B. Miller and T. Russell, *Most reliable two-terminal graphs with node failures*, Networks 76 (2020), 414–426, doi:10.1002/net.21968 (related but distinct node-failure setting).

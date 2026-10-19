# Confidence-graph obstruction to equilibrium and exact circulation in noisy opinion copying

## Finding

In a finite multi-opinion noisy copying process, a *partial* confidence graph forces strictly irreversible stationary opinion flux, independently of the social graph and of the unanimity group size. The obstruction is witnessed by a three-configuration cycle with an explicit graph-independent affinity. Conversely, when one neighbor suffices to induce copying on a complete social graph, the finite process is reversible **exactly** for an empty or a complete confidence graph. The obstruction specializes to the three-opinion bounded-confidence noisy \(q\)-voter process of Doniec, Lipiecki, and Sznajd-Weron [1], including a closed stationary entropy-production law for the smallest two-person system.

**Theorem.** Let \(m\ge3\), let \(G\) be a finite undirected simple social graph on \(N\ge2\) labeled vertices, and let \(q\in\{1,\ldots,\min_{v\in G}\deg(v)\}\). Let \(H\) be a simple undirected graph on the \(m\) opinion labels, specifying permitted conformist copying. Assume the transition process and timescale stated below, with \(0<p<1\).

(a) If \(H\) contains an edge and a missing edge, the finite labeled-configuration Markov chain is irreducible but not reversible. In fact, three configurations form a directed cycle with Kolmogorov affinity
\[
\Lambda_m(p)=\log\!\left(1+\frac{m(1-p)}{p}\right)>0.
\]
The affinity is independent of \(N,G,q\) and of which qualifying confidence edges are used.

(b) For \(q=1\) and \(G=K_N\), **reversibility holds if and only if** \(H\) is empty or complete. If \(H\) is empty, the stationary law is the uniform product measure. If \(H\) is complete, write \(n_j(s)\) for the number of opinion-\(j\) vertices in configuration \(s\), and set \(\theta=(N-1)p/[m(1-p)]\). The explicit stationary probability is
\[
\pi(s)=Z^{-1}\prod_{j=1}^m(\theta)_{n_j(s)},
\qquad
(\theta)_r=\prod_{h=0}^{r-1}(\theta+h),
\]
where \(Z\) sums the displayed weights over all labeled configurations. At \(p=1\), the process is independent uniform resampling and reversible for every \(G,H,q\).

(c) For the original three opinions with compatibility path \(1\!\sim\!2\!\sim\!3\) and \(1\not\sim3\), on \(K_2\) with \(q=1\), let a count configuration be denoted by \((n_1,n_2,n_3)\). In the order \((2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)\), the unique stationary count probabilities are
\[
\pi_{\rm cnt}=\frac{1}{9}(2-p,\ 2p,\ 2,\ 3-2p,\ 2p,\ 2-p).
\]
There are two oriented stationary probability-current triangles, each with current \(J=2p(1-p)/27\) and affinity \(\log((3-2p)/p)\); all other edge currents vanish. Consequently, the exact count-chain entropy-production rate in natural logarithm units per unit model time is
\[
\mathcal E(p)=\frac{4p(1-p)}{27}\log\frac{3-2p}{p}.
\]
It is strictly positive for \(0<p<1\), approaches zero at both endpoints, and has a **unique global maximum** at the unique solution \(p_*\in(0,1/2)\) of
\[
(1-2p_*)\log\frac{3-2p_*}{p_*}=\frac{3(1-p_*)}{3-2p_*}.
\]
Numerically, \(p_*\approx0.291984797141795\) and \(\mathcal E(p_*)\approx0.064719539702587\).

## Assumptions and scope

The social graph \(G\) and confidence graph \(H\) play different roles. Each social vertex has a state in \(\{1,\ldots,m\}\). Each vertex updates at the event times of an independent rate-one Poisson clock. With probability \(p\), it draws a fresh opinion uniformly from all \(m\) opinions (including its current opinion); otherwise, it samples \(q\) **distinct** social neighbors uniformly without replacement and copies their shared opinion only if they are unanimous and that opinion is adjacent to its current one in \(H\). A null update has no state change. A rate-one clock at every vertex corresponds to one random-sequential elementary update per expected duration \(1/N\), i.e. ordinary Monte Carlo steps. Positive independence ensures that all single-vertex changes have positive rates. The cycle affinity refers to the labeled-state continuous-time chain; the entropy-production formula in (c) refers to the lumped count chain on \(K_2\).

Write \(u=p/m\) and \(v=1-p\). If a configuration \(s\) has state \(i\) at vertex \(x\), and \(s'\) changes only this vertex to \(j\ne i\), its off-diagonal generator entry is
\[
Q(s,s')=u+v\,\mathbf 1_{\{ij\in E(H)\}}
\frac{\binom{d_j(x;s)}{q}}{\binom{\deg_G(x)}{q}},
\]
where \(d_j(x;s)\) is the number of \(j\)-opinion neighbors of \(x\), and a binomial numerator is zero if its top argument is smaller than \(q\). Off-diagonal rates for multi-vertex changes are zero; row sums vanish. All claims quantify over every permitted finite \(N,q,G,H,p\) unless explicitly restricted.

## Proof

**Step 1: elementary irreversibility cycle.** If \(H\) is neither empty nor complete, there are three *distinct* opinions \(a,b,c\) such that \(ab\in E(H)\) while \(ac\notin E(H)\). Indeed, take a connected component containing an edge; if it is not all vertices, an endpoint of that edge has a nonneighbor. If it contains all vertices yet is not complete, a shortest path from a vertex to one of its nonneighbors starts with a neighbor and ends at a nonneighbor. Fix a social vertex \(x\) and let \(A\) be the all-\(a\) configuration, \(B\) the configuration with only \(x\) changed to \(b\), and \(C\) the one with only \(x\) changed to \(c\).

All \(q\) neighbors of \(x\) have opinion \(a\), for **every** one of the three configurations. Hence
\[
Q(A,C)=Q(C,B)=Q(A,B)=Q(B,C)=Q(C,A)=u,
\qquad Q(B,A)=u+v.
\]
The products of rates along \(A\to C\to B\to A\) and its reverse are \(u^2(u+v)\) and \(u^3\). Their log ratio is exactly \(\log((u+v)/u)=\Lambda_m(p)>0\). Independent resampling gives positive rate for every single-site recoloring, so the finite state space is irreducible. Kolmogorov's necessary cycle-product condition for detailed balance is violated, and the unique stationary measure is not reversible. No limit, finite truncation or simulation is used in this argument.

**Step 2: sharp classification when \(q=1\) on \(K_N\).** Necessity is Step 1. For empty \(H\), every off-diagonal single-site rate is \(u\); the uniform probability on all \(m^N\) states satisfies detailed balance. For complete \(H\), if a site changes from \(i\) to \(j\), denote its pre-change counts by \(n_i,n_j\). The forward rate is \(u+v n_j/(N-1)\) and the reverse rate is \(u+v(n_i-1)/(N-1)\). Setting \(\theta=(N-1)u/v\), the proposed weight obeys
\[
\frac{\pi(s')}{\pi(s)}
=\frac{\theta+n_j}{\theta+n_i-1}
=\frac{Q(s,s')}{Q(s',s)}.
\]
Normalization is finite and positive. Every possible edge satisfies detailed balance, proving sufficiency and the exact law. For \(p=1\), \(v=0\) and all changes occur at the common rate \(u=1/m\), proving the last assertion without using \(\theta\) at the boundary.

**Step 3: exact smallest-population stationary law.** For \(N=2,q=1\) with confidence path \(1-2-3\), the six count states in part (c) form an irreducible Markov chain. A change from opinion \(i\) to \(j\) in a count state \(n\) has aggregate rate
\[
\underbrace{n_i}_{\text{available changing vertices}}
\left(\frac p3+(1-p)n_j\,\mathbf1_{\{|i-j|=1\}}\right),
\]
where the second term uses that each changing vertex has exactly one social neighbor. Direct substitution of the six displayed stationary probabilities into all six generator balance equations gives zero, and their sum is one. Irreducibility proves uniqueness. Their only nonzero currents follow the two directed triangles
\[
(2,0,0)\longrightarrow(1,0,1)\longrightarrow(1,1,0)\longrightarrow(2,0,0)
\]
and
\[
(0,0,2)\longrightarrow(1,0,1)\longrightarrow(0,1,1)\longrightarrow(0,0,2).
\]
Every edge in these triangles carries \(J=2p(1-p)/27\). Each corresponding loop's forward/backward rate product is \((3-2p)/p\). The stationary entropy-production identity \(\mathcal E=\sum_{\{s,t\}}[\pi_sQ_{st}-\pi_tQ_{ts}]\log[\pi_sQ_{st}/(\pi_tQ_{ts})]\) sums over **unordered** adjacent pairs; since the log stationary-mass factors telescope on each triangle, it yields \(2J\log[(3-2p)/p]\), as claimed. Count-level entropy production is explicitly claimed, avoiding any unproved equality to an alternative coarse-graining.

**Step 4: unique maximum.** Put \(L(p)=\log[(3-2p)/p]>0\) and \(f(p)=p(1-p)L(p)\). Direct differentiation gives
\[
f'(p)=(1-2p)L(p)-\frac{3(1-p)}{3-2p},
\]
\[
f''(p)=-2L(p)-\frac{3(1-2p)}{p(3-2p)}+\frac{3}{(3-2p)^2}.
\]
For \(0<p<1/2\), \(L(p)\ge\log4\), the middle summand is nonpositive, and the last is at most \(3/4\), so \(f''<0\) there. Furthermore \(f'(p)\to+\infty\) as \(p\downarrow0\), while \(f'(1/2)=-3/4\). There is exactly one critical point in \((0,1/2)\). For \(1/2\le p<1\), the displayed expression for \(f'\) is negative. Thus this point is the unique global maximum. Since \(p\log(1/p)\to0\) as \(p\downarrow0\) and \(\log[(3-2p)/p]\to0\) as \(p\uparrow1\), the endpoint limits of \(\mathcal E\) are both zero.

## Verification

The standalone `verify.py` uses Python's exact rational arithmetic to construct the finite labeled-state generators. It checks all six cycle-edge rates on the graphs \(K_2\), \(K_3\), a four-cycle and \(K_4\) at admissible unanimity group sizes; explicit detailed balance for complete confidence on \(K_2,K_3,K_4\); every stationarity equation, triangle current and numerical entropy-production identity on \(K_2\); and the unique peak equation by bisection. It reports **1479 exact graph, balance, and stationary-flow comparisons**, plus the numerical maximizer. These are independent finite checks of formulas whose universal assertions are proved above, not exhaustive verification of all graphs or parameters. To reproduce: `python3 verify.py` using only the standard Python library.

## Relationship to prior work

Doniec, Lipiecki, and Sznajd-Weron [1] specify three-state bounded-confidence copying with uniform independent resampling and analyze mean-field collective behaviors, stable concentrations and hysteresis; their exact finite-size transition probabilities (notably their independence and conformity terms in Section 3) motivate the process here. They do **not** in the inspected sections state this graph-independent microscopic cycle criterion, full \(q=1\) confidence-graph reversibility classification, or the exact two-person count-chain entropy production. Radosz and Doniec [2] consider a related earlier three-state bounded-confidence process, but there the independent opinion changes themselves are restricted to adjacent opinions; its transition graph and rates therefore differ from [1] and from this theorem. General Kolmogorov-cycle and stochastic-thermodynamic principles are established mathematics, **not** claimed as new; more recent discussions of nonequilibrium opinion imitation [3] address different models or broader thermodynamic methodology. The model-specific sharp classification and explicit circulation formula are the assessed contribution.

## Limitations

Part (a) is a one-sided obstruction: it does not assert that \(H\) empty or complete suffices for reversibility on arbitrary social graphs and arbitrary \(q\). The if-and-only-if statement in (b) requires **both** \(q=1\) and complete social contacts. Part (c) concerns the six-state **count chain** on two social vertices; its entropy production is not a universal formula for larger populations. The exact model requires strictly positive uniform independent opinion resampling and unbiased compatibility, so no assertion is made at \(p=0\), where irreducibility can fail. The proof is analytic, but literature coverage cannot establish publication priority; in particular, a more general reversibility theorem may imply some results.

## References

[1] M. Doniec, A. Lipiecki, and K. Sznajd-Weron, *Consensus, Polarization and Hysteresis in the Three-State Noisy q-Voter Model with Bounded Confidence*, Entropy **24** (2022), 983. DOI: 10.3390/e24070983. First public publication verified 2022-07-16. Model and Results sections, https://www.mdpi.com/1099-4300/24/7/983 .

[2] W. Radosz and M. Doniec, *Three-State Opinion Q-Voter Model with Bounded Confidence*, ICCS (2021), DOI: 10.1007/978-3-030-77967-2_24; open article https://www.iccs-meeting.org/archive/iccs2021/papers/127440285.pdf , especially Section 2 and Algorithm 1.

[3] *Stochastic thermodynamics of social imitation beyond energetics*, Nature Communications (2026), DOI: 10.1038/s41467-026-76212-0; general stochastic-thermodynamic framework for social imitation.

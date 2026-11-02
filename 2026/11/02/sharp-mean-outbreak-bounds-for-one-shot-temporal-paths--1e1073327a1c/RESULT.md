# Sharp mean outbreak bounds for one-shot temporal paths

## Finding
Fix an integer \(n\ge2\) and a per-contact transmission probability \(0<q\le1\). Let the contact network be the undirected path \(P_n\) on vertices \(1,\ldots,n\). Each edge is used in exactly one contact, and the \(n-1\) contacts occur at distinct positive times in an arbitrary order. One uniformly random vertex is infected before the first contact, remains infectious throughout, and transmits to its susceptible contact partner independently with probability \(q\). Let \(Z\) denote the total number ever infected after all contacts.

Across **all** contact orders, the sharp bounds on the seed-averaged, transmission-averaged outbreak size are
\[
\boxed{
1+\frac{2(n-1)}nq+\frac{n-2}{n}q^2
\;\le\;\mathbb E Z\;\le\;
1+\frac{2(n-1)}nq+\frac1n\sum_{d=2}^{n-1}(n-d)q^d.
}
\]
For \(n\ge4\), equality on the left occurs **exactly** when successive comparisons of edge-contact times alternate between increasing and decreasing (a zigzag order). Equality on the right occurs **exactly** when the contact times are monotone along the path. For \(n=2,3\), every order attains both bounds, which coincide. The empty sum is zero.

If the contact order is instead chosen uniformly among all \((n-1)!\) permutations, its joint mean outbreak size is exactly
\[
\boxed{\mathbb E_{\mathrm{order},\mathrm{seed},\mathrm{transmission}}Z
=1+\frac2n\sum_{d=1}^{n-1}\frac{(n-d)q^d}{d!}.}
\]
The mean number of **direct** secondary cases caused by the uniform index case, evaluated before secondary transmissions and averaged over contact outcomes, is always \(R_{\mathrm{index}}=2(n-1)q/n\), independent of the contact ordering. For \(q_n=1-1/n\), as \(n\to\infty\), the maximum mean outbreak size divided by \(n\) tends to \(1/e\), while the minimum tends to \(4\) and the random-order average tends to \(2e-1\). Thus contact calendars on the *same fixed path* with the *same direct index-case reproduction mean* can have mean outbreak sizes separated by an unbounded ratio (asymptotically \(n/(4e)\)).

## Assumptions and scope
The model is a finite-horizon, irreversible SI-type contagion: infection starts at time zero, every edge is contacted once at a positive distinct time, infection does not recover during observation, and an infected-susceptible contact succeeds with independent probability \(q\). A contact has no effect if both parties have the same infection status. There is a single uniform random initial case. The only control variable is the permutation of contact times, not their absolute values or the underlying path. The quantity \(R_{\mathrm{index}}\) is explicitly an index-case **direct-offspring mean**, not a claim about an infinite-population threshold or about a general next-generation operator.

Writing \(t_i\) for the time of edge \(\{i,i+1\}\), define an *alternating order* by the property that, for every \(i\) with \(1\le i\le n-3\), the inequalities \(t_i<t_{i+1}\) and \(t_{i+1}<t_{i+2}\) have opposite truth values. A *monotone order* has all consecutive times strictly increasing or all strictly decreasing along the path.

## Proof
**Unique-path reachability.** For distinct vertices \(u,v\), let \(d=|v-u|\). Because the underlying graph is a path, infection starting at \(u\) can reach \(v\) only along their unique \(d\)-edge path. The contacts on that path must occur in strictly increasing order in the direction from \(u\) to \(v\). If they do, each of its \(d\) contacts must transmit; by independence this happens with probability \(q^d\). Conversely, if the chronological ordering fails, some necessary edge is encountered before its upstream endpoint becomes infected, so that direction is impossible. This remains true even when other infections branch off the unique path.

**The exact mean.** Linearity of expectation over ordered source-target pairs gives
\[
\mathbb E Z=1+\frac1n\sum_{u\ne v} q^{|u-v|}
\mathbf1\{\text{edge times increase from }u\text{ toward }v\}.
\]
For each of the \(n-1\) adjacent unordered pairs, both one-edge directions are admissible. They contribute \(2(n-1)q/n\). For each unordered pair at distance \(d\ge2\), at most one of its two directions can have increasing contact times (the times are distinct). Precisely \(n-d\) unordered pairs have distance \(d\). Every two-edge interval is monotone in one direction, so all \(n-2\) distance-two pairs necessarily contribute \(q^2/n\). Every interval of length \(d\ge3\) contributes either \(q^d/n\) (if its times are strictly monotone) or zero. Since \(q>0\), discarding all terms for \(d\ge3\) gives the lower bound, and including every allowable term gives the upper bound.

**All equality cases.** An order minimizes the mean if and only if no consecutive triple of edge times is strictly monotone. This is exactly alternation of consecutive inequality signs, and in that case every longer interval also fails monotonicity. An order maximizes the mean if and only if all consecutive triples are monotone. For \(n\ge4\), overlapping triples force all consecutive inequality signs to agree, so the entire edge-time sequence is monotone. Both types exist for any \(n\). For \(n\le3\), there is no distance-three pair and all orders tie.

**Uniform random order.** For a particular unordered pair at distance \(d\ge2\), its \(d\) edge times have a uniformly random relative order. Exactly two of the \(d!\) relative orders are strictly monotone, so its expected contribution is \(2q^d/(nd!)\). The same formula correctly counts the two possible directions at distance one. Summing by distance proves the random-calendar formula.

**Same direct-offspring mean.** A seed at vertex \(u\) has \(\deg(u)\) initially susceptible neighbors and one eventual direct contact with each; unique paths preclude infection of a neighbor before its contact with the seed. Its expected number of direct secondary cases is therefore \(q\deg(u)\). Averaging and using \(\sum_u\deg(u)=2(n-1)\) proves \(R_{\mathrm{index}}\), regardless of calendar.

**Divergent separation.** With \(q_n=1-1/n\), the lower formula tends to \(1+2+1=4\). The upper formula, divided by \(n\), has leading Riemann sum
\[
\frac1{n^2}\sum_{d=2}^{n-1}(n-d)(1-1/n)^d
\longrightarrow\int_0^1(1-x)e^{-x}\,dx=\frac1e.
\]
For the random-order expression, dominated convergence for the factorial series gives \(1+2\sum_{d\ge1}1/d!=2e-1\). Thus the extremal ratio is asymptotic to \(n/(4e)\). The proof applies to every integer \(n\) and is not inferred from finite computation.

## Verification
The standalone standard-library script `verify.py` independently simulates the epidemic **contact by contact** for every initial vertex and every subset of successful contacts. It uses exact rational probabilities, exhaustively compares all permutations through \(n=7\), tests \(q\in\{1/2,2/3,1\}\), and compares the independently simulated means with the pair formula, both sharp bounds, the equality characterizations, and the random-calendar average. Its recorded successful run reads `ALL_CHECKS_PASSED assertions=10494; exact event simulation through 7 vertices; probabilities=1/2,2/3,1`. The symbolic arguments prove all \(n\); these finite computations are cross-checks, not infinite certificates.

## Relationship to prior work
Holme and Masuda (first public preprint July 24, 2014; journal 2015) analyzed why the mean number of direct secondary cases need not determine epidemic final size on empirical temporal contact networks, using stochastic SIR simulations. Their inspected full-text model and results do **not** provide the sharp all-order path formulas here. The present result supplies a clean exactly solvable finite-contact mechanism and an unbounded size separation while holding the path and transmission parameter fixed.

Enright, Meeks, and Skerman (first preprint 2018; journal 2021) studied **minimizing the maximum** temporal reachability over source vertices. Their inspected Section 2.2, Proposition 4, proves that the minimum possible *maximum* reachability on sufficiently long paths is four. That is different from minimizing the *uniform-source expected outbreak* with arbitrary transmission probability, deriving every equality case, or comparing to a random calendar. Both statements exploit path contact order, so the underlying path argument is not claimed as a new temporal-graph principle.

A published result titled *Local maxima determine temporal zero forcing on injectively timed paths* (public research record `593121ec75a3`) was also compared in full. It concerns the minimum number of initially corrupted vertices needed to force the entire path in a synchronous temporal zero-forcing rule and is not a statement about single-seed SI outbreak expectations or their optimization. Work on random temporal graphs and temporal paths independently supplies related factorial-order probabilities, so the \(1/d!\) ingredient is not claimed to be new by itself.

## Limitations
This result does not cover recovery, repeated contact events, simultaneous contacts, more general contact graphs, nonuniform seed laws, multiple initial cases, or behaviorally endogenous meetings. The exact unbounded-ratio claim uses transmission probabilities approaching one as the number of vertices grows; for every *fixed* \(q<1\), both bounds stay bounded as \(n\to\infty\). In this closed finite outbreak the defined index-case mean is not a stand-alone epidemic threshold. The literature comparisons do not establish exhaustive historical priority; an overlooked equivalent edge-ordered-path average theorem remains possible.

## References
1. P. Holme and N. Masuda, *The Basic Reproduction Number as a Predictor for Epidemic Outbreaks in Temporal Networks*, arXiv:1407.6598, first posted 2014-07-24; PLOS ONE 10(3), e0120567 (2015), https://pmc.ncbi.nlm.nih.gov/articles/PMC4368036/.
2. J. Enright, K. Meeks, and F. Skerman, *Assigning Times to Minimise Reachability in Temporal Graphs*, arXiv:1802.05905, first posted 2018-02-16; Journal of Computer and System Sciences 115, 169–186 (2021), https://arxiv.org/pdf/1802.05905.
3. *Local Maxima Determine Temporal Zero Forcing on Injectively Timed Paths*, public mathematical research record `593121ec75a3` (2026), consulted for a distinct contagion-like rule.
4. A. Casteigts, M. Raskin, M. Renken, and V. Zamaraev, *Sharp Thresholds in Random Simple Temporal Graphs*, arXiv:2011.03738 (2020), related random-time reachability, https://arxiv.org/abs/2011.03738.

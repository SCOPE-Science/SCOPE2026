# Exact fixed-point and oscillation census for majority dynamics on clique windmills

## Finding
For every integer \(r\ge1\), the generalized windmill \(G_r=K_1\vee(rK_3)\) has one hub and \(r\) labelled outer triangles. Let \(F_r\) update all binary states simultaneously by strict majority among each vertex's *open* neighbours, leaving a bit unchanged only when its neighbours tie. Then
\[
F_r^{6}=F_r^{4}.
\]
All eventual orbits have primitive period one or two. The sharp maximal preperiod is \(1\) for \(r=1\), \(3\) for \(r=2\), and \(4\) for every \(r\ge3\). The number of fixed states is
\[
P_1(r)=2\sum_{b=0}^{\lfloor r/2\rfloor}\binom rb=\begin{cases}2^r,&r\text{ odd},\\2^r+\binom{r}{r/2},&r\text{ even}.\end{cases}
\]
The number of **primitive two-cycles** (rather than periodic states) is
\[
C_2(r)=\sum_{\substack{a,b\ge0,\ a+b\le r\\2(2a+3b)>3r>2(a+3b)}}\binom ra\binom{r-a}b3^a.
\]
With \(u\in(0,1)\) the unique solution of \(u^2(1+u)=1\), and \(\beta=(1+3u^2+u^3)u^{-3/2}=4.787079\ldots<5\),
\[
0\le5^r-C_2(r)\le 2\beta^r.
\]
Thus primitive oscillations number \(5^r(1+o(1))\), exponentially more than the \(O(2^r\sqrt r)\) fixed states, while the proportion of periodic binary states among all \(2^{3r+1}\) states is asymptotic to \((5/8)^r\).

## Assumptions and scope
The graph is simple and undirected. Every outer vertex has degree three (the hub and its two triangle neighbours), while the hub has degree \(3r\). Binary states are labelled and independent on each outer triangle; counting cycles identifies the two time-phases as one orbit. Strict majority uses no self-loop. At a hub tie for even \(r\), the hub keeps its old bit. Define the preperiod of an initial state as the least nonnegative integer \(t\) satisfying \(F_r^{t+2}(x)=F_r^t(x)\).

## Proof
Write a triangle's binary configuration as \(q\in\{0,1\}^3\) with Hamming weight \(w\); let \(\overline q\) denote bitwise complement. A single update under fixed hub bit \(h\) has the following exact local table:
\[
\begin{array}{c|cccc}
w&0&1&2&3\\\hline
h=0&0&0&\overline q&1\\
h=1&0&\overline q&1&1
\end{array}
\]
Here \(0\) and \(1\) mean the uniform all-zero/all-one triples, not scalar weights. This follows by checking whether the two other triangle bits plus \(h\) contain at least two ones. For \(h=0\), every triangle's Hamming weight is nonincreasing; for \(h=1\) it is nondecreasing. The hub becomes one if the total triangle weight \(S\) exceeds \(3r/2\), zero if it lies below that threshold, and stays at its previous bit if equality holds.

If the hub retains its value on one update, the monotone change in \(S\) makes that hub value permanent. Subsequently every triangle settles into a uniform triple in at most two additional updates (under fixed hub zero: weight two to one to zero; under fixed hub one: weight one to two to three). If the hub never repeats on consecutive steps, its values alternate. In the first two alternating steps, every triangle enters the set \(\{000,111\}\) together with the three weight-two triples at the next zero-hub phase (or the three weight-one triples at the next one-hub phase). The two-step local action is then the identity. Thus three successive hub switches already make the states at times one and three identical, hence the orbit is two-periodic from time one. The only remaining pattern requiring four steps is a hub switch twice, followed by locking; the two final local updates settle all triangles. Hence \(F_r^{6}=F_r^{4}\).

At a fixed point every triangle is uniform. For hub zero, write \(b\) for the number of all-one triangles. The hub stays zero precisely when \(2b\le r\); for hub one, it stays one precisely when \(2b\ge r\). The binomial symmetry \(b\leftrightarrow r-b\) proves the fixed-point count.

On a primitive two-cycle, the hub necessarily alternates: holding the hub constant makes each triangle's weight monotone, hence forbids a nontrivial periodic triangle. Choose the unique time-phase with hub zero. The alternating local tables permit exactly three triangle types: all zero, all one, or any of the three weight-two patterns. Let their counts be \(r-a-b\), \(b\), and \(a\) respectively. On the hub-zero phase the outer total is \(2a+3b\); on the hub-one phase it is \(a+3b\), as weight-two triples become their weight-one complements. The hub must switch in both directions. Its thresholds give the *strict* inequalities \(2(2a+3b)>3r>2(a+3b)\); equality never causes a switch because ties retain the bit. Choosing triangle types yields \(\binom ra\binom{r-a}b3^a\). Every such choice gives one two-cycle and every two-cycle has exactly one zero-hub representative, proving the formula without dividing by two.

For the sharp preperiod, complete exhaustive enumeration of \(2^{3r+1}\) initial states for \(r=1,2\) yields maxima one and three. For \(r=3\), hub one with successive triangle bit patterns \((011,001,001)\) has preperiod four. For \(r=4\), hub one with patterns \((011,011,001,000)\) likewise has preperiod four. Appending a pair of all-zero and all-one triangles preserves the hub decision at every step: it adds exactly three outer ones while increasing the hub's comparison threshold by three. It also preserves the existing transient dynamics. These two witnesses therefore extend to every odd/even \(r\ge3\), respectively, proving sharpness for all sizes.

Finally, among \(5^r\) candidate zero-hub triangle arrangements (one all-zero, one all-one, three weight-two choices per triangle), the two switching conditions are the only exclusions. Let \(u\in(0,1)\) solve \(u^2(1+u)=1\). The multiset of zero-hub weights has generating function \(1+3u^2+u^3\). Markov's inequality applied to \(u^S\) bounds the number of choices failing \(S>3r/2\) by \(\beta^r\). For the one-hub total \(S'\), the complementary total \(3r-S'\) has the same one-triangle weight multiset \(\{0,2,2,2,3\}\); applying the same bound excludes at most another \(\beta^r\). Because \(u\) minimizes \((1+3u^2+u^3)u^{-3/2}\), and this quantity at \(u=1\) equals five, \(\beta<5\). This proves the two-sided exponential estimate and the claimed asymptotic. The periodic-state fraction follows from \((P_1(r)+2C_2(r))/2^{3r+1}\sim(5/8)^r\).

## Verification
Run `python3 windmill_majority_verify.py` from a directory containing the supplied standalone file. It evaluates the majority rule directly from graph adjacency and independently from the local sector table; every one of the \(2^{3r+1}\) states for \(1\le r\le5\) is enumerated for fixed points, primitive two-cycles and maximal preperiod. It further checks explicit witnesses through \(r=16\), and evaluates the exact formula at larger sizes. Recorded results include \((P_1,C_2,T_{\max})=(2,3,1),(6,9,3),(8,45,4),(22,189,4),(32,1683,4)\) for \(r=1,2,3,4,5\). Finite enumeration is not used in place of the infinite-family argument.

## Relationship to prior work
Goles and Olivos (1980) established eventual periods at most two for symmetric threshold networks, which already covers the general *period bound* but not the sharp four-update bound or the exact attractor census. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014, arXiv:1405.2486) examine convergence and disagreement for majority updates on unimodular and random graphs. Kaaser, Mallmann-Trenn and Natale (2015, arXiv:1508.03519) give general voting-time bounds and module arguments. Goles and Ruz (online 2014) characterize attractors and threshold-graph structural conditions broadly. The inspected sources do not give the stated clique-windmill fixed/primitive-two-cycle formulas, exponential five-base law, or sharp all-size preperiod classification. These are specialized exact statements, not a new proof of the established general period-two theorem.

## Limitations
The finding concerns only identical synchronous strict-majority rules on a shared-hub family with triangle modules. It does not classify arbitrary block-graph or general threshold networks, heterogeneous thresholds, asynchronous updates, or basins of individual cycles. A 1980 primary paper relevant to the generic period-two theorem was accessible through citations and abstract, not through its full text; unindexed exact enumerations could exist. The specified independent audit has not been performed. Computations for finite \(r\) supplement the symbolic proof but cannot certify it for all \(r\).

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: https://doi.org/10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (2014-05-11), https://arxiv.org/abs/1405.2486.
3. E. Goles and G. A. Ruz, *Dynamics of neural networks over undirected graphs*, Neural Networks 63 (2015), 156–169; online 2014-12-12, https://doi.org/10.1016/j.neunet.2014.10.013. Author-hosted PDF: https://capes.cl/wp-content/uploads/2014/09/Goles-Ruz_2015.pdf.
4. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1 (2015-08-14), https://arxiv.org/abs/1508.03519.

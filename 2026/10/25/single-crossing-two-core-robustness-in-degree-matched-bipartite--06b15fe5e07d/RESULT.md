# Single-crossing two-core robustness in degree-matched bipartite ecological networks

## Finding

Consider the connected *two-cycle bouquet* \(B_{a,b}\), obtained by identifying one vertex of a simple cycle of even length \(a\) with one vertex of a disjoint simple cycle of even length \(b\). Assume \(4\leq a\leq b\). This is a simple bipartite graph with \(n=a+b-1\) vertices. Designate the common vertex as belonging to the first guild. Each vertex initially survives independently with probability \(p\in(0,1)\). Starting from the induced graph of initial survivors, repeatedly remove every vertex having fewer than two currently surviving neighbors. Let \(X_{a,b}(p)\) be the number of vertices in the final \(2\)-core, and let \(U_{a,b}(p)=\Pr[X_{a,b}(p)>0]\) and \(M_{a,b}(p)=\mathbb E[X_{a,b}(p)]\).

**Theorem (distribution and unique balancing crossover).** The complete probability generating function is

\[
\begin{aligned}
\mathbb E[z^{X_{a,b}}]={}&1-p^a-p^b+p^{a+b-1}\\
&+(p^a-p^{a+b-1})z^a\\
&+(p^b-p^{a+b-1})z^b\\
&+p^{a+b-1}z^{a+b-1}.
\end{aligned}
\]

In particular the possible final sizes are \(0,a,b,a+b-1\), with the two terms of exponent \(a=b\) combined whenever the cycle lengths coincide. This formula includes every probability, not just the first two moments.

Consequently,

\[
U_{a,b}(p)=p^a+p^b-p^{a+b-1},\qquad
M_{a,b}(p)=a p^a+b p^b-p^{a+b-1}.
\]

For every even \(a,b\) satisfying \(4\leq a\) and \(b\geq a+4\), compare the more unequal bouquet \(B_{a,b}\) with the balancing transfer \(B_{a+2,b-2}\). These graphs have identical numbers of vertices and edges and identical degree multisets **within each bipartite guild**. Nevertheless,

\[
U_{a,b}(p)-U_{a+2,b-2}(p)
=(1-p^2)(p^a-p^{b-2})>0
\quad(0<p<1).
\]

There is exactly one \(p_*\in(0,1)\) such that

\[
\begin{cases}
M_{a,b}(p)>M_{a+2,b-2}(p),&0<p<p_*,\\
M_{a,b}(p)=M_{a+2,b-2}(p),&p=p_*,\\
M_{a,b}(p)<M_{a+2,b-2}(p),&p_*<p<1.
\end{cases}
\]

Thus, making the two cycle lengths more unequal strictly improves the chance that *some* core survives at every nontrivial retention probability, but improves the *expected number* of surviving core vertices only below one sharp retention threshold.

**Smallest matched-degree example in this family.** Two nonisomorphic bipartite two-cycle bouquets with the same vertex count first occur at \(n=11\), namely \(B_{4,8}\) and \(B_{6,6}\). Each has five vertices in the first guild with degrees \((4,2,2,2,2)\), and six vertices of degree \(2\) in the second guild. For every \(0<p<1\),

\[
U_{4,8}-U_{6,6}=p^4(1-p^2)^2>0,
\]

while

\[
M_{4,8}-M_{6,6}=4p^4(1-p^2)(1-2p^2).
\]

The expected-size ranking reverses exactly at \(p_*=1/\sqrt 2\). The 11-vertex minimality is **within bipartite two-cycle bouquets**, not among all bipartite interaction networks.

## Assumptions and scope

The graph is simple, undirected, bipartite, and consists of exactly two even cycles with precisely one shared vertex; the common vertex is assigned to the first guild. Initial vertex retention indicators are independent with common probability \(p\); no new links form after deletion. The secondary-loss rule is deterministic degree-at-least-two pruning, applied until stable. Species counted in \(X\) are precisely vertices of this graph-theoretic \(2\)-core; this stylized criterion is not an assertion that every real species biologically requires two partners. Endpoints \(p=0,1\) are excluded from strict inequalities, since the relevant comparisons then tie.

## Proof

**1. Identify the final core.** Each initial cycle whose every vertex survives is a subgraph of minimum degree two and therefore lies entirely in the final \(2\)-core. Conversely, suppose one of the two original cycles is broken by initial removal of at least one of its vertices. Its surviving edges form disjoint paths, possibly including the common vertex. Every such path not already part of the other intact cycle can be pruned starting at its leaf ends. If neither original cycle is intact, the surviving graph contains no cycle and its \(2\)-core is empty. Therefore the final core is exactly the union of the original cycles that survive intact. This argument depends on the shared-vertex bouquet structure; it is not asserted for arbitrary cactus graphs with bridge paths joining cycles.

**2. Recover the full distribution.** Let \(A\) and \(B\) be the events that all vertices of the length-\(a\) and length-\(b\) cycles, respectively, survive initial deletion. By independence,

\[
\Pr(A)=p^a,\qquad \Pr(B)=p^b,\qquad
\Pr(A\cap B)=p^{a+b-1},
\]

because the cycles share precisely one vertex. If neither event occurs, \(X=0\); if exactly one occurs, \(X=a\) or \(X=b\); if both occur, the common vertex is counted only once and \(X=a+b-1\). Inclusion–exclusion proves the displayed distribution and its expectation and nonempty-core probability.

**3. Compare a two-vertex balancing transfer.** The guild-degree multisets depend on \(a+b\), not on the individual cycle lengths: the first guild has one degree-four vertex and \((a+b)/2-2\) degree-two vertices, while the second guild has \((a+b)/2\) degree-two vertices. Both families therefore have matched guild populations and matched degree multisets. Because \(a+b\) is unchanged, the intersection correction \(p^{a+b-1}\) cancels from both objective differences. Direct factorization gives

\[
\begin{aligned}
U_{a,b}-U_{a+2,b-2}
&=p^a+p^b-p^{a+2}-p^{b-2}\\
&=(1-p^2)(p^a-p^{b-2})>0.
\end{aligned}
\]

The strict inequality uses \(b-2>a\) and \(0<p<1\).

**4. Prove exactly one mean crossover.** Put \(A_0=a/2\), \(B_0=b/2\), \(t=p^2\), and \(k=B_0-A_0-1\geq1\). Then

\[
M_{a,b}-M_{a+2,b-2}=2t^{A_0}H(t),
\quad H(t)=A_0-(A_0+1)t-(B_0-1)t^k+B_0t^{k+1}.
\]

For \(k=1\), \(H(t)=(1-t)[A_0-(A_0+2)t]\), which has exactly one zero in \((0,1)\), at \(t=A_0/(A_0+2)\), positive before and negative after. For \(k\geq2\), the nonzero coefficient signs of \(H\), in ascending exponent order, are \(+,-,-,+\), so Descartes' rule of signs gives at most two positive roots counting multiplicities. One root is \(t=1\); it is simple, since \(H'(1)=2k>0\). Moreover \(H(0)=A_0>0\) and \(H(t)<0\) immediately to the left of \(1\). The intermediate value theorem forces a root in \((0,1)\); Descartes' bound implies this is the only other positive root and is simple. Its sign changes from positive to negative. Since \(p\mapsto p^2\) increases strictly on \((0,1)\), the unique threshold and asserted ordering follow.

**5. Verify the first possible equal-degree pair.** The two even cycle lengths are at least four, and \(n=a+b-1\) is odd. For sums \(a+b=8\) and \(10\), the only unordered admissible pairs are \((4,4)\) and \((4,6)\), respectively. At sum \(12\), two unequal cycle-length multisets exist: \((4,8)\) and \((6,6)\). Hence \(n=11\) is the first possible same-size nonisomorphic pair in the specified family. Substitution into the formulas yields the exact expressions above and \(p_*=1/\sqrt2\). This completes the proof.

## Verification

The supplied standard-library program `verify.py` independently constructs the bipartite graphs, enumerates every initial vertex-retention subset, prunes the induced graph by its actual current degrees, and compares the resulting distribution with all Bernstein-basis coefficients of the closed-form law. It checks nine graph configurations, involving 119,424 initial-retention subsets, including the 11-vertex comparison and all graph sizes through 15 vertices among the listed configurations. It separately verifies exact factor identities and strict inequalities at rational values. Run `python3 verify.py` and compare its output to `certificate.txt`. This is computational evidence for the finite examples, not a substitute for the general proof in Steps 1–4.

## Relationship to prior work

Secondary coextinction in ecological networks and the value of adaptive rewiring were studied by Staniczenko and coauthors (2010). James, Pitchford and Plank (2012) examined network architecture and individual species persistence. Vieira and Almeida-Neto (2015, first public 2014) developed a stochastic model of complex coextinctions. The most directly related **topological mechanism** is the \(k\)-core pruning applied to ecological networks by Morone, Del Ferraro and Makse (preprint 2018); its accessible full text discusses \(2\)-core extraction, nonlinear mutualistic response, and collapse thresholds. None of these inspected statements provides the present site-percolation law for two-cycle bouquets, the all-parameter unique mean crossover under guild-degree preservation, or the first 11-vertex example. The proof is self-contained and deliberately claims only that precisely delimited extension, not the novelty of \(k\)-cores, site percolation, or secondary-extinction modeling.

## Limitations

The result is exact for uniform independent primary deletion followed by deterministic \(2\)-core pruning. It does not cover heterogeneous or correlated primary extinctions, threshold-one survival, variable partner requirements, obligate directional trophic dependencies, time-evolving interaction weights, new partner formation, or the abundance dynamics in published ecological models. There is no claim that the 11-vertex pair is minimal outside the bipartite two-cycle bouquet class. Related generic graph reliability identities or a differently indexed prior cycle-optimization theorem may already subsume this calculation; an independent bibliographic audit has not been performed.

## References

1. Staniczenko, P. P. A., Lewis, O. T., Jones, N. S., and Reed-Tsochas, F. (2010), *Structural dynamics and robustness of food webs*, Ecology Letters 13, 891–899. DOI:10.1111/j.1461-0248.2010.01485.x. First public online date: 2010-06-14.
2. James, A., Pitchford, J. W., and Plank, M. J. (2012), *Disentangling nestedness from models of ecological complexity*, Nature 487, 227–230. DOI:10.1038/nature11214. Public date: 2012-06-20.
3. Vieira, M. C., and Almeida-Neto, M. (2015), *A simple stochastic model for complex coextinctions in mutualistic networks: robustness decreases with connectance*, Ecology Letters 18, 144–152. DOI:10.1111/ele.12394. First public online date: 2014-11-28.
4. Morone, F., Del Ferraro, G., and Makse, H. A., *The k-core as a predictor of structural collapse in mutualistic ecosystems*, arXiv:1811.00141v1, first posted 2018-10-31. Full text: https://arxiv.org/html/1811.00141v1.

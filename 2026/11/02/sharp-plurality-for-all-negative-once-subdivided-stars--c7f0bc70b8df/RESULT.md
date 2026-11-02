# Sharp plurality for all-negative once-subdivided stars

## Finding
Let \(T_m\) be the tree obtained by subdividing every edge of the star \(K_{1,m}\) exactly once, with center \(c\), intermediate vertices \(a_1,\ldots,a_m\), and leaves \(b_1,\ldots,b_m\). Thus the edges are precisely \(ca_i\) and \(a_i b_i\), for \(1\le i\le m\). Give every edge sign \(-1\), and let \(\Gamma_m^-\) denote this signed graph. In the two-color signed-burning process of Fallat, Gupta, Khodamoradi, and Zilles (2026), every round first spreads existing fire to unburned vertices by the strict sign-adjusted majority rule and then ignites one still-unburned vertex, if any, in a chosen color. A burned vertex never changes color. The plurality \(Y(\Gamma)\) is the maximum number of vertices of one color attainable upon complete burning, optimized over all legal ignition schedules.

**Theorem.** For every integer \(m\ge3\),
\[
Y(\Gamma_m^-)=m+2=\frac{|V(T_m)|+3}{2}.
\]
In fact, in every attainable final coloring, if the center is yellow, no arm has both its vertices yellow; if the center is green, at most two arms have both vertices yellow. The latter bound is sharp simultaneously for all \(m\ge3\).

The path boundaries \(m=1,2\) have plurality \(2,3\), respectively, by the known exact all-negative-path result and independently by exhaustive simulation; they are not included in the displayed infinite theorem.

## Assumptions and scope
All graphs are finite and simple. Yellow and green are represented by \(+1\) and \(-1\), and unburned by \(0\). Because every edge is negative, an unburned vertex \(v\) at the start of a round receives influence \(-\sum_{u\sim v}\nu(u)\), where \(\nu\) is the coloring at the end of the previous round. It takes the sign of that influence when nonzero and otherwise remains unburned. After simultaneous spreading, the player must ignite one unburned vertex if there is one. The initial configuration is all zero. The objective optimizes over *all* completing sequences, with no fixed deadline or minimum-duration restriction. The conclusion concerns the specific all-negative signature; switching-equivalent signatures need not have the same plurality.

## Proof
We prove an upper bound for yellow; global color reversal then makes it the plurality bound. Fix a legal completed process, and write \(t_v\) for the first round in which \(v\) becomes burned. Every \(t_v\) is finite, because the process completes. Each vertex retains its final color thereafter. A leaf \(b_i\) of final color yellow whose intermediate neighbor \(a_i\) is also yellow must have been *ignited* yellow: spreading from a yellow intermediate vertex across the negative edge can give that leaf only green. Moreover, the intermediate vertex cannot burn before the leaf: if it did, the leaf would become green at the next spread step, before it could be ignited in that round; both cannot be ignited in one round.

First suppose \(c\) ends yellow. If an arm were entirely yellow, then \(b_i\) would be ignited before \(a_i\) burned. At the very next spread step, \(a_i\) would receive negative influence from \(b_i\), and any influence from the center (if already burned) would also be negative. Thus it would become green before any subsequent ignition, a contradiction. So when \(c\) is yellow, each arm contains at most one yellow vertex, giving at most \(m+1\) yellows in all.

Now suppose \(c\) ends green, first burning at round \(t_c\). Consider an arm whose two vertices end yellow. The leaf \(b_i\) was ignited yellow at round \(t_b\), and the intermediate vertex \(a_i\) must burn later at round \(t_a>t_b\) if it is ignited. There are two cases.

**Case 1: \(a_i\) was ignited yellow.** For \(a_i\) to remain unburned through the spread step at round \(t_b+1\), its yellow leaf neighbor must be balanced by an already green center: thus \(t_c\le t_b\). If \(t_c<t_b\), then at round \(t_c+1\), before its leaf has burned, \(a_i\) would receive positive influence from the green center and burn yellow by spreading. This contradicts its later ignition. Hence \(t_b=t_c\). As the process ignites at most one vertex per round, at most one doubly-yellow arm can be of this type.

**Case 2: \(a_i\) burned yellow by spreading.** With a green center and a yellow leaf, the only already-burned neighbor that can produce positive influence at \(a_i\) is the center, and the leaf must still be unburned at the preceding round. Therefore \(t_a=t_c+1\): otherwise the unburned intermediate vertex would already burn yellow at the first spread following the center's burning. Its leaf must be ignited at the end of that same round \(t_a\), since leaving it unburned until the next round would make it green by spreading from the yellow intermediate vertex. Hence \(t_b=t_c+1\). At most one doubly-yellow arm can be of this type, since only one ignition is permitted in that round.

Thus, when \(c\) is green, at most two arms are doubly yellow. Each remaining arm contributes at most one yellow vertex, so the final number of yellow vertices is at most \(2\cdot2+(m-2)=m+2\). Together with the center-yellow bound, \(Y(\Gamma_m^-)\le m+2\).

For sharpness, choose three distinct arms, numbered \(1,2,3\). In round \(1\), ignite \(a_1\) yellow. In round \(2\), spreading burns \(c\) and \(b_1\) green; ignite \(b_2\) yellow. In round \(3\), the two contributions to \(a_2\) cancel, while every \(a_j\) with \(j\ge3\) burns yellow from \(c\); ignite \(b_3\) yellow. In round \(4\), all remaining leaves \(b_j\) with \(j\ge4\) burn green, while \(a_2\) remains unburned because its two burned neighbors have opposite colors; ignite \(a_2\) yellow. This is legal and completes all vertices. The yellow vertices are \(a_1,a_2,b_2,a_3,b_3,a_4,\ldots,a_m\), exactly \(m+2\) of them. Consequently equality holds for every \(m\ge3\). \(\square\)

## Verification
The included independent standard-library program `verify.py` implements the original signed-graph neighbor-influence rule on the original labelled vertices. It exhaustively traverses every reachable partial configuration and legal ignition for \(1\le m\le6\), comparing the maximum yellow count with the formula (with path exceptions), and separately performs arm-permutation-orbit enumeration for \(3\le m\le60\). It also executes the displayed four-round witness for each of those \(58\) branching orders. The actual run ended `VERIFY_OK`; the final claimed infinity is certified by the preceding proof, not by these finite experiments. Reproduce with `python3 verify.py` in a directory containing that file; no third-party packages are needed.

## Relationship to prior work
Fallat, Gupta, Khodamoradi, and Zilles, *Burning Signed Graphs*, first posted on 2026-10-01 (arXiv:2610.02506), introduce the signed-burning plurality and prove exact values or bounds for signed paths, including the all-negative path. Their Sections 2 and 3 develop the process and path bounds, while Section 5 explicitly identifies signed trees as a natural next problem. This theorem treats an infinite nonpath family, and the proof uses a different timing obstruction caused by a high-degree center. It does not follow by applying the path formula independently to arms: the ignition choices are shared across the arms and the center contributes to their signed majorities. Relevant searches for signed-burning plurality on spiders, subdivided stars, and competing two-color fires did not identify an earlier formula; this is best-knowledge rather than certified historical priority.

## Limitations
The result requires exactly two edges per arm and every edge negative, with \(m\ge3\). It does not give plurality for arbitrary signatures, unequal arm lengths, or arbitrary trees. It does not classify every optimal ignition schedule or count them. External historical priority and the proof have not received independent assessment. Experimental checks cover finite \(m\) only.

## References
1. S. Fallat, H. Gupta, K. Khodamoradi, and S. Zilles, *Burning Signed Graphs*, arXiv:2610.02506, first publicly posted 2026-10-01. https://arxiv.org/abs/2610.02506 . Accessible full extracted text at https://www.paperpeel.com/paper/2610.02506 (Sections 2, 3, 5 inspected).

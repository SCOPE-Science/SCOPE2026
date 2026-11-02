# Critical nonstackable pebble configurations on the five- and seven-cycles

## Finding
For the labelled simple cycle \(C_n\) with vertices \(0,1,\ldots,n-1\) in cyclic order, a configuration is a vector \(c=(c_0,\ldots,c_{n-1})\) of nonnegative integers. A legal pebbling move removes two pebbles from one vertex and adds one at an adjacent vertex. A configuration is *stackable* if finitely many such moves leave all surviving pebbles at one vertex. A critical obstruction is a nonstackable configuration of size \(\operatorname{stack}(C_n)-1\), where \(\operatorname{stack}\) is the least integer \(t\ge2\) for which every size-\(t\) configuration is stackable.

The complete critical-obstruction classifications for the first two odd cycles beyond the triangle are:

* On \(C_5\), \(\operatorname{stack}(C_5)=8\), and the **ten** critical configurations (seven pebbles) are exactly the two disjoint dihedral orbits of \((5,0,1,1,0)\) and \((3,3,0,1,0)\). Each orbit has five labelled members.
* On \(C_7\), \(\operatorname{stack}(C_7)=17\), and the **fourteen** critical configurations (sixteen pebbles) are exactly the single dihedral orbit of \((14,0,1,0,1,0,0)\). This orbit has fourteen labelled members.

Here the dihedral group acts by rotating or reversing the vertex coordinates. An *almost stacked* configuration has at most one vertex with more than one pebble. Accordingly, every critical obstruction on \(C_7\) is almost stacked, but exactly one of the two critical orbits on \(C_5\) is almost stacked. In particular, the proposed stronger statement that **every** maximum-size nonstackable configuration must be almost stacked is false already for \(C_5\). This does not refute the Almost Stacked Hypothesis, which only asserts that testing almost-stacked configurations suffices to determine a threshold.

## Assumptions and scope
Graphs are simple, undirected, unweighted, and vertex-labelled in cyclic order. Only \(n\in\{5,7\}\) is asserted. Pebble counts are unbounded nonnegative integers, and a move always consumes one pebble in total. The target of stacking is not prescribed. A configuration with no pebbles is not deemed stacked. All symmetry counts concern labelled configurations, not graphs modulo vertex relabelling.

## Proof
Let \(\mathcal C_t(n)=\{c\in\mathbb N^n:\sum_i c_i=t\}\), which has \(\binom{t+n-1}{n-1}\) members. Let \(\mathcal G_t(n)\) be the subset of stackable configurations and \(\mathcal S_t(n)\) the \(n\) single-support configurations of size \(t\). Define the *parent* of a configuration \(d\in\mathcal C_{t-1}(n)\) relative to an oriented cycle edge \(u\to v\) by
\[
P_{u,v}(d)=d+2e_u-e_v\quad\text{provided }d_v\ge1.
\]
This is a nonnegative size-\(t\) configuration having a legal first move \(u\to v\) that yields \(d\). Conversely, **every** legal move from a size-\(t\) configuration is of this form, because a move decreases the total count by exactly one.

Therefore the following recurrence is exact, with no heuristic pruning:
\[
\mathcal G_1(n)=\mathcal S_1(n),\qquad
\mathcal G_t(n)=\mathcal S_t(n)\cup
\bigcup_{d\in\mathcal G_{t-1}(n)}
\{P_{u,v}(d):u\to v\text{ is an oriented cycle edge},\ d_v\ge1\},\quad t\ge2.
\]
Indeed, any successful nonstacked configuration must make a first move into a successful configuration of size one less. This proves the recurrence by induction on \(t\), while the converse follows by prepending the legal parent move.

The accompanying completely specified exact-arithmetic verifier enumerates every weak composition, computes the above recurrence up to \(t=8\) for \(C_5\) and \(t=17\) for \(C_7\), and forms \(\mathcal C_t(n)\setminus\mathcal G_t(n)\). An independent memoized **forward** recursion checks every individual configuration by all legal first moves. The two independent formulations agree at each size, not merely at the reported boundary. For \(C_5\), the counts of nonstackable configurations at \(t=1,\ldots,8\) are
\[
(0,10,20,35,41,35,10,0).
\]
For \(C_7\), the counts at \(t=1,\ldots,17\) are
\[
(0,21,63,161,343,644,1030,1407,1491,1197,770,448,245,126,56,14,0).
\]
The exact endpoint sets equal the listed disjoint unions of dihedral orbits (five plus five and fourteen, respectively). The verifier tests set equality, not just equal cardinalities. Since every size-\(8\) configuration on \(C_5\) and every size-\(17\) configuration on \(C_7\) is stackable, while the preceding sizes have the displayed obstructions, the threshold values follow without assuming numerical values from the literature.

The first \(C_5\) representative has a single pile of five; the second has two piles of three, so the latter is not almost stacked. The \(C_7\) representative has just one pile exceeding one, and dihedral symmetries preserve that property. This proves the final structural distinction.

## Verification
Run `python verify_cycle_stacking.py` using Python 3 and the standard library only. It systematically generates all \(\binom{22}{6}=74613\) size-sixteen configurations on \(C_7\), all \(\binom{23}{6}=100947\) size-seventeen configurations, and all smaller compositions needed by the induction. The script verifies both forward and reverse exact reachability, the entire nonstackable-count profiles, exact orbit equality and orbit sizes, and the zero-obstruction threshold layers. Computational proof applies only to the specified finite graphs; it is not an induction on graph order.

## Relationship to prior work
Csernák and Soukup introduced the stacking number, documented a general exact search recurrence, and **already reported** the numerical values \(\operatorname{stack}(C_5)=8\) and \(\operatorname{stack}(C_7)=17\). Those threshold values, and the general search method, are not claimed as new. Their public computational report gives the same threshold table. Their subsequent Almost Stacked Hypothesis work verifies the existential threshold assertion for connected graphs up to seven vertices. Neither examined primary paper nor the inspected public report states the exact critical-obstruction **orbit classifications**, the two-versus-one orbit distinction, or the boundary separating the existential and universal interpretations. The published code can generate witness sets, however, so independent historical priority for this explicit structural classification deserves further checking.

## Limitations
This is a complete **finite** classification for exactly two cycles, not an infinite odd-cycle theorem. The original papers' threshold values and algorithms are prior art. Unexamined alternative presentations or executable supplementary outputs may already encode the same orbit structure; independent audit and comprehensive priority checking have not occurred. The result does not establish the Almost Stacked Hypothesis for larger graphs or say that all nonstackable configurations (as opposed to the critical layer) are almost stacked.

## References
1. T. Csernák and L. Soukup, *Stacking and Clearing in Graph Pebbling*, arXiv:2604.22341v1, first publicly posted 2026-04-24. https://arxiv.org/abs/2604.22341
2. T. Csernák and L. Soukup, *The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem*, arXiv:2610.09650v1, first publicly posted 2026-10-07. https://arxiv.org/abs/2610.09650
3. L. Soukup, *Pebbling Report for Selected Graphs* and associated source `special_graph_pebbling_report.tex`, public supplementary repository: https://github.com/lajossoukup/pebbling

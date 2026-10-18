# Exact multiplicities of minimum power-dominating sets in sunlet graphs

## Finding
For the labelled sunlet graph \(S_n=C_n\circ K_1\) on \(2n\) vertices, \(n\ge3\), let \(P_n\) count the minimum power-dominating vertex sets. If \(n=3q\), then \(P_n=3\). If \(n=3q+2\), then \(P_n=3n\). If \(n=3q+1\) and \(q\ge2\), then \(P_n=n(9q+4)/2\). The exceptional value is \(P_4=22\).

More precisely, write \(P_{n,b}\) for minimum power-dominating sets with exactly \(b\) chosen pendant vertices. The complete distribution is
\[
\begin{array}{c|ccc}
n & P_{n,0}&P_{n,1}&P_{n,2}\\\hline
3q & 3&0&0\\
3q+2 & n&2n&0\\
3q+1,\ q\ge2&n(q+2)/2&n(2q+1)&2nq\\
4&6&12&4
\end{array}
\]
All remaining values of \(P_{n,b}\) vanish. The previously known cardinality of any minimum set is \(\gamma_P(S_n)=\lceil n/3\rceil\); that scalar equality is not part of the claimed novel contribution.

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. Fix \(n\ge3\), and write cycle vertices \(c_i\) and private leaves \(\ell_i\), with indices in \(\mathbb Z/n\mathbb Z\). Edges are \(c_ic_{i+1}\) and \(c_i\ell_i\). Starting from a sensor set \(A\subseteq V(S_n)\), mark the closed neighborhood \(N[A]\); repeatedly mark the unique still-unmarked neighbor of any marked vertex with exactly one unmarked neighbor. The set is power dominating when every vertex is eventually marked. Distinct labelled subsets count separately.

## Proof
**Capacity and minimum cardinality.** A selected cycle vertex initially marks its private leaf and at most three cycle vertices: itself and its two neighbors. A selected leaf initially marks its own cycle vertex and its leaf, and its cycle vertex can subsequently force at most one neighboring cycle vertex. Crucially, an unselected cycle vertex whose private leaf is initially unmarked cannot force an unmarked *cycle* vertex: its unmarked private leaf would give a second unmarked neighbor. After both cycle neighbors are marked it may force its private leaf, but can never extend monitoring along the cycle. Accordingly each cycle sensor accounts for at most three marked cycle vertices and each leaf sensor at most two. Hence a power-dominating set with \(a\) cycle sensors and \(b\) leaf sensors satisfies \(n\le3a+2b=3(a+b)-b\). Conversely a dominating set of the underlying cycle, using \(\lceil n/3\rceil\) cycle vertices, observes the entire sunlet after the private leaves are forced. Thus \(k=\lceil n/3\rceil\), and an optimum has \(0\le b\le3k-n\). Simultaneously selecting \(c_i\) and \(\ell_i\) is redundant, because \(c_i\) already initially observes \(\ell_i\), so an optimum never does so.

**Cyclic gap notation.** When \(a>0\), cyclically list its selected cycle vertices and their positive clockwise distances \(d_1,\ldots,d_a\), with \(\sum d_i=n\). An isolated gap of length \(d\ge3\) leaves exactly \(d-3\) unmarked cycle vertices after the initial observation, between the two already marked boundary neighborhoods. Distance two creates one overlap between the length-three marked blocks; distance one creates two overlaps. Once all the initially unmarked cycle vertices have been marked, every remaining private leaf is forced by its marked cycle neighbor. A leaf sensor may cover its own unmarked cycle vertex and, when the other neighboring cycle vertex is already marked, force one adjacent unmarked cycle vertex; it cannot cover unmarked cycle vertices in two separated gaps.

**Case \(n=3q\).** Capacity forces \(b=0\) and \(a=q\). All cycle-sensor marked blocks must be disjoint and cover the cycle, so every cyclic gap has length three. There are exactly three cyclic translations.

**Case \(n=3q+2\).** Now \(a+b=q+1\) and \(b\le1\). For \(b=0\), the gaps of the dominating cycle sensor set have length at most three, and their total deficit from length three is one; hence one gap has length two and the rest length three. Exactly \(n\) cycle sensor sets occur. For \(b=1\), capacity is tight: the \(q\) cycle-sensor three-blocks must be disjoint, with exactly two consecutive unmarked cycle vertices in a unique gap of length five. Its other gaps have length three. There are \(n\) cycle-sensor patterns; in the exceptional gap, either of the two unmarked cycle positions may carry the leaf sensor, which then forces the other. This gives \(2n\) sets.

**Case \(n=3q+1\): no leaf sensor.** There are \(q+1\) cycle sensors. All gaps are at most three, and the deficiency from all-three gaps is two. Either one gap has length one or two gaps have length two; the other gaps have length three. For \(a=q+1\) selected sensors, cyclic starts count each set exactly \(a\) times; the number is \(n/a\,[a+\binom a2]=n(q+2)/2\).

**Case \(n=3q+1\): one leaf sensor.** There are \(q\) cycle sensors, whose initial three-blocks have at most one total overlap, because the single leaf sensor can add at most two cycle vertices while \(n=3q+1\). If there is no overlap, the gaps are one length four and \(q-1\) lengths three. There are \(n\) patterns. The sole unmarked cycle vertex may be covered by selecting its own leaf, or by selecting the leaf belonging to either adjacent initially marked cycle vertex; the latter forces the missing cycle vertex. These give \(3n\) solutions. If there is exactly one overlapping vertex, one gap is length two, and two unmarked cycle vertices remain. They must be consecutive to be covered by the single leaf sensor, so there is one gap of length five; all remaining gaps are three. The alternative of two separated gaps of length four cannot work. For \(q\ge2\) these patterns number \(n(q-1)\); either missing vertex may carry the leaf sensor, yielding \(2n(q-1)\). In total this case has \(n(2q+1)\) solutions. At \(q=1\) only the first type occurs, yielding \(12\) sets for \(n=4\).

**Case \(n=3q+1\): two leaf sensors.** Let \(q\ge2\). There are \(a=q-1\) cycle sensors. Capacity is tight; their three-blocks are disjoint and the exactly four remaining unmarked cycle vertices must be covered two at a time by the two leaf sensors. Thus either one gap has four consecutive unmarked cycle vertices (a gap of length seven), or two gaps have two consecutive unmarked cycle vertices each (two gaps of length five); all other gaps have length three. In a single four-vertex run, there are exactly four successful unordered pairs of private-leaf sensors: choose one from the first two and one from the last two positions. Each two-vertex run has exactly two possible leaf sensors, giving four choices for a pair of runs. The number of core-sensor patterns of the first type is \(n\); of the second, \(n\binom{q-1}{2}/(q-1)=n(q-2)/2\). The count is therefore \(4n+4n(q-2)/2=2nq\). For \(n=4\), two sensors on private leaves and no cycle sensors succeed precisely when their indices are adjacent on the four-cycle, giving four sets.

Adding the disjoint cases proves every displayed count and the absence of any other minimum sets. The number of cycle-sensor patterns in a specified gap multiset is \(n/a\) times the number of cyclic gap sequences indexed by a distinguished selected vertex: every sensor set is counted once for each of its \(a\) possible distinguished vertices.

## Verification
Run \(`python3 verify.py`\) using Python 3 and the standard library. It enumerates all candidate vertex subsets of optimum cardinality for each \(3\le n\le13\), simulating initial closed-neighborhood observation and all available single-neighbor forcing steps directly. It separately excludes any lower-cardinality successful set for \(3\le n\le8\). The recorded run checked \(90,728\) distinct subsets and agreed with the predicted counts by number of pendant sensors. This finite verification is not a proof for unbounded \(n\); the preceding structural argument is.

## Relationship to prior work
Saibavani and Parvathi (published online 11 December 2019) proved the scalar formula \(\gamma_P(S_n)=\lceil n/3\rceil\) in their Theorem 3.1, as part of a study of the sunlet, its line graph, middle graph and total graph. Its accessible manuscript's theorem and proof concern minimum cardinality rather than the multiplicities or leaf/cycle sensor profile established here. The original power domination framework was developed by Haynes, Hedetniemi, Hedetniemi and Henning. Literature on power-domination polynomials of book graphs and spider trees concerns distinct graph families and does not imply these sunlet optimal-solution counts.

## Limitations
This is an enumeration only of minimum-cardinality power-dominating sets; it does not count all (nonminimum) power-dominating sets, determine reconfiguration geometry, or address other sunlet variants. The formulas require \(n\ge3\); the exceptional \(n=4\) term is essential. An independently conducted comprehensive priority audit has not been performed; equivalent formulations in unindexed papers remain a possible bibliographic risk.

## References
1. T. N. Saibavani and N. Parvathi, *Power domination number of sunlet graph and other graphs*, Journal of Discrete Mathematical Sciences and Cryptography **22** (2019), 1121–1127. DOI: 10.1080/09720529.2019.1689610. Publisher issue lists publication online 11 December 2019.
2. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi and M. A. Henning, *Domination in graphs applied to electric power networks*, SIAM Journal on Discrete Mathematics **15** (2002), 519–529. DOI: 10.1137/S0895480100375831.

# Ternary digram-presence spectra: 328 supports, lossless traversal, and exact stabilization

## Finding
Let \(\Sigma=\{0,1,2\}\) and let \(S_2(w)=\{w_iw_{i+1}:1\le i<|w|\}\), the **set**, rather than multiset, of adjacent pairs of a nonempty finite word. There are exactly **328** realizable subsets of \(\Sigma^2\), out of \(2^9=512\) candidates. Their edge-count generating polynomial is
\[
P(z)=1+9z+21z^2+44z^3+72z^4+81z^5+60z^6+30z^7+9z^8+z^9.
\]
Every realizable support \(E\) has a shortest realizing word of length \(|E|+1\); in particular, every distinct digram is traversed exactly once. Exactly **13** realizable supports occur at only one word length: the empty set, the six singleton nonloop digrams, and the six two-digram directed paths on three distinct letters. Every other support, numbering **315**, can be realized by a word of **every** length \(n\ge |E|+1\). Consequently, for every \(n\ge10\) there are exactly **315** digram-presence profiles of ternary words of length \(n\), and the threshold \(10\) is sharp for simultaneous realization of every cyclic feasible profile.

The lossless-traversal assertion is best possible with respect to alphabet size: for the four-letter word `02103101`, there are only six distinct digrams, but the shortest realization of its digram set has eight letters rather than seven.

## Assumptions and scope
The alphabet consists of **labeled** symbols. Words are nonempty and linear, not circular. A digram occurs when two consecutive positions carry its two symbols; repeated appearances have no extra weight. A support set may be empty, realized by any one-letter word. When counting supports, words of different lengths with the same support count once. The stabilization statement concerns fixed, exact word length; a singleton finite support cannot be used to pad an existing realization without introducing a new digram.

For any alphabet size \(q\), associate with a support \(E\subseteq\Sigma^2\) the loop-allowed simple directed graph \(G_E\), with one directed edge \(a\to b\) per digram \(ab\), discarding isolated vertices. Realization of \(E\) is equivalent to a directed walk traversing every edge of \(G_E\) at least once and no unlisted edge. This is the standard de Bruijn graph correspondence for length-two factors, not a new identification.

## Proof
**1. Traversability and strong components.** For nonempty \(E\), a covering walk visits its strongly connected components in a linear order and cannot return to one after leaving: returning would place the two components on a directed cycle, contrary to maximal strong connectivity. All edges between distinct components must therefore be precisely the single edges between successive components on that order; an additional such edge cannot also be covered without revisiting a component. Hence the component condensation is a directed path with exactly one edge between each successive pair. Conversely, if the condensation has this form, traverse each strongly connected component from its fixed entry to its fixed exit while visiting every internal edge at least once, and use the successive connecting edges. Such internal covering walks exist because strongly connected directed graphs admit a directed path between every ordered pair of vertices. Thus the condition characterizes realizable nonempty supports for all alphabet sizes.

**2. Every feasible ternary support has an edge-simple realization.** Consider the at most three active vertices. A strongly connected component of size one has only optional loops; its internal in/out imbalance is zero. A component of size two must have both directed cross-edges, and again its internal imbalance is zero, regardless of loops. A strong component of size three has at least one incoming and outgoing **nonloop** edge at each vertex. With only two other vertices, the difference \(\deg^+(v)-\deg^-(v)\) is in \(\{-1,0,1\}\). The three differences add to zero, hence they are all zero or consist of one \(+1\), one \(-1\), and one zero. Its edges therefore admit a directed Eulerian trail by the standard directed Euler criterion (weak connectivity plus this imbalance condition). For a feasible graph with multiple components, there can be at most one two-vertex component; its internal edges are balanced. The intercomponent edges form a single directed path, contributing imbalance \(+1\) only at the source and \(-1\) only at the sink of the full graph (intermediate component entries and exits cancel). Therefore the complete graph has the Euler-trail imbalance condition and is weakly connected. It has an Euler trail using every distinct edge exactly once. Any realization of \(m=|E|\) different digrams needs at least \(m\) transitions, and this trail attains \(m\). The empty support is realized at length one.

**3. Exact labeled enumeration.** Count nonempty edge supports according to the number of active vertices (vertices incident to at least one edge, loops included). For one active vertex there are \(3z\) supports. With two active vertices, either direction of the sole cross-edge is chosen, or both are chosen; the two possible loops are independent. Choosing the vertex pair gives
\[
3(2z+z^2)(1+z)^2.
\]
For three active vertices, the strongly connected off-diagonal directed graphs are counted by
\[
2z^3+9z^4+6z^5+z^6.
\]
This is a direct classification of the \(2^6=64\) labeled loopless directed graphs on three vertices: two oriented 3-cycles with three edges, nine strong graphs with four, six with five, and the complete six-edge graph. Every such graph permits any selection of the three loops. If the condensation has two components, its sizes are two and one: three choices for the two-vertex component, whose cross-arcs must both occur, and four choices for the unique intercomponent arc (two directions times either of the two vertices), giving \(12z^3(1+z)^3\). If the condensation has three singleton components, it is a directed path on the three vertices, with \(3!=6\) label orders, giving \(6z^2(1+z)^3\). The zero-edge support contributes one. Summing,
\[
P(z)=1+3z+3(2z+z^2)(1+z)^2
 +(2z^3+9z^4+6z^5+z^6+12z^3+6z^2)(1+z)^3.
\]
Expansion gives the displayed polynomial and \(P(1)=328\).

**4. Exact-length stabilization.** A feasible directed graph without a directed cycle must be a directed path without loops: an acyclic directed graph with a covering walk must use each edge exactly once, and any repeated vertex would yield a cycle. With at most three labeled vertices, these are the empty support (one), the single nonloop arc (six), and the two-edge directed path on distinct symbols (six). Thus there are exactly thirteen supports with only one attainable word length, \(|E|+1\).

Every other feasible support contains a directed cycle. For a connected strong component, an Euler trail can be extended by an arbitrary number of edges at its terminal vertex, since every vertex in that component has an outgoing edge; the support remains unchanged. With two or three strong components, a directed cycle must be a loop or a reciprocal two-vertex component, as three distinct vertices cannot lie in one component when the condensation has another component. A loop in an Euler trail can be traversed an arbitrary number of additional times. If the cyclic component consists of two mutually connected vertices and the other component is a singleton without a loop, then the Euler trail either starts or ends in the cyclic component, depending on the orientation of the unique intercomponent edge. At the cyclic endpoint, extending backward or forward through the reciprocal edge pair by any number of single steps preserves the support. In the three-singleton case, any cycle is necessarily a loop. Thus every cyclic feasible support has a realization at every length \(n\ge |E|+1\). Subtracting the thirteen acyclic supports from 328 yields 315 persistent supports. Since every feasible support has at most nine edges, all persistent supports occur by \(n=10\). The complete nine-edge support cannot occur before ten letters, so this uniform threshold is sharp.

**5. The sharp four-letter obstruction.** The word `02103101` has the six distinct edges
\[
E=\{02,21,10,03,31,01\}.
\]
Their directed degree imbalances at vertices \(0,1,2,3\) are \((+2,-2,0,0)\). An Eulerian trail using each edge once would require all imbalances to be zero apart from at most one \(+1\) and one \(-1\); none exists. Hence a realizing word must have at least seven transitions, or eight letters. The displayed word realizes \(E\) in eight letters, proving the minimum exactly and establishing failure first at alphabet size four.

## Verification
A standalone Python program, `verify.py`, checks the full finite-state closure on \(3\cdot2^9\) possible (support,last-symbol) states and obtains all 328 supports. Separately, it enumerates all ternary words through length ten, verifies the support distribution, the minimum length \(|E|+1\) for every feasible support, and the 13 acyclic exceptions. It also verifies the explicit four-letter counterexample and its degree imbalances. Its exact recorded output is `verification_output.txt`. These finite tests independently check arithmetic and classifications; the all-length claims follow from the preceding graph arguments rather than from finite experiments.

## Relationship to prior work
Bernardini et al., *On Strings Having the Same Length-k Substrings*, studies precisely set-valued substring observations and a shortest-string problem via directed Eulerian **walks**, including the directed Chinese Postman connection. Its accessible full text provides the general graph framework but not the ternary two-factor 328-support enumerator, the alphabet-three edge-simple phenomenon, the 315/13 exact-length dichotomy, or the explicit four-letter boundary. A preliminary version appeared at CPM 2022, so these general framework results are not claimed as new. Celikkanat et al. (first posted 2024-11-04) analyze k-mer representations in genome learning; their representation-learning application motivates the small-alphabet support-only specialization, without asserting the present exact characterization. Gabrys and Milenkovic consider counted substring spectra, which differ from binary presence-only supports. Prior related binary adjacent-pair **multispectrum** enumerations likewise retain multiplicities and do not imply these ternary support counts.

## Limitations
The enumeration and exact-length classification are for three labeled symbols and adjacent factors of length **two**. The general graph characterization is standard and is used as a tool, not claimed as novel. The four-symbol example proves failure of lossless edge traversal in a different alphabet; it does not enumerate all four-symbol feasible supports. Publication-priority verification is not exhaustive, particularly for unindexed exact graph enumerations. No independent mathematical audit is claimed.

## References
1. G. Bernardini, A. Conte, E. Gabory, R. Grossi, G. Loukides, S. P. Pissis, G. Punzi and M. Sweering, *On Strings Having the Same Length-k Substrings*, Theory of Computing Systems 70 (2026), article 21. Preliminary conference version CPM 2022. https://doi.org/10.1007/s00224-025-10240-z
2. A. Celikkanat, A. R. Masegosa and T. D. Nielsen, *Revisiting K-mer Profile for Effective and Scalable Genome Representation Learning*, arXiv:2411.02125, first submitted 2024-11-04. https://arxiv.org/abs/2411.02125
3. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (2018). https://arxiv.org/abs/1804.04548

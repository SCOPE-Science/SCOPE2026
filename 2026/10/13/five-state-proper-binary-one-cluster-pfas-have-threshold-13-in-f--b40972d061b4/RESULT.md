# Five-state proper binary one-cluster PFAs have threshold \(13\) in five classes
## Finding
Let \(\mathcal A=(Q,\{a,b\},\delta)\) be a partial deterministic finite automaton with \(|Q|=5\). Call it proper if at least one of the ten letter-state transitions is undefined. Call it one-cluster if at least one letter is total and its functional digraph has one weak component, equivalently one directed cycle with rooted in-trees.

Among all carefully synchronizing proper binary one-cluster PFAs on five labeled states, the maximum length of a shortest carefully synchronizing word is
\[
13.
\]
Exactly \(1200\) ordered labeled transition pairs attain this maximum. Under simultaneous relabeling of the five states and exchange of \(a\) and \(b\), the \(1200\) extremizers form exactly five isomorphism classes, each of orbit size \(240\).

Writing \(\bot\) for an undefined transition and listing images of states \(0,1,2,3,4\), canonical representatives are
\[
\begin{aligned}
a&=(\bot,0,1,2,3),& b&=(2,4,3,1,3),\\
a&=(\bot,0,1,2,3),& b&=(4,4,1,2,3),\\
a&=(\bot,0,1,2,4),& b&=(2,3,4,4,1),\\
a&=(\bot,0,1,3,4),& b&=(2,3,4,4,1),\\
a&=(\bot,0,1,4,3),& b&=(2,3,4,4,1).
\end{aligned}
\]
One shortest carefully synchronizing word for the five representatives, in the same order, is respectively `bbababbabaabb`, `bababaabbaaab`, and `bbababbbababb` for each of the final three representatives.

## Assumptions and scope
For a subset \(S\subseteq Q\), a letter may act on \(S\) only when its transition is defined at every state of \(S\). A word is carefully synchronizing if every transition used from every currently possible state is defined and the final image of \(Q\) is a singleton.

The alphabet has exactly two named letters during labeled enumeration. The final classification quotients by all \(5!\) state relabelings and by the exchange of the two letters.

The claim concerns proper PFAs. If both letters are total, complete one-cluster DFAs such as the five-state Černý automaton belong to a different regime and can have larger reset threshold.

## Proof
A partial state map on five states has \(6^5=7776\) possibilities because each state may map to one of five states or to \(\bot\). Exactly \(1569\) of these maps are total and one-cluster.

The exhaustive search considers every ordered pair of partial maps for which at least one letter is total one-cluster, then removes pairs in which both letters are total. This leaves exactly
\[
14{,}594{,}838
\]
proper binary one-cluster PFAs.

For each candidate, the first verification engine performs breadth-first search in the power automaton beginning at \(Q\). From a subset it follows a letter only when the letter is defined everywhere on that subset. The first singleton reached therefore gives the exact shortest careful reset length.

A second engine constructs the same power automaton independently, reverses its defined edges, and performs a multi-source breadth-first search from all five singleton subsets. Its distance to \(Q\) must equal the forward distance. The two engines agree for every candidate.

Exactly \(8{,}206{,}270\) candidates are carefully synchronizing. Their shortest-length histogram is
\[
\begin{array}{c|rrrrrrrrrrrrr}
\ell&1&2&3&4&5&6&7&8&9&10&11&12&13\\
\hline
N_\ell&
46510&2023800&3416160&1715520&432840&276240&163440&
64320&36000&22320&4800&3120&1200.
\end{array}
\]
No candidate has threshold above \(13\).

For every one of the \(1200\) threshold-\(13\) automata, all \(5!\) simultaneous state relabelings and both letter orders are examined and the lexicographically least transition pair is taken as canonical. Exactly five canonical pairs occur. Each has an orbit of size \(240=2\cdot5!\), and the five disjoint orbits account for all \(1200\) extremizers.

## Verification
Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The program regenerates all \(7776\) partial state maps, independently checks which total maps are one-cluster, exhausts all \(14{,}594{,}838\) proper one-cluster ordered pairs, and compares forward and reverse power-automaton distances for every pair. It then checks the complete threshold histogram, the \(1200\) extremizers, the five canonical representatives, and the five orbit sizes.

## Relationship to prior work
Ruszil extends one-cluster synchronization from complete automata to PFAs, defines the one-cluster condition through a total letter whose functional graph has one cluster, proves exponential lower bounds when alphabet size is unrestricted, and proves NP-hardness of careful synchronizability even for binary one-cluster PFAs. The paper does not give a five-state binary threshold census or an equality classification.

De Bondt, Don, and Zantema exhaustively study small PFAs without the one-cluster restriction. Their published table shows that proper binary five-state PFAs realize carefully synchronizing lengths through \(15\). That result does not determine the maximum after imposing the one-cluster condition; the present census gives the strict value \(13\) and classifies all equality cases.

Targeted searches using the phrases “proper binary one-cluster PFA”, “five states”, “careful synchronization”, “threshold \(13\)”, and “equality cases” located these general sources but no published statement of the five-class census.

## Limitations
This is a finite five-state, two-letter classification. It does not give a formula for larger state sets, and it does not address one-cluster PFAs with more than two letters.

The exhaustive calculation treats all labeled transition pairs rather than only “basic” PFAs; the final isomorphism quotient removes state-label and letter-order redundancy but not other notions of presentation equivalence. Published source code or unpublished computations associated with earlier PFA censuses could in principle contain the same filtered data even though the inspected publications do not report it.

## References
1. J. Ruszil, “Careful Synchronization of One-Cluster Automata,” arXiv:2311.15020v1, first public version 2023-11-25; Developments in Language Theory 2024, pp. 252–265, DOI 10.1007/978-3-031-66159-4_18.
2. M. de Bondt, H. Don, and H. Zantema, “Lower Bounds for Synchronizing Word Lengths in Partial Automata,” arXiv:1801.10436v1, 2018; International Journal of Foundations of Computer Science 30(1), 29–60, 2019, DOI 10.1142/S0129054119400021.

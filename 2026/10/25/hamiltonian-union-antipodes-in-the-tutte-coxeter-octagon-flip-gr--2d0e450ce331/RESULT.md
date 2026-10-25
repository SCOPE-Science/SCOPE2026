# Hamiltonian-union antipodes in the Tutte–Coxeter octagon-flip graph

## Finding

Let \(T\) be the Tutte–Coxeter graph, defined explicitly below. Let \(\mathcal{F}_8(T)\) have all perfect matchings of \(T\) as vertices, with two matchings adjacent exactly when their symmetric difference is one alternating cycle of length eight. Then \(\mathcal{F}_8(T)\) is a connected, ten-regular graph on \(288\) vertices, with \(1440\) edges, radius \(5\), and diameter \(6\). Its vertex eccentricity is determined exactly by the lengths of the cycles in the complementary two-factor \(T-M\):

| Cycle lengths of \(T-M\) | Matchings | Number at distances \(0,1,2,3,4,5,6\) from \(M\) | Eccentricity |
| --- | ---: | --- | ---: |
| \((10,20)\) | \(144\) | \((1,10,45,97,96,37,2)\) | \(6\) |
| \((30)\) | \(144\) | \((1,10,42,97,101,37,0)\) | \(5\) |

For distinct perfect matchings \(M,N\), the following conditions are equivalent:

\[
\operatorname{dist}_{\mathcal{F}_8(T)}(M,N)=6
\quad\Longleftrightarrow\quad
M\mathbin{\triangle}N\text{ is one Hamiltonian cycle of }T.
\]

There are exactly \(144\) unordered such antipodal pairs. Every matching with complementary two-factor \((10,20)\) has precisely two antipodes, and every matching whose complement is a Hamiltonian \(30\)-cycle has none. The graph \(T\) has \(90\) eight-cycles and no shorter simple cycle. Thus length eight is also the least permitted *single-cycle switch length* that can connect all perfect matchings.

## Assumptions and scope

All objects are finite and labeled. Start with \(X=\{0,1,2,3,4,5\}\). Its \(15\) two-element subsets are *duads*; its \(15\) partitions into three disjoint duads are *synthemes*. The bipartite graph \(T\) has these two collections as its parts, joining duad \(d\) to syntheme \(s\) if \(d\in s\). It has \(30\) vertices and \(45\) edges. This is the classical Tutte–Coxeter, or Tutte eight-cage, incidence model. The statement is independent of the particular ordering of duads and synthemes.

A perfect matching is a \(15\)-edge subset meeting each graph vertex exactly once. For such \(M\), the complement \(T-M\) has degree two at each vertex, hence is a disjoint union of simple cycles. If \(M\mathbin{\triangle}N\) is exactly one eight-cycle then the two matchings are adjacent in \(\mathcal{F}_8(T)\); an alternating eight-cycle may be flipped by replacing its four selected edges with the other four cycle edges. Cycles are not required to be facial or embedded. Distances refer only to these **eight-cycle** moves, not to unrestricted alternating-cycle moves, to four-cycle switch Markov chains, or to distances in \(T\) itself.

## Proof

**1. A finite and exhaustive representation.** Order the duads lexicographically and form all synthemes by partitioning the six-element set into three pairs. Sorting their triples of duad indices lexicographically fixes an ordering \(s_0,\ldots,s_{14}\). Every perfect matching is uniquely a vector \((m_0,\ldots,m_{14})\) in which \(m_i\) is the index of the duad matched to \(s_i\), with \(m_i\in s_i\), and all fifteen indices distinct. Conversely, every such vector selects fifteen disjoint incidence edges and is a perfect matching. The recursive enumerator in `verify_permutation.py` visits synthemes in order, tries all three incident duads not yet used, and retains precisely the completed length-fifteen vectors. Since the recursion considers every legal next choice exactly once, this is an exhaustive enumeration rather than sampling. The result is \(288\) distinct vectors.

**2. Exhaustive and sound characterization of the eight-cycle exchange relation.** Given vectors \(m,n\), the relative permutation \(m^{-1}\circ n\) on the syntheme indices has one nontrivial cycle of length \(k\) for each alternating cycle of length \(2k\) in \(M\mathbin{\triangle}N\). This is because, alternately following an edge of \(N\) and the unique inverse edge of \(M\), one passes from one syntheme to the next. Hence the exchange criterion is exactly that the relative permutation has a single nontrivial four-cycle. Checking every unordered pair of the \(288\) enumerated vectors gives \(1440\) distinct exchange edges and degree ten for every matching.

An independent enumeration in `verify_cycles.py` constructs the graph as 30 abstract vertices and 45 incidence edges, explicitly enumerates all simple four-, six-, and eight-cycles, and finds respectively \(0,0,90\) of them. It enumerates perfect matchings by picking the least unmatched vertex and trying all available incident edges. For each eight-cycle and each matching, it flips precisely when the matching contains one of the two alternating four-edge sets. This produces the same \(1440\)-edge exchange graph. Both programs order matchings by their 15-entry incidence vector and serialize the sorted exchange-edge index pairs, one pair per line. Their resulting SHA-256 digest is identically

`ba8739d1315a1daa2d3810948317a38cdf47b81a8cd37f5377e6825b7136e6a3`.

**3. Distance certificate.** For each of the \(288\) exchange-graph vertices, ordinary breadth-first search assigns distance zero at the source and assigns each new vertex one greater than its predecessor's distance. Standard breadth-first-search induction proves these are exact shortest-path lengths: no path of length smaller than the recorded distance can reach a vertex, and each first visit provides a path of that length. Both programs check that every distance is finite, proving connectivity. They independently compute the size of every cycle in \(T-M\) and group the 288 distance vectors by this cycle-length partition. Their identical results are precisely the two rows in the table above. In particular there are \(144\) matchings of each complementary type, all degrees are ten, the minimum eccentricity is five, and the maximum is six.

**4. Characterization of antipodes.** Each program tests all \(288\cdot287/2=41328\) unordered pairs and records those at distance six. Independently it determines whether the symmetric-difference edge set forms a single cycle through all 30 graph vertices. Both tests select exactly the same \(144\) unordered pairs; this proves both directions of the displayed equivalence, not just one implication. By the distance profiles, only complement type \((10,20)\) participates, each with exactly two distance-six partners. Thus both the antipodal-pair count and its complement-type qualification follow.

**5. Least possible move length.** The independent simple-cycle generator finds no four-cycle or six-cycle. The graph is simple and bipartite, so it also has no simple cycles of lengths two, three, five, or seven. Hence no alternating-cycle flip of length below eight exists. The length-eight exchange graph just proved is connected. Therefore eight is the minimal allowed single-cycle flip length yielding connectivity.

## Verification

The package includes complete independent programs `verify_permutation.py` and `verify_cycles.py` and their exact UTF-8 outputs `permutation_output.txt` and `cycles_output.txt`. Execute using a Python 3 interpreter, with no package dependencies:

```bash
python verify_permutation.py
python verify_cycles.py
```

The first verifier enumerates incidence bijections and computes symmetric-difference permutation cycles. The second independently generates incidence edges and matchings, enumerates all simple eight-cycles, and performs explicit alternating-cycle flips. Both enumerate the 288-vertex exchange graph, run breadth-first search from every vertex, and cross-check the Hamiltonian-union antipodal condition. Their common digest is specified in the proof. The exhaustive computation is feasible in seconds on an ordinary machine; no probabilistic test, remote lookup, or unexecuted certificate is needed.

## Relationship to prior work

The duad–syntheme model and the Tutte–Coxeter graph are classical; Baez's 2015 exposition explains the 30-vertex incidence construction, the graph's girth eight, and its symmetries [1]. Dyer, Jerrum and Müller studied a four-cycle switch Markov chain for perfect matchings in bipartite graphs; their 2015 preprint addresses ergodicity and mixing of that **different move model**, which has no nontrivial transition on a graph of girth eight [2]. Ito and collaborators studied shortest perfect-matching reconfiguration under **arbitrary-length alternating-cycle** moves, emphasizing algorithmic complexity and selected graph classes; the fixed eight-cycle metric here is a distinct restriction [3]. A later tabulation of matching polynomials already reports the count \(288\) for this graph; that scalar count is not asserted to be new [4]. The contribution here is the *restricted-switch distance geometry*, its two complementary-factor strata, and its Hamiltonian-union characterization of all longest pairs.

## Limitations

This is an exact finite classification for the single specified graph and the specified move model, not a uniform theorem for all generalized quadrangles, cubic cages, or other flip lengths. The two executable exhaustive proofs demonstrate the stated mathematical invariants, but they do not establish publication priority. Searches of the accessible literature and mathematical-result records found no equivalent eight-cycle metric classification; an inaccessible or differently titled result remains possible. No conclusion about mixing times or asymptotic reconfiguration follows from this finite calculation.

## References

[1] J. C. Baez, "Tutte–Coxeter Graph," *Visual Insight*, American Mathematical Society, 15 August 2015. https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/

[2] M. Dyer, M. Jerrum, H. Müller, "On the switch Markov chain for perfect matchings," first public arXiv submission 30 January 2015, arXiv:1501.07725. https://arxiv.org/abs/1501.07725

[3] T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi, Y. Okamoto, "Shortest Reconfiguration of Perfect Matchings via Alternating Cycles," first public arXiv submission 3 July 2019, arXiv:1907.01700. https://arxiv.org/abs/1907.01700

[4] "Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions," *Symmetry* 17 (2025), Article 133, doi:10.3390/sym17010133. The consulted indexed passage gives the matching count; complete direct text access was unavailable.

# Frozen and mobile Hamiltonian paths under face switches in the four-cube

## Finding

Let \(Q_4\) have vertex set \(\{0,1\}^4\), with edges between binary strings differing in one coordinate. A Hamiltonian path is an unoriented, unrooted simple path using all sixteen vertices. Its *face switch* toggles the four boundary edges of one coordinate square: two opposite edges in the path are removed and the other two are inserted, but a switch is admitted only when the result is again a single spanning path. Define \(\mathcal H\) with the Hamiltonian paths as vertices and these switches as edges.

**Theorem (complete finite classification).** The graph \(\mathcal H\) contains exactly \(45,696\) configurations and \(69,120\) exchange edges. Its connected-component size distribution is
\[
5184\,z+32\,z^{528}+32\,z^{738}.
\]
The \(5,184\) singleton components are frozen Hamiltonian paths. The remaining \(64\) components are exactly one connected, nontrivial component for each pair of distinct feasible endpoints, with endpoint separation either one or three in Hamming distance.

More precisely, for each of the \(32\) opposite-parity endpoint pairs at distance one there are exactly \(672\) Hamiltonian paths: \(144\) frozen configurations and one connected component of \(528\) configurations. For each of the \(32\) endpoint pairs at distance three there are exactly \(756\) Hamiltonian paths: \(18\) frozen configurations and one connected component of \(738\) configurations. The degree distribution of the entire exchange graph, as \((\mathrm{degree}:\mathrm{multiplicity})\), is
\[
(0:5184),(1:8064),(2:6528),(3:7296),(4:9408),
(5:2304),(6:2880),(7:3456),(8:576).
\]
Thus preserving just a path's two endpoints does not guarantee reachability by single face switches: there are frozen configurations for every feasible endpoint pair, while all other configurations with the same endpoints communicate.

## Assumptions and scope

The cube is the **labelled** four-dimensional binary hypercube. Hamiltonian paths are identified under reversal only. Switches use one of its exactly \(24\) coordinate-square faces, never a general four-cycle in an abstract graph. Only Hamiltonicity-preserving switches count; disconnected 2-regular/linear forests do not. No assertion is made for hypercubes of other dimensions, grid graphs, backbite moves, or double switches.

## Proof

This is an exhaustive *finite* classification certified by two standalone exact enumerators included with this report. Both programs traverse an explicitly finite search space without random sampling.

1. Index the \(32\) edges of \(Q_4\). The primary program recursively extends a self-avoiding path starting at the all-zero vertex, until all \(16\) vertices have been visited. Its completeness follows inductively: every path from that start is extended at each step by every unused adjacent vertex. Every arbitrary Hamiltonian path has an endpoint that can be mapped to zero by XOR translation. Applying all \(16\) translations to the starting-at-zero list and deduplicating edge sets yields precisely all unoriented labelled Hamiltonian paths, with no missing configurations.
2. The \(24\) coordinate squares are enumerated once: choose two varying coordinates and a fixed assignment to the other two. For every candidate path's \(32\)-bit edge set, test whether precisely one opposite edge pair occurs in that square. Toggle the four edge bits and retain the adjacent configuration if and only if the resulting edge set is in the full enumerated Hamiltonian-path list. The membership test exactly enforces the path condition. Every legal face switch is thus considered, and no other adjacency is admitted.
3. Perform ordinary graph traversal over every vertex to determine exact component sizes and degrees. Independently extract the two degree-one endpoints of each spanning path from its edge mask. The parity condition forces endpoint Hamming distance to be odd, hence either one or three. There are \(32\) unordered pairs at each of these distances. The program verifies the stated counts in each endpoint fiber and the complete component census.
4. The independent C++17 checker enumerates simple Hamiltonian paths from **every one** of the sixteen possible starting vertices, with a separate recursive construction, deduplicating only complete unoriented edge sets. It independently builds the graph by face-edge toggles and tests exact membership. Its degree census, edges and connected-component sizes agree with the primary enumeration. Source code is the finite proof certificate and can be replayed without external dependencies.

The total component size is \(5184+32\cdot528+32\cdot738=45696\), and the sum of all vertex degrees is \(138240\), twice the reported \(69120\) edges. The endpoint-fiber sizes satisfy \(32\cdot672+32\cdot756=45696\). These checks supplement, rather than substitute for, the exhaustive source-level generation proof.

## Verification

Run `python3 verify_primary.py` and compile and run `verify_alt.cpp` with a conforming C++17 compiler. Both programs should print a success marker and the complete component and degree distributions. The two methods differ crucially in generating paths: the Python code starts at zero and transports paths by all cube translations, while the C++ code starts at every endpoint and deduplicates resulting edge sets. Both compute switches and components from stored complete edge sets.

## Relationship to prior work

Chebiryak and Kroening (2008) study **Hamiltonian cycles** in hypercubes and enumerate the four-cube cycles; this theorem concerns *paths* and their strict face-switch reconfiguration. The general switch-reconfiguration framework of Takaoka (2018) does not state this labelled four-cube endpoint-fiber census in its accessible abstract. Kazazi's January 2026 rectangular-grid work uses additional double switches and endpoint-relocating backbites and deals with planar rectangular grids rather than the binary four-cube. Kazazi's October 2026 Hamiltonian-path work uses the backbite operation, again not the endpoint-preserving face switch. These operation differences prevent deriving the theorem's sharp component sizes directly from the cited statements. Existing count-only hypercube Hamiltonian-path work may be relevant; no independent novelty certification is claimed.

## Limitations

This finite theorem applies only to \(Q_4\). Enumeration provides an exact proof once the generator and transition rules are verified; it does not establish infinite-dimensional behaviour. The data do not rule out an equivalent earlier computation in unindexed or inaccessible literature. Independent external audit has not been performed.

## References

- Y. Chebiryak and D. Kroening, *Towards a Classification of Hamiltonian Cycles in the 6-Cube*, 2008, DOI: 10.3233/SAT190038 (earliest verified public date 2008-02-01).
- A. Takaoka, *Complexity of Hamiltonian Cycle Reconfiguration*, Algorithms 11(9), 140 (2018), DOI: 10.3390/a11090140.
- A. Kazazi, *Reconfiguration of Hamiltonian Paths and Cycles in Rectangular Grid Graphs*, arXiv:2601.06749 (2026).
- A. Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths*, arXiv:2610.05068 (2026).

# Square-switch components of Hamiltonian cycles in the four-cube

## Finding
Let \(Q_4\) be the graph on all sixteen four-bit words, adjacent when they differ in exactly one bit. Let \(\mathcal H\) contain its undirected Hamiltonian cycles, where cyclic rotations and reversal represent the same cycle. Define a graph \(\mathcal F\) on \(\mathcal H\): two cycles are adjacent when replacing the two selected opposite edges of one square face by the other two face edges produces the other Hamiltonian cycle. Equivalently, this is the graph of valid Hamiltonian two-edge switches.

**Theorem (exact finite classification).** The graph \(\mathcal F\) has exactly \(1344\) vertices and \(1920\) edges. Its degree distribution is:

| Degree | Number of Hamiltonian cycles |
|---:|---:|
| 0 | 240 |
| 1 | 384 |
| 2 | 192 |
| 4 | 288 |
| 8 | 240 |

It has precisely \(241\) connected components: \(240\) isolated vertices and one connected component \(\mathcal G\) of size \(1104\). The latter has radius \(10\), diameter \(12\), and eccentricity multiplicities \(96,192,816\) at eccentricities \(10,11,12\), respectively.

Under the entire \(384\)-element automorphism group of \(Q_4\), the Hamiltonian cycles form nine orbits. Their (orbit size, switch degree) pairs, with repeated entries representing distinct orbits, are
\[
(48,0),\ (96,0),\ (96,0),\ (384,1),\ (192,2),\ (96,4),\ (192,4),\ (48,8),\ (192,8).
\]
Thus the isolated cycles comprise three full symmetry orbits and the nontrivial component comprises the other six.

The numbers of unordered pairs in \(\mathcal G\) at distances \(1,2,\ldots,12\) are, in order,
\[
(1920,7488,14208,41232,47424,112080,81408,152736,54912,79488,7488,8472).
\]
Their sum is \(608856=\binom{1104}{2}\).

## Assumptions and scope
The vertex labels are the integers \(0,1,\ldots,15\) interpreted as four-bit words. An edge is an unordered pair \(\{u,v\}\) for which \(u\oplus v\) is a power of two. A Hamiltonian cycle is a set of sixteen edges forming one spanning simple cycle; neither starting point nor orientation is distinguished. A square face is obtained by fixing two coordinate positions and varying the other two. Exactly \(24\) such faces occur. A switch is counted only when its resulting sixteen-edge set is again one Hamiltonian cycle, not merely a disjoint union of cycles. No statement about dimensions other than four is made.

## Proof
**1. Exhaustive state enumeration.** Every Hamiltonian cycle passes through vertex \(0\). Starting there and recursively extending a vertex-simple walk across all sixteen vertices enumerates every oriented Hamiltonian cycle; demanding that the second vertex have smaller label than the last vertex picks exactly one orientation. This gives \(1344\) distinct sixteen-edge masks. Independently, recursively pairing the smallest remaining vertex with each still-unmatched neighbor constructs exactly \(272\) perfect matchings. Each Hamiltonian sixteen-cycle has exactly two alternating perfect matchings, and conversely the disjoint union of two perfect matchings is Hamiltonian precisely if its degree-two graph is connected. Enumerating every unordered pair of matchings, testing disjointness and connectivity, gives exactly the same set of \(1344\) masks. Both exhaustive constructions are implemented in `verify.py`.

**2. Exact move equivalence.** The symmetric difference of the edge sets of any two cycles is an even-degree subgraph. Two distinct Hamiltonian cycles differing in at most four edges therefore differ in exactly four edges: a nonempty simple even-degree subgraph on at most four edges in a graph of girth four is a four-cycle. Every four-cycle in \(Q_4\) is a square face, and the two original edges must be opposite. Therefore a valid two-edge Hamiltonian switch is equivalent to taking the symmetric difference with exactly one of the twenty-four square-face masks and checking that the result remains Hamiltonian. This establishes necessity and sufficiency of the implemented adjacency test, without an extra assumption about how the cycle is drawn.

**3. Components, degrees and distances.** Enumerating all twenty-four face masks against all \(1344\) cycle masks constructs the entire finite adjacency graph. An independent edge-pair test joins two cycles exactly when their symmetric difference equals a square-face mask; the two adjacency lists agree entry by entry. Their degrees total \(3840\), hence there are \(1920\) edges. Complete connected-component traversal finds \(240\) singleton components and a single component on \(1104\) vertices. Breadth-first search from every vertex of that component determines all eccentricities and the complete pair-distance distribution reported above; the greatest distance is \(12\) and the smallest eccentricity is \(10\).

**4. Symmetry classification.** All coordinate permutations and independent coordinate complements act as automorphisms, giving \(4!\,2^4=384\) explicit transformations. Applying each to the set of sixteen cycle edges partitions the \(1344\) cycles into nine orbits, with sizes and constant switch degrees listed in the theorem. Since each automorphism preserves square faces and validity of switches, the degree is constant within each orbit. All three degree-zero orbits are isolated; the other six lie in the unique nontrivial component. These finite computations are fully reproducible by the standalone implementation and its asserted intermediate totals.

## Verification
Run `python3 verify.py` with Python 3 and no external dependencies. The executable checks the exhaustive path and perfect-matching enumerations against each other; confirms all twenty-four faces; compares the face-flip adjacency list with a separately constructed symmetric-difference adjacency list; computes every component and all shortest-path distances in the connected component; and checks all \(384\) coordinate automorphisms and their nine orbits. The script terminates with `VERIFY_OK` only after every claimed count passes an exact assertion. Both primary enumerations are finite and bounded by the full sixteen-vertex state space, so no extrapolation or untested infinite range is used.

## Relationship to prior work
Gilbert's 1958 study already classifies Hamiltonian cycles of the four-cube up to automorphism; the known nine symmetry types are not asserted to be new. Chebiryak and Kroening (2008) explicitly tabulate the already-known \(1344\) cycles and nine automorphism types, but their subject is a different classification by coordinate-change numbers, not the graph of valid two-edge switches. Kleer, Patel and Stroh (2020) formalize Hamiltonian switch-chain irreducibility and prove positive results under large minimum-degree assumptions, along with examples of reducibility. Their theorems do not imply the four-cube's exact component profile: this graph has sixteen vertices and minimum degree four, far below their positive threshold of fifteen, and their counterexamples are different graphs. The new assertion here concerns exactly \(241\) components, the \(240\) isolated cycles, the unique \(1104\)-vertex component and its exact metric and symmetry profile. Existence and enumeration of the cycles, the definition of switching, and the number of symmetry types are treated as prior context.

## Limitations
The result is specific to the four-dimensional cube and to switches changing two selected edges; a larger switch size may connect previously separated components. The computation gives no mixing-time bound even within the large component. The comparison with Gilbert's original paper was limited to its accessible bibliographic account and indexed portions rather than its entire original text; undiscovered tables or earlier computation of this switch graph remain an originality risk. None of these limits affects the exact finite calculation.

## References
1. E. N. Gilbert, *Gray Codes and Paths on the n-Cube*, Bell System Technical Journal 37 (1958), 815–826. DOI: 10.1002/j.1538-7305.1958.tb03887.x; public listing dated 1958-05-01.
2. Y. Chebiryak and D. Kroening, *Towards a Classification of Hamiltonian Cycles in the 6-Cube*, Journal on Satisfiability, Boolean Modeling and Computation 4 (2008), 57–74. DOI: 10.3233/SAT190038.
3. P. Kleer, V. Patel and F. Stroh, *Switch-based Markov Chains for Sampling Hamiltonian Cycles in Dense Graphs*, Electronic Journal of Combinatorics 27(4) (2020), #P4.29. DOI: 10.37236/9503.
4. OEIS A066037, number of undirected Hamiltonian cycles of the binary hypercube, the previously tabulated value \(1344\) in dimension four.

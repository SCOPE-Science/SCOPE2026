# Two stable exchange components for minimum zero forcing on three-row grids

## Finding
For the Cartesian grid \(G_n=P_3\square P_n\), with \(n\ge5\), the zero forcing number is \(Z(G_n)=3\). Exactly 26 three-vertex sets achieve it. Under *token jumping* (replace one selected vertex by one unselected vertex, keeping a minimum zero forcing set), their reconfiguration graph is the disjoint union \(H\sqcup H\) of two isomorphic, connected graphs on 13 vertices and 24 edges each. Each component has degree polynomial
\[
2t^2+2t^3+8t^4+t^6,
\]
radius three and diameter five, with five vertices of eccentricity three, six of eccentricity four, and two of eccentricity five.

The disconnected regime begins sharply at \(n=5\): for \(n=4\), there are 26 minimum zero forcing sets and their exchange graph is connected, with 56 edges. For \(n=3\), the graph is connected with 20 configurations and 44 exchange edges. In both exceptional cases \(Z(G_n)=3\).

The result also classifies every minimum set, not merely their number. Index rows by \(r=0,1,2\) and columns by \(j=0,\ldots,n-1\). The three-bit *column mask* \(s_j\) has bit \(r\) set precisely when \((r,j)\) belongs to the initial forcing set. Let \(\mathcal L\) be the following thirteen three-column words, with masks in the order \((s_0,s_1,s_2)\):

```
(0,3,1) (0,6,4) (1,1,1) (1,3,0) (3,0,1)
(3,2,0) (4,4,4) (4,6,0) (5,1,0) (5,4,0)
(6,0,4) (6,2,0) (7,0,0)
```

For \(n\ge5\) the complete set of minimum forcing configurations is exactly
\[
\{(p_0,p_1,p_2,0,\ldots,0):p\in\mathcal L\}
\;\cup\;
\{(0,\ldots,0,p_2,p_1,p_0):p\in\mathcal L\}.
\]
The two displayed families are disjoint. Their induced exchange graphs are the two copies of \(H\), and there are no exchange edges between them.

## Assumptions and scope
All graphs are finite, undirected, and simple. A vertex is *blue* if initially selected; a blue vertex may force its unique white neighbor to become blue. A zero forcing set is one that eventually colors all vertices blue, regardless of the order of legal forces. The exchange graph has one vertex for each *minimum* zero forcing set, with adjacent sets differing in exactly one selected vertex. The result concerns ordinary zero forcing, not skew, positive semidefinite, or leaky forcing.

The infinite classification is computationally assisted but fully quantified over all \(n\ge5\). Its finite-state verification checks an exhaustive transition-graph closure for arbitrarily long column words; it is not an extrapolation from finitely many lengths. The exceptional cases \(n=3,4\) are separately exhaustive finite enumerations.

## Proof
**1. Fort equivalence.** A *fort* is a nonempty vertex set \(F\) for which every vertex outside \(F\) has either zero or at least two neighbors inside \(F\). An initially blue set \(S\) is zero forcing if and only if every fort meets \(S\). Indeed, if forcing stops before all vertices become blue, the remaining white vertices form a fort disjoint from \(S\). Conversely, a first force into an initially unblue fort disjoint from \(S\) is impossible, because the forcing vertex would then have exactly one neighbor in that fort.

**2. Exact column automaton.** Encode the candidate fort by three-bit masks \(f_j\), with artificial boundary masks \(f_0=f_{n+1}=0\); here the actual column masks are indexed \(1\) through \(n\) for this automaton only. The requirement \(f_j\wedge s_j=0\) encodes disjointness from the blue set. Define \(V(a,b,c)\) to mean that in the middle column \(b\), every row bit absent from \(b\) has a number of neighbors in the fort unequal to one. More explicitly, for each \(r=0,1,2\) with bit \(r\) absent from \(b\), require
\[
\operatorname{bit}_r(a)+\operatorname{bit}_r(c)
+\mathbf1_{r>0}\operatorname{bit}_{r-1}(b)
+\mathbf1_{r<2}\operatorname{bit}_{r+1}(b)\ne1.
\]
This is exactly the fort condition at every vertex in the middle column.

An exact nondeterministic machine stores \((a,b,z)\) where \(a,b\in\{0,\ldots,7\}\) are the two most recent fort masks and \(z\in\{0,1\}\) remembers whether a nonzero fort mask has appeared. This gives 128 possible local states. At the first grid column, choose any \(b\) disjoint from its blue mask and initialize \((0,b,\mathbf1_{b\ne0})\). Upon reading the next blue mask \(s\), choose \(c\) disjoint from \(s\), retain the transition precisely if \(V(a,b,c)\), and update to \((b,c,z\vee\mathbf1_{c\ne0})\). At the right boundary accept precisely if \(z=1\) and \(V(a,b,0)\). By induction on the number of examined columns, accepting paths are in bijection with nonempty forts disjoint from the initial blue set. Thus the initial blue set forces exactly when this automaton has **no** accepting path.

**3. Finite exhaustive closure over all lengths.** Independently recognize the language consisting of the thirteen left-end words from the Finding and their thirteen reflected right-end words, with arbitrarily many zero masks beyond the three occupied columns. Compare this pattern recognizer with the determinized fort machine in a finite product automaton. Track total blue population, truncated at three, and word length, truncated at five. Exhaustively follow every allowed next column mask, merging repeated product states. The standalone file `verify/infinite_fort_dfa.py` verifies that precisely 926 states are reachable in this product and that **no** state of population three and length at least five disagrees about whether its word is zero forcing. This is an exhaustive check of every possible input word, including arbitrarily long words, because the length-five state loops through all continuations and the search ends only when every transition closes within the explored state set.

A second exhaustive closure, with blue population at most two and length truncated at three, has exactly 245 reachable states, every one of whose length-at-least-three states admits a fort. Hence no set of fewer than three vertices can force \(G_n\) when \(n\ge3\). Conversely each listed template forces by the preceding language equivalence, establishing the exact minimum \(Z(G_n)=3\) and the complete 26-set classification for \(n\ge5\).

**4. Exchange components.** Every pattern in \(\mathcal L\) contains three marked positions in its first three columns. Two such patterns are adjacent if and only if they share exactly two marked positions. This defines a fixed 13-vertex graph \(H\) that can be constructed directly from the displayed templates. Exact enumeration of its 78 possible unordered pairs gives 24 edges, a single connected component, degree distribution \((2,2,8,1)\) at degrees \((2,3,4,6)\), and eccentricities distributed as stated. For \(n\ge5\), a left-end and a right-end template cannot share two marked positions: they have disjoint supports except possibly the single middle column at \(n=5\), where each has at most one marked vertex. Hence there are no exchanges between the two copies of \(H\). Both are connected.

**5. Small-width boundary.** Directly enumerate all \(\binom{3n}{3}\) triples for \(n=3,4\), apply the unique-white-neighbor closure, then compare each unordered pair of valid triples. The standalone `verify/direct_grid.py` reproduces 20 vertices and 44 edges, connected, for \(n=3\); and 26 vertices and 56 edges, connected, for \(n=4\). The same independent direct procedure is also run through \(n=10\), providing a separate finite cross-check on the automaton and templates.

## Verification
Run `python3 verify/infinite_fort_dfa.py` and `python3 verify/direct_grid.py` from the package root with Python 3.10 or later; neither script requires third-party libraries. Their expected terminal results are, respectively, `FORT_AUTOMATON_ALL_LENGTHS_PASS` with counts 926 and 245, and `DIRECT_FORCING_ALL_SMALL_GRIDS_PASS` together with `REFERENCE_COMPONENT_13_VERTICES_24_EDGES_PASS`.

The first program's state-set closure is a checkable finite certificate for the infinite theorem, using only bit operations, set inclusion and breadth-first search; its code explicitly implements the transition invariant proved above. The second program reconstructs actual grid adjacency and ordinary forcing without using the fort characterization, and also reconstructs the finite reference graph \(H\). Both were executed successfully on the packaged files. No unproved infinite extrapolation is used.

## Relationship to prior work
Barioli et al., *Zero forcing parameters and minimum rank problems*, arXiv:1003.2028v1, publicly posted March 10, 2010, gives the zero-forcing framework and connects it with minimum rank and path covers; neither a three-row-grid minimum-set census nor this exchange graph is asserted there. Geneson, Haas and Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (September 1, 2020), introduces and studies the same token-jumping exchange graph generally. Its forest-connectivity theorem and examples of disconnected graphs do not imply the fixed 13-vertex structure of this cyclic grid family. Inspection of its sections on examples, disconnected graphs, forests, and algorithms did not identify a three-row-grid treatment.

The new claim is the complete width-three boundary template classification, the sharp connected-to-disconnected transition from four to five columns, and the exact stable component geometry, not the definition of zero forcing or of its exchange graph. Related results on zero forcing polynomials of fans and friendship graphs concern different base graphs and do not imply this grid-specific statement.

## Limitations
The component classification is restricted to the ordinary zero forcing graphs of \(P_3\square P_n\). No assertion is made for grids with four or more rows, alternative recoloring rules, or the token-addition/removal graph. The all-length proof depends on a small, fully supplied, auditable finite-state exhaustive calculation, rather than a purely handwritten classification of each of the 26 cases. Historical literature under alternative terminology or unavailable exact tables may still contain equivalent results; absence from the inspected sources is not an independent priority certification. No independent mathematical audit has been performed.

## References
1. F. Barioli et al., *Zero forcing parameters and minimum rank problems*, arXiv:1003.2028v1 (2010-03-10), https://arxiv.org/abs/1003.2028.
2. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (2020-09-01), https://arxiv.org/abs/2009.00220.
3. AIM Minimum Rank--Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra Appl. 428 (2008), 1628--1648, DOI:10.1016/j.laa.2007.10.009; historical background only.

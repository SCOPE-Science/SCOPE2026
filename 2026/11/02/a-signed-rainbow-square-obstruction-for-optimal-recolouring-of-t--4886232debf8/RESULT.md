# A signed-rainbow-square obstruction for optimal recolouring of the Chvátal graph

## Finding
Let \(H\) be the twelve-vertex Chvátal graph described by the edge list below and let \(\mathcal R_4(H)\) be the graph of proper vertex colourings \(c:V(H)\to\{0,1,2,3\}\), with an edge precisely when two colourings differ at one vertex. There are exactly **18,024** colourings, **64,320** recolouring edges, and **two connected components of 9,012 colourings each**. None is frozen.

These components are precisely the level sets of the explicitly defined signed-rainbow-four-cycle invariant \(I(c)\in\{-3,+3\}\) given in the table below; every single-vertex recolouring preserves \(I\). Each component has radius **16** and diameter **20**. Globally, the exact eccentricity enumerator, in increasing order from eccentricity 16 through 20, is \[(192,9024,8424,336,48).\] Each component contributes exactly half of every entry.

Allowing a **single simultaneous change at at most two vertices** between two proper endpoint colourings makes the entire space connected; this is sharp, as the one-vertex graph is disconnected. Exactly 11,616 unordered distance-two pairs bridge the two sectors, supported on twenty of the twenty-four edges of \(H\). Five named colours also suffice for connectivity under ordinary single-vertex recolouring; four do not.

## Assumptions and scope
Every graph and colouring is finite, labelled, simple, and undirected. Vertex set is \(V(H)=\{0,1,\ldots,11\}\). Edges in \(H\), listed once each, are:

`(0,1), (0,4), (0,6), (0,9), (1,2), (1,5), (1,7), (2,3), (2,6), (2,8), (3,4), (3,7), (3,9), (4,5), (4,8), (5,10), (5,11), (6,10), (6,11), (7,8), (7,11), (8,10), (9,10), (9,11)`

The four colours are **named**; colour permutations produce distinct states. Recolouring steps require a proper colouring at every intermediate state. For simultaneous two-vertex steps, only the two endpoint colourings must be proper, not an intermediate one-vertex recolouring. Distances, eccentricities, radius, and diameter refer to shortest paths inside the appropriate connected component.

For an oriented four-cycle \(Q=(v_0,v_1,v_2,v_3)\), put \(s_Q(c)=0\) unless its four vertex colours are pairwise distinct. If distinct, set \(s_Q(c)=(-1)^{\mathrm{inv}(c(v_0),c(v_1),c(v_2),c(v_3))}\), where \(\mathrm{inv}\) counts inverted pairs in the indicated sequence of the integers 0 through 3. Define \(I(c)=\sum_{j=1}^{11}\epsilon_j s_{Q_j}(c)\), using:

| Term | Oriented four-cycle | \(\epsilon_j\) |
|---:|---|---:|
| 1 | `(0,1,2,6)` | +1 |
| 2 | `(0,1,5,4)` | -1 |
| 3 | `(0,4,3,9)` | -1 |
| 4 | `(0,6,11,9)` | +1 |
| 5 | `(1,2,3,7)` | +1 |
| 6 | `(1,5,11,7)` | -1 |
| 7 | `(2,3,4,8)` | +1 |
| 8 | `(2,6,10,8)` | -1 |
| 9 | `(3,7,11,9)` | -1 |
| 10 | `(4,5,10,8)` | +1 |
| 11 | `(5,10,6,11)` | +1 |

This is a **signed sum of rainbow square indicators**, not the usual three-colour winding number on an odd cycle. All listed sequences close to four-cycles in the specified graph.

## Proof
**1. Complete colour space.** The exhaustive recursion in `chvatal_verifier_a.py` assigns vertex colours in order 0 through 11 and tries every colour not used by an already-coloured neighbour. This branches on every and only possible extension, so its 18,024 leaves are *all* proper four-colourings, without duplication; it also returns zero proper three-colourings. The independent construction in `chvatal_verifier_b.py` instead enumerates all four ordered vertex-set partitions into independent sets and obtains exactly the same 18,024 colourings. Thus \(\chi(H)=4\); the count 18,024 was known previously [3].

**2. Signed obstruction.** Program A evaluates each of the eleven oriented four-cycles and its permutation sign at all 18,024 states, and checks exhaustively that exactly 9,012 states have \(I=+3\) and 9,012 have \(I=-3\), with no other values. It enumerates every legal single-vertex recolouring (by checking all twelve vertices and four target colours), verifying \(I(c)=I(c')\) across each of the resulting 64,320 undirected edges. This finite exhaustive check is a proof of invariance on the specified graph, not an unproved general four-cycle identity. In particular the graph has at least two components.

**3. Exhaustiveness of the sectors.** A complete graph traversal computes exactly two components of size 9,012; the independent Hamming-one-bucket construction in Program B checks the same components without relying on Program A's recursion or edge algorithm. Invariance and the fact that each level set has 9,012 states now imply that each level set is *one entire component*. A permutation of two colour names reverses all nonzero rainbow-square signs, and hence exchanges these two components.

**4. Exact distance bounds.** Program A uses the listed eight automorphisms of \(H\) and all twenty-four permutations of the named colours. It independently verifies that each listed vertex map preserves the 24 edges and that the eight maps form a group. Their joint action on colourings partitions the 18,024 vertices into **108 orbits**. Eccentricity is invariant under these transformations. Breadth-first search from one representative of each orbit reaches exactly 9,012 vertices and gives the complete eccentricity enumerator \[(192,9024,8424,336,48).\] Consequently the two component radii are 16, their diameters 20, and each contributes half the indicated eccentricity counts.

**5. Minimal simultaneous moves.** Program B independently enumerates every unordered pair of proper four-colourings whose Hamming distance is exactly two. Of these, **11,616** cross the two invariant sectors, each changing the colours at two adjacent vertices. In particular the valid pair `(2,3,0,3,0,1,1,2,1,1,0,0)` and `(2,3,0,1,0,1,1,2,1,3,0,0)` changes only vertices 3 and 9 and joins opposite sectors. Since each sector is already connected using one-vertex steps, adding this one two-vertex step connects the entire space. No zero- or one-vertex step crosses sectors, proving sharpness.

**6. Five colours.** Theorem 2 of Feghali–Johnson–Paulusma [4] shows that the proper \((\Delta+1)\)-colourings of a connected graph with \(\Delta\ge3\) have at most one nonisolated component; all other components are frozen singletons. Here \(\Delta=4\), and in a frozen five-colouring every vertex must have neighbours of the other four colours, forcing all five colour classes to have equal size (count edges between each pair of classes). This is impossible because \(5\nmid12\). Hence there are no frozen five-colourings, so the five-colour recolouring graph is connected. This deduction invokes a known theorem, not a new general connectivity result.

## Verification
The package includes two independent, Python-stdlib-only programs, run by:

`python3 chvatal_verifier_a.py`

`python3 chvatal_verifier_b.py`

Each reconstructs all state and edge objects afresh. A verifies the signed invariant, every legal edge, symmetry orbit completeness, all component distances and precise eccentricities. B enumerates independent-set partitions, builds legal edges via deletion-coordinate grouping, and checks all 11,616 cross-sector two-vertex transitions. Assertions abort on a mismatch. Both programs were executed successfully against these exact package contents before acceptance. The 108 orbit representative breadth-first searches cover *all* possible eccentricities because the verified transformations are graph automorphisms. An isolated computational log is not being used as a proof of an infinite theorem.

## Relationship to prior work
Chvátal's original graph [1] is established prior art, as are its triangle-free, four-regular and four-chromatic properties. Henderson [3] explicitly reported the count of 18,024 proper named four-colourings. Cereceda–van den Heuvel–Johnson [2], sections 3–4, establish three-colour cycle winding obstructions and examples of disconnected \(k\)-colouring graphs for \(k\ge4\); their results do not specify the Chvátal recolouring graph or this signed rainbow-square invariant. Feghali–Johnson–Paulusma [4] proves the five-colour connectivity invoked in Step 6, but its \(\Delta+1\) theorem does not cover the four-colour component theorem where \(k=\Delta=4\). The nontrivial contribution is the **complete description of the optimal recolouring sectors by an explicit eleven-term signed-square invariant**, their exact metric, and the sharp two-vertex escape from those sectors. The published count 18,024 and the general five-colour theorem are not claimed as discoveries.

## Limitations
This theorem covers precisely the displayed labelled twelve-vertex graph and the stated recolouring rules. The signed invariant is established by complete finite verification; no universal identity for all four-chromatic graphs is claimed. Historical novelty is qualified: unindexed literature might state an equivalent reconfiguration census or four-cycle invariant under another name. The original 1970 graph note was not available in full, although it is not expected from its title to address recolouring dynamics. No independent scholarly audit has been performed.

## References
[1] Václav Chvátal, “The smallest triangle-free 4-chromatic 4-regular graph,” Journal of Combinatorial Theory 9 (1970), 93–94; DOI: 10.1016/S0021-9800(70)80057-6. Earlier original graph source; exact first public calendar day not determined here.
[2] Luis Cereceda, Jan van den Heuvel, Matthew Johnson, “Connectedness of the Graph of Vertex-Colourings,” LSE-CDAM-2005-11, July 2005, https://matthewjohnsondurham.github.io/papers/cdam-2005-11.pdf (original public day not established).
[3] Matthew Henderson, “Chromatic Polynomials,” July 11, 2014, https://mhenderson.github.io/mjhmathblog/posts/2014-07-11-chromatic-polynomials/index.html. The number of proper four-colourings of the Chvátal graph is explicitly recorded as 18,024, and is prior art.
[4] Carl Feghali, Matthew Johnson, Daniël Paulusma, “A Reconfigurations Analogue of Brooks' Theorem and its Consequences,” arXiv:1501.05800v1, January 23, 2015, https://arxiv.org/pdf/1501.05800. In particular Theorem 2 proves connectivity of non-frozen \(\Delta+1\)-colourings.

# Exact \((3,5)\)-geodesic chromatic numbers of circular ladders

## Finding
Let \(Q_n=C_n\square K_2\) be the circular ladder (prism graph) with \(n\ge3\). In a \((3,5)\)-proper coloring, no shortest path with at most five edges contains three vertices of the same color. The exact number of colors is
\[
\chi^3_5(Q_n)=\begin{cases}
2,&n\in\{3,4\},\\
3,&n\in\{5,6\},\\
5,&n=9,\\
4,&n\in\{7,8\}\text{ or }n\ge10.
\end{cases}
\]
In particular, the nine-rung prism is the only member requiring five colors, while every prism with at least ten rungs admits four colors despite increasing diameter. This is a complete classification at the fixed parameters \((k,d)=(3,5)\), not an assertion for other parameters.

## Assumptions and scope
Vertices are \((i,r)\) with \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\). Each \((i,r)\) is adjacent to \((i\pm1,r)\) and \((i,1-r)\). A geodesic is a shortest path between its endpoints. All geodesics of length at most five are tested, including those with multiple choices of shortest paths. A colored column is the ordered pair \((f(i,0),f(i,1))\); symbols in the finite witness table are the integers \(0,1,2,3,4\), used as opaque color names. A color class may contain vertices with adjacent positions; only monochromatic triples on bounded geodesics are prohibited.

## Proof
**Small-order lower bounds.** Any one-coloring of \(Q_3\) or \(Q_4\) has a monochromatic three-vertex shortest path, so at least two colors are needed. For \(5\le n\le9\), the graph diameter equals \(\lfloor n/2\rfloor+1\le5\), so \((3,5)\)-proper coloring is exactly ordinary general-position coloring. The published theorem that \(\operatorname{gp}(P_2\square C_n)=4\) for these values of \(n\) (Chandran et al., Theorem 7.7, citing Klavžar et al.) gives
\[
\chi^3_5(Q_n)\ge\left\lceil \frac{2n}{4}\right\rceil.
\]
This yields the claimed lower bounds \(3,3,4,4,5\) for \(n=5,6,7,8,9\) respectively. Thus the five-color obstruction at nine rungs is already implied by an earlier general-position result; the finite enumeration below independently corroborates, rather than originates, that obstruction.

**Uniform lower bound for large orders.** For every \(n\ge10\), the subgraph on any five consecutive columns is an isometric copy of \(P_5\square K_2\): its rim distances are at most four, shorter than any path going the other way around the cycle. An exact finite search establishes that \(P_5\square K_2\) admits no \((3,5)\)-proper three-coloring. Here is its complete, independently reproducible proof procedure (implemented as `verify_prism.py`). Enumerate all shortest paths with at most five edges by building graph distances with breadth-first search and enumerating simple paths of at most that length; record each contained unordered vertex triple. Color the ten vertices in the fixed order \((0,0),(0,1),(1,0),(1,1),\ldots,(4,1)\). Up to permutation of colors, the first vertex has color zero, and at each later vertex the only possible labels are existing labels and one new label. Reject a candidate label precisely when it completes a monochromatic recorded triple. The exhaustive recursion visits 88 nodes, never reaches a full coloring, and has no timeout or heuristic cutoff. Every labeled three-coloring is equivalent to one of these explored canonical labelings; therefore the search proves non-three-colorability, not merely an experimental lower bound. Isometry transfers the obstruction to every \(Q_n\) with \(n\ge10\), giving \(\chi^3_5(Q_n)\ge4\).

**Finite upper witnesses.** The complete `prism_witnesses.json` specifies an explicit valid coloring (a list of row-ordered pairs) for each
\[
n\in\{3,4,5,6,7,8,9,10,11,12,13,14,15,17,21\}.
\]
The associated palette sizes are, in that order,
\[
2,2,3,3,4,4,5,4,4,4,4,4,4,4,4.
\]
Their validity is a finite, exhaustive verification, not an inference from sample behavior: `verify_prism.py` reconstructs every bounded geodesic from the indicated graph and checks every contained three-vertex subset against each coloring.

**Locality and pumping.** For \(n\ge10\), every geodesic of at most five edges in \(Q_n\) is contained in six consecutive cyclic columns, and these six columns form an isometric \(P_6\square K_2\). Consequently a coloring is valid if and only if every cyclic six-column word is valid as a coloring of the linear six-column strip. This is a finite-window condition. Regard each ordered pair of colors as one letter, a five-column word as a state, and an admissible six-column word as an edge between its first and last five-column windows. Cyclic valid colorings are directed closed walks in this finite directed graph.

The four-periodic ordered-pair sequence
\[
(0,1),(1,0),(2,3),(3,2),(0,1),(1,0),(2,3),(3,2),\ldots
\]
forms a legal walk: it is a segment of the explicit valid twelve-column periodic witness, hence all of its six-column windows are legal. Four witness words, of lengths \(12,14,15,21\), begin with at least ten columns of this periodic sequence. In each, the first five-column state equals the state four steps later; the intervening four transitions form a directed closed walk. Repeating this closed walk preserves validity and increases the circumference by four. Equivalently, insert four additional consecutive periodic columns immediately after the first four columns, any number of times. Thus each base \(b\in\{12,14,15,21\}\) generates valid four-colorings for all \(b+4j\), \(j\ge0\). These classes give all orders \(n\ge12\) except \(n=13,17\); the separate witnesses for \(n=10,11,13,17\) fill the gaps. Together with the explicit small witnesses, this proves all upper bounds and the formula.

## Verification
The package contains a standard-library-only checker `verify_prism.py`, immutable `prism_witnesses.json`, and its recorded output `verify_prism_output.txt`. The program constructs its own adjacency matrices, computes shortest-path distances with breadth-first search, enumerates all simple paths of up to five edges and all triples on each geodesic, and tests every witness. It also exhaustively rules out palettes smaller than the claimed answer for prism orders \(3\) through \(9\), and independently rules out three colors on the five-column straight ladder. For each of the four pumping seeds it explicitly checks four longer pumped instances in addition to the original. Its final output line is `VERIFY_OK`. Only the finite instances are checked computationally; the locality lemma and closed-walk pumping argument prove the infinite extension.

## Relationship to prior work
Cody and Detore (arXiv:2601.04351v1, initially publicly posted January 7, 2026) define the \((k,d)\)-chromatic number and solve paths and cycles, but their discussion of Cartesian products poses further calculations as an open research direction; it does not determine prism graphs. Chandran, Di Stefano, Haritha, Thomas and Tuite (arXiv:2408.13494v2, Section 7) study ordinary general-position colorings and establish known bounds for cylindrical graphs. Their cited classification of the general-position number of \(P_2\square C_n\) covers the small-case lower bounds above, but they do not provide the fixed bounded-geodesic \((3,5)\) prism formula; for large \(n\), general-position coloring imposes many more constraints than the present fixed five-edge bound. The earlier maximum-position classification of Cody and Moore (arXiv:2409.05644) concerns maximum admissible vertex sets, not partitions into bounded-geodesic color classes. Nothing here claims an original definition of the invariant or a new lower bound for the nine-rung general-position case.

## Limitations
The theorem addresses only \((3,5)\) and circular ladders; it says nothing about other parameters, arbitrary cylinder width, or all minimum colorings. The lower-bound certificate for the five-column straight ladder is exhaustive finite code rather than a short hand-derived obstruction; the complete source is included for replay and inspection. The theorem has undergone only a self-review, not independent mathematical audit. An equivalent, unindexed result under different notation remains a bibliographic risk.

## References
1. B. Cody and R. Detore, *Metric general position extensions of classical graph invariants*, arXiv:2601.04351v1 (first posted 2026-01-07), https://arxiv.org/html/2601.04351v1.
2. U. Chandran S. V., G. Di Stefano, Haritha S., E. J. Thomas, and J. Tuite, *Colouring a graph with position sets*, arXiv:2408.13494v2 (2025 revision, original preprint 2024), especially Section 7, https://arxiv.org/pdf/2408.13494.
3. S. Klavžar, B. Patkós, G. Rus, and I. G. Yero, *On general position sets in Cartesian products*, Results in Mathematics 76 (2021), Article 123 (general-position number cited in Reference 2).
4. B. Cody and G. Moore, *The k-general d-position problem for graphs*, arXiv:2409.05644 (2024), https://arxiv.org/abs/2409.05644.

# Power-of-two rigidity of perfect edge domination in Boolean cubes

## Finding

For each integer \(d\ge 2\), let \(Q_d\) be the graph with vertex set \(\{0,1\}^d\), two vertices joined precisely when they differ in one coordinate. A *perfect edge-dominating set* (PEDS) is an edge subset \(F\) such that each edge outside \(F\) shares an endpoint with exactly one edge in \(F\). Edges within \(F\) are not required to be uniquely dominated.

A PEDS \(F\) other than \(E(Q_d)\) exists **if and only if \(d\) is a power of two**. Every such nontrivial PEDS has cardinality exactly \(2^{d-1}\), and every nontrivial PEDS has precisely the following form:

Choose one of the two bipartition classes \(U\) (even or odd binary vectors). Choose a subset \(B\subseteq U\) so that every vertex in the opposite bipartition class has exactly one neighbor in \(B\). Then \(F\) is the set of **all** graph edges incident with \(B\). Conversely, every such \(B\) produces a PEDS, and different pairs \((U,B)\) produce different nontrivial PEDS.

In particular, writing \(\gamma_{\mathrm{pe}}\) for the minimum PEDS cardinality,

\[
\gamma_{\mathrm{pe}}(Q_d)=
\begin{cases}
2^{d-1},&d\text{ is a power of }2,\\
d\,2^{d-1},&\text{otherwise},
\end{cases}
\qquad(d\ge2).
\]

For dimensions not a power of two, the full edge set is the **unique** PEDS. In the power-of-two dimensions, \(\lvert B\rvert=2^{d-1}/d\), and its opposite-part neighborhoods partition that bipartition class.

## Assumptions and scope

All graphs are finite, undirected and simple. The dimension is an integer \(d\ge2\). A graph edge is adjacent to another edge when they share an endpoint, and the PEDS requirement applies only to unchosen edges. The binary vector parity classes are fixed by the sum of coordinate bits modulo two. The dimension \(d=1\) is excluded to avoid the degenerate one-edge case. The theorem determines existence, all configurations by an exact code-like condition, and the minimum size; it does **not** count all codes \(B\) in arbitrary admissible dimensions.

## Proof

**Step 1: degree constraints.** Fix a PEDS \(F\) and write \(t(v)=\deg_F(v)\). For any unselected edge \(uv\notin F\), the number of selected edges incident to one of its endpoints is \(t(u)+t(v)\). Therefore the PEDS condition is exactly \(t(u)+t(v)=1\) for every \(uv\notin F\). If \(t(v)\ge2\), an unselected incident edge would violate this identity, so every incident edge is selected, whence \(t(v)=d\). Accordingly, every vertex has type **black** \((t=d)\), **yellow** \((t=1)\), or **white** \((t=0)\).

**Step 2: there are no selected yellow–yellow edges.** Suppose \(yy'\in F\) and \(t(y)=t(y')=1\). Because \(d\ge2\), choose a neighbor \(w\ne y'\) of \(y\). The edge \(yw\notin F\) forces \(t(w)=0\). In the unique coordinate square containing edges \(yy'\) and \(yw\), let \(x\) be the fourth vertex (adjacent to \(y'\) and \(w\)). The edge \(y'x\notin F\) forces \(t(x)=0\), but then the unselected edge \(wx\) has both endpoint degrees zero, contradicting its required sum one.

**Step 3: a selected black–black edge makes the set trivial.** Suppose adjacent vertices \(b,b'\) are both black. Every neighbor \(y\) of \(b\) has a selected incident edge, so is black or yellow. If \(y\ne b'\) is yellow, consider the unique coordinate square \(b,y,x,b'\). Since \(y\) has its single selected edge to \(b\), the edge \(yx\notin F\) forces \(x\) white. Yet \(b'x\in F\), contradicting whiteness. Therefore every neighbor of \(b\) is black, and the same argument propagates along black–black edges. Connectivity of \(Q_d\) forces all vertices black and \(F=E(Q_d)\).

**Step 4: canonical bipartition and divisibility.** Assume \(F\ne E(Q_d)\). A black vertex must exist: otherwise every selected edge would join two yellow vertices (impossible by Step 2), and the empty selected set cannot dominate an edge. By Step 3, no black–black edge occurs. There is no black–white edge because every black-incident edge is selected, contradicting the white degree; no yellow–yellow edge because a selected such edge is prohibited by Step 2 and an unselected such edge would have endpoint-degree sum two; and no white–white edge because an unselected such edge has endpoint-degree sum zero. Thus every edge crosses the partition \(B\cup W\) versus \(Y\). Since \(Q_d\) is connected and bipartite, this partition agrees, up to reversal, with its canonical binary parity bipartition. In particular, all selected edges join \(B\) to \(Y\), and each yellow vertex has exactly one black neighbor. Because \(B\) is in one parity class and \(Y\) is the entire other class,

\[
 d\lvert B\rvert=\lvert Y\rvert=2^{d-1},\qquad
 \lvert F\rvert=\lvert Y\rvert=2^{d-1}.
\]

Thus the integer \(d\) divides the power of two \(2^{d-1}\); therefore \(d\) itself must be a power of two. The argument also proves the claimed exhaustive structural form. Conversely, if \(B\) is contained in one parity class and every vertex in the other class has precisely one neighbor in \(B\), choosing every edge incident to \(B\) gives a PEDS: each unchosen edge joins a vertex in the opposite class with one selected incident edge to a same-class vertex with none, hence is uniquely dominated.

**Step 5: construction in every power-of-two dimension.** Let \(d=2^r\), \(r\ge1\). Label the \(d\) coordinate positions by the elements of \(\mathbb F_2^r\). Put

\[
B=\left\{x\in\{0,1\}^d:\ \sum_a x_a=0\pmod2,\quad \sum_a x_a a=0\in\mathbb F_2^r\right\}.
\]

For every odd-parity vertex \(y\), the syndrome \(s=\sum_a y_a a\) identifies a *unique* coordinate position \(a=s\). Flipping that coordinate turns \(y\) into an even vector of syndrome zero. No other coordinate flip does so. Therefore every odd vertex has exactly one neighbor in \(B\), completing the construction and the proof.

## Verification

The standalone Python 3 program `verify.py` implements an independent graph-edge definition of a PEDS and the explicit syndrome construction. It exhaustively checks all \(16\) edge subsets of \(Q_2\) and all \(4096\) edge subsets of \(Q_3\). It enumerates all \(512\) candidates supported in one bipartition class for \(Q_4\) and counts eight satisfying the exact-neighbor condition. Finally it directly tests the constructed PEDSs for \(d=2,4,8\) (respectively \(2,8,128\) selected edges). All checks pass. Run `python3 verify.py`. Finite verification supplements, but does not replace, the dimension-unrestricted proof above.

## Relationship to prior work

Lin, Lozin, Moyano and Szwarcfiter (2017) introduce the standard black/yellow/white coloring of PEDS and basic consequences in arbitrary graphs; the present theorem uses those general definitions but derives the Boolean-cube square rigidity and precise power-of-two criterion, which are not a stated consequence of their algorithmic and complexity results. Their Observation 7 concerns efficient edge domination; this theorem concerns the more permissive PEDS definition.

Grippo, Lin, Moyano and Vera (2026) investigate PEDS counting and extremal structures of trees, forests and chordal graphs, plus counting algorithms on generalized series-parallel and chordal graphs. The Boolean cubes of dimension at least four do not lie in those graph classes. Their full manuscript was unavailable for complete inspection, so an unobserved related result cannot be categorically excluded.

Do Forte, Hanafi and Lucena (2023) introduce and computationally test integer-programming formulations for perfect vertex and edge domination. A potentially relevant hypercube computational test set does not, by itself, supply the present infinite-family characterization; its full text was not available for a definitive section-by-section comparison. Do Forte and collaborators (2022) instead study neighborhood star-free graphs, in which vertices of degree at least two belong to triangles, unlike these triangle-free cubes.

## Limitations

The result covers binary cubes \(Q_d\), \(d\ge2\), and the standard definition exempting selected edges from unique domination. It does not enumerate all nontrivial PEDSs for general power-of-two dimensions or solve weighted PEDS. The detailed bibliographic-priority determination remains uncertain because the full text of some relevant sources could not be checked. The mathematical claims have not undergone independent external validation.

## References

1. L. N. Grippo, M. C. Lin, V. Moyano, C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894 (first public version 2026-07-04), https://arxiv.org/abs/2607.03894.
2. M. C. Lin, V. V. Lozin, V. A. Moyano, J. L. Szwarcfiter, *Perfect Edge Domination: Hard and Solvable Cases*, Annals of Operations Research (2017), DOI:10.1007/s10479-017-2664-3, https://wrap.warwick.ac.uk/92507/.
3. V. L. do Forte, S. Hanafi, A. Lucena, *Extended formulations for perfect domination problems and their algorithmic implications*, European Journal of Operational Research 310 (2023), 566–581, DOI:10.1016/j.ejor.2023.03.022.
4. V. L. do Forte et al., *Some New Results on Efficient and Perfect Edge Domination of Graphs*, arXiv:2204.11785 (2022), https://arxiv.org/abs/2204.11785.

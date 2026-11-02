# Parity obstructions to metric general-position perfection of three-arm trees

## Finding

For every even integer \(k\ge4\) and odd integer \(q\ge3\), define
\[
d=q(k-1)-1,\qquad L=\frac d2,\qquad T=T_{q,k}=S(L,L,L).
\]
Here \(S(L,L,L)\) is a three-arm tree with a common center and three internally disjoint paths, each of length \(L\) edges. Then
\[
\boxed{\omega_d^k(T)=d+1=q(k-1),\qquad\chi_d^k(T)\ge q+1.}
\]
Thus none of these trees is \((k,d)\)-perfect. In particular, for the 13-vertex tree \(S(4,4,4)\),
\[
\boxed{\omega_8^4(S(4,4,4))=9,\qquad\chi_8^4(S(4,4,4))=4
>\left\lceil\frac{9}{3}\right\rceil=3.}
\]
This answers Question 6.7 of Cody and Detore [1] negatively.

## Assumptions and scope

All graphs are finite, simple, undirected, and connected. Path length means the number of edges. Following Definition 1.1 and Definition 3.1 of [1], a vertex coloring of a graph \(G\) is \((k,d)\)-proper if no shortest path with at most \(d\) edges contains \(k\) vertices of one color; \(\chi_d^k(G)\) is its minimum number of colors. A vertex set \(Q\) is a \((k,d)\)-clique if every \(k\)-element subset of \(Q\) lies on some shortest path of length at most \(d\); \(\omega_d^k(G)\) is the largest size of such a set. A graph is \((k,d)\)-perfect if the equality
\[
\chi_d^k(H)=\left\lceil\frac{\omega_d^k(H)}{k-1}\right\rceil
\]
holds for every induced subgraph \(H\) of \(G\). To disprove perfection it is enough to find strict inequality for \(H=G\).

Write the common center as \(o\). For each arm \(i\in\{1,2,3\}\), write its vertices as \(v_{i,1},\ldots,v_{i,L}\) in increasing distance from \(o\). Since \(k\) is even and \(q\) odd, \(q(k-1)\) is odd, so \(d\) is even and \(L\) is an integer. The diameter of \(T\) is \(2L=d\).

## Proof

**1. Exact clique parameter.** Every path between leaves of distinct arms has \(2L+1=d+1=q(k-1)\) vertices and length \(d\). Its vertex set is a \((k,d)\)-clique: any \(k\) of its vertices lie on this same shortest path. Thus \(\omega_d^k(T)\ge d+1\).

Conversely, suppose \(Q\subseteq V(T)\) has more than \(d+1=2L+1\) vertices. The center and the vertices in any two arms total only \(2L+1\); hence \(Q\) meets all three arms. Choose one vertex of \(Q\) from each arm. Since \(|Q|>d+1\ge k\), these three vertices extend to a \(k\)-element subset of \(Q\). Every simple path in a tree meets at most two of the three arms away from the center: a simple path cannot traverse three branches from a degree-three vertex. Accordingly, no geodesic contains this \(k\)-subset, and \(Q\) is not a \((k,d)\)-clique. This gives \(\omega_d^k(T)\le d+1\), proving equality.

**2. Parity obstruction for colorings.** The clique lower bound from [1, Proposition 2.3] gives
\[
\chi_d^k(T)\ge\left\lceil\frac{q(k-1)}{k-1}\right\rceil=q.
\]
Assume for contradiction that a \((k,d)\)-proper coloring uses at most \(q\) colors. Regard it as using a palette of exactly \(q\) names, allowing initially unused names. Let \(P_{ij}\) be the diameter path joining the leaves of arms \(i\) and \(j\), for distinct \(i,j\in\{1,2,3\}\). Each \(P_{ij}\) has exactly \(q(k-1)\) vertices. A color occurs on this path at most \(k-1\) times. There are only \(q\) colors, so equality in the total-count bound forces **every** color to occur exactly \(k-1\) times on **each** diameter path. In particular, every palette color is used.

Choose one color \(c\) different from the color assigned to the center \(o\); such a color exists because \(q\ge3\). Let \(a_i\) be the number of vertices with color \(c\) on the \(i\)-th arm, excluding \(o\). Since \(o\) does not have color \(c\), the three diameter paths give
\[
a_1+a_2=k-1,\qquad a_1+a_3=k-1,\qquad a_2+a_3=k-1.
\]
Subtracting shows \(a_1=a_2=a_3\), so \(2a_1=k-1\). But \(a_1\) is an integer and \(k-1\) is odd. This is impossible. Therefore \(\chi_d^k(T)\ge q+1\), strictly exceeding \(\lceil\omega_d^k(T)/(k-1)\rceil=q\). Since the failure occurs on \(T\) itself, \(T\) is not \((k,d)\)-perfect.

**3. Exact small witness.** Choose \(k=4\), \(q=3\), so \(d=8\), \(L=4\). The preceding argument establishes \(\omega_8^4=9\) and \(\chi_8^4\ge4\). For the reverse inequality, color the center \(o\) with color \(0\), and on every arm color the depth-\(t\) vertex with \(t\bmod4\), for \(1\le t\le4\). Every geodesic of \(T\) is contained in a diameter path between leaves in two different arms. On each diameter path, color \(0\) appears exactly three times (at the center and both depth-four leaves), and each other color appears exactly twice. Thus no geodesic contains four vertices of one color, so the coloring is \((4,8)\)-proper. Consequently \(\chi_8^4=4\).

## Verification

The accompanying standard-library Python script `verify.py` constructs the original 13-vertex tree and all 91 shortest paths, independently enumerates its \((4,8)\)-cliques among all vertex subsets, and obtains \(\omega_8^4=9\). With the center's color fixed to zero (permissible by renaming color names), it tests all \(3^{12}=531441\) assignments of three colors on the other vertices. None satisfies the three diameter-path constraints. It then constructs the four-color depth-residue coloring and checks every shortest path. Successful output ends with `VERIFY_OK`. The exhaustive computation supports only the 13-vertex example; the infinite two-parameter statement rests on the preceding proof.

## Relationship to prior work

Cody and Detore [1] introduced the chromatic and clique parameters and the definition of \((k,d)\)-perfection. They proved that all paths are \((k,d)\)-perfect for all parameters and all finite trees are \((3,2)\)-perfect (Proposition 3.6). Their Question 6.7 asks whether the tree result extends to all parameters. The parity obstruction above gives a negative answer for infinitely many pairs of parameters; it does not contradict the earlier positive statements. Cody and Moore [2] studied the underlying \(k\)-general \(d\)-position sets rather than the perfection question. The general-position coloring studied by Chandran et al. [3] concerns the related \(k=3\) geodesic condition rather than this higher-order parity obstruction.

## Limitations

For general even \(k\ge4\) and odd \(q\ge3\), only the lower bound \(\chi_d^k(T)\ge q+1\) is established here; an exact general chromatic formula is not claimed. The small case \((k,d)=(4,8)\) is exact. The example is not asserted to have minimum order among all counterexamples. This does not characterize all trees that are \((k,d)\)-perfect, all parameter pairs causing failure, or the corresponding invariants on induced subtrees. Priority against unindexed or otherwise inaccessible research remains provisional.

## References

[1] Brent Cody and Rose Detore, *Metric general position extensions of classical graph invariants*, arXiv:2601.04351, first public version 2026-01-07; revised manuscript, Definition 1.1, Proposition 2.3, Definition 3.1, Proposition 3.6, and Question 6.7. https://arxiv.org/abs/2601.04351

[2] Brent Cody and Garrett Moore, *The \(k\)-general \(d\)-position problem for graphs*, arXiv:2409.05644 (2024). https://arxiv.org/abs/2409.05644

[3] Ullas Chandran S. V. et al., *Colouring a graph with position sets*, arXiv:2408.13494 (first public version 2024). https://arxiv.org/abs/2408.13494

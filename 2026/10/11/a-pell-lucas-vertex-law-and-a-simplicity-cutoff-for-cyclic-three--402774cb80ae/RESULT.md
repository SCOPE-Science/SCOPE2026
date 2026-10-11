# A Pell–Lucas vertex law and a simplicity cutoff for cyclic three-term deformations

## Finding
For each integer \(n\ge4\), write indices modulo \(n\), let \(e_i\) be the coordinate unit vectors in \(\mathbb R^n\), and put
\[
Q_n=\sum_{i\in\mathbb Z/n\mathbb Z}\operatorname{conv}\{e_i,e_{i+1}\}
+\sum_{i\in\mathbb Z/n\mathbb Z}\operatorname{conv}\{e_i,e_{i+1},e_{i+2}\}.
\]
Then \(Q_n\) has dimension \(n-1\), and its number of vertices is exactly
\[
\boxed{f_0(Q_n)=(1+\sqrt2)^n+(1-\sqrt2)^n
-2\left(\left(\frac{1+\sqrt5}{2}\right)^n+
\left(\frac{1-\sqrt5}{2}\right)^n\right).}
\]
Furthermore, \(Q_n\) is simple if and only if \(n=4\). Its initial vertex counts for \(n=4,5,6,7,8,9\) are, respectively, \(20,60,162,420,1060,2634\). Equivalently, the vertex sequence is a Pell–Lucas trace minus twice a Lucas trace; the subtraction counts precisely the two directed-cycle obstructions in a local orientation model.

## Assumptions and scope
All sums are Minkowski sums in \(\mathbb R^n\), and every displayed simplex is counted once per cyclic index. The case \(n=3\) is excluded because cyclic triples repeat the same underlying three-element set. Every summand has coordinate sum \(1\), so \(Q_n\subseteq\{x:\sum_i x_i=2n\}\). The cycle-edge summands span the linear subspace \(\{x:\sum_i x_i=0\}\), hence \(\dim Q_n=n-1\).

Up to translation by \(\sum_i e_i\), this is the second graph polytope of the cycle \(C_n\), formed from all connected induced vertex subsets of cardinality at most three. It is a geometric deformation of the graphical zonotope of the squared cycle \(C_n^2\): each simplex support is a clique of that graph, so its normal fan coarsens the graphical fan of \(C_n^2\). No statement is made about its entire face vector, except the simplicity classification.

## Proof
**1. Winner assignments are vertices and are distinct.** Let \(\mathcal H_n\) consist of the \(n\) two-element cyclic edges and the \(n\) three-element cyclic intervals. For a linear functional with pairwise distinct coordinate coefficients \(w_i\), each hyperedge \(H\) has a unique maximizing coordinate \(a(H)\in H\), and the exposed vertex of \(Q_n\) is \(v(a)=\sum_{H\in\mathcal H_n}e_{a(H)}\). Conversely, every vertex admits an exposing functional with distinct coordinate coefficients (perturb inside its full-dimensional normal cone). Two distinct feasible winner assignments cannot yield the same vector: if distinct assignments \(a,b\) are exposed by \(w,z\), then
\[
(w-z)\cdot(v(a)-v(b))=
\sum_{H\in\mathcal H_n}\bigl[(w_{a(H)}-w_{b(H)})+(z_{b(H)}-z_{a(H)})\bigr]>0,
\]
because each summand is nonnegative and one is positive. Thus it suffices to count feasible winner assignments.

**2. Encode edge winners and valleys.** Write \(s_i=+\) if \(w_i<w_{i+1}\) and \(s_i=-\) otherwise. The cyclic signs determine every winner on a consecutive triple, except at a *valley* \(i\) satisfying \((s_{i-1},s_i)=(-,+)\). At such a valley, \(w_i\) is smaller than both neighbors and the triple winner can be either neighbor. Therefore a sign word \(s\) with \(v(s)\) valleys has exactly \(2^{v(s)}\) formal winner assignments. Direct the comparisons from smaller to larger coordinates, orienting all cycle edges according to the signs and adding at every valley one directed chord joining \(i-1\) and \(i+1\), oriented toward its chosen triple winner. A formal assignment is feasible exactly when this directed comparison multigraph is acyclic: a topological ordering supplies strict coordinates satisfying every required inequality. The remaining triple winners are already forced by the cycle comparisons.

**3. Characterize exactly the forbidden assignments.** Every valley has both cycle edges pointing away from it. Valleys cannot be adjacent, and no added chord has a valley as endpoint. Hence a valley belongs to no directed cycle. After deleting all valleys, replace the two removed cycle edges across each valley with its chord. The remaining underlying multigraph is one cyclic polygon on \(n-v(s)\) vertices (possibly a two-vertex cycle with parallel edges when \(n=4\)). Accordingly, a directed cycle occurs precisely when every remaining comparison runs uniformly clockwise or uniformly counterclockwise.

The clockwise option exists if and only if the positions carrying the sign \(-\) form an independent set in the cyclic adjacency graph on the \(n\) edge positions. Indeed, each isolated minus edge is removed at its terminal valley, whereas two consecutive minus edges leave an unremoved backward edge. In that case precisely one assignment of chord directions completes the clockwise directed cycle. Analogously, the counterclockwise option exists if and only if the positions carrying \(+\) form a cyclic independent set, and then precisely one chord assignment is forbidden. These two forbidden orientations are disjoint: if both independent-set conditions hold, the word alternates and at least one chord is present; opposite directed cycles prescribe opposing directions for that chord. The all-plus and all-minus words each give only their expected one obstruction. Thus the total number of forbidden formal assignments is twice the number of independent sets of an \(n\)-cycle.

**4. Evaluate both cyclic traces.** The total number of formal assignments is the weighted cyclic binary-word sum
\[
\sum_{s\in\{-,+\}^n}2^{v(s)}=
\operatorname{tr}\begin{pmatrix}1&2\\1&1\end{pmatrix}^{n}
=(1+\sqrt2)^n+(1-\sqrt2)^n.
\]
The number of cyclic independent sets is
\[
\operatorname{tr}\begin{pmatrix}1&1\\1&0\end{pmatrix}^{n}
=\left(\frac{1+\sqrt5}{2}\right)^n+
\left(\frac{1-\sqrt5}{2}\right)^n.
\]
Subtracting twice the latter count gives the asserted vertex formula for all \(n\ge4\).

**5. The simplicity cutoff.** A normal cone of a vertex is the order cone of the winner-comparison partial order, modulo the all-ones line. Its irredundant facet inequalities correspond exactly to cover relations in that poset: transitive comparisons are redundant, while identifying the endpoints of a cover preserves acyclicity and produces a codimension-one face. This order-cone criterion is also established for hypergraphic polytopes by Benedetti, Bergeron and Machacek (Theorem 3.2). Since \(Q_n\) has dimension \(n-1\), a vertex is simple exactly when its comparison poset has \(n-1\) covers. For every \(n\ge5\), take an exposing functional whose coordinate values in cyclic order are
\[
(w_0,w_1,\ldots,w_{n-1})=(0,1,\ldots,n-3,n-1,n-2).
\]
The cover relations are exactly \(0\prec1\prec\cdots\prec n-2\), together with \(1\prec n-1\prec n-2\). There are \(n\) distinct covers, and thus this vertex is nonsimple. For \(n=4\), exhaustive inspection of all \(4!=24\) strict coordinate orders yields \(20\) distinct winner assignments and precisely three covers for every assignment. This finite step is reproduced by the included exact-integer checker, completing the proof. \(\square\)

## Verification
Run `python3 verify.py` with Python 3 and the standard library. For \(4\le n\le12\), an independent directed-graph enumeration checks all \(2^n\) sign words, each of their valley-chord assignments, the cyclic independent-set obstruction criterion, and both integer traces. A separate implementation enumerates all coordinate permutations for \(4\le n\le8\), merges identical Minkowski-sum vertex coordinates, and computes each normal-cone cover count. Its resulting degree-of-normal-cone-facets distributions, indexed by \(n\), are \(\{3:20\}\), \(\{4:50,5:10\}\), \(\{5:96,6:66\}\), \(\{6:182,7:238\}\), and \(\{7:336,8:724\}\). Explicit nonsimplicity witnesses are independently tested for \(5\le n\le40\). These finite tests check the algebra and the low-dimensional base case; the symbolic argument in the Proof establishes the all-dimensional claim.

## Relationship to prior work
Benedetti, Bergeron and Machacek (arXiv:1712.08848, first posted 23 December 2017) establish the general identification between acyclic hypergraph orientations, faces, and Hasse-cover simplicity. Applying their theorem does not evaluate the cyclic length-three vertex count. Padrol, Pilaud and Poullot (arXiv:2111.12422, first public version 24 November 2021, primary MSC 52B11) give the general deformation-cone theory of graphical zonotopes, including simplex summands supported on cliques. Pešović and Stojadinović (arXiv:2209.12053, first public version 24 September 2022, primary MSC 05C22) introduce the intermediate \(m\)-graph polytopes and give a general Hopf-algebraic \(f\)-polynomial specialization; this paper provides the closest graph-polytope construction. Their formula in principle allows instance-by-instance enumeration, but it does not display the cyclic second-stage Pell–Lucas cancellation or the sharp simplicity cutoff. Gélinas and Yang (arXiv:2605.03913, first public version 5 May 2026) establish a lattice characterization for cyclic-interval hypergraphic posets, rather than this exact polytope vertex count or simplicity criterion. These are comparisons of scientific conclusions, not claims that the general theories cannot be specialized to the present family.

## Limitations
This theorem applies only to the specified \(n\)-cycle family, to the two- and three-element summands each with unit coefficient, and to \(n\ge4\). The sequence and simplicity cutoff do not determine all higher-dimensional faces or flag enumerators. Finite verifier output alone is not a proof for unbounded \(n\). An equivalent cyclic-hypergraph enumeration could exist under other terminology despite the targeted literature and database searches; independent literature adjudication has not been performed.

## References
1. C. Benedetti, N. Bergeron, J. Machacek, *Hypergraphic polytopes: combinatorial properties and antipode*, arXiv:1712.08848 (2017), https://arxiv.org/abs/1712.08848, Theorems 2.18 and 3.2.
2. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (2021), https://arxiv.org/abs/2111.12422, especially the graphical deformation and clique-simplex theory.
3. M. Pešović, T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053 (2022), https://arxiv.org/abs/2209.12053, Definition 2.1 and formula (3).
4. F. Gélinas, Y. Yang, *Lattice characterization of cyclic interval hypergraphic posets*, arXiv:2605.03913 (2026), https://arxiv.org/abs/2605.03913, introduction and main theorem.

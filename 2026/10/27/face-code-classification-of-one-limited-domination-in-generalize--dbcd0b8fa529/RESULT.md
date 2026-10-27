# Face-code classification of one-limited domination in generalized Hamming graphs

## Finding
Let \(d\ge1\), \(q_1,\ldots,q_d\ge2\), \(G=K_{q_1}\square\cdots\square K_{q_d}\), \(N=\prod_iq_i\), and \(q_* = \min_i q_i\). A set \(D\subseteq V(G)\) is **one-limited dominating** if every vertex outside \(D\) has a neighbor in \(D\), while every vertex of \(D\) has at most one neighbor outside \(D\). A **coordinate face** fixes some coordinate values and allows all values in each remaining coordinate; it is **proper** if at least one coordinate is fixed.

**Complete set classification.** The one-limited dominating sets are exactly the complements of unions of proper coordinate faces with pairwise Hamming distance at least three (the empty union is allowed). Here the distance between two sets is the minimum Hamming distance between their members.

**Exact extremum and rigidity.** Every such graph satisfies
\[
\gamma_1^{\mathrm L}(G)=N-\frac{N}{q_*}.
\]
Its minimum sets are *exactly* the complements of the individual coordinate hyperplanes
\[
F_{i,a}=\{x\in V(G):x_i=a\}\quad (q_i=q_*,\ 0\le a<q_i).
\]
Thus the number of distinct labelled minimum sets is exactly
\[
q_*\,|\{i:q_i=q_*\}|.
\]
This applies to unequal clique sizes and arbitrarily many factors. The full face-code classification is stronger than the extremal statement.

## Assumptions and scope
The factors are finite simple complete graphs on explicitly labelled alphabets of sizes \(q_i\ge2\). Vertices are tuples; adjacency means differing in exactly one coordinate. Distances between vertices equal Hamming distances. A face is a product whose \(i\)-th factor is either the whole \(i\)-th alphabet or a singleton. All collections of faces are finite, and the empty collection is permitted. No connectedness assumption beyond that of the factors is necessary.

The use of *one-limited* differs from the older notion of an external-neighborhood nearly perfect set, although the complement of a one-limited dominating set is such a set.

## Proof
Put \(T=V(G)\setminus D\). The one-limited constraint says that no vertex of \(D\) has two neighbors in \(T\). Consequently:

1. **Full coordinate line rule.** If two distinct vertices in a coordinate line lie in \(T\), every vertex of that line lies in \(T\): any omitted vertex is adjacent to both selected vertices, violating the constraint. The statement is automatic for a two-point line.

2. **Rectangle rule.** If three corners of a coordinate rectangle lie in \(T\), so does its fourth corner. Indeed, the fourth corner is adjacent to the two opposite corners that differ from it in one coordinate; if outside \(T\), it would be a vertex of \(D\) with two neighbors in \(T\). This also applies when the two varying coordinates have unequal alphabet sizes.

**Component lemma.** Every connected component \(C\) of \(G[T]\) is a coordinate face. To prove this, call coordinate \(i\) *active* when an edge of \(C\) changes coordinate \(i\). The full-line rule makes the entire \(i\)-line lie in \(C\) at both ends of an active edge. Moreover, this property propagates across any edge \(xy\) of \(C\): if that edge changes another coordinate \(j\ne i\), then for every vertex \(z\) in the \(i\)-line through \(y\), its counterpart \(z'\) in the \(i\)-line through \(x\) lies in \(C\), and \(z\) is adjacent to both \(y\) and \(z'\); hence \(z\in T\) (with \(z=y\) already known). Therefore the full \(i\)-line property holds at every vertex of connected \(C\). Every inactive coordinate has a fixed value on \(C\), since no edge of a connecting path changes it. Closure under every active coordinate change now shows \(C\) consists of *all* tuples obtained by freely varying its active coordinates and fixing the others. This proves the lemma.

Distinct components of \(G[T]\) have distance at least three. Distance one would connect them. If their distance were two, a common neighbor on a two-step shortest path would either lie in \(T\), joining the components, or in \(D\), contradicting one-limitedness. Every component must also be a proper face, since domination requires each vertex of \(T\) to have a neighbor in \(D\); the whole graph has none. This proves necessity of the stated face-code structure.

For sufficiency, suppose \(T\) is the union of proper faces pairwise at distance at least three. Each vertex in any one proper face has a neighbor outside that face, obtained by changing a fixed coordinate; this neighbor is not in another face because all the other faces are at distance at least three. Hence \(D\) dominates \(T\). An outside vertex can have **at most one neighbor in a fixed face**: a coordinate change into that face must correct one fixed coordinate, and the resulting face vertex is uniquely determined. A vertex in \(D\) cannot have neighbors in two distinct faces, as that would put their mutual distance at most two. Therefore every vertex in \(D\) has at most one neighbor in \(T\). This establishes the full equivalence.

For the sharp minimum, let \(T\ne\emptyset\). Each component of \(G[T]\) is a proper face, so at least one coordinate is fixed there. Each vertex of a component has exactly \(\sum_{i\in I}(q_i-1)\) neighbors in \(D\), where \(I\) is the nonempty set of fixed coordinates. This is at least \(q_*-1\). Hence the number \(e(T,D)\) of crossing edges obeys
\[
(q_*-1)|T|\le e(T,D)\le |D|=N-|T|.
\]
The second inequality is the one-limited constraint. Thus \(|T|\le N/q_*\) and \(|D|\ge N-N/q_*\). If \(q_i=q_*\), taking \(T=F_{i,a}\) attains equality: each vertex of \(D\) has exactly one neighbor in \(T\), and every vertex of \(T\) has \(q_*-1\) neighbors in \(D\).

For equality, each vertex of each face component must have exactly \(q_*-1\) neighbors outside its component; hence there is **exactly one** fixed coordinate, necessarily of alphabet size \(q_*\). Every component is therefore a full coordinate hyperplane of a minimum-size alphabet. If \(T\) contained two components, choose one such hyperplane \(F_{i,a}\). Every vertex outside it is adjacent to a vertex in \(F_{i,a}\) (change just coordinate \(i\)); no second component of \(G[T]\) can then exist. Thus \(T\) is one such hyperplane, and conversely all of them attain the bound. Their complements are distinct, proving the count.

## Verification
The accompanying `verify_hamming.py` constructs the graphs directly from their tuple alphabets and independently checks the defining neighbor constraints against the face-union characterization. It enumerates **all subsets** for ten profiles of order at most eighteen. For five larger profiles, an integer linear program establishes the predicted optimum and excludes all enumerated coordinate-hyperplane complements before obtaining a strictly larger feasible cardinality. The recorded output ends with `VERIFY_OK`. These are finite corroborations; the unrestricted result is proved above.

For example, the three-factor graph \(K_3\square K_3\square K_4\) has order \(36\), one-limited domination number \(24\), and exactly six minimum sets. The mixed-alphabet graph \(K_2\square K_3\square K_4\) has order \(24\), domination number \(12\), and exactly two minimum sets.

## Relationship to prior work
Božović, Radić, Kovijanić-Vukićević and Tepeh introduced \(k\)-limited domination and general bounds in 2026 [1]. Tepeh's 2026 product paper [2] proves a universal Cartesian-product upper bound and determines some grids, rook graphs, and hypercube cases; it does **not** state this general multi-factor face-code characterization. Its product upper bound yields the present numerical optimum in the binary-factor case, and its hypercube result is previously known. The two-factor rook-graph minimum formula and low-capacity optimizer configurations have also been established previously and are not claimed new here.

Kwaśnik and Perl [3] studied **maximal nearly perfect sets** in two graph products. Our complementary \(T\) is a nearly perfect set, but their product estimates do not classify all such complements that are dominated from outside or determine the all-factor extremum. Bespalov et al. [4] studied perfect two-colorings of uniform-alphabet Hamming graphs. At equality, the present two classes do form a perfect coloring, making that literature relevant to homogeneous extremizers; however, the face-code description concerns *every feasible set*, and the theorem permits unequal alphabet sizes. These previously available reductions and special cases are acknowledged rather than claimed original.

## Limitations
The result concerns capacity one, not general \(k\). It does not count all feasible sets by size (the face-code criterion is a characterization, not a closed polynomial). It concerns Cartesian products of complete graphs, not arbitrary Cartesian products. The literature comparison cannot exclude an equivalent unindexed characterization under the terminology of nearly perfect sets, completely regular codes, or Hamming subcube packings; the full bibliography of older work may contain further special cases. Scientific verification here is self-review only; no independent audit has been performed.

## References
[1] D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, “On \(k\)-limited domination in graphs,” arXiv:2606.22422v1 (first posted 21 June 2026). https://arxiv.org/abs/2606.22422

[2] A. Tepeh, “On \(k\)-limited domination: complexity and Cartesian products,” arXiv:2606.22428v1 (first posted 21 June 2026; v2 1 October 2026), especially Theorem 7, Proposition 6, and the hypercube discussion. https://arxiv.org/html/2606.22428v2

[3] M. Kwaśnik and M. Perl, “Nearly perfect sets in products of graphs,” *Opuscula Mathematica* 24(2) (2004), 177–180, especially Proposition 1 and Theorem 1. https://www.opuscula.agh.edu.pl/vol24/2/art/opuscula_math_2415.pdf

[4] E. A. Bespalov, D. S. Krotov, A. A. Matiushev, A. A. Taranenko and K. V. Vorob'ev, “Perfect 2-colorings of Hamming graphs,” *Journal of Combinatorial Designs* 29(6) (2021), 367–396, arXiv:1911.13151. https://arxiv.org/pdf/1911.13151

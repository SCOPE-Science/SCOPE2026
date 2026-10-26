# The first seven-vertex branching probe needed to distinguish finite trees from walk profiles

## Finding
For finite simple undirected trees, define the **path profile**
\[
W(T)=(\mathbf 1^{\mathsf T}A_T^k\mathbf 1)_{k\ge 0},
\]
and let \(\operatorname{hom}(F,T)\) count edge-preserving vertex maps from a connected source tree \(F\) to \(T\). Let \(S(a,b,c)\) be the tree formed by identifying one endpoint of three disjoint paths of respective positive edge lengths \(a,b,c\).

**Theorem (sharp bounded-source threshold through fourteen target vertices).**

1. On all unlabelled target trees of order at most thirteen, the combined invariant \((W(T),\operatorname{hom}(S(1,1,3),T))\) distinguishes isomorphism classes. Replacing \(S(1,1,3)\) by \(S(1,2,2)\) also works. No fixed source tree of order at most five can do so, even when all path counts are also supplied.
2. On all unlabelled target trees of order at most fourteen, the combined invariant \((W(T),\operatorname{hom}(S(1,1,4),T))\) distinguishes isomorphism classes. Replacing \(S(1,1,4)\) by \(S(1,2,3)\) also works. These are precisely the two seven-vertex source-tree isomorphism types with this property. No source tree of order at most six can do so, even when all path counts are supplied; in fact, an explicit nonisomorphic fourteen-vertex pair has identical counts from **every** tree source of order at most six.
3. The path profiles alone have no collision through eleven vertices, one colliding pair at order twelve, two at thirteen, and six at fourteen. Among these nine pairs the least order of a separating connected tree source is six for eight pairs and seven for exactly one pair (at target order fourteen).

The new information is the sharp source-pattern requirement and the thirteen-to-fourteen threshold, not the previously observed first twelve-vertex walk-profile collision.

## Assumptions and scope
All graphs are finite, simple, loopless, undirected and unlabelled up to graph isomorphism. A graph homomorphism preserves edges but need not be injective. Paths of arbitrary finite length are allowed in \(W(T)\), including the one-vertex path. Every additional probe is one fixed connected, unrooted source tree. A source tree of order seven has six edges; the parameters in \(S(a,b,c)\) count edges, so \(|V(S(a,b,c))|=a+b+c+1\). Different target orders are separated by the first entry of \(W(T)\).

At target order fourteen, the unique pair remaining after all tree sources of order at most six and all paths is represented on vertices \(0,\ldots,13\) by the following edge lists:

\[
\begin{aligned}
E(T_A)={}&\{01,12,13,34,3\,10,45,56,59,67,68,8\,12,10\,11,12\,13\},\\
E(T_B)={}&\{01,06,12,13,25,34,37,6\,13,78,89,8\,10,10\,11,10\,12\}.
\end{aligned}
\]

Here an item such as \(3\,10\) denotes the unordered edge joining vertices \(3\) and \(10\), not a numerical product. The exact machine-readable edge pairs occur in the verifier output. Both trees have degree multiset consisting of six ones, four twos and four threes.

For the two seven-vertex probes, the values on this pair are
\[
\begin{array}{c|cc}
F&\operatorname{hom}(F,T_A)&\operatorname{hom}(F,T_B)\\\hline
S(1,1,4)&1506&1504\\
S(1,2,3)&1472&1473
\end{array}.
\]
These counts are not induced-subtree counts. They count all edge-preserving maps, including maps identifying nonadjacent source vertices.

## Proof
**Finite horizon for the path profile.** For an \(n\)-vertex tree, the scalar sequence \(w_k=\mathbf 1^{\mathsf T}A^k\mathbf 1\) obeys a linear recurrence of order at most \(n\), by Cayley–Hamilton. For two such trees of the same order, the difference sequence is annihilated by the product of their two characteristic polynomials, hence obeys a recurrence of order at most \(2n\). Equality for \(k=0,\ldots,2n-1\) therefore implies equality for all nonnegative \(k\). Consequently the recorded signatures test infinite path profiles exactly, not merely at a truncated set of queries.

**Complete finite target census.** Begin with the one-vertex tree. From every representative of every \((n-1)\)-vertex free-tree isomorphism type, attach one new leaf at every possible vertex; deduplicate the results by a canonical center-rooted code. For a tree with a unique center, the code sorts recursively encoded branches there; for a tree with two adjacent centers, it sorts the two recursively encoded halves. This code is complete for free-tree isomorphism, as follows inductively from the canonical center and the multisets of its rooted branches. Any tree with at least two vertices has a leaf whose deletion yields a smaller tree, so the generation is exhaustive by induction. The counts for successive orders through fourteen are
\[
1,1,1,2,3,6,11,23,47,106,235,551,1301,3159,
\]
for a total of \(5447\) free trees. An unrelated generator independently produced the same totals.

**Complete finite source census.** For a rooted source tree, put
\[
q_v(x)=\prod_{u\text{ child of }v}\left(\sum_{y\sim x}q_u(y)\right),
\qquad
\operatorname{hom}(F,T)=\sum_{x\in V(T)}q_r(x),
\]
with each empty product equal to one. This recursion counts every graph homomorphism exactly by conditioning on the image of a source vertex. Exhaustively enumerating the one, one, one, two, three, six and eleven unlabelled source trees of orders one through seven and applying this recurrence to each of the walk-profile collision pairs gives the pair multiplicities in the theorem. In particular, at target order fourteen, five pairs have a least witness of six vertices and one pair has a least witness of seven vertices. All sources through six agree on the displayed exceptional pair, whereas two seven-vertex spiders distinguish it.

**A single probe suffices.** For each of the two stated six-vertex spider probes, the combined path/profile value is injective on each target-order class through thirteen. For each of the two stated seven-vertex spiders it is injective through fourteen. Testing all eleven seven-vertex source-tree types shows that the other nine each leave at least one pair unresolved. The existence of the exceptional pair excludes every source of order six or less from solving the fourteen-vertex problem, establishing sharpness.

There is also a direct moment interpretation of the displayed positive witness. If \(d=A\mathbf1\) and \(u_j=A^j\mathbf1\), then
\[
\operatorname{hom}(S(1,1,4),T)=\sum_v d(v)^2u_4(v),\qquad
\operatorname{hom}(S(1,2,3),T)=\sum_v d(v)u_2(v)u_3(v).
\]
Thus the first new source level detects nonlinear correlations of local walk counts absent from all total walk counts and all smaller tree-pattern counts.

## Verification
Run \(\texttt{python3 artifacts/verify.py}\) from the directory containing the embedded files. It uses only the Python standard library, generates all \(5447\) target free trees and all relevant source free trees, checks both profile signatures and every bounded-source comparison, verifies both exceptional witness counts, and checks the stated uniqueness of the successful seven-vertex probes. The recorded expected output is \(\texttt{artifacts/verification_output.txt}\). A distinct enumerator based on NetworkX, with independent profile/count implementations, is \(\texttt{artifacts/independent_check.py}\); its expected output is \(\texttt{artifacts/independent_output.txt}\). This secondary check requires NetworkX version 3 or later.

All equality claims about all path lengths use the proved recurrence bound, not inference from a numerical sample. All sources through the claimed finite size are enumerated, rather than selected heuristically.

## Relationship to prior work
Dell, Grohe and Rattan (arXiv:1802.08876, 2018) prove that equality of all tree-source homomorphism counts is equivalent to fractional isomorphism, and study the strictly weaker path-source profile through its linear-algebraic characterization. Their global equivalences do not specify the smallest distinguishing source pattern on free-tree targets of order at most fourteen. Neuen (arXiv:2304.07011, 2023) develops homomorphism-distinguishing closedness for bounded-treewidth source classes; it is not a finite host-order/source-size census.

An earlier finite tree census established the first twelve-vertex ambiguity under generalized spectrum and another prior finite study recorded the corresponding first walk-profile collision. Those observations supply background/overlap constraints but do not determine the thirteen-vertex success and fourteen-vertex obstruction for a single six-vertex tree probe, nor the exact two successful seven-vertex probes. The present statement is strictly about the new **probe-size hierarchy** with all paths held fixed.

## Limitations
The classification is proved only for host trees with at most fourteen vertices, and does not claim any single bounded source probe resolves all trees of arbitrary order. The computation is exhaustive within its finite scope but not an asymptotic theorem about witness size. Historical priority remains subject to the possibility of an unlocated census or a published implication that supplies these exact finite thresholds. Self-review is not an independent scientific audit.

## References
1. H. Dell, M. Grohe, G. Rattan, *Lovász Meets Weisfeiler and Leman*, arXiv:1802.08876, first public version February 24, 2018. https://arxiv.org/abs/1802.08876
2. D. Neuen, *Homomorphism-Distinguishing Closedness for Graphs of Bounded Tree-Width*, arXiv:2304.07011, first public version April 14, 2023. https://arxiv.org/abs/2304.07011
3. A. Atserias, P. G. Kolaitis, W.-L. Wu, *On the Expressive Power of Homomorphism Counts*, arXiv:2101.12733, January 29, 2021. https://arxiv.org/abs/2101.12733

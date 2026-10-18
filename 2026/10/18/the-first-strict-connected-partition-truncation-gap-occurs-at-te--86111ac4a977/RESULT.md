# The first strict connected-partition truncation gap occurs at ten vertices

## Finding
Let \(\mathcal T_k\) be the set of isomorphism classes of simple, unrooted trees on \(k\) vertices. For an edge subset \(F\subseteq E(T)\), let \(\mu_T(F)\) be the integer partition of \(k\) consisting of the component orders of \((V(T),F)\). Define
\[
N_\mu(T)=\#\{F\subseteq E(T):\mu_T(F)=\mu\},\qquad
\sigma_t(T)=(N_\mu(T):k-\ell(\mu)\le t),
\]
where \(\ell(\mu)\) is the number of parts. Thus \(\sigma_t\) counts spanning-forest types using at most \(t\) edges. Let \(\tau(k)\) be the least \(t\) for which \(\sigma_t\) distinguishes every pair of nonisomorphic trees in \(\mathcal T_k\), with value infinity if no such \(t\) exists.

**Theorem.** The lower bound for this exact reconstruction invariant is attained for every \(4\le k\le9\), but first becomes strict at order ten:
\[
\tau(k)=\left\lfloor\frac{k}{2}\right\rfloor\quad(4\le k\le9),
\qquad\boxed{\tau(10)=6>5=\left\lfloor\frac{10}{2}\right\rfloor}.
\]
Moreover, among the \(106\) unrooted trees of order \(10\), exactly one unordered pair has identical \(\sigma_5\) vectors, and every pair is separated by \(\sigma_6\).

Here is an explicit representative of the unique indistinguishable pair at rank five. Vertices are \(\{0,1,\ldots,9\}\), and ordered pairs denote undirected edges:
\[
\begin{aligned}
E(T_A)&=\{(0,1),(1,2),(2,3),(3,4),(4,5),(4,8),(5,6),(5,7),(8,9)\},\\
E(T_B)&=\{(0,1),(1,2),(2,3),(3,4),(3,9),(4,5),(4,8),(5,6),(6,7)\}.
\end{aligned}
\]
The trees are nonisomorphic: their diameters are \(6\) and \(7\), respectively. Both have the same count of every spanning-forest component type with at most five edges. They are first separated by six-edge forests: the component-order partition \((4,2,2,2)\) occurs once in \(T_A\) and never in \(T_B\). In \(T_A\) its four components have vertex sets \(\{0,1\}\), \(\{2,3\}\), \(\{4,5,6,7\}\), and \(\{8,9\}\).

## Assumptions and scope
All graph objects are finite, simple, undirected trees, taken up to isomorphism. The counting invariant includes **all** integer partitions \(\mu\) of \(k\) with \(k-\ell(\mu)\le t\), including multiplicities. The theorem concerns orders \(4\) through \(10\) only. A statement that \(\sigma_t\) distinguishes trees refers to injectivity on the *entire* finite set \(\mathcal T_k\), not only on selected subfamilies.

## Proof
First enumerate all rooted unlabeled trees without omissions. Encode a rooted tree as a balanced-parenthesis word: \(\texttt{(}\) followed by the child-rooted codes in lexicographically sorted order and then \(\texttt{)}\). For order \(k\), enumerate every multiset of previously constructed rooted trees with total order \(k-1\). This is exhaustive because removing the root of any rooted tree produces exactly such a multiset, and two rooted trees have equal codes precisely when they are root-preservingly isomorphic.

Next pass from rooted to unrooted trees by their centers. Every tree has either a unique center vertex or a unique center edge. Encode a one-center tree by its rooted code at that center; encode a two-center tree by the sorted pair of rooted codes obtained after cutting the central edge. These descriptions are isomorphism invariants and distinguish nonisomorphic unrooted trees. Taking one representative for each resulting code therefore gives precisely \(\mathcal T_k\), not a sample. The obtained numbers of rooted trees for orders \(1\) through \(10\) are \(1,1,2,4,9,20,48,115,286,719\). The numbers of unrooted trees for orders \(4\) through \(10\) are \(2,3,6,11,23,47,106\).

For every representative \(T\), enumerate each of its \(2^{k-1}\) edge subsets \(F\). The connected-component orders of \((V(T),F)\) give \(\mu_T(F)\), and \(k-\ell(\mu_T(F))=|F|\) because every spanning subgraph of a tree is a forest. This determines each integer \(N_\mu(T)\) exactly. A second implementation derives the components by graph traversal rather than by disjoint-set union; it agrees on every tested edge subset and count. Group the resulting vectors by equality of the first \(t+1\) rank layers. If a group has \(r\) representatives, it contributes \(\binom r2\) indistinguishable unordered pairs.

The complete table relevant to the first gap is

| \(k\) | \(|\mathcal T_k|\) | \(b=\lfloor k/2\rfloor\) | Pairs equal at rank \(b-1\) | Pairs equal at rank \(b\) | \(\tau(k)\) |
|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 2 | 1 | 0 | 2 |
| 5 | 3 | 2 | 3 | 0 | 2 |
| 6 | 6 | 3 | 1 | 0 | 3 |
| 7 | 11 | 3 | 5 | 0 | 3 |
| 8 | 23 | 4 | 2 | 0 | 4 |
| 9 | 47 | 4 | 10 | 0 | 4 |
| 10 | 106 | 5 | 3 | 1 | 6 |

The rank-six comparison at order ten has zero indistinguishable pairs. Since the vectors are nested as \(t\) increases, any collision at rank \(t\) persists at all smaller ranks. The table proves each minimum value and establishes order ten as the first strict departure from \(\lfloor k/2\rfloor\). The unique rank-five collision has the edge representatives above; its rank-six discrepancy follows from direct counting of the displayed forest type. The exhaustive canonical enumeration certifies that there are no other collisions. \(\square\)

## Verification
Run `python3 verify.py` with Python's standard library. The program independently enumerates all unlabeled rooted trees by recursive child multisets, deduplicates unrooted trees using center encodings, counts every edge-subset component partition using both disjoint-set union and component traversal, and compares complete prefix profiles. It asserts the rooted and unrooted counts, all equalities between the two counting methods, the rank-five unique pair, and its rank-six separation. Exact integer output is saved as `verification_output.txt`. The computation uses no floating-point tolerance, random trials, or external graph-enumeration package.

## Relationship to prior work
Awan, *First-Derivative Chromatic Symmetric Reconstruction For Proper Trees* (2026), Section 4 and Theorem 3, introduced the precise rank-truncated connected-partition reconstruction parameter and proved \(\tau(k)\ge\lfloor k/2\rfloor\) for \(k\ge4\), with the example \(\tau(5)=2\). Its inspected full text does not give the first strict order or the \(106\)-tree rank-five collision classification. The current finite result determines that exact boundary rather than strengthening the universal lower bound.

Zeng, *Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees* (2026), derives reconstruction criteria from full chromatic-symmetric-function data and provides cut-partition computations for diameter-six trees. It does not establish the minimal truncation rank for the complete class of ten-vertex trees. The distinction is important: reconstruction from the *entire* invariant does not imply reconstruction from layers of at most five selected edges.

## Limitations
The theorem makes no claim about \(\tau(k)\) for \(k\ge11\) and neither confirms nor refutes tree reconstruction from the full chromatic symmetric function in arbitrary order. It is a complete finite census with a mathematically exhaustive generator, not a general infinite-order classification. Its originality is subject to the possibility of equivalent numerical data in literature or supplementary material not identified by the targeted searches.

## References
1. S. A. Awan, *First-Derivative Chromatic Symmetric Reconstruction For Proper Trees*, arXiv:2609.13464, first posted 2026-09-11, especially Theorem 3 and Section 4. https://arxiv.org/pdf/2609.13464
2. Z. Zeng, *Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees*, arXiv:2608.18179, first posted 2026-08-18, especially Sections 3–5. https://arxiv.org/pdf/2608.18179
3. R. P. Stanley, *A symmetric function generalization of the chromatic polynomial of a graph*, Advances in Mathematics 111 (1995), 166–194, cited for the power-sum component-partition expansion.

# Zero-forcing polynomials of complements of trees from leaf twins and five-vertex paths

## Finding
Let \(T\) be any finite simple tree with \(n\geq 5\) vertices. Write \(d_v=\deg_T(v)\), and let \(\ell_v\) be the number of leaves of \(T\) adjacent to \(v\). Let \(p_5(T)\) be the number of unoriented simple paths with exactly four edges (five distinct vertices). Define
\[
 b_T=\binom{n}{2}-\sum_{v\in V(T)}\binom{\ell_v}{2},
\qquad
 a_T=\sum_{v\in V(T)}\left(\binom{d_v}{2}-\binom{\ell_v}{2}\right)(n-1-d_v)-p_5(T).
\]
If \(T\) is not a star, its ordinary zero-forcing polynomial is exactly
\[
 \boxed{\mathcal Z(\overline T;x)=a_Tx^{n-3}+b_Tx^{n-2}+nx^{n-1}+x^n.}
\]
If \(T=K_{1,n-1}\), then
\[
 \boxed{\mathcal Z(\overline T;x)=(n-1)x^{n-1}+x^n.}
\]
In particular, all coefficients can be evaluated using \(O(n)\) integer-arithmetic operations from an adjacency-list representation of \(T\). For a nonstar, the minimum zero-forcing sets have exactly \(n-3\) vertices and their precise number is \(a_T\). The formula refines the previously known minimum cardinality, rather than proposing a new minimum zero-forcing number.

## Assumptions and scope
All graphs are finite, simple, undirected, unweighted. The complement \(\overline T\) has the same vertex set as \(T\), and distinct vertices are adjacent in \(\overline T\) exactly when they are nonadjacent in \(T\). Starting from a blue set \(B\), the ordinary zero-forcing rule permits a blue vertex with exactly one white neighbor to color that neighbor blue. A set is zero forcing if some finite sequence of such moves colors all vertices. The polynomial \(\mathcal Z(G;x)=\sum_{B\subseteq V(G),\, B\text{ zero forcing}} x^{|B|}\) includes the all-blue set and does not count unsuccessful starting sets. Trees have order \(n\ge5\); no claim is made here for disconnected forests or smaller orders.

The path count can be evaluated without enumerating paths:
\[
 p_5(T)=\sum_{b\in V(T)}\ \sum_{\{u,w\}\subseteq N_T(b)}(d_u-1)(d_w-1).
\]
The two endpoints of a path have no imposed degree restrictions; this formula counts each unoriented length-four path exactly once by its central vertex \(b\).

## Proof
**Step 1: the possible number of initially white vertices.** Suppose \(W\) is the initially white set and \(|W|\ge4\). If a first force in \(\overline T\) is possible, some blue vertex \(v\) is adjacent in \(T\) to all but one of the vertices of \(W\). After that force, the remaining white set \(U\subseteq N_T(v)\) has \(|U|=|W|-1\ge3\). A second blue vertex \(y\ne v\) is adjacent in \(T\) to at most one vertex of \(U\), because two such common neighbors with \(v\) would create a cycle in \(T\). Thus \(y\) has at least \(|U|-1\ge2\) white neighbors in \(\overline T\). Vertex \(v\) has none. No further force is possible. Therefore a zero-forcing set omits at most three vertices.

**Step 2: zero or one white vertex.** Every all-blue set succeeds. If \(T\) is not a star, no vertex is universal in \(T\), so \(\overline T\) has no isolated vertices. Hence every choice of just one white vertex can be forced by a blue neighbor, giving coefficients \(1\) and \(n\) in the two highest degrees.

**Step 3: exactly two white vertices.** Let \(W=\{u,w\}\). A first force is possible if and only if an outside vertex is adjacent in \(T\) to exactly one of \(u,w\), because this is equivalent to having exactly one white neighbor in \(\overline T\). When such a force occurs, the last white vertex is forceable by Step 2. Thus the only failed pairs have equal neighborhoods outside the pair in \(T\). In a connected tree of order at least five, such pairs are exactly pairs of leaves with the same neighbor: if the equal external neighborhood contained two vertices there would be a cycle, and if it were empty the entire tree would consist of the selected pair. Conversely, sibling leaves have the same adjacency to every outside vertex and cannot be individually forced. Each bad pair has a unique common neighbor, and hence the number of successful pairs is \(b_T\).

**Step 4: exactly three white vertices.** Let \(W=\{u,w,t\}\). A first force by a blue vertex \(v\) is possible exactly when the two vertices it does not see in \(\overline T\), say \(u,w\), are neighbors of \(v\) in \(T\), while \(t\) is not. The first force colors \(t\); the remaining white pair is \(\{u,w\}\). By Step 3, this continuation succeeds precisely when \(u,w\) are not both leaves with common neighbor \(v\). If at least one of \(u,w\) is not a leaf, it has a neighbor other than \(v\), and that blue vertex distinguishes \(u\) from \(w\) in \(\overline T\), since a tree cannot contain a cycle. This proves necessity and sufficiency of a **valid witness** \(v\): select two of its neighbors, not both leaves, plus a third vertex outside its closed tree neighborhood.

For fixed \(v\), the number of such triples is
\[
 \left(\binom{d_v}{2}-\binom{\ell_v}{2}\right)(n-1-d_v).
\]
A triple cannot have two distinct witness centers for the same selected pair, since that would give a four-cycle. If it has two witness centers using distinct pairs, their union is a unique simple five-vertex path \(a-v-b-w-c\) with selected vertices \(\{a,b,c\}\), and conversely every such path supplies two distinct valid witnesses. Three witnesses would form a cycle by subdividing the edges of a triangle on the three selected vertices, so no triple has more than two valid witnesses. Subtracting one for each five-vertex path gives the exact distinct triple count \(a_T\). Combining Steps 1–4 establishes the polynomial for nonstars.

**Step 5: stars.** If \(T=K_{1,n-1}\), its complement is \(K_{n-1}\) together with an isolated vertex. Every zero-forcing set must include the isolated vertex and all but at most one vertex of the clique. There are \(n-1\) minimum sets and one all-blue set, giving the second formula.

**Step 6: linear evaluation.** The degrees and the leaf-neighbor counts take \(O(n)\) operations. For each vertex \(b\), put \(s_b=\sum_{u\in N_T(b)}(d_u-1)\) and \(t_b=\sum_{u\in N_T(b)}(d_u-1)^2\). Then its contribution to \(p_5(T)\) is \((s_b^2-t_b)/2\). Each tree edge contributes to two such neighbor sums, so \(p_5(T)\), \(a_T\), and \(b_T\) are computable in \(O(n)\) arithmetic operations. This is an arithmetic-operation bound, not a bit-complexity claim.

## Verification
The included standalone Python 3 program `verify.py` implements forcing directly on the complement of each input tree and independently calculates the displayed coefficient formulas from degree and leaf counts. It exhaustively examines **every labeled tree on each of 5, 6, and 7 vertices** using Prüfer sequences, and for each tests all initial white subsets of sizes zero through four. It also tests seeded generated trees for orders 8 through 26 and every star in the stated range. Running `python3 verify.py` produces the included `verify_output.txt`, ending in `VERIFY_OK trees= 20110 white-subsets= 3134704`. These finite checks are corroboration; the steps above prove the theorem for all \(n\ge5\).

The coefficients also detect branching arrangement beyond the degree sequence. The spiders with arm lengths \((1,1,3)\) and \((1,2,2)\) both have tree-degree multiset \((3,2,2,1,1,1)\), but their complement polynomials are, respectively,
\[
 8x^3+14x^4+6x^5+x^6,
 \qquad 11x^3+15x^4+6x^5+x^6.
\]

## Relationship to prior work
Boyer et al. introduced and studied the ordinary zero-forcing polynomial, including several exact graph-family enumerations and structural constraints. Curl et al. proved that the zero forcing number of a nonstar tree complement is \(n-3\) and that of a star complement is \(n-1\). Those previously established scalar results are respected. The new assertion here is the entire coefficient distribution for the complements of **all** trees of order at least five, including the sibling-leaf correction, the nonovercounting five-vertex-path term, and linear-time computation. Work on coefficient comparisons of \(\mathcal Z(T;x)\) for trees concerns \(T\), not generally \(\overline T\), and is not a source of the asserted formula by graph complementation.

## Limitations
The theorem concerns ordinary zero forcing only, not skew or positive-semidefinite variants. It assumes a tree of order at least five. The polynomial is not claimed to distinguish all tree isomorphism types, nor is an exhaustive literature novelty certificate claimed. A formula might be equivalent to an enumeration under different terminology. The supporting finite verification does not establish an infinite theorem on its own.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910, first posted 2018-01-26. https://arxiv.org/abs/1801.08910
2. E. Curl, S. Fallat, R. Moruzzi Jr., C. Reinhart, D. Young, *On the zero forcing number of the complement of graphs with forbidden subgraphs*, arXiv:2206.03932, first posted 2022-06-08. https://arxiv.org/abs/2206.03932

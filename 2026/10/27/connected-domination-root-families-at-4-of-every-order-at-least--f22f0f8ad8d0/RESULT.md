# Connected domination-root families at \(-4\) of every order at least 35 and arbitrary multiplicity

## Finding
For any integers \(k\geq1\) and \(a,b\geq0\), there exists a connected simple graph \(H_{k,a,b}\) on exactly \(33k+2a+3b\) vertices whose ordinary domination polynomial is
\[
D(H_{k,a,b};z)=D(G_{33};z)^k\,[z(z+2)]^a\,[z(z^2+3z+1)]^b.
\]
Here \(G_{33}\) is the explicit graph in Alikhani–Griswold (2026); \(-4\) is a zero of the displayed polynomial of **exact multiplicity \(k\)**. Thus every order \(n\geq35\), as well as \(n=33\), admits a connected graph with a domination root at \(-4\). For any prescribed positive \(k\), the same holds with multiplicity exactly \(k\) at order \(33k\) and every order at least \(33k+2\).

## Assumptions and scope
All graphs here are finite, undirected and simple. A subset \(S\subseteq V(G)\) is dominating if \(N_G[S]=V(G)\), and \(D(G;z)=\sum_{S\text{ dominating}}z^{|S|}\). A *support vertex* is a vertex adjacent to a leaf, which means a degree-one vertex. In \(G_{33}\), take vertex \(4\), adjacent to leaf \(5\), using the labels and full edge list in the cited 2026 paper. In \(K_2\), take either vertex. In \(P_3\), take its middle vertex. Make \(k+a+b\) mutually disjoint blocks and choose any tree on the blocks. For each tree edge, insert precisely one graph edge between the two designated support vertices. No vertices are identified. This defines \(H_{k,a,b}\), including the single-block case.

## Proof
**Support-bridge factorization.** Let \(G_1,\dots,G_t\) be graphs with a designated support vertex \(u_i\) and a leaf \(w_i\) adjacent to it. Insert any edges only between the designated support vertices, with no identification of vertices. For any dominating set \(S\) of the resulting graph, the leaf \(w_i\) forces \(u_i\in S\) or \(w_i\in S\). Consequently \(u_i\) is already dominated by \(S\cap V(G_i)\). Every other vertex of \(G_i\) has no neighbors outside \(G_i\), so it must also be dominated internally. Hence \(S\cap V(G_i)\) dominates \(G_i\). Conversely, any union of individually dominating subsets is dominating after inserting the new edges. The correspondence preserves cardinality, so
\[
D(G;z)=\prod_{i=1}^{t}D(G_i;z).
\]
The factorization holds even when a designated vertex has several new external edges.

**Construction.** Each block has its required support vertex. Join the blocks along a tree as defined above. The graph is connected and simple; the bridge-factorization identity applies. For a two-vertex edge, its nonempty subsets are exactly its dominating sets, hence \(D(K_2;z)=2z+z^2=z(z+2)\). For the three-vertex path, the single dominating singleton is the middle vertex, all three pairs and the triple dominate, so \(D(P_3;z)=z+3z^2+z^3=z(z^2+3z+1)\). Thus the polynomial identity follows.

Alikhani–Griswold (2026, Theorem 2.1 and Corollary 2.2) give
\[
D(G_{33};z)=z^{11}(z+2)(z+4)(z^2+3z+1)Q_{18}(z),
\]
where \(Q_{18}(-4)\ne0\). In fact, their exact coefficient data yield \(D'(G_{33};-4)=1{,}100{,}417{,}597{,}440{,}000\ne0\), which is independently checked in the attached verifier. The extra factors at \(z=-4\) have respective values \(8\) and \(-20\), both nonzero. Therefore the multiplicity at \(-4\) is precisely \(k\).

Finally, every integer \(m\geq2\) can be written \(2a+3b\) with nonnegative integers \(a,b\): if \(m\) is even, use only twos; if odd, use one three and the remainder in twos. Taking \(k=1\) proves the all-order statement, and leaving \(k\) arbitrary proves the multiplicity refinement.

## Verification
The standalone standard-library program `verify.py` reconstructs the 36-edge, 33-vertex source graph, evaluates the weighted dominating-set formula exactly using variable elimination, and compares its results at 34 distinct integer arguments against every coefficient reported in the 2026 primary paper. Both sides have degree at most 33, so agreement at 34 distinct values proves equality of the two polynomials, not merely a numerical sample. The program checks the simple zero at \(-4\) and a direct five-vertex support-bridge example. The general support-bridge lemma above is a direct bijective proof; finite computations are not used to prove its all-order quantifiers.

## Relationship to prior work
The 33-vertex graph and its simple root at \(-4\) are **not new** (Alikhani–Griswold, arXiv:2608.00109v1, public 31 July 2026). That paper specifically raises the question of infinite graph families sharing this root; disconnected unions make its literal unrestricted formulation straightforward. The claim here is the stronger **connected, every-sufficiently-large-order and exact-multiplicity** conclusion. The key bridge mechanism is a special case of the pre-existing irrelevant-edge/ domination-covered theory of Kotek et al. (2012, Theorems 3.10–3.11). The present claim combines these known ingredients to obtain the precise connected-family conclusions; it does **not** assert originality of either constituent result or of the underlying irrelevant-edge principle. No inspected source stated or implied the exact combined connected all-order/multiplicity formulation for the post-2026 root example.

## Limitations
These are existence constructions; no minimal connected order is established, no classification of all \(-4\)-rooted graphs is attempted, and no other negative integer roots are constructed. The mechanism is elementary once the known seed and known irrelevant-edge theorem are supplied. Its originality rests only on the explicit connected all-order and multiplicity synthesis, and broader historical priority may be incomplete.

## References
1. S. Alikhani and M. Griswold, *On the Integer Domination Root Conjecture*, arXiv:2608.00109v1 (public 31 July 2026), https://arxiv.org/html/2608.00109v1 .
2. T. Kotek, J. Preen, F. Simon, P. Tittmann, M. Trinks, *Recurrence Relations and Splitting Formulas for the Domination Polynomial*, Electron. J. Combin. 19(3) (2012), P47, https://doi.org/10.37236/2475 .

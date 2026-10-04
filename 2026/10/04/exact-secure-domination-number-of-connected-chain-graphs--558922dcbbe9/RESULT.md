# Exact secure domination number of connected chain graphs

## Finding
Let \(G=(A\cup B,E)\) be a finite connected chain graph. A set \(D\subseteq V(G)\) is a secure dominating set if it dominates \(G\) and, for every \(u\notin D\), some \(v\in D\cap N(u)\) has the property that \((D\setminus\{v\})\cup\{u\}\) is again dominating.

Let \(L_A\subseteq A\) and \(L_B\subseteq B\) be the leaf sets in the two bipartition classes, and put
\[
e_A=\max\{|L_A|-1,0\},\qquad e_B=\max\{|L_B|-1,0\}.
\]
Then
\[
\boxed{\gamma_s(G)=e_A+e_B+\min\{4,\ |A|-e_A,\ |B|-e_B\}.}
\]
Thus secure domination on connected chain graphs is determined by the two side sizes and the excess multiplicities in the two possible leaf-twin classes.

## Assumptions and scope
A connected chain graph admits nonempty twin blocks \(A_1,\ldots,A_p,B_1,\ldots,B_p\) such that
\[
N(a)=B_1\cup\cdots\cup B_i\quad(a\in A_i),\qquad
N(b)=A_j\cup\cdots\cup A_p\quad(b\in B_j).
\]
Consequently, the only possible leaves in \(A\) are all vertices of \(A_1\), and this happens exactly when \(|B_1|=1\); symmetrically, the only possible leaves in \(B\) are all vertices of \(B_p\), and this happens exactly when \(|A_p|=1\). The theorem includes stars, complete bipartite graphs, half graphs, and the two-vertex graph.

## Proof
First use a leaf-twin reduction. Suppose \(t\ge2\) leaves have the same support vertex \(s\). Every secure dominating set contains at least \(t-1\) of those leaves: if two such leaves were outside the set, then their only possible defender would be \(s\), and after moving the guard at \(s\) to one leaf the other leaf would be undominated. Conversely, delete \(t-1\) of the twin leaves while retaining one representative. From any secure dominating set in the original graph, retain the unique omitted leaf when one exists, and otherwise retain any selected leaf. Removing the other \(t-1\) selected twins preserves every defense: a deleted leaf can defend only \(s\), and the retained twin can play the same role. In the other direction, adjoining the deleted leaves to a secure dominating set of the reduced graph cannot destroy any defense. Therefore deleting \(t-1\) equal leaves decreases \(\gamma_s\) by exactly \(t-1\).

Apply this reduction to the leaf classes on both sides. The resulting connected chain graph \(H=(X\cup Y,E)\) has at most one leaf in each bipartition class, with
\[
|X|=|A|-e_A,\qquad |Y|=|B|-e_B,
\]
and
\[
\gamma_s(G)=e_A+e_B+\gamma_s(H).
\]
It remains to prove \(\gamma_s(H)=\min\{4,|X|,|Y|\}\).

For the lower bound, the following holds for every bipartite graph with sides \(X,Y\):
\[
\gamma_s(H)\ge \min\{4,|X|,|Y|\}.
\]
Indeed, suppose a secure dominating set \(D\) had \(|D|\le3\) while both \(|X|>|D|\) and \(|Y|>|D|\). There are outside vertices on both sides, so domination forces \(D\) to meet both sides. Since \(|D|\le3\), one side contributes exactly one selected vertex. Choose an outside vertex on the opposite side. Its defender must be that unique selected vertex; after the swap, all selected vertices lie in one bipartition class. Such a set dominates only if it contains that entire class, contradicting that the class has more than \(|D|\) vertices.

For the upper bound, first observe that \(X\) itself is a secure dominating set whenever \(Y\) contains at most one leaf. If \(y\in Y\) is a leaf, its support can defend it because no other vertex of \(Y\) is a leaf. If \(y\) has degree at least two, choose a neighbor that is not the support of the possible unique leaf of \(Y\); after moving that guard to \(y\), every other vertex of \(Y\) still has a selected neighbor. Hence \(\gamma_s(H)\le |X|\), and symmetrically \(\gamma_s(H)\le|Y|\).

Finally suppose \(|X|,|Y|\ge4\). Order the individual vertices so that
\[
N(x_1)\subseteq\cdots\subseteq N(x_m),\qquad
N(y_1)\supseteq\cdots\supseteq N(y_n).
\]
Connectedness makes \(x_m\) universal to \(Y\) and \(y_1\) universal to \(X\). Consider
\[
S=\{x_{m-1},x_m,y_1,y_2\}.
\]
It dominates \(H\). For an outside \(x\in X\), if \(x\) is adjacent to \(y_2\), then \(y_2\) defends \(x\), while \(y_1\) and \(x_m\) remain universal to their opposite sides. If \(x\) is not adjacent to \(y_2\), nesting shows that \(x\) is adjacent only to \(y_1\), hence is the unique possible leaf in \(X\); then \(y_1\) defends \(x\), because every other vertex of \(X\) is adjacent to \(y_2\). The argument for outside vertices of \(Y\) is symmetric, using \(x_{m-1}\) and \(x_m\). Thus \(S\) is secure and \(\gamma_s(H)\le4\). The lower and upper bounds coincide, proving the formula.

## Verification
The accompanying `verify.py` independently constructs every canonical connected chain-graph block profile of total order at most \(10\), exactly tests the secure condition for vertex subsets, computes \(\gamma_s\) by exhaustive search, and compares it with the formula. It also checks the leaf-twin reduction numerically on every profile and explicitly verifies the three-by-three half graph \(H_3\). Its replay output is:

`VERIFY_OK profiles=511 twin_reduction_checks=511 secure_subset_checks=178382 swap_checks=88263 max_order=10 h3_gamma=3`

The computation is supplementary finite evidence; the theorem for arbitrary order is established by the proof above.

## Relationship to prior work
Burger, Cockayne, Gründlingh, Mynhardt, van Vuuren, and Winterbach developed finite-order protection from secure domination; the publicly available manuscript copy is dated 11 September 2003 and lists AMS subject classification 05C69. Its abstract treats paths, cycles, multipartite graphs, and graph products, not the chain-graph formula proved here.

A much later same-object source is Swathi D and Sadagopan, arXiv:2512.23989v2. Section 3.3 defines chain graphs and Algorithm 2 initializes four extreme vertices, then adds all but one vertex from each multiple pendant class, and labels the output a minimum secure dominating set. That routine does not imply the present formula in the small-side regime. For the half graph \(H_3\), there are no multiple pendant classes, so the displayed routine returns four vertices, while the whole \(A\)-side is a secure dominating set of size \(3\), and the bipartite lower bound above excludes size \(2\). Thus \(\gamma_s(H_3)=3\). When both reduced sides have size at least four, the four-extreme-vertex construction is consistent with the formula.

Jha's secure-total-domination work on chain graphs concerns a strictly stronger condition requiring the selected set itself to be total dominating, so it does not imply ordinary secure domination. Burger, de Villiers, and van Vuuren's 2016 paper on minimum secure dominating sets supplies a direct 05C69 classification and general small-value structure, not this chain-graph formula.

## Limitations
The theorem gives the minimum cardinality, not a classification or enumerator of every minimum secure dominating set. The finite verifier covers all canonical profiles only through total order \(10\) and is not used as an infinite proof. The closest same-object comparison is a 2025/2026 preprint rather than a peer-reviewed publication; its displayed chain-graph routine is compared at the statement level, with \(H_3\) giving a direct discrepancy in the small-side case.

## References
1. A. P. Burger, E. J. Cockayne, W. R. Gründlingh, C. M. Mynhardt, J. H. van Vuuren, W. Winterbach, *Finite Order Domination in Graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 49, 159–175. Public PDF: `https://combinatorialpress.com/article/jcmcc/Volume%20049/vol-049-paper%2011.pdf`.
2. Swathi D, N. Sadagopan, *Secure Domination in Bisplit graphs -- A Structural and algorithmic study*, arXiv:2512.23989v2, Section 3.3 and Algorithm 2.
3. A. Jha, *Secure total domination in chain graphs and cographs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 826–832, DOI:10.1016/j.akcej.2019.10.005.
4. A. P. Burger, A. P. de Villiers, J. H. van Vuuren, *On minimum secure dominating sets of graphs*, Quaestiones Mathematicae 39 (2016), 189–202, DOI:10.2989/16073606.2015.1068238.

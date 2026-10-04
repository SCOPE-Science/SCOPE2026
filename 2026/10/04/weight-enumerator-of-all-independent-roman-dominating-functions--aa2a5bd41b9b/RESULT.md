# Weight enumerator of all independent Roman dominating functions on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with parts \(V_1,\ldots,V_r\), where \(r\ge2\) and \(n_i=|V_i|\). An independent Roman dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\), while the vertices receiving positive labels form an independent set.

Such a function exists exactly in the following form: choose one part \(V_i\), label every vertex of \(V_i\) by \(1\) or \(2\) with at least one label \(2\), and label every vertex outside \(V_i\) by \(0\). Therefore, for the weight \(w(f)=\sum_{v\in V(G)}f(v)\),
\[
I_R(G;x):=\sum_{f}x^{w(f)}=\sum_{i=1}^r\left((x+x^2)^{n_i}-x^{n_i}\right),
\]
where the sum on the left is over all independent Roman dominating functions.

It follows that
\[
i_R(G)=1+\min_i n_i.
\]
If \(m=\min_i n_i\) and exactly \(c_m\) parts have size \(m\), then there are exactly \(m c_m\) functions of minimum weight. In addition, \(I_R(G;x)\) determines the multiset of part sizes and hence determines the graph up to isomorphism inside the connected complete multipartite class.

## Assumptions and scope
Graphs are finite, simple, and undirected. The result is stated for connected complete multipartite graphs, equivalently \(r\ge2\) with every \(n_i\ge1\). The one-part edgeless case is excluded because its Roman condition behaves differently. The enumerator counts all labelings satisfying the independent Roman conditions, not only minimum-weight labelings.

## Proof
Let \(P=\{v:f(v)>0\}\). Since \(P\) is independent in a complete multipartite graph, all vertices of \(P\) lie in a single part, say \(V_i\). The set \(P\) cannot be empty because every vertex would then be labeled \(0\) and no label \(2\) would exist.

Suppose some vertex of \(V_i\) were labeled \(0\). Every neighbor of that vertex lies outside \(V_i\), but all positive labels lie inside \(V_i\). Hence the zero-labeled vertex would have no neighbor labeled \(2\), contradicting Roman domination. Therefore every vertex of \(V_i\) is positive. All vertices outside \(V_i\) are zero, and since \(r\ge2\), at least one such vertex exists. Each such zero-labeled vertex is adjacent to every vertex of \(V_i\), so the Roman condition is equivalent to requiring at least one label \(2\) in \(V_i\). This proves the classification.

For a fixed part of size \(n_i\), arbitrary labels \(1\) and \(2\) contribute the weight polynomial \((x+x^2)^{n_i}\). The forbidden all-one labeling contributes \(x^{n_i}\), giving the stated summand. The least possible weight from a part of size \(n_i\) is \(n_i+1\), achieved by choosing exactly one vertex labeled \(2\); this gives the minimum and the count of minimum functions.

Finally let \(L=\max_i n_i\). The degree of \(I_R(G;x)\) is \(2L\), and the coefficient of \(x^{2L}\) is exactly the number of parts of size \(L\). Subtracting that many copies of \((x+x^2)^L-x^L\) leaves the enumerator for the smaller parts. Iterating recovers every part-size multiplicity, proving reconstruction.

## Verification
The standalone checker `verify.py` exhaustively enumerates every nondecreasing complete-multipartite profile with at least two parts through order \(9\). For every \((0, 1, 2)\)-labeling it compares the literal neighborhood definition with the structural criterion, compares every enumerator coefficient with the closed formula, checks the minimum and the number of minimum functions, and reconstructs each part-size profile from its polynomial. The replay result is:

`VERIFY_OK profiles=87 labelings=748341 valid_functions=2316 coefficient_checks=1369 min_checks=87 reconstruction_checks=87 max_order=9`

The finite computation is a consistency check; the theorem for arbitrary part sizes follows from the proof above.

## Relationship to prior work
Ebrahimi Targhi', Jafari Rad, Mynhard, and Wu study independent Roman domination through bounds, extremal trees, and Nordhaus--Gaddum inequalities. Their public article page gives publication date 2012-02-29 and the full paper assigns classification 05C69. Jafari Rad's later note improves bounds and contains a complete-bipartite equality characterization for balanced graphs in a restricted degree range. These results concern the minimum parameter or inequalities rather than a classification and weight enumerator of every independent Roman dominating function on arbitrary complete multipartite graphs. A later survey likewise treats independent Roman domination as one Roman variant and records parameter relationships, without supplying this arbitrary-part all-function enumerator.

The novelty claim here is the all-function structural classification, its exact weight enumerator, and the reconstruction consequence. The scalar minimum is included as a corollary and is not relied upon as the originality-bearing component.

## Limitations
The comparison did not locate an earlier source stating the same arbitrary complete-multipartite all-function classification or enumerator. Older or poorly indexed literature could contain an equivalent statement under different terminology. The result does not address disconnected one-part graphs, algorithmic complexity on general graphs, or other Roman variants.

## References
1. E. Ebrahimi Targhi', N. Jafari Rad, C. M. Mynhard, and Y. Wu, “Bounds for Independent Roman Domination in Graphs,” Journal of Combinatorial Mathematics and Combinatorial Computing 80 (2012), 351–365. Public record: https://combinatorialpress.com/jcmcc-articles/volume-080/bounds-for-independent-roman-domination-in-graphs/
2. N. Jafari Rad, “Note on the Independent Roman Domination Number of a Graph,” Journal of Combinatorial Mathematics and Combinatorial Computing 95, 119–125. Full text: https://combinatorialpress.com/article/jcmcc/Volume%20095/vol-095-paper%209.pdf
3. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami, and L. Volkmann, “Varieties of Roman domination II,” AKCE International Journal of Graphs and Combinatorics 17 (2020), 966–984. https://www.tandfonline.com/doi/abs/10.1016/j.akcej.2019.12.001

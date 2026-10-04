# All irredundant sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), with nonempty parts \(V_1,\ldots,V_r\) of sizes \(n_1,\ldots,n_r\). A set \(D\subseteq V(G)\) is irredundant when every \(v\in D\) has a private vertex \(w\) satisfying \(N[w]\cap D=\{v\}\).

The irredundant sets are exactly the following:

1. the empty set;
2. every set contained in a single part \(V_i\); and
3. every set \(\{u,v\}\) with \(u\in V_i\), \(v\in V_j\), \(i\ne j\), provided \(n_i,n_j\ge2\).

Hence the maximal irredundant sets are exactly the full parts \(V_i\) and the two-vertex transversals joining two distinct non-singleton parts. If \(R_G(x)=\sum_{k\ge1}i_k(G)x^k\) counts nonempty irredundant sets by size, then
\[
R_G(x)=\sum_{i=1}^r\big((1+x)^{n_i}-1\big)+x^2\sum_{\substack{1\le i<j\le r\\n_i,n_j\ge2}}n_i n_j.
\]
If \(M_G(x)\) counts maximal irredundant sets by size, then
\[
M_G(x)=\sum_{i=1}^r x^{n_i}+x^2\sum_{\substack{1\le i<j\le r\\n_i,n_j\ge2}}n_i n_j.
\]
Therefore
\[
\operatorname{IR}(G)=\max_i n_i=\alpha(G),
\]
and
\[
\operatorname{ir}(G)=\begin{cases}1,&\min_i n_i=1,\\2,&\min_i n_i\ge2.\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, and connected. The multipartite presentation has \(r\ge2\) nonempty parts. Private vertices use closed neighborhoods: \(w\) is private to \(v\in D\) when \(N[w]\cap D=\{v\}\). The empty set is vacuously irredundant but is not included in the displayed irredundance polynomial, matching the convention that the polynomial starts at size one.

The result concerns irredundance in a single complete multipartite graph. It does not concern direct products of complete multipartite graphs, irredundance graphs, or domination polynomials.

## Proof
First suppose \(D\subseteq V_i\). The induced graph \(G[D]\) is edgeless, so each \(v\in D\) is isolated in \(G[D]\). Thus \(v\in N[v]\cap D\) and no other vertex of \(D\) lies in \(N[v]\); equivalently, \(N[v]\cap D=\{v\}\). Hence every subset of one part is irredundant.

Next let \(D=\{u,v\}\) with \(u\in V_i\), \(v\in V_j\), \(i\ne j\), and \(n_i,n_j\ge2\). Choose \(v'\in V_j\setminus\{v\}\) and \(u'\in V_i\setminus\{u\}\). Since vertices in the same part are nonadjacent while vertices in different parts are adjacent,
\[
N[v']\cap D=\{u\},\qquad N[u']\cap D=\{v\}.
\]
Thus \(D\) is irredundant.

Conversely, let \(D\) be irredundant and meet at least two parts. Choose \(v\in D\cap V_i\). Because \(D\) meets another part, \(v\) is not isolated in \(G[D]\), so \(v\) needs an external private vertex \(w\notin D\). The vertex \(w\) cannot lie in \(V_i\), because then it is nonadjacent to \(v\). Therefore \(w\in V_j\) for some \(j\ne i\). In a complete multipartite graph, \(w\) is adjacent to every selected vertex outside \(V_j\) and to no selected vertex inside \(V_j\). The equality \(N[w]\cap D=\{v\}\) therefore forces
\[
D\setminus V_j=\{v\}.
\]
In particular, every selected vertex other than \(v\) lies in the single part \(V_j\), and \(D\cap V_i=\{v\}\).

Now choose any \(u\in D\cap V_j\). The same argument applied to \(u\) shows that all selected vertices other than \(u\) lie in one part. Since \(v\in V_i\), this forces \(D\cap V_j=\{u\}\). Hence \(D=\{u,v\}\). The private vertex for \(v\) lies in \(V_j\setminus D\), so \(n_j\ge2\); symmetrically \(n_i\ge2\). This proves the classification.

For maximality, any proper subset of a part \(V_i\) can be enlarged inside \(V_i\) and remains irredundant, while a full part cannot be enlarged without violating the classification. A two-vertex transversal between non-singleton parts also cannot be enlarged: adding a vertex in either occupied part makes one occupied part contain two selected vertices, and adding a vertex in a third part creates support in three parts. Thus precisely the stated sets are maximal.

The polynomial formulas now follow by counting. Part \(V_i\) contributes \((1+x)^{n_i}-1\) nonempty one-part subsets. For each unordered pair of non-singleton parts, there are \(n_i n_j\) cross pairs, all of size two. Maximal sets contribute one monomial \(x^{n_i}\) for each full part and the same cross-pair term. The formulas for \(\operatorname{IR}(G)\) and \(\operatorname{ir}(G)\) are immediate from the sizes of the maximal irredundant sets.

## Verification
The standalone verifier constructs every complete multipartite profile through order \(9\), builds closed neighborhoods literally, tests every nonempty vertex subset for private vertices, and compares the result with the structural criterion above. It independently checks the coefficient counts of \(R_G(x)\), reconstructs maximal irredundant sets from the literal predicate, checks the maximal-set formula, and checks \(\operatorname{IR}(G)\) and \(\operatorname{ir}(G)\).

A replay of the packaged program returned:

`VERIFY_OK profiles=87 subset_checks=22845 irredundant_sets=2975 maximal_sets=995 max_order=9`

This finite census is supplementary evidence only. The theorem for arbitrary part sizes is established by the proof above.

## Relationship to prior work
Cockayne, Hedetniemi, and Miller introduced graph irredundance in 1978. Bollobás and Cockayne developed the domination–independence–irredundance parameter chain in 1979. Mynhardt and Roux give the modern private-neighborhood formulation and state that the concept was introduced in 1978; their paper also records primary subject classification \(05C69\).

The closest structural comparison located is the work of Alon and Defant on direct products of complete multipartite graphs. Their Theorem 1.3 proves that an irredundant set in a direct product of \(n\) complete multipartite factors decomposes into an independent part plus at most \(2^n\) exceptional vertices. For one factor this gives only the coarse bound that at most two selected vertices need lie outside an independent part. It does not classify the possible exceptional configuration, maximal irredundant sets, or the two counting polynomials above. The present theorem is therefore a sharp one-factor structural classification rather than a direct-product corollary.

The irredundance polynomial and maximal irredundance polynomial are standard counting objects. The inspected reference pages define those polynomials but give no complete-multipartite specialization. Searches under complete-multipartite, complete-bipartite, private-neighbor, upper-irredundance, and irredundance-polynomial terminology did not expose an earlier exact arbitrary-part classification. This negative search is supporting evidence rather than a proof of novelty.

## Limitations
The result is restricted to complete multipartite graphs and does not extend automatically to cographs or direct products. The exact 1979 foundational paper was available only through its abstract and bibliographic record in the inspected lawful sources; an older family-specific statement hidden in pre-digital literature remains a residual bibliographic risk. The later direct-product paper was inspected in full and is not statement-equivalent to the one-factor all-set classification.

## References
1. E. J. Cockayne, S. T. Hedetniemi, and D. J. Miller, “Properties of Hereditary Hypergraphs and Middle Graphs,” *Canadian Mathematical Bulletin* 21 (1978), 461–468. DOI: `10.4153/CMB-1978-079-5`.
2. B. Bollobás and E. J. Cockayne, “Graph-theoretic parameters concerning domination, independence, and irredundance,” *Journal of Graph Theory* 3 (1979), 241–249. DOI: `10.1002/jgt.3190030306`.
3. K. Mynhardt and R. Roux, “Irredundance Graphs,” arXiv:`1812.03382`.
4. N. Alon and C. Defant, “Isoperimetry, Stability, and Irredundance in Direct Products,” arXiv:`1904.02595`; later *Discrete Mathematics* 343 (2020), 111902.
5. E. W. Weisstein, “Irredundance Polynomial” and “Maximal Irredundance Polynomial,” MathWorld.

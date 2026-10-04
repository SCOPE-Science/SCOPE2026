# Total outer-component domination of complete multipartite graphs with a corrected bipartite boundary
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), \(N=\sum_i n_i\ge3\), and let \(D\subsetneq V(G)\). Put \(d_i=|D\cap V_i|\), \(c_i=n_i-d_i\), \(p=|\{i:d_i>0\}|\), \(q=|\{i:c_i>0\}|\), and \(c=\sum_i c_i\). Then \(D\) is a total outer-\(k\)-connected component dominating set if and only if \(p\ge2\) and either (i) \(k=1\) with \(q\ge2\) or \(c=1\), or (ii) \(k\ge2\), \(q=1\), and \(c=k\). Consequently, if \(\beta_i=n_i\) for \(r\ge3\) and \(\beta_i=n_i-1\) for \(r=2\), then the exact bivariate enumerator \(\Phi_G(x,y)=\sum_D x^{|D|}y^{k(D)}\) over all such sets is \[\Phi_G(x,y)=yF_1(x)+\sum_{k\ge2}\left(\sum_{i:k\le\beta_i}\binom{n_i}{k}\right)x^{N-k}y^k,\] where \[F_1(x)=(1+x)^N-\sum_i(1+x)^{n_i}+r-1-x^N-\sum_i\sum_{j=2}^{\beta_i}\binom{n_i}{j}x^{N-j}.\] For \(k\ge2\), \(\gamma_{tc}^k(G)=N-k\) exactly when \(k\le\max_i n_i\) if \(r\ge3\), and exactly when \(k<\max_i n_i\) if \(r=2\); otherwise it is \(0\). In particular, for \(K_{m,n}\) with \(2\le m\le n\), the endpoint \(k=n\) has \(\gamma_{tc}^n(K_{m,n})=0\), correcting the non-strict endpoint in Proposition 3.2 of Rad and Volkmann (2016).

The correction at the complete-bipartite endpoint is forced directly by the definition. If \(G=K_{m,n}\) and \(k=n\), then obtaining \(n\) components in \(G-D\) requires \(G-D\) to consist of the whole size-\(n\) part, so \(D\) is contained in the other part. Such a set has no edges inside \(G[D]\) and therefore is not a total dominating set. In particular \(K_{2,2}=C_4\) has \(\gamma_{tc}^2=0\), which also agrees with Theorem 2.6 of the same paper.

## Assumptions and scope
The graph is finite, simple, connected, complete multipartite, has at least two nonempty parts and order at least three. The definition is the one in Rad--Volkmann: \(D\) must be a total dominating set and \(G[V(G)\setminus D]\) must have exactly \(k\ge1\) connected components. The complement is required to be nonempty, as in their TO\(1\)CDS convention for proper sets.

## Proof
A set \(D\) is total dominating in a complete multipartite graph exactly when it meets at least two parts. Indeed, if it meets two parts, every vertex has a neighbor of \(D\) in a different part, including vertices of \(D\) themselves. Conversely, if \(D\) meets at most one part, every selected vertex has no selected neighbor, so total domination fails.

Now put \(C=V(G)\setminus D\). If \(C\) meets at least two parts, then \(G[C]\) is itself a connected complete multipartite graph, so it has one component. If \(C\) lies in a single part, then \(G[C]\) is edgeless and has exactly \(|C|\) components. Combining these two facts gives the profile characterization in the Finding.

For \(k\ge2\), \(C\) must consist of exactly \(k\) vertices from one part \(V_i\). When \(r\ge3\), deleting any such \(C\), even all of \(V_i\), leaves all vertices of at least two other parts in \(D\), so every \(k\)-subset of \(V_i\) is allowed. When \(r=2\), total domination additionally requires at least one selected vertex to remain in \(V_i\), hence \(k<n_i\). This proves the coefficient \(\sum_{i:k\le\beta_i}\binom{n_i}{k}\) and the formula for \(\gamma_{tc}^k\).

For \(k=1\), start from the polynomial for all total dominating sets, \((1+x)^N-\sum_i(1+x)^{n_i}+r-1\). Remove \(x^N\), since the complement must be nonempty. The only remaining sets whose complements are disconnected have complements of size at least two inside a single part. Those complements may have sizes \(2,\ldots,n_i\) for \(r\ge3\), but only \(2,\ldots,n_i-1\) for \(r=2\), yielding the displayed subtraction and hence \(F_1(x)\).

## Verification
A standalone checker exhaustively enumerates every nondecreasing complete-multipartite profile of order from \(3\) through \(10\), every vertex subset, and every \(k\). It compares the literal graph definition against the profile characterization, compares all enumerator coefficients, checks the closed formulas for \(\gamma_{tc}^k\), and separately verifies the complete-bipartite endpoint \(\gamma_{tc}^n(K_{m,n})=0\) for \(2\le m\le n\le7\). Its replay result is:

`VERIFY_OK profiles=127 subset_checks=64912 criterion_checks=614128 coefficient_checks=1097 gamma_checks=1049 boundary_checks=20 max_order=10`

The finite census is a verification aid; the infinite theorem is proved by the two structural observations above.

## Relationship to prior work
Rad and Volkmann introduced total outer-\(k\)-connected component domination and gave exact values for complete graphs, complete bipartite graphs and paths. Their Proposition 3.2 states, for \(2\le m\le n\), a positive value \(m+n-k\) for the complete-bipartite graph through the endpoint \(k=n\). Under their own definition, that endpoint cannot occur because the only possible complement with \(n\) components is the whole size-\(n\) part, leaving a selected set contained in one independent part. Their Theorem 2.6 independently lists \(C_4=K_{2,2}\) among graphs with \(\gamma_{tc}^2=0\), exposing the same boundary conflict. The result here replaces that endpoint by the strict condition \(k<n\) for complete bipartite graphs and extends the classification and enumeration to arbitrary complete multipartite graphs.

Semantic searches for the parameter together with “complete multipartite”, “TOkCDS”, the endpoint \(k=n\), and polynomial/enumerator terminology did not surface a later published correction or an arbitrary complete-multipartite all-set formula. Related indexed findings on total domination and other multipartite domination variants do not imply this component-count classification.

## Limitations
The theorem is specific to complete multipartite graphs and to the total outer-component definition above. It does not classify analogous parameters for arbitrary cographs or general bipartite graphs. The literature search cannot exclude an obscure correction under substantially different terminology, although the defining paper itself and targeted searches were inspected directly.

## References
1. N. Jafari Rad and L. Volkmann, “Generalization of the total outer-connected domination in graphs,” *RAIRO Operations Research* 50 (2016), 233–239, DOI 10.1051/ro/2015016. The open full text contains the definition, Theorem 2.6, and Proposition 3.2.
2. Author-uploaded public copy of the same article, public upload dated 2015-08-06; this is used only as the earliest verified public-source date.

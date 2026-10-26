# The independent-domination polynomial of a twice-centralized graph

## Finding

For a finite simple connected graph \(G\) with \(n\ge 3\) vertices and \(m\) edges, write \(\mathtt C(G)\) for its central graph: subdivide each edge once, and join each originally nonadjacent pair. Let \(a_s(G)\) count independent vertex subsets of \(G\) of cardinality \(s\), including \(a_0(G)=1\), and let \(\alpha(G)\) be the independence number. Write \(D_i(F;z)=\sum_{S}z^{|S|}\), where \(S\) ranges over all independent dominating sets of \(F\). Set \(M=m+\binom n2\).

**Theorem.** For every such \(G\),
\[
\boxed{D_i(\mathtt C^2(G);z)=
\sum_{s=0}^{\alpha(G)}a_s(G)z^{M-(n-1)s+\binom{s+1}{2}}
+mz^{M-1}+2mz^{M-n+2}.}
\]
Here \(\mathtt C^2(G)=\mathtt C(\mathtt C(G))\); polynomial terms at identical degrees are added. In particular,
\[
\boxed{|\mathcal{ID}(\mathtt C^2(G))|=\sum_{s=0}^{\alpha(G)}a_s(G)+3m,}
\]
where \(\mathcal{ID}(F)\) is the family of all independent dominating sets of \(F\). The theorem gives an explicit bijection, not only equality of counts.

For \(n\ge4\), the minimum independent dominating sets of \(\mathtt C^2(G)\) have the following complete classification. If \(G\) is complete, there are exactly \(n^2\) minimum sets. If \(G\) is a star, there are exactly \(n\). For every other connected \(G\), minimum sets are in a natural bijection with the maximum independent sets of \(G\), hence their number is \(a_{\alpha(G)}(G)\). For a nonstar connected graph on \(n\ge4\) vertices, the full polynomial, together with \(n,m\), recovers every coefficient \(a_s(G)\).

## Assumptions and scope

All graphs are finite, undirected, simple and vertex-labelled; isomorphic graphs are not distinguished in the theorem, but sets within a graph are counted by actual vertices. An independent dominating set is an independent set that dominates every unselected vertex. The degree of its monomial is its cardinality. No choice of an ordering of edges in constructing central graphs affects the asserted bijection or counting polynomial.

The polynomial identity holds for all connected graphs of order at least three. The classifications of the minimum sets and the coefficient-recovery statement are asserted for order at least four. No assertion is made for disconnected input graphs.

## Proof

**Step 1: A general bijection.** Fix any finite simple graph \(H\), and distinguish the old vertices \(V(H)\) and the new degree-two subdivision vertices \(w_e\) in \(\mathtt C(H)\). Let \(S\) be an independent dominating set in \(\mathtt C(H)\), and put \(X=S\cap V(H)\). The old vertices are adjacent in \(\mathtt C(H)\) exactly when nonadjacent in \(H\), so \(X\) is a clique of \(H\), with the empty set allowed. For each edge \(e=uv\) of \(H\), independence prohibits \(w_e\in S\) if \(u\in X\) or \(v\in X\). If neither endpoint belongs to \(X\), domination forces \(w_e\in S\), since \(u,v\) are its only neighbors. Therefore
\[
S=\Phi_H(X):=X\cup\{w_e:e\in E(H-X)\}.
\]
This set is always independent for every clique \(X\). For an old vertex \(v\notin X\), it fails to be dominated precisely when (i) no selected old vertex is a nonneighbor of \(v\) in \(H\), and (ii) every edge incident with \(v\) has its other endpoint in \(X\). Those conditions are equivalent to \(N_H(v)=X\). Thus \(\Phi_H(X)\) is dominating if and only if no \(v\notin X\) has \(N_H(v)=X\).

**Step 2: All cliques are admissible in the intermediate central graph.** Put \(H=\mathtt C(G)\). No vertex of \(H\) has a clique as its open neighborhood. Indeed, an edge-subdivision vertex \(w_{uv}\) of \(H\) has neighborhood \(\{u,v\}\), whose two members are nonadjacent in \(H\). An old vertex \(v\in V(G)\) has degree exactly \(n-1\ge2\) in \(H\). As \(G\) is connected, it has a neighbor \(u\) in \(G\). The vertex \(w_{uv}\in N_H(v)\) is isolated in \(H[N_H(v)]\): its only neighbors in \(H\) are \(u,v\), and \(u\notin N_H(v)\), since \(uv\) was an edge of \(G\). Hence \(N_H(v)\) is not a clique. In particular, \(N_H(v)\ne X\) for every clique \(X\subseteq V(H)\). By Step 1,
\[
\boxed{\mathcal{ID}(\mathtt C(H))=\{\Phi_H(X):X\text{ a clique of }H\},}
\]
and \(\Phi_H\) is injective since \(\Phi_H(X)\cap V(H)=X\).

**Step 3: Exhaust the cliques of \(H\).** No two subdivision vertices of \(H\) are adjacent. A subdivision vertex \(w_{uv}\) is adjacent only to its two old endpoints \(u,v\), which are themselves nonadjacent in \(H\). Thus a clique is exactly one of: (a) a subset of old vertices which was independent in \(G\), including the empty set; (b) one of the \(m\) singleton subdivision vertices; or (c) one of the \(2m\) incident old--subdivision pairs \(\{u,w_{uv}\}\), \(\{v,w_{uv}\}\). The list is disjoint and exhaustive.

**Step 4: Record cardinalities.** There are \(M=m+\binom n2\) edges in \(H\). Every old vertex has degree \(n-1\) in \(H\), every subdivision vertex degree \(2\). For a clique \(X\subseteq V(H)\), with \(k=|X|\), the number of edges incident with \(X\) is \(\sum_{x\in X}\deg_H(x)-\binom{k}{2}\). Consequently
\[
|\Phi_H(X)|=k+M-\sum_{x\in X}\deg_H(x)+\binom k2.
\]
For a type-(a) clique of size \(s\), this equals \(M-(n-1)s+\binom{s+1}{2}\). For type (b), it equals \(M-1\). For type (c), it equals \(M-n+2\). Summing the three disjoint families proves the polynomial formula. Setting \(z=1\) proves the total-count identity.

**Step 5: Minimum-set classification and recovery.** Write \(e_s=M-(n-1)s+\binom{s+1}{2}\). Direct subtraction gives
\[
e_{s+1}-e_s=s+2-n.
\]
For a connected graph of order \(n\ge4\), either \(\alpha(G)\le n-2\), or \(\alpha(G)=n-1\), in which latter case connectedness forces \(G\) to be a star. If \(G\) is neither complete nor a star, then \(2\le\alpha(G)\le n-2\) and the displayed differences are strictly negative throughout the relevant sizes. Thus the type-(a) minimum is attained exactly at \(s=\alpha(G)\). As \(e_2=M-2n+5<M-n+2<M-1\), neither exceptional clique type can minimize, so minimum sets correspond exactly to maximum independent sets of \(G\). If \(G\) is a star, \(\alpha(G)=n-1\) and \(e_{n-2}=e_{n-1}\) is the minimum. There are \(n-1\) independent subsets of size \(n-2\) and one of size \(n-1\); the exceptional clique types are larger because \(n\ge4\). If \(G=K_n\), \(\alpha(G)=1\) and \(e_1=M-n+2\), tying exactly the \(2m\) incident-pair cliques; singleton subdivisions are larger, since \(n\ge4\). The count is \(n+2m=n^2\).

For connected nonstar \(G\) with \(n\ge4\), the degrees \(e_0,e_1,\dots,e_{\alpha(G)}\) are pairwise distinct, and the only extra contributions to the polynomial are the explicitly known \(mz^{M-1}+2mz^{M-n+2}\). Subtracting them and reading coefficients at \(e_s\) recovers all \(a_s(G)\). This completes the proof.

## Verification

A standard-library Python verifier in `verify.py` constructs both central graph iterates independently, enumerates all maximal independent sets of the final graph using Bron--Kerbosch on its complement, and compares the complete cardinality histogram with the asserted polynomial. Since independent dominating sets are exactly maximal independent sets, this checks every counted configuration for each finite host, not a random sample of solutions. The verifier exhausts all connected labelled host graphs of orders \(3,4,5\) (respectively \(4,38,728\) instances) and checks \(100\) seeded connected labelled six-vertex hosts, including the minimum-set trichotomy where applicable. The run returned `VERIFY_OK host_graphs=870 independent_domination_sets_checked=21149`. Execute with `python3 verify.py` from any directory with Python 3.8 or later; no dependencies other than the standard library. The complete infinite theorem follows from Steps 1--5 rather than these finite tests.

## Relationship to prior work

Cabrera-Martínez, López-Carmona, Rios-Villamar and Serrano-Díaz (arXiv:2609.16357v1, first posted 2026-09-14) establish independent-domination **numbers** for central graphs, including an exact second-iterate numerical formula in Theorem 2.12. The minimum-size consequence here agrees with that earlier result. The contribution here is the complete polynomial of *all* independent dominating sets, its canonical bijection with the three types of intermediate cliques, the exact total count, and the minimum-set multiplicities. The independent-domination polynomial itself was studied by Jahari and Alikhani (arXiv:1808.07369); their inspected account does not treat this iterated central operation. A related public result, *Independent domination of higher iterated central graphs* (2026), studies minimum **numbers** from the third iterate onward and does not classify minimum sets or give the second-iterate polynomial.

## Limitations

The central-graph operator is used with the specified complement-on-original-vertices convention; this is not the line graph, total graph, or ordinary edge-subdivision graph. The input is required to be connected and of order at least three; the minimum-set trichotomy and coefficient recovery require at least four. While the polynomial identity is an exact proved enumeration for every permitted input, the independent-domination polynomial alone is not asserted to recover the isomorphism class of \(G\). Searches of selected relevant papers and published records do not establish universal historical priority. No corresponding full polynomial theorem is asserted here for higher central iterates.

## References

1. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar and A. Serrano-Díaz, *Independent domination in central graphs*, arXiv:2609.16357v1 (2026), especially Theorems 2.1 and 2.12. https://arxiv.org/abs/2609.16357
2. S. Jahari and S. Alikhani, *On the independent domination polynomial of a graph*, arXiv:1808.07369v3 (2018; subsequently published in Discrete Applied Mathematics). https://arxiv.org/abs/1808.07369
3. *Independent domination of higher iterated central graphs*, public research record dated 2026-09-17, identifier 7dc2104ad847.

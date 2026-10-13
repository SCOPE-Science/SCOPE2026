# One missing edge forces a linear Cayley-host penalty for cocktail-party graphs

## Finding
Let \(r\ge2\) and let \(CP_r=K_{2,\ldots,2}\), the cocktail-party graph with \(r\) parts of two vertices each. Delete any edge \(e\), and write \(G_r=CP_r-e\). For a finite graph \(G\), define \(\eta(G)\) to be the minimum order of an abelian group \(\Gamma\) such that an undirected Cayley graph \(\operatorname{Cay}(\Gamma,S)\), with \(S=-S\) and \(0\notin S\), contains an induced copy of \(G\).

**Theorem.** For every integer \(r\ge2\),
\[
\eta(G_r)=3r-1.
\]
Moreover, the same lower bound holds for induced hosts among **all finite vertex-transitive graphs**, not only abelian Cayley graphs. In contrast, \(CP_r\) itself is an abelian Cayley graph on \(2r\) vertices, so deleting a single edge incurs the exact additional cost \(r-1\).

## Assumptions and scope
All graphs are finite, simple and undirected. Induced embedding means preserving both edges and nonedges. The vertex-transitive lower bound is an assertion about every finite vertex-transitive host, irrespective of connectedness. The upper construction is cyclic and makes no demands on valency beyond those explicitly specified. All edges of \(CP_r\) are equivalent by automorphism, so the choice of \(e\) is immaterial.

## Proof
Write \(F_r=\overline{G_r}\). In the complement \(\overline{CP_r}\), each two-vertex part contributes a single edge, so \(\overline{CP_r}=rK_2\). Deleting \(e\) from \(CP_r\) adds one edge between vertices in distinct matching pairs. Hence
\[
F_r\cong P_4\;\dot\cup\;(r-2)K_2,
\]
with \(2r\) vertices, \(r+1\) edges and maximum degree two.

**Lower bound.** Let a finite vertex-transitive graph \(H\) on \(N\) vertices contain \(G_r\) as an induced subgraph. Its complement \(J=\overline H\) is vertex-transitive and therefore regular of some degree \(d\), and it contains \(F_r\) as an induced subgraph on \(2r\) vertices. Since \(F_r\) contains \(P_4\), necessarily \(d\ge2\). Let \(t=N-2r\) be the number of vertices outside the induced copy. Exactly \(2rd-2(r+1)\) edges of \(J\) cross from the \(2r\) selected vertices to the \(t\) others, by summing degrees on the selected vertices and subtracting twice the internal edge count. There can be at most \(td\) crossing edges, by summing degrees outside. Consequently
\[
2rd-2(r+1)\le td,
\qquad (2r-t)d\le2(r+1).
\]
If \(t\ge2r\) then certainly \(t\ge r-1\); otherwise \(2r-t>0\), and using \(d\ge2\) yields \(2(2r-t)\le2(r+1)\), hence \(t\ge r-1\). In either case \(N=2r+t\ge3r-1\). This argument only uses regularity of \(J\), so it even establishes the stated stronger lower bound for all hosts whose complement is regular.

**Upper bound.** Put \(N=3r-1\) and consider the cycle \(C_N\), a Cayley graph on the cyclic group \(\mathbb Z_N\) with step set \(\{1,-1\}\). On its vertices choose \(r-1\) disjoint consecutive blocks, of lengths \(4,2,2,\ldots,2\), separated cyclically by exactly one omitted vertex between consecutive blocks (including the last and first). The number of used vertices is \(4+2(r-2)=2r\), and there are exactly \(r-1\) separating vertices. The cycle induced by the chosen vertices is therefore \(P_4\dot\cup(r-2)K_2=F_r\). Taking graph complements, the induced subgraph of \(\overline{C_N}\) on those \(2r\) vertices is exactly \(G_r\). Since \(\overline{C_N}\) is the abelian Cayley graph \(\operatorname{Cay}(\mathbb Z_N,\mathbb Z_N\setminus\{0,1,-1\})\), we obtain \(\eta(G_r)\le N=3r-1\). Combining both bounds completes the proof.

Finally, \(CP_r\) is Cayley on \(\mathbb Z_{2r}\) with the zero step and the unique order-two step \(r\) removed: the connection set is \(\mathbb Z_{2r}\setminus\{0,r\}\). Its own order is \(2r\), and no induced host can have fewer vertices, so \(\eta(CP_r)=2r\). Thus the additional \(r-1\) vertices are necessary and sufficient.

## Verification
The self-contained Python 3 program `verify.py` checks the explicit cycle-block construction for every integer \(2\le r\le100\), verifies the induced complementary component sizes and edge counts, and checks the lower-bound arithmetic for these parameters. Run `python3 verify.py`; its actual output is included as `verification_output.txt`. The universal lower bound and upper construction are proved above, independent of finite tests.

## Relationship to prior work
Souop and Bitjoka [1] introduced this specific minimum induced abelian Cayley-host order as a graph invariant and obtained exact values for paths and complete bipartite graphs. The family here instead begins with cocktail-party graphs and removes one edge. The bipartite boundary \(r=2\), where \(G_2=P_4\) and \(\eta(P_4)=5\), agrees with their earlier path theorem and is not claimed separately as new. The value of \(\eta(CP_r)=2r\) itself follows from its Cayley representation and is also standard. The contribution is the exact **linear perturbation cost** for \(r\ge3\), with a universal regular-host lower bound and a matching cyclic construction. The standard Cayley characterization of cocktail-party graphs [2] concerns the undeleted family and does not directly imply the perturbation result.

## Limitations
The theorem concerns precisely one deleted cross-part edge from a cocktail-party graph; it does not classify arbitrary edge deletions, arbitrary unequal multipartite graphs, or all optimal host isomorphism types. A literature search did not identify a covering result, but the full text of [1] was not retrievable; an unindexed equivalent or stronger result remains possible. No independent audit has been performed.

## References
[1] R. Fokam Souop and L. Bitjoka, *Induced Embeddings of Graphs into Abelian Cayley Graphs*, arXiv:2609.01486, first publicly posted 2026-09-01, https://arxiv.org/abs/2609.01486.

[2] *Distance-regular Cayley graphs with least eigenvalue \(-2\)*, Designs, Codes and Cryptography (2016), doi:10.1007/s10623-016-0209-4, https://doi.org/10.1007/s10623-016-0209-4; see the discussion of cocktail-party Cayley graphs in Section 4.2.

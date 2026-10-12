# Every anti-foundation double-membership graph has universal closed wreath subgroups

## Finding
Let \(M\models\mathsf{ZFA}\) be countable, where \(\mathsf{ZFA}\) means ZFC with Foundation replaced by Aczel's Anti-Foundation Axiom, and let \(D(M)\) be its double-membership graph:
\[
x\mathrel D y \quad\Longleftrightarrow\quad x\in y\ \text{and}\ y\in x.
\]
Equip \(\operatorname{Aut}(D(M))\) with the pointwise-convergence topology. Then for every finite group \(G\),
\[
\boxed{G\wr S_\infty\ \leq_{\mathrm{closed}}\ \operatorname{Aut}(D(M)),}
\]
where the wreath product is the unrestricted permutation wreath product
\[
G\wr S_\infty=G^{\mathbb N}\rtimes S_\infty.
\]
Consequently \(\operatorname{Aut}(D(M))\) contains a closed copy of \(S_\infty\), is not locally compact, and contains every countable group as an abstract subgroup.

## Assumptions and scope
The graph is the reduct retaining only double membership; loops are allowed in the ambient graph. The finite graph used below is simple, so loops play no role in the subgroup construction. Countability of \(M\) is used to identify the infinitely many relevant components with a countable family and hence to obtain \(S_\infty\).

The statement is a uniform lower bound on automorphism-group complexity. It does not classify \(\operatorname{Aut}(D(M))\), does not claim that the displayed wreath subgroups are normal, and does not identify the automorphism groups of the infinite connected components.

## Proof
Adam-Day, Howe, and Mennuni recall the earlier result of Adam-Day and Cameron that, for every finite connected graph \(\Gamma\), the double-membership graph of every countable model of \(\mathsf{ZFA}\) has infinitely many connected components isomorphic to \(\Gamma\). Their Proposition 3.3 gives a more general component-realization mechanism, and the finite-component statement is used throughout their analysis.

Fix a finite group \(G\). By Frucht's theorem, choose a finite connected simple graph \(\Gamma_G\) with
\[
\operatorname{Aut}(\Gamma_G)\cong G.
\]
Let \(\mathcal C_G\) be the set of connected components of \(D(M)\) isomorphic to \(\Gamma_G\). The cited anti-foundation result says that \(\mathcal C_G\) is infinite. Since \(D(M)\) is countable and every member of \(\mathcal C_G\) is finite, \(\mathcal C_G\) is countably infinite. Let
\[
U_G=\bigcup\mathcal C_G.
\]

Consider the pointwise stabilizer
\[
H_G=\{h\in\operatorname{Aut}(D(M)): h(x)=x\text{ for all }x\notin U_G\}.
\]
Because \(U_G\) is a union of connected components, every automorphism of the induced graph \(D(M)\upharpoonright U_G\) extends by the identity on the complement. Conversely, an element of \(H_G\) restricts to an automorphism of that induced graph. Thus
\[
H_G\cong\operatorname{Aut}\!\left(\bigsqcup_{i\in\mathbb N}\Gamma_G\right).
\]
An automorphism of this disjoint union consists of an arbitrary automorphism of each copy of \(\Gamma_G\), together with an arbitrary permutation of the copies. Hence
\[
H_G\cong \operatorname{Aut}(\Gamma_G)^{\mathbb N}\rtimes S_\infty
\cong G^{\mathbb N}\rtimes S_\infty
=G\wr S_\infty.
\]

The subgroup \(H_G\) is closed: it is the intersection of the point stabilizers of all vertices in \(D(M)\setminus U_G\). Under the natural identification above, the subspace topology is exactly the usual permutation-wreath topology, so the isomorphism is topological.

Taking \(G\) trivial gives a closed copy of \(S_\infty\). The Polish permutation group \(S_\infty\) is not locally compact, while every closed subgroup of a locally compact Hausdorff group is locally compact; therefore \(\operatorname{Aut}(D(M))\) is not locally compact. Finally, every countable group embeds in \(S_\infty\) by its left-regular action on a countable set, so every countable group embeds abstractly in \(\operatorname{Aut}(D(M))\).

## Verification
A standalone finite verifier checks the component-to-wreath calculation directly for disjoint unions of copies of \(K_2\) and \(K_3\). It exhaustively enumerates graph automorphisms and verifies
\[
\left|\operatorname{Aut}\!\left(\bigsqcup_{i=1}^k K_q\right)\right|
=(q!)^k k!
\]
for several pairs \((q,k)\), and separately checks explicit within-component and component-permuting automorphisms. Running `python3 artifacts/verify.py` prints `VERIFY_OK 41814 exact assertions`.

The finite computation is only a replay of the wreath-product step. The general theorem relies on the published component-realization result and Frucht's theorem.

## Relationship to prior work
Adam-Day, Howe, and Mennuni study the connected components and first-order theories of double-membership graphs of models of Anti-Foundation. Their paper explicitly records that every finite connected graph occurs as infinitely many connected components in every such countable graph, but it does not discuss automorphism groups. Adam-Day and Cameron proved the finite-component realization in the earlier graph-theoretic paper.

Frucht's theorem supplies a connected finite graph with any prescribed finite automorphism group. The standard automorphism calculation for a countable disjoint union of isomorphic connected finite graphs gives the wreath product. The present conclusion is the synthesis: every anti-foundation double-membership graph, independently of which countable model produced it, contains the full closed wreath profile \(G\wr S_\infty\) for every finite \(G\).

Targeted searches for double-membership automorphism groups, Frucht/wreath formulations, closed \(S_\infty\) subgroups, and universal countable-group embeddings found the component theorem and general graph-wreath literature, but no statement of this anti-foundation consequence.

## Limitations
The argument gives embedded closed subgroups, not a decomposition of the full automorphism group. Infinite connected components may contribute additional symmetries, and different models can have very different global double-membership graphs. The originality risk is that the deduction is short once the finite-component theorem, Frucht's theorem, and the standard disjoint-union automorphism formula are placed side by side, so it may exist as uncatalogued folklore.

## References
1. B. Adam-Day, J. Howe, and R. Mennuni, *On double-membership graphs of models of Anti-Foundation*, arXiv:1908.02708; Bulletin of Symbolic Logic 29 (2023), 128--144, DOI:10.1017/bsl.2022.37.
2. B. Adam-Day and P. J. Cameron, *Undirecting membership in models of Anti-Foundation*, Aequationes Mathematicae 95 (2021), 393--400, DOI:10.1007/s00010-020-00763-w.
3. G. Sabidussi, *Graphs with given group and given graph-theoretical properties*, Canadian Journal of Mathematics 9 (1957), 515--525, DOI:10.4153/CJM-1957-060-7, recalling Frucht's theorem in connected form.

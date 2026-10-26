# A triangle criterion and exact optimal-partition census for super coalitions near maximal super domination

## Finding
Let \(G\) be a finite simple graph on \(n\ge5\) vertices, without isolated vertices, whose super domination number satisfies \(\gamma_{\mathrm{sp}}(G)\ge n-2\). Define the *two-deletion graph* \(B_G\) on the same vertex set by joining distinct \(u,v\) precisely when \(V(G)\setminus\{u,v\}\) is a super dominating set. Write \(e(B_G)\) for its edge count, \(t(B_G)\) for its number of unordered triangles, and \(m_j(B_G)\) for its number of matchings of size \(j\). Let \(c_{\mathrm{sp}}(G)\) be the largest size of a partition of \(V(G)\) into nonempty, individually non-super-dominating blocks such that every block has a different partner whose union with it super dominates \(G\).

Then
\[
c_{\mathrm{sp}}(G)=\begin{cases}4,&t(B_G)>0,\\3,&t(B_G)=0.\end{cases}
\]
Moreover, if \(t(B_G)>0\), the number of *unordered* optimal four-block partitions is exactly \(t(B_G)\), with one partition for each triangle \(\{a,b,c\}\) of \(B_G\):
\[
\bigl\{\{a\},\{b\},\{c\},V(G)\setminus\{a,b,c\}\bigr\}.
\]
For **every** graph under the stated assumptions, the number \(T_3(G)\) of admissible unordered three-block partitions, whether or not optimal, is
\[
T_3(G)=\binom n2+(n-3)e(B_G)+m_2(B_G)-2\mathbf1_{\{n=5\}}m_2(B_G)-2\mathbf1_{\{n=6\}}m_3(B_G).
\]
Consequently this is the exact optimal-partition count when \(t(B_G)=0\).

A concrete application covers complete multipartite graphs \(K_{n_1,\ldots,n_r}\) with \(r\ge2\), all \(n_i\ge1\), and total order \(n\ge5\). If \(q\) parts have size at least two, then their super coalition number is four exactly when \(q\ge3\), and three otherwise. In the four-block case the number of optimal partitions is
\[
\sum_{1\le i<j<k\le r\atop n_i,n_j,n_k\ge2} n_i n_j n_k.
\]
For instance, \(K_{2,2,2}\) has eight optimal four-block partitions, whereas \(K_{2,3}\) has sixteen optimal three-block partitions.

## Assumptions and scope
For \(D\subseteq V(G)\), write \(U=V(G)\setminus D\). The set \(D\) is *super dominating* if for each \(v\in U\) there exists \(w\in D\) for which \(N_G(w)\cap U=\{v\}\). The super domination number is the minimum cardinality of such a set. A super coalition partition, as used here, is a set partition into nonempty blocks, none super dominating, in which every block is in at least one super-dominating pairwise union. Blocks are not labelled. The theorem concerns all such graphs of order at least five and assumes no other symmetry, regularity, or connectivity. The no-isolate hypothesis ensures that every complement of one vertex is super dominating; the lower bound on \(\gamma_{\mathrm{sp}}\) ensures that no set with at most \(n-3\) vertices can super dominate.

## Proof
**Lemma 1 (eligible remainders).** Under the assumptions, \(V(G)\setminus R\) is super dominating for a nonempty proper set \(R\) if and only if \(|R|=1\), or \(|R|=2\) and its two vertices are adjacent in \(B_G\). Indeed, the one-deletion case is certified by a neighbor of the deleted vertex, and the two-deletion case is the definition of \(B_G\). A set of three or more omitted vertices would contradict \(\gamma_{\mathrm{sp}}(G)\ge n-2\).

**Lemma 2 (four-block rigidity).** Take any admissible partition with \(k\) blocks. Every block has a coalition partner; by Lemma 1 at most two other nonempty blocks may remain, whence \(k\le4\). When \(k=4\), the two blocks outside a coalition pair must both be singletons. Since \(n\ge5\), at least one block \(L\) is nonsingleton. It must belong to every coalition pair, so all three other blocks are singletons \(\{a\},\{b\},\{c\}\). The singleton \(\{a\}\) can only partner \(L\), and by Lemma 1 this happens exactly when \(bc\in E(B_G)\). Applying the same argument to the other two singletons forces \(ab,ac,bc\in E(B_G)\). Conversely, every triangle yields the displayed four-part partition. Each block is individually non-super-dominating, since the three singleton blocks and the remaining block \(L\) have sizes smaller than \(n-2\). Thus four-block partitions are in bijection with triangles of \(B_G\).

**Lemma 3 (existence of three blocks).** If \(B_G\) is not complete, choose a nonedge \(uv\) and use the partition \(\{\{u\},\{v\},V\setminus\{u,v\}\}\). Its large block is not super dominating and its unions with the two singleton blocks are one-deletion super dominating sets. If \(B_G\) is complete, choose four distinct vertices \(u,v,x,y\) and use \(\{\{u,v\},\{x,y\},V\setminus\{u,v,x,y\}\}\). All three blocks have cardinality at most \(n-3\), and every union of two is super dominating because the third block is a singleton or an edge of \(B_G\). Hence three blocks always exist. Lemmas 2 and 3 establish the maximum.

**Lemma 4 (exact three-block census).** Call a nonempty block *small* when it is a singleton or a two-vertex edge of \(B_G\). In a three-block partition, the union of two blocks is super dominating if and only if the remaining block is small. Every block has a partner exactly when at least two blocks are small. Both small blocks are individually not super dominating, since \(n\ge5\). The remaining block must also fail super domination. If the two designated small blocks are singletons, their union must be a nonedge of \(B_G\), giving \(\binom n2-e(B_G)\) possibilities. If one is a singleton and the other an edge, there are \((n-2)e(B_G)\) possibilities; their union has size three and the residual block is not super dominating. If both are disjoint edges, there are \(m_2(B_G)\) possibilities, again with a nonsuper residual block. Every admissible three-block partition is counted once, except when all three blocks are small. The latter is possible only at \(n=5\), with block sizes \(2,2,1\), and at \(n=6\), with block sizes \(2,2,2\). The respective exceptional partitions are indexed by \(m_2(B_G)\) and \(m_3(B_G)\), and were counted three times. Subtracting twice each exceptional total and collecting terms gives the displayed formula.

**Multipartite specialization.** For a complete multipartite graph, a super dominating set may omit two vertices exactly when they are in different parts, each of size at least two; otherwise, it may omit at most one. To see this independently, a witness for one of two omitted vertices has to be selected in the part of the other omitted vertex, forcing both parts to have selected survivors. Therefore \(\gamma_{\mathrm{sp}}\ge n-2\), and \(B_G\) is the complete multipartite graph on the parts of size at least two, with vertices in singleton parts isolated. Its triangles choose one vertex from each of three different qualifying parts, which proves the two stated formulas. In \(K_{2,3}\), \(e(B_G)=6\), \(m_2(B_G)=6\), \(n=5\), giving \(10+2\cdot6-6=16\); in \(K_{2,2,2}\), there are \(2^3=8\) triangles.

## Verification
Run the accompanying `verify.py` using Python 3 standard library. It independently constructs super dominating sets from open-neighborhood witnesses, enumerates unlabelled set partitions, checks each pairwise coalition directly, constructs the two-deletion graph, and compares the maximum and both counts for every eligible five-vertex graph and independently chosen six- and seven-vertex graphs. The recorded run returned `VERIFY_OK: high-super-domination graphs tested 2388`. Finite enumeration supports, but does not replace, the all-order combinatorial proof.

## Relationship to prior work
The super coalition invariant and its defining conditions were introduced by Alikhani and Ghanbari (arXiv:2607.22686, first public source recorded 2026-07-15). Their Sections 2–7 (arXiv HTML full text) prove the general upper bound \(c_{\mathrm{sp}}(G)\le n+2-\gamma_{\mathrm{sp}}(G)\) in Theorem 3.2, give lower bounds, and treat paths, cycles, cliques, stars, wheels and friendship graphs. They do not classify equality at the four-block ceiling in the present near-maximal regime or enumerate eligible partitions. A separate publicly indexed result entitled *All super dominating sets of complete multipartite graphs* gives the precise eligible two-deletion pairs for that family. Neither the full text of the motivating paper nor the accessible summary of that separate result gives the general two-deletion-graph triangle criterion or the graph-matching census of three-block coalitions. The multipartite application is a specialization of the more general transfer theorem here; the eligible-pair characterization itself is prior work, not claimed as new.

## Limitations
This theorem assumes no isolated vertices, at least five vertices and super domination number at least \(n-2\); it does not classify arbitrary graphs with smaller super domination number. The motivating preprint was inspected in full via its accessible arXiv HTML version. Full text of the separately indexed multipartite result was not retrieved, leaving some residual overlap uncertainty for the already credited specialization; unidentified other literature could also overlap. The transfer proof is elementary and makes no independent-audit or external-certification claim.

## References
1. S. Alikhani and N. Ghanbari, *Super Coalition Number in Graphs*, arXiv:2607.22686 (first posted July 2026), https://arxiv.org/abs/2607.22686 .
2. D. J. Klein, J. A. Rodríguez-Velázquez and E. Yi, *On the super domination number of graphs*, 2018 preprint / 2019 journal publication, DOI:10.22049/CCO.2019.26587.1122.
3. *All super dominating sets of complete multipartite graphs*, public mathematical record dated 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-all-super-dominating-sets-of-complete-multipartite-graphs--315739371089 .

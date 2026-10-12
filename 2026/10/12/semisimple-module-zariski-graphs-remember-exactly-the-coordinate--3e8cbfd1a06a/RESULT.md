# Semisimple module Zariski graphs remember exactly the coordinate subspace-count signature
## Finding
Let \(r\ge2\), let \(R=\prod_{i=1}^{r}\mathbb F_{q_i}\), and let \(M=\bigoplus_{i=1}^{r}V_i\) with \(V_i\cong\mathbb F_{q_i}^{d_i}\), \(d_i\ge1\), under the coordinatewise faithful \(R\)-action. Put \(T=\operatorname{Spec}(M)\) and let \(G(M)=G(\tau_T)\) be the Zariski topology-graph. For each \(i\), let \(a_i\) be the number of proper subspaces of \(V_i\), equivalently \(a_i=\sum_{k=0}^{d_i-1}{d_i\brack k}_{q_i}\). For every nonempty proper \(S\subset[r]\), let \(C_S\) be the set of submodules \(N=\bigoplus_iN_i\) such that \(N_i=V_i\) exactly for \(i\in S\). Then the vertex set is the disjoint union of the \(C_S\), \(|C_S|=\prod_{i\notin S}a_i\), and two vertices in cells \(C_S,C_U\) are adjacent exactly when \(S\cap U=\varnothing\). The cells \(C_S\) are exactly the false-twin classes. Consequently the twin quotient is the disjointness graph on the nonempty proper subsets of \([r]\), whose automorphism group is \(S_r\). Hence
\[
\operatorname{Aut}G(M)\cong\left(\prod_{\varnothing\ne S\subsetneq[r]}S_{\prod_{i\notin S}a_i}\right)\rtimes H,
\qquad
H=\{\pi\in S_r:a_{\pi(i)}=a_i\text{ for all }i\}.
\]
Moreover, for two modules of this form, \(G(M)\cong G(M')\) if and only if they have the same number of simple ring factors and the multisets \(\{a_1,\ldots,a_r\}\) agree. Thus this graph detects exactly the coordinate proper-subspace counts, not the fields and dimensions separately. In particular, \(\mathbb F_2^3\) and \(\mathbb F_{13}^2\) each have \(15\) proper subspaces, so the modules \((\mathbb F_2^3)\oplus(\mathbb F_2^3)\) over \(\mathbb F_2\times\mathbb F_2\) and \((\mathbb F_{13}^2)\oplus(\mathbb F_{13}^2)\) over \(\mathbb F_{13}\times\mathbb F_{13}\) have isomorphic Zariski topology-graphs, both \(K_{15,15}\), although the modules and coefficient rings are nonisomorphic.

## Assumptions and scope
The ring is a finite product of fields \(R=\prod_{i=1}^r\mathbb F_{q_i}\) with \(r\ge2\). The module is the faithful semisimple module \(M=\bigoplus_iV_i\), where every \(V_i\) is a nonzero finite-dimensional vector space over the corresponding field. The graph is the Zariski topology-graph with \(T=\operatorname{Spec}(M)\). No claim is made for nonsemisimple modules, nonfaithful modules, or proper choices of \(T\).

## Proof
Every \(R\)-submodule has the unique form \(N=\bigoplus_iN_i\) with \(N_i\le V_i\). Its colon ideal is coordinatewise: the \(i\)-th component of \((N:M)\) is \(\mathbb F_{q_i}\) when \(N_i=V_i\), and is \(0\) otherwise. Define the full-coordinate support \(S(N)=\{i:N_i=V_i\}\).

A proper submodule \(P\) is prime exactly when there is one index \(j\) such that \(P_j<V_j\) and \(P_i=V_i\) for every \(i
e j\). If two coordinates are proper, an idempotent supported on one deficient coordinate and a vector supported on the other violate primality. Conversely, with exactly one deficient coordinate, the prime-submodule condition reduces to the elementary field argument that a nonzero scalar cannot carry a vector outside a proper subspace into that subspace.

Thus the prime spectrum is the disjoint union of the families indexed by \(j\), and a prime from the \(j\)-family lies in \(V(N)\) exactly when \(j
otin S(N)\). Therefore \(V(N)
e\operatorname{Spec}(M)\) exactly when \(S(N)
e\varnothing\), while \(N<M\) exactly when \(S(N)
e[r]\). For two such vertices \(N,K\),
\[
V(N)\cup V(K)=\operatorname{Spec}(M)
\quad\Longleftrightarrow\quad
S(N)\cap S(K)=\varnothing.
\]
This proves the support-cell description. If \(a_i\) denotes the number of proper subspaces of \(V_i\), then coordinates outside \(S\) can be chosen independently among their proper subspaces, giving \(|C_S|=\prod_{i
otin S}a_i\).

Vertices in one cell have identical open neighborhoods. Distinct cells have different neighborhoods: if \(i\in S\setminus U\), every vertex in the nonempty cell \(C_{\{i\}}\) is adjacent to every vertex of \(C_U\) and to no vertex of \(C_S\). Hence the cells are exactly the false-twin classes.

The twin quotient \(D_r\) has vertices the nonempty proper subsets of \([r]\), with disjointness adjacency. A subset \(S\) has quotient degree \(2^{r-|S|}-1\), so every quotient automorphism preserves \(|S|\). In particular it permutes the singleton supports. A support \(S\) is recovered from the singleton vertices to which it is nonadjacent, so every quotient automorphism is induced by a unique coordinate permutation. Hence \(\operatorname{Aut}(D_r)\cong S_r\).

An automorphism of the blown-up graph may independently permute vertices inside every false-twin cell. A coordinate permutation lifts exactly when it preserves every cell size. Since the cell indexed by \([r]\setminus\{i\}\) has size \(a_i\), this condition is exactly \(a_{\pi(i)}=a_i\) for every \(i\). This gives the stated semidirect product.

For graph isomorphism between two modules, the false-twin quotient recovers \(2^r-2\), hence \(r\), and then recovers the quotient up to a coordinate permutation. The same codimension-one support cells recover the individual \(a_i\) up to that permutation. Conversely, equality of the multisets \(\{a_i\}\) supplies a coordinate permutation matching every cell size, hence an isomorphism of the blow-ups. Finally, direct Gaussian-binomial counts give \(a(2,3)=1+7+7=15\) and \(a(13,2)=1+14=15\), yielding the explicit \(K_{15,15}\) collision.

## Verification
The accompanying standard-library program `verify_semisimple_zariski.py` enumerates all subspaces for small prime fields, checks the prime-submodule definition directly by exhaustive scalar/vector tests, constructs \(V(N)\) from colon-ideal inclusion, and verifies the support/disjointness description for \((\mathbb F_2^2)\oplus\mathbb F_3\) and \((\mathbb F_2^2)\oplus(\mathbb F_2^2)\). It also verifies false-twin cell sizes for several abstract signatures, exhaustively confirms \(|\operatorname{Aut}(D_2)|=2\) and \(|\operatorname{Aut}(D_3)|=6\), and checks the \(15\)-proper-subspace collision between \(\mathbb F_2^3\) and \(\mathbb F_{13}^2\). These finite checks support, but do not replace, the general proof.

## Relationship to prior work
The Zariski topology-graph of modules was introduced in the 2014 Communications in Algebra paper, which has primary MSC \(13C13\) and was published online on 4 April 2014. Its later full-text sequel develops decomposition, bipartiteness, clique, chromatic, and localization results; it explicitly records decomposition of submodules and prime submodules along idempotent factors. The 2018 annihilating-submodule paper likewise develops the direct-product decomposition and coloring theory. The present result uses that algebraic setup but gives a different statement: a complete false-twin blow-up description for finite semisimple modules, the full automorphism group, an if-and-only-if graph-isomorphism classification, and an explicit pair of nonisomorphic semisimple modules with the same graph.

## Limitations
The 2014 foundational article's full text was not available through the lawful open route inspected here; its abstract, metadata, and later full-text sequel were available. The result therefore retains a literature risk that an unindexed passage or another source may contain an equivalent automorphism or isomorphism classification. The theorem does not claim that the signature \(a_i\) determines \((q_i,d_i)\); the explicit collision proves that it does not.

## References
1. H. Ansari-Toroghy and S. Habibi, *The Zariski Topology-Graph of Modules Over Commutative Rings*, Communications in Algebra 42 (2014), 3283–3296, DOI 10.1080/00927872.2013.780065.
2. H. Ansari-Toroghy and S. Habibi, *The annihilating-submodule graph of modules over commutative rings*, Mathematical Reports 20(70) (2018), 245–262.
3. H. Ansari-Toroghy and S. Habibi, *The Zariski topology-graph of modules over commutative rings II*, Arabian Journal of Mathematics 10 (2021), 41–50, DOI 10.1007/s40065-020-00301-1.

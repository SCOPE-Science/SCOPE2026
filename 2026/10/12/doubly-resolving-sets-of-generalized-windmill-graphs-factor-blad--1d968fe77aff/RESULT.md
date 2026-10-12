# Doubly resolving sets of generalized windmill graphs factor blade by blade
## Finding
For integers \(k\ge2\) and \(m\ge2\), define the generalized windmill
\[
W_{k,m}=K_1\vee kK_m.
\]
Thus \(W_{k,m}\) has a center \(c\) and \(k\) pairwise disjoint peripheral cliques \(B_1,\ldots,B_k\), each of cardinality \(m\); the center is adjacent to every peripheral vertex, vertices in a common \(B_i\) are adjacent, and vertices in distinct peripheral cliques are nonadjacent.

A set \(S\subseteq V(W_{k,m})\) is a doubly resolving set if and only if
\[
|B_i\setminus S|\le1\qquad(1\le i\le k).
\]
Equivalently, the center may be chosen or omitted independently, while each peripheral clique contributes either all \(m\) vertices or exactly \(m-1\) vertices. Therefore the complete cardinality enumerator is
\[
D_{W_{k,m}}(z)=\sum_{S\text{ doubly resolving}}z^{|S|}
=(1+z)\bigl(mz^{m-1}+z^m\bigr)^k
=z^{k(m-1)}(1+z)(m+z)^k.
\]
In particular,
\[
\psi(W_{k,m})=k(m-1),
\]
every minimum doubly resolving set omits the center and exactly one vertex from each peripheral clique, and the number of minimum doubly resolving sets is
\[
m^k.
\]
For \(m=2\), this specializes to the friendship graph and gives \(\psi(W_{k,2})=k\), with exactly \(2^k\) minimum sets.

## Assumptions and scope
All graphs are finite, simple, connected, and unweighted. Two landmarks \(x,y\) doubly resolve vertices \(u,v\) when
\[
d(u,x)-d(v,x)\ne d(u,y)-d(v,y).
\]
A set is doubly resolving when every distinct vertex pair is doubly resolved by two landmarks in the set. The theorem is asserted only for \(k\ge2\) and \(m\ge2\). The one-blade case is a complete graph, while \(m=1\) gives a star; in both boundaries the stated bladewise criterion is false.

## Proof
First suppose that \(S\) is doubly resolving. Fix a peripheral clique \(B_i\). Any two distinct vertices \(u,v\in B_i\) are twins: every vertex outside \(\{u,v\}\) is at the same distance from \(u\) and \(v\). If both \(u\) and \(v\) were absent from \(S\), then every landmark \(s\in S\) would satisfy \(d(u,s)=d(v,s)\), so the difference \(d(u,s)-d(v,s)\) would be constantly zero on \(S\). Hence \(S\) could not doubly resolve \(u,v\). Thus \(|B_i\setminus S|\le1\) for every \(i\).

Conversely, assume \(|B_i\setminus S|\le1\) for every \(i\). Since \(m\ge2\), every \(B_i\) meets \(S\); since \(k\ge2\), for each blade there is also a landmark in another blade. We check all possible vertex pairs by comparing the difference function
\[
\Delta_{u,v}(s)=d(u,s)-d(v,s).
\]
If \(u,v\in B_i\), then at least one of \(u,v\) lies in \(S\). If both do, their own two coordinates give values \(-1\) and \(1\). If exactly one does, say \(u\in S\), then \(\Delta_{u,v}(u)=-1\), while every landmark in another peripheral clique gives \(0\). Thus the pair is doubly resolved.

If \(u\in B_i\) and \(v\in B_j\) with \(i\ne j\), choose \(s_i\in S\cap B_i\) and \(s_j\in S\cap B_j\). At \(s_i\), the value \(\Delta_{u,v}(s_i)\) is either \(-2\) or \(-1\); at \(s_j\), it is either \(2\) or \(1\). These values are different, so \(u,v\) are doubly resolved.

Finally, let one vertex be the center \(c\) and the other be \(u\in B_i\). Choose \(s_i\in S\cap B_i\) and \(s_j\in S\cap B_j\) for some \(j\ne i\). Then \(\Delta_{c,u}(s_i)\) is \(1\) when \(s_i=u\) and \(0\) otherwise, whereas \(\Delta_{c,u}(s_j)=-1\). Hence \(c,u\) are doubly resolved. This proves sufficiency.

The polynomial follows independently across the blades. In one \(m\)-vertex peripheral clique, a valid choice has either \(m-1\) selected vertices, in \(m\) ways, or all \(m\) vertices, in one way, contributing \(mz^{m-1}+z^m\). The center contributes \(1+z\). Multiplication gives the stated formula. Its least exponent is \(k(m-1)\), and the coefficient there is \(m^k\), proving the minimum and the basis count.

## Verification
The accompanying verifier constructs \(W_{k,m}\), computes all-pairs graph distances, and checks every vertex subset against the definition of a doubly resolving set. For the eight parameter pairs \((k,m)\in\{2,3,4\}^2\) with order at most \(13\), it compares the exact definition with the bladewise criterion, checks every polynomial coefficient against \((1+z)(mz^{m-1}+z^m)^k\), and checks the minimum size and basis count. It reports:

`VERIFY_OK parameter_pairs=8 subset_checks=18720 basis_checks=225 max_order=13 boundary_checks=2`

The finite computation is a regression check, not the proof for arbitrary parameters; the preceding case analysis is the infinite proof. The verifier also confirms that the excluded boundaries \(k=1\) and \(m=1\) each contain counterexamples to the bladewise criterion.

## Relationship to prior work
Cáceres, Hernando, Mora, Pelayo, Puertas, Seara, and Wood introduced doubly resolving sets in their 2005 preprint on Cartesian-product metric dimension. Their Section 4 defines the parameter, proves general product bounds, and treats standard families such as complete graphs, paths, cycles, and trees; its searchable full text contains no occurrence of “friendship” or “windmill.” The first public arXiv version is dated 26 July 2005 and carries MSC 05C12.

Widyaningrum and Kusmayadi studied the strong metric dimension of windmill graphs, a different resolving parameter. Yang, Rafiullah, Siddiqui, and Ahmad studied the ordinary and edge metric dimensions of friendship graphs; their friendship section states the ordinary metric dimension and proves the edge metric dimension, but contains no doubly-resolving or double-metric result. Nie and Xu give a general twin-set lower bound for doubly resolving sets and results for corona products; that lower bound explains the necessity of selecting all but at most one vertex in each blade, but it does not supply the converse, the all-set characterization, or the enumerator above.

Database searches also found work on doubly resolving sets of complete multipartite graphs and of thick chain graphs. Those results do not imply this theorem: for \(k,m\ge2\), \(W_{k,m}\) contains triangles and has adjacent vertices inside each blade but nonadjacent vertices across blades, so it is neither a chain graph nor a complete multipartite graph. A same-object database record on generalized windmills concerns the general-position polynomial, not doubly resolving sets.

## Limitations
The theorem does not include \(k=1\) or \(m=1\), and it does not assert an originality theorem relative to every unindexed or inaccessible source. Literature searches used the aliases “windmill,” “generalized windmill,” “Dutch windmill,” “friendship graph,” “doubly resolving,” and “double metric dimension.” No inspected source stated the bladewise if-and-only-if characterization or its counting polynomial. The general twin-set lemma is a genuine prior ingredient for the lower bound; the sufficiency and exact enumeration are the additional content established here.

## References
1. J. Cáceres, C. Hernando, M. Mora, I. M. Pelayo, M. L. Puertas, C. Seara, and D. R. Wood, *On the Metric Dimension of Cartesian Products of Graphs*, arXiv:math/0507527v1, first submitted 26 July 2005; SIAM Journal on Discrete Mathematics 21(2), 423–441, DOI 10.1137/050641867.
2. M. Widyaningrum and T. A. Kusmayadi, *On the strong metric dimension of sun graph, windmill graph, and Möbius ladder graph*, Journal of Physics: Conference Series 1008 (2018) 012032, DOI 10.1088/1742-6596/1008/1/012032.
3. B. Yang, M. Rafiullah, H. M. A. Siddiqui, and S. Ahmad, *On Resolvability Parameters of Some Wheel-Related Graphs*, Journal of Chemistry 2019, 9259032, DOI 10.1155/2019/9259032.
4. K. Nie and K. Xu, *The doubly metric dimension of corona product graphs*, Filomat 37(13) (2023), 4375–4386, DOI 10.2298/FIL2313375N.

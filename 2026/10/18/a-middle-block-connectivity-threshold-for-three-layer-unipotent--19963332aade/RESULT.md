# A middle-block connectivity threshold for three-layer unipotent commuting graphs

## Finding

For any prime power \(q\) and positive integers \(a,b,c\), let \(G_{a,b,c}(q)\) be the three-block unipotent matrix group defined below. Its **reduced commuting graph** \(\Gamma(G)\) has one vertex for every noncentral group element, with an edge precisely when two distinct elements commute.

**Connectivity threshold.** The reduced commuting graph is disconnected if and only if \(b=1\). In this case, with \(K_m\) denoting a complete graph on \(m\) vertices and \(mK_n\) denoting a disjoint union of \(m\) copies, its full graph isomorphism type is
\[
\Gamma(G_{a,1,c}(q))\cong
K_{q^{ac}(q^a-1)}\sqcup K_{q^{ac}(q^c-1)}
\sqcup \frac{(q^a-1)(q^c-1)}{q-1}\,K_{q^{ac}(q-1)}.
\]
In particular, the group has abelian centralizers of all noncentral elements if and only if \(b=1\).

**Uniform sharp diameter bound.** For every \(b\ge2\), the reduced commuting graph is connected of diameter at most \(3\). More precisely,
\[
\operatorname{diam}\Gamma(G_{a,b,c}(q))=2\quad\text{if }\min(a,c)=1<b,
\]
and
\[
\operatorname{diam}\Gamma(G_{a,b,c}(q))=3\quad\text{if }2\le b\le\min(a,c).
\]
These equalities hold for every finite field, including characteristic two. Intermediate parameters \(1<\min(a,c)<b\) satisfy the proven universal bound but their exact diameter is not classified here.

## Assumptions and scope

Let \(\mathbb F_q\) be any finite field and \(a,b,c\in\mathbb Z_{\ge1}\). The group consists of block matrices
\[
g(A,B,C)=\begin{pmatrix}I_a&A&C\\0&I_b&B\\0&0&I_c\end{pmatrix},
\quad A\in M_{a\times b}(\mathbb F_q),\ B\in M_{b\times c}(\mathbb F_q),\ C\in M_{a\times c}(\mathbb F_q).
\]
Matrix multiplication supplies the group law; no restriction on field characteristic is imposed. The center is exactly \(\{g(0,0,C):C\in M_{a\times c}(\mathbb F_q)\}\), of order \(q^{ac}\). This is an ordinary commuting graph on noncentral *elements*, not a graph on conjugacy classes, and not the graph obtained by including the center as universal vertices. The graph has \(q^{ac}(q^{b(a+c)}-1)\) vertices.

## Proof

**Step 1 (commutation equation).** Multiplication is
\[
g(A,B,C)g(D,E,H)=g(A+D,B+E,C+H+AE).
\]
Hence two elements commute exactly when
\[
AE=DB.\tag{1}
\]
If \(AE=DB\) for every \(D,E\), taking \(D=0\) and then \(E=0\) forces \(A=B=0\), establishing the center. Therefore graph adjacency depends only on the nonzero pair \((A,B)\): every such pair represents \(q^{ac}\) mutually adjacent vertices with identical external neighbors.

**Step 2 (the \(b=1\) graph).** Write \(A=\alpha\) as a column and \(B=\beta\) as a row. If \(\beta=0\) and \(\alpha\ne0\), (1) forces \(E=0\), so all first-only elements constitute one complete component. Dually, all elements with \(A=0\) and \(B\ne0\) constitute another complete component. For \(\alpha\ne0\) and \(\beta\ne0\), the equality \(\alpha\varepsilon=\delta\beta\) of rank-one outer products holds for a noncentral pair \((\delta,\varepsilon)\) if and only if
\[
(\delta,\varepsilon)=(t\alpha,t\beta)\quad\text{for a unique }t\in\mathbb F_q^\times.
\]
Thus mixed pairs split into scalar lines, each containing \(q-1\) nonzero pairs; their number is \((q^a-1)(q^c-1)/(q-1)\). Each quotient pair has \(q^{ac}\) central lifts. This proves the asserted clique decomposition, and all centralizers of noncentral elements are abelian.

**Step 3 (diameter at most three for \(b\ge2\)).** Identify the middle space with \(M=\mathbb F_q^b\). Given any two noncentral pairs \((A,B)\) and \((D,E)\), select a single nonzero \(u\in M\) as follows. For a pair \((A,B)\), a vector \(u\) is unsuitable for the next construction only if
\[
Au=0\quad\text{and}\quad\operatorname{im}B\subseteq\langle u\rangle.
\]
If \(B=0\), the unsuitable vectors lie in the proper subspace \(\ker A\). If \(B\) has rank one, they lie in the proper one-dimensional subspace \(\operatorname{im}B\). If \(B\) has rank at least two, no nonzero vector is unsuitable. The union of two proper subspaces cannot cover a vector space over any field, so choose \(u\ne0\) suitable for both pairs.

For each pair choose a nonzero linear functional \(\phi\) satisfying \(\phi(u)=0\) and
\[
(Au\phi,\,u\phi B)\ne(0,0).
\]
Such a functional exists: if \(Au\ne0\), any nonzero \(\phi\in u^\perp\) works; otherwise suitability gives \(\operatorname{im}B\not\subseteq\langle u\rangle\), so select \(\phi\in u^\perp\) not annihilating \(\operatorname{im}B\). The condition \(b\ge2\) ensures that \(u^\perp\ne0\). Write \(T=u\phi\in\operatorname{End}(M)\); then \(T^2=0\), and the noncentral element represented by \((AT,TB)\) commutes with \((A,B)\), because \(A(TB)=(AT)B\). It is distinct from the original noncentral pair: \((AT,TB)=(A,B)\) would imply \((AT^2,T^2B)=(A,B)\), a contradiction.

Use \(T_x=u\phi_x\) and \(T_y=u\phi_y\) for the two initial vertices, sharing the chosen \(u\). Since \(\phi_x(u)=\phi_y(u)=0\), one has both \(T_xT_y=0\) and \(T_yT_x=0\). Their two constructed noncentral neighbors commute with each other by (1). Consequently any two vertices are joined by a path of at most three edges. This proves connectivity and the diameter bound for all \(b\ge2\).

**Step 4 (exact diameter two when \(a=1\) or \(c=1\)).** Suppose \(a=1\). For two arbitrary noncentral pairs \((A,B)\), \((D,E)\), regard \(A,D\) as row vectors of length \(b\). If they are linearly independent, take any nonzero row \(U\in M_{1\times b}\); the map \(V\mapsto(AV,DV)\) from \(M_{b\times c}\) onto \(M_{1\times c}^2\) is surjective, so choose \(V\) satisfying \(AV=UB\) and \(DV=UE\). Then \((U,V)\ne(0,0)\) commutes with both initial elements. If \(A,D\) are dependent, their common kernel in \(\mathbb F_q^b\) is nonzero because \(b\ge2\); set \(U=0\) and take any nonzero matrix \(V\) whose columns lie in that kernel. Again it commutes with both. Thus every two vertices have distance at most two. Interchanging the first and third blocks and transposing yields the same conclusion for \(c=1\). Noncommuting noncentral pairs always exist, so the diameter is exactly two.

**Step 5 (sharp diameter three when \(a,c\ge b\ge2\)).** Choose an injective matrix \(P\in M_{a\times b}\) and a surjective matrix \(Q\in M_{b\times c}\), and consider noncentral vertices represented by \((P,Q)\) and \((P,0)\). They do not commute, since \(PQ\ne0\). A common noncentral commuter \((U,V)\) would satisfy \(PV=0\) and \(PV=UQ\), whence \(V=0\) by injectivity and \(U=0\) by surjectivity. There is therefore no path of length two. Step 3 supplies a path of length three, proving equality.

**Step 6 (abelian-centralizer boundary).** Step 2 proves the property when \(b=1\). For \(b\ge2\), choose \(A\ne0\) of rank one and \(B=0\). Its centralizer contains all elements with second block zero, and all elements with first block zero and second block \(V\) satisfying \(AV=0\). Because \(\ker A\ne0\), select such a nonzero \(V\), and then select \(U\) with \(UV\ne0\). The two centralizer elements represented by \((U,0)\) and \((0,V)\) do not commute. Hence some noncentral centralizer is nonabelian when \(b\ge2\).

## Verification

The accompanying standalone `verify_graph.py` constructs nonzero matrix pairs directly over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\) and the extension field \(\mathbb F_4\). It evaluates equation (1), independently creates all graph edges, computes connected components and shortest-path diameters, and checks the claimed clique multiplicities or diameter bounds in thirteen finite parameter cases. It returns `ALL_GRAPH_CHECKS_PASSED 13` when successful. The characteristic-independent proof above, not this finite enumeration, establishes the theorem for all prime powers and sizes.

## Relationship to prior work

Cameron, Coll, Mayers and Russoniello's 2021 study of the breadth of Lie poset algebras includes the corresponding three-layer Lie poset; its focus is the maximum adjoint rank, not connectivity or commuting-graph diameter. The 2006 paper of Diaconis and Thiem treats the same no-four-chain pattern groups and their conjugacy/character theory, not this graph connectivity threshold. Nien's 2021 paper describes irreducible representations of precisely these three-block unipotent radicals, not the reduced commuting-graph decomposition or diameter transition.

Giudici and Pope's 2012 Theorem 1.4 states a general diameter-two criterion for class-two groups with \(|Z(G)|^3<|G|\). It applies here whenever \(b(a+c)>2ac\), so these diameter-two cases are not asserted as independent new consequences. It does not cover the parameter-uniform diameter-three bound or the full disconnected-versus-connected classification. Their work also gives a diameter-three result for ordinary unitriangular groups of size at least four; those are distinct groups in general. Majeed and Ramkumar's 2026 work on the full four-by-four unitriangular group likewise studies a distinct nilpotency-class-three example. The finite AC-group structural literature explains why commuting graphs split into cliques once centralizers are abelian, but does not by itself identify exactly which three-block groups satisfy the AC property or supply their component sizes.

## Limitations

The exact diameter for \(1<\min(a,c)<b\) is not determined here: the stated claim is an upper bound of three in that regime. The result does not classify the full spectrum, automorphism group, clique number, or perfectness for connected cases. An equivalent group-specific statement in less readily indexed work on commuting graphs of pattern groups cannot be ruled out solely from the sources checked. Graphs include all noncentral **group elements**, not central classes or chosen representatives.

## References

- A. Cameron, V. E. Coll Jr., N. Mayers and N. Russoniello, *The breadth of Lie poset algebras*, first public version 2021-05-06, https://arxiv.org/abs/2105.02429.
- P. Diaconis and N. Thiem, *Supercharacter formulas for pattern groups*, first public 2006-10-04, https://arxiv.org/abs/math/0610161.
- M. Giudici and A. Pope, *On Bounding the Diameter of the Commuting Graph of a Group*, first public 2012-06-19, https://arxiv.org/abs/1206.3731.
- C. Nien, *Characters of unipotent radicals of standard parabolic subgroups with 3 parts*, first published online 2021-09-23, https://doi.org/10.1007/s10801-021-01052-8.
- M. Majeed and P. B. Ramkumar, *Commuting Graph of Unitriangular Group UT(4; p)*, first public 2026-08-10, https://arxiv.org/abs/2608.09235.

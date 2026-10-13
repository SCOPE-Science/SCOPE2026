# Support components determine centralizers and commuting counts in graph Lie algebras

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph, with \(n=|V|\) vertices and \(m=|E|\) edges. Construct the two-step graph Lie algebra \(L_G(K)\) over any field \(K\) from vertex generators \(v_i\) and central independent edge generators \(z_{ij}\) by
\[
[v_i,v_j]=z_{ij}\quad\text{when }\{i,j\}\in E,\ i<j,
\]
and use anticommutativity, with all other basis brackets zero. In characteristic two the bracket is alternating by this prescription.

For \(S\subseteq V\), set \(c(S)=c(G[S])\), the number of components of the induced graph; set \(c(\varnothing)=0\). Write \(b(S)=|V\setminus (S\cup N(S))|\), the number of vertices outside \(S\) having no neighbor in \(S\). Then **every** element \(x=\sum_i a_iv_i+z\), whose support \(\{i:a_i\ne0\}\) equals \(S\), satisfies
\[
\dim_K C_{L_G(K)}(x)=m+c(S)+b(S),\qquad
\operatorname{rank}(\operatorname{ad}_x)=n-c(S)-b(S).
\]
Thus the adjoint rank depends only on vertex-coordinate support, not on nonzero coefficient values or field characteristic.

For each prime power \(q\), the entire adjoint-rank distribution is
\[
\boxed{\sum_{x\in L_G(\mathbf F_q)}T^{\operatorname{rank}(\operatorname{ad}_x)}
=q^m\sum_{S\subseteq V}(q-1)^{|S|}T^{n-c(S)-b(S)}.}
\]
If \(Q(G;u,v)=\sum_{S\subseteq V}u^{|S|}v^{c(S)}\) is the established induced-subgraph component polynomial, then the **ordered** number of commuting pairs, and the element commutativity degree, are
\[
\boxed{|\{(x,y)\in L_G(\mathbf F_q)^2:[x,y]=0\}|=q^{2m}Q(G;q-1,q+1),\quad
d(L_G)=q^{-2n}Q(G;q-1,q+1).}
\]
This relationship applies with isolated vertices and in characteristic two. It uses the already-known graph polynomial \(Q\); no claim is made to invent that polynomial or its pre-existing special-graph evaluations.

## Assumptions and scope

The graph is simple and undirected, with arbitrarily many vertices (including zero) and independent central edge basis vectors. In particular, parallel edges or repeated edge labels are **not** within the claim. The centralizer statement holds over an arbitrary field; the numerical enumerators require a finite field \(\mathbf F_q\), with \(q\) any prime power. The polynomial variable \(T\) is formal. The dimension of \(L_G(K)\) is \(n+m\), and the summation ranges over all subsets \(S\subseteq V\). No restriction to connected graphs is imposed.

## Proof

**1. Edgewise centralizer equations.** Fix \(x=\sum_i a_iv_i+z\) and \(y=\sum_i b_iv_i+w\). Since the edge basis is independent and central,
\[
[x,y]=0\quad\Longleftrightarrow\quad
a_ib_j-a_jb_i=0\quad\text{for every }\{i,j\}\in E.
\]
Let \(S=\{i:a_i\ne0\}\). Along an edge wholly inside \(S\), the displayed equation is equivalent to \(b_i/a_i=b_j/a_j\). Hence there is one freely chosen common ratio on each connected component of \(G[S]\), providing exactly \(c(S)\) independent vertex coordinates. Along an edge from \(S\) to its complement, the outside coefficient is forced to be zero. At a vertex outside \(S\) with no neighbor inside \(S\), the vertex coefficient is unrestricted: edges joining two such outside vertices impose \(0=0\), so exactly \(b(S)\) additional coordinates are free. All \(m\) central coordinates of \(y\) are free. Therefore
\[
\dim_K C_{L_G}(x)=m+c(S)+b(S).
\]
The rank-nullity theorem in the \((n+m)\)-dimensional Lie algebra yields \(\operatorname{rank}(\operatorname{ad}_x)=n-c(S)-b(S)\). This argument works without division by two, including in characteristic two.

**2. Full rank spectrum.** For a prescribed vertex-coordinate support \(S\), each coefficient \(a_i\) with \(i\in S\) has \(q-1\) choices, each coefficient outside \(S\) is zero, and the central part of \(x\) has \(q^m\) choices. Summing their common rank from part 1 gives the asserted rank enumerator. This includes the cases of empty support and isolated vertices.

**3. Commuting-pair count by projective directions.** Disregard temporarily the \(2m\) independent central coordinates in the ordered pair \((x,y)\). Regard the pair of vertex coefficients at vertex \(i\) as a column \((a_i,b_i)\in\mathbf F_q^2\). An edge contributes zero bracket precisely when its two columns have determinant zero. Let \(S\) be the set of vertices with nonzero columns. A nonzero column determines one of the \(q+1\) points in \(\mathbf P^1(\mathbf F_q)\), and has \(q-1\) possible nonzero amplitudes along that point. For two adjacent vertices of \(S\), vanishing determinant means that their projective directions agree. Hence each connected component of \(G[S]\) freely chooses one direction. There are exactly \((q-1)^{|S|}(q+1)^{c(S)}\) admissible column assignments supported exactly on \(S\). Restoring the \(2m\) unrestricted central coordinates multiplies by \(q^{2m}\). Summing over \(S\) proves the commuting-pair formula.

Dividing by \(|L_G(\mathbf F_q)|^2=q^{2(n+m)}\) gives the stated commutativity degree. Comparing this count with the sum of the centralizer cardinalities also proves the graph-polynomial identity
\[
\sum_{S\subseteq V}(X-1)^{|S|}X^{c(S)+b(S)}
=Q(G;X-1,X+1).
\]
Indeed both sides agree for every prime-power integer \(X=q\), so they are identical polynomials with integer coefficients.

**4. Explicit forest computation.** Suppose \(G\) is a forest. Choose a root in each component. For the subtree rooted at a vertex \(v\), define \(A_v\) to be the weighted number of admissible projective-column assignments with the root column zero, and \(B_v\) the weighted number with the root direction fixed in advance to one specified point of \(\mathbf P^1(\mathbf F_q)\) (including its \(q-1\) nonzero amplitudes). The weights are ordinary counts. If \(u\) runs through children of \(v\), then
\[
A_v=\prod_u(A_u+(q+1)B_u),\qquad
B_v=(q-1)\prod_u(A_u+B_u).
\]
At a leaf, \((A_v,B_v)=(1,q-1)\). The component count is \(A_r+(q+1)B_r\), and the counts multiply over disjoint tree components. Each vertex requires only a bounded number of additions and multiplications per incident child, so this computes \(Q(G;q-1,q+1)\) in \(O(n)\) arithmetic operations. This recurrence is a specialization of well-known tree evaluations of the subgraph component polynomial, rather than a claim of a previously unknown graph algorithm.

## Verification

The included standalone `verify.py` (Python 3 standard library only) directly checks each ordered vertex-coordinate pair against all edge determinant equations, and independently computes the adjoint rank by finite-field Gaussian elimination. It exhausts every simple graph on at most four vertices over \(\mathbf F_2\) and \(\mathbf F_3\), and every simple graph on at most three vertices over \(\mathbf F_4\) (implemented by adjoining a root of \(X^2+X+1\)). It separately checks the support-sum versus projective-direction count identity for every simple graph on at most five vertices over field sizes 2, 3, and 5; it also compares the forest recurrence with the direct subset sum for all 1,442 labeled trees on at most six vertices over field sizes 2, 3, and 5. The bundled script returns `VERIFY_OK`.

These finite calculations are checks of implementation and sample cases, **not** a substitute for the arbitrary-graph proofs in the previous section. Run `python3 verify.py` from the directory containing that file.

## Relationship to prior work

Barrionuevo–Tirao (2022, arXiv:2206.10572v1, §2) gives precisely the independent-edge two-step graph Lie algebra, and studies geometric rigidity over complex scalars; it does not derive support-wise centralizer dimensions or finite-field commuting counts. Godoy Molina–Lagos (2023, arXiv:2308.00272v2, §§2–5) develops graph ideals and graded derivations, not these enumeration invariants. Shamsaki–Erfanian–Parvizi (2024, arXiv:2406.10064v1, §3, Lemma 3.2) introduces finite-field Lie commutativity degree and the general adjoint-rank averaging identity; the present support formula supplies a new complete explicit evaluation for the graph Lie family. Tittmann–Averbouch–Makowsky (2008/2011, arXiv:0812.4147v2, §4.2, Theorem 10) establishes the graph polynomial \(Q\) and its weighted-colouring interpretation; the graph polynomial and its intrinsic recurrences are thus prior work. The stated finding is the correspondence with graph-Lie commuting pairs **together with** the exact centralizer and adjoint-rank spectra, not an independent discovery of the combinatorial polynomial.

A distinct use of “graph Lie algebra” occurs in Gintz (2018), where a Lie algebra is generated inside a Clifford-type graph algebra; it is not generally the two-step independent-central-edge construction here. Relevant published results on almost-abelian algebras cover some highly special graph examples but not the whole graph family.

## Limitations

The claim concerns graph Lie algebras with one independent central basis element for **each** edge. It does not apply unchanged to arbitrary quotient labelings in which two edges share a central generator; then the edge equations can cancel across labels. The formula counts elements and ordered commuting pairs, not isomorphism classes or subalgebra pairs. The known graph polynomial \(Q\) may be expensive to evaluate on unrestricted graphs; only the forest recursion is asserted to be linear in arithmetic operations. Although relevant full primary texts and alternate terminology have been compared, an equivalent formulation hidden in earlier graphical-group or representation-theoretic literature cannot be absolutely excluded by literature search alone. Independent validation has not been performed.

## References

1. J. Barrionuevo and P. Tirao, *Rigid 2-step graph Lie algebras*, arXiv:2206.10572v1 (first public 2022-06-21), https://arxiv.org/html/2206.10572v1.
2. A. Shamsaki, A. Erfanian and M. Parvizi, *On the commutativity degree of a finite-dimensional Lie algebra*, arXiv:2406.10064v1 (2024), https://arxiv.org/html/2406.10064v1.
3. P. Tittmann, I. Averbouch and J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, arXiv:0812.4147v2 (2009), *European Journal of Combinatorics* **32** (2011), 954–974, https://arxiv.org/html/0812.4147v2.
4. M. Godoy Molina and D. Lagos, *Lie Algebras Associated with Labeled Directed Graphs*, arXiv:2308.00272v2 (2023), https://arxiv.org/html/2308.00272v2.
5. M. Gintz, *Classifying Graph Lie Algebras* (2018), https://math.mit.edu/research/highschool/primes/materials/2017/Gintz.pdf (different graph Lie construction).

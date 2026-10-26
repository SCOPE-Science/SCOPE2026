# Graph-isomorphism completeness of perfect evolution-algebra isomorphism over fixed finite fields

## Finding

**Theorem.** Fix a finite field \(K=\mathbb F_q\). Given two finite-dimensional perfect evolution \(K\)-algebras by their structure matrices relative to natural bases, deciding whether they are isomorphic is **GI-complete under polynomial-time many-one reductions**. More precisely:

1. Each \(n\)-dimensional input has an explicit two-relation directed graph with \(n(q-1)\) vertices and at most \((n^2+n)(q-1)\) ordered relation entries. Two perfect evolution algebras are isomorphic if and only if these finite relational structures are isomorphic. For every **fixed** \(q\), the structures can be converted into ordinary uncolored graphs of polynomial size.
2. Graph isomorphism reduces to isomorphism of perfect evolution \(K\)-algebras even when every structure constant belongs to \(\{0,1\}\) and, after ordering the natural basis, the structure matrix has the block form \(\begin{pmatrix}I&C\\0&I\end{pmatrix}\), where every column of \(C\) has precisely two ones.

Thus the perfect evolution-algebra isomorphism decision problem over every fixed finite field is polynomial-time equivalent to ordinary graph isomorphism. This is a complexity classification, **not** a claim that either problem has a polynomial-time decision algorithm.

## Assumptions and scope

An evolution \(K\)-algebra \(E\) has a natural basis \(e_1,\ldots,e_n\) with \(e_ie_j=0\) for distinct indices and \(e_i^2=\sum_j a_{ij}e_j\). It is perfect when \(E^2=E\), equivalently its structure matrix \(A=(a_{ij})\) is invertible. The input consists of two explicit square matrices over a **fixed** finite field, with a field representation and arithmetic fixed in advance. Nonperfect matrices are outside the theorem. A polynomial-time reduction is measured in the number of input symbols, with \(q\) fixed.

A relation-isomorphism preserves each of two named binary relations. Standard fixed-color and incidence gadgets convert such a structure into a simple uncolored graph without changing its isomorphism relation and with polynomial size.

## Proof

**Step 1: monomial rigidity.** Let \(E_A,E_B\) be perfect and let \(\phi:E_A\to E_B\) be an algebra isomorphism. Write \(\phi(e_i)=\sum_k t_{ki}f_k\). If \(i\ne j\), then \(0=\phi(e_ie_j)=\sum_k t_{ki}t_{kj}f_k^2\). As the \(f_k^2\) are linearly independent, every row of the invertible matrix \((t_{ki})\) has at most one nonzero entry. Invertibility forces exactly one nonzero entry per row and column. Therefore \(\phi(e_i)=c_if_{\sigma(i)}\) for a permutation \(\sigma\) and nonzero scalars \(c_i\). Conversely, such a monomial linear map is an isomorphism precisely when
\[
 a_{ij}c_j=c_i^2b_{\sigma(i),\sigma(j)}\qquad\text{for all }i,j.\tag{1}
\]
This establishes the exact equivalence used below in every characteristic.

**Step 2: a graph encoding of all scalings.** Choose a primitive element \(g\) of \(K^\times\). For a structure matrix \(A\), put
\[
 X_A=\{(i,t):1\le i\le n,\ t\in K^\times\}.
\]
Define two ordered binary relations on \(X_A\):
\[
 R_1(A)=\{((i,t),(i,gt)):i,t\},
\]
\[
 R_2(A)=\{((i,t),(j,a_{ij}t^2)):
          a_{ij}\ne0,\ t\in K^\times\}.
\]
The connected components of the directed cycle relation \(R_1\) are exactly the fibers over the indices \(i\). For \(q=2\) these components are singleton loops; the same argument applies. Hence every bijection preserving \(R_1\) maps each fiber to another and acts on the field coordinate by multiplication by some \(c_i\):
\[
 (i,t)\longmapsto(\sigma(i),c_it).
\]
Preservation of \(R_2\) implies matching zero/nonzero support and, for every nonzero \(a_{ij}\),
\[
 c_ja_{ij}t^2=b_{\sigma(i),\sigma(j)}(c_it)^2.
\]
Canceling \(t^2\) yields (1). Conversely, every monomial isomorphism satisfying (1) gives precisely this bijection preserving both relations. Thus the two relational structures are isomorphic **if and only if** the corresponding perfect algebras are isomorphic.

The cardinality of \(X_A\) is \(n(q-1)\), and the total number of relation pairs is at most \((n+n^2)(q-1)\). A fixed finite collection of binary relations reduces to ordinary uncolored graph isomorphism by creating an incidence vertex for each relation pair with separately recognizable source, target and relation-type attachments. Fixed vertex colors can themselves be replaced with constant-size marker gadgets. Both transformations are polynomial time; the output is polynomial in \(n\) for fixed \(q\). This proves membership in GI.

**Step 3: graph-isomorphism hardness on unipotent structure matrices.** Let \(G\) be a finite simple undirected graph with \(n\ge1\) vertices and \(m\) edges. Let \(C_G\) be its \(n\)-by-\(m\) vertex-edge incidence matrix, viewed over \(K\). Define \(E_G\) by the structure matrix
\[
 M_G=\begin{pmatrix}I_n&C_G\\0&I_m\end{pmatrix}.
\]
The determinant is one, so \(E_G\) is perfect in every characteristic. Its directed support graph has a loop at every vertex; moreover, each original graph vertex points to precisely those edge-nodes incident with it. Every original vertex-node has indegree one (its loop); every edge-node has indegree three (its loop and its two distinct endpoints), and no other kinds of nodes occur. Therefore every support-digraph isomorphism preserves the two node types and restricts to an isomorphism of the original undirected graphs. Conversely, every isomorphism \(G\cong H\) acts on vertices and induced edges, giving a simultaneous row-and-column permutation of \(M_G\) into \(M_H\), hence an isomorphism \(E_G\cong E_H\).

By Step 1 any algebra isomorphism induces a directed support-graph isomorphism. Consequently,
\[
 G\cong H\quad\Longleftrightarrow\quad E_G\cong E_H.
\]
The construction uses \(n+m\) basis elements, and the matrices are computable in polynomial time. This proves GI-hardness even for the stated restricted block-unitriangular matrices. Combining Steps 2 and 3 proves the theorem.

## Verification

The standalone `check.py` enumerates all invertible \(2\)-by-\(2\) matrices over \(\mathbb F_2\) and \(\mathbb F_3\), compares every pair using two **independent** searches (monomial algebra maps versus all vertex permutations preserving both relations), and checks further deterministic samples for \(3\)-by-\(3\) matrices over \(\mathbb F_2\) and \(2\)-by-\(2\) matrices over \(\mathbb F_5\). It also constructs and verifies the incidence reduction for every labeled undirected graph of orders one through five over three fields. Run `python3 check.py` from the package directory; successful completion prints `VERIFY_OK`.

The universal complexity statements depend on the above proofs. Finite checks alone would not establish the claimed all-dimension reduction.

## Relationship to prior work

The October 2026 evolution-algebra survey explicitly asks in Question 50 for the complexity of perfect evolution-algebra isomorphism over finite fields relative to graph isomorphism [1]. The monomial-rigidity step is established earlier by Elduque and Labra [2] and is also presented as Theorem 2.4 in Costoya, Mayorga and Viruel [3]. The graph-to-algebra incidence embedding in Step 3 is closely related to the explicit 2025 graph-automorphism realizations in [3], so it is **not** represented as an unrelated discovery. The contribution claimed here is the **complete fixed-field polynomial-time equivalence**, especially the \(n(q-1)\)-vertex cyclic-fiber encoding that preserves *isomorphisms*, including the diagonal scalar constraints.

Falcón, Falcón and Núñez [4] previously constructed total-colored graphs associated with finite-field evolution algebras to encode **isotopisms**; the cited general construction indexes nonzero products of arbitrary algebra elements, whose count can grow exponentially with dimension at fixed field size. The present proof is different both in its monomial-isomorphism condition and its linear-size fixed-field vertex construction. The literature on graph evolution algebras and random walks [5] deals with isomorphism of other associated algebra constructions rather than giving the all-input fixed-field GI classification.

## Limitations

The conclusion is for each fixed finite field. The graph encoding has size proportional to \(q\); therefore the argument alone does not prove membership in GI with complexity polynomial in \(\log q\) when the field order varies as part of the input. It also does not extend to nonperfect evolution algebras without additional arguments, because their natural-basis changes need not be monomial. The proof does not establish graph-isomorphism membership for general finite-dimensional nonassociative algebra isomorphism. Earlier graphical encodings or unindexed complexity results may imply the same equivalence; an independent literature review has not been performed.

## References

[1] I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (October 15, 2026), Question 50. https://arxiv.org/html/2610.22248

[2] A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685; J. Algebra Appl. **14** (2015), 1550103. https://arxiv.org/abs/1312.4685

[3] C. Costoya, P. Mayorga and A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterr. J. Math. **22** (2025), 149, especially Theorem 2.4 and Section 5. https://doi.org/10.1007/s00009-025-02924-0

[4] R. M. Falcón, Ó. J. Falcón and J. Núñez, *An Application of Total-Colored Graphs to Describe Mutations in Non-Mendelian Genetics*, Mathematics **7** (2019), 1068. https://doi.org/10.3390/math7111068

[5] P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516 (2017). https://arxiv.org/abs/1710.10516

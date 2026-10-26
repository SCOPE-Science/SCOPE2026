# Finite-field reconstruction from commuting graphs of complete multipartite graphical Lie algebras

## Finding
Let \(q\) be any **odd prime power** and let \(G=K_{n_1,\ldots,n_s}\), where \(s\ge2\) and all \(n_i\ge1\). Let \(L(G,q)\) be the two-step nilpotent graphical Lie algebra over \(\mathbb F_q\), with an independent central generator for each edge of \(G\). Write
\[
N=\sum_{i=1}^{s}n_i,\qquad E=\sum_{1\le i<j\le s}n_i n_j,\qquad c=q^E,
\qquad d=\frac{q^N-1-\sum_{i=1}^s(q^{n_i}-1)}{q-1}.
\]
Define the **full commuting graph** \(\mathcal C(L)\) to have one vertex for *every element* of \(L\), with two distinct vertices adjacent exactly when their Lie bracket vanishes. Then
\[
\boxed{\mathcal C(L(G,q))\ \cong\ K_c\ \vee\ \left(\bigsqcup_{i=1}^{s}K_{c(q^{n_i}-1)}\ \sqcup\ dK_{c(q-1)}\right).}
\]
Here \(K_m\) is a complete graph on \(m\) vertices, \(\sqcup\) is disjoint union, and \(\vee\) is graph join. In particular, \(d\) is a strictly positive integer.

**Inverse classification.** Within this entire family, two full commuting graphs are isomorphic if and only if their field orders agree and their unordered multisets of multipartite block sizes agree. No field order is supplied to the reconstruction algorithm. Thus the commuting graph alone determines \(q\) and \(\{n_1,\ldots,n_s\}\), and hence determines the original complete multipartite graph.

The same centralizer classification gives the complete adjoint-rank polynomial
\[
\boxed{\sum_{x\in L(G,q)}z^{\operatorname{rank}(\operatorname{ad}_x)}
=c\left(1+\sum_{i=1}^s(q^{n_i}-1)z^{N-n_i}
+\left[q^N-1-\sum_{i=1}^s(q^{n_i}-1)\right]z^{N-1}\right).}
\]
Terms with equal exponents are combined. An exact ordered-pair commuting probability is
\[
\boxed{\Pr([X,Y]=0)=q^{-2N}\left(q^N+\sum_{i=1}^s(q^{n_i}-1)q^{n_i}
+q\left[q^N-1-\sum_{i=1}^s(q^{n_i}-1)\right]\right),}
\]
for independent uniform elements \(X,Y\in L(G,q)\).

## Assumptions and scope
The graph is simple, complete multipartite, and has at least two nonempty parts. Every original graph edge has its *own* central basis vector. Repeated-edge-label versions of the graphical Lie construction are **not** included. The coefficient field is an arbitrary finite field of odd order, without requiring the order to be prime. The zero element and all other central elements are included as vertices of the **full** commuting graph. This differs from conventions restricting vertices to noncentral elements, or to projective lines in the central quotient. The result asserts reconstruction only **within the stated family**; it does not characterize all Lie algebras with the same commuting graph.

Explicitly, let \(V_i=\mathbb F_q^{n_i}\), \(V=\bigoplus_i V_i\), and \(Z=\bigoplus_{i<j}(V_i\otimes_{\mathbb F_q}V_j)\). On \(L=V\oplus Z\), set \([Z,L]=0\) and, for \(u,v\in V\), set the component in \(V_i\otimes V_j\) equal to \(u_i\otimes v_j-v_i\otimes u_j\). This is exactly the uniquely edge-labeled graphical Lie algebra. It is alternating and satisfies Jacobi because all brackets land in the central subspace \(Z\).

## Proof
**1. Center and centralizers.** The center is exactly \(Z\): any nonzero component \(x_i\in V_i\) has a nonzero bracket with a suitable vector supported in a different part. Indeed, select such a part \(j\), choose nonzero \(v_j\), and obtain the nonzero pure tensor \(x_i\otimes v_j\) (or its negative) in the edge component.

Let \(x=(x_1,\ldots,x_s)\in V\setminus\{0\}\), with support \(S=\{i:x_i\ne0\}\). A vector \(y=(y_1,\ldots,y_s)\) commutes with \(x\) exactly when
\[
x_i\otimes y_j=y_i\otimes x_j \quad\text{for all }i<j.
\]
If \(S=\{i\}\), then these equalities force \(y_j=0\) for all \(j\ne i\), and impose no condition on \(y_i\). Hence \(C_L(x)=V_i\oplus Z\).

If \(|S|\ge2\), choose distinct \(i,j\in S\). Equality of the two pure tensors forces \(y_i=\lambda x_i\) and \(y_j=\lambda x_j\) for one scalar \(\lambda\): this follows by applying linear functionals taking value one on the two fixed nonzero vectors. Using one fixed active index against every other active index gives the *same* \(\lambda\). Comparing that index against every inactive index forces all corresponding \(y_j\) to vanish. Thus \(C_L(x)=\mathbb F_qx\oplus Z\). The central component of an element never changes its centralizer. Therefore, for a noncentral \(x\),
\[
\boxed{C_L(x)/Z=\begin{cases}V_i,&x\bmod Z\in V_i\setminus\{0\},\\
\mathbb F_q(x\bmod Z),&x\bmod Z\text{ has support in at least two parts}.\end{cases}}
\]

**2. Commuting components.** Distinct central elements commute with everything, yielding the universal clique \(K_c\). No noncentral element is universal because the center is exactly \(Z\). Remove these \(c\) vertices. For each part \(i\), all elements whose noncentral component lies in \(V_i\setminus\{0\}\) mutually commute, giving one clique of order \(c(q^{n_i}-1)\). For each projective line \(\ell\subset V\) not contained in a single part, all elements with noncentral component in \(\ell\setminus\{0\}\) form a clique of order \(c(q-1)\). The preceding centralizer calculation proves that no edges connect any two different cliques. There are \((q^N-1)/(q-1)\) projective lines in \(V\), of which \(\sum_i(q^{n_i}-1)/(q-1)\) lie in individual parts. Their difference is \(d\). At least one line contains a vector with nonzero components in two parts, so \(d>0\). This proves the graph decomposition.

**3. Reconstruction across field orders.** Suppose only the abstract full commuting graph is given, known to belong to this family. Its universal vertices are exactly the center, and their number \(c\) is therefore intrinsic. Delete them and list the orders of the resulting connected components, each a clique. Let \(b\) be the smallest of those orders. Since \(d>0\) and \(q^{n_i}-1\ge q-1\),
\[
b=c(q-1),\qquad\boxed{q=1+b/c}.
\]
Thus even the field order is recovered. The total graph order is \(q^{N+E}=cq^N\), hence \(N\) is the unique integer satisfying \(q^N=|V(\mathcal C(L))|/c\). Every connected component strictly larger than \(b\) has order \(c(q^a-1)\) for one multipartite part of size \(a\ge2\); recover its size uniquely as the integer \(a\) with \(q^a=1+|C|/c\), with multiplicity. The remaining number of singleton parts is precisely \(N\) minus the sum of these recovered sizes. This recovers the whole unordered multiset. Conversely, equal parameters give isomorphic graphs by the explicit decomposition.

**4. Adjoint ranks and commutation frequency.** Since \(\ker(\operatorname{ad}_x)=C_L(x)\), the center contributes \(c\) rank-zero elements; a single active part \(i\) contributes \(c(q^{n_i}-1)\) rank-\((N-n_i)\) elements; and all remaining noncentral elements contribute rank \(N-1\). This proves the polynomial. For the probability, sum \(|C_L(x)|\) over the same three cases. The centralizers have respective orders \(q^{N+E}\), \(q^{n_i+E}\), and \(q^{1+E}\). Divide the sum by \(q^{2(N+E)}\) to obtain the displayed probability.

## Verification
The standalone standard-library script `verify.py` constructs the bilinear Lie brackets coordinate by coordinate, rather than using the claimed centralizer formula to decide commutation. It enumerates all nonzero quotient vectors over several small prime fields, computes the connected components of the resulting commuting relation, independently counts all point-centralizers, and reconstructs the field and unordered part sizes from those components. It tests twelve configurations over fields of orders \(2,3,5,7\), including cases with singleton parts, repeated block sizes, and more than two parts. The characteristic-two configurations are additional implementation stress checks, not part of the stated odd-characteristic theorem. The script terminates with `VERIFY_OK 12 independent bracket cases`.

As an illustrative example, for \(q=3\) and block sizes \((2,1)\), one has \(N=3\), \(E=2\), \(c=9\), and \(d=8\). The full commuting graph is
\[
K_9\vee(K_{72}\sqcup9K_{18}),
\]
with \(243\) vertices. Its nine universal vertices and smallest noncentral clique size \(18\) recover \(q=1+18/9=3\), and the unique larger clique recovers the block of size two.

## Relationship to prior work
Godoy Molina and Lagos (2023, arXiv:2308.00272) construct the uniquely edge-labeled two-step Lie algebras and study graph ideals, orientation changes, and strata-preserving derivations, including two labelings of complete bipartite graphs; the full commuting graph and inverse field/block reconstruction are different invariants. Chareh Khah Moghaddam, Erfanian, and Shamsaki (2024, arXiv:2406.15902) introduce and analyze the *noncommuting* graph with noncentral vertices and give general graph and isomorphism results, not the above multipartite full-commuting-clique census. Sriwongsa (2025, arXiv:2505.00726) proves general complete-multipartite structure of the **projective noncommuting graph** for AC Lie algebras; this supplies relevant broader context but does not state the full-vertex clique sizes or recovery of a varying field order and every multipartite block size for these graph algebras. A general equivalence under other terminology remains possible; no exhaustive priority claim is made.

## Limitations
The assumptions about complete multipartite graphs and distinct edge labels are essential to the tensor argument. The theorem does not extend automatically to repeated-label graphical Lie algebras, arbitrary graphs, or graph reconstruction among all finite Lie algebras. The verification uses prime fields and finite sizes; it is not a proof for arbitrary prime powers. The all-parameter result follows from the preceding tensor proof. Literature inspection and searches do not certify exhaustive novelty, and no independent audit has been performed.

## References
1. M. Godoy Molina and D. Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272, first posted 2023-08-01. https://arxiv.org/abs/2308.00272
2. A. Chareh Khah Moghaddam, A. Erfanian, and A. Shamsaki, *On the non-commuting graph associated to a finite-dimensional Lie algebra*, arXiv:2406.15902, first posted 2024-06-22. https://arxiv.org/abs/2406.15902
3. S. Sriwongsa, *Non-commuting graphs of projective spaces over central quotients of Lie algebras*, arXiv:2505.00726, first posted 2025-04-27. https://arxiv.org/abs/2505.00726

# Exact power-graph component sizes of full transformation semigroups from kernel-fiber profiles

## Finding
Let \(X\) be a labeled set of \(n\ge1\) points. Write \(T_X\) for the full transformation semigroup, with composition as multiplication, and let \(\mathcal P(T_X)\) be its simple undirected power graph: distinct vertices \(f,g\) are joined precisely when one is a positive power of the other. For an idempotent \(e\in T_X\), write its fixed roots as \(R=\{r_1,\ldots,r_k\}\), its fibers as \(F_i=e^{-1}(r_i)\), and \(m_i=|F_i|\ge1\). Put \(b_i=m_i-1\). Denote by \(C_e\) the power-graph component containing \(e\).

**Theorem.** The components are indexed bijectively by idempotents \(e\), and the exact cardinality of the component corresponding to \(e\) is
\[
|C_e|=\sum_{\sigma\in S_k}\left(\prod_{i=1}^k m_{\sigma(i)}^{\,m_i-1}\right)
\prod_{B\in\operatorname{Cyc}(\sigma)}\left(1-\prod_{i\in B}\frac{m_i-1}{m_i}\right).
\]
Here \(\operatorname{Cyc}(\sigma)\) is the set of cycles of the permutation \(\sigma\), viewed as disjoint subsets of \(\{1,\ldots,k\}\), and the empty-product convention is one. This formula is valid without restrictions on the fiber sizes, including \(n=1\).

The component order depends only on the multiset \(\{m_1,\ldots,m_k\}\), not the labels or the locations of the roots. The first divergence among component orders for the same idempotent rank occurs at \(n=5\): rank-two idempotents of fiber sizes \((4,1)\) have component order \(17\), while those of sizes \((3,2)\) have component order \(11\). There are respectively \(20\) and \(60\) such components in \(T_5\).

## Assumptions and scope
All sets are finite, all maps are total self-maps, and the power graph uses **all** transformations (not only singular transformations). The graph contains the idempotents and its edges are undirected. The rank of an idempotent means the cardinality of its image. The formula counts labeled transformations and vertices, not isomorphism types of functional digraphs. It specializes to the known \(|C_{\mathrm{id}}|=n!\) and \(|C_e|=(n-1)!\) at ranks \(n\) and \(n-1\), and gives \(|C_e|=n^{n-2}\) for a constant idempotent when \(n\ge2\), with the value one at \(n=1\). For any \(n\), the number of components is the classical number of idempotents \(\sum_{k=1}^n\binom nk k^{n-k}\).

## Proof
**1. Unique eventual idempotent.** For each \(f\in T_X\), the functional digraph comprises directed cycles with finite in-trees. For every sufficiently large positive multiple \(M\) of all cycle lengths, \(f^M\) fixes all cyclic vertices and sends every other vertex to one of them. Hence \(e_f=f^M\) is idempotent and is independent of sufficiently large common multiples. If \(g=f^t\) for some positive \(t\), then \(e_g=e_f\), since \(f^{tM}=f^M\) for sufficiently large such \(M\). Thus every power-graph edge preserves the eventual idempotent. Conversely each \(f\) is adjacent to \(e_f\) unless already equal, so every fiber \(\{f:e_f=e\}\) is connected through \(e\), and distinct such fibers are disconnected. It follows that \(C_e=\{f:f^M=e\text{ for some }M\ge1\}\).

**2. Permuted fibers.** Fix \(e\) as in the statement. If \(f^M=e\), then \(fe=ef\), and \(f^M\) restricts to the identity on \(R\). Consequently \(f|_R\) is a permutation, say \(f(r_i)=r_{\sigma(i)}\), and for every \(x\in F_i\),
\[
e(f(x))=f(e(x))=r_{\sigma(i)},\qquad\text{so }f(x)\in F_{\sigma(i)}.
\]
The functional digraph has no cycle outside \(R\), since any vertex on such a cycle would be fixed by the sufficiently large power \(f^M=e\) and hence lie in \(R\). Conversely, if \(f\) permutes the roots by \(\sigma\), takes every \(F_i\) into \(F_{\sigma(i)}\), and has no directed cycle outside \(R\), then each orbit eventually reaches a root. If the orbit of \(x\in F_i\) reaches a root after \(d\) steps, it is \(r_{\sigma^d(i)}\) by the fiber condition; therefore a sufficiently large multiple \(M\) of the order of \(\sigma\) satisfies \(f^M(x)=r_{\sigma^M(i)}=r_i=e(x)\) for every \(x\). Thus these conditions are necessary and sufficient for \(f\in C_e\).

**3. Directed-forest determinant.** Fix the root permutation \(\sigma\). Set \(U=X\setminus R\) and \(U_i=F_i\setminus\{r_i\}\); thus \(|U_i|=b_i\). We must count functions assigning to every \(x\in U_i\) one outgoing arrow to any vertex of \(F_{\sigma(i)}\), subject to no directed cycles wholly in \(U\). For each \(x\in U_i\) there are \(m_{\sigma(i)}\) candidate targets, exactly one of which is a root. Let \(L\) be the \(|U|\times|U|\) matrix whose entry indexed by \(x,y\in U\) is
\[
L_{xy}=m_{\sigma(i)}\mathbf1_{x=y}-\mathbf1_{y\in U_{\sigma(i)}}\quad\text{when }x\in U_i.
\]
The directed all-minors matrix-tree identity gives that the number of such rooted forests is \(\det L\). For completeness this version can be checked by expanding \(\det L\) multilinearly from its diagonal choices and off-diagonal arrows: the signed terms cancel assignments containing a directed cycle within \(U\); precisely the acyclic assignments remain with coefficient one. Self-loop choices cancel in the same way. If \(U\) is empty, this determinant is one by convention.

Define the positive diagonal matrix \(D_{xx}=m_{\sigma(i)}\) for \(x\in U_i\), and rectangular matrices \(P_{xi}=\mathbf1_{x\in U_i}\), \(Q_{iy}=\mathbf1_{y\in U_{\sigma(i)}}\). Then \(L=D-PQ\), and the determinant lemma gives
\[
\det L=\left(\prod_i m_{\sigma(i)}^{b_i}\right)\det(I_k-QD^{-1}P).
\]
The matrix \(M=QD^{-1}P\) has at most one nonzero entry in each row, namely
\[
M_{i,\sigma(i)}=\frac{b_{\sigma(i)}}{m_{\sigma^2(i)}}.
\]
Restricting \(I_k-M\) to a cycle \(B\) of \(\sigma\) and expanding its determinant yields \(1-\prod_{i\in B}b_i/m_i\), because the denominators and numerators cycle through each of the same indices. Multiplying the independent cycle determinants gives the summand claimed in the theorem. Summing over the disjoint choices of \(\sigma\in S_k\) proves the formula. The determinant shows that the rational-looking summands are nonnegative integers; no divisions need be performed in an implementation.

**4. First fiber-profile distinction.** For \(n=5\) and rank two, profiles are precisely \((4,1)\) and \((3,2)\). For \((4,1)\), the identity permutation contributes \(16\) rooted forests and the swap contributes \(1\), so the component order is \(17\). For \((3,2)\), the identity contributes \(3\) and the swap contributes \(8\), giving \(11\). Choose the two distinct roots in \(\binom52=10\) ways. For \((4,1)\) there are two ways to assign all three other points to one of the roots, giving \(20\) idempotents; for \((3,2)\) there are six assignments, giving \(60\). For \(n\le4\), direct substitution in the displayed formula shows a common order at each fixed rank, establishing that \(n=5\) is the first distinction.

## Verification
The accompanying standard-library Python script `verify.py` enumerates all \(n^n\) self-maps for every \(1\le n\le6\), computes the eventual idempotent by taking a common multiple of all cycle lengths, and independently compares each observed fiber cardinality with the exact rational-expression formula. It also explicitly constructs power-graph edges and connected components for \(1\le n\le5\) and checks they coincide with eventual-idempotent fibers. It reproduces the complete \(n=5\) profile breakdown: five components of order \(125\), twenty of order \(17\), sixty of order \(11\), thirty plus sixty of order \(10\), twenty of order \(24\), and one of order \(120\), totaling \(5^5=3125\) vertices. Run with `python3 verify.py`; the success marker is `VERIFY_OK`. The proof above establishes the result for arbitrary \(n\), independently of enumeration.

## Relationship to prior work
Zeng, Cheng, Yang and Shao (2025) proved that every connected component of the power graph of \(T_X\) has a unique idempotent and established the qualitative membership characterization and the group cases of rank \(n\) and \(n-1\) (Theorem 3.13 and related results). Those statements are used as background, though Step 1 also proves the necessary indexing directly. Their paper does not give the displayed kernel-fiber-dependent cardinality formula or the \(17\)-versus-\(11\) rank-two split at \(n=5\). Eze, Imam and Balarabe (2026) give a direct graph description for \(T_3\), including its ten components, and investigate other structural properties; their \(n=3\) count agrees with the specialization here. The new statement is the explicit all-rank count by fiber profile, derived using constrained directed-forest enumeration, not the already known existence of the idempotent index. The classical directed matrix-tree principle is employed as an enumeration tool, not claimed as new.

## Limitations
The formula gives the number of vertices in each component but not its internal edge count, diameter, full automorphism group or graph isomorphism class. The calculations concern the full transformation semigroup and do not automatically apply to partial, order-preserving or restricted transformation semigroups. Earlier sources characterize component membership; the possibility of an equivalent component-size enumeration in older transformation enumeration or forest-counting literature is a residual historical risk. Finite checks through \(n=6\) corroborate, but cannot certify, the theorem for all \(n\).

## References
1. L. Zeng, Y. Cheng, B. Yang, Y. Shao, *Power graphs of full transformation semigroups*, Filomat 39(8) (2025), 2725–2735, https://doi.org/10.2298/FIL2508725Z. In particular Sections 3–4 and Theorem 3.13.
2. C. Eze, A. T. Imam, M. Balarabe, *Structural properties of the power graph of the full transformation semigroup*, J. Semigroup Theory Appl. 2026 (2026), Article 5, first publicly posted September 29, 2026, https://doi.org/10.28919/jsta/9965. In particular Section 4's explicit \(n=3\) components.
3. Classical directed matrix-tree theorem (rooted-forest determinant form); the special case needed here is explained in the proof.

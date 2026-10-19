# Triangles and sharp cliques in the center-avoiding Heisenberg comaximal graph

## Finding
Let \(q\) be a prime power, \(n\ge 3\), and let \(H_n(q)\) be the \((2n+1)\)-dimensional Heisenberg Lie algebra over \(\mathbb F_q\). Let \(X_n(q)\) be the induced subgraph of its comaximal graph on the nonzero proper Lie subalgebras intersecting the one-dimensional center trivially. Here two distinct subalgebras are adjacent if their generated Lie algebra is all of \(H_n(q)\).

Write
\[
 L_n(q)=\prod_{i=1}^n(q^i+1),\qquad
 C_n(q)=q^{n(n+1)/2}.
\]
Define the nonsingular symmetric-matrix count \(S_n(q)\) by
\[
 S_0(q)=1,\quad S_1(q)=q-1,\quad
 S_k(q)=(q-1)q^{k-1}S_{k-1}(q)
 +(q^{k-1}-1)q^{k-1}S_{k-2}(q)\quad(k\ge2).
\]
Then \(X_n(q)\) is a disjoint union of isolated vertices and a \(q^n\)-fold independent-set blow-up of the oppositeness graph on Lagrangian subspaces of a symplectic \(2n\)-space. Its nonisolated part has
\[
 |V_{\mathrm{active}}|=q^nL_n(q),\qquad
 \deg=q^{n(n+3)/2},
\]
\[
 |E|=\frac{L_n(q)}2q^{n(n+5)/2},\qquad
 \boxed{\#\text{triangles}=\frac{L_n(q)}6q^{n(n+7)/2}S_n(q)},
\]
and its exact clique number is
\[
 \boxed{\omega(X_n(q))=q^n+1}.
\]
The number of isolated vertices is exactly
\[
 I_n(q)=\sum_{s=1}^{n-1}q^s
 \frac{\prod_{j=0}^{s-1}(q^{2n-j}-q^j)}
 {\prod_{j=0}^{s-1}(q^s-q^j)}.
\]
The corresponding closed symmetric-matrix count is
\[
 S_{2r}(q)=q^{r(r+1)}\prod_{j=1}^r(q^{2j-1}-1),\qquad
 S_{2r+1}(q)=q^{r(r+1)}\prod_{j=1}^{r+1}(q^{2j-1}-1).
\]
In particular, for \(n=3,q=2\), the induced graph has \(1080\) active vertices, \(1386\) isolates, valency \(512\), \(276480\) edges, \(20643840\) triangles, and clique number \(9\).

## Assumptions and scope
The result applies to every prime-power field, including characteristic two, and every integer \(n\ge3\). Fix a symplectic vector space \((V,\langle\ ,\ \rangle)\) of dimension \(2n\). Define \(H_n(q)=V\oplus \mathbb F_q z\), with \([u+az,v+bz]=\langle u,v\rangle z\). The center is exactly \(\mathbb F_q z\). A Lagrangian means an \(n\)-dimensional totally isotropic subspace of \(V\). An independent-set blow-up of multiplicity \(m\) replaces each base vertex by \(m\) nonadjacent clones and each base edge by a complete bipartite graph. All triangles are unordered triples of pairwise distinct vertices. The investigated graph is the specified *induced* center-avoiding subgraph, not the full comaximal graph; isolated vertices here can have neighbors outside the induced subgraph.

## Proof
**1. Classification and generation.** If \(A\le H_n(q)\) is a Lie subalgebra with \(A\cap\mathbb F_qz=0\), projection \(\pi:A\to V\) is injective. For \(u,v\in\pi(A)\), their lifts have bracket \(\langle u,v\rangle z\in A\), hence \(\langle u,v\rangle=0\). Thus \(U=\pi(A)\) is totally isotropic. Conversely every nonzero totally isotropic \(s\)-space \(U\) and every linear functional \(\ell\in U^*\) define a Lie subalgebra \(A(U,\ell)=\{u+\ell(u)z:u\in U\}\). These are all such subalgebras and there are exactly \(q^s\) over each \(U\).

For two such \(A(U,\ell)\), \(A(W,m)\), the projection of the Lie algebra they generate is exactly \(U+W\), because all brackets are central. If \(U+W=V\), the cross-pairing is nonzero somewhere: otherwise \(U+W\) would be totally isotropic, contradicting nondegeneracy and positive dimension. Therefore a nonzero bracket generates the center and the generated algebra is all \(H_n(q)\). Conversely full generation requires \(U+W=V\). Since \(\dim U,\dim W\le n\), this occurs exactly when \(U\) and \(W\) are complementary Lagrangians. Smaller isotropic projected subspaces therefore give isolated vertices of \(X_n(q)\); the \(q^n\) lifts above each Lagrangian are pairwise nonadjacent, and two distinct fibers are completely joined precisely for opposite Lagrangians.

**2. Counting Lagrangians and isolates.** Count isotropic ordered independent \(s\)-tuples iteratively. Given an isotropic independent \(j\)-tuple, the next vector can be chosen in its \((2n-j)\)-dimensional orthogonal complement, outside its \(j\)-dimensional span: \(q^{2n-j}-q^j\) choices. Divide by the number \(\prod_{j=0}^{s-1}(q^s-q^j)\) of ordered bases of an \(s\)-space. This proves the isolate formula. In the Lagrangian case, the standard double count of pairs (isotropic line, containing Lagrangian) gives \(L_n(q)=(q^n+1)L_{n-1}(q)\), with \(L_0(q)=1\), hence the stated product.

**3. Opposite Lagrangians and common complements.** Fix opposite Lagrangians \(L,M\) with \(V=L\oplus M\). The symplectic form identifies \(L\cong M^*\). Every Lagrangian transverse to \(L\) is the graph of a linear map \(M\to L\) represented by a symmetric \(n\times n\) matrix, giving \(C_n(q)=q^{n(n+1)/2}\) complements to \(L\). A third Lagrangian transverse to both \(L\) and \(M\) corresponds exactly to an *invertible* symmetric matrix; hence every ordered opposite pair has \(S_n(q)\) common opposite Lagrangians.

For completeness, split symmetric matrices of order \(k\) by their top-left entry \(a\). If \(a\ne0\), Schur complementation gives \((q-1)q^{k-1}S_{k-1}\) nonsingular matrices. If \(a=0\), the remaining first-row vector \(v\) must be nonzero. For any fixed \(v\ne0\), a congruence change on the remaining coordinates sends it to a standard coordinate vector; nonsingularity reduces to an arbitrary nonsingular symmetric block of order \(k-2\), with \(q^{k-1}\) unconstrained entries. This gives \((q^{k-1}-1)q^{k-1}S_{k-2}\). The recurrence follows in all characteristics; induction yields both closed products.

**4. Numerical invariants.** There are \(L_n(q)\) base vertices, each with \(C_n(q)\) opposite Lagrangians. Each base vertex has \(q^n\) lifts, so valency is \(q^nC_n(q)\). The number of edges is \(L_n(q)C_n(q)q^{2n}/2\). The number of ordered base triangles is \(L_n(q)C_n(q)S_n(q)\), and each lifts in exactly \(q^{3n}\) ways; division by six proves the triangle formula. The first-example values follow by \(L_3(2)=135\), \(C_3(2)=64\), \(S_3(2)=28\), and the isotropic-subspace counts above.

**5. Sharp clique number.** Any clique of positive size at least two contains at most one lift of each base Lagrangian. The Lagrangians in a base clique are mutually complementary, hence have disjoint nonzero vector sets, yielding \(r(q^n-1)\le q^{2n}-1\) and \(r\le q^n+1\). Equality is attained by a symplectic spread: let \(K=\mathbb F_{q^n}\) and view \(V=K^2\) over \(\mathbb F_q\), with \(\langle(x,y),(u,v)\rangle=\operatorname{Tr}_{K/\mathbb F_q}(xv-yu)\). Its \(q^n+1\) one-dimensional \(K\)-subspaces are pairwise complementary \(\mathbb F_q\)-Lagrangians. Taking one lift above each gives the asserted clique. The trace form is nondegenerate because the field extension is separable.

## Verification
The standalone standard-library script `verify.py` constructs canonical reduced-row-echelon representatives of all totally isotropic subspaces over prime fields, checks their exact counts, counts complementary Lagrangian pairs and common complements, verifies the symmetric-matrix recurrence by independent matrix enumeration, and checks the rank of Lie brackets and generators for all center-avoiding pairs in the smaller cases. It also checks the \(n=3,q=2\) triangle count. The five checked instances are \((q,n)=(2,1),(3,1),(2,2),(3,2),(2,3)\), all producing `VERIFY_OK`. The first four are verification boundaries; only \(n\ge3\) is claimed as new. The proof, not this finite sample, covers every prime-power field and every \(n\ge3\). Run `python verify.py` in the directory containing the embedded script.

## Relationship to prior work
Towers, Zuleta and Gutierrez introduced Lie-algebra comaximal graphs in arXiv:2605.09583 (first public May 10, 2026), treating dimensions up to three. Their follow-up arXiv:2608.16575 (first public August 17, 2026) counts triangles in dimensions three and studies several four-dimensional algebras. Neither inspected work treats center-avoiding Heisenberg subalgebras in dimensions at least seven. An existing result on the five-dimensional Heisenberg comaximal graph gives detailed valencies and describes isotropic projection fibers and their complements; the present claim **does not claim** that five-dimensional case as new. Oppositeness of Lagrangians, symplectic spreads, and counts of invertible symmetric matrices are classical; the mathematical contribution here is the exact induced Lie-comaximal graph structure for all higher Heisenberg ranks and its matched triangle, isolate and sharp-clique enumeration.

## Limitations
The result does not classify the full graph on all Lie subalgebras, only the induced center-avoiding subgraph. It does not claim new elementary formulas for Lagrangian counts or nonsingular symmetric matrices themselves. Its novelty comparison covers accessible relevant papers and mathematical result records, not every unindexed treatment of symplectic dual-polar oppositeness or graph products. Computational verification samples only prime fields; the field-uniform theorem is proved algebraically. Independent external mathematical audit has not been performed.

## References
1. D. Towers, Y. Zuleta, I. Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants*, arXiv:2608.16575v1 (first public 2026-08-17), https://arxiv.org/abs/2608.16575.
2. D. A. Towers, Y. Zuleta, I. Gutierrez, *The comaximal graph of a finite-dimensional Lie algebra*, arXiv:2605.09583v1 (first public 2026-05-10), https://arxiv.org/abs/2605.09583.
3. Standard symplectic polar-space constructions (Lagrangian oppositeness and finite Desarguesian spreads) and classical finite-field counts of nonsingular symmetric matrices, both rederived as needed above.

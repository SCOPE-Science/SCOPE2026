# Fixed-point spheres and full orientation character of balanced higher-matching complexes

## Finding
For every integer \(n\ge2\), let \(X_n=M_{n-1}(K_{n,n})\) be the simplicial complex of subsets of the \(n^2\) edges of the complete balanced bipartite graph in which every vertex has selected degree at most \(n-1\). Write \(G_n=(S_n\times S_n)\rtimes C_2\) for the full graph automorphism group, and let \(s(i,j)=(j,i)\) be its natural bipartition exchange.

**Theorem.** Every involution in \(G_n\) exchanging the two vertex classes has geometric fixed-point space
\[
 |X_n|^{\langle s\rangle}\simeq S^{\binom{n}{2}-1}.
\]
The same statement holds with \(s\) replaced by any bipartition-exchanging involution. Furthermore, writing \(d=(n-1)^2-1\), the only nonzero reduced integral homology of \(X_n\) is in degree \(d\), and its full integral one-dimensional orientation character is
\[
\chi_n((\sigma,\tau)s^e)=\operatorname{sgn}(\sigma)^{n+1}\operatorname{sgn}(\tau)^{n+1}(-1)^{e(n-1)(n+2)/2}.
\]
Its full symmetry quotient has
\[
\widetilde H_i(|X_n|/G_n;\mathbb Q)\cong
\begin{cases}\mathbb Q,&n\equiv1\pmod4\text{ and }i=d,\\0,&\text{otherwise.}\end{cases}
\]
At \(n=2\), the fixed-point sphere is \(S^0\); the quotient statement continues to hold in reduced degree zero.

## Assumptions and scope
The group elements are written \((\sigma,\tau)s^e\), with \(\sigma,\tau\in S_n\) and \(e\in\{0,1\}\), acting on matrix coordinates by row and column relabeling, with the bipartition swap applied first. A *geometric fixed point* is a fixed point of the action on the realization, not necessarily a vertex fixed individually. All homotopy equivalences are ordinary (not equivariant) and all homology statements include integral orientations. The theorem covers every integer \(n\ge2\) and no unspecified degree ranges.

## Proof
**1. Identify the fixed simplicial complex.** The orbits of the transpose on the \(n^2\) matrix positions are the \(n\) diagonal singletons and the \(\binom n2\) unordered off-diagonal pairs, in natural bijection with the unordered pairs \(\{i,j\}\) allowing \(i=j\). Every point of \(|X_n|\) fixed by transpose has equal barycentric coordinates on the two members of each off-diagonal orbit. Dividing each orbit's total barycentric weight equally among its positions gives a piecewise-linear homeomorphism from the fixed-point set onto the realization of a simplicial complex \(D_n\) on \(m=n(n+1)/2\) orbit vertices. Its faces are exactly selections of loops and undirected edges of \(K_n\) in which no vertex has *all* of its \(n\) incident orbit vertices selected; a loop contributes one to that vertex's count. This loop convention differs from bounded-degree graph complexes in which a loop has degree two.

**2. Compute the homotopy type of the fixed complex.** For each \(i\in[n]\), let \(T_i\) be its incident orbit-star: the loop \(\{i,i\}\) together with \(\{i,j\}\) for all \(j\ne i\). Thus \(D_n\) has precisely the \(n\) sets \(T_i\), each of size \(n\), as its minimal nonfaces. Its combinatorial Alexander dual is
\[
 D_n^\vee=\bigcup_{i=1}^n\Delta(V\setminus T_i),\qquad |V|=m.
\]
For every proper collection of these simplices, their intersection is a nonempty simplex: an omitted index \(j\) leaves the loop \(\{j,j\}\) available. Their total intersection is geometrically empty. Every nonempty intersection is contractible, so the nerve lemma gives \(D_n^\vee\simeq\partial\Delta^{n-1}\simeq S^{n-2}\). Integral combinatorial Alexander duality therefore yields
\[
\widetilde H_k(D_n;\mathbb Z)\cong
\begin{cases}\mathbb Z,&k=m-n-1=\binom n2-1,\\0,&\text{otherwise.}\end{cases}
\]
For \(n=2\), the complex is an edge and an isolated vertex, hence \(S^0\). For \(n\ge4\), all subsets of at most three orbit vertices are faces, since the minimal nonfaces have size at least four; therefore \(D_n\) contains the complete two-skeleton and is simply connected. For \(n=3\), the only missing triangles are the three stars \(T_i\). Each such triangle boundary is filled by a three-triangle fan using a loop at a different vertex, so \(D_3\) is also simply connected. The integral homology calculation, Hurewicz theorem and homology Whitehead theorem now give \(D_n\simeq S^{\binom n2-1}\) for all \(n\ge3\).

Every class-exchanging involution has the form \((\sigma,\sigma^{-1})s\). It is conjugate to \(s\) within \(G_n\), so its fixed-point space has the same homotopy type.

**3. Determine the integral orientation character.** Singh's sphere theorem [1] establishes \(X_n\simeq S^d\) for \(d=(n-1)^2-1\). For the group action, take the combinatorial Alexander dual of \(X_n\) inside the simplex on \(E=[n]\times[n]\). The dual is covered by the \(2n\) simplices on complements of the \(n\) full rows and \(n\) full columns. Their nonempty intersection nerve is the join of the two simplex boundaries, \(\partial\Delta^{n-1}*\partial\Delta^{n-1}\simeq S^{2n-3}\). The cover-to-nerve isomorphism on integral homology is natural under the row, column and swap permutations. A row permutation \(\sigma\) has degree \(\operatorname{sgn}(\sigma)\) on this join, and similarly for columns. Exchanging the two join factors has degree \((-1)^{(n-1)^2}\), by the graded sign of interchanging the factors of a join.

Equivariant combinatorial Alexander duality multiplies this nerve orientation character by the sign of the induced permutation of the \(n^2\) vertices of the ambient simplex. A row permutation has ambient sign \(\operatorname{sgn}(\sigma)^n\), a column permutation \(\operatorname{sgn}(\tau)^n\), and matrix transpose has ambient sign \((-1)^{n(n-1)/2}\). Multiplying these factors proves the displayed character, since \(n(n-1)/2+(n-1)^2\) and \((n-1)(n+2)/2\) have the same parity.

**4. Compute the rational quotient.** After barycentric subdivision, finite-group averaging identifies rational homology of a simplicial quotient with the invariant rational homology of the original. If \(n\) is even, a row transposition acts by \(-1\), so there are no reduced invariants. If \(n\) is odd, both row and column groups act trivially, while class interchange acts by \((-1)^{(n-1)(n+2)/2}\). For odd \(n\) this sign is positive exactly when \(n\equiv1\pmod4\). This gives the quotient formula, including the reduced zero-dimensional case \(n=2\).

## Verification
The standalone `verify_matching_fixed.py` enumerates **all** faces of the fixed complex \(D_n\) for \(n=2,3,4\), calculates its full reduced mod-two Betti vector by independent bit-vector elimination, and finds respectively one class in degrees \(0,2,5\) and none elsewhere. Independently, for each \(n=2,3,4\) it enumerates all admissible original matching faces and computes exact signed fixed-simplex Lefschetz sums for five group elements: identity, a row transposition, a column transposition, class interchange, and a transposition followed by class interchange. Every computed top character agrees with the theorem's closed formula. Run `python verify_matching_fixed.py` using Python's standard library. The finite checks corroborate but do not replace the all-\(n\) proof.

## Relationship to prior work
Singh [1, Theorem 1.2] proves the ordinary sphere homotopy type \(X_n\simeq S^d\); that result is not claimed as new here. Reiner and Roberts [2, Theorem 3.3] describe the rational \(S_n\times S_n\) homology representation for the much larger family of generalized chessboard complexes. Their result covers the side-preserving subgroup in the present special case. The contribution here is the explicit homotopy type of **every class-exchanging involution's full geometric fixed-point space**, not determined by the ordinary sphere type or the side-preserving representation, together with the integral full-group extension and resulting all-parameter quotient dichotomy. No claim is made that novelty is proved by lack of an indexed match.

## Limitations
The theorem does not identify an equivariant homotopy equivalence to a linear representation sphere, does not compute integral quotient torsion, and does not classify fixed points for arbitrary subgroups. The fixed-point result concerns involutions exchanging the bipartition; an arbitrary class-exchanging element need not have order two. Finite calculations through \(n=4\) are independent corroborations only. A previously unindexed or differently formulated equivariant result may exist.

## References
[1] Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632 (first public version June 24, 2020), Theorem 1.2 and §4; https://arxiv.org/abs/2006.13632.

[2] Victor Reiner and Joel Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, Journal of Algebraic Combinatorics **11** (2000), 135–154, Theorem 3.3; https://www-users.cse.umn.edu/~rober005/chessmatch.pdf.

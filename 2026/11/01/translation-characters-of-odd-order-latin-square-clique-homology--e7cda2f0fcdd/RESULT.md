# Translation characters of odd-order Latin-square clique homology

## Finding
Let \(A\) be any finite abelian group of odd order \(n\ge5\). Its *group-table Latin-square graph* \(G_A\) has vertex set \(A\times A\), with two distinct vertices \((r,c)\) and \((s,d)\) adjacent precisely when \(r=s\), \(c=d\), or \(r+c=s+d\). Let \(X_A=\operatorname{Cl}(G_A)\) be its **full** clique complex. The translation group \(T=A\times A\) acts on \(X_A\) by \((u,v)(r,c)=(r+u,c+v)\).

Write \(V_A=\ker(\mathbb Q[A]\xrightarrow{\mathrm{sum}}\mathbb Q)\) for the rational augmentation module of the regular permutation representation, and write \(V_1,V_2,V_3\) for its pullbacks to \(T\) through \((u,v)\mapsto u\), \((u,v)\mapsto v\), and \((u,v)\mapsto u+v\), respectively. Then the complete nonzero reduced rational homology representation is
\[
\boxed{\ H_2(X_A;\mathbb Q)\cong_{\mathbb Q[T]}V_1\otimes_{\mathbb Q}V_2\otimes_{\mathbb Q}V_3.\ }
\]
All other reduced rational homology groups vanish. Explicitly, for every \((u,v)\in T\), the degree-two character is
\[
\boxed{\ \chi(u,v)=\big(n\mathbf 1_{u=0}-1\big)\big(n\mathbf 1_{v=0}-1\big)\big(n\mathbf 1_{u+v=0}-1\big).\ }
\]
Thus \(\chi(0,0)=(n-1)^3\); for a nonzero translation on exactly one of the three line-preserving axes, \(\chi=n-1\); for every other nonzero translation, \(\chi=-1\).

Let \(\widehat A\) denote the complex character group of \(A\). For each pair \((\alpha,\beta)\in\widehat A^2\), the multiplicity in \(H_2(X_A;\mathbb C)\) of the one-dimensional character \((u,v)\mapsto\alpha(u)\beta(v)\) is exactly
\[
\boxed{\ m_{\alpha,\beta}=n-\big|\{\mathbf1,\alpha,\beta\}\big|.\ }
\]
Consequently, the translation-fixed degree-two homology has dimension \(n-1\), and every character of \(T\) occurs with positive multiplicity. These formulas apply equally to cyclic and noncyclic finite abelian groups of odd order.

## Assumptions and scope
The group operation is written additively; \(0\) is its identity. A clique is a nonempty vertex subset whose distinct pairs are graph-adjacent; the full clique complex also contains the empty face. A fixed simplex means an **unordered** clique preserved setwise by the group element, not necessarily vertexwise. Simplicial chains have their usual alternating orientation, and fixed simplices contribute the sign of their induced vertex permutation.

The theorem is about \(H_2\) as a rational \(T\)-representation, not a proposed \(T\)-equivariant homotopy equivalence or an integral lattice isomorphism. The lower bound \(n\ge5\) is needed for the published all-field clique-homology theorem used below. Odd order excludes \(2\)-by-\(2\) group-table intercalates and ensures every nonidentity translation orbit has at least three vertices.

## Proof
**1. Translation action and the nonequivariant homology input.** Translation preserves equality of row coordinates, column coordinates, and sums, so it acts simplicially. An intercalate in the group table would involve distinct \(r_1,r_2\) and distinct \(c_1,c_2\) satisfying
\[
r_1+c_1=r_2+c_2,\qquad r_1+c_2=r_2+c_1.
\]
Subtracting gives \(2(c_1-c_2)=0\). Multiplication by \(2\) is an automorphism of the odd-order group, forcing \(c_1=c_2\), a contradiction. Thus the number \(I(A)\) of intercalates vanishes.

Cioabă and Mim's all-field Latin-square graph theorem (Theorem 3.12, with Theorems 3.6 and 3.8 and Proposition 3.11 in their June 25, 2026 preprint) states for any Latin square of order \(n\ge5\) that the associated clique complex has \(H_1=0\), \(H_i=0\) for \(i\ge3\), and \(\dim H_2=(n-1)^3-I\) over every field. Applied here over \(\mathbb Q\), it yields \(\dim H_2(X_A;\mathbb Q)=(n-1)^3\) and the asserted degree concentration. The graph is connected: any two cells can be joined through two cells sharing first and second coordinates, so \(H_0(X_A;\mathbb Q)\cong\mathbb Q\) with trivial translation action.

**2. Classify nonidentity translation-fixed simplices.** Fix \(t=(u,v)\ne(0,0)\). Its order \(d\) is odd and at least three; it acts freely on vertices, and each vertex orbit has \(d\) points. If a nonempty clique \(F\) is preserved by \(t\), the whole orbit of any \((r,c)\in F\) is in \(F\). In particular, \((r,c)\) and \((r+u,c+v)\) must be adjacent. Consequently,
\[
u=0\quad\text{or}\quad v=0\quad\text{or}\quad u+v=0.
\]
A nonzero \(t\) satisfies **at most one** of these conditions.

Suppose \(u=0\), so the orbit lies in the row with first coordinate \(r\). It contains at least three distinct cells of this row. Any vertex outside this row is adjacent to at most two of its cells: at most one by sharing a column, and at most one by sharing their sum. As \(F\) is a clique, \(F\) therefore lies entirely in that row. The same argument applies to columns when \(v=0\), and to fixed-sum lines when \(u+v=0\), by exchanging the three pairwise-orthogonal Latin line classes. For the fixed-sum case explicitly, a vertex outside a given sum-line meets that line in at most one equal-row cell and at most one equal-column cell.

Thus if no axis condition holds, \(t\) preserves **no** nonempty simplex. If one axis condition holds, every nonempty preserved simplex lies in one of the \(n\) full \((n-1)\)-simplices of that line class. Distinct lines in a class are disjoint, and each line is preserved by \(t\). There is no double counting.

**3. Compute the signed Lefschetz trace.** For any finite simplex and any permutation of its vertices, the alternating trace on its ordinary chain groups is \(1\): this follows directly from its contractible chain complex with trivial degree-zero homology. Equivalently, the sum over all setwise invariant nonempty faces of \((-1)^{\dim F}\) times the sign of the induced permutation on \(F\) is \(1\). Therefore, the alternating trace \(L(t)\) on the full simplicial chain complex of \(X_A\) is \(n\) when \(t\ne0\) preserves one of the three line classes and is \(0\) for every other nonzero \(t\).

The Euler–Poincaré trace identity, justified over \(\mathbb Q\) by exactness of boundaries and the chain-level action, gives
\[
L(t)=\sum_i(-1)^i\operatorname{tr}(t\mid H_i)=1+\chi(t).
\]
Hence \(\chi(t)=n-1\) on a nonzero axis translation and \(\chi(t)=-1\) otherwise. At the identity, \(\chi(0,0)=(n-1)^3\) by Step 1. The three cases are exactly the product formula in the Finding.

**4. Recover the rational module.** The trace of an element \(a\in A\) on the regular permutation module \(\mathbb Q[A]\) is \(n\) for \(a=0\) and \(0\) otherwise. Subtracting the trivial line, the augmentation character is \(n\mathbf1_{a=0}-1\). Therefore \(V_1\otimes V_2\otimes V_3\) has precisely the product character calculated in Step 3. Finite-group representations over characteristic zero are semisimple, and rational representations of the finite abelian group \(T\) are determined by their complex characters; the asserted \(\mathbb Q[T]\)-isomorphism follows.

**5. Fourier multiplicities.** After extension to \(\mathbb C\), the augmentation module is the direct sum of all nontrivial one-dimensional characters of \(A\), once each. A constituent of the triple tensor product has character \((u,v)\mapsto\xi(u)\eta(v)\gamma(u+v)\), with \(\xi,\eta,\gamma\in\widehat A\setminus\{\mathbf1\}\). To equal \((\alpha,\beta)\), we must have \(\xi=\alpha\gamma^{-1}\) and \(\eta=\beta\gamma^{-1}\). Thus \(\gamma\) must avoid exactly the distinct characters in \(\{\mathbf1,\alpha,\beta\}\), giving the displayed multiplicity. The trivial character has multiplicity \(n-1\). This completes the proof.

## Verification
The accompanying standard-library program `check_translation.py` enumerates every nonempty clique, computes signed fixed-simplex traces for every group translation, calculates the complete simplicial boundary ranks over \(\mathbb F_2\), and separately checks all complex-character multiplicities. It passed for the cyclic groups of orders \(5\), \(7\), and \(9\), and the noncyclic group \(C_3\times C_3\). The respective clique counts were \(515\), \(2863\), \(14283\), and \(14283\); the full mod-two second Betti ranks were \(64\), \(216\), \(512\), and \(512\); all other positive-degree mod-two Betti ranks were zero. In total, \(236\) group translations were checked for exact signed traces, together with \(236\) Fourier multiplicities. Run `python3 check_translation.py` from the directory containing the program. These finite calculations confirm test instances; the argument in the Proof establishes the theorem for every finite abelian group of odd order at least five.

## Relationship to prior work
Cioabă and Mim (arXiv:2606.27328, first posted June 25, 2026) determine the nonequivariant field homology of Latin-square graph clique complexes, including the dimension \((n-1)^3-I\). Even the stronger nonequivariant wedge-of-second-dimensional-spheres description does not supply the action of \(A\times A\) on homology. Neither the Betti formula nor a nonequivariant wedge type implies the translation character or the Fourier multiplicities, because distinct group representations can have the same underlying vector-space dimension.

The present theorem refines these results to an explicit, complete rational \(A\times A\)-representation for the naturally symmetric odd-order group-table subfamily. The substantive additional step is the classification of setwise translation-invariant cliques, followed by signed Lefschetz and Fourier analysis. The established all-field homology theorem and standard character theory are used as inputs rather than claimed anew.

## Limitations
The theorem assumes a finite **abelian** group of odd order at least five. For even order, group tables may have intercalates and nonidentity translations of order two, so both the top Betti rank and the fixed-clique argument change; the formulas above are not asserted there. The rational \(A\times A\)-module is completely determined, but an integral isomorphism of lattices, actions of further graph automorphisms, and equivariant homotopy classifications are not established. The originality comparison is supported by inspected sources and indexed searches, not by a proof that no equivalent unindexed result exists.

## References
Cioabă, Sebastian M., and Mutasim Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328v1, first submitted 2026-06-25, particularly Section 3 and Theorem 3.12. https://arxiv.org/abs/2606.27328v1

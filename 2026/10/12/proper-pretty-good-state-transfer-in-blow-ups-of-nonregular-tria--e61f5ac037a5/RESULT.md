# Proper pretty good state transfer in blow-ups of nonregular triangle-leaf cones

## Finding
For each integer \(s\ge1\), consider \(G_s=K_1\vee(K_2\sqcup sK_1)\), with apex \(h\), adjacent triangle vertices \(a,b\), and leaves \(\ell_1,\ldots,\ell_s\). Let \(B_s=G_s[\overline{K_2}]\) be the simple unweighted graph whose vertices are \((\epsilon,v)\), with \(\epsilon\in\{0,1\}\) and \(v\in V(G_s)\), and whose adjacency is independent of \(\epsilon\) and determined by adjacency of the corresponding distinct base vertices.

**Theorem.** For continuous-time adjacency evolution \(U_s(t)=\exp(itA(B_s))\), all distinct vertex pairs admitting pretty good state transfer (PGST) are precisely
\[
\big\{\{(0,h),(1,h)\},\{(0,a),(1,a)\},\{(0,b),(1,b)\}\big\}
\]
for every \(s\ge1\), together with the clone pair of the sole leaf when \(s=1\). If \(s\ge2\), no leaf clone pair has PGST. None of these pairs, and no other distinct pair, has perfect state transfer (PST).

PGST means that for every \(\varepsilon>0\) there is \(t>0\) with \(|U_s(t)_{u,v}|>1-\varepsilon\); PST means equality at some positive time. All the PGST claimed here is therefore *proper*, not perfect.

## Assumptions and scope
All graphs are finite, simple, undirected, and unweighted. The Hamiltonian is the adjacency matrix, not a normalized or ordinary Laplacian. The blow-up replaces each vertex by two nonadjacent clones, and replaces each base edge by a complete bipartite graph on the corresponding two clone pairs. The parameter \(s\) is any positive integer; no genericity or asymptotic assumption is imposed. The claim classifies *every pair* of distinct vertices, not only the apex pair.

## Proof
**1. Exact invariant decomposition and spectral support.** In \(G_s\), the three orthonormal vectors given by the apex, the symmetric triangle-edge vector, and the uniform leaf vector span an invariant subspace with symmetric matrix
\[
Q_s=\begin{pmatrix}0&\sqrt2&\sqrt s\\ \sqrt2&1&0\\ \sqrt s&0&0\end{pmatrix}.
\]
Its characteristic polynomial is
\[
f_s(x)=x^3-x^2-(s+2)x+s.
\]
The antisymmetric difference of the two non-apex triangle vertices has eigenvalue \(-1\), and the zero-sum leaf vectors span the \(0\)-eigenspace of dimension \(s-1\). Therefore
\[
\det(xI-A(G_s))=x^{s-1}(x+1)f_s(x).
\]
The real-symmetric irreducible tridiagonal form obtained by ordering the leaf aggregate, apex, and edge aggregate has nonzero subdiagonal entries, so the three roots of \(f_s\) are real and simple. Since \(f_s(0)=s\), \(f_s(1)=-2\), and \(f_s(-1)=2s\), no root is any of \(0,1,-1\).

For each root \(\lambda\), the corresponding quotient eigenvector has nonzero apex component: if it vanished, the remaining equations and \(\lambda\notin\{0,1\}\) would force the entire vector to vanish. The other two components are nonzero by their coupling equations. It follows that all three cubic roots occur in the spectral support of \(h\), each of \(a,b\), and every leaf. The eigenvalue \(-1\) occurs additionally and with nonzero projection at \(a,b\), but not at \(h\) or the leaves. The zero eigenvalue occurs at a leaf exactly when \(s\ge2\), with projection squared norm \(1-1/s\); it does not occur at \(h,a,b\).

**2. Clone transfer is a phase-parity problem.** The adjacency of the blow-up equals \(J_2\otimes A(G_s)\). Let \(P_+=J_2/2\) and \(P_-=I_2-P_+\). Then
\[
\exp(itA(B_s))=P_+\otimes\exp(2itA(G_s))+P_-\otimes I.
\]
Consequently, between different base vertices the amplitude has modulus at most \(1/2\), so no distinct-base pair admits PGST. For the clone pair above a fixed base vertex \(v\), the amplitude is
\[
\frac12\left(\langle v,\exp(2itA(G_s))v\rangle-1\right).
\]
Writing the diagonal entry as a positive convex combination of spectral phases, its limit can be \(-1\) exactly when *every* eigenvalue in the support of \(v\) admits simultaneous phases tending to \(-1\). The continuous-parameter Kronecker closure theorem makes this equivalent to the following criterion:
\[
\sum_{\lambda\in\operatorname{supp}(v)}n_\lambda\lambda=0,
\quad n_\lambda\in\mathbb Z
\quad\Longrightarrow\quad
\sum_{\lambda\in\operatorname{supp}(v)}n_\lambda\equiv0\pmod2.
\tag{1}
\]
One may take the approximating times positive and unbounded, since the positive semiorbit of a one-parameter subgroup has the same compact closure as the full orbit. If zero occurs in a vertex support, relation \(1\cdot0=0\) violates (1); hence no leaf clone pair works when \(s\ge2\).

**3. All integer parameters and the arithmetic exception.** Since \(f_s\) is monic, any rational root is integral. The identity
\[
f_s(r)=(r-1)(r^2-s-2)-2
\]
forces \(r-1\mid2\), so \(r\in\{-1,0,2,3\}\). Direct substitution shows that for positive integral \(s\), the only possibility is \(s=6\), with root \(r=3\). Therefore \(f_s\) is irreducible over \(\mathbb Q\) whenever \(s\ne6\).

Write its roots \(\lambda_1,\lambda_2,\lambda_3\). Their sum is \(1\). For \(s\ne6\), irreducibility yields a transitive Galois group on the three roots; by Cauchy's theorem it contains a three-cycle. If \(a\lambda_1+b\lambda_2+c\lambda_3=0\) for rational \(a,b,c\), cyclic conjugation and summation imply \(a+b+c=0\). The three cyclic conjugate equations have a circulant coefficient matrix with rank \(2\) whenever \((a,b,c)\ne(0,0,0)\) and \(a+b+c=0\): its two nonzero eigenvalues have squared product proportional to \(a^2+b^2+c^2-ab-bc-ca>0\). Hence its nullspace consists of constant triples, contradicting the distinctness of the roots. Thus the three roots are linearly independent over \(\mathbb Q\).

For the apex (and the sole leaf if \(s=1\)), there are no nontrivial relations in (1). For either triangle-edge vertex, its support also includes \(-1\). Using \(\lambda_1+\lambda_2+\lambda_3=1\), every integer relation
\[
a_1\lambda_1+a_2\lambda_2+a_3\lambda_3+b(-1)=0
\]
forces \(a_1=a_2=a_3=b\); its total coefficient sum is \(4b\), even. Thus condition (1) holds at all three triangle vertices for every \(s\ne6\).

At \(s=6\), factorization gives
\[
f_6(x)=(x-3)(x^2+2x-2),
\qquad \{\lambda_i\}=\{3,-1+\sqrt3,-1-\sqrt3\}.
\]
For the cubic support alone, a relation \(3a+b(-1+\sqrt3)+c(-1-\sqrt3)=0\) has \(b=c\) and \(3a=2b\), so \((a,b,c)=(2k,3k,3k)\) and coefficient sum \(8k\). For triangle-edge support, including the additional eigenvalue \(-1\) with coefficient \(d\), every relation has \(b=c\), \(d=3a-2b\), and total coefficient sum \(4a\). Both sums are even. Therefore (1) remains true at the three triangle vertices even in the sole reducible case. This proves the entire PGST classification.

**4. Exclusion of PST.** Perfect clone transfer would require the three cubic-root phases all to equal \(-1\) at one time; consequently all three root ratios would be ratios of odd integers and hence rational. For \(s\ne6\), this contradicts the established rational linear independence of the roots. For \(s=6\), the ratio of \(3\) to \(-1+\sqrt3\) is irrational. Leaves at \(s\ge2\) already fail PGST, and all distinct-base pairs are bounded by amplitude \(1/2\). Hence PST never occurs between distinct vertices.

## Verification
A standalone exact-arithmetic Python script `verify.py` constructs each base adjacency matrix directly, computes its integer characteristic polynomial by Newton identities, and checks the predicted factorization and nullity for every \(1\le s\le20\). It also checks the exceptional rational-root reduction for \(1\le s\le2000\) and the parity identities at \(s=6\) on a large integer coefficient grid. The script reports:

`VERIFY_OK exact_graph_charpolys=20 exact_nullities=20 integer_root_scope=2000 exceptional_roots=[(6, 3)] exceptional_integer_relations=1681`

These are finite corroborating computations. The proof above, including the unbounded parameter range and the phase approximation, is analytical and does not depend on exhaustion or extrapolation.

## Relationship to prior work
The theory of spectral phase arithmetic and quantum walks for integral Hamiltonians is developed by Coutinho, Baptista, Godsil, Spier and Werner [1]. Bhattacharjya, Monterde and Pal [2] establish the general blow-up phase criterion and classify various families, including cones over *regular* graphs; their concluding open question explicitly asks about cones over *nonregular* graphs. That general criterion is used, not claimed here as new. The new statement is a complete classification for the particular infinite nonregular-cone family \(K_1\vee(K_2\sqcup sK_1)\), including all possible transferring pairs, spectral-support change at multiple leaves, exceptional reducibility at \(s=6\), and impossibility of exact transfer. Twin-transfer theory [3] provides further general context.

## Limitations
No classification of all nonregular cones is claimed. The only Hamiltonian addressed is the unweighted adjacency matrix. The two-fold blow-up is essential to this statement; other blow-up multiplicities are not analyzed here. The spectrum criterion itself is inherited from [2]. No quantitative transfer-time bounds are established. A more general unpublished or unlocated theorem could subsume this family; bibliographic checks do not prove universal novelty. Independent mathematical audit has not been performed.

## References
[1] G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier, and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public 2022-08-18 UTC), https://arxiv.org/html/2208.08971v1 .

[2] B. Bhattacharjya, H. Monterde, and H. Pal, *Quantum walks on blow-up graphs*, arXiv:2308.13887v1 (first public 2023-08-26 UTC); inspected full open HTML v2, https://arxiv.org/html/2308.13887v2 .

[3] S. Kirkland, H. Monterde, and S. Plosker, *Quantum state transfer between twins in weighted graphs*, arXiv:2201.02720, https://arxiv.org/abs/2201.02720 .

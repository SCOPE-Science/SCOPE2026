# Corank-one rigidity for graph and random-walk evolution algebras

## Finding
Let \(G\) be any finite connected simple undirected graph with at least two vertices, adjacency matrix \(A\), and \(\operatorname{rank}_{\mathbb R}A=|V(G)|-1\). Let \(E_G\) and \(E_{\mathrm{RW},G}\) be the real evolution algebras with structure matrices \(A\) and \(D^{-1}A\), respectively, where \(D=\operatorname{diag}(d_v)\) is the positive degree matrix. Then **every** algebra isomorphism \(E_G\longrightarrow E_{\mathrm{RW},G}\) is monomial in the indicated natural bases: it sends each basis vector to a nonzero scalar multiple of another basis vector. Consequently,
\[
E_G\cong E_{\mathrm{RW},G}\quad\Longleftrightarrow\quad
G\text{ is regular or bipartite biregular}.
\]
Here bipartite biregular means that the degree is constant separately on each class of a bipartition. The statement applies both when \(G\) is twin-free and when it has a unique pair of false twins. The monomial rigidity threshold is sharp in rank: the star \(K_{1,3}\), with adjacency nullity \(2\), has nonmonomial real automorphisms of its graph evolution algebra.

## Assumptions and scope
Work over \(\mathbb R\), with a simple graph with no loops, at least two vertices, and no isolated vertices. In either algebra the natural basis is \((e_v)_{v\in V}\), distinct basis vectors multiply to zero, and
\[
e_v^2=\sum_{w\sim v}e_w\quad\text{in }E_G,\qquad
 e_v^2=\frac{1}{d_v}\sum_{w\sim v}e_w\quad\text{in }E_{\mathrm{RW},G}.
\]
A monomial map is \(e_v\mapsto \alpha_v e_{\sigma(v)}\), where \(\alpha_v\ne0\) and \(\sigma\) is a permutation. Twins mean distinct vertices with identical (open) neighbor sets; such vertices in a simple graph are nonadjacent. The rank is the ordinary real matrix rank, not the rank of the graph incidence matrix.

## Proof
**1. Orthogonality constrained by the adjacency kernel.** Let \(\varphi:E_G\to E_{\mathrm{RW},G}\) be any isomorphism and let its invertible matrix \(P\) have columns \(p_i=(p_{vi})_{v\in V}\), so \(\varphi(e_i)=\sum_v p_{vi}e_v\). For \(i\ne j\), the identity \(0=\varphi(e_ie_j)=\varphi(e_i)\varphi(e_j)\) implies
\[
 (D^{-1}A)^T(p_i\circ p_j)=0,
\]
where \(\circ\) denotes coordinatewise multiplication. Since \(A\) is symmetric and \(D\) invertible, \(\ker((D^{-1}A)^T)=D\ker A\). Select a nonzero \(z\in\ker A\); by the rank hypothesis, every coordinatewise product \(p_i\circ p_j\) with \(i\ne j\) is a scalar multiple of \(Dz\). Put \(S=\operatorname{supp}z\). Nonzero adjacency rows rule out \(|S|=1\).

**2. Kernel support of size at least three.** Suppose \(|S|\ge3\). If columns \(p_i,p_j\) overlap at any coordinate, their product is a nonzero multiple of \(Dz\); therefore both columns are nonzero at every coordinate of \(S\). Fix \(i\). For each \(k\ne i\), the restriction \(p_k|_S\) is a scalar multiple of the fixed vector \(((Dz)_v/p_{vi})_{v\in S}\). Thus the restriction of the whole invertible matrix \(P\) to the rows \(S\) has rank at most two, contrary to its row rank \(|S|\ge3\). Hence distinct columns never overlap. Invertibility then forces exactly one nonzero entry in each row and column, so \(P\) is monomial.

**3. Kernel support of size two.** Suppose \(S=\{u,v\}\). The relation \(Az=0\) says that the \(u\)- and \(v\)-rows of \(A\) are proportional; these are nonzero binary rows, so they are equal. Thus \(u,v\) are twins, \(d_u=d_v=\delta\), and \(\ker A=\mathbb R(e_u-e_v)\). No second distinct twin pair is possible because the kernel is one-dimensional. Orthogonality from step 1 becomes
\[
 p_{ui}p_{uj}+p_{vi}p_{vj}=0\quad(i\ne j),
\]
while every row outside \(\{u,v\}\) has at most one nonzero entry. Because the two rows of \(P\) indexed by \(u,v\) are linearly independent, their nonzero column-vectors form a pairwise orthogonal spanning family in \(\mathbb R^2\); such a family has exactly two nonzero members. The other \(|V|-2\) rows have distinct single-column supports (invertibility). These supports must be disjoint from the two twin-row supports, otherwise the entire matrix would have fewer than \(|V|\) nonzero columns. After reordering columns, \(P\) consists of one invertible \(2\times2\) block \(Q\) in rows \(u,v\), and nonzero monomial entries outside that block.

Let the source columns corresponding to \(Q\) be \(i,j\). Their image squares are nonzero scalar multiples of the same element \(\sum_{w\sim u}e_w\), so \(e_i^2,e_j^2\) are proportional because \(\varphi\) is injective. Again, nonzero binary adjacency rows are proportional only when equal, hence \(i,j\) are a twin pair. By uniqueness they are exactly \(u,v\). Thus \(Q\) maps the source twin pair to the target twin pair, and all other basis vectors are mapped monomially outside it.

Write \(Q=\begin{pmatrix}a&b\\c&d\end{pmatrix}\). The mixed product \(e_ue_v=0\) gives \(ab+cd=0\). The equal squares \(e_u^2=e_v^2\) give \(a^2+c^2=b^2+d^2\). Choose a vertex \(w\) adjacent to the twin vertices. Since \(e_w^2\) contains both \(e_u,e_v\) and \(\varphi(e_w)\) is a scalar multiple of a basis vector outside the twin pair, comparison of the two twin coordinates in \(\varphi(e_w^2)=\varphi(e_w)^2\) gives
\[
 a+b=c+d=\gamma\ne0.
\]
Indeed the target graph's twins always occur together and with equal coefficients in any target basis square; the column sum of an invertible \(Q\) cannot be zero. Substitution into the equal-norm equation yields \(a+c=\gamma\), hence \(Q=\begin{pmatrix}a&\gamma-a\\\gamma-a&a\end{pmatrix}\). Orthogonality now yields \(2a(\gamma-a)=0\); over \(\mathbb R\), \(a=0\) or \(a=\gamma\). So \(Q\) is a scalar multiple of the identity or swap, and the full \(P\) is monomial.

**4. Degrees force regularity or biregularity.** Write the established monomial isomorphism as \(\varphi(e_i)=\alpha_i e_{\sigma(i)}\), with \(\alpha_i\ne0\). Comparing nonzero coordinate supports of \(\varphi(e_i^2)=\varphi(e_i)^2\) shows \(\sigma(N(i))=N(\sigma(i))\), so \(\sigma\) is a graph automorphism and preserves degrees. Comparing coefficients along any edge \(i\sim j\) gives
\[
\alpha_j=\frac{\alpha_i^2}{d_i},\qquad \alpha_i=\frac{\alpha_j^2}{d_j}.
\]
In particular, all neighbors of a vertex have the same \(\alpha\)-value. Connectedness forces \(\alpha\) to be constant on even-walk classes: on all vertices if the graph is nonbipartite, or separately on the two sides if bipartite. In the first case the displayed identity forces all degrees equal; in the second it forces the degrees to be constant on each side.

**5. Converse.** If \(G\) is \(d\)-regular, \(e_i\mapsto d e_i\) is an isomorphism \(E_G\to E_{\mathrm{RW},G}\). For a bipartite \((r,s)\)-biregular graph with sides \(X,Y\), take positive reals \(a=(r^2s)^{1/3}\) and \(b=(s^2r)^{1/3}\). The diagonal map \(e_x\mapsto a e_x\) for \(x\in X\), \(e_y\mapsto b e_y\) for \(y\in Y\), satisfies \(a^2/r=b\) and \(b^2/s=a\), hence is an isomorphism. This proves both directions.

**6. Sharpness of monomial rigidity.** In \(K_{1,3}\), let \(c\) be the center and \(x_1,x_2,x_3\) its leaves. The squares are \(x_i^2=c\) and \(c^2=x_1+x_2+x_3\). Every real orthogonal transformation of the leaf space fixing \(x_1+x_2+x_3\), extended by \(c\mapsto c\), is an algebra automorphism. The stabilizer contains rotations by angles other than integer multiples of \(\pi/2\), hence nonmonomial automorphisms. The star's adjacency kernel has dimension \(2\), demonstrating that the corank-one bound on monomial rigidity cannot be dropped.

## Verification
The argument is uniform in the number of vertices. The included `verify.py` uses only the Python standard library. It exhaustively checks adjacency nullity, connectedness, twin classes, and degree patterns for all labeled graphs with three through six vertices, plus an explicit check of the nonregular corank-one diamond and twin-free five-vertex path. This is a consistency check, not a substitute for the proof. Neither finite enumeration nor numerical approximations are used to establish the theorem for arbitrary graphs.

## Relationship to prior work
The October 2026 evolution-algebra survey [1, Question 26] records the graph/random-walk isomorphism criterion as unresolved for singular connected graphs. The original paper [2] proves it in the nonsingular case and treats examples; the 2024 paper [3] considers several singular families and an individual twin-free graph. The 2025 paper [4] treats automorphism groups, including the standard pairwise-linearly-independent-squares (2LI) criterion and worked non-2LI examples. In particular, 2LI already explains why the twin-free portion admits only monomial basis changes; no originality is claimed for that ingredient alone. The additional general twin-pair block argument gives the full corank-one isomorphism criterion, including all graphs for which 2LI fails at exactly one pair, rather than another individual graph. The theorem does not solve the general higher-nullity conjecture.

## Limitations
The result concerns finite simple connected graphs over \(\mathbb R\), with adjacency nullity exactly one. It does not classify graph/random-walk evolution algebras with higher nullity, nor arbitrary homomorphisms. Nonmonomial isomorphisms may occur in higher nullity even for graphs whose two algebras are isomorphic. The literature comparison was bounded and does not prove absolute novelty; a differently phrased earlier general theorem covering all corank-one graphs remains a possible priority risk.

## References
[1] I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, first submitted 2026-10-15, especially §1.7 and Question 26.

[2] P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516, initially submitted 2017-10-28, especially its nonsingular criterion and singular examples.

[3] P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez, S. J. Vidal, *On some singular graphs with non-isomorphic associated evolution algebras*, arXiv:2405.12341v1, initially submitted 2024-05-20, especially §§2–3.

[4] M. L. Rodiño Montoya, N. A. Viana Bedoya, C. Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604v2, initially submitted 2025-05-21, especially §§2–3 and Example 2.19.

# Twin-blowup isomorphisms between graph and random-walk evolution algebras

## Finding

Let \(K\) be a field of characteristic zero. Let \(H\) be a finite connected loopless simple graph with at least two vertices and with nonsingular adjacency matrix over \(K\). Replace each vertex \(i\) of \(H\) by a nonempty independent class of size \(n_i\), and join two classes completely exactly when their vertices are adjacent in \(H\). Denote the resulting graph by \(G=H[n_1,\ldots,n_t]\), and write \(d_i=\sum_{j\sim i}n_j\) for the degree of every vertex in class \(i\).

The adjacency evolution algebra \(A(G)\) and random-walk evolution algebra \(A_{\mathrm{RW}}(G)\) are isomorphic as \(K\)-algebras **if and only if** one of the following holds:

1. \(H\) is nonbipartite and all \(d_i\) equal the same integer \(D\) (so \(G\) is regular).
2. \(H\) is bipartite with classes of colors \(X,Y\), all \(d_i\) on \(X\) equal \(D_X\), all \(d_i\) on \(Y\) equal \(D_Y\), and \(D_X^2D_Y\) is a cube in \(K^\times\) (so \(G\) is biregular with an arithmetic cube condition).

Thus over \(\mathbb R\) or \(\mathbb C\) the isomorphism criterion is precisely that \(G\) is regular or biregular. This establishes the singular-graph criterion for **all** such blowups, including arbitrary complete multipartite graphs: for \(t\ge3\), \(A(K_{n_1,\ldots,n_t})\cong A_{\mathrm{RW}}(K_{n_1,\ldots,n_t})\) exactly when all part sizes are equal; for \(t=2\) the isomorphism always exists over \(\mathbb R\) or \(\mathbb C\).

**All isomorphisms are also described explicitly.** An isomorphism \(T:A(G)\to A_{\mathrm{RW}}(G)\) induces an automorphism \(\sigma\) of \(H\) satisfying \(n_{\sigma(i)}=n_i\). In the nonbipartite case, every block \(W_i\to W_{\sigma(i)}\) is \(D Q_i\), where \(Q_i\) is an isometry of the standard dot products sending the block-sum vector to the corresponding block-sum vector. In the bipartite case, choose \(b\in K^\times\) with \(b^3=D_X^2D_Y\), and set \(a=b^2/D_X\). Every block on color \(X\) is \(bQ_i\), and every block on color \(Y\) is \(aQ_i\), with the same condition on \(Q_i\). Conversely, every such choice yields an isomorphism. Under this convention, \(Q_i\) is an isometry between two standard dot-product spaces of equal dimension and maps the all-ones vector to the all-ones vector. Different permissible \(\sigma\), cube roots, and block isometries exhaust the isomorphisms.

For instance, \(K_{2,3}\) gives a biregular graph whose associated algebras are isomorphic over \(\mathbb R\) and \(\mathbb C\), but **not over \(\mathbb Q\)**, since \(18\) is not a rational cube.

## Assumptions and scope

The base graph \(H\) is simple, connected, and has an invertible adjacency matrix over \(K\); each \(n_i\) is a positive integer. The field has characteristic zero. The blowup's adjacency matrix is singular whenever some \(n_i>1\), because its rows repeat. The theorem applies even if some \(n_i=1\). The no-loops and characteristic-zero assumptions enter the degree normalization and nonvanishing of the integers \(n_i\).

For each block, let \(W_i=\operatorname{span}_K\{e_{i,1},\ldots,e_{i,n_i}\}\), let \(s_i=\sum_{a=1}^{n_i}e_{i,a}\), and let \(u_i=\sum_{j\sim i}s_j\). The adjacency product is \(xy=\langle x_i,y_i\rangle u_i\) for \(x,y\in W_i\), and products between different blocks vanish. The random-walk product on \(W_i\) is \(xy=d_i^{-1}\langle x_i,y_i\rangle u_i\). Both dot products are the coordinatewise nondegenerate symmetric bilinear forms, not Hermitian forms.

## Proof

**1. Intrinsic recovery of the blocks from a pencil.** The \(t\) vectors \(u_i\) are linearly independent: in coordinates relative to the independent vectors \(s_1,\ldots,s_t\), the matrix with rows \(u_i\) is the invertible adjacency matrix of \(H\). Thus the square space of either algebra is \(U=\operatorname{span}\{u_i\}\), of dimension \(t\).

For a functional \(\ell\in U^*\), consider the symmetric bilinear form \(B_\ell(x,y)=\ell(xy)\) on the full underlying vector space \(E=\bigoplus W_i\). For \(A(G)\) it has diagonal blocks \(\ell(u_i)I_{n_i}\), hence
\[
\det B_\ell=\prod_{i=1}^t\ell(u_i)^{n_i}.
\]
For \(A_{\mathrm{RW}}(G)\) it is the same polynomial multiplied by the nonzero scalar \(\prod_i d_i^{-n_i}\). Since the \(u_i\) are independent, the linear factors \(\ell(u_i)\) are pairwise nonproportional. An algebra isomorphism induces an invertible linear change on \(U^*\), and its pullback changes the determinant by a nonzero scalar square. Unique factorization of the determinant into linear forms forces a permutation \(\sigma\) such that \(T(u_i)=c_i u_{\sigma(i)}\) with \(c_i\in K^\times\) and \(n_{\sigma(i)}=n_i\). For a functional vanishing on exactly one \(u_i\), \(B_\ell\) has radical exactly \(W_i\). Transport of radicals therefore gives \(T(W_i)=W_{\sigma(i)}\). This argument accounts for **all** invertible linear algebra isomorphisms, not merely monomial ones.

**2. Adjacency and the block-sum vectors.** Because \(T(u_i)=c_i u_{\sigma(i)}\) and \(u_i=\sum_{j\sim i}s_j\), projecting this equality onto each distinct target block shows that the set of neighbors of \(\sigma(i)\) equals \(\sigma\) of the set of neighbors of \(i\). Thus \(\sigma\in\operatorname{Aut}(H)\). It also yields
\[
T(s_j)=c_i s_{\sigma(j)}\quad\text{whenever }j\sim i.
\]
Consequently there are nonzero scalars \(k_j\) with \(T(s_j)=k_j s_{\sigma(j)}\) and \(k_j=c_i\) on every edge \(i\sim j\). Since \(\sigma\) preserves the class sizes and the graph, it preserves the weighted degrees: \(d_{\sigma(i)}=d_i\).

**3. The norm constraint.** For \(x,y\in W_i\), the homomorphism identity gives
\[
\langle T_i x,T_i y\rangle=d_i c_i\langle x,y\rangle.
\]
Substitute \(x=y=s_i\). The squared norm of the all-ones vector is the nonzero scalar \(n_i\) in characteristic zero, so
\[
k_i^2 n_i=d_i c_i n_i,\qquad k_i^2=d_i c_i.
\]
Together with \(k_j=c_i\) on edges, these are necessary equations. Conversely, if these equations are satisfied, any block isometry \(Q_i\) sending \(s_i\) to \(s_{\sigma(i)}\), multiplied by \(k_i\), satisfies \(T(u_i)=c_i u_{\sigma(i)}\) and the product identity. Such isometries exist, for instance coordinate permutation maps. The equations therefore characterize every isomorphism, with all remaining freedom exactly the indicated block isometries.

**4. Parity of walks.** If \(i,k\) have a common neighbor \(j\), then \(c_i=k_j=c_k\). Connectivity implies that \(c_i\) is constant along even walks. For nonbipartite connected \(H\), an odd cycle makes every pair of vertices connected by an even walk; hence all \(c_i=c\) and all \(k_i=c\). The norm constraint becomes \(c^2=d_i c\), forcing \(d_i=c=D\) for every \(i\). Conversely \(T=D\operatorname{id}\) works, and the freedom of all isomorphisms is exactly that of Step 3.

For bipartite connected \(H\) with colors \(X,Y\), even walks connect exactly the vertices in each color. Set \(c_i=a\) on \(X\), \(c_i=b\) on \(Y\). Then \(k_i=b\) on \(X\), \(k_i=a\) on \(Y\); the norm constraints become
\[
b^2=d_i a\ (i\in X),\qquad a^2=d_i b\ (i\in Y).
\]
They force constant degrees \(D_X,D_Y\) on the two sides, with \(b^2=D_Xa\) and \(a^2=D_Yb\), equivalently
\[
b^3=D_X^2D_Y,\qquad a=b^2/D_X.
\]
Conversely, any nonzero root \(b\) of this cubic yields the desired block scalings and hence an explicit isomorphism. This is the claimed field-dependent iff classification. Over \(\mathbb R\) every positive integer has a real cube root; over \(\mathbb C\) every nonzero scalar has three cube roots.

**5. Complete multipartite specialization.** Take \(H=K_t\). Its adjacency determinant is \((-1)^{t-1}(t-1)\ne0\). For \(t\ge3\), \(H\) is nonbipartite, and \(d_i=N-n_i\), so regularity is equivalent to equality of the \(n_i\). For \(t=2\), the graph is bipartite and has constant degree on each side, so the cube criterion gives the asserted characteristic-zero field condition and automatic real/complex isomorphism.

## Verification

The standalone `checker.py` uses exact integer and rational operations. It enumerates all connected simple base graphs on two to four vertices having invertible adjacency, and all \(1\)- or \(2\)-vertex choices for their blowup classes, for \(412\) instances. It classifies the degree/parity alternatives, checks every available rational diagonal witness directly against all basis multiplication identities, verifies a nontrivial determinant-pencil factorization, and verifies the rational cube obstruction for \(K_{2,3}\). Output: `VERIFY_OK`, with \(412\) cases, \(8\) meeting the degree criterion, \(404\) not meeting it, \(385\) having singular expanded adjacency, and \(6\) exact rational witnesses. The negative cases are mathematical deductions from the proof, not computational infeasibility claims. Finite checks corroborate but do not prove the universal assertion.

Run with `python checker.py` (Python 3 and SymPy are needed). The theorem has no dependence on the checker.

## Relationship to prior work

Cadavid, Rodiño Montoya and Rodríguez (2018 preprint, 2019 journal version) prove the iff criterion for finite graphs with **nonsingular expanded adjacency matrices**, and establish the sufficiency of regularity/biregularity over the real field. Their Theorem 2.3 does not treat the singular expanded graphs here when some \(n_i>1\). Their complete-bipartite example is a special case, not presented as new here.

Cadavid, Rodiño Montoya, Rodríguez and Vidal (2024) prove nonisomorphism for specific singular caterpillar trees, tadpole graphs and a bull graph, with techniques involving twins. In particular, their double-star caterpillar examples overlap the present result; those examples are not original instances. The present statement uniformly handles **every** positive independent-set blowup of **every** connected nonsingular base graph, and derives the complete allowed block structure and a field-dependent cubic obstruction.

Kaygorodov, Martín González and Viruel (2026, arXiv:2610.22248, Question 26) explicitly retain the general singular-graph iff problem as open, citing the nonsingular results and partial singular families. The present theorem resolves that problem within the stated blowup class; it does not resolve the general conjecture.

## Limitations

The nonsingularity of the **base** adjacency matrix and characteristic zero are essential hypotheses of the method. Singular-base blowups and general singular connected graphs remain outside the result. Over arbitrary characteristic-zero fields, even biregular graphs can fail the isomorphism condition because the cube root does not exist; the simple example \(K_{2,3}\) over \(\mathbb Q\) illustrates this. The classification does not claim that any isomorphism must be monomial on individual vertices: arbitrary block-orthogonal transformations fixing class-sum vectors are allowed. Unindexed older results or broader equivalent bilinear-pencil formulations remain a historical-priority risk. No independent mathematical audit is claimed.

## References

1. P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516 (first posted 2017; revised 2018), especially Theorem 2.3, Example 2.3 and Remark 2.3. https://arxiv.org/pdf/1710.10516
2. P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez, S. J. Vidal, *On some singular graphs with non-isomorphic associated evolution algebras*, arXiv:2405.12341 (2024), especially Section 3. https://arxiv.org/pdf/2405.12341
3. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (15 October 2026), Question 26. https://arxiv.org/html/2610.22248

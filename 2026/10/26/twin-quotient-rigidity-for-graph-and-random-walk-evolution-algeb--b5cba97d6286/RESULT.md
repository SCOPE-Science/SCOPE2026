# Twin-quotient rigidity for graph and random-walk evolution algebras

## Finding

Let \(H\) be an arbitrary finite connected simple undirected graph with at least two vertices and **invertible real adjacency matrix**. Replace every vertex \(i\) of \(H\) by an independent nonempty set \(V_i\) of size \(a_i\), and join all vertices of \(V_i\) to all vertices of \(V_j\) exactly when \(ij\) is an edge of \(H\). Denote the resulting (possibly singular) graph by \(G=H[a_1,\ldots,a_k]\).

Let \(E(G)\) be the real evolution algebra with natural basis \(e_v\) and squares \(e_v^2=\sum_{w\sim v}e_w\). Let \(E_{\mathrm{RW}}(G)\) have the same zero mixed products and squares \(e_v^2=\deg(v)^{-1}\sum_{w\sim v}e_w\).

**Theorem.** For every \(H\) and every choice of positive integer sizes as above,
\[
 E(G)\cong E_{\mathrm{RW}}(G)
 \quad\Longleftrightarrow\quad
 G\text{ is regular or connected bipartite biregular}.
\]
Here biregular means that a bipartition exists on whose two sides the vertex degrees are separately constant; the constants may differ. Isomorphism means an invertible real-linear map preserving multiplication, not merely isotopy.

In particular, for every complete multipartite graph \(K_{a_1,\ldots,a_k}\) with \(k\ge3\) and all part sizes positive,
\[
 E(K_{a_1,\ldots,a_k})\cong E_{\mathrm{RW}}(K_{a_1,\ldots,a_k})
 \quad\Longleftrightarrow\quad
 a_1=\cdots=a_k.
\]
For \(k=2\), the two algebras are always isomorphic. The family of covered singular graphs has unbounded adjacency nullity.

## Assumptions and scope

All graphs here are finite, undirected, simple, connected and have no isolated vertices. All algebra structures and isomorphisms are over \(\mathbb R\). The invertibility hypothesis concerns **the base graph** \(H\), not the blow-up graph \(G\). The quotient graph \(H\) is automatically false-twin-free, since distinct equal rows of its adjacency matrix would contradict invertibility. Consequently its blown-up parts are exactly the classes of vertices having identical open neighborhoods.

Write \(k=|V(H)|\), \(n=\sum_i a_i\), \(S_i=\sum_{v\in V_i}e_v\), \(U_i=\sum_{j\sim_H i}S_j\), and \(d_i=\sum_{j\sim_H i}a_j>0\). All vertices in \(V_i\) have degree \(d_i\). Let \(W_i\) be the real span of the basis elements in \(V_i\). The different \(W_i\) are pairwise disjoint coordinate blocks and have dimensions \(a_i\). The Euclidean dot product below is the **standard coordinate** dot product in each block, not an invariant inner product chosen on the abstract algebra.

## Proof

**1. Independent neighborhood squares and intrinsic block detection.** The vectors \(S_1,\ldots,S_k\) are independent because they have disjoint nonempty supports. Relative to these vectors, \(U_i\) are the rows of the adjacency matrix of \(H\). Since that matrix is invertible, \(U_1,\ldots,U_k\) are independent. For any \(x=\sum_i x_i\) and \(y=\sum_i y_i\), with \(x_i,y_i\in W_i\), the two products are
\[
 xy=\sum_{i=1}^{k}\langle x_i,y_i\rangle U_i
 \quad\text{in }E(G),\qquad
 xy=\sum_{i=1}^{k}\frac{\langle x_i,y_i\rangle}{d_i}U_i
 \quad\text{in }E_{\mathrm{RW}}(G).
\]
For either multiplication, the left-multiplication operator \(L_x:y\mapsto xy\) therefore has rank exactly the number of nonzero blocks \(x_i\): each nonzero block gives a nonzero coordinate functional, the coordinate functionals act independently, and the outputs \(U_i\) are independent. In particular, the **nonzero rank-one locus** is the disjoint union of \(W_i\setminus\{0\}\). The maximal linear subspaces consisting of zero together with rank-one elements are exactly \(W_1,\ldots,W_k\). Indeed, a linear subspace containing nonzero vectors from two different blocks contains their sum, which has rank two.

An algebra isomorphism \(F:E(G)\to E_{\mathrm{RW}}(G)\) satisfies \(L_{F(x)}=F L_x F^{-1}\), so it preserves multiplication ranks. Thus it permutes these maximal subspaces: \(F(W_i)=W_{\sigma(i)}\) for a permutation \(\sigma\) of the \(k\) parts. Invertibility gives \(a_{\sigma(i)}=a_i\).

**2. The base graph is preserved.** For each \(i\), every standard basis element \(e_v\) in \(W_i\) satisfies \(e_v^2=U_i\) in the source. Hence
\[
 F(U_i)=F(e_v)^2=\lambda_i U_{\sigma(i)},\qquad \lambda_i>0,
\]
where positivity holds because \(F(e_v)\ne0\), its squared Euclidean coordinate norm is positive, and \(d_{\sigma(i)}>0\). On the other hand,
\[
 F(U_i)=\sum_{j\sim_H i}F(S_j).
\]
Each vector \(F(S_j)\) is nonzero and lies in a different coordinate block \(W_{\sigma(j)}\). Comparing nonzero blocks with \(U_{\sigma(i)}\) proves
\[
 j\sim_H i\ \Longleftrightarrow\ \sigma(j)\sim_H\sigma(i).
\]
Thus \(\sigma\) is an automorphism of the base graph. For every edge \(ij\), comparing the component in block \(W_{\sigma(j)}\) gives
\[
 F(S_j)=\lambda_i S_{\sigma(j)}.
\]
Because \(H\) is connected and has no isolated vertex, for each \(j\) there is a well-defined nonzero scalar \(s_j\) satisfying \(F(S_j)=s_j S_{\sigma(j)}\). The edge relations become \(s_j=\lambda_i\) for every edge \(ij\).

**3. Orthogonal-similitude identities.** Applying \(F\) to the product of arbitrary \(x,y\in W_i\), and comparing with the target product, yields
\[
 \langle F(x),F(y)\rangle
 =\lambda_i d_{\sigma(i)}\langle x,y\rangle.
\]
In particular, take \(x=y=S_i\). Because \(a_{\sigma(i)}=a_i\), the norms of \(S_i\) and \(S_{\sigma(i)}\) have the same positive square \(a_i\). The relation \(F(S_i)=s_iS_{\sigma(i)}\) now implies the scalar identity
\[
 \boxed{s_i^2=\lambda_i d_{\sigma(i)}.}
\]
Since \(\sigma\) preserves both adjacency and part sizes, it preserves the weighted degrees, so \(d_{\sigma(i)}=d_i\).

**4. Parity propagation and necessity.** For each edge \(ij\), \(s_j=\lambda_i\) and \(s_i=\lambda_j\). It follows that the \(\lambda_i\) are constant on every even-walk connectivity class. In a connected nonbipartite graph all vertices lie in one such class. Thus \(s_i=\lambda_i=\lambda>0\) for every \(i\), and the boxed identity gives \(d_i=\lambda\), so \(G\) is regular.

If \(H\) is connected bipartite with sides \(P,Q\), then there are positive constants \(\alpha,\beta\) such that \(\lambda_i=\alpha\), \(s_i=\beta\) for \(i\in P\), and \(\lambda_j=\beta\), \(s_j=\alpha\) for \(j\in Q\). Hence
\[
 d_i=\beta^2/\alpha\quad(i\in P),\qquad
 d_j=\alpha^2/\beta\quad(j\in Q).
\]
Thus the degrees are constant on each side, making \(G\) bipartite biregular. This proves the difficult implication.

**5. Explicit sufficiency.** If \(G\) is regular of degree \(d\), then the map \(F(e_v)=d e_v\) sends \(E(G)\) isomorphically onto \(E_{\mathrm{RW}}(G)\). Indeed, its image of each source square is \(dU_i\), while the target square of \(d e_v\) is \(d^2U_i/d=dU_i\).

If \(G\) is bipartite biregular of degrees \(d_P,d_Q\) on the respective sides, set
\[
 c_P=(d_P^2d_Q)^{1/3},\qquad
 c_Q=(d_Pd_Q^2)^{1/3},
\]
using positive real cube roots, and map \(e_v\mapsto c_Pe_v\) on side \(P\) and \(e_v\mapsto c_Qe_v\) on side \(Q\). The identities \(c_P^2/d_P=c_Q\) and \(c_Q^2/d_Q=c_P\) verify every basis square, and mixed products remain zero. The diagonal map is invertible. Sufficiency is established without an adjacency-rank restriction.

**6. Multipartite and nullity consequences.** For \(H=K_k\), its real adjacency matrix is \(J-I\), with eigenvalues \(k-1,-1,\ldots,-1\), hence invertible for \(k\ge2\). Its blow-ups are precisely \(K_{a_1,\ldots,a_k}\). For \(k\ge3\), the graph contains triangles and is nonbipartite, and its degrees are \(n-a_i\). Regularity is equivalent to equality of all part sizes. When \(k=2\), every complete bipartite graph is biregular. Finally the adjacency matrix of \(G\) has rank exactly \(k\), since the \(k\) independent neighborhood vectors are precisely its distinct rows. Therefore its nullity is \(n-k=\sum_i(a_i-1)\), which can grow arbitrarily large while the theorem remains applicable.

## Verification

Run `python3 verify.py` in the directory containing this file. The self-contained exact-arithmetic script constructs the quotient graph and its blow-up, checks independence of the neighborhood vectors and the multiplication-rank formula for 117 blow-ups of three invertible base graphs, and checks the explicit diagonal scaling identities in all regular and biregular cases. Its output ends with `VERIFY_OK cases= 117 rank_tests= 3480`.

For instance, \(K_{1,2,3}\) has degrees \(5,4,3\), adjacency rank \(3\), nullity \(3\), and nonisomorphic graph and random-walk evolution algebras. For \(K_{2,2,2}\) the degree is constantly \(4\) and scaling by \(4\) is an isomorphism. The blow-up of the four-vertex path with sizes \((2,1,2,1)\) has degrees \((1,4,2,2)\), adjacency nullity \(2\), and nonisomorphic associated algebras; the underlying four-vertex path has invertible adjacency matrix.

These finite computations test assumptions and formula normalization; the unbounded assertion is established solely by the algebraic proof above.

## Relationship to prior work

Cadavid, Rodiño Montoya and Rodríguez (2017/2019) proved the equivalence for graphs with invertible adjacency matrices and gave the isomorphisms for regular or bipartite biregular graphs in general. Cadavid, Rodiño Montoya, Rodríguez and Vidal (2024 preprint; published 2026) proved nonisomorphism for several singular families, notably double-star and caterpillar trees; these stronger **absence-of-nonzero-homomorphisms** results cover some special blow-ups of nonsingular path bases, but not arbitrary twin blow-ups or complete multipartite graphs with unrestricted part sizes. The 2026 evolution-algebra survey records the singular-graph converse as its Question 26, confirming that the general conjecture is broader than existing nonsingular and selected-singular results.

The present theorem uses an intrinsic **rank-one multiplication locus** to recover twin parts and an **orthogonal-similitude constraint** to force degree regularity. This handles simultaneously all independent-set blow-ups of any nonsingular base graph, with no bound on adjacency nullity. The theorem does not claim that all homomorphisms vanish in the nonisomorphic case, and does not resolve the original conjecture when the false-twin quotient itself has singular adjacency matrix.

## Limitations

The result is stated over \(\mathbb R\). Positivity and positive real cube roots are used for the proof and construction. The base adjacency matrix must be invertible. Although the blown-up graph may be highly singular, the theorem does not cover singular false-twin-free graphs (for example, certain paths and cycles) or graphs with a singular false-twin quotient. No complete classification of homomorphisms or automorphisms is asserted. The finite verifier is not a substitute for the general proof. The literature comparison is necessarily limited to accessible indexed work; an unnoticed equivalent theorem remains possible.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, 15 October 2026, especially Question 26, https://arxiv.org/html/2610.22248.
2. P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516 (initially public 28 October 2017), Theorem 2.3, https://arxiv.org/pdf/1710.10516. Published in *Linear and Multilinear Algebra* 69 (2021), 1858–1877.
3. P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez, S. J. Vidal, *On some singular graphs with non-isomorphic associated evolution algebras*, arXiv:2405.12341v1, 20 May 2024, Propositions 3.1–3.3 and Example 3.4, https://arxiv.org/pdf/2405.12341. Subsequently published online 9 May 2026, DOI:10.1142/S0219498827502173.

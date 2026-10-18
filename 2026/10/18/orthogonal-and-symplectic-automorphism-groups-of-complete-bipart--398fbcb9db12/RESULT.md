# Orthogonal and symplectic automorphism groups of complete bipartite evolution algebras

## Finding

For every field \(K\) and integers \(m,n\geq1\) nonzero in \(K\), let \(E_{m,n}(K)\) be the graph evolution algebra of the complete bipartite graph \(K_{m,n}\). Its full linear algebra-automorphism group is

\[
\operatorname{Aut}_K E_{m,n}(K)\cong
\begin{cases}
\mu_3(K)\times H_m(K)\times H_n(K),&m\ne n,\\
\bigl(\mu_3(K)\times H_m(K)\times H_m(K)\bigr)\rtimes C_2,&m=n.
\end{cases}
\]

Here \(\mu_3(K)=\{\lambda\in K^\times:\lambda^3=1\}\), \(H_s(K)\) is the orthogonal stabilizer of the all-ones vector in \(K^s\), and the last \(C_2\) interchanges the two orthogonal factors and inverts the cubic-root factor. The nonzero-in-\(K\) hypothesis is essential to this proof and is not silently dropped.

The classification yields exact automorphism-group orders for every finite field of admissible characteristic, exhibiting a sharp orthogonal/symplectic dichotomy. In particular \(E_{1,3}(\mathbb F_5)\) has twelve automorphisms, including nonmonomial transformations not induced by graph symmetries, while \(E_{1,3}(\mathbb F_4)\) has 180 automorphisms.

## Assumptions and scope

Write \(U=K^m\) and \(V=K^n\), with standard nondegenerate symmetric dot products \(\langle-,-\rangle\), and put \(u=(1,\ldots,1)\in U\) and \(v=(1,\ldots,1)\in V\). The multiplication on \(E=U\oplus V\) is

\[
(x,y)(x',y')=\langle y,y'\rangle u+\langle x,x'\rangle v.
\]

Thus distinct natural-basis vectors multiply to zero; every basis vector in \(U\) squares to \(v\), and every basis vector in \(V\) squares to \(u\). The assumptions are \(m,n\ge1\), \(m\cdot1_K\ne0\), and \(n\cdot1_K\ne0\). No assumption about algebraic closure or odd characteristic is used in the structural theorem.

Let

\[
H_s(K)=\{P\in\operatorname{GL}_s(K):P^{\mathsf T}P=I_s,\ P\mathbf1_s=\mathbf1_s\}.
\]

Because \(s\ne0\) in \(K\), \(K^s=K\mathbf1_s\perp\mathbf1_s^\perp\) with the latter nondegenerate, and \(H_s(K)\) is canonically the full isometry group of that codimension-one form. For \(s=1\), the group is trivial.

## Proof

First \(E^2=W=Ku\oplus Kv\), since \(u,v\) are linearly independent vectors in distinct summands. This two-dimensional subspace is characteristic under every automorphism. Inside it,

\[
u^2=mv,\qquad v^2=nu,\qquad uv=0.
\]

Let \(f\) be an algebra automorphism and write \(f(u)=au+bv\), \(f(v)=cu+dv\). The equality \(f(u)f(v)=0\) gives \(mac=0\) and \(nbd=0\). Since \(m,n\) are nonzero in \(K\), we have \(ac=bd=0\). The restriction of \(f\) to \(W\) is invertible. Therefore its matrix in \((u,v)\) is either diagonal or anti-diagonal. These two cases are exhaustive, including characteristic two.

Suppose first \(f(u)=au\), \(f(v)=bv\), with \(a,b\ne0\). Relative to \(U\oplus V\), write \(f=\begin{pmatrix}A&B\\C&D\end{pmatrix}\). Preservation of squares and polarization of products for vectors supported in \(U\) and \(V\) yields

\[
A^{\mathsf T}A=bI_m,\quad C^{\mathsf T}C=0,\quad
B^{\mathsf T}B=0,\quad D^{\mathsf T}D=aI_n,
\]

and preservation of zero mixed products yields

\[
A^{\mathsf T}B=0,\qquad C^{\mathsf T}D=0.
\]

These equalities can also be verified directly on basis products; they do not require dividing by two. The first and last norm conditions imply \(A,D\) invertible. Therefore the mixed-product equalities force \(B=C=0\). Since \(Au=au\) and \(Dv=bv\), taking squared norms gives \(a^2m=bm\) and \(b^2n=an\), hence \(b=a^2\) and \(a=b^2\). Consequently \(a^3=1\). Setting \(P=a^{-1}A\) and \(Q=a^{-2}D\) produces \(P\in H_m(K)\), \(Q\in H_n(K)\). Conversely every block map \(\operatorname{diag}(aP,a^2Q)\) with \(a^3=1\) preserves all basis products. These maps form the direct product claimed, using the fixed scalars and componentwise orthogonal multiplication.

Now assume the restriction of \(f\) to \(W\) is anti-diagonal. Its square-preservation identities instead force injective linear maps \(U\to V\) and \(V\to U\) (the corresponding Gram matrices are nonzero scalar multiples of the two identity matrices). Hence \(m\le n\) and \(n\le m\), so \(m=n\). For equal part sizes, the coordinate swap \(\tau(x,y)=(y,x)\) is an algebra automorphism. The composition \(\tau f\) has diagonal restriction to \(W\), so is already in the classified subgroup. Conversely the swap realizes the other coset. Conjugating a block automorphism by \(\tau\) swaps \(P,Q\) and sends \(a\) to \(a^2=a^{-1}\). This proves the semidirect-product description.

For \(K=\mathbb F_q\), let \(h_q(s)=|H_s(\mathbb F_q)|\). The complete exact count is

\[
|\operatorname{Aut}_{\mathbb F_q}E_{m,n}|=(1+\mathbf1_{m=n})\gcd(3,q-1)h_q(m)h_q(n).
\]

If \(q\) is odd, write \(d=s-1\). For \(d=0\), \(h_q(s)=1\). For \(d=2k+1\),

\[
h_q(s)=2q^{k^2}\prod_{j=1}^k(q^{2j}-1).
\]

For \(d=2k\ge2\),

\[
h_q(s)=2q^{k(k-1)}(q^k-\epsilon)\prod_{j=1}^{k-1}(q^{2j}-1),\qquad
\epsilon=\chi((-1)^ks),
\]

where \(\chi\) is the quadratic character on \(\mathbb F_q^\times\). Indeed \(\mathbf1_s^\perp\) has discriminant \(1/s\), and the orthogonal-group order formula gives the displayed split sign. If \(q\) is even then admissibility forces \(s\) odd. On the hyperplane \(\mathbf1_s^\perp\), every vector satisfies \(\langle x,x\rangle=(\sum_i x_i)^2=0\), so the restriction is alternating and nondegenerate, of even dimension \(d=2k\). Thus

\[
h_q(s)=|\mathrm{Sp}_{2k}(q)|=q^{k^2}\prod_{j=1}^k(q^{2j}-1).
\]

This proves the finite-field formulas.

## Verification

Run `python verify.py` with NumPy installed (see `requirements.txt`). The program exhaustively enumerates all invertible endomorphism matrices and checks their multiplication tables for six small cases over prime fields. Independently it enumerates orthogonal stabilizers over \(\mathbb F_3\) and \(\mathbb F_5\), constructs the four-element field explicitly to check the symplectic count \(60\) for the three-vertex part, and verifies a genuinely nonmonomial automorphism of \(E_{1,3}(\mathbb F_5)\). It prints `ALL_TESTS_PASSED` on success. The general theorem follows from the preceding proof, not from finite experiments.

For the latter nonmonomial example, the automorphism fixes the \(U\)-basis vector and acts on \(V\) by

\[
R=\begin{pmatrix}4&3&4\\3&4&4\\4&4&3\end{pmatrix}\quad\text{over }\mathbb F_5,
\]

where \(R^{\mathsf T}R=I_3\), \(R\mathbf1_3=\mathbf1_3\), and every matrix entry is nonzero. Hence it cannot be a graph-induced permutation.

## Relationship to prior work

Montoya, Viana Bedoya, and Henao (2025) develop natural diagonal and graph-action automorphisms of finite-graph evolution algebras and formulate conditions under which these capture the full automorphism group. Their treatment of star graphs identifies graph-induced transformations, rather than the complete orthogonal stabilizer. The present theorem computes the full automorphism group of every admissible complete bipartite graph, including transformations with nonmonomial natural-basis matrices, and evaluates its finite-field cardinality. Cadavid, Rodiño Montoya, and Rodríguez (2017) study isomorphisms with graph random-walk algebras; Camacho and collaborators (2010) introduce graph evolution algebras including complete bipartite examples. The older nonsingular-structure-matrix monomial theorems do not apply to complete bipartite adjacency matrices of rank two in dimensions greater than two.

## Limitations

The theorem does not cover characteristics dividing either part size, in which the restrictions of the square on the two-dimensional characteristic subspace have additional degeneracies. It classifies automorphisms as abstract groups and as explicitly parametrized linear transformations, not algebra endomorphisms or isomorphisms between different graph families. The finite-field formulas use standard finite classical-group order results. Relevant literature may contain an equivalent general theorem under another graph-algebra or bilinear-form terminology; no independence or complete bibliographic coverage is claimed.

## References

1. Montoya, Viana Bedoya, and Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs* (first public version May 21, 2025), arXiv:2505.15604, https://arxiv.org/abs/2505.15604 .
2. Cadavid, Rodiño Montoya, and Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks* (2017), arXiv:1710.10516, https://arxiv.org/abs/1710.10516 .
3. Camacho, Gómez, Omirov, and Turdibaev, *Some properties of evolution algebras* (2010), arXiv:1004.1987, https://arxiv.org/abs/1004.1987 .

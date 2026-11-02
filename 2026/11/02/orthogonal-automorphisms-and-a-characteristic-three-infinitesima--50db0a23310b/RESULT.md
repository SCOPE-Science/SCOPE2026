# Orthogonal automorphisms and a characteristic-three infinitesimal defect for complete-bipartite evolution algebras

## Finding

Let \(k\) be a field of characteristic different from \(2\), and let \(r,s\ge 2\) be integers whose images in \(k\) are nonzero. Let \(E_{r,s}\) be the graph evolution algebra of the complete bipartite graph \(K_{r,s}\): for its natural basis \(e_1,\ldots,e_r,f_1,\ldots,f_s\),
\[
e_i^2=v_0:=\sum_{j=1}^s f_j,\qquad f_j^2=u_0:=\sum_{i=1}^r e_i,
\]
and products of different basis vectors are zero. Set \(U=\langle e_i\rangle\), \(V=\langle f_j\rangle\), and define the nondegenerate quadratic spaces
\[
U_0=u_0^\perp\subseteq U,\qquad V_0=v_0^\perp\subseteq V
\]
using their ordinary coordinate dot products. Write \(\mu_3(k)=\{\alpha\in k^\times:\alpha^3=1\}\).

**Complete automorphism classification.** For \(r\ne s\), every automorphism is uniquely
\[
T_{\alpha,P,Q}|_U=\alpha(\operatorname{id}_{ku_0}\oplus P),\qquad
T_{\alpha,P,Q}|_V=\alpha^2(\operatorname{id}_{kv_0}\oplus Q),
\]
where \(\alpha\in\mu_3(k)\), \(P\in O(U_0)(k)\), and \(Q\in O(V_0)(k)\). Therefore
\[
\operatorname{Aut}_k(E_{r,s})\cong\mu_3(k)\times O(U_0)(k)\times O(V_0)(k).
\]
For \(r=s\), there is also the block exchange \(\tau:e_i\leftrightarrow f_i\); every automorphism belongs to exactly one of the two cosets of the preceding group, and
\[
\operatorname{Aut}_k(E_{r,r})\cong
\big(\mu_3(k)\times O(U_0)(k)\times O(V_0)(k)\big)\rtimes C_2,
\]
with exchange action \((\alpha,P,Q)\mapsto(\alpha^{-1},Q,P)\).

**Infinitesimal symmetry and smoothness.** Put
\[
d_{r,s}=\binom{r-1}{2}+\binom{s-1}{2}.
\]
The geometric automorphism-group dimension is \(d_{r,s}\). Its tangent space at the identity, equivalently \(\operatorname{Der}_k(E_{r,s})\), has dimension
\[
\dim_k\operatorname{Der}(E_{r,s})
=d_{r,s}+\begin{cases}1,&\operatorname{char}k=3,\\0,&\operatorname{char}k\ne3.\end{cases}
\]
Thus the automorphism group scheme is smooth exactly when \(\operatorname{char}k\ne3\). In characteristic \(3\), the additional infinitesimal direction is represented by the derivation \(D|_U=\operatorname{id}_U\), \(D|_V=-\operatorname{id}_V\), and is not a tangent vector to the reduced geometric group. The multiplicative cube-root group scheme \(\mu_3\) supplies precisely this nonreduced direction.

**Finite-field orders.** If \(k=\mathbb F_q\), \(q\) odd and \(\operatorname{char}k\nmid rs\), put \(g=\gcd(3,q-1)\). For \(d\ge1\), define \(O_q(d,a)\) to be the order of the orthogonal group of a nondegenerate \(d\)-dimensional quadratic space with determinant in the square class \(a\). Explicitly,
\[
O_q(2m+1,a)=2q^{m^2}\prod_{i=1}^{m}(q^{2i}-1),\qquad m\ge0,
\]
\[
O_q(2m,a)=2q^{m(m-1)}(q^m-\epsilon)\prod_{i=1}^{m-1}(q^{2i}-1),\quad
\epsilon=\chi_q((-1)^m a),\quad m\ge1,
\]
where \(\chi_q\) denotes the quadratic character of \(\mathbb F_q^\times\). Then
\[
\boxed{\ |\operatorname{Aut}_{\mathbb F_q}(E_{r,s})|=
(1+\mathbf 1_{r=s})\,g\,O_q(r-1,r)\,O_q(s-1,s).\ }
\]
The determinant classes \(r\) and \(s\) follow from Gram matrices \(I+J\) for the coordinate-difference bases of \(U_0\) and \(V_0\).

## Assumptions and scope

The classification and smoothness statement concern the *ordinary algebra automorphisms* and their affine group scheme, not merely permutations of the natural basis. The characteristic and invertibility hypotheses are essential to the orthogonal decompositions. In particular, no assertion is made when \(\operatorname{char}k=2\) or when a characteristic divides \(r\) or \(s\).

For the balanced case \(r=s=n\), the adjacency matrix of \(K_{n,n}\) has eigenvalues \(n,-n\), and \(0\) with multiplicity \(2n-2\). Over \(\mathbb C\), each such graph evolution algebra is a Ramanujan evolution algebra in the sense of Giacomelli's Definition 8.4: all eigenvalues with modulus different from \(n\) are zero. This is a statement about each finite algebra; as \(n\) varies, these graphs are not a bounded-degree expander family. Results over other fields are algebraic base-change analogues, not new spectral claims over finite fields.

## Proof

### Intrinsic recovery of the bipartition

For \(x=u+v\in U\oplus V\), left multiplication is
\[
L_x(u'+v')=(v\cdot v')u_0+(u\cdot u')v_0.
\]
Both dot forms on their complete coordinate spaces are nondegenerate and \(u_0,v_0\) are nonzero, so \(\operatorname{rank} L_x\) equals the number of nonzero components among \(u\) and \(v\). Thus
\[
\{x:\operatorname{rank}L_x\le1\}=U\cup V.
\]
An invertible linear map preserving this set must permute its two maximal linear subspaces: a subspace meeting both \(U\setminus\{0\}\) and \(V\setminus\{0\}\) would contain a sum of rank-two left multiplication. Consequently every automorphism preserves \(U,V\) separately, or swaps them. Swapping is possible only when \(r=s\); in that case the explicit \(\tau\) supplies it. Hence, after optional composition with \(\tau\), an automorphism is block diagonal \(A\oplus B\).

### The exact equations and their solution

Since \(E_{r,s}^2=ku_0\oplus kv_0\), a block diagonal automorphism satisfies \(Au_0=\alpha u_0\), \(Bv_0=\beta v_0\) for some \(\alpha,\beta\in k^\times\). Comparing products in \(U\) and \(V\), and polarizing because \(\operatorname{char}k\ne2\), gives the necessary and sufficient equations
\[
A^{\mathsf T}A=\beta I_r,\quad B^{\mathsf T}B=\alpha I_s,\quad
Au_0=\alpha u_0,\quad Bv_0=\beta v_0.
\]
Taking dot norms of \(u_0,v_0\), and using \(r,s\in k^\times\), yields \(\beta=\alpha^2\) and \(\alpha=\beta^2\), so \(\alpha^3=1\). The nondegenerate orthogonal decompositions \(U=ku_0\perp U_0\) and \(V=kv_0\perp V_0\) then force \(A=\alpha(1\oplus P)\) and \(B=\alpha^2(1\oplus Q)\), with \(P,Q\) orthogonal. Conversely these matrices satisfy all four equations and hence preserve every product. The block exchange acts by the asserted involution.

### Geometric dimension and the characteristic-three tangent defect

The same equations hold on the block-preserving open locus of the affine automorphism scheme. Near the identity they hold **scheme-theoretically**, not merely on field-valued points: writing a general block matrix \(\left(\begin{smallmatrix}A&C\\D&B\end{smallmatrix}\right)\), the vanishing of products of elements from opposite blocks gives \(A^{\mathsf T}C=0\) and \(D^{\mathsf T}B=0\). Both \(A,B\) are invertible in an open neighbourhood of the identity, forcing \(C=D=0\) there. Inverting \(r,s\) in the coefficient field then reduces this neighbourhood to \(\mu_3\times O(U_0)\times O(V_0)\). Translation covers each geometric component, including the block-exchange component when \(r=s\). This gives geometric dimension \(d_{r,s}\), and shows that smoothness is equivalent to smoothness of \(\mu_3\) because the orthogonal groups are smooth in characteristic different from two. The group scheme \(\mu_3\) is smooth precisely when \(3\ne0\) in \(k\).

For a direct tangent computation, let \(D\) be a derivation. The identity \(D(uv)=D(u)v+uD(v)=0\) for \(u\in U,v\in V\) and nondegeneracy of the dot forms force \(D\) to preserve \(U,V\). Write \(D|_U=X\), \(D|_V=Y\), \(Xu_0=a u_0\), and \(Yv_0=b v_0\). Differentiating the four equations above, or applying Leibniz to squares, gives
\[
X+X^{\mathsf T}=bI_r,\quad Y+Y^{\mathsf T}=aI_s,\quad
2a=b,\quad2b=a.
\]
Hence \(3a=0\). If \(\operatorname{char}k\ne3\), then \(a=b=0\), and \(X,Y\) are independent skew-adjoint operators on \(U_0,V_0\), with dimension \(d_{r,s}\). In characteristic three, \(a\) is free and \(b=-a\), adding one dimension, witnessed by the displayed scalar derivation.

### Finite-field enumeration

With the coordinate-difference basis \(e_i-e_r\), \(1\le i<r\), the Gram matrix on \(U_0\) is \(I_{r-1}+J_{r-1}\), of determinant \(r\). The analogous determinant on \(V_0\) is \(s\). Apply the standard odd-characteristic finite orthogonal-group order formulas for these dimension/discriminant pairs, multiply by \(|\mu_3(\mathbb F_q)|=\gcd(3,q-1)\), and by two when the blocks can be exchanged. Every factor counts a unique automorphism by the classification, proving the formula.

## Verification

Execute `python3 verify.py` in the same directory. Its independent finite-field calculations enumerate every invertible \(2\times2\) block over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), filter the exact multiplication equations, and confirm full balanced \(K_{2,2}\) automorphism counts of \(8,8,24\), respectively. A separate modular Gaussian elimination on all Leibniz identities computes derivation dimensions for seven further \((\operatorname{char}k,r,s)\) cases, including the dimension jump at characteristic three. The script prints `VERIFY_OK` on success. These finite checks do **not** establish the all-field theorem; the proof above does.

## Relationship to prior work

Giacomelli, *Expander Evolution Algebras* (arXiv:2605.12672v1, 12 May 2026), introduces Ramanujan evolution algebras in Definition 8.4 and asks for automorphism groups in Open Problem 6. Its main results do not classify the automorphisms of \(K_{n,n}\).

Rodiño Montoya, Viana Bedoya, and Henao, *Group actions and Automorphisms of evolution algebras associated to finite graphs* (arXiv:2505.15604v1), Theorem 2.9 and Corollary 2.10, already determine the diagonal cube-root subgroup for connected bipartite graphs; Theorem 2.18 gives a free graph-symmetry action. Neither statement characterizes the additional nonmonomial orthogonal factors, the all-field automorphism group, or the characteristic-three nonreduced direction. This diagonal subgroup is explicitly treated as prior art here.

Earlier graph evolution-algebra work discusses complete bipartite graph constructions and graph-versus-random-walk algebra isomorphisms (e.g. arXiv:1707.05897 and arXiv:2505.15604). These are distinct from the complete automorphism classification and the scheme-theoretic smoothness criterion. The classical Elduque--Labra results (arXiv:1902.02191) emphasize nonsingular/perfect graph evolution algebras; \(E_{r,s}\) has only a two-dimensional square and is singular for \(r,s\ge2\).

## Limitations

This is an exact classification for the explicitly stated family, not a classification for all Ramanujan evolution algebras. It does not resolve the comparison of automorphism-group sizes between Ramanujan and non-Ramanujan algebras requested in the second half of the open problem. No claims are made in characteristic two or when the characteristic divides a bipartition size. The classification has not received independent mathematical audit. A previously unlocated formulation in literature on orthogonal similitudes or automorphism schemes of singular evolution algebras could contain some or all of the result.

## References

1. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1 (12 May 2026), Definition 8.4 and Open Problem 6. https://arxiv.org/html/2605.12672v1
2. M. L. Rodiño Montoya, J. Viana Bedoya and O. Henao, *Group actions and Automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604v1 (21 May 2025), §§2.2–2.3. https://arxiv.org/html/2505.15604v1
3. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, Linear and Multilinear Algebra 69 (2021), arXiv:1902.02191. https://arxiv.org/abs/1902.02191
4. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *On the connection between evolution algebras, random walks and graphs*, Journal of Algebra and Its Applications 19 (2020), arXiv:1707.05897. https://arxiv.org/abs/1707.05897

# Triangle-supported invariant forms and the missing rank in windmill Lie algebras

## Finding
Let \(G\) be any finite simple graph with \(n\) vertices, \(e\) edges and \(c_3(G)\) triangles. For its graphical class-two nilpotent Lie algebra \(L_G\), over an arbitrary field \(k\), the vector space of symmetric ad-invariant bilinear forms admits an explicit linear identification
\[
\operatorname{InvSym}(L_G)\cong\operatorname{Sym}^2(k^{n})^*\oplus k^{c_3(G)}.
\]
In particular its dimension is \(\binom{n+1}{2}+c_3(G)\). The intersection of the radicals of **all** these forms is precisely the span of the derived basis elements associated with edges lying in no triangle.

For the friendship (windmill) graph \(F_t\) formed by gluing \(t\geq1\) distinct triangles at one common vertex, put \(n=2t+1\), \(e=3t\) and \(N=\binom{n+1}{2}\). Over every finite field \(\mathbb F_q\), let \(H_{t,q}(z)\) count symmetric invariant forms by matrix rank. Define \(r_0=0\), \(r_k=2k+1\) for \(1\leq k\leq t\), and \(d_k=n-r_k\). Then **the complete rank enumerator** is
\[
H_{t,q}(z)=\sum_{k=0}^t\binom tk(q-1)^k q^{N-\binom{d_k+1}{2}}z^{2r_k}
\sum_{j=0}^{d_k}{d_k\brack j}_q\nu_j(q)z^j,
\]
where \({d\brack j}_q\) is the Gaussian binomial coefficient, and the number \(\nu_j(q)\) of invertible symmetric \(j\)-by-\(j\) matrices is explicitly
\[
\nu_{2s}(q)=q^{s(s+1)}\prod_{i=1}^s(q^{2i-1}-1),\qquad
\nu_{2s+1}(q)=q^{s(s+1)}\prod_{i=0}^s(q^{2i+1}-1).
\]
These product formulas include \(\nu_0(q)=1\), and are valid in **all** characteristics.

For every \(t\geq2\), the rank of an invariant form on \(L_{F_t}\), whose dimension is \(5t+1\), has the **sharp maximum** \(4t+2\). The rank \(4t+1\) never occurs. The exact numbers at the top two attainable ranks are
\[
\#\{\operatorname{rank}B=4t+2\}=(q-1)^tq^N,\qquad
\#\{\operatorname{rank}B=4t\}=t(q-1)^tq^{N-1}.
\]
Thus the minimum possible radical dimension is \(t-1\); radical dimension \(t\) is impossible. For \(t=1\), the same full enumerator applies but the separate second-highest-rank formula above is **not** asserted.

## Assumptions and scope
A graphical Lie algebra is the \(k\)-space \(L_G=V\oplus W\) with vertex basis \(v_1,\ldots,v_n\), edge basis \(z_{ij}\) for \(\{i,j\}\in E(G)\), and alternating bracket \([v_i,v_j]=z_{ij}\) when \(i<j\) is an edge, with all edge vectors central; for missing edges the bracket is zero. This definition works in characteristic two because the bracket remains alternating and satisfies Jacobi. A symmetric bilinear form is ad-invariant if \(B([x,y],z)=B(x,[y,z])\) for every \(x,y,z\in L_G\). No nondegeneracy is assumed. Rank means the rank of the full symmetric matrix of \(B\), not of its vertex restriction. For the finite-field enumerator \(q\) is any prime power, \(t\geq1\), and \(z\) is a formal indeterminate.

## Proof
**1. Triangle coordinates.** Put \(A=B|_{V\times V}\). Since \(W=[L_G,L_G]\) is central, ad-invariance gives \(B(W,W)=0\). Set \(T(x,y,z)=B([x,y],z)\) for \(x,y,z\in V\). The bracket is alternating, and ad-invariance and symmetry imply that \(T\) is an alternating trilinear form, including in characteristic two. If a pair among three distinct vertices is not an edge, cyclic alternation gives \(T(v_i,v_j,v_k)=0\). Hence \(T\) can be nonzero only on three-cliques, and there is precisely one freely chosen scalar \(\lambda_{ijk}\) per triangle with \(i<j<k\). Conversely, given any symmetric matrix \(A\) and arbitrary such triangle scalars, set
\[
B(v_i,v_j)=A_{ij},\quad B(z_{ij},z_{ab})=0,\quad
B(z_{ij},v_k)=T(v_i,v_j,v_k),
\]
with the last entry equal to the assigned alternating triangle coefficient when all three vertices form a triangle, and zero otherwise. This determines a symmetric invariant form: the only nonzero invariance checks involve three vertices and are precisely cyclic alternation of \(T\). The data are independent, proving the direct-sum description and dimension. If an edge lies in no triangle its edge vector is radical for every form. Conversely, an edge occurring in some triangle pairs nontrivially with the third vertex for a choice of its triangle coefficient, and arbitrary \(A\) separates every nonzero vertex component. Independently varying each triangle coefficient shows no nonzero linear combination supported on triangle edges can lie in every radical; this proves the common-radical assertion.

**2. Universal rank reduction.** Let \(C:W\to V^*\) be the cross-pairing map, with entries \(B(v_i,z_{ab})\), and set \(r=\operatorname{rank}C\), \(K=\ker(C^T:V\to W^*)\). The form has block matrix
\[
M_B=\begin{pmatrix}A&C\\ C^T&0\end{pmatrix}.
\]
Choose complements to \(K\subset V\) and \(\ker C\subset W\), with the latter two complements perfectly paired. The resulting \(2r\)-dimensional block has the shape \(\left(\begin{smallmatrix}D&I\\I&0\end{smallmatrix}\right)\), which is invertible in every characteristic and has inverse \(\left(\begin{smallmatrix}0&I\\I&-D\end{smallmatrix}\right)\). Its Schur complement on \(K\) is exactly \(A|_K\). Therefore
\[
\operatorname{rank}B=2r+\operatorname{rank}(A|_K).
\]
This is a rank identity, not a claim about hyperbolic isometry types in characteristic two.

**3. Windmill triangle weights.** Number the vertices of \(F_t\) as a hub \(h\) and private vertices \(a_i,b_i\), with triangles \(\{h,a_i,b_i\}\), \(1\le i\le t\). Let \(\lambda_i=T(h,a_i,b_i)\). If precisely \(k\) of these weights are nonzero, then the image of \(C\) is, for \(k>0\), the span in \(V^*\) of the hub coordinate and the two private coordinates of each active triangle. Thus \(r_k=2k+1\); for \(k=0\) it is zero. The kernel \(K\) has dimension \(d_k=n-r_k\); for \(k>0\) it is literally spanned by the private vertices belonging to inactive triangles. There are \(\binom tk(q-1)^k\) ways to choose which weights are active and their nonzero values.

**4. Counting ranks.** For a fixed cross-pairing of rank \(r_k\), restriction of a symmetric \(n\)-by-\(n\) matrix \(A\) to \(K\) is a surjective linear map onto the \(\binom{d_k+1}{2}\)-dimensional space of symmetric forms on \(K\); every fiber has cardinality \(q^{N-\binom{d_k+1}{2}}\). A rank-\(j\) symmetric form on a \(d\)-space is specified by its \((d-j)\)-dimensional radical and a nonsingular symmetric form on the quotient. Thus there are exactly \({d\brack j}_q\nu_j(q)\) choices. The displayed products for \(\nu_j(q)\) follow by finite classical-group orbit enumeration. Write \(g_j=|\operatorname{GL}_j(q)|=\prod_{a=0}^{j-1}(q^j-q^a)\) and \(s_u=|\operatorname{Sp}_{2u}(q)|=q^{u^2}\prod_{a=1}^u(q^{2a}-1)\). In odd dimension \(j=2u+1\), the count is \(g_j/s_u\): for odd \(q\), sum the two discriminant orbits, whose orthogonal stabilizers each have order \(2s_u\); for even \(q\), the single nonalternating orbit has stabilizer order \(s_u\). In even dimension \(j=2u\) and odd \(q\), sum the two orthogonal orbits with stabilizer orders \(2q^{u(u-1)}(q^u-1)\prod_{a=1}^{u-1}(q^{2a}-1)\) and \(2q^{u(u-1)}(q^u+1)\prod_{a=1}^{u-1}(q^{2a}-1)\). For even \(q\), sum the alternating orbit \(g_j/s_u\) and the nonalternating orbit \(g_j/(q^{2u-1}s_{u-1})\). Cancelling factors in both parity regimes yields exactly the stated characteristic-independent products; the zero-dimensional case is one. Thus the full polynomial formula holds over every finite field.

**5. Sharp top ranks.** For \(t\geq2\), choosing all \(t\) weights nonzero gives \(r=n\), \(d=0\), and hence rank \(2n=4t+2\), independently of \(A\); its multiplicity is \((q-1)^tq^N\). If any weight vanishes, \(r\le2t-1=n-2\), so the rank is at most \(2r+(n-r)=n+r\le2n-2=4t\). Thus rank \(4t+1\) is impossible. Rank \(4t\) can only arise with exactly one inactive triangle, with \(r=n-2\), \(d=2\), and a nonsingular two-dimensional restriction \(A|_K\). The number of choices is \(t(q-1)^{t-1}q^{N-3}\nu_2(q)\). Since \(\nu_2(q)=q^2(q-1)\), this equals \(t(q-1)^tq^{N-1}\). The algebra has dimension \(n+e=5t+1\), so the radical statements follow.

## Verification
A standalone Python 3 checker named `check_invariant_forms.py` computes the ad-invariance linear constraints directly from Lie brackets for six graphs (empty graph, path, triangle, four-cycle, two-triangle windmill, and complete four-vertex graph) over \(\mathbb F_2\) and \(\mathbb F_3\). In all 12 comparisons the free dimension equals \(\binom{n+1}{2}+c_3(G)\). It also independently enumerates all symmetric matrices and triangle weights and verifies the full rank polynomial for \(F_1\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), and \(F_2\) over \(\mathbb F_2\). In the latter case the coefficient counts by rank \(0,1,2,3,4,5,6,7,8,10\) are respectively \(1,31,620,4340,13888,13888,8192,24576,32768,32768\); rank \(9\) is absent. The checker also compares the product formulas for nonsingular symmetric matrices against brute-force counts and classical-group orders in the tested small dimensions. The terminal marker is `TRIANGLE_INVARIANT_FORM_RANK_ENUMERATOR_OK 12 4`. These finite checks support but do not replace the general proof.

## Relationship to prior work
Mainkar's graphical class-two construction (arXiv:1310.3414) and the earlier free-nilpotent metric analysis of del Barco–Ovando (arXiv:1104.4773) provide the Lie-algebraic setting. Del Barco (arXiv:1602.08286, Theorem 3.4) already proved over the real numbers that a graphical two-step algebra admits a **nondegenerate** invariant metric exactly when its graph is a disjoint union of triangles and isolated vertices. In particular the nonexistence of such a metric for \(F_t\), \(t\ge2\), is prior work and **not** a novelty claim. Benito, de-la-Concepción and Laliena (arXiv:1604.02923) analyze invariant forms on free nilpotent algebras and their nondegenerate quotients through alternating 3-forms. The present claim instead supplies the explicit triangle-supported parameter space **for arbitrary graphs**, its universal forced radical, and the complete finite-field **rank enumerator** and missing-rank phenomenon for the windmill family; none of the inspected cited results states these rank multiplicities. The general alternating-3-form framework is relevant background and a route toward these calculations, not evidence of independent discovery. See References and the separately recorded originality assessment.

## Limitations
The rank polynomial counts forms as distinct matrices relative to the specified graphical basis, not isometry or automorphism orbits. The classification does not provide rank distributions for every graph, only a parameterization and a rank-reduction identity for general graphs and a closed polynomial for windmills. No new claim is made about existence of nondegenerate invariant metrics for graphical Lie algebras; that existence classification is already known over the real field. All claims are proved over arbitrary fields where indicated and over finite fields for the counting formula; finite computations are corroboration only. Historical priority remains provisional because equivalent specialized counting formulas may exist in less searchable literature. No independent mathematical audit has been performed.

## References
1. G. Ovando and V. del Barco, *Free Nilpotent Lie Algebras Admitting Ad-Invariant Metrics*, first arXiv version 2011-04-25, arXiv:1104.4773, https://arxiv.org/abs/1104.4773.
2. M. G. Mainkar, *Graphs and two-step nilpotent Lie algebras*, first arXiv version 2013-10-12, arXiv:1310.3414, https://arxiv.org/abs/1310.3414.
3. V. del Barco, *Lie algebras admitting symmetric, invariant and nondegenerate bilinear forms*, first arXiv version 2016-02-26, arXiv:1602.08286, https://arxiv.org/abs/1602.08286; especially Section 3 and Theorem 3.4.
4. P. Benito, D. de-la-Concepción and J. Laliena, *Free nilpotent and nilpotent quadratic Lie algebras*, first arXiv version 2016-04-11, arXiv:1604.02923, https://arxiv.org/abs/1604.02923; especially Sections 1–2 and 4.

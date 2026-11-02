# Witt-type edge gaps in commuting rank-one evolution-algebra retractions

## Finding

Let \(K=\mathbb F_q\) with \(q\) an odd prime power, and let \(n\ge3\). Take a nonsingular symmetric bilinear form \(B\) on an \(n\)-dimensional vector space \(V\), and a nonzero vector \(u\). On \(V\) put the commutative (generally nonassociative) evolution-algebra product \(x\cdot y=B(x,y)u\). Write \(\Gamma(B,u)\) for the simple commuting graph on rank-one algebra endomorphisms \(P\) with \(P^2=P\): vertices are distinct projections, and adjacency means \(PQ=QP\).

Let \(\mathscr L\) denote the projective singular lines of \(B\), and put \(M=|\mathscr L|\), \(\varepsilon=\mathbf1_{B(u,u)=0}\). When \(\varepsilon=0\), let \(S\) be the number of singular lines in the nondegenerate hyperplane \(u^\perp\). When \(\varepsilon=1\), let \(J\) be the number of singular lines in the nondegenerate orthogonal quotient \(u^\perp/Ku\). In dimension zero the singular-line count is defined to be zero.

The graph has an intrinsic incidence model. Its vertices are pairs \((\ell,H)\) with \(\ell\in\mathscr L\setminus\{Ku\}\), \(H\) a hyperplane containing \(u\), and \(\ell\not\subset H\); the pair represents the unique projection with image \(\ell\) and kernel \(H\). Distinct vertices \((\ell,H),(m,H')\) commute if and only if \(\ell\subset H'\) and \(m\subset H\). In particular, their products vanish in both orders. Exactly \(q^{2n-6}\) commuting projection pairs lie over any unordered pair of distinct singular lines \(\ell,m\ne Ku\) with \(u\notin\ell+m\), and there are none over such a pair with \(u\in\ell+m\).

Consequently, writing \(v(\Gamma)\) and \(e(\Gamma)\) for the vertex and edge counts,
\[
v(\Gamma)=q^{n-2}(M-\varepsilon),\qquad
 e(\Gamma)=q^{2n-6}\begin{cases}
\binom M2-(M-S)/2,&\varepsilon=0,\\
\binom{M-1}2-q(q-1)J/2,&\varepsilon=1.
\end{cases}
\]
The quantities \(M,S,J\) are fully explicit using the finite quadratic-space formula below.

**Odd-dimensional norm-class gap.** For fixed \(B\) and odd dimension \(n=2s+1\ge3\), choosing anisotropic \(u\) from either possible square class of \(B(u,u)\) produces graphs with exactly the same number of vertices, but edge counts differing by precisely
\[
q^{2n-6+s-1}=q^{(5n-15)/2}.
\]
This supplies a commuting-retraction graph invariant separating the two anisotropic norm classes, even though their projection counts coincide. For \(B\) the ordinary dot product on \(\mathbb F_3^3\), \(u=(1,0,0)\) gives \((v,e)=(12,4)\), whereas \(u=(1,1,0)\) gives \((12,5)\); isotropic \(u=(1,1,1)\) gives \((9,3)\).

## Assumptions and scope

The field has arbitrary odd prime-power order; characteristic two is not asserted. The form \(B\) is nondegenerate; the vector \(u\) is nonzero and may be singular or nonsingular. The algebra is an evolution algebra because \(B\) is diagonalizable over fields of odd characteristic, so an orthogonal basis is a natural basis. A projection is an algebra homomorphism and an idempotent for **composition**; this must not be confused with idempotent elements of the nonassociative algebra. The graph contains only rank-one, nonzero projections; loops are excluded. Every assertion holds for all \(n\ge3\), including the smallest-dimensional quotient boundary.

For a nondegenerate quadratic space \((W,Q)\) of dimension \(d\), its singular-line count \(L(W)\) is zero when \(d=0\), equals \((q^{d-1}-1)/(q-1)\) when \(d\) is odd, and when \(d=2t>0\) equals
\[
L(W)=\frac{q^{2t-1}-1}{q-1}+\sigma q^{t-1},\qquad
\sigma=\chi\bigl((-1)^t\det(B|_W)\bigr)\in\{-1,1\}.
\]
Here \(\chi\) is the nonzero quadratic character and the determinant is evaluated in any basis; its square class is intrinsic. For nonsingular \(u\), apply the formula to \(W=u^\perp\), where the determinant square class is \(\det(B)/B(u,u)\). For singular \(u\), apply it to \(W=u^\perp/Ku\), whose form is nondegenerate and has dimension \(n-2\). Both cases make the edge formula numerical without enumerating the graph.

## Proof

**1. Classify rank-one algebra retracts.** An algebra endomorphism \(T\) satisfies
\[
B(Tx,Ty)u=B(x,y)T(u)\quad\text{for all }x,y\in V.
\]
Because \(B\) is nondegenerate and \(u\ne0\), this forces \(T(u)=c u\) and \(B(Tx,Ty)=c B(x,y)\) for one scalar \(c\). If \(\operatorname{rank}T=1\), the left form has rank at most one while \(B\) has rank \(n\ge3\), so \(c=0\). Hence \(T(u)=0\) and \(\operatorname{im}T\) is totally singular. Conversely, any linear map satisfying these two conditions preserves multiplication, since both \(T(xy)\) and \(T(x)T(y)\) vanish. A rank-one linear idempotent is uniquely specified by its image line \(\ell\) and complementary kernel hyperplane \(H\). Here these must obey \(B(\ell,\ell)=0\), \(u\in H\), and \(\ell\not\subset H\). This proves the incidence model. If \(u\in\ell\), no kernel can contain \(u\) and complement \(\ell\); otherwise, for fixed nonzero \(v\in\ell\), the linear functional \(f\) defining \(P(x)=f(x)v\) has \(f(v)=1\) and \(f(u)=0\). These are two independent linear equations on \(V^*\), giving \(q^{n-2}\) projections per permissible line and the stated vertex count.

**2. Determine adjacency and fiber sizes.** If distinct rank-one idempotents \(P,Q\) commute, the image of \(PQ\) lies in both one-dimensional images. If these images are different, \(PQ=QP=0\); if they coincide, the identities \(PQ=Q\) and \(QP=P\) force \(P=Q\), a contradiction. Therefore distinct vertices commute exactly when each image line lies in the other's kernel. Fix distinct permissible singular lines \(\ell=Kv\), \(m=Kw\). Writing \(P=vf\), \(Q=wg\), the equations are \(f(v)=g(w)=1\), \(f(u)=g(u)=0\), and \(f(w)=g(v)=0\). If \(u\notin Kv+Kw\), each functional obeys three independent equations and has \(q^{n-3}\) choices, giving \(q^{2n-6}\) unordered edges over \(\{\ell,m\}\). If \(u\in Kv+Kw\), the equations contradict one another: the vector \(u\) has nonzero coefficients on both \(v,w\), because neither line equals \(Ku\). Thus that fiber contributes zero edges.

**3. Count forbidden line pairs, nonsingular case.** Suppose \(B(u,u)\ne0\). For any singular line \(\ell=Kv\), the plane \(Ku+Kv\) has a second singular line different from \(\ell\) if and only if \(B(u,v)\ne0\). Indeed, \(Q(v+tu)=2tB(u,v)+t^2Q(u)\), with projectively distinct second root \(t=-2B(u,v)/Q(u)\) precisely when \(B(u,v)\ne0\). These second lines pair up by an involution, while the \(S\) singular lines in \(u^\perp\) have no second partner. Hence there are exactly \((M-S)/2\) forbidden unordered pairs. Removing those from \(\binom M2\) proves the first edge formula.

**4. Count forbidden line pairs, singular case.** Suppose \(B(u,u)=0\). There are \(M-1\) allowed singular lines other than \(Ku\). A line \(\ell=Kv\) not orthogonal to \(u\) has no second allowed singular line in \(Ku+Kv\), since \(Q(v+tu)=2tB(u,v)\). If \(\ell\subset u^\perp\), the plane \(Ku+\ell\) is totally singular and contains exactly \(q\) allowed projective lines besides \(Ku\), of which \(q-1\) differ from \(\ell\). Each singular line of \(u^\perp/Ku\) lifts to such a totally singular plane containing \(Ku\), and this plane contains \(q\) allowed lines. Therefore exactly \(qJ\) allowed lines have \(B(u,\ell)=0\), giving \(qJ(q-1)/2\) forbidden unordered pairs. This proves the second edge formula.

**5. Quadric formulas and odd-dimensional edge gap.** Write \(Z(W)=|\{w\in W:Q(w)=0\}|\). For a hyperbolic plane \(H\), in split coordinates the equation \(Q(h)=c\) has \(2q-1\) solutions when \(c=0\) and \(q-1\) otherwise. Thus, for \(W=H\perp W_0\) with \(\dim W_0=d-2\),
\[
Z(W)=qZ(W_0)+(q-1)q^{d-2}.
\]
The anisotropic two-dimensional core has \(Z=1\), the hyperbolic plane has \(Z=2q-1\), and a nondegenerate one-dimensional core has \(Z=1\). The standard Witt decomposition over finite fields of odd order and induction yield \(Z=q^{d-1}\) for odd \(d\), and \(Z=q^{d-1}+(q-1)\sigma q^{(d-2)/2}\) for even \(d\), where \(\sigma=\chi((-1)^{d/2}\det B_W)\). Dividing \(Z-1\) by \(q-1\) yields the quoted singular-line formulas. In odd ambient dimension \(n=2s+1\), the nondegenerate hyperplane \(u^\perp\) has dimension \(2s\) and its sign changes when \(Q(u)\) moves between square classes. Its two possible singular-line counts differ by \(2q^{s-1}\). The ambient \(M\) is fixed, so the edge totals differ by \(q^{2n-6}q^{s-1}=q^{(5n-15)/2}\). Every nonzero field element is represented by a nondegenerate quadratic form in \(n\ge3\) over a finite field of odd order, so both classes occur. The proof is complete.

## Verification

The standalone `verify_retraction_graph.py` independently constructs normalized singular lines, lists all rank-one projections via linear functionals, and compares each graph edge by literal composition of two rank-one matrices. It checks nine \((q,n,u)\) configurations for \(q\in\{3,5\}\) and \(n\in\{3,4\}\). For \(q=3\) and \(n=3\), a second, independent test examines all \(3^9\) linear endomorphism matrices, filters by rank one and composition-idempotence, and checks the algebra-homomorphism equation on all basis products. The resulting maps exactly match those from the incidence construction for three inequivalent choices of \(u\). The verifier prints `VERIFY_OK`. These finite checks do not establish the unrestricted theorem; Steps 1–5 prove it.

## Relationship to prior work

Boudi, Cabrera Casado and Siles Molina (arXiv:2006.14460v1, posted 2020-06-25) study natural families, evolution subspaces and algebra homomorphism preliminaries, but not commuting graphs of rank-one idempotent algebra endomorphisms. Paniello (*Markov evolution algebras*, online 2021-02-28) studies real row-stochastic evolution algebras and their evolution in time. The present family is algebraic over finite fields, not itself a real stochastic Markov model.

Martín Barquero, Martín González and Sánchez-Ortega (*Commutative Algebras with One-Dimensional Square*, published online 2025-02-26) classify these algebras using pointed bilinear spaces and, for their nonsingular-idempotent category, express algebra morphisms by the same bilinear compatibility identity. The morphism reduction in Step 1 is therefore established background, not an independently novel general endomorphism theorem. Their Sections 4.1–4.2 and Theorem 4.9 do not supply the rank-one idempotent **commuting-graph edge census** or its odd-dimensional norm-class gap. The finite orthogonal-point formulas are classical. The assessed additional result is the exact incidence/commutation classification and edge count in the evolution-algebra setting, especially its discriminatory norm-class gap. Searches for equivalent polar-graph, zero-product projection and finite-field evolution-retraction formulations did not find a covering result; priority beyond the inspected literature is not asserted.

## Limitations

The theorem is restricted to nondegenerate \(B\), odd-characteristic finite fields, rank-one composition-idempotent **algebra endomorphisms**, and \(n\ge3\). It makes no claim about higher-rank retractions, the full endomorphism monoid, characteristic two, or universal publication priority. The underlying pointed-space classification is prior work. Independent validation has not been performed.

## References

1. N. Boudi, Y. Cabrera Casado, M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460v1 (posted 2020-06-25), https://arxiv.org/abs/2006.14460.
2. I. Paniello, *Markov evolution algebras*, *Linear and Multilinear Algebra* 70 (2022), 4633–4653; first online 2021-02-28, doi:10.1080/03081087.2021.1893636.
3. D. Martín Barquero, C. Martín González, J. Sánchez-Ortega, *Commutative Algebras with One-Dimensional Square*, *Mediterranean Journal of Mathematics* 22 (2025), article 48; first online 2025-02-26, doi:10.1007/s00009-025-02812-7. Accessible full text: https://d-nb.info/1367481449/34.

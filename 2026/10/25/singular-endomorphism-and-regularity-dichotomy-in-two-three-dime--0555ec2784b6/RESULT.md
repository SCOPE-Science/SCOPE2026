# Singular endomorphism and regularity dichotomy in two three-dimensional Leibniz algebras

## Finding

For every prime power \(q\), let \(J_q\) be the three-dimensional left Leibniz algebra over \(\mathbb F_q\) with ordered basis \(e,f,z\) and only nonzero basis product \([e,f]=z\). For odd \(q\), let \(H_{q,\lambda}\) have only the products \([e,e]=z\) and \([f,f]=\lambda z\), where \(\lambda\in\mathbb F_q^\times\) and \(-\lambda\) is nonsquare in \(\mathbb F_q\). (All omitted brackets vanish.) These are class-two nilpotent non-Lie Leibniz algebras.

For \(L\) one of these algebras, write \(E(L)=\operatorname{End}_{\mathbb F_q}(L)\) and define the rank enumerator \(R_L(t)=\sum_{F\in E(L)}t^{\operatorname{rank}(F)}\). The full polynomials are

\[
R_{J_q}(t)=1+(q^2-1)(2q+1)t+2q(q-1)(q^2-1)t^2+q^2(q-1)^2t^3,
\]
\[
R_{H_{q,\lambda}}(t)=1+(q^2-1)t+2q^2(q^2-1)t^3.
\]

Call \(F\in E(L)\) **regular** (in the von Neumann sense) when there exists \(G\in E(L)\) with \(FGF=F\). Let \(I(L)=|\{F\in E(L):F^2=F\}|\) and \(V(L)=|\{F\in E(L):\exists G\in E(L),FGF=F\}|\). Then

\[
I(J_q)=2q^2+2,\qquad V(J_q)=q^4+q^2-2q+1,
\]
\[
I(H_{q,\lambda})=2,\qquad V(H_{q,\lambda})=1+2q^2(q^2-1).
\]

More precisely, in \(J_q\), the regular maps are exactly zero, the automorphisms and the rank-one endomorphisms whose induced map on \(L/\mathbb F_qz\) is nonzero. In \(H_{q,\lambda}\), the regular maps are exactly zero and the automorphisms. Therefore, as the field order grows over odd prime powers (with the admissible parameter chosen for each field),

\[
\frac{V(J_q)}{|E(J_q)|}\longrightarrow\frac13,
\qquad
\frac{V(H_{q,\lambda})}{|E(H_{q,\lambda})|}\longrightarrow1.
\]

The rank-two stratum exists in \(J_q\) and is empty in \(H_{q,\lambda}\). Thus two canonical small non-Lie Leibniz algebras have sharply contrasting singular endomorphism geometry even though both have one-dimensional derived ideal and three-dimensional underlying vector space.

## Assumptions and scope

The characteristic of \(\mathbb F_q\) is unrestricted for \(J_q\). The anisotropic family \(H_{q,\lambda}\) is defined here only for odd \(q\), and its parameter is required to satisfy the nonsquare condition. Both are bilinear left Leibniz algebras because their bracket values lie in a central one-dimensional ideal. All linear-map ranks refer to the underlying three-dimensional vector spaces. Composition is ordinary function composition; in matrix notation \(FGF\) means \(F\circ G\circ F\). A von Neumann regular endomorphism is not to be confused with a regular element of a Lie algebra or a regular matrix in the invertibility sense.

## Proof

**General reduction.** In each family \([L,L]=\mathbb F_q z\) is nonzero and central. Every algebra endomorphism \(F\) preserves this characteristic derived ideal. Relative to the direct sum \(L=\langle e,f\rangle\oplus\langle z\rangle\), it consequently has a unique matrix

\[
F=\begin{pmatrix}A&0\\w&s\end{pmatrix},\qquad A\in M_2(\mathbb F_q),\quad w\in\mathbb F_q^{1\times2},\quad s\in\mathbb F_q.
\]

Let \(B\) be the matrix of the bracket form, so that \([u,v]=u^{\mathsf T}Bv\,z\) for quotient coordinate columns \(u,v\). Checking the four basis brackets shows that \(F\) is an endomorphism if and only if

\[
A^{\mathsf T}BA=sB. \tag{1}
\]

The row \(w\) is unrestricted whenever (1) holds. This also proves there are no other endomorphisms.

**The one-sided algebra.** In \(J_q\), \(B=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\). Put \(A=\left(\begin{smallmatrix}a&c\\b&d\end{smallmatrix}\right)\). Equation (1) reads

\[
ab=bc=cd=0,\qquad s=ad.\tag{2}
\]

The only possibilities are the zero matrix \(A\), a nonzero matrix with only its first row supported, a nonzero matrix with only its second row supported, or an invertible diagonal matrix \(\operatorname{diag}(a,d)\) with \(a,d\ne0\). These classes are disjoint. There are respectively \(1\), \(2(q^2-1)\), and \((q-1)^2\) matrices of the first, middle (combined), and final kinds; the associated scalars \(s\) are zero in the first two kinds and nonzero in the last.

For \(A=0\), choosing \(w=0\) gives the zero map, and choosing \(w\ne0\) gives a rank-one map. For a nonzero one-row \(A\), \(s=0\); the map \(F\) has rank one precisely when the row \(w\) lies in the one-dimensional row space of \(A\), giving \(q\) choices, and otherwise rank two, giving \(q^2-q\) choices. For invertible diagonal \(A\) we have \(s\ne0\), so every choice of \(w\) gives rank three. This yields exactly the polynomial \(R_{J_q}(t)\) above and \(|E(J_q)|=q^3(3q-2)\).

Idempotence implies \(A^2=A\) and \(wA+sw=w\), besides \(s^2=s\). The zero-\(A\) case forces \(w=0\). For invertible \(A\), the only idempotent is \(F=I\). Every nonzero one-row idempotent \(A\) has its nonzero diagonal entry equal to \(1\), and each of the two row types has \(q\) choices of its other nonzero-row parameter and \(q\) choices of \(w\) in its row space; hence \(I(J_q)=2q^2+2\).

For regularity, every central-image map \(F\) with \(A=0\) and \(w\ne0\) has \(F(z)=0\), so \(FGF=0\) for every endomorphism \(G\), and is nonregular. If \(F\) has rank two, then necessarily \(s=0\) and the image of \(F\) includes \(z\); the restriction of \(F\) to any two-dimensional image \(G(\operatorname{im}F)\) kills its central component, and \(G(z)\in\mathbb F_qz\), so \(FGF\) has rank at most one and cannot equal \(F\). Conversely, suppose \(A\) is a nonzero one-row matrix and \(w\) belongs to its row space. Then \(F\) has rank one with image spanned by either \(e+u z\) or \(f+u z\) for some \(u\). A coefficient of the nonzero row of \(A\) is invertible. A one-row endomorphism \(G\) can therefore be chosen to send that spanning vector to the corresponding rescaled input basis vector; using equation (2), the other quotient column and the central row of \(G\) may be zero. This constructs \(FGF=F\). Zero and automorphisms are also regular. Hence

\[
V(J_q)=1+2q(q^2-1)+q^2(q-1)^2=q^4+q^2-2q+1.
\]

**The anisotropic algebra.** In \(H_{q,\lambda}\), \(B=\operatorname{diag}(1,\lambda)\) and the associated quadratic form \(x^2+\lambda y^2\) is anisotropic by assumption. If \(s=0\), each column of \(A\) is isotropic by equation (1), and thus \(A=0\). If \(s\ne0\), taking determinants in (1) shows that \(A\) is invertible. Therefore every nonzero induced quotient map is a similitude of \(B\).

Identify the quotient with the quadratic extension \(\mathbb F_{q^2}\) so that this quadratic form is the field norm. A norm similitude is exactly a map \(x\mapsto c x\) or \(x\mapsto c x^q\), for \(c\in\mathbb F_{q^2}^\times\); these two forms give distinct maps because \(q\) is odd. Thus \(B\) has precisely \(2(q^2-1)\) similitudes. Every such \(A\) admits \(q^2\) choices of \(w\) and gives an automorphism of rank three. When \(A=0\), the \(q^2\) possible \(w\) give one rank-zero and \(q^2-1\) rank-one endomorphisms, none of rank two. This proves \(R_{H_{q,\lambda}}(t)\) and \(|E(H_{q,\lambda})|=q^2(2q^2-1)\).

Any nonzero rank-one map has central image and annihilates \(z\), and hence is square-zero; it is neither idempotent nor regular. Any invertible endomorphism is regular, and the only invertible idempotent is the identity. This yields \(I(H_{q,\lambda})=2\) and \(V(H_{q,\lambda})=1+2q^2(q^2-1)\).

The asymptotic proportions follow by dividing the displayed regular counts by their exact endomorphism counts and comparing leading powers of \(q\). The conclusion is uniform over permissible \(\lambda\) because every nonsquare form is equivalent under a suitable change of quotient basis.

## Verification

The included self-contained Python program `verify.py` independently enumerates all possible induced \(2\times2\) quotient matrices by testing the four original bracket-preservation equations. It reconstructs complete \(3\times3\) endomorphism matrices for all central-coordinate rows, computes ranks by modular Gaussian elimination, directly checks idempotence, and for the small cases explicitly tests whether each map satisfies \(FGF=F\) for some endomorphism \(G\). Running `python verify.py` produced `VERIFY_OK` with checks for \(J_q\) over prime fields \(q=2,3,5\) and \(H_{q,\lambda}\) at \((q,\lambda)=(3,1),(5,2),(7,4)\). For \(q=2,3\) in the first family and \(q=3\) in the second, regularity is verified by exhaustive endomorphism-pair enumeration. In the larger tests, the regularity count is compared with the proved structural classification, not exhaustively paired. These finite checks do not constitute a proof for all prime powers.

## Relationship to prior work

Kurdachenko, Pypka, and Semko's first work (arXiv:2305.00592v1) identifies the automorphism group of the three-dimensional Leibniz algebra whose original brackets become \([e,f]=z\) after a change of basis. Their later work (arXiv:2310.11180v1) treats the anisotropic one-dimensional-derived case and determines its automorphism group. The classification and counts of automorphisms are **prior structural information**, not the novelty claimed here. The contribution of the present theorem is the full singular endomorphism rank census, its idempotent and regular-element subcensuses, and the exact asymptotic contrast between the two families. Previously published work on low-dimensional derivation algebras concerns derivations rather than multiplicative endomorphisms. An equivalent census under alternate bilinear-form or endomorphism-monoid terminology may exist; the investigation does not prove exhaustive publication priority.

## Limitations

The anisotropic assertion excludes characteristic two and isotropic symmetric forms. The comparison is between these two specific algebra isomorphism types, not an arbitrary-class classification of three-dimensional Leibniz algebras. The asserted limit is taken as the field size tends to infinity, not as dimension grows. The tests involve prime fields only; general finite-field orders are handled by the proof. 

## References

1. L. A. Kurdachenko, O. O. Pypka, and M. M. Semko, *Automorphism groups of some 3-dimensional Leibniz algebras*, arXiv:2305.00592v1 (first posted 2023-04-30), https://arxiv.org/abs/2305.00592.
2. L. A. Kurdachenko, O. O. Pypka, and M. M. Semko, *On the automorphism groups of some nilpotent 3-dimensional Leibniz algebras*, arXiv:2310.11180v1 (first posted 2023-10-17), https://arxiv.org/abs/2310.11180.
3. L. A. Kurdachenko, M. M. Semko, and V. S. Yashchuk, *On the algebra of derivations of some nilpotent Leibniz algebras*, Researches in Mathematics 31(1) (2023), https://vestnmath.dnu.dp.ua/index.php/rim/article/view/400.

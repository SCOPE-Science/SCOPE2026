# Five-dimensional monomial algebras with indistinguishable finite automorphism groups

## Finding
Let \(k=\mathbb F_2\) and consider the two commutative, unital monomial algebras
\[
A=k[x,y]/(x^2,xy^2,y^3),\qquad
B=k[x,y]/(xy,x^3,y^3).
\]
Both are five-dimensional split local algebras, with maximal ideals \(\mathfrak m_A,\mathfrak m_B\) satisfying \(\mathfrak m^3=0\) and Hilbert function \((1,2,2)\). They are **not isomorphic as algebras**, but their abstract groups of \(k\)-algebra automorphisms are isomorphic:
\[
\operatorname{Aut}_k(A)\cong\operatorname{Aut}_k(B)
\cong (C_2)^4\rtimes C_2,
\]
where the nontrivial element of \(C_2\) acts on \(\mathbb F_2^4\) as the direct sum of two nontrivial two-dimensional unipotent Jordan blocks. Each automorphism group has order \(32\), center of order \(4\), and commutator subgroup of order \(4\).

Moreover, these two isomorphism types **exhaust** the commutative local monomial \(\mathbb F_2\)-algebras with embedding dimension two, radical cube zero and Hilbert function \((1,2,2)\). Dimension five is the smallest possible dimension for distinct two-generated local monomial \(\mathbb F_2\)-algebras with the same Hilbert function and isomorphic abstract automorphism groups. Thus even fixing vector-space dimension, embedding dimension, Loewy length and the entire Hilbert function does not make the finite rational automorphism group a complete invariant.

## Assumptions and scope
All automorphism groups are **groups of \(\mathbb F_2\)-rational algebra automorphisms viewed as abstract finite groups**, not algebraic groups or group schemes. The minimality statement concerns commutative unital *monomial* quotients of \(\mathbb F_2[x,y]\) with two-dimensional cotangent space; it does not assert minimality among arbitrary nonmonomial algebras or larger embedding dimensions. A Hilbert function \((1,2,2)\) means
\[
\dim A/\mathfrak m=1,\quad \dim\mathfrak m/\mathfrak m^2=2,\quad \dim\mathfrak m^2=2,\quad\mathfrak m^3=0.
\]
The characteristic-zero algebraic-group reconstruction theorem for monomial algebras is **not contradicted**.

## Proof
**1. Nonisomorphism and identical filtrations.** A basis of \(A\) is \(1,x,y,y^2,xy\), whereas a basis of \(B\) is \(1,x,y,x^2,y^2\). The asserted Hilbert functions follow. Because the characteristic is two and \(\mathfrak m^3=0\), squaring defines a well-defined linear map
\[
F_A:\mathfrak m_A/\mathfrak m_A^2\to\mathfrak m_A^2,\qquad \bar z\mapsto z^2
\]
and likewise \(F_B\). For \(A\), \((a x+b y)^2=b y^2\); hence \(\dim\ker F_A=1\). For \(B\), \((a x+b y)^2=a x^2+b y^2\), so \(\ker F_B=0\). These kernel dimensions are invariant under algebra isomorphism. Thus \(A\not\cong B\).

**2. Automorphism group of \(A\).** An endomorphism is determined by the images of \(x,y\). Since an automorphism induces an invertible map on \(\mathfrak m/\mathfrak m^2\), and the condition \(\phi(x)^2=0\) forces the coefficient of \(y\) in \(\phi(x)\) to vanish, its generator images have the unique form
\[
\phi(x)=x+u y^2+v xy,\qquad
\phi(y)=y+t x+s y^2+r xy,
\qquad u,v,s,r,t\in k.
\]
Every such choice respects the defining monomial relations; the linear part is invertible, hence it is an automorphism by the nilpotent local inverse criterion. There are \(2^5=32\) choices. Let \(N_A\) be the subgroup with \(t=0\), and write \(n_A(u,v,s,r)\) for its members. Because all elements of \(N_A\) fix \(y^2\) and \(xy\), composition adds these four coordinates. Thus \(N_A\cong(C_2)^4\). The involution
\[
T_A(x)=x,\qquad T_A(y)=y+x
\]
complements \(N_A\), and explicit conjugation gives
\[
T_A n_A(u,v,s,r)T_A^{-1}=n_A(u,v,s+u,r+v).
\]
Thus \(\operatorname{Aut}(A)=N_A\rtimes\langle T_A\rangle\).

**3. Automorphism group of \(B\).** Since \(xy=0\) while \(x^2,y^2\) are independent, the invertible tangent map of an automorphism must be a monomial \(2\times2\) matrix. Over \(k=\mathbb F_2\), the only possibilities are the identity and the transposition. Automorphisms inducing the identity are
\[
 n_B(C):\quad
 \begin{pmatrix}x\\y\end{pmatrix}
 \longmapsto
 \begin{pmatrix}x\\y\end{pmatrix}
 +C^\mathsf{T}\begin{pmatrix}x^2\\y^2\end{pmatrix},
 \qquad C\in M_2(k),
\]
where columns of \(C\) specify the socle additions to \(x\) and to \(y\). Every such automorphism fixes \(x^2,y^2\), so their subgroup \(N_B\) is \((M_2(k),+)\). The swap \(S_B(x)=y,\ S_B(y)=x\) is an involution and conjugation is
\[
S_B n_B(C) S_B^{-1}=n_B(PCP),\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
This gives \(\operatorname{Aut}(B)=N_B\rtimes\langle S_B\rangle\), also of order \(32\).

**4. Explicit group isomorphism.** Write \(E_{11},E_{12}\) for matrix units and let \(I,P\) be the identity and swap matrices in \(M_2(k)\). The linear map
\[
\Psi:k^4\longrightarrow M_2(k),\quad
(u,v,s,r)\longmapsto uE_{11}+vE_{12}+sI+rP
\]
is invertible. Since \(PE_{11}P=E_{11}+I\) and \(PE_{12}P=E_{12}+P\) over \(k\), it intertwines the two involutions:
\[
\Psi(u,v,s+u,r+v)=P\Psi(u,v,s,r)P.
\]
It therefore induces the explicit semidirect-product isomorphism
\[
n_A(u,v,s,r)\mapsto n_B(\Psi(u,v,s,r)),
\qquad T_A\mapsto S_B.
\]
Both involutions act with rank-two square-zero difference from the identity on their four-dimensional normal elementary abelian subgroups, yielding the Jordan-block description. For such a semidirect product the center is the two-dimensional fixed subspace and the commutator subgroup is the two-dimensional image of the involution-minus-identity map; both have order four.

**5. Classification and minimality.** A two-generated monomial quotient with \(\mathfrak m^3=0\) is obtained by retaining \(1,x,y\) and a subset of the three quadratic monomials \(x^2,xy,y^2\), with all cubics zero. Hilbert type \((1,2,2)\) means precisely two quadratic monomials survive. Up to exchanging \(x,y\), the omitted quadratic monomial is either \(x^2\) or \(xy\); these yield \(A\) and \(B\). The squaring invariant above distinguishes the two types. In smaller dimensions with two generators, the only possible nontrivial comparison is Hilbert type \((1,2,1)\), for which the two monomial types are \(k[x,y]/(x^2,xy,y^3)\) and \(k[x,y]/(x^2,y^2)\). A direct generator-image count gives automorphism-group orders \(8\) and \(24\), respectively. Hilbert type \((1,2)\) is unique. Hence no smaller-dimensional pair with fixed Hilbert function exists.

## Verification
The accompanying standalone `verify.py` uses exact bit-vector arithmetic in the displayed monomial bases. It independently enumerates all algebra automorphisms by checking the defining zero relations and the invertibility of the tangent map; tests \(|\operatorname{Aut}(A)|=|\operatorname{Aut}(B)|=32\), the dimension-four comparison orders \(8,24\), and the distinct square-map kernels; then verifies bijectivity and all \(32^2=1024\) multiplication instances for the explicit group isomorphism. It prints `VERIFY_OK` when all assertions pass. These finite computations are complete for the four fixed small algebras but do not establish any assertion outside the explicitly stated family.

## Relationship to prior work
Díaz and Lucchini Arteche, arXiv:2409.15081 (first submitted September 23, 2024), prove a characteristic-zero reconstruction theorem for finite-dimensional local monomial algebras from their **algebraic** automorphism groups. Their Example 2.2 discusses derivations for the monomial ideal \((x^3,xy,y^3)\), which also appears here as one member of the pair, but does not provide a second five-dimensional algebra with an isomorphic finite rational automorphism group. The present result is a distinct boundary phenomenon concerning groups of points over \(\mathbb F_2\), not a negation of their characteristic-zero theorem.

Díaz, Liendo, Manzano-Flores and Regeta, arXiv:2408.02197 (first submitted August 5, 2024), describe automorphism groups of zero-dimensional monomial algebras over characteristic-zero fields; their examples address several related monomial presentations but do not imply this finite-characteristic isomorphism. Existing results on truncated coordinate-cross algebras determine the automorphism group of the second algebra \(B\), and a published quadratic-tensor classification distinguishes the two algebra structures. Neither contains the explicit matching automorphism group calculation for \(A\) nor the resulting minimal failure of finite-point reconstruction, as compared in the review. The originality conclusion remains subject to independently locating equivalent statements under different small-ring or finite-group terminology.

## Limitations
The isomorphism of automorphism groups is **abstract**, not an isomorphism of automorphism schemes and not an equivalence of their natural actions on the filtered algebras. This counterexample is specific to the group of \(\mathbb F_2\)-points; it is not asserted for larger finite fields. The minimality claim only covers two-generated monomial local algebras compared at equal Hilbert function. An independent literature review or mathematical audit has not been performed.

## References
1. R. Díaz and G. Lucchini Arteche, *Finite-dimensional monomial algebras are determined by their automorphism group*, arXiv:2409.15081v1, first posted September 23, 2024. https://arxiv.org/abs/2409.15081
2. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197v1, first posted August 5, 2024. https://arxiv.org/abs/2408.02197
3. *Segre-quadric monomiality criterion for two-generated short local algebras*, published mathematical result, 2026. https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-segre-quadric-monomiality-two-generated-short-local-algebras--0eb926948571
4. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, published mathematical result, 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb

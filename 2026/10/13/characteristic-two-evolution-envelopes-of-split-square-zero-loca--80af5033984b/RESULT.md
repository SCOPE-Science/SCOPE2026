# Characteristic-two evolution envelopes of split square-zero local algebras
## Finding
For any field \(K\) of characteristic \(2\), any integer \(r\ge1\), and any \(r\)-dimensional \(K\)-vector space \(V\), set
\[
 A_r=K1\oplus V,\qquad (s1+v)(t1+w)=st1+sw+tv.
\]
An *evolution algebra* is a commutative algebra admitting a basis of pairwise orthogonal elements (the products of distinct basis elements vanish); associativity is not assumed. An *ideal embedding* \(A_r\hookrightarrow E\) is an injective algebra homomorphism whose image is an ideal. Write \(\operatorname{edim}(A_r)\) for the minimum possible \(\dim_K E\). Then
\[
 \boxed{\operatorname{edim}(A_r)=2r+1.}
\]
The constructed minimum is an *evolution envelope*: \(E^2\subseteq A_r\), with the latter identified with its image. The excess in the sense of Costoya–Fernández Ouaridi–Viruel, Theorem 3.5, is exactly \(\varepsilon(A_r)=r\).

In sharp contrast, define the **naive simultaneous-square rank** of a homogeneous quadratic map \(H:A_r\to A_r\) to be the smallest \(s\) for which \(H(a)=\sum_{i=1}^s\ell_i(a)^2w_i\) with \(\ell_i\in A_r^*\) and \(w_i\in A_r\). Since the squaring map in characteristic two is
\[
 H(s1+v)=s^2 1,
\]
its naive simultaneous-square rank is \(1\). Thus the difference between minimal evolution dimension and this square-map rank is exactly \(2r\), unbounded as \(r\to\infty\). The rank-one map does **not** encode the mixed products; this comparison is not a claim that the characteristic-different-from-two Waring correspondence extends to characteristic two.

## Assumptions and scope
The field \(K\) is arbitrary of characteristic \(2\), including imperfect and finite fields. The radical \(V\) is finite-dimensional and square-zero; the algebra is unital and split, with unit \(1\). The statement does not classify nonsplit local algebras, nonunital algebras, or algebras with higher radical nilpotency. All dimensions are over \(K\).

## Proof
**Upper bound and explicit envelope.** Choose a basis \(v_1,\ldots,v_r\) of \(V\). On a vector space of dimension \(2r+1\), choose natural basis
\[
 e_0,e_1,\ldots,e_r,f_1,\ldots,f_r.
\]
Declare products of distinct natural basis elements zero. Introduce
\[
 u=e_0+\sum_{i=1}^r f_i,\qquad z_i=e_i+f_i\quad(1\le i\le r)
\]
and prescribe all basis squares by
\[
 e_0^2=u+\sum_{i=1}^r z_i,\qquad e_i^2=f_i^2=z_i\quad(1\le i\le r).
\]
These prescriptions define an evolution algebra \(E\), with \(E^2\subseteq \operatorname{span}\{u,z_1,\ldots,z_r\}\). The vectors \(u,z_1,\ldots,z_r\) are independent: their \(e_0,e_1,\ldots,e_r\) coordinates are the standard basis. In characteristic two, direct multiplication gives
\[
 u^2=e_0^2+\sum_i f_i^2=u,\qquad
 uz_i=f_i^2=z_i,\qquad z_i^2=e_i^2+f_i^2=0,
\]
while \(z_i z_j=0\) for \(i\ne j\). Therefore \(1\mapsto u\), \(v_i\mapsto z_i\) extends to an injective homomorphism \(A_r\hookrightarrow E\). Since every natural-basis square belongs to this image, \(E^2\subseteq A_r\); in particular the image is an ideal. Hence \(\operatorname{edim}(A_r)\le 2r+1\).

**Lower bound over every characteristic-two field.** Conversely let \(A_r\) be embedded as an ideal in an evolution algebra \(E\) of dimension \(m\), with natural basis \(h_1,\ldots,h_m\). Write \(\ell_i\in A_r^*\) for the \(i\)-th coordinate of an embedded element. If \(\ell_i\not\equiv0\), choose \(a\in A_r\) with \(\ell_i(a)\ne0\). Since \(A_r\) is an ideal, \(h_i a=\ell_i(a)h_i^2\in A_r\), so \(h_i^2\in A_r\). For an inactive coordinate take its coefficient vector as zero. Thus there exist \(w_i\in A_r\) such that the multiplication tensor on \(A_r\) is expressed as
\[
 ab=\sum_{i=1}^m\ell_i(a)\ell_i(b)w_i\qquad(a,b\in A_r).
\]
Let \(U\) be the span of the symmetric bilinear forms \(\ell_i\otimes\ell_i\); therefore \(\dim U\le m\). Let \(\rho:U\to\operatorname{Bil}_{\mathrm{sym}}(V,K)\) denote restriction to \(V\times V\).

With coordinates \(a=(s,x_1,\ldots,x_r)\), \(b=(t,y_1,\ldots,y_r)\), the scalar coordinate bilinear forms of the multiplication \(ab\) are
\[
 B_0(a,b)=st,\qquad B_j(a,b)=s y_j+t x_j\quad(1\le j\le r).
\]
They are linearly independent: the first is detected on \((1,1)\), the others on \((1,v_j)\). They lie in \(U\) by the multiplication decomposition. All vanish on \(V\times V\), so
\[
 \dim\ker(\rho)\ge r+1.
\]
The restricted coordinate functionals \(\ell_i|_V\) span \(V^*\), because the coordinate embedding \(V\hookrightarrow E\) is injective. Choose \(r\) of them that are linearly independent, say \(g_1,\ldots,g_r\). Then their tensor squares \(g_j\otimes g_j\) are linearly independent bilinear forms on \(V\times V\): evaluate on pairs of dual vectors satisfying \(g_j(t_k)=\delta_{jk}\). Hence \(\dim\rho(U)\ge r\). Rank-nullity now yields
\[
 m\ge\dim U=\dim\ker\rho+\dim\rho(U)\ge(r+1)+r=2r+1.
\]
This proves equality without relying on polarization, field cardinality, finite enumeration, or any unproved assertion about tensor-rank classification.

**Squaring-map discrepancy.** In characteristic two, \((s1+v)^2=s^2 1+2sv+v^2=s^2 1\). Therefore \(H=\ell^2 1\) for the unit-coordinate functional \(\ell(s1+v)=s\). Since \(H\ne0\), its minimal square-decomposition length is exactly one. The difference \(\operatorname{edim}(A_r)-1=2r\) follows. The invariant \(\varepsilon(A_r)=r\) follows from Theorem 3.5 of the motivating paper, which applies over arbitrary fields and relates this invariant to minimal envelope dimension.

## Verification
The included standalone `verify.py` directly reconstructs the natural-basis algebra and ideal embeddings and tests multiplication against the declared split square-zero algebra over \(\mathbb F_2\) for ranks \(1\) through \(4\), \(\mathbb F_4\) for ranks \(1,2\), and \(\mathbb F_8\) for rank \(1\). It checks the defining bilinear multiplication on every basis pair, the ideal property on every natural-basis/embedded-basis pair, additional scalar combinations, and the exact bilinear-form ranks \(2r+1\) and \(r\) for the exhibited coordinate restrictions. It prints `VERIFY_OK` on success. These finite checks corroborate the construction only. The arbitrary-field, arbitrary-rank lower bound is the preceding symbolic tensor-restriction proof.

## Relationship to prior work
Costoya, Fernández Ouaridi and Viruel (arXiv:2609.32784v1, 26 September 2026) prove that every finite-dimensional commutative algebra admits an evolution-envelope embedding. Their Theorem 3.5 describes the minimal dimension as the algebra dimension plus an off-diagonal decomposition invariant, over arbitrary characteristic. Their Section 4's squaring-map/Waring correspondence explicitly assumes characteristic different from two. They do not evaluate the invariant for the present family in characteristic two.

The publicly available *Exact evolution dimension of split square-zero local algebras* (2026) proves \(2r+1\) for **characteristic different from two**, using polarization and a quadratic Waring-rank lower bound. The present characteristic-two assertion is a distinct missing case: it has the same numerical envelope dimension but disproves the naive extension of the square-map/Waring interpretation by an unbounded gap. Classical bilinear complexity gives relevant lower-bound context, but the proof above is self-contained and relies on no publication-uniqueness assumption.

## Limitations
The square-decomposition rank in characteristic two is explicitly a naive quadratic-map invariant, not the symmetric bilinear multiplication rank. No assertion is made that all algebra multiplications with the same squaring map have the same envelope dimension. The result is specific to split unital square-zero local algebras. Literature indexing and older characteristic-two bilinear-decomposition results remain possible sources of historical overlap; no independent review has been carried out.

## References
1. Cristina Costoya, Amir Fernández Ouaridi, Antonio Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784v1 (first submitted 26 September 2026), Sections 3–5, especially Theorems 3.5 and 4.2. https://arxiv.org/abs/2609.32784
2. *Exact evolution dimension of split square-zero local algebras* (2026), public mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-evolution-dimension-of-split-square-zero-local-algebras--c49ccd826d54 (characteristic different from two only).
3. A. Alder, V. Strassen, *On the algorithmic complexity of associative algebras*, Theoretical Computer Science 15 (1981), 201–211, DOI:10.1016/0304-3975(81)90070-0 (background lower-bound theory).

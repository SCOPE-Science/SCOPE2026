# Rank and orbit census for splitting projections on the plane exterior algebra

## Finding
Let \(K\) be any field and let \(E=\Lambda_K(K^2)\) be the associative exterior algebra with basis \(1,x,y,z\), with \(xy=z=-yx\), \(x^2=y^2=0\), and \(z\) annihilating \(x,y,z\). A linear map \(P:E\to E\) is an *idempotent weight-minus-one Rota–Baxter operator* when \(P^2=P\) and
\[
P(a)P(b)=P\bigl(P(a)b+aP(b)-ab\bigr) \qquad(a,b\in E).
\]
Put \(J=Kx\oplus Ky\oplus Kz\). Define the incidence set
\[
\mathcal I(K)=\{(T,\ell):T\subset J,\ \dim T=2,\ Kz\subset T,\ \ell\subset J,\ \dim\ell=1,\ \ell\not\subset T\}.
\]
Every such operator is uniquely projection onto its image along its kernel, and its ordered (image, kernel) pair is *exactly* one of the following four isolated pairs or four families:
\[
(0,E),\quad (E,0),\quad(K1,J),\quad(J,K1),
\]
\[
(\ell,K1\oplus T),\quad(K1\oplus T,\ell),\quad(K1\oplus\ell,T),\quad(T,K1\oplus\ell),\qquad (T,\ell)\in\mathcal I(K).
\]
The automorphism group \(\operatorname{Aut}_K(E)\) is transitive on \(\mathcal I(K)\). Consequently there are exactly eight conjugacy classes of these operators over *every* field, including characteristic two: four isolated operators and four families each represented by the same incidence-pair geometry.

For a finite field \(K=\mathbb F_q\), \(|\mathcal I(K)|=q^2(q+1)\). The exact rank-enumerator and total are
\[
\sum_P t^{\operatorname{rank}P}
=1+[1+q^2(q+1)]t+2q^2(q+1)t^2+[1+q^2(q+1)]t^3+t^4,
\]
\[
\boxed{\#\{P\}=4+4q^2(q+1).}
\]
The four non-singleton conjugacy classes each contain exactly \(q^2(q+1)\) operators. The incidence set is an affine-plane bundle over \(\mathbb P^1_K\); this supplies a geometric explanation for the cubic count.

## Assumptions and scope
The field \(K\) is arbitrary: it need not be algebraically closed and may have any characteristic. Subalgebras are allowed to be nonunital. Projections are linear maps with \(P^2=P\), not arbitrary operators satisfying the Rota–Baxter identity. Thus the theorem does *not* assert that every weight-minus-one Rota–Baxter operator in positive characteristic is idempotent.

## Proof
**Projection lemma.** For any associative algebra and idempotent linear map \(P\), write \(E=U\oplus V\), where \(U=\operatorname{im}P\) and \(V=\ker P\). Substituting two elements of \(U\) into the Rota–Baxter identity gives \(uv=P(uv)\), so \(U\) is a subalgebra. Substituting two elements of \(V\) gives \(P(vw)=0\), so \(V\) is a subalgebra. Conversely, if \(U\) and \(V\) are complementary subalgebras, bilinear expansion of the identity on \(U\oplus V\) establishes the Rota–Baxter law; on mixed inputs its right-hand argument vanishes. Thus the objects classified are exactly ordered complementary subalgebra pairs.

**Unit dichotomy.** The radical \(J\) satisfies \(J^3=0\). Every element \(a1+j\), with \(a\ne0\) and \(j\in J\), is invertible. Since its minimal polynomial has a nonzero constant coefficient, \(1\) is a linear combination of positive powers of this element. Every subalgebra containing such an element therefore contains \(1\). It follows that each subalgebra is contained in \(J\) or is of the form \(K1\oplus T\), where \(T\subseteq J\) is a subalgebra.

**Radical subalgebras.** For \(u,v\in J\), their product is
\[
uv=(u_xv_y-u_yv_x)z.
\]
Every radical line is a subalgebra since \(u^2=0\). A radical plane \(T\) is closed under products if and only if \(z\in T\): if \(z\notin T\), its projection to \(J/Kz\) is an isomorphism, so some products span \(Kz\) outside \(T\); the converse follows because \(J^2=Kz\). The entire \(J\) is a subalgebra. Consequently the proper subalgebras are exactly radical lines, radical planes through \(z\), \(J\), and their unital counterparts \(K1\), \(K1\oplus\ell\), and \(K1\oplus T\).

**Complement classification.** In a complementary pair \((U,V)\), the unit belongs to exactly one of the subalgebras: if both contained it, the intersection would be nonzero; if neither did, both would lie in \(J\). If one component is zero, the other is \(E\). If their dimensions are \((1,3)\), the pair is \((K1,J)\) or \((\ell,K1\oplus T)\) with \(\ell\not\subset T\). The reverse \((3,1)\) cases follow by swapping the pair. For dimensions \((2,2)\), one is \(K1\oplus\ell\) and the other is a radical plane \(T\) containing \(z\); direct sum is equivalent to \(\ell\not\subset T\). These are precisely the eight displayed types, with uniqueness because image and kernel determine \(P\).

**Automorphism orbits.** Every algebra automorphism fixes \(1\), preserves \(J\) and \(Kz=J^2\), and has the form
\[
x\longmapsto ax+by+uz,\qquad
 y\longmapsto cx+dy+vz,\qquad
 z\longmapsto(ad-bc)z,
\]
where \(\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\in\operatorname{GL}_2(K)\) and \(u,v\in K\). Conversely every such map preserves multiplication and is invertible. Given two pairs \((T,\ell)\) in \(\mathcal I(K)\), an invertible linear change of \(x,y\) takes the projected line of \(T\) and the transverse projected line of \(\ell\) to their counterparts; adjusting \(u,v\) sends the chosen lift of \(\ell\) to the target lift. Hence the action on \(\mathcal I(K)\) is transitive. The four incidence families are not conjugate to one another, because the ranks and whether the image contains \(1\) or is contained in \(J\) are preserved. The four isolated maps are pairwise distinguished by rank, or, in rank one versus three, by their image. This gives eight orbits.

**Finite-field count and geometry.** Planes \(T\) containing \(z\) are indexed by the lines of \(J/Kz\cong K^2\), hence there are \(q+1\) of them. For each \(T\), the number of lines \(\ell\) in \(J\) outside \(T\) is
\[
\frac{q^3-1}{q-1}-\frac{q^2-1}{q-1}=q^2.
\]
Thus each incidence family has \(q^2(q+1)\) members. Over arbitrary \(K\), the parameter \(T\) ranges over \(\mathbb P^1_K\), and the allowed \(\ell\) form \(\mathbb P(J)\setminus\mathbb P(T)\cong\mathbb A^2_K\) on each fiber. Reading ranks off the displayed pairs yields the enumerator.

## Verification
The standalone `verify.py` independently enumerates all vector subspaces of the four-dimensional algebra in reduced row-echelon form over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). It tests subalgebra closure under all products of basis elements, enumerates all complementary ordered pairs, constructs each projection, and checks all 16 basis-pair Rota–Baxter identities and idempotence. It additionally exhausts the algebra automorphism parameters and verifies transitivity on the incidence family. All tests pass.

The verified rank distributions for \(q=2,3,5\) are respectively \((1,13,24,13,1)\), \((1,37,72,37,1)\), and \((1,151,300,151,1)\). The proof above, not these finite tests, establishes the formula for every field.

## Relationship to prior work
Shakoor and Noor's September 2026 study of four-dimensional real Grassmann Rota–Baxter operators treats the full operator equations by matrix families, but the inspected results do not provide finite-field rank distributions or conjugacy-orbit sizes for the idempotent projection locus. Benito, Gubarev and Pozhidaev's 2018 theorem shows that all nonzero-weight operators on the plane Grassmann algebra split in characteristic zero; that is a stronger splitting assertion in characteristic zero but does not classify the eight subalgebra-pair orbits over arbitrary fields or give their finite-field counts. Gubarev's wider characteristic-zero splitting theorem is likewise distinguished from the finite-field incidence count. An existing weight-zero census over \(\mathbb F_2\) studies a different Rota–Baxter identity and does not imply these weight-minus-one formulas.

## Limitations
Only *idempotent* weight-minus-one operators are classified over arbitrary fields. No assertion is made about general nonsplitting positive-characteristic operators, higher exterior ranks, or deformation spaces beyond the stated incidence strata. Literature coverage remains incomplete for some older full texts, and an equivalent finite-field orbit enumeration might exist under alternative terminology. Exhaustive computational checks cover the three indicated prime fields, not all finite fields.

## References
1. K. Shakoor and Noor-ul-Ain, *The Classification of the Rota-Baxter Operators on Four-dimensional Grassmann Algebra*, arXiv:2609.07377v1, publicly posted 2026-09-07.
2. P. Benito, V. Gubarev, and A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, Mediterranean Journal of Mathematics 15 (2018), article 189. DOI: 10.1007/s00009-018-1234-5 (see §4.4 and Theorem 4.9).
3. V. Gubarev, *Rota-Baxter operators on unital algebras*, arXiv:1805.00723 (2018); Moscow Mathematical Journal 21 (2021), 325–364.

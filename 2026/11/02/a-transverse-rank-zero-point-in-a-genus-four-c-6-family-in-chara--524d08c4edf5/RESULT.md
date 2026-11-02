# A transverse rank-zero point in a genus-four \(C_6\)-family in characteristic five

## Finding
Let \(k=\overline{\mathbb F}_5\). For \((a,b)\in k^2\), consider the smooth projective model of
\[
C_{a,b}:\quad y^2=x^{10}+x^7+ax^4+bx.
\]
Set
\[
\Delta=a^3+a^2-2ab-2b^2+b,\qquad
L=a^2+2b,\qquad
S=b^2(1+2a^5)+4(a^5+b^5).
\]
Define the smooth parameter space \(U=\{(a,b)\in\mathbb A_k^2:b\Delta\ne0\}\). Every curve in \(U\) has genus four. Its Jacobian \(5\)-rank \(f_5\) and \(a\)-number are **completely determined** by
\[
f_5(C_{a,b})=2\mathbf1_{S\ne0}+\mathbf1_{L\ne0},\qquad
a(C_{a,b})=\begin{cases}1,&L\ne0,\\2,&L=0.\end{cases}
\]
The loci \(V(S)\cap U\) and \(V(L)\cap U\) are nonempty smooth geometrically irreducible curves, and meet **transversely at exactly one point**:
\[
V(S,L)\cap U=\{(a,b)=(-1,2)\}.
\]
Thus the \(5\)-ranks \(3,2,1,0\) all occur, respectively, on the four disjoint strata determined by the nonvanishing or vanishing of \(L,S\). The \(5\)-rank-zero fiber is unique in this coefficient-marked two-parameter family; it has \(a\)-number two. No smooth member is ordinary or superspecial.

## Assumptions and scope
All parameter and geometric statements are over an algebraically closed field of characteristic five. The coefficients of the highest-degree, degree-seven, and degree-one monomials are fixed to one, and the assertion of a unique parameter does not assert uniqueness up to isomorphism among all genus-four curves. The \(5\)-rank is the dimension of the stable Frobenius image on \(H^1(C,\mathcal O_C)\), equivalently the Jacobian \(5\)-rank; the \(a\)-number is the dimension of the kernel of Cartier on \(H^0(C,\Omega^1_C)\). All identities below are in characteristic five.

Write \(f(x)=xg(x^3)\) with \(g(z)=z^3+z^2+az+b\). The root \(x=0\) of \(f\) is simple exactly when \(b\ne0\). For nonzero roots the derivative criterion reduces to separability of \(g\), because the characteristic differs from three. The discriminant of \(g\) is \(\Delta\) above. Therefore \(f\) is squarefree exactly on \(U\), and a degree-ten squarefree hyperelliptic model has genus four.

## Proof
**Cartier matrix.** The regular-differential basis is
\[
\omega_j=x^{j-1}dx/y,\quad 1\le j\le4.
\]
Write \(f^{(5-1)/2}=f^2=\sum c_mx^m\). Coefficient extraction gives the matrix \(M=(c_{5i-j})_{1\le i,j\le4}\), namely
\[
M=\begin{pmatrix}
0&0&b^2&0\\
0&a^2+2b&0&0\\
1+2a&0&0&2(a+b)\\
0&0&2&0
\end{pmatrix}.
\]
The Cartier map has actual \(5^{-1}\)-semilinear coefficients \(M^{(1/5)}\). The linearization of its twice-iterated action, after applying the inverse Frobenius scalar twist, is represented by \(M^{(5)}M\). Thus computing the stable rank requires Frobenius twists; the ordinary rank of \(M\) alone is not the \(5\)-rank.

**Stable Cartier image.** The coordinate line \(k\omega_2\) is Cartier-stable and contributes one stable dimension exactly when \(L\ne0\). Its complementary space is the three-dimensional block spanned by \(\omega_1,\omega_3,\omega_4\). In this block Cartier alternates between \(k\omega_3\) and \(\operatorname{span}(\omega_1,\omega_4)\). A twice-iterated Cartier operation on \(\omega_3\), raised to its twenty-fifth power to eliminate fractional coefficient exponents, has scalar
\[
S=(1+2a)^5b^2+\bigl(2(a+b)\bigr)^5\cdot2
=b^2(1+2a^5)+4(a^5+b^5).
\]
Since the map \(\omega_3\mapsto b^{2/5}\omega_1+2^{1/5}\omega_4\) is always nonzero, its three-dimensional block has stable dimension two if \(S\ne0\). If \(S=0\), three successive Cartier iterations annihilate the entire block (the successive twisted reverse scalar is \(S^5=0\)); its stable dimension is zero. This proves the claimed \(5\)-rank formula for every geometric parameter in \(U\).

**First Cartier rank.** The three-dimensional block has rank two unless \(1+2a=2(a+b)=0\). The latter equalities force \((a,b)=(2,3)\), which lies outside \(U\) because \(\Delta(2,3)=0\). Thus the first Cartier rank is \(2+\mathbf1_{L\ne0}\) on \(U\). Subtracting from genus four proves the \(a\)-number formula.

**Irreducibility of the rank-one curve.** Write
\[
S=(2b^2+4)a^5+(b^2+4b^5)=A(b)a^5+B(b).
\]
The two polynomials \(A,B\) are coprime in \(k[b]\): a common root would have \(b^2=3\) and \(b^3=1\), forcing \(b=2\), inconsistent with \(b^2=3\). Moreover,
\[
B'(b)A(b)-B(b)A'(b)=3b+4b^6\ne0.
\]
Consequently the rational function \(-B/A\) has nonzero derivative, hence is not a fifth power in \(k(b)\). The polynomial \(a^5+B/A\) is irreducible over \(k(b)\), and Gauss's lemma gives absolute irreducibility of \(S\) in \(k[a,b]\).

Its partial derivatives are \(S_a=0\) and \(S_b=2b(1+2a^5)\). On \(U\), a singular point of \(V(S)\) would have \(a=2\), and \(S=0\) would then force \(b=3\), where \(\Delta=0\). Thus \(V(S)\cap U\) is smooth. It is nonempty at \((a,b)=(0,1)\), where \(\Delta=4\) and \(L=2\).

**Unique transverse intersection.** The smooth curve \(V(L)\) is the graph \(b=2a^2\). Substituting in \(S\) and \(\Delta\) gives identities in \(\mathbb F_5[a]\):
\[
S(a,2a^2)=-2a^4(a+1)(a-2)^5,\qquad
\Delta(a,2a^2)=2a^2(a-2)^2.
\]
On \(U\), the first eliminates \(a=0,2\); hence \(S=L=0\) has only \(a=-1\), \(b=2\). At this point \(\Delta=3\), \(L_a=-2\ne0\), \(S_a=0\), and \(S_b=1\ne0\). The curves meet transversely. Nonemptiness of the rank-two stratum follows from \((a,b)=(1,2)\), and that of the rank-three stratum from \((a,b)=(0,2)\). As open subsets of two smooth irreducible curves, the rank-one and rank-two strata are geometrically irreducible.

## Verification
Two independently implemented standalone scripts accompany the result. Running `python verify_symbolic.py` (SymPy required) reconstructs the full coefficient matrix, verifies the twisted-square scalar, the cubic discriminant, the two restrictions along \(L=0\), the non-fifth-power derivative, and the four witness parameters. It prints `CHAR5_C6_SYMBOLIC_IDENTITIES_OK`.

Running `python verify_fields.py` (Python standard library only) directly convolves the coefficients of \(f^2\) and iterates Frobenius-twisted matrix products, independently over \(\mathbb F_5\) and \(\mathbb F_{25}\). It checks each resulting stable rank and first Cartier rank against the formula. The enumeration outcomes are:

| Base field | \(f_5=3,a=1\) | \(f_5=2,a=2\) | \(f_5=1,a=1\) | \(f_5=0,a=2\) | Singular models |
|---|---:|---:|---:|---:|---:|
| \(\mathbb F_5\) | 12 | 2 | 2 | 1 | 8 |
| \(\mathbb F_{25}\) | 534 | 22 | 20 | 1 | 48 |

Both completed successfully. The infinite geometric statement follows from the symbolic and algebraic argument, **not** the finite-field enumeration.

## Relationship to prior work
Kudo, Nakagawa, and Takagi's 2022 preprint (arXiv:2210.14822; subsequently published in 2023) studies precisely the genus-four family \(y^2=x^{10}+x^7+ax^4+bx\), emphasizing superspecial enumeration for primes at least seven and the automorphism classification; its Lemma 2.2.2 gives the standard coefficient extraction method. The present result specializes to characteristic five and determines all stable Frobenius ranks and the scheme geometry of their parameter strata, neither stated nor implied by its superspecial-enumeration results. The normal-form comparison is direct, not merely a similar title.

Sohn's 2025 article on genus-four superelliptic \(a\)-numbers is also relevant to the first Cartier-rank part of this theorem; only its abstract and bibliographic record were accessible, so its exact overlap with that auxiliary formula is unresolved. The central stable \(5\)-rank equations and transverse coefficient-space geometry do not follow from the available description.

Ohashi and Kudo's 2023 preprint (arXiv:2312.16858) treats superspecial genus-four hyperelliptic curves with larger Klein-four symmetry and records the characteristic-five superspecial background; it supplies neither these rank-one and rank-zero equations nor the unique transverse parameter. Achter, Glass, and Pries' *Curves of given p-rank with trivial automorphism group* (arXiv:0708.2199) proves general existence and stratum-dimension results in moduli; such results do not determine exact incidence of this coefficient slice with the strata.

## Limitations
The classification concerns this normalized coefficient family, not all genus-four hyperelliptic curves, all curves with automorphism group containing \(C_6\), or full isomorphism classes. A coefficient-marked unique point may have alternative models in other normalizations. Newton polygons, endomorphism algebras, and deeper Ekedahl–Oort types are not determined. The originality assessment is literature-based, not a proof that no unpublished equivalent calculation exists. Independent external mathematical validation has not been performed.

## References
1. M. Kudo, T. Nakagawa, and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing \(\mathbb Z_6\)*, arXiv:2210.14822, first publicly submitted 26 October 2022. https://arxiv.org/html/2210.14822v1
2. R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858, first publicly submitted 28 December 2023. https://arxiv.org/abs/2312.16858
3. J. Achter, D. Glass, and R. Pries, *Curves of given p-rank with trivial automorphism group*, arXiv:0708.2199 (2007). https://arxiv.org/html/0708.2199v1
4. G. Sohn, *The a-number of superelliptic curves of genus four*, Journal of Applied and Pure Mathematics 7 (2025), 59–66, doi:10.23091/japm.2025.059. https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003184347

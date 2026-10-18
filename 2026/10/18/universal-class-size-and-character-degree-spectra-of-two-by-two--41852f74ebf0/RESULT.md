# Universal class-size and character-degree spectra of two-by-two Borel groups over finite chain rings

## Finding
Let \(R\) be a finite commutative chain ring of length \(m\ge2\), with residue field of cardinality \(q\), maximal ideal \(\mathfrak m=(\pi)\), and unit-group order \(U=(q-1)q^{m-1}\). Let \(B=B_2(R)\) be the group of invertible upper-triangular \(2\times2\) matrices. Write \(w_j=(q-1)q^{m-j-1}\) for \(0\le j<m\), and put
\[
v_0=(q-2)q^{m-1},\qquad v_j=w_j\ (1\le j<m),\qquad v_m=1.
\]
The following are complete **multiset formulas**; when two displayed sizes coincide, their multiplicities are added.

**Conjugacy-class sizes.** For each \(0\le j\le m\) there are exactly \(Uv_j\) conjugacy classes of size \(q^{m-j}\). For each \(0\le j<m\) there are additionally exactly \(Uq^{m-j-1}\) classes of size \(w_j\). The first family has no \(j=0\) contribution when \(q=2\).

**Complex irreducible character degrees.** There are \(U^2\) irreducible characters of degree \(1\); for each \(0\le j<m\) there are additionally \(Uq^j\) irreducible characters of degree \(w_j\). Again, coincident degrees are aggregated, including the degree-one layer for \(q=2\).

Consequently,
\[
k(B)=U^2+q^{m-1}(q^m-1),\quad |B|=U^2q^m,\quad
\operatorname{cp}(B)=\frac{U^2+q^{m-1}(q^m-1)}{U^2q^m}.
\]
The complex group algebra and both full distributions therefore depend only on \((q,m)\), **not** on the isomorphism type or characteristic of the ring. The group center has size \(U\) when \(q>2\), and \(2U\) when \(q=2\). In particular, for \(m=3,q=2\) the conjugacy-class sizes are \(1,2,4\), with respective class multiplicities \(8,12,24\); the irreducible character degrees are \(1,2,4\), with multiplicities \(32,8,4\).

## Assumptions and scope
A chain ring is a finite commutative local principal ideal ring whose ideals form \(R\supset(\pi)\supset\cdots\supset(\pi^{m-1})\supset(\pi^m)=0\). The quotient \(R/(\pi)\) is a field of size \(q\). Define the truncated valuation \(\nu(0)=m\), and for nonzero \(a\in R\), \(\nu(a)=j\) when \(a\in(\pi^j)\setminus(\pi^{j+1})\). The claims concern conjugacy *inside* \(B_2(R)\) and ordinary complex irreducible representations of that finite group, not conjugacy in the ambient general linear group. All statements are valid for every prime-power residue cardinality and every ring of the stated type, including characteristic two.

## Proof
**1. An affine splitting.** Every element has a unique representation
\[
\begin{pmatrix}dt&du\\0&d\end{pmatrix},\qquad d,t\in R^\times,\ u\in R.
\]
Matrix multiplication sends \((d,t,u)\) and \((d',t',u')\) to \((dd',tt',u+tu')\). Hence
\[
B_2(R)\cong R^\times\times\bigl(R_{\rm add}\rtimes R^\times\bigr),
\]
where units act on the additive group by multiplication. Denote the second factor by \(H\), of order \(Uq^m\). Two elements \((t,u),(t',u')\in H\) commute precisely when
\[
(t-1)u'=(t'-1)u. \tag{1}
\]

**2. Centralizer-size dichotomy.** Fix \((t,u)\in H\) and put \(\alpha=\nu(t-1)\), \(\beta=\nu(u)\). Write \(s=t'-1\), so that \(t'\) is a unit exactly when \(s\not\equiv-1\pmod\pi\). With this restriction temporarily removed, the \(R\)-linear map
\[
(s,z)\longmapsto (t-1)z-us
\]
from \(R^2\) onto the ideal \((\pi^{\min(\alpha,\beta)})\) has kernel of cardinality \(q^{m+\min(\alpha,\beta)}\). If \(\beta<\alpha\), no solution has \(s\equiv-1\pmod\pi\), since that would make \(us\) have valuation \(\beta\) while \((t-1)z\) has valuation at least \(\alpha\). If \(\beta\ge\alpha\), each of the \(q^{m-1}\) forbidden values of \(s\) admits exactly \(q^\alpha\) solutions for \(z\). Subtracting them gives
\[
|C_H(t,u)|=\begin{cases}
Uq^\alpha,&\beta\ge\alpha,\\
q^{m+\beta},&\beta<\alpha.
\end{cases}
\]
Because \(|H|=Uq^m\), the two respective class sizes are \(q^{m-\alpha}\) and \(w_\beta\). Central scalar factors multiply centralizers by \(U\) and do not alter conjugacy-class sizes in \(B\).

**3. Class multiplicities.** The number of units \(t\) with \(\nu(t-1)=j\) is \(v_j\) for \(0\le j\le m\): for \(j=0\), the nonunit residue \(-1\) must be excluded from \(t-1\). For fixed \(\alpha=j\), exactly \(q^{m-j}\) translations \(u\) satisfy \(\beta\ge\alpha\). Thus the first family contains \(v_jq^{m-j}\) elements in \(H\), divided into \(v_j\) classes of size \(q^{m-j}\). For fixed \(\beta=j<m\), exactly \(q^{m-j-1}\) units \(t\) satisfy \(\alpha>\beta\), and \(w_j\) translations have valuation \(j\). Hence the second family contains \(q^{m-j-1}w_j\) elements of \(H\), divided into \(q^{m-j-1}\) classes of size \(w_j\). Multiplication by the scalar-center factor \(R^\times\) supplies \(U\) copies of each class, proving the two full class-size formulas. Summation uses \(\sum_{j=0}^m v_j=U\) and \(U\sum_{j=0}^{m-1}q^{m-j-1}=q^{m-1}(q^m-1)\).

**4. Character degrees.** The additive group \(R\) has a character \(\psi:R\to\mathbb C^\times\) nontrivial on its socle \((\pi^{m-1})\): first choose a nontrivial socle character and extend it to \(R\) (every character of a subgroup of a finite abelian group extends). Every nonzero ideal contains the socle, so \(c\mapsto[x\mapsto\psi(cx)]\) is an injective map \(R\to\widehat{R_{\rm add}}\); equality of cardinalities makes it bijective. The \(R^\times\)-action on the additive dual therefore coincides with multiplication on \(R\). The zero character has orbit size one and stabilizer \(R^\times\). For each \(j<m\), the \(w_j\) elements of valuation \(j\) form exactly one unit orbit; its stabilizer is \(1+(\pi^{m-j})\), of order \(q^j\). Clifford's little-group construction applies to the abelian normal subgroup \(R_{\rm add}\): an invariant additive character extends to its stabilizer semidirect product by acting trivially on the unit stabilizer, each character of the abelian stabilizer gives a distinct induced irreducible, and its degree is the orbit size. Hence \(H\) has \(U\) linear characters and, for each \(j<m\), precisely \(q^j\) irreducibles of degree \(w_j\). Every complex irreducible of the direct product \(R^\times\times H\) is a tensor product with one of the \(U\) linear characters of \(R^\times\). This proves the degree distribution. Independently, the squared-degree sum is \(U^2+U\sum_{j<m}q^jw_j^2=U^2q^m=|B|\), checking exhaustion.

**5. Center and isomorphism consequences.** An affine element \((t,u)\) commutes with all translations only if \(t=1\). Such an element commutes with all units precisely when \((v-1)u=0\) for every \(v\in R^\times\). If \(q>2\), some \(v-1\) is a unit, so \(u=0\). If \(q=2\), the ideal generated by these differences is \((\pi)\), whose annihilator is the socle of cardinality two; multiplying by the central \(R^\times\) factor proves the claimed center orders. Finally the irreducible-degree multiset determines the Wedderburn decomposition of the semisimple algebra \(\mathbb C[B]\), so complex group algebras of all chain rings with the same \((q,m)\) are (noncanonically) isomorphic.

## Verification
The standalone standard-Python program `verify_borel_chain.py` constructs the affine group law via explicit upper-triangular matrices over residue rings and truncated polynomial rings. It independently counts every group element's centralizer and conjugacy-class size, compares full class-size multiplicities with the formulas, and enumerates additive-character orbits via the unit action to check the degree spectrum and squared-degree sum. Its finite tests include nonisomorphic ring models with identical \((q,m)\). They test examples only and do not constitute an all-ring proof; the preceding argument supplies that proof.

## Relationship to prior work
P. Singla's 2010 treatment of complex representations of full general linear groups over principal ideal local rings of length two proves residue-field independence for those ambient groups, rather than the present all-length internal Borel conjugacy-class spectrum. Prasad–Singla–Spallone (2012) analyze **ambient** similarity classes and centralizers in matrix rings of length two, which do not by themselves determine conjugacy under the Borel subgroup. Gupta–Singla (2024) prove a strong Gelfand-pair theorem for \((\operatorname{GL}_2(R),B_2(R))\) and explicitly discuss unit orbits on additive characters; that orbit statement is antecedent to the character-degree portion above. Fulman–Guralnick (2021) enumerate conjugacy classes for classical affine groups of **vector spaces over finite fields**, not affine groups of nonreduced finite chain rings. None of the inspected works states the full two-family Borel class-size distribution over chain rings of arbitrary length. The affine semidirect decomposition and classical Clifford theory are standard and are not claimed as new. No bibliographic uniqueness claim is made; previously published specialized classifications of affine groups over finite chain rings could subsume the result.

## Limitations
These formulas concern only invertible upper-triangular matrices of order two over **commutative chain rings**, not arbitrary finite local rings, higher matrix orders, conjugacy within \(\operatorname{GL}_2(R)\), or individual character values. The representation-degree formula follows from standard Clifford-theoretic orbit techniques; the distinct assessed contribution is the complete two-family Borel conjugacy-class-size distribution and its simultaneous ring-independent comparison with the character-degree distribution. Independent peer verification and exhaustive historical-literature screening have not been performed.

## References
1. P. Singla, *On Representations of General Linear Groups over Principal Ideal Local Rings of Length Two*, arXiv:1001.5304 (first submitted 2010-01-29), https://arxiv.org/abs/1001.5304.
2. A. Prasad, P. Singla and S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157 (first submitted 2012-12-26), https://arxiv.org/abs/1212.6157.
3. A. Gupta and P. Singla, *On Gelfand pairs and degenerate Gelfand-Graev modules of General Linear groups of degree two over principal ideal local rings of finite length*, arXiv:2410.21761 (first submitted 2024-10-29), https://arxiv.org/abs/2410.21761.
4. J. Fulman and R. Guralnick, *Enumeration of conjugacy classes in affine groups*, arXiv:2112.15219 (first submitted 2021-12-30), https://arxiv.org/abs/2112.15219.

# The first modular rank gap in one-generated Zinbiel algebras

## Finding

Let \(k\) be **any** field of characteristic \(p>0\), and let \(2\le n\le p+1\). The truncated, nonunital, one-generator Zinbiel algebra \(Z_n(k)\) has basis \(e_1,\ldots,e_n\) and product
\[
e_i\circ e_j=\begin{cases}\binom{i+j-1}{j}e_{i+j},&i+j\le n,\\0,&i+j>n.\end{cases}
\]
For \(a\in Z_n(k)\), write \(L_a(b)=a\circ b\), \(R_a(b)=b\circ a\), and let \(d(a)\) be the least \(i\) with nonzero coefficient of \(e_i\), setting \(d(0)=n\). Write \(J_s\) for one nilpotent Jordan block of size \(s\), with \(J_s^h\) its \(h\)-th power.

**Complete joint Jordan-type classification.** If \(n\le p\), then both \(L_a\) and \(R_a\) have Jordan type \(J_n^{d(a)}\), for every \(a\). At the first modular dimension \(n=p+1\), their Jordan types are as follows:

| First nonzero degree | Jordan type of \(L_a\) | Jordan type of \(R_a\) |
| --- | --- | --- |
| \(d=1\) | \(J_{p+1}\) | \(J_p\oplus J_1\) |
| \(2\le d\le p-1\) | \(J_p^d\oplus J_1\) | \(J_p^d\oplus J_1\) |
| \(d=p\) | \(J_1^{\oplus(p+1)}\) | \(J_2\oplus J_1^{\oplus(p-1)}\) |
| \(d=p+1\) (including zero) | \(J_1^{\oplus(p+1)}\) | \(J_1^{\oplus(p+1)}\) |

The middle interval is empty for \(p=2\). Every Jordan block in this statement is nilpotent, so its type is defined over the ground field, without algebraic closure.

**Exact finite-field census.** Put \(k=\mathbb F_q\), with \(q\) a power of \(p\), and define
\[
\Phi_n(u,v)=\sum_{a\in Z_n(\mathbb F_q)}u^{\operatorname{rank}L_a}v^{\operatorname{rank}R_a}.
\]
Then, for \(2\le n\le p\),
\[
\Phi_n(u,v)=q+(q-1)\sum_{r=1}^{n-1}q^r(uv)^r,
\]
whereas at \(n=p+1\),
\[
\boxed{\Phi_{p+1}(u,v)=q+(q-1)qv+(q-1)\sum_{r=1}^{p-2}q^{r+1}(uv)^r+(q-1)q^p u^p v^{p-1}.}
\]
In particular, the attainable left ranks are exactly \(0,1,\ldots,p-2,p\): rank \(p-1\) is **impossible**. The attainable right ranks are exactly \(0,1,\ldots,p-1\). The left and right annihilators have dimensions two and one, respectively, at \(n=p+1\), compared with dimension one on both sides for \(n\le p\).

The joint rank strata, and hence the joint Jordan strata, are explicitly coordinate-flag strata. At \(n=p+1\), the \((p,p-1)\)-stratum is \(\{a_1\ne0\}\cong\mathbb G_m\times\mathbb A^p\); the \((r,r)\)-stratum for \(1\le r\le p-2\) is \(\{a_1=\cdots=a_{p-r-1}=0,\ a_{p-r}\ne0\}\cong\mathbb G_m\times\mathbb A^{r+1}\); the \((0,1)\)-stratum is \(\{a_1=\cdots=a_{p-1}=0,\ a_p\ne0\}\cong\mathbb G_m\times\mathbb A^1\); and the \((0,0)\)-stratum is \(\{a_1=\cdots=a_p=0\}\cong\mathbb A^1\). Their closures are nested coordinate linear spaces. All assertions are valid over arbitrary fields of characteristic \(p\), with point formulas over finite fields.

## Assumptions and scope

The multiplication table specifies a quotient of the free one-generated Zinbiel algebra by words of length greater than \(n\); no characteristic-zero classification theorem is assumed over positive characteristic. The product identity holds integrally by the binomial shuffle identity, hence after reduction modulo every prime. The main classification concerns all \(a\), not just generic generators, and both handed multiplication operators rather than derivations. It is limited to \(2\le n\le p+1\); no claim about later modular dimensions is made.

## Proof

**Step 1: the multiplication and its triangular filtration.** The Zinbiel identity \((x\circ y)\circ z=x\circ(y\circ z)+x\circ(z\circ y)\) follows on basis vectors from the integer equality
\[
\binom{i+j-1}{j}\binom{i+j+k-1}{k}=
\left(\binom{j+k-1}{k}+\binom{j+k-1}{j}\right)\binom{i+j+k-1}{j+k}.
\]
All products increase the basis index strictly. Let \(a=\sum_{i=1}^n a_i e_i\). If \(d=d(a)<n\), then for each input \(e_j\), the lowest potentially nonzero output of \(L_a(e_j)\) is at degree \(d+j\), with coefficient \(a_d\binom{d+j-1}{j}\); for \(R_a(e_j)\) it is \(a_d\binom{d+j-1}{d}\). Terms of larger index cannot cancel these leading coefficients.

**Step 2: before the modular boundary.** Suppose \(n\le p\). For all \(d+j\le n\), both binomial coefficients just displayed are units in \(k\), because their upper index is strictly less than \(p\). Applying either multiplication operator \(h\) times raises the least possible degree by \(hd\). The coefficient of \(e_{j+hd}\) in the image of \(e_j\) is a product of nonzero leading coefficients whenever \(j+hd\le n\). Thus the first \(\max(n-hd,0)\) admissible columns have distinct nonzero leading pivots, while every image is contained in the space spanned by \(e_{hd+1},\ldots,e_n\). For every \(h\ge1\),
\[
\operatorname{rank}L_a^h=\operatorname{rank}R_a^h=\max(n-hd,0).
\]
These power ranks uniquely specify the nilpotent Jordan partition of \(J_n^d\). When \(d=n\), both operators are zero and the same formula holds.

**Step 3: the unique surviving product in the first modular top degree.** Let \(n=p+1\). For \(i+j=p+1\), the structure coefficient is \(\binom p j\), zero modulo \(p\) unless \(j=p\). Consequently the only basis product with output \(e_{p+1}\) is
\[
e_1\circ e_p=e_{p+1}.
\]
For all outputs \(e_s\) with \(s\le p\), the corresponding structure coefficients are nonzero for every decomposition \(s=i+j\) into positive indices.

If \(d=1\), left multiplication has a nonzero first superdiagonal all the way from \(e_1\) to \(e_{p+1}\). Its \(h\)-th power has rank \(\max(p+1-h,0)\), hence type \(J_{p+1}\). Right multiplication instead has nonzero first superdiagonal only through output \(e_p\): \(R_a(e_p)=0\), since \(e_p\circ e_1=pe_{p+1}=0\). There may be an additional \(e_{p+1}\)-term in \(R_a(e_1)\), arising from \(a_p\), but this does not create a new independent column or affect the leading pivots of any positive power. Indeed, only input columns \(e_1,\ldots,e_{p-1}\) can be nonzero, their leading terms are linearly independent, and after the first application no \(e_1\) input can occur again. Thus \(\operatorname{rank}R_a^h=\max(p-h,0)\) for \(h\ge1\), which is the power-rank sequence of \(J_p\oplus J_1\).

Now let \(2\le d\le p-1\). Left multiplication has no \(e_{p+1}\) output at all; it maps the first \(p-d\) input columns with distinct nonzero leading pivots into \(\langle e_{d+1},\ldots,e_p\rangle\), and all later columns to zero. Right multiplication may have an extra \(e_{p+1}\)-term, but only in the first input column (from the \(e_p\)-coefficient of \(a\)); its only potentially nonzero columns are again the first \(p-d\), and they retain independent leading pivots. After one application the degree is greater than one, so the possible top-degree term never appears on later iterations. The same leading-pivot argument therefore gives, for either hand and every \(h\ge1\),
\[
\operatorname{rank}L_a^h=\operatorname{rank}R_a^h=\max(p-hd,0).
\]
Hence the joint type is \(J_p^d\oplus J_1\). If \(d=p\), only the coefficient \(a_p\) can act: \(L_a=0\) while \(R_a(e_1)=a_p e_{p+1}\) and all other columns vanish. If \(d=p+1\), both operators vanish. This proves the Jordan table, including \(p=2\).

**Step 4: exact strata and counts.** For \(1\le d<n\), the vectors with first nonzero index \(d\) have \(a_d\in k^\times\) and \(n-d\) unrestricted later coordinates. Over \(\mathbb F_q\) there are \((q-1)q^{n-d}\) such vectors. The remaining vectors have only the last coordinate possibly nonzero, numbering \(q\). Substituting the proven ranks by cases gives both displayed polynomials. At \(n=p+1\), the nonzero left ranks are \(p\) and \(p-d\) for \(2\le d\le p-1\), establishing the missing value \(p-1\). The right ranks are \(p-1\), \(p-d\) for these intermediate degrees, and one for \(d=p\). The stratum equations follow from the first nonzero coordinate condition; their closures are the corresponding coordinate flags.

**Step 5: annihilators.** For \(n\le p\), an element annihilating every element on either side must have vanishing coefficients through \(e_{n-1}\), since its first nonzero coefficient produces a nonzero product with \(e_1\). Thus each annihilator is \(\langle e_n\rangle\). At \(n=p+1\), the unique top-degree product above gives the left annihilator \(\langle e_p,e_{p+1}\rangle\) and the right annihilator \(\langle e_{p+1}\rangle\). This proves the sharpness of the first modular boundary.

## Verification

The accompanying standalone Python checker constructs each structure coefficient directly from the binomial table over prime and extension fields, independently computes the matrices of \(L_a\) and \(R_a\), and obtains Jordan type from ranks of **every positive power**. It exhaustively checks 11 field/dimension configurations and tests 3 further configurations with reproducible pseudorandom samples. The exhaustive tests include \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_9\) using polynomial-extension arithmetic, plus \(\mathbb F_5\) in the dimension-six modular case. All 14 configurations passed. The checker also evaluates the integer Zinbiel identity in each tested dimension.

For \(p=q=5\) and \(n=6\), the observed joint rank multiplicities are \(5\) for \((0,0)\), \(20\) for \((0,1)\), \(100\) for \((1,1)\), \(500\) for \((2,2)\), \(2500\) for \((3,3)\), and \(12500\) for \((5,4)\), totalling \(5^6\). Finite tests corroborate but are not used as an infinite-family proof. Run `python zinbiel_joint_census_check.py` to reproduce.

## Relationship to prior work

Adashev, Omirov and Khudoyberdiyev's 2007 preprint **already provides** the binomial multiplication table for the complex null-filiform Zinbiel algebra, in Theorem 2.1. That multiplication table is foundational prior work and is not claimed as new. Its theorem is an isomorphism classification over complex scalars and does not state the complete positive-characteristic left/right Jordan census, the first modular rank gap, or the finite-field joint multiplicity polynomial.

Adashev, Camacho, Gómez-Vidal and Karimjanov (2013) study characteristic sequences and the complex graded nilindex \(n-3\) family, while Adashev, Ladra and Omirov (2014) classify another complex graded family with two Jordan blocks. Those are different classification statements; neither gives this all-element modular joint census. The documented free-Zinbiel shuffle model supplies the same integral structure constants but not the claimed finite-field stratification. Unlike these antecedents, this result fixes the first dimension where the prime characteristic divides a top-degree binomial coefficient and compares the Jordan types of **both** multiplication hands for every element, including the radical and annihilator strata.

Turemuratova (2026) explicitly observes the unequal left/right annihilator behavior in a **three-dimensional characteristic-two example**, exactly the smallest modular boundary case considered here. That **special-case observation is prior work and is not claimed as new**. Its paper classifies two-dimensional products over selected finite fields; it does not present the whole positive-characteristic first-boundary Jordan and rank census. Alvarez, Fehlberg Júnior and Kaygorodov (2022) classify complex five-dimensional Zinbiel algebras and their degenerations, not positive-characteristic joint multiplication distributions.

This comparison does not assert that no undocumented equivalent or easily transformed rank formula exists. Publication-priority verification is not independent.

## Limitations

The theorem does not classify arbitrary Zinbiel algebras, all null-filiform Zinbiel algebras in positive characteristic, or multiplication spectra at dimensions above \(p+1\). The result concerns labelled elements, not orbits of the automorphism group. The geometric claim is about the explicit reduced set-theoretic rank strata; no scheme-theoretic reducedness of determinantal rank conditions is asserted. All publication-priority comparisons remain provisional pending independent review.

## References

1. J. Q. Adashev, B. A. Omirov and A. Kh. Khudoyberdiyev, *Classifications of some classes of Zinbiel algebras*, arXiv:math/0702809v1 (first submitted 2007-02-27), especially Theorem 2.1, https://arxiv.org/abs/math/0702809 .
2. J. Q. Adashev, L. M. Camacho, S. Gómez-Vidal and I. A. Karimjanov, *Naturally graded Zinbiel algebras with nilindex \(n-3\)*, arXiv:1303.5881v1 (2013-03-23), https://arxiv.org/abs/1303.5881 .
3. J. K. Adashev, M. Ladra and B. A. Omirov, *The classification of naturally graded Zinbiel algebras with characteristic sequence equal to \((n-p,p)\)*, arXiv:1410.7549v1 (2014-10-28), https://arxiv.org/abs/1410.7549 . In this title \(p\) denotes a **block-size parameter**, not the field characteristic.
4. SageMath Reference Manual, *Free Zinbiel Algebras*, documentation of the integral shuffle/divided-power multiplication, https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/free_zinbiel_algebra.html .
5. B. M. Turemuratova, *Description of Zinbiel algebras over finite fields*, ICSEL 2(10) (2026), pp. 154–159, published 2026-10-15, especially Section 4.4 and Table 5, https://uniconflix.com/index.php/ICSEL/en/article/download/6750/3837/8017 .
6. M. A. Alvarez, R. Fehlberg Júnior and I. Kaygorodov, *The algebraic and geometric classification of Zinbiel algebras*, arXiv:2206.00315v1 (2022), https://arxiv.org/abs/2206.00315 .

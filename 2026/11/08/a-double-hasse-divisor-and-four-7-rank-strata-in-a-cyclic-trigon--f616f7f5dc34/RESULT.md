# A double Hasse divisor and four \(7\)-rank strata in a cyclic-trigonal genus-four family

## Finding

Let \(k=\overline{\mathbb F}_7\). For every triple \((a,b,c)\in k^3\), put
\[
f_{a,b,c}(x)=x^5+a x^2+b x+c,
\qquad C_{a,b,c}:y^3=f_{a,b,c}(x),
\]
where \(C_{a,b,c}\) means the unique smooth projective model of the displayed affine equation. Define
\[
\Delta(a,b,c)=3a^5c+a^4b^2+3a^2bc^2+3ab^3c-3b^5+3c^4.
\]
The polynomial \(f_{a,b,c}\) is squarefree if and only if \(\Delta\ne0\), and precisely those parameters give a smooth genus-four cyclic triple cover with six distinct branch points.

In the dual of the differential basis specified below, the Hasse–Witt determinant is **exactly**
\[
\boxed{\det H=4b^2\Delta.}
\]
For every parameter with \(\Delta\ne0\), the geometric Jacobian \(7\)-rank \(f_7\) and Cartier \(a\)-number are **completely determined** by
\[
\boxed{
(f_7,a(C_{a,b,c}))=
\begin{cases}
(4,0),&b\ne0,\\
(0,2),&b=0,\ a=0,\\
(1,2),&b=0,\ a^5=c^3,\\
(2,2),&b=0,\ a\ne0,\ a^5\ne c^3.
\end{cases}}
\]
The cases do not overlap on the smooth base: when \(b=0\), smoothness forces \(c\ne0\) and \(a^5\ne-c^3\). In particular, \(7\)-rank three never occurs. The reduced nonordinary locus of this natural three-coefficient family is the smooth-base portion of \(b=0\), and the determinant vanishes there to order two, not one.

On the normalized chart \(c=1\), the rank-one locus consists of the five solutions of \(a^5=1\), which are mutually isomorphic under \(x\mapsto\zeta x\) for \(\zeta^5=1\). The unique rank-zero coefficient parameter on that chart is \((a,b)=(0,0)\). The counts concern coefficient parameters and do not classify all genus-four curves up to isomorphism.

## Assumptions and scope

All geometric rank statements are over the algebraic closure of the seven-element field. The base is the open subscheme \(U=\operatorname{Spec}k[a,b,c,\Delta^{-1}]\), not the complete moduli space of cyclic-trigonal genus-four curves. The polynomial has degree five in \(x\); the cover has degree three because the characteristic is prime to three. A smooth model exists and is geometrically integral because the divisor of \(f\) has valuation one at each simple root, so \(f\) is not a cube in \(k(x)\).

For \(\Delta\ne0\), the map \(x:C\to\mathbb P^1\) has degree three and is totally ramified at the five simple roots and at infinity. Riemann–Hurwitz gives \(2g-2=3(-2)+6(3-1)=6\), hence \(g=4\).

The \(a\)-number is \(\dim_k\ker\mathcal C\), where \(\mathcal C\) is the Cartier operator on regular differentials. The geometric \(7\)-rank is the eventual rank of its semilinear iterates, not the rank of its first matrix. No Newton polygon beyond its slope-zero multiplicity, no global isomorphism classification, and no information about curves outside this family is asserted.

## Proof

**Step 1: a regular-differential basis and coefficient extraction.** For \(j\in\{1,2\}\) and \(i\ge0\), the differential \(x^i\,dx/y^j\) has order \(5j-3i-4\) at the unique point over infinity. The four holomorphic differentials
\[
\omega_0=\frac{dx}{y},\qquad
\omega_1=\frac{dx}{y^2},\qquad
\omega_2=\frac{x\,dx}{y^2},\qquad
\omega_3=\frac{x^2\,dx}{y^2}
\]
are linearly independent and constitute a basis by the genus calculation. They are regular at finite branch points as well, using a local parameter \(y\).

For \(j\in\{1,2\}\), write \(m=2j\), so \(3m= j(7-1)\). Then
\[
\frac{x^i dx}{y^j}=\frac{x^if(x)^m dx}{(y^j)^7}.
\]
Cartier extraction retains only powers of \(x\) congruent to \(6\pmod 7\). Thus the seventh powers of the coefficients of the Cartier operator are obtained from \([x^{7(r+1)-1-i}]f(x)^m\), where \(r\) indexes an output basis vector. The \(j=1\) part is one-dimensional with coefficient \(2b\); the \(j=2\) part has coefficient matrix
\[
B=\begin{pmatrix}
-3a^3c-a^2b^2-2bc^2&-2a^2bc-3ab^3-3c^3&-a^2c^2-2ab^2c+b^4\\
-2ab&-2ac-b^2&-3a^3-2bc\\
1&0&0
\end{pmatrix}.
\]
More precisely, if \(\mathcal C(v)=Q v^{(1/7)}\) in column coordinates, then \(Q^{(7)}=\operatorname{diag}(2b,B)\). By Cartier–Hasse–Witt adjunction, the dual Hasse–Witt matrix is \(H=(Q^{(7)})^{\mathsf T}\). Direct expansion gives
\[
\det B=2b\Delta,
\qquad\det H=(2b)\det B=4b^2\Delta.
\]
The independent discriminant calculation \(\operatorname{Disc}_x(f)=\Delta\) is an exact polynomial identity in \(\mathbb F_7[a,b,c]\); it is not inferred from sample points.

**Step 2: the first Cartier rank and \(a\)-numbers.** If \(\Delta\ne0\) and \(b\ne0\), then \(H\) is invertible; the Jacobian is ordinary, with \((f_7,a)=(4,0)\). On \(b=0\) the determinant vanishes. There \(\Delta=3c(a^5+c^3)\), so a smooth parameter has \(c\ne0\). The block \(B\) has determinant zero and the minor using rows \(0,2\), columns \(0,1\), equals \(3c^3\ne0\). Therefore \(\operatorname{rank}\mathcal C=2\) for every smooth \(b=0\) fiber and its Cartier \(a\)-number is exactly \(4-2=2\). In particular there are no \(a\)-numbers one, three, or four in this family.

**Step 3: normalized semilinear Frobenius.** For \(b=0\), choose \(\xi,\eta\in k^\times\) with \(\xi^5=c\) and \(\eta^3=c\); setting \(x=\xi u\), \(y=\eta v\) gives
\[
 v^3=u^5+A u^2+1,\qquad A=a\xi^2/c,
 \qquad A^5=a^5/c^3.
\]
The one-dimensional Cartier block is zero. The other block, in the normalized basis and after taking seventh powers, is
\[
M(A)=\begin{pmatrix}
-3A^3&-3&-A^2\\
0&-2A&-3A^3\\
1&0&0
\end{pmatrix}.
\]
Let \(M^{(7^r)}\) mean raising its coefficients to their \(7^r\)-th powers. Since Cartier is inverse-Frobenius-semilinear, the rank of its \(n\)-th iterate on this three-dimensional block equals the rank of
\[
P_n=M^{(7^{n-1})}\cdots M^{(7)}M.
\]
The first matrix has rank two for every \(A\), as seen from its nonzero constant minor and zero determinant. Exact polynomial arithmetic in \(\mathbb F_7[A]\) gives
\[
\gcd\{\text{all }2\times2\text{ minors of }P_2\}=A^4(A^{10}-1),
\qquad (P_2)_{2,1}=-3,
\]
with indices beginning at zero. In particular, the minor using rows \(0,2\) and columns \(0,1\) is \(3A^4(A^{10}-1)\), and all other minors vanish when that polynomial does. Thus \(P_2\) has rank two precisely when \(A\ne0\) and \(A^{10}\ne1\); otherwise it has rank one.

An exact third-iterate computation further gives
\[
\gcd\{\text{nine entries of }P_3\}=A.
\]
At \(A=0\), the matrix \(M(0)\) is nilpotent of index three, hence \(P_3=0\). At every \(A\) with \(A^5=1\), one has \((P_3)_{1,0}=1\) upon reduction modulo \(A^5-1\); hence \(P_3\) has rank one. If \(A^{10}=1\) but \(A^5\ne1\), then \(A^5=-1\), and the curve is singular since \(\Delta=3c^4(A^5+1)\). These are all rank drops, because the ranks of successive semilinear iterates form a nonincreasing sequence that stabilizes once two consecutive ranks agree.

Consequently, for smooth \(b=0\) curves the eventual ranks are \(0\) at \(A=0\), \(1\) at \(A^5=1\), and \(2\) everywhere else. Translating through \(A^5=a^5/c^3\) proves the displayed classification.

**Step 4: geometric symmetry and finite-field check.** For \(c=1\) and \(b=0\), an element \(\zeta\) with \(\zeta^5=1\) induces an isomorphism between the parameter \(a\) and \(a\zeta^2\) by rescaling \(x\). The five roots of \(a^5=1\) therefore form one scaling orbit. Direct polynomial-gcd enumeration on the \(c=1\) chart over \(\mathbb F_7\) yields 44 smooth parameter pairs: 38 ordinary, four of rank two, one of rank one, and one of rank zero. Over \(\mathbb F_{49}\) the corresponding counts are 2306, 46, one, and one, respectively, among 2354 smooth parameter pairs. These finite checks corroborate but are not the proof of the statements over \(k\).

## Verification

The package contains executable independent checks:

* `verify_cartier.py` (SymPy) derives all necessary coefficients by multinomial enumeration, independently cross-checks by polynomial expansion, computes the discriminant, and verifies \(\det H=4b^2\Delta\) as a polynomial identity for all \((a,b,c)\).
* `verify_stable_rank.py` (Python standard library only) calculates the semilinear products in exact \(\mathbb F_7[A]\) arithmetic, their determinant minors and gcds, and the rank-stability conditions. It checks \(P_3=0\) at \(A=0\) and the indicated normalized finite-field ranks.
* `verify_finite_fields.py` (Python standard library only) checks geometric smoothness of each normalized quintic over \(\mathbb F_7\) and \(\mathbb F_{49}\) by Euclidean gcd with its derivative, giving the finite-field counts above independently of the discriminant formula.

All three programs executed successfully on their actual package paths. The symbolic identities prove the all-parameter claims together with the mathematical Cartier-operator argument; the finite enumerations alone would not establish a geometric classification over an algebraic closure.

## Relationship to prior work

Baldwin–Eilbeck–Gibbons–Ônishi (2006/2008) study the general cyclic \((3,5)\) trigonal model and its holomorphic differentials and Abelian functions, furnishing the standard genus-four geometric context. Their paper is concerned with complex-analytic sigma and addition formulas, not characteristic-seven Cartier strata.

Borges–Gonçalves (first public December 7, 2022) develop systematic \(p\)-rank formulas for Fermat-type curves \(y^m=x^n+1\) and related constructions. In particular, the undeformed member \(y^3=x^5+1\) is of their Fermat type; that isolated fiber's \(p\)-rank is not presented as an independent novelty claim. Their formulas do not directly cover the mixed-parameter characteristic-seven family or the full Hasse determinant/discriminant identity.

Lin–Mantovan–Singhal (2023/2024) prove generic \(p\)-ordinary behavior for abelian covers with at most five branch points and sufficiently large characteristic. The present cyclic degree-three genus-four family has six branch points in characteristic seven; their Theorem 1.1 does not apply to this case, nor provide its full nonordinary stratification. Their extensions to some larger branch counts establish generic ordinariness in selected monodromy data, not these exact coefficient equations.

Kudo–Harashita (2016/2017) prove the nonexistence of superspecial genus-four curves in characteristic seven and give general computational criteria. This is compatible with the present result, since no smooth member has Cartier \(a\)-number four; it does not imply the exact four-stratum distribution here. Searches did not locate a prior statement implying the entire \(\Delta\)-relative identity together with the rank-zero, rank-one, rank-two, and ordinary loci. An older unindexed special-family calculation remains a historical-priority possibility.

## Limitations

The classification concerns this explicitly defined family of quintic triple covers, not arbitrary cyclic genus-four curves. It determines geometric \(p\)-rank and Cartier \(a\)-number but not full Newton or Ekedahl–Oort types. The multiplicity-two statement concerns the displayed determinant on the coefficient parameter base, not a claim of multiplicity on a moduli stack quotient. The five normalized rank-one parameters are proven isomorphic by explicit scaling; no claim that different generic coefficients give nonisomorphic curves is made. Independent mathematical audit has not been performed.

## References

1. H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987, first public 2022-12-07; HTML https://arxiv.org/html/2212.03987v3 (especially Sections 1, 2 and 6).
2. S. Baldwin, J. C. Eilbeck, J. Gibbons and Y. Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four*, arXiv:math/0612654, first public 2006-12-21; HTML https://arxiv.org/html/math/0612654v1 (especially Sections 1–2).
3. Y. Lin, E. Mantovan and D. Singhal, *Abelian covers of \(\mathbb P^1\) of \(p\)-ordinary Ekedahl–Oort type*, arXiv:2303.13350, first public 2023-03-23; HTML https://arxiv.org/html/2303.13350v3 (Theorem 1.1, Sections 5–8).
4. M. Kudo and S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114, first public 2016-07-05; HTML https://arxiv.org/html/1607.01114v2 (especially the introduction and Section 5).

# Arithmetic splitting of geometrically decomposed Richelot kernels in a cubic-symmetric genus-two pencil

## Finding
Let \(q\) be any power of a prime \(p\ge7\), let \(s\in\mathbb F_q\) with \(s^2\ne4\), and let \(C_s\) denote the smooth projective curve
\[
C_s:\qquad y^2=x^6+s x^3+1.
\]
Let \(J_s\) be its principally polarized Jacobian. Define \(\mathcal D_s\) to be the reduced finite étale \(\mathbb F_q\)-scheme whose geometric points are the maximal Weil-isotropic subgroup schemes \(G\subset J_s[2]\) for which the principally polarized quotient \(J_s/G\) becomes a product of elliptic curves after extension to \(\overline{\mathbb F}_q\). Two distinct kernels are counted separately, even when their quotients are isomorphic. **Geometric decomposition** is meant: this does not assert that the two elliptic factors separately descend to \(\mathbb F_q\).

The entire Frobenius cycle structure of \(\mathcal D_s\) is as follows. The symbols \(1^a2^b\) denote \(a\) fixed geometric points and \(b\) two-cycles.

| Parameter | \(q\equiv1\pmod3\) | \(q\equiv2\pmod3\) |
|---|---|---|
| \(s\ne0\), \(s^2\ne-50\) | \(1^3\) | \(1^1 2^1\) |
| \(s=0\) | \(1^4\) | \(1^2 2^1\) |
| \(s^2=-50\) | \(1^6\) | \(1^2 2^2\) |

In particular, the numbers of \(\mathbb F_q\)-rational geometrically decomposed Richelot kernels in the three rows are \(3,4,6\), respectively, when \(q\equiv1\pmod3\), and \(1,2,2\), respectively, when \(q\equiv2\pmod3\). Every geometric kernel in \(\mathcal D_s\) is defined over \(\mathbb F_{q^2}\).

For \(E_q=1+\chi_q(-2)\), where \(\chi_q\) is the quadratic character, the three respective numbers of smooth **coefficient parameters** in \(\mathbb F_q\) are \(q-3-E_q\), \(1\), and \(E_q\). These count parameters, not geometric isomorphism classes. The zeta function of \(\mathcal D_s\) is obtained from its table entry by
\[
Z(\mathcal D_s/\mathbb F_q,T)=(1-T)^{-a}(1-T^2)^{-b}
\]
for cycle type \(1^a2^b\).

## Assumptions and scope
The characteristic restriction \(p\ge7\) excludes the characteristics \(2,3,5\), where the determinant classifications may degenerate. The equation has six distinct finite geometric branch points exactly when \(s^2\ne4\); then its smooth projective model has genus two. All assertions concern the *canonical reduced scheme of geometric decomposed kernels*, not the moduli of isogeny targets or the product decomposition over the ground field. The uniform statement includes arbitrary finite extension fields, not only prime fields.

## Proof
**1. Branch roots and kernels.** Fix a primitive cube root \(\omega\) over an algebraic closure and choose \(A\ne0\) with \(A^3+A^{-3}=-s\). The six distinct branch roots are
\[
L_j=A\omega^j,\qquad R_j=A^{-1}\omega^j,\qquad j\in\{0,1,2\}.
\]
Maximal isotropic subgroups of \(J_s[2]\) correspond bijectively to the fifteen unordered partitions of these six roots into three unordered pairs. For a partition \(M\), let its three monic quadratic factors be \(h_1,h_2,h_3\). The classical Richelot criterion states that the quotient is geometrically a product of elliptic curves exactly when the coefficient determinant \(\det(h_1,h_2,h_3)\) vanishes (a basis-independent zero condition). This is the same notion as the decomposed outgoing Richelot kernels in Katsura--Takashima, Proposition 4.5, and their preceding Richelot construction.

**2. Exhaustive determinant computation and exceptional locus.** Put \(t=A^2\). Multiply each coefficient determinant by \(A^3\), thereby obtaining a polynomial \(D_M(t,\omega)\) in the ring defined by \(\omega^2+\omega+1=0\). In the following exact table, \(N(D)=D(t,\omega)D(t,\omega^2)\). The table groups all fifteen partitions, so it is exhaustive.

| Number of partitions | \(N(D_M)\) |
|---:|---|
| 3 | \(0\) |
| 1 | \(27t^2(t+1)^2\) |
| 2 | \(27t^2(t^2-t+1)\) |
| 3 | \((t-1)^2(t^2+4t+1)^2\) |
| 6 | \((t^2+t+1)(t^4-4t^3+15t^2-4t+1)\) |

These identities are direct determinants of the six displayed roots, and are independently reproduced by the accompanying symbolic checker. Because \(p\ge7\), the integer factors \(3\), \(5\) and \(27\) do not vanish accidentally. Also
\[
s^2-4=\frac{(t^3-1)^2}{t^3},\qquad
s^2=\frac{(t^3+1)^2}{t^3},
\]
so the roots of \(t^3-1\) give precisely the excluded singular fibers, and the roots of \(t^3+1\) give \(s=0\). Finally,
\[
t^6+52t^3+1=(t^2+4t+1)(t^4-4t^3+15t^2-4t+1),
\]
so every other nonzero determinant vanishes only at \(s^2=-50\). Conversely, at \(s=0\) choose \(A^2=-1\); exactly one additional partition vanishes. At \(s^2=-50\), choose \(A\) with \(A^2\) a root of \(t^2+4t+1\) (choosing the sign of \(A\) to give the prescribed \(s\)); exactly three additional partitions vanish. Hence the *geometric* cardinalities are \(3,4,6\). Those geometric counts are consistent with the previously known reduced-automorphism classification; the arithmetic Frobenius refinement below is the present claim.

For explicit labels write each root \(L_j\) as index \(j\), and \(R_j\) as index \(3+j\). The three always-vanishing partitions are
\[
P_b=\{\{L_j,R_{b-j}\}:j=0,1,2\},\quad b\in\mathbb Z/3\mathbb Z.
\]
When \(s=0\) with \(A^2=-1\), the extra partition is \(E=\{\{L_j,R_j\}:j=0,1,2\}\). When \(s^2=-50\) with \(A^2\) solving \(t^2+4t+1=0\), the three extra partitions (in indices \(0,\ldots,5\)) are
\[
Q_0=(01)(25)(34),\quad Q_1=(02)(14)(35),\quad Q_2=(03)(12)(45).
\]
Here \((ij)\) denotes an unordered pair, not an automorphism.

**3. Frobenius on the kernel labels.** Let \(\epsilon=1\) if \(q\equiv1\pmod3\), and \(\epsilon=-1\) if \(q\equiv2\pmod3\). Then \(\omega^q=\omega^\epsilon\). For arbitrary \(s\), since \(A^3\) and \(A^{-3}\) are roots of \(z^2+sz+1\), there are \(\eta\in\{\pm1\}\) and \(k\in\mathbb Z/3\mathbb Z\) such that
\[
A^q=\omega^k A^\eta.
\]
On the labeled roots, Frobenius sends \(L_j\) to \(L_{k+\epsilon j}\) and \(R_j\) to \(R_{-k+\epsilon j}\) if \(\eta=1\), and interchanges \(L,R\) with those respective exponents if \(\eta=-1\). In either case,
\[
P_b\longmapsto P_{\epsilon b}.
\]
Thus the three generic decomposed kernels are all fixed for \(\epsilon=1\), and form one fixed point and a two-cycle for \(\epsilon=-1\).

On \(s=0\), use the normalization \(A^2=-1\). As Frobenius preserves this relation, \(A^q=A\) or \(A^{-1}=-A\); in particular one may set \(k=0\) above. The additional partition \(E\) is fixed for either sign \(\epsilon\).

On \(s^2=-50\), use \(A^2=t\) with \(t^2+4t+1=0\). Since the two roots of this quadratic are \(t,t^{-1}\), Frobenius maps \(A\) to \(\pm A\) or \(\pm A^{-1}\). The sign must be positive after choosing the appropriate exponent: the identity \(A^3+A^{-3}=-s\ne0\) is Frobenius-invariant, so changing the sign would change its value. Therefore again \(k=0\). Direct application to \(Q_0,Q_1,Q_2\) shows that all three are fixed when \(\epsilon=1\), while Frobenius exchanges \(Q_0,Q_1\) and fixes \(Q_2\) when \(\epsilon=-1\). This proves all six cycle types and quadratic splitting.

**4. Parameter frequencies.** Because \(p\ge7\), the excluded parameters \(\pm2\), the parameter \(0\), and the roots of \(s^2+50=0\) are disjoint. The last polynomial has precisely \(1+\chi_q(-50)=1+\chi_q(-2)\) roots in \(\mathbb F_q\), proving the stated counts of coefficient values.

## Verification
Execute `python3 verify_decomposed.py` (Python 3 with SymPy). The program reconstructs all fifteen determinants from the six symbolic roots; computes their cyclotomic norm factors; verifies the special partition sets at \(s=0\) and \(s^2=-50\); verifies their complete generic vanishing locus; and enumerates all Frobenius permutations \((\epsilon,\eta,k)\). It also checks the coefficient-frequency identities for eighteen prime fields. Expected last marker: `GENUS2_DECOMPOSED_RICHELOT_FROBENIUS_EXACT_PASS`.

The universal conclusion comes from the algebraic determinant identities and Frobenius-action proof, not from tests at finitely many primes. The checker does not establish that no unindexed prior publication covers this classification.

## Relationship to prior work
Katsura and Takashima (arXiv:2003.00633, first submitted 2020-03-02), Proposition 4.5 and Section 5, establish the geometric correspondence between decomposed Richelot kernels and long reduced involutions and count the latter for the reduced automorphism types \(S_3\), \(D_{12}\), and \(S_4\). In particular the **geometric counts \(3,4,6\) are prior mathematics, not new findings here**. Moriya and Kudo (arXiv:2209.02926, first submitted 2022-09-07) develop decomposed Richelot algorithms and quotient constructions, primarily for genus three. The contribution assessed here is the exact **finite-field Frobenius descent** of the complete decomposed-kernel set in this one-parameter genus-two pencil, including all six cycle types and coefficient frequencies. Neither inspected work states these arithmetic cycle-type formulas.

## Limitations
The assertion concerns geometrically decomposed quotient polarized abelian surfaces, not necessarily products of elliptic curves defined individually over the base field. Distinct kernels need not give nonisomorphic quotient targets. It does not classify the other Richelot kernels, isomorphism classes of the curves, or characteristics \(2\), \(3\), or \(5\). The geometric counts, determinant criterion, and automorphism classification are known inputs. An equivalent Galois calculation in other published literature is a residual priority risk; no independently performed mathematical audit or validation is claimed.

## References
1. T. Katsura and K. Takashima, *Counting Richelot isogenies between superspecial abelian surfaces*, arXiv:2003.00633 (first public version 2020-03-02), especially Proposition 4.5 and Sections 5--6, https://arxiv.org/abs/2003.00633.
2. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926 (first public version 2022-09-07), Sections 1--3, https://arxiv.org/abs/2209.02926.
3. N. Bruin and K. Doerksen, *The arithmetic of genus two curves with (4,4)-split Jacobians*, Canadian Journal of Mathematics 63 (2011), 992--1024, doi:10.4153/CJM-2011-039-3, general arithmetic Richelot background.

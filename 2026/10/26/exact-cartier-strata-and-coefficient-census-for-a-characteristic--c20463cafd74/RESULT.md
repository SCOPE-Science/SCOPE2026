# Exact Cartier strata and coefficient census for a characteristic-five cyclic trigonal genus-four family

## Finding

Let \(k\) be an algebraically closed field of characteristic \(5\), and let \(C_{a,b,c}\) be the smooth projective curve associated to
\[
 y^3=x^5+a x^3+b x+c,\qquad a,b,c\in k.
\]
Put
\[
 \Delta(a,b,c)=a^5c^2-3b^3(a^2+b)^2.
\]
The affine equation has a smooth genus-four projective model exactly when \(\Delta\ne0\). On that smooth parameter locus, the Jacobian's \(5\)-rank \(f_5\) and \(a\)-number \(a_J\) are **completely determined** by
\[
 (f_5,a_J)=
 \begin{cases}
 (0,4),&a=0,\\
 (0,2),&a\ne0,\ b=-a^2,\\
 (2,2),&a\ne0,\ b\ne-a^2.
 \end{cases}
\]
In particular, this entire smooth family has \(5\)-rank at most \(2\); its rank-zero locus has two explicitly distinguished types, superspecial and non-superspecial. The first type, including superspecial genus-four examples in characteristic five, is known from earlier work and is **not** asserted to be a new existence result.

For each \(q=5^m\), \(m\ge1\), the **exact number of fixed-coordinate coefficient triples** \((a,b,c)\in\mathbb F_q^3\) producing smooth curves in the respective strata is
\[
 \begin{array}{c|c}
 (f_5,a_J)&\text{number of coefficient triples}\\\hline
 (0,4)&q(q-1)\\
 (0,2)&(q-1)^2\\
 (2,2)&(q-1)^3
 \end{array}
\]
Thus the number of smooth coefficient triples is \(q^2(q-1)\), and exactly \(q^2\) coefficient triples produce singular affine equations. These numbers count **marked equations**, not abstract curves, isomorphism classes, or moduli points. No Newton-polygon classification of the \((0,2)\) locus is claimed.

## Assumptions and scope

The ground field is any perfect field of characteristic five for the Cartier formulas, and its algebraic closure for the geometric rank assertions. For counting, the coefficients lie in a specified finite field \(\mathbb F_{5^m}\). Throughout \(\Delta\ne0\); a singular polynomial is not admitted to the smooth family. Rank \(f_5\) means the dimension over \(\mathbb F_5\) of the geometric \(5\)-torsion group of the Jacobian, and \(a_J=\dim\ker\mathcal C\) for the Cartier operator on \(H^0(C,\Omega^1_C)\).

The family is the odd-plus-constant quintic slice of cyclic cubic covers. It contains the distinguished automorphism-rich model \(y^3=x^5-x\) and gives a controlled deformation in the same six-branch-point inertia class (trielliptic signature \((3,1)\), up to interchanging characters). This is a slice inside the moduli of cyclic covers, not all genus-four curves or all curves of that signature.

## Proof

**1. Smoothness and genus.** Write \(F(x)=x^5+a x^3+b x+c\). Its formal derivative in characteristic \(5\) is \(F'(x)=3a x^2+b\). When \(a=0\), the polynomial is separable exactly if \(b\ne0\); the expression \(\Delta=-3b^5\) detects precisely this condition. When \(a\ne0\), a multiple root \(t\) obeys \(t^2=3b/a\). Substitution into \(F\) gives
\[
 F(t)=c+\frac{4b(a^2+b)}{a^2}t.
\]
Since the possible roots of the derivative are \(t\) and \(-t\), the existence of a common root is equivalent to
\[
 c^2=\frac{3b^3(a^2+b)^2}{a^5},
\]
including the cases when \(t=0\) or \(b=-a^2\). Hence \(F\) is squarefree if and only if \(\Delta\ne0\). The extension \(k(x,y)/k(x)\) given by \(y^3=F(x)\) is separable of degree three, totally ramified at five simple finite roots and infinity. Riemann–Hurwitz yields \(2g-2=-6+6\cdot2=6\), so \(g=4\). The point at infinity on the smooth projective model is unique.

**2. Cartier basis and formulas.** A basis of regular differentials is
\[
 \omega_0=\frac{dx}{y},\qquad
 \omega_1=\frac{dx}{y^2},\qquad
 \omega_2=\frac{x\,dx}{y^2},\qquad
 \omega_3=\frac{x^2\,dx}{y^2}.
\]
To verify regularity, at infinity \(\operatorname{ord}_\infty(x)=-3\), \(\operatorname{ord}_\infty(y)=-5\), and \(\operatorname{ord}_\infty(dx)=-4\), so all four displayed differentials are regular; they are also regular at finite branch points because \(dx\) vanishes to order \(2\) there. They are independent and their number equals the genus.

The Cartier operator \(\mathcal C\) is additive and \(5^{-1}\)-linear. Since \(y^3=F(x)\),
\[
 \frac{dx}{y}=\left(\frac1{y^2}\right)^5F(x)^3\,dx,\qquad
 \frac{dx}{y^2}=\left(\frac1y\right)^5F(x)\,dx.
\]
The rule \(\mathcal C(x^{5j+4}dx)=x^jdx\) (and vanishing for the other residue classes) applies to the polynomial numerator. The only coefficients of \(F^3\) at exponents \(4,9,14\) are, respectively,
\[
 [x^4]F^3=abc,\qquad
 [x^9]F^3=a(a^2+b),\qquad
 [x^{14}]F^3=0.
\]
For \(F\), \([x^4]F=0\); for \(xF\), \([x^4](xF)=a\); and for \(x^2F\), \([x^4](x^2F)=0\). Therefore, writing \(u^{1/5}\) for the unique fifth root in the perfect field,
\[
 \begin{aligned}
 \mathcal C(\omega_0)&=(abc)^{1/5}\omega_1+
             \bigl(a(a^2+b)\bigr)^{1/5}\omega_2,\\
 \mathcal C(\omega_1)&=0,\\
 \mathcal C(\omega_2)&=a^{1/5}\omega_0,\\
 \mathcal C(\omega_3)&=0.
 \end{aligned}
\]
This computation is symbolic and valid for every admitted parameter, not a finite numerical inference.

**3. Semilinear rank and stable rank.** If \(a=0\), the Cartier operator is identically zero. Hence \(a_J=4\), \(f_5=0\), and the Jacobian is superspecial. If \(a\ne0\) and \(b=-a^2\), smoothness forces \(c\ne0\), so \(abc\ne0\); the operator has rank \(2\) and is nilpotent of index \(3\), with the chain \(\omega_2\mapsto\omega_0\mapsto\omega_1\mapsto0\) up to nonzero scalars. Thus \((f_5,a_J)=(0,2)\). If \(a\ne0\) and \(b\ne-a^2\), the two-dimensional subspace spanned by \(\omega_0\) and \(\mathcal C(\omega_0)\) is mapped bijectively (semilinearly) into itself by \(\mathcal C\), while the complementary nilpotent part is killed. Thus its stable rank is \(2\), and its instantaneous rank is also \(2\), giving \((f_5,a_J)=(2,2)\). Geometric \(5\)-rank equals the stable Cartier rank, and \(a_J=4-\operatorname{rank}\mathcal C\), completing the classification.

**4. Exact counting.** Fix \(q=5^m\). For \(a=0\), smoothness is equivalent to \(b\ne0\), with \(c\) arbitrary, giving \(q(q-1)\) presentations of type \((0,4)\). For \(a\ne0\) and \(b=-a^2\), the discriminant becomes \(a^5c^2\); hence smoothness is \(c\ne0\), giving \((q-1)^2\) presentations of type \((0,2)\).

To count *all* singular presentations, for \(a=0\) there are exactly \(q\) (namely \(b=0\), all \(c\)). Fix \(a\ne0\). The cases \(b=0\) and \(b=-a^2\) each give one singular \(c\). For the remaining \(b\), the derivative equation \(t^2=3b/a\) has two roots in \(\mathbb F_q\) or none. It yields two singular \(c\)'s exactly in the square case. Writing \(\chi\) for the quadratic character, the number of singular \(c\)'s, summed over all \(b\), is \(q-\chi(2a)\). Consequently the total number of singular triples is
\[
 q+\sum_{a\in\mathbb F_q^\times}\bigl(q-\chi(2a)\bigr)=q^2.
\]
Subtracting from \(q^3\), and then subtracting the two rank-zero strata, gives
\[
 q^3-q^2-q(q-1)-(q-1)^2=(q-1)^3
\]
for type \((2,2)\). All counts hold for every positive integer \(m\).

## Verification

The independent standard-library verifier `verify.py` implements \(\mathbb F_5\) and \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\), computes the smoothness test by polynomial gcd (separately from the displayed discriminant), expands \(F^3\) directly to recover the Cartier matrix, checks its semilinear powers and ranks, and exhaustively enumerates marked parameter triples over both fields. Execute `python3 verify.py` in the same directory as this file. The observed counters were

| Field | singular | \((0,4)\) | \((0,2)\) | \((2,2)\) |
|---|---:|---:|---:|---:|
| \(\mathbb F_5\) | 25 | 20 | 16 | 64 |
| \(\mathbb F_{25}\) | 625 | 600 | 576 | 13824 |

The verifier terminates with `VERIFY_OK`. All \(125\) triples over \(\mathbb F_5\) were individually checked for the semilinear Cartier ranks, and for \(\mathbb F_{25}\) the matrix checks include forty representatives of each of the three smooth strata in addition to the exhaustive separability and census checks for all \(15625\) triples. The general theorem rests on the four symbolic proof steps, not on extrapolation from these fields.

## Relationship to prior work

Kudo (2018, arXiv:1804.09063) proves existence and provides equations for superspecial genus-four nonhyperelliptic curves, including characteristic five. That establishes the background superspecial phenomenon; no superspecial existence claim is presented as new here. Özman–Pries–Weir (2019, arXiv:1907.05684) prove general existence and geometric irreducibility results for \(p\)-rank strata of cyclic cubic covers, including the genus-four signature \((3,1)\). Their theorem does not state an explicit equation for the rank-zero locus **in the particular fixed-coefficient slice considered here**, nor the three arithmetic marked counts. Obus–Shaska (2020, arXiv:2006.12685) classify superelliptic curves with many automorphisms over \(\mathbb C\) and analyze complex multiplication; that motivates the automorphism-rich seed but does not supply the characteristic-five Cartier stratification.

Baldwin–Eilbeck–Gibbons–Ônishi (2008) study Abelian functions on general cyclic trigonal genus-four curves of quintic form, without the positive-characteristic arithmetic census. Sohn (2025, DOI:10.23091/japm.2025.059) directly studies the \(a\)-numbers of genus-four superelliptic curves. Only its abstract was accessible during this comparison, so overlap in its unavailable full text **cannot be excluded**; in particular this result does not claim that the methods or isolated \(a\)-number computations are new. The claimed distinction is the complete simultaneous \(5\)-rank/\(a\)-number stratification and exact marked finite-field census of this specified slice. A search of relevant indexed mathematical findings did not locate a stronger or equivalent recorded statement, but negative searches alone cannot establish global novelty.

## Limitations

This is a classification of **coefficient-marked** equations, not isomorphism classes or a complete genus-four moduli classification. It does not establish that all \(5\)-rank-zero curves in the non-superspecial stratum have supersingular Newton polygons: \(p\)-rank zero does not imply supersingularity in genus four. The pre-existing superspecial curve and the existence of trielliptic rank-zero curves are credited to prior literature. The 2025 Sohn article is materially relevant but its full text was not accessible for comparison; therefore the originality assessment has residual coverage risk. No independent external audit was performed.

## References

1. M. Kudo, *On the existence of superspecial nonhyperelliptic curves of genus 4*, arXiv:1804.09063 (first public 2018-04-24), https://arxiv.org/abs/1804.09063.
2. E. Özman, R. Pries, C. Weir, *The boundary of the p-rank 0 stratum of the moduli space of cyclic covers of the projective line*, arXiv:1907.05684 (first public 2019-07-12), https://arxiv.org/abs/1907.05684.
3. A. Obus, T. Shaska, *Superelliptic curves with many automorphisms and CM Jacobians*, arXiv:2006.12685 (first public 2020-06-23), https://arxiv.org/abs/2006.12685.
4. S. Baldwin, J. C. Eilbeck, J. Gibbons, Y. Ônishi, *Abelian functions for cyclic trigonal curves of genus 4*, J. Geom. Phys. 58 (2008), 450–467, DOI:10.1016/j.geomphys.2007.12.001.
5. G. Sohn, *The a-number of superelliptic curves of genus four*, J. Appl. Pure Math. 7 (2025), 59–66, DOI:10.23091/japm.2025.059 (abstract available; complete text not inspected).

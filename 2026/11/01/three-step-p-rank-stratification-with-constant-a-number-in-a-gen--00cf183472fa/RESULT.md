# Three-step \(p\)-rank stratification with constant \(a\)-number in a genus-four trigonal family

## Finding
Let \(k=\overline{\mathbb F}_7\), and let \(C_{a,b}\) be the smooth projective model of the cyclic trigonal curve
\[
 y^3=x^5+a x^2+b,
\]
for \(a,b\in k\) satisfying \(b(b^3+a^5)\ne0\). This curve has genus four and its Jacobian has \(a\)-number **exactly two for every smooth parameter pair**. Its geometric \(p\)-rank takes exactly three values, with complete stratification
\[
 f(J(C_{a,b}))=\begin{cases}
 0,&a=0,\\
 1,&a\ne0,\ a^5=b^3,\\
 2,&a\ne0,\ a^5\ne b^3.
 \end{cases}
\]
In particular, this entire natural cyclic genus-four family is nonordinary. Both nonzero-rank strata are nonempty; the \(p\)-rank-one stratum is smooth because \(b^3+a^5=2b^3\ne0\) there.

## Assumptions and scope
The classification is over the algebraic closure of characteristic seven and concerns the smooth *marked-coefficient* two-parameter family, not an asserted classification of isomorphism classes over smaller fields. Its parameter discriminant is precisely \(b(b^3+a^5)\). All rank statements refer to the Jacobian of the smooth complete curve.

## Proof
Write \(F(x)=x^5+a x^2+b\). In characteristic seven its derivative is \(F'(x)=x(5x^3+2a)\). Thus a repeated root at \(x=0\) occurs exactly when \(b=0\); at a nonzero critical point, \(x^3=a\) and the equation \(F(x)=0\) becomes \(2a x^2+b=0\), yielding exactly \(b^3+a^5=0\). Therefore the stated parameter condition is equivalent to separability of the degree-five polynomial. The tame cyclic cover of \(\mathbb P^1\) has six totally ramified branch points (five finite and infinity), so Riemann--Hurwitz gives \(2g-2=3(-2)+6(3-1)=6\) and \(g=4\).

A regular differential basis is
\[
 \omega_0=\frac{dx}{y},\quad\omega_1=\frac{dx}{y^2},\quad
 \omega_2=\frac{x\,dx}{y^2},\quad\omega_3=\frac{x^2\,dx}{y^2}.
\]
The characteristic-seven Cartier formula is
\[
 \mathcal C\!\left(\frac{x^i dx}{y^j}\right)
 =\sum_{r\ge0}\bigl([x^{7r+6}]x^i F(x)^{2j}\bigr)^{1/7}
 \frac{x^r dx}{y^j},\qquad j\in\{1,2\}.
\]
Direct expansion shows that the matrix of seventh powers of Cartier coefficients in this basis equals
\[
 H=\begin{pmatrix}
0&0&0&0\\
0&4a^3b&4b^3&6a^2b^2\\
0&0&5ab&4a^3\\
0&1&0&0
\end{pmatrix}.
\]
Its lower-right \(3\times3\) block has determinant zero identically in characteristic seven but rank exactly two when \(b\ne0\); hence Cartier on all four forms has rank two and the \(a\)-number equals \(4-2=2\) everywhere on the smooth family.

Over \(k\), a weighted scaling of \(x\) and \(y\) identifies \(C_{a,b}\) with \(C_{u,1}\), where \(u^5=a^5/b^3\). In these coordinates the lower-right Cartier seventh-power matrix is
\[
 B(u)=\begin{pmatrix}
4u^3&4&6u^2\\
0&5u&4u^3\\
1&0&0
\end{pmatrix}.
\]
The rank of the second Cartier iterate is that of \(B(u)^{(7)}B(u)\), where \((7)\) raises all coefficients to the seventh power. Direct symbolic minor calculation over \(\mathbb F_7[u]\) gives
\[
 \gcd\{\text{all nonzero }2\times2\text{ minors of }B(u)^{(7)}B(u)\}
 =u^4(u^{10}-1),
\]
up to a nonzero scalar. The smoothness condition has become \(u^5\ne-1\). Consequently the second Cartier iterate has rank two precisely when \(u\ne0\) and \(u^5\ne1\). In that case the Cartier image and its second image have the same dimension, so all later stable images have dimension two, giving \(p\)-rank two.

For \(u=0\), the successive ranks of Cartier and its second and third iterates are \(2,1,0\), hence \(p\)-rank zero. If \(u^5=1\), a fifth-root-of-unity scaling identifies the curve with \(u=1\). At \(u=1\), the successive ranks are \(2,1,1,1\), giving stable rank one and hence \(p\)-rank one. This proves the exact classification.

## Verification
The standalone exact-arithmetic script `verify.py` expands the relevant powers of \(F\), reproduces the Cartier coefficient matrix, constructs its semilinear second-iterate matrix, computes the greatest common divisor of all its \(2\times2\) minors over \(\mathbb F_7[u]\), and directly checks stable iteration ranks at the two exceptional normalized parameters. It ends with `VERIFY_OK`. The proof is symbolic over the entire algebraic closure; finite evaluation is used only for representatives which are algebraically identified with the full exceptional strata.

## Relationship to prior work
Baldwin--Eilbeck--Gibbons--Ônishi [1] develop Abelian functions of the general cyclic \((3,5)\) genus-four family and supply a regular differential basis, but do not give this characteristic-seven Cartier locus. The present feature is the constant \(a\)-number two together with the three strata \(f=0,1,2\) for the quadratic-coefficient family; these conclusions do not follow from changing the coefficient positions in a neighboring sparse equation. The published genus-three Picard curve computations of Kazemifard--Tafazolian [2] do not imply this genus-four classification.

## Limitations
The assertion does not classify the full genus-four cyclic trigonal moduli space, characteristic primes other than seven, or isomorphism classes over finite nonclosed fields. It does not determine the complete Newton polygon or zeta function for the generic member. General finite-characteristic Cartier machinery is classical; the assessed contribution is this explicit complete parameter stratification and invariant constancy. No independent scientific audit has been performed, and earlier unindexed equivalent computations remain a possible priority risk.

## References
[1] S. Baldwin, J. C. Eilbeck, J. Gibbons and Y. Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four*, arXiv:math/0612654v1 (first posted 21 December 2006), https://arxiv.org/pdf/math/0612654 .

[2] A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields Appl. 34 (2015), 107--122, https://doi.org/10.1016/j.ffa.2014.12.002 .

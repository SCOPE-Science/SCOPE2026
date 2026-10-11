# Exact eighth-moment cost of one isolated quartic torsion collision
## Finding
Let \(G\) be a compact abelian group with normalized Haar measure, and let \(\lambda_0,\lambda_1,\lambda_2\in\widehat G\) be distinct characters. Assume that among the unordered fourfold products
\[
\lambda_0^{\alpha_0}\lambda_1^{\alpha_1}\lambda_2^{\alpha_2},\qquad \alpha_j\ge 0,\quad \alpha_0+\alpha_1+\alpha_2=4,
\]
the only equality between two distinct exponent triples is
\[
\lambda_0^4=\lambda_1^4.
\]
Then the sharp constant in
\[
\|a\lambda_0+b\lambda_1+c\lambda_2\|_{L^8(G)}
\le K_{\mathrm{iso}}\bigl(|a|^2+|b|^2+|c|^2\bigr)^{1/2}
\]
is determined by
\[
K_{\mathrm{iso}}^8=X_*,
\]
where \(X_*\) is the unique positive root of
\[
343X^3+155931X^2-1117059X-1095481=0.
\]
Numerically,
\[
X_*=7.91378569515504976342868902599\ldots,
\qquad
K_{\mathrm{iso}}=1.29508429140811989427097580821\ldots.
\]
If \(u_*\in(0,1/2)\) is the unique root of
\[
28u^3-72u^2+12u+3=0,
\]
then
\[
u_*=0.334719056638195611541075837435\ldots.
\]
Every nonzero extremizer, and only every such extremizer, satisfies
\[
|a|^2=|b|^2=u_*\bigl(|a|^2+|b|^2+|c|^2\bigr),
\]
\[
|c|^2=(1-2u_*)\bigl(|a|^2+|b|^2+|c|^2\bigr),
\]
and
\[
4(\arg a-\arg b)\in2\pi\mathbb Z.
\]
The phase of \(c\) is arbitrary.

## Assumptions and scope
The collision hypothesis is a statement about exponent triples of total degree four, not merely about pairwise distinctness of the characters. It implies that \(\lambda_1\lambda_0^{-1}\) has exact order four and excludes every other fourth-order collision involving \(\lambda_2\). The hypothesis is nonempty: on a product whose dual contains \(\mathbb Z\times\mathbb Z/4\mathbb Z\), the three dual elements \((0,0)\), \((0,1)\), and \((1,0)\) have exactly this collision pattern at total degree four.

This is an exact \(L^8/L^2\) statement for the indicated three-character spectra. It does not assert that every non-\(B_4\) three-character set has the same constant.

## Proof
Write
\[
x=|a|^2,\qquad y=|b|^2,\qquad z=|c|^2.
\]
Parseval applied to the fourth power gives the eighth moment as the sum of squared fourth-convolution coefficients. If all fifteen degree-four exponent triples were distinct, the moment would be
\[
P_0=(x+y+z)^4+12(x+y+z)^2(xy+xz+yz)+6(xy+xz+yz)^2+60(x+y+z)xyz.
\]
Under the stated hypothesis, only the coefficients belonging to \(a^4\) and \(b^4\) merge. Therefore
\[
\|a\lambda_0+b\lambda_1+c\lambda_2\|_8^8
=P_0+2x^2y^2\cos\bigl(4(\arg a-\arg b)\bigr).
\]
For fixed magnitudes, the phase term is maximal exactly when
\[
4(\arg a-\arg b)\in2\pi\mathbb Z
\]
provided \(ab\ne0\).

Normalize \(x+y+z=1\). Put \(s=x+y\) and \(p=xy\), so \(z=1-s\). With the maximizing phase, the objective equals
\[
8p^2+p\bigl(12s^2+96sz+72z^2\bigr)
+s^4+16s^3z+36s^2z^2+16sz^3+z^4.
\]
For fixed \(s\) and \(z\), both coefficients involving \(p\) are nonnegative and the coefficient of \(p\) is positive away from the trivial zero case. Hence the objective is strictly increasing in \(p\). Since \(p\le s^2/4\), equality forces \(x=y=s/2\).

Set \(x=y=u\) and \(z=1-2u\), with \(0\le u\le1/2\). The normalized eighth power becomes
\[
Q(u)=56u^4-192u^3+48u^2+24u+1,
\]
and
\[
Q'(u)=8\bigl(28u^3-72u^2+12u+3\bigr).
\]
Let
\[
f(u)=28u^3-72u^2+12u+3.
\]
On \([0,1/2]\), the derivative \(f'(u)=12(7u^2-12u+1)\) has only one zero before \(1/2\), namely \((6-\sqrt{29})/7\). The function \(f\) is positive through that local maximum, while \(f(1/2)<0\); consequently \(f\) has exactly one zero \(u_*\) in \((0,1/2)\), and \(Q\) increases before \(u_*\) and decreases after it. The boundary values are \(Q(0)=1\) and \(Q(1/2)=9/2\), so \(u_*\) gives the unique magnitude maximum.

Eliminating \(u\) between \(f(u)=0\) and \(X=Q(u)\) gives
\[
343X^3+155931X^2-1117059X-1095481=0.
\]
Its other two real roots are negative, so \(X_*=Q(u_*)\) is its unique positive root. The preceding strictness statements also give the complete equality classification.

## Verification
The accompanying checker reconstructs the collision-free fourth-convolution polynomial from the fifteen multinomial types, verifies the symmetric-polynomial identity for \(P_0\), verifies the reduction to \(Q\), checks the derivative factorization and exact resultant, isolates the relevant root rationally, and numerically checks direct Haar averages on the explicit model \(\mathbb T\times\mathbb Z_4\) against the closed formula.

The proof of the infinite statement is analytic. Numerical checks are corroboration, not a replacement for the Parseval and one-variable arguments.

## Relationship to prior work
Classical \(\Lambda(p)\) theory treats even moments through additive relations. Bourgain explicitly notes that for even exponents the norm problem becomes algebraic and combinatorial, while Michels develops the \(\Lambda(p)\)-set framework in the harmonic-analysis setting. Standard \(B_h\) theory gives a universal sharp baseline for collision-free \(B_h\) sets and only a strict inequality when a collision is present.

The present result resolves the first isolated fourth-order torsion defect exactly: one pure quartic collision raises the three-character \(\Lambda(8)\) constant above the collision-free \(B_4\) baseline and determines the displacement of the extremizing masses. The general strictness result does not supply this defect, its cubic, or its equality class.

## Limitations
Only the isolated collision pattern \(\lambda_0^4=\lambda_1^4\) is treated. Additional fourth-order collisions change the Parseval polynomial and can change both the sharp constant and the extremizers. No claim is made about non-even exponents, about more than three characters, or about spectra having several independent degree-four relations.

A literature search did not locate an implication-equivalent exact formula, but older work may encode this small finite optimization under different notation.

## References
1. C. Michels, “\(\Lambda(p)\)-sets and the limit order of operator ideals,” arXiv:math/9904176, first public 30 April 1999.
2. J. Bourgain, “Bounded orthogonal systems and the \(\Lambda(p)\)-set problem,” *Acta Mathematica* 162 (1989), 227–245, DOI 10.1007/BF02392838.
3. T. Tao and V. Vu, *Additive Combinatorics*, section on \(\Lambda(p)\)-sets and \(B_h\)-sets, especially the proposition comparing \(B_h\) sets with the sharp \(\Lambda(2h)\) baseline.

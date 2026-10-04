# A uniformly non-square counterexample to the \(p\)-isosceles conjecture at \(p=4\)
## Finding
Let \(c=\sqrt{\sqrt{17}-4}\), \(d=(2+c+c^2)/4\), and define a norm on \(\mathbb R^2\) by \(\|(s,t)\|_* = \max\{|s-ct|,|cs+t|,d|s-t|\}\). Then \(X=(\mathbb R^2,\|\cdot\|_*)\) is uniformly non-square, but its Baronti--Bertella \(p\)-isosceles constant at \(p=4\) attains their universal upper bound: \[H_4(X)=\max_{0\le a\le1}\frac{\bigl((1+a)^4+(1-a)^4\bigr)^{1/4}}{1+a^2}=\left(\frac{71+17\sqrt{17}}{64}\right)^{1/4}.\] Consequently, Conjecture 6 of Baronti--Bertella (2024), which asserts for every \(p\ge1\) that equality in this upper bound characterizes non-uniformly-non-square spaces, is false already for \(p=4\) in dimension two.

## Assumptions and scope
For a real Banach space \(Y\) and \(p\ge 1\), the \(p\)-isosceles constant is
\[
H_p(Y)=\sup\left\{(1+\lambda^p)^{1/p}\over \|x+\lambda y\|}:x,y\in S_Y,\ x\perp_I y,\ \lambda\ge0\right\},
\]
where \(x\perp_I y\) means \(\|x+y\|=\|x-y\|\). The source paper proves the universal bound
\[
H_p(Y)\le U_p:=\max_{0\le a\le1}\frac{\bigl((1+a)^p+(1-a)^p\bigr)^{1/p}}{1+a^2}
\]
and conjectures that equality is equivalent to failure of uniform non-squareness for every \(p\ge1\). The claim above concerns the first simple superquadratic exponent \(p=4\).

## Proof
Put \(u=c^2=\sqrt{17}-4\). Since \(4<\sqrt{17}<5\), one has \(0<c<1\). For \(p=4\), if
\[
F(a)=\frac{\bigl((1+a)^4+(1-a)^4\bigr)^{1/4}}{1+a^2},
\]
then, with \(v=a^2\),
\[
F(a)^4=\frac{2(1+6v+v^2)}{(1+v)^4},\qquad
\frac{d}{dv}F(a)^4=-\frac{4(v^2+8v-1)}{(1+v)^5}.
\]
Thus the unique maximizer on \([0,1]\) is \(v=u=\sqrt{17}-4\), hence \(a=c\). Using \(u^2+8u-1=0\),
\[
U_4^4=\frac{2(1+6u+u^2)}{(1+u)^4}=\frac{71+17\sqrt{17}}{64}.
\]

Let \(x=(1,0)\), \(y=(0,1)\), and \(\lambda_0=(1-c)/(1+c)\). Because \(d<1\) and \(2d\le1+c\),
\[
\|x\|_*=\|y\|_*=1,\qquad \|x+y\|_*=\|x-y\|_*=1+c,
\]
so \(x\perp_I y\). At \(\lambda_0\), the first two defining functionals coincide:
\[
1-c\lambda_0=c+\lambda_0=\frac{1+c^2}{1+c}.
\]
The third term does not dominate because
\[
d(1-\lambda_0)=\frac{2cd}{1+c}\le\frac{1+c^2}{1+c},
\]
where the inequality reduces to \((c-1)(c^2+2)\le0\). Hence
\[
\|x+\lambda_0y\|_* = \frac{1+c^2}{1+c}.
\]
Therefore
\[
H_4(X)\ge\frac{(1+\lambda_0^4)^{1/4}}{\|x+\lambda_0y\|_*}
=\frac{\bigl((1+c)^4+(1-c)^4\bigr)^{1/4}}{1+c^2}=U_4.
\]
The universal upper bound from Baronti--Bertella gives the reverse inequality, hence \(H_4(X)=U_4\).

It remains to show that \(X\) is uniformly non-square. Its closed unit ball is the intersection of the three strips
\[
|s-ct|\le1,\qquad |cs+t|\le1,\qquad d|s-t|\le1.
\]
The first strip is active at \((1,0)\), the second at \((0,1)\), and the third is nonredundant. Indeed, for
\[
z=\left(\frac{1-c}{1+c^2},-\frac{1+c}{1+c^2}\right)
\]
the first two absolute values equal \(1\), while
\[
d|z_1-z_2|=\frac{2d}{1+c^2}>1
\]
because \(c>c^2\). Thus the unit ball is a centrally symmetric hexagon, not a parallelogram.

A two-dimensional normed space that is not uniformly non-square must have a parallelogram as its unit ball. To see this, compactness gives \(r,s\in S_X\) with \(\|r+s\|=\|r-s\|=2\). Then \((r+s)/2\) and \((r-s)/2\) are boundary midpoints of two adjacent sides of the parallelogram \(\operatorname{conv}\{\pm r,\pm s}\). Supporting lines at those midpoints, and their negatives, force the whole unit ball to lie inside that parallelogram, while convexity gives the reverse inclusion. Hence the ball is exactly that parallelogram. Since the ball of \(X\) above is not a parallelogram, \(X\) is uniformly non-square.

## Verification
The accompanying `verify.py` checks the algebraic relations \(u^2+8u-1=0\), the closed form for \(U_4^4\), the stated inequalities for \(c,d\), the isosceles pair, and the extremizing ratio numerically at high precision. These checks are supplementary: the global maximization and the uniform-non-squareness conclusion are proved analytically above.

## Relationship to prior work
Baronti and Bertella define \(H_p\), prove the universal bound used above, prove the proposed equality characterization for \(1\le p\le2\) under the attainment hypothesis, and state Conjecture 6 for all \(p\ge1\). Their paper also computes the upper bound exactly on \(\ell_\infty^2\), a non-uniformly-non-square space. The construction here instead preserves one extremizing isosceles configuration while cutting an unused corner of the corresponding parallelogram; that makes the plane uniformly non-square without changing the extremal \(H_4\) value. Searches for the conjecture, \(H_4\), and p-isosceles equality cases found the source paper and later papers on different isosceles-based constants, but no published statement implying or matching this counterexample.

## Limitations
The result disproves the stated all-\(p\) equivalence by a single explicit exponent \(p=4\). It does not classify the exponents \(p>2\) for which analogous counterexamples exist, nor does it determine \(H_p\) for the constructed hexagonal norm when \(p\ne4\). The originality assessment is literature-search based rather than an exhaustive mathematical database proof.

## References
1. M. Baronti and V. Bertella, “A Generalization of the Isosceles Constant in Banach Spaces,” *Mediterranean Journal of Mathematics* 21 (2024), Article 113, DOI 10.1007/s00009-024-02654-9. The accepted manuscript available from the University of Genoa repository contains Definition 3, Theorem 5.1, Theorem 5.5, and Conjecture 6.
2. University of Genoa IRIS record for the accepted manuscript, handle 11567/1182495.

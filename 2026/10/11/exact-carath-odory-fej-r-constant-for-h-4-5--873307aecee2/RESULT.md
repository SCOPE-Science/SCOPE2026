# Exact Carathéodory–Fejér constant for \(H=\{4,5\}\)
## Finding
Let \(M(\{4,5\})\) be the supremum of \(a\in\mathbb R\) for which there exist \(b,c\in\mathbb R\) such that
\[
1+a\cos\theta+b\cos(4\theta)+c\cos(5\theta)\ge 0
\qquad(\theta\in\mathbb R).
\]
Then
\[
M(\{4,5\})=\frac{2}{\sqrt3}\cos\!\left(\frac{\pi}{18}\right).
\]
Equivalently, the sharp value is the unique real root greater than \(1\) of
\[
3A^3-3A-1=0.
\]
The extremizer is unique. If
\[
r=\cos\!\left(\frac{7\pi}{9}\right),
\]
then its coefficients are
\[
A=\frac{2(2r^2-2r-1)}{3},
\qquad
b=\frac{8(r^2-r-1)}{9},
\qquad
c=-\frac{4r^2-4r-7}{9}.
\]
Numerically,
\[
A=1.137158042603257\ldots,
\qquad
b=0.313660917291061\ldots,
\qquad
c=0.176502874687803\ldots.
\]

## Assumptions and scope
The polynomial is real and even, its constant coefficient is normalized to \(1\), and nonnegativity is required for every real \(\theta\). Only the frequencies \(1\), \(4\), and \(5\) are allowed. No statement is made here for other sparse supports or for a discretized sampling grid.

## Proof
Put
\[
\tau=\cos\!\left(\frac{\pi}{9}\right),
\qquad
\sigma=\cos\!\left(\frac{2\pi}{9}\right),
\qquad
\theta_0=\frac{7\pi}{9}.
\]
At \(\theta=\pi\), the fourth and fifth cosine values are \(1\) and \(-1\). At \(\theta=\theta_0\), they are \(-\tau\) and \(\tau\), while \(\cos\theta_0=-\sigma\). Therefore every admissible polynomial \(T\) satisfies
\[
0\le \tau T(\pi)+T(\theta_0)
   =1+\tau-a(\tau+\sigma).
\]
Hence
\[
a\le \frac{1+\tau}{\tau+\sigma}.
\]
The sum-to-product identities give
\[
1+\tau=2\cos^2\!\left(\frac{\pi}{18}\right),
\qquad
\tau+\sigma=2\cos\!\left(\frac{\pi}{6}\right)
\cos\!\left(\frac{\pi}{18}\right),
\]
so the upper bound equals
\[
A=\frac{2}{\sqrt3}\cos\!\left(\frac{\pi}{18}\right).
\]
The triple-angle identity then yields \(3A^3-3A-1=0\).

It remains to prove attainment. Set
\[
r=\cos\!\left(\frac{7\pi}{9}\right).
\]
Then \(r\in(-1,-3/4)\) and \(8r^3-6r-1=0\). Define \(A,b,c\) as in the finding and put \(x=\cos\theta\). With the Chebyshev polynomials \(T_4(x)=8x^4-8x^2+1\) and \(T_5(x)=16x^5-20x^3+5x\), direct algebra modulo \(8r^3-6r-1=0\) gives
\[
1+Ax+bT_4(x)+cT_5(x)
=
\frac{(x+1)(x-r)^2 R_r(x)}{\frac92(8r^2-6r-1)},
\]
where
\[
R_r(x)=32r(3r-2)x^2-128r(r-1)x+4r(16r-15).
\]
The denominator is positive because \(r<-3/4\). The leading coefficient of \(R_r\) is positive, and its discriminant is
\[
-64(80r^2-62r-13)<0.
\]
Thus \(R_r(x)>0\) for every real \(x\). Since \(x+1\ge0\) for \(x\in[-1,1]\), the displayed factorization proves global nonnegativity and hence attainment of \(A\).

For uniqueness, equality in the positive weighted upper-bound certificate forces \(T(\pi)=T(\theta_0)=0\). Because \(\theta_0\) is an interior zero of a nonnegative smooth function, also \(T'(\theta_0)=0\). The first and derivative conditions give
\[
b-c=A-1,
\qquad
4b+5c=2A\cos\!\left(\frac{\pi}{9}\right),
\]
which determine \(b\) and \(c\) uniquely and reduce to the coefficients above.

## Verification
The accompanying `artifacts/verify.py` checks, in exact symbolic arithmetic, the cubic relation for \(r\), the factorization modulo \(8r^3-6r-1\), the three contact identities, the cubic equation for \(A\), and the residual-quadratic discriminant. It then identifies the intended real root numerically and checks the sign conditions used in the proof. Its replay output is

`VERIFY_OK r=-0.766044443118978 A=1.137158042603257 B=0.313660917291061 C=0.176502874687803 cubic=3A^3-3A-1 factor_mod_p=1`

The numerical root identification is only a check of the root branch; the proof of nonnegativity and sharpness is exact.

## Relationship to prior work
Kolountzakis and Révész formulate the continuous sparse Carathéodory–Fejér problem \(M(H)\) for arbitrary \(H\subset\{2,3,\ldots\}\), establish its relation to positive-definite support problems, and list several exact families. Their listed exact cases include singletons, complements of singletons, tails, and parity families, but not the finite support \(H=\{4,5\}\). Krenedits and Révész later extend the reduction to locally compact Abelian groups and again treat the general framework rather than this exact two-harmonic value.

A published exact calculation for the neighboring support \(H=\{3,4\}\) is implication-incomparable: monotonicity of \(M(H)\) only compares nested supports, and neither \(\{3,4\}\) nor \(\{4,5\}\) contains the other. Likewise, exact values for supports \(\{2,4\}\), \(\{2,5\}\), and \(\{3,5\}\) do not determine the present value.

## Limitations
The result is only for the continuous real-even problem with the fixed sparse support \(\{1,4,5\}\). It does not determine the discretized grid analogue, the full two-element-support classification, or the extremal quantity for arbitrary \(H\). The originality comparison cannot exclude an older equivalent statement hidden under substantially different notation for positive trigonometric polynomials.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1, submitted 2003-02-17. Primary MSC 42B10.
2. S. Krenedits and S. Gy. Révész, *The Carathéodory–Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071v1, submitted 2013-03-30.

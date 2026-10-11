# Exact sparse Carathéodory–Fejér constant for frequencies \(1,2,5\)

## Finding
Let \(\mathcal M(\{1,2,5\})\) be the sparse Carathéodory–Fejér extremum in the normalization of Krenedits and Révész: among all real trigonometric polynomials
\[
T(\theta)=1+a\cos\theta+b\cos(2\theta)+c\cos(5\theta)\ge 0
\]
for every real \(\theta\), maximize the coefficient \(a\). Put \(d=\cos(3\pi/7)\). Then
\[
\mathcal M(\{{1,2,5\}})=1+2d=1+2\cos(3\pi/7).
\]
The extremizer is unique. Its coefficients are
\[
a=1+2d,\qquad b=\frac{{2+8d-8d^2}}7,\qquad c=\frac{{2-6d-8d^2}}7.
\]
Numerically the sharp value is \(1.4450418679126288\ldots\).

## Assumptions and scope
The variable \(\theta\) ranges over all real numbers. The polynomial is real and even, has constant coefficient \(1\), and only the nonconstant frequencies \(1,2,5\) are allowed. This is the continuous-circle Carathéodory–Fejér problem \(\mathcal M(\Omega)\), not a sampled cyclic-grid variant. No assertion is made for larger supports or for arbitrary three-frequency sets.

## Proof
Write
\[
d=\cos(3\pi/7),\qquad q=\cos(2\pi/7).
\]
At \(\theta=\pi\), the second and fifth harmonics are \(1\) and \(-1\). At \(\theta=5\pi/7\), they are \(-d\) and \(d\). Give the first point weight \(d/(1+d)\) and the second point weight \(1/(1+d)\). For every admissible \(T\), nonnegativity therefore gives
\[
0\le \frac d{{1+d}}T(\pi)+\frac1{{1+d}}T(5\pi/7)
 =1-a\frac{{q+d}}{{1+d}}.
\]
The standard seventh-root identities
\[
q=\frac12+d-2d^2,\qquad 8d^3-4d^2-4d+1=0
\]
imply
\[
(1+2d)(q+d)=1+d,
\]
so every admissible polynomial satisfies \(a\le1+2d\).

It remains to attain the bound. Set
\[
a_*=1+2d,\qquad b_*=\frac{{2+8d-8d^2}}7,\qquad c_*=\frac{{2-6d-8d^2}}7
\]
and let \(x=\cos\theta\). Using \(\cos(2\theta)=2x^2-1\), \(\cos(5\theta)=16x^5-20x^3+5x\), and the same seventh-root identities, direct expansion gives
\[
1+a_*x+b_*(2x^2-1)+c_*(16x^5-20x^3+5x)
=(x+1)(x+q)^2Q(x),
\]
where
\[
Q(x)=\frac{32(1+d)(1-4d)}7x^2
+\frac{16(8d^2-1)}7x
+\frac{8d(10d+3)}7.
\]
Here \(0<d<1/4\), hence the leading coefficient of \(Q\) is positive. Its discriminant equals
\[
\Delta_Q=\frac{256}{49}(232d^2+100d-34).
\]
To see that this is negative without numerical assumptions, use \(d=\sin(\pi/14)\), \(\pi<22/7\), and the alternating Taylor bound
\[
\sin y<y-\frac{y^3}{6}+\frac{y^5}{120}
\]
for \(0<y<1\). The right side is increasing on the relevant interval, and at \(y=11/49\) it is smaller than \(223/1000\). Thus \(d<223/1000\), and, since \(232t^2+100t-34\) is increasing for \(t>0\),
\[
232d^2+100d-34
<232\left(\frac{223}{1000}\right)^2+100\left(\frac{223}{1000}\right)-34
=-\frac{20359}{125000}<0.
\]
Therefore \(Q(x)>0\) for every real \(x\). Since \(x+1\ge0\) on \([-1,1]\), the displayed factorization proves \(T_*(\theta)\ge0\) for all \(\theta\), so the upper bound is attained.

For uniqueness, equality in the positive weighted bound forces
\[
T(\pi)=T(5\pi/7)=0.
\]
Because \(5\pi/7\) is an interior point of the circle parameter and \(T\ge0\), also \(T'(5\pi/7)=0\). These three linear conditions on \(a,b,c\) have nonzero determinant and their unique solution is exactly \((a_*,b_*,c_*)\). Hence the extremizer is unique.

## Verification
The accompanying `verify_exact.py` reconstructs the three contact equations, checks the exact coefficient solution, reduces the factorization using the minimal polynomial \(8d^3-4d^2-4d+1\), verifies the discriminant formula, and checks the rational Taylor inequality used above. It uses exact symbolic or rational arithmetic for those identities. The proof itself is universal and does not rely on finite sampling.

## Relationship to prior work
Krenedits and Révész formulate \(\mathcal M(\Omega)\) for arbitrary frequency sets and explain its equivalence with positive-definite sequence extremals. Their paper records the classical full-interval value and general transfer results, but the inspected full text contains no evaluation for \(\Omega=\{1,2,5\}\). The closest located exact sparse results concern different, incomparable supports, notably frequencies \(\{1,2,4\}\) and \(\{1,3,4\}\); neither coefficient feasible set contains the other, so those constants do not imply the present value.

## Limitations
This result is only for the continuous real-even problem with support \(\{0,\pm1,\pm2,\pm5\}\). It does not determine the corresponding discretized constants on finite cyclic grids, does not assert a formula for a general support \(\{1,p,q\}\), and does not claim that the displayed two-contact mechanism exhausts other sparse Carathéodory–Fejér problems.

## References
1. S. Krenedits and S. Gy. Révész, *The Carathéodory–Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071v1, first public 2013-03-30; later *J. Approx. Theory* 194 (2015), 108–131.
2. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218, first public 2003-12-10; *J. London Math. Soc.* 74 (2006), 475–496.

# Pluricanonical thresholds of the minimal-volume rank-one surface
## Finding
Let
\[
X=T(2,2,4,10)=S^*(2,2,4,10)
\]
be the unique stable surface of rank one with minimal volume
\[
K_X^2=\frac1{6351}.
\]
Then the two cyclic quotient singularities of \(X\) have Hirzebruch--Jung strings
\[
C_{73}=[2,2,2,2,2,2,2,2,2,4,2,2]
\]
and
\[
C_{87}=[2,2,2,2,10,2].
\]
Their determinants are \(73\) and \(87\). More precisely, the quotient types can be written
\[
\frac1{73}(1,66)
\qquad\text{and}\qquad
\frac1{87}(1,70),
\]
with the second equivalently \(\frac1{87}(1,46)\) after reversing the string. Their local canonical indices are \(73\) and \(87\), so
\[
\operatorname{ind}(K_X)=\operatorname{lcm}(73,87)=6351.
\]
In particular,
\[
\operatorname{ind}(K_X)K_X^2=1.
\]

The first two pluricanonical thresholds are
\[
P_n(X)=0\quad(1\le n\le10),\qquad P_{11}(X)=1,
\]
and
\[
P_n(X)\le1\quad(1\le n\le97),\qquad P_{98}(X)=2.
\]
Thus \(11\) is the smallest positive integer with a nonzero pluricanonical section, while \(98\) is the smallest positive integer for which the pluricanonical system has positive projective dimension.

For completeness, among \(2\le n\le97\), the values with \(P_n(X)=1\) are exactly
\[
\begin{aligned}
&11,22,33,37,44,48,49,55,59,60,61,66,70,71,72,73,74,77,\\
&81,82,83,84,85,86,87,88,92,93,94,95,96,97.
\end{aligned}
\]
All other \(P_n(X)\) in this range vanish.

## Assumptions and scope
The base field is \(\mathbf C\). The surface \(X\) is the surface identified by Alexeev--Liu as \(T(2,2,4,10)=S^*(2,2,4,10)\), and Liu--Liu prove that this surface is the unique rank-one stable surface attaining \(K_X^2=1/6351\).

The plurigenera are
\[
P_n(X)=h^0\!\left(X,\mathcal O_X(nK_X)\right)
\]
for the rank-one reflexive pluricanonical sheaves. The statement concerns existence and dimension of global sections. It does not assert base-point-freeness or birationality of \(|98K_X|\).

## Proof
Alexeev--Liu describe \(T(a_1,a_2,a_3,a_4)\) as having two cyclic quotient singularities with resolution strings
\[
[2^{a_4-1},a_3,a_1,2^{a_2-1}]
\]
and
\[
[2^{a_3-1},a_2,a_4,2^{a_1-1}].
\]
Substituting \((a_1,a_2,a_3,a_4)=(2,2,4,10)\) gives \(C_{73}\) and \(C_{87}\) above. The standard determinant recursion for a Hirzebruch--Jung string gives
\[
\det C_{73}=73,\qquad \det C_{87}=87.
\]
Deleting the first vertex gives tail determinants \(66\) and \(70\), hence the quotient descriptions
\[
\frac1{73}(1,66),\qquad \frac1{87}(1,70).
\]
For \(\frac1r(1,q)\), the local Cartier index of the canonical divisor is
\[
\frac r{\gcd(r,1+q)}.
\]
Here
\[
\gcd(73,67)=1,\qquad \gcd(87,71)=1,
\]
so the two local canonical indices are \(73\) and \(87\). These are the only singularities, and \(K_X\) is Cartier on the smooth locus, so
\[
\operatorname{ind}(K_X)=\operatorname{lcm}(73,87)=6351.
\]

We next compute the exact plurigenera. Let \(f:Y\to X\) be the minimal resolution and write
\[
f^*K_X=K_Y+B_Y.
\]
For a chain with self-intersection numbers \(-e_i\), write
\[
B_Y=\sum_i b_iE_i.
\]
Since \(f^*K_X\cdot E_j=0\), adjunction gives the linear system
\[
\sum_i b_i(E_i\cdot E_j)=2-e_j.
\]
Solving it on \(C_{73}\) gives
\[
(b_i)=\frac1{73}(6,12,18,24,30,36,42,48,54,60,40,20),
\]
and on \(C_{87}\) gives
\[
(b_i)=\frac1{87}(16,32,48,64,80,40).
\]

Liu--Liu recall Blache's Riemann--Roch correction in the form
\[
\delta_n(X)=\frac12\left(K_Y+\{nB_Y\}\right)\cdot\{nB_Y\}
\]
and, for a klt surface with ample \(K_X\),
\[
P_n(X)
=
\chi(\mathcal O_X)
+\frac{n(n-1)}2K_X^2
+\delta_n(X)
\qquad(n\ge2).
\]
The surface \(X\) is rational, so
\[
\chi(\mathcal O_X)=1,\qquad P_1(X)=p_g(X)=0.
\]
Because the two exceptional configurations are disjoint, \(\delta_n(X)\) is the sum of the two chain contributions. Substituting the two discrepancy vectors above and \(K_X^2=1/6351\) gives exact rational values that are integers after summation. Direct exact evaluation for \(2\le n\le98\) gives the list in the finding: all \(P_n\) vanish for \(2\le n\le10\), \(P_{11}=1\), no \(P_n\) exceeds \(1\) for \(n\le97\), and
\[
P_{98}=2.
\]
Therefore \(11\) and \(98\) are the claimed first thresholds.

## Verification
The accompanying `verify.py` uses exact rational arithmetic only. It reconstructs both intersection matrices, checks their determinants and tail determinants, solves the discrepancy linear systems, computes the local and global canonical indices, evaluates Blache's correction term, and checks every plurigenus from \(n=2\) through \(n=98\).

The script verifies that the complete set of \(n\in[2,97]\) with \(P_n=1\) is exactly the set printed above, that all remaining values in that interval are \(0\), and that \(P_{98}=2\). It also verifies
\[
\operatorname{ind}(K_X)=6351,\qquad \operatorname{ind}(K_X)K_X^2=1.
\]
The saved replay output ends in `VERIFY_OK`.

The finite computation is exhaustive only for the explicitly claimed range \(n\le98\). No extrapolation to the full canonical ring is made.

## Relationship to prior work
Alexeev--Liu construct the surface \(T(2,2,4,10)=S^*(2,2,4,10)\), record its two resolution strings, and compute \(K_X^2=1/6351\). Liu--Liu prove that the surface attaining this minimal rank-one stable volume is unique. They also state Blache's exact plurigenus formula and use computed plurigenus tables as filters in their classification argument.

Neither inspected source states the global canonical index \(6351\), the identity
\[
\operatorname{ind}(K_X)K_X^2=1,
\]
the first positive pluricanonical degree \(11\), or the first degree \(98\) with \(P_n\ge2\). Targeted searches using the surface names, the volume, the two local orders, and the numerical thresholds did not locate these statements.

## Limitations
The calculation determines only the first section-dimension thresholds and the canonical Cartier index. It does not determine generators or relations of the canonical ring, the base locus of \(|nK_X|\), or the smallest \(n\) for which the pluricanonical map is birational.

The surface has appeared in the literature since 2019, so differently phrased or unindexed computations of its canonical ring remain a residual originality risk. Search failure is not treated as proof of novelty.

## References
1. J. Liu and W. Liu, *The minimal volume of stable surfaces of rank one*, arXiv:2605.05641v1, first posted 7 May 2026; primary MSC 14J29.
2. V. Alexeev and W. Liu, *Open surfaces of small volume*, Algebraic Geometry 6 (2019), 312--327; arXiv:1612.09116.
3. R. Blache, *Riemann--Roch theorem for normal surfaces and applications*, Abh. Math. Sem. Univ. Hamburg 65 (1995), 307--340.

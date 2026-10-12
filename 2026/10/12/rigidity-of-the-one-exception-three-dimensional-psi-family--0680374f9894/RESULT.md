# Rigidity of the one-exception three-dimensional PSI family
## Finding
Let \(r,s\in\mathbb Z\setminus\{0\}\). Then the multiset \(\{r^{[8]},s\}\) is permutation-spectrally integral in dimension \(3\) if and only if \(s=r\). Thus the one-exception fully nonzero slice of Cheng--Zhang Conjecture 3.5 is rigid: it contains no nonconstant examples.

## Assumptions and scope
A multiset of nine integers is permutation-spectrally integral in dimension \(3\), abbreviated \(\operatorname{PSI}_3\), when every \(3\times3\) matrix whose entries are exactly that multiset has three integer eigenvalues. The claim concerns precisely the fully nonzero two-value family with one exceptional entry, \(r\neq0\) and \(s\neq0\). It does not settle the general fully nonzero conjecture with several exceptional values.

Cheng and Zhang prove that, for the one-exception family in dimension \(n\), with \(t=s/r\), the \(\operatorname{PSI}_n\) property is equivalent to rational squareness of
\[
(t-(n-1))^2+4(n-1)\qquad\text{and}\qquad 4t+n^2-4.
\]
At \(n=3\), these are \((t-2)^2+8\) and \(4t+5\).

## Proof
Assume first that \(\{r^{[8]},s\}\) is \(\operatorname{PSI}_3\), and put \(t=s/r\in\mathbb Q\). By Cheng--Zhang Theorem 5.2 there are \(u,v\in\mathbb Q\) satisfying
\[
u^2=(t-2)^2+8,\qquad v^2=4t+5.\]
Set \(q=u-(t-2)\). Since \((u-(t-2))(u+(t-2))=8\), one has \(q\neq0\), and
\[
t=2+\frac4q-\frac q2.
\]
Multiplying the second square equation by \(q^2\) gives
\[
(qv)^2=q(-2q^2+13q+16).
\]
With \(X=-2q\) and \(Y=2qv\), this becomes the elliptic curve
\[
E:\quad Y^2=X^3+13X^2-32X,
\]
and
\[
t=\frac{X^2+8X-32}{4X}.
\]
The parameter construction never has \(X=0\).

It remains to determine \(E(\mathbb Q)\). We use the standard two-isogeny descent for a curve \(E_{a,b}:Y^2=X^3+aX^2+bX\) with rational point \((0,0)\) of order two. For a square class \(d\) dividing \(b\), membership in the descent image is equivalent to solubility of
\[
N^2=dM^4+aM^2e^2+(b/d)e^4,
\]
and for the two-isogenous curve
\[
E'_{a,b}:Y^2=X^3-2aX^2+(a^2-4b)X
\]
the two descent images satisfy
\[
2^{\operatorname{rank}E(\mathbb Q)}=\frac{|\alpha(E)|\,|\alpha'(E')|}{4}.
\]

For \(E\), \(a=13\) and \(b=-32\), so the possible square classes are \(\pm1,\pm2\). The points \((4,12)\) and \((-8,24)\) show that \(1\) and \(-2\) occur. The classes \(-1\) and \(2\) are impossible modulo \(3\): in either homogeneous quartic, for primitive \((M,e)\) the right-hand side is always \(2\pmod3\), which is not a square. Hence \(|\alpha(E)|=2\).

The isogenous curve is
\[
E':Y^2=X^3-26X^2+297X.
\]
Its possible square classes are \(\pm1,\pm3,\pm11,\pm33\). Every negative class is impossible over \(\mathbb R\), because all three terms in its homogeneous quartic are negative for a nonzero pair \((M,e)\). The classes \(3\) and \(11\) are impossible modulo \(16\). Indeed, if one of \(M,e\) is odd and the other even, the right-hand side is congruent to \(3\) or \(11\pmod{16}\); if both are odd, it is \(12\pmod{16}\). None is a square modulo \(16\). The identity and the two-torsion point supply the classes \(1\) and \(33\). Thus \(|\alpha'(E')|=2\), and the descent formula gives \(\operatorname{rank}E(\mathbb Q)=0\).

The discriminant of \(E\) has prime divisors only \(2,3,11\), so reduction at \(5\) and \(7\) is good. Direct counting gives
\[
|E(\mathbb F_5)|=|E(\mathbb F_7)|=6.
\]
Good reduction therefore bounds the rational torsion order by \(6\). But the six distinct rational points
\[
O,\ (0,0),\ (4,12),\ (4,-12),\ (-8,24),\ (-8,-24)
\]
already lie on \(E\). Since the rank is zero, these are all rational points.

The parameter construction excludes \(X=0\) and the point at infinity. For \(X=4\) and \(X=-8\), the formula for \(t\) gives \(t=1\). Therefore \(s/r=1\), so \(s=r\).

Conversely, if \(s=r\), the multiset is constant. Every arrangement is the all-\(r\) matrix and has eigenvalues \(3r,0,0\), so it is \(\operatorname{PSI}_3\).

## Verification
The standalone verifier `verify.py` checks the birational parameter formula, the explicit rational points, the modulo-\(3\) and modulo-\(16\) descent obstructions, and the exact point counts modulo \(5\) and \(7\). Its recorded output ends with `CHECK_OK`. The finite computation is supplementary: the rank-zero conclusion uses the standard two-isogeny descent theorem stated in the proof, not a bounded rational-point search.

## Relationship to prior work
Cheng and Zhang define \(\operatorname{PSI}_n\), conjecture that every fully nonzero \(\operatorname{PSI}_3\) multiset is constant, and prove the exact two-square criterion for a one-exception multiset in every dimension. They do not solve the resulting rational-square system in dimension \(3\); their paper instead uses the same criterion to construct nonconstant examples in infinitely many higher dimensions. The result here closes the entire one-exception slice of their three-dimensional conjecture by identifying the associated elliptic curve and determining all of its rational points.

published-finding corpus searches for the claim, its square conditions, the associated elliptic curve, and one-exception \(\operatorname{PSI}_3\) terminology returned no result implying this classification. The closest records concerned unrelated matrix-integrality, spectral, and exceptional-entry phenomena.

## Limitations
This result treats only multisets with eight equal nonzero entries and one possibly different nonzero entry. It does not settle Cheng--Zhang Conjecture 3.5 for general fully nonzero nine-element multisets, nor their two-distinct-exception rational splitting problem. The arithmetic proof relies on the standard two-isogeny descent theorem for elliptic curves with a rational two-torsion point.

## References
1. Shuming Cheng and Siran Zhang, “Square matrices with integer eigenvalues under entry permutations,” arXiv:2609.36524v1, first submitted 2026-09-29. In particular, Definition 2.1, Conjecture 3.5, Theorem 5.2, and Section 6.
2. Joseph H. Silverman and John Tate, *Rational Points on Elliptic Curves*, for standard two-isogeny descent and reduction of torsion at primes of good reduction.

# Minimal prime support in arithmetic-progression Heronian triangles

## Statement

Let \(a<b<c\) be positive integers in a nonconstant arithmetic progression, and suppose the triangle with side lengths \((a,b,c)\) has positive integer area \(K\). Write \(\omega(K)\) for the number of distinct prime divisors of \(K\).

**Theorem.**
\[
\omega(K)=2
\]
if and only if, for some integers \(u,v\ge 0\),
\[
(a,b,c)=(3t,4t,5t),\qquad t=2^u3^v.
\]
Equivalently, the arithmetic-progression Heronian triangles whose area has the minimum possible number of distinct prime divisors are exactly the \(2,3\)-smooth integral scalings of the \(3\)-\(4\)-\(5\) triangle.

In particular, the unique primitive arithmetic-progression Heronian triangle with \(\omega(K)=2\) is
\[
(3,4,5),\qquad K=6.
\]

## Proof

Write the sides as
\[
(b-d,\ b,\ b+d),\qquad d>0.
\]
The triangle inequality is \(2d<b\). Heron's formula gives
\[
K=\frac b4\sqrt{3(b^2-4d^2)}.
\]

If \(b\) were odd, then modulo \(8\) the integer
\[
3b^2(b^2-4d^2)=16K^2
\]
would be congruent to \(3\) when \(d\) is even and to \(7\) when \(d\) is odd, impossible because the right side is divisible by \(8\). Hence \(b=2x\) for some positive integer \(x\), and \(d<x\). Thus
\[
K=x\sqrt{3(x^2-d^2)}.
\]
Since \(K/x\) is rational and its square is an integer, \(K/x\) is an integer. Let
\[
\sqrt{3(x^2-d^2)}=3y.
\]
Then
\[
x^2-d^2=3y^2,\qquad K=3xy. \tag{1}
\]

Set
\[
g=\gcd(x,y),\qquad x=gX,\quad y=gY.
\]
Equation (1) shows \(g\mid d\); write \(d=gD\). We obtain
\[
X^2-D^2=3Y^2,\qquad \gcd(X,Y)=1,\qquad 0<D<X. \tag{2}
\]
If a prime \(r\) divided both \(X\) and \(D\), then \(r^2\mid 3Y^2\). For \(r\ne3\) this contradicts \(\gcd(X,Y)=1\); for \(r=3\) it would force \(9\mid 3Y^2\), again contradicting \(3\nmid Y\). Hence
\[
\gcd(X,D)=1.
\]
Also \(D\) is odd: if \(D\) were even, then \(X\) would be odd and (2) modulo \(4\) would give
\[
1\equiv3Y^2\pmod4,
\]
which is impossible. Therefore
\[
\gcd(2X,D)=1,
\]
so the normalized triangle
\[
(2X-D,\ 2X,\ 2X+D)
\]
is primitive. Its area is \(3XY\), and the original triangle is its integral scaling by \(g\):
\[
K=3g^2XY. \tag{3}
\]

Reducing (2) modulo \(2\), with \(D\) odd, shows that \(X\) and \(Y\) have opposite parity. Thus \(6\mid K\). Therefore the hypothesis \(\omega(K)=2\) means that the only prime divisors of \(K\) are \(2\) and \(3\). By (3), every prime divisor of \(g\), \(X\), and \(Y\) is consequently in \(\{2,3\}\).

Moreover \(3\nmid X\): otherwise (2) modulo \(3\) gives \(3\mid D\), contradicting \(\gcd(X,D)=1\). Hence
\[
X=2^A
\]
for some \(A\ge0\). Since \(0<D<X\), we have \(A\ge1\). Because \(\gcd(X,Y)=1\), it follows that
\[
Y=3^B
\]
for some \(B\ge0\). Equation (2) becomes
\[
D^2=2^{2A}-3^{2B+1}. \tag{4}
\]

If \(B\ge1\) and \(A\ge2\), then the right side of (4) is congruent to
\[
-3\equiv5\pmod8,
\]
which is not a quadratic residue modulo \(8\). If \(B\ge1\) and \(A=1\), the right side is negative. Hence \(B=0\), so
\[
D^2=2^{2A}-3.
\]
Therefore
\[
(2^A-D)(2^A+D)=3.
\]
Both factors are positive integers, so they are \(1\) and \(3\). Their sum gives \(2^{A+1}=4\), hence
\[
A=1,\qquad D=1.
\]
Thus the primitive normalized triangle is \((3,4,5)\).

Finally, (3) and \(\omega(K)=2\) force \(g\) to have no prime factors other than \(2\) and \(3\):
\[
g=2^u3^v.
\]
Conversely, every triangle
\[
(3g,4g,5g),\qquad g=2^u3^v,
\]
is Heronian, is in arithmetic progression, and has area
\[
K=6g^2=2^{2u+1}3^{2v+1},
\]
which has exactly two distinct prime divisors. This proves the theorem.

## Computational check

A standalone exact-integer verification in `artifacts/verify.py` scans every pair
\[
1\le d<x\le3000,
\]
corresponding to 4,498,500 arithmetic-progression side triples with middle side at most \(6000\). It recognizes Heronian cases by testing whether \(3(x^2-d^2)\) is a square, and then independently tests whether the area has prime support exactly \(\{2,3\}\).

The scan finds 6,434 Heronian parameter pairs. Exactly 44 have area supported on two primes, and all 44 are precisely the predicted \(3\)-\(4\)-\(5\) scalings; there are zero mismatches. This finite check is supporting evidence only and is not used in the proof.

## Literature context and originality

MacDougall's treatment of Heronian triangles with sides in arithmetic progression derives the same basic reduction
\[
d^2+3y^2=x^2
\]
and gives a complete two-parameter description of primitive solutions. That general parametrization is prior work and is not claimed here.

Bailey and Gosnell later gave another generation method for all Heronian arithmetic-progression triangles, emphasizing the inradius. A recent article by Read revisits HAP triangles. Current database material also records enumeration by perimeter.

The contribution here is the prime-support rigidity imposed on the area: among all arithmetic-progression Heronian triangles, having the minimum possible number of distinct area primes forces the primitive core to be \(3\)-\(4\)-\(5\), and the full nonprimitive family consists exactly of its \(2,3\)-smooth scalings.

Searches for formulations involving two prime factors, two distinct prime divisors, \(2^a3^b\)-supported area, smooth area, and equivalent arithmetic-progression Heronian descriptions did not locate this classification. **Originality is therefore asserted only to the best of our knowledge.** The principal residual risk is the 2025 paper *On HAP triangles*: its publisher extract and references were inspected, but the full article was not available for inspection here, so an equivalent observation buried in that article cannot be excluded.

## Limitations

The theorem uses the arithmetic-progression hypothesis essentially. It does not classify arbitrary Heronian triangles with \(\omega(K)=2\); for example, primitive Heronian triangles outside this family can have \(2,3\)-smooth area. It also does not classify HAP triangles with three or more distinct prime divisors in their area.

## References

1. J. A. MacDougall, “Heron Triangles With Sides in Arithmetic Progression,” *Journal of Recreational Mathematics* 31, 189–196 (2003). Author-posted full text: https://www.researchgate.net/publication/242732258_Heron_Triangles_With_Sides_in_Arithmetic_Progression
2. H. Bailey and W. Gosnell, “Heronian Triangles with Sides in Arithmetic Progression: An Inradius Perspective,” *Mathematics Magazine* 85 (2012), 290–294. https://doi.org/10.4169/math.mag.85.4.290
3. E. Read, “On HAP triangles,” *The Mathematical Gazette* 109 (2025), 294–302. https://doi.org/10.1017/mag.2025.10079
4. OEIS Foundation Inc., A387908, “Number of distinct integer-sided triangles with perimeter \(6n\) and integer area whose sides are in arithmetic progression.” https://oeis.org/A387908

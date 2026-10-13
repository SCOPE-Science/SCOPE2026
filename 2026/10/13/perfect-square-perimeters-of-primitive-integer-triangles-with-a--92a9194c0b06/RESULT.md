# Perfect-square perimeters of primitive integer triangles with a sixty-degree angle

## Finding
Let \(E(X)\), for real \(X\ge1\), count non-equilateral primitive integer-sided triangles with a \(60^\circ\) angle, without counting side permutations separately, whose perimeter is a perfect square not exceeding \(X\). A triangle is primitive when the greatest common divisor of its three side lengths is one. Then
\[
\boxed{E(X)=\frac{3\log 2}{4\pi^2}\sqrt X+O\bigl(X^{1/4}\log(2X)\bigr)}\qquad(X\to\infty).
\]
In particular, infinitely many such triangles exist, and the leading constant is approximately \(0.05267286958\).

Every qualifying triangle has perimeter \(9(uv)^2\) for a **unique** pair of positive coprime integers \((u,v)\) in exactly one of the following disjoint families:
\[
\begin{array}{ll}
\mathrm I:&3u^2<v^2<6u^2,\quad 3\nmid v,\quad r=3u^2,\quad s=v^2;\\
\mathrm {II}:&u^2<3v^2<2u^2,\quad 3\nmid u,\quad r=u^2,\quad s=3v^2.
\end{array}
\]
For either family, set \(m=r+s\) and \(n=2r-s\). The side lengths adjacent to the sixty-degree angle, arranged as \(a>b\), and the opposite side \(c\) are precisely
\[
\boxed{a=\frac{m^2-n^2}{3},\qquad b=\frac{n(2m-n)}3,\qquad c=\frac{m^2-mn+n^2}3.}
\]
Conversely every admissible \((u,v)\) produces one primitive triangle. In particular, the perimeter of every primitive sixty-degree triangle with square perimeter is divisible by nine.

## Assumptions and scope
All sides are positive integers, triangles are nondegenerate, and the included angle is exactly \(60^\circ\). The ordering \(a>b\) removes duplication. Every non-equilateral sixty-degree triangle has \(a>c>b\). The only primitive equilateral triangle is \((1,1,1)\), whose perimeter three is not square, so excluding it does not change \(E(X)\). The implicit error constant is absolute; no claim is made about whether distinct triangles can have the same perimeter (they can).

## Proof
**1. Unique rational parameter and its normalization.** The law of cosines is \(c^2=a^2-ab+b^2\). For \(a>b\), put \(t=(a+c)/b>2\). Algebra gives
\[
\frac ab=\frac{t^2-1}{2t-1},\qquad \frac cb=\frac{t^2-t+1}{2t-1}.
\]
Write the rational \(t=m/n\) in lowest terms with \(m>2n>0\). Every primitive triangle corresponds uniquely to this reduced pair, up to dividing the following common factor:
\[
A=m^2-n^2,\qquad B=n(2m-n),\qquad C=m^2-mn+n^2.
\]
Indeed the ratios \(A:B:C\) reproduce \(a:b:c\); conversely \(t\) is recovered from the side lengths, which proves injectivity.

The gcd of \(A,B,C\) equals \(d=3\) if \(3\mid m+n\), and \(d=1\) otherwise. To prove this, a common prime divisor of \(A\) and \(B\) cannot divide \(n\) (as \(\gcd(m,n)=1\)); thus it divides \(2m-n\). If this prime is odd and different from three, \(4A\equiv-3n^2\) modulo it is impossible. The prime two cannot divide both \(A\) and \(B\) either, by parity. Therefore any common prime factor must be three, occurring precisely when \(m\equiv-n\pmod3\). In that case \(C=(m+n)^2-3mn\), so \(v_3(C)=1\) because \(3\nmid mn\); the common gcd is exactly three.

**2. The square-perimeter obstruction.** Define \(x=m+n\) and \(y=2m-n\). They satisfy \(0<x<y<2x\), \(x+y=3m\), and \(\gcd(x,y)\mid3\). Direct expansion yields \(A+B+C=xy\), hence the primitive perimeter is \(P=xy/d\).

If \(d=1\), then \(\gcd(x,y)=1\). Were \(P=xy\) square, both \(x\) and \(y\) would be squares, impossible since their sum is divisible by three and two coprime squares cannot sum to zero modulo three. Thus \(d=3\).

Write \(x=3r\), \(y=3s\). Then \(r<s<2r\), \(\gcd(r,s)=1\), \(m=r+s\), \(n=2r-s\), and \(P=3rs\). Conversely, any coprime \(r,s\) in this interval with \(3\nmid r+s\) gives \(\gcd(m,n)=1\) and the normalized triangle above. Finally, since \(r,s\) are coprime, \(3rs\) is square if and only if precisely one of \(r,s\) is three times a square and the other is a square. This gives families I and II, including the displayed exclusions modulo three. In either case \(P=9(uv)^2\), proving the claimed bijection and divisibility statement.

**3. Lattice-point asymptotic.** Put \(Y=\sqrt X/3\). Each family counts coprime positive lattice pairs subject to \(uv\le Y\), one coordinate prime to three, and \(\alpha u<v<\beta u\), with \((\alpha,\beta)=(\sqrt3,\sqrt6)\) in family I and \((\alpha,\beta)=(1/\sqrt3,\sqrt{2/3})\) in family II. Each region has area
\[
\operatorname{area}(Y)=\int_\alpha^\beta\int_0^{\sqrt{Y/t}}w\,dw\,dt
=\frac Y2\log\frac\beta\alpha=\frac{Y\log2}{4}.
\]
For fixed positive \(\alpha<\beta\), elementary slicing at one coordinate shows that the unrestricted lattice-point count differs from the area by \(O_{\alpha,\beta}(\sqrt Y+1)\). Restricting a specified coordinate not to be divisible by three changes the main count to two thirds of the area, with the same error, since among consecutive integers each block of three contains two admissible values. If the specified coordinate is \(u\), slice on \(v\); if it is \(v\), slice on \(u\).

Now use \(\mathbf 1_{\gcd(u,v)=1}=\sum_{d\mid u,\ d\mid v}\mu(d)\). All terms with \(3\mid d\) vanish, and for other \(d\) the region rescales to \(Y/d^2\). The range has \(u,v=O(\sqrt Y)\), so summing the elementary errors yields \(O(\sqrt Y\log(2Y))\), with the tail of the absolutely convergent density series absorbed by the same bound. Its density factor is
\[
\frac23\sum_{\substack{d\ge1\\3\nmid d}}\frac{\mu(d)}{d^2}
=\frac23\prod_{p\ne3}\left(1-\frac1{p^2}\right)
=\frac{3}{4\zeta(2)}.
\]
Thus both families contribute \(\frac{3Y\log2}{16\zeta(2)}+O(\sqrt Y\log(2Y))\). Adding, substituting \(Y=\sqrt X/3\), and using \(\zeta(2)=\pi^2/6\), proves
\[
E(X)=\frac{3\log2}{4\pi^2}\sqrt X+O\bigl(X^{1/4}\log(2X)\bigr).
\]

## Verification
The self-contained stdlib-only script `artifacts/verify_square_perimeter.py` implements the two-family exact bijection and a mathematically independent second enumeration. For square perimeter \(P=q^2\), expanding the cosine law with \(c=P-a-b\) gives the factorization \((2P-3a)(2P-3b)=P^2\). The second implementation enumerates all positive divisor pairs of \(q^4\), reconstructs integral sides, and checks positivity, order, primitivity, and the law of cosines. For \(X=100,1000,10000,100000,1000000,10000000\), both enumerations return respectively \(1,1,6,16,54,165\) triangles and exactly identical side triples. Execute `python3 artifacts/verify_square_perimeter.py` from the directory containing this report. These checks are finite regression tests, not substitutes for the infinite proof.

## Relationship to prior work
Classical results of Gilder and Burn treat integral sixty-degree triangles. Zelator's fully inspected 2008 preprint parametrizes all such triangles; Zimhoni's fully inspected later paper produces their primitive forms via two trees. Gordon and Wells discuss unrestricted perimeter counting, while the OEIS A350038 record tabulates *distinct possible perimeters*. Those results do not state the square-perimeter subfamily's precise coprime two-wedge classification, its factor-of-nine obstruction, or a \(\sqrt X\)-asymptotic with the coefficient and error given here. The existence of a general parametrization does not by itself establish this sparse-subfamily counting law. Primary comparisons and remaining access limitations appear in the scientific review.

## Limitations
Originality remains conditional on the literature searched; in particular, the complete texts of Gordon and Wells (2010), Gordon (2012), and several earlier printed articles were not accessible for full-page comparison. The exact formula does not count all triangles by distinct perimeter, but individual primitive triangles, possibly several with the same perimeter. The proof uses fixed sixty-degree geometry only; it does not establish analogous constants for other angles.

## References
1. J. Gilder, *Integer-sided triangles with an angle of 60°*, Mathematical Gazette 66 (1982), 261–266. DOI: 10.2307/3615511.
2. B. Burn, *Triangles with a 60° angle and sides of integer length*, Mathematical Gazette 87 (2003), 148–153. DOI: 10.1017/S0025557200172377.
3. K. Zelator, *Triangle angles and sides in progression and the diophantine equation x²+3y²=z²*, arXiv:0803.3778, first publicly submitted 2008-03-26. https://arxiv.org/pdf/0803.3778
4. R. A. Gordon and J. M. Wells, *On the perimeter of integral triangles*, International Journal of Pure and Applied Mathematics 64 (2010), no. 4. https://www.ijpam.eu/contents/2010-64-4/5/index.html
5. R. A. Gordon, *Properties of Eisenstein triples*, Mathematics Magazine 85 (2012), 12–25. DOI: 10.4169/math.mag.85.1.12.
6. N. Zimhoni, *A forest of Eisensteinian triplets*, arXiv:1904.11782 (2019). https://arxiv.org/pdf/1904.11782
7. OEIS A350038, *Numbers that are the perimeter of a primitive 60-degree integer triangle*, https://oeis.org/A350038 (recorded 2021).

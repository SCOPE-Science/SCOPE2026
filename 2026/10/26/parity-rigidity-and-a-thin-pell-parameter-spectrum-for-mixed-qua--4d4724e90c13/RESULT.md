# Parity rigidity and a thin Pell-parameter spectrum for mixed quadratic divisibility

## Finding

Consider positive integers \(x,y\) satisfying the asymmetric simultaneous divisibilities
\[
x\mid 2y^{2}+1,\qquad y\mid x^{2}+1.
\]
They are necessarily coprime, \(x\) is odd, and the quantity
\[
 k=\frac{x^{2}+2y^{2}+1}{xy}
\]
is an integer at least \(3\). The complete solution set has the following disjoint description.

**Odd second coordinate.** If \(y\) is odd, necessarily \(k=4\). Conversely, all such solutions are obtained, for \(n\geq0\), by taking the positive integer coefficients \(u_n,v_n\) of
\[
 u_n+v_n\sqrt2=(1+\sqrt2)^{2n+1},\qquad
 y=v_n,\qquad x=2v_n\pm u_n.
\]
Both signs give positive integers. These are precisely the positive integral points of \(x^{2}+2y^{2}+1=4xy\).

**Even second coordinate.** If \(y\) is even, then \(y\equiv2\pmod4\), and \(k\) is odd. Conversely, for each odd \(k\geq3\), put \(D=k^{2}-8\). All solutions having this parameter and even \(y\) are exactly
\[
 y=2t,\quad x=kt\pm s,\quad t\geq1,\quad s\geq0,
 \qquad s^{2}-Dt^{2}=-1.
\]
In this parametrization \(t\) is automatically odd and \(s\equiv0\pmod4\). At \(k=3\) the only solution is \((x,y)=(3,2)\); each solvable odd parameter \(k\geq5\) supplies infinitely many solutions.

Consequently the set \(\mathcal K\) of parameters attained by positive solutions is exactly
\[
\mathcal K=\{4\}\ \cup\ \bigl\{\text{odd }k\geq3:\ \exists s\in\mathbb Z,\ t\geq1,\ s^{2}-(k^{2}-8)t^{2}=-1\bigr\}.
\]
In particular its counting function satisfies, for sufficiently large real \(X\),
\[
\#\{k\in\mathcal K:k\leq X\}
\ll\frac{X}{\sqrt{\log\log X}}.
\]
The implied constant is absolute. Thus the attained conic parameters have natural density zero.

## Assumptions and scope

All divisibilities are in \(\mathbb Z\); \(x,y\) are strictly positive integers, \(k\) is an integer, and every occurrence of a prime is a positive rational prime. The counting bound is asymptotic as \(X\to\infty\) and uses the standard reciprocal-prime Mertens estimate for primes in a fixed reduced progression modulo \(8\). The assertion is an exact classification of pairs through Pell equations, not a closed formula for which individual odd parameters have a negative-Pell solution.

## Proof

**1. Conic reduction and parity.** A common divisor of \(x\) and \(y\) divides \(2y^2+1\), hence divides \(1\). Thus \(\gcd(x,y)=1\). Also \(x\) is odd. The two given congruences are equivalent, by coprimality, to
\[
xy\mid x^2+2y^2+1.
\]
Writing the quotient as \(k\), positivity and \(x^2+2y^2\ge2\sqrt2\,xy\) give \(k\ge3\). Since \(x\) is odd, \(x^2+1\equiv2\pmod8\). Therefore the second divisibility forces \(y\) either odd or congruent to \(2\) modulo \(4\). If \(y\) is odd, then \(x^2+2y^2+1\equiv4\pmod8\), and hence \(k\equiv4\pmod8\). If \(y\) is even, both \(xy\) and the numerator have \(2\)-adic valuation exactly \(1\); therefore \(k\) is odd.

**2. Descent on the odd-coordinate chamber.** For odd \(y\), the two conjugate-root replacements on the fixed conic are
\[
 x'=ky-x=\frac{2y^2+1}{x},\qquad
 y'=\frac{kx}{2}-y=\frac{x^2+1}{2y}.
\]
Both are positive odd integers: integrality of \(x'\) is given, while \(x^2+1\) is divisible by \(2y\) because \(y\) is odd and divides it; each quotient is odd. Replacing \(x\) by \(x'\), or \(y\) by \(y'\), preserves the conic equation, the parameter \(k\), and positivity. Let \(\Delta=x^2-2y^2\). Since \(x,y\) are odd, \(\Delta\equiv-1\pmod8\), so \(\Delta\neq1\). If \(\Delta>1\) then \(x'<x\). If \(\Delta<-1\) then \(y'<y\). In either case the sum of the positive coordinates strictly decreases. The remaining possibility \(\Delta=-1\) gives \(x^2+1=2y^2\); inserting this into the conic yields \(kx=4y\). Since \(\gcd(x,y)=1\) and \(x\) is odd, this forces \(x=1\), hence \(y=1\) and \(k=4\). Thus all descent paths terminate at \((1,1)\), proving \(k=4\). Completing the square gives
\[
 (x-2y)^2-2y^2=-1.
\]
The standard norm-minus-one Pell solution formula in \(\mathbb Z[\sqrt2]\) gives precisely the displayed powers of \(1+\sqrt2\). Both signs of \(x=2y\pm u\) are positive because \(u^2=2y^2-1<4y^2\). Conversely, these points satisfy the conic at \(k=4\) and hence both divisibilities.

**3. Even-coordinate chamber.** Write \(y=2t\), with \(t\) odd. The conic becomes \(x^2+8t^2+1=2kxt\), whence
\[
 (x-kt)^2-(k^2-8)t^2=-1.
\]
Putting \(s=|x-kt|\) proves necessity. Conversely, take odd \(k\ge3\) and an integer solution \(s^2-(k^2-8)t^2=-1\) with \(t\ge1\). Modulo \(4\), \(t\) must be odd; since \(k^2-8\equiv1\pmod8\), reducing modulo \(8\) forces \(s^2\equiv0\pmod8\), hence \(4\mid s\). Moreover \(s^2=k^2t^2-8t^2-1<k^2t^2\), so both \(x=kt\pm s\) are positive odd integers. Their substitution yields \(x^2+2y^2+1=kxy\), which is equivalent to the two divisibilities. If \(k=3\), \(D=1\), and \((t-s)(t+s)=1\) forces \(t=1,s=0\), producing only \((3,2)\). For odd \(k\ge5\), \(D=k^2-8>1\) is nonsquare: if \(D=d^2\), the positive even factors \((k-d)(k+d)=8\) force \(k=3\). A norm-minus-one unit exists by assumption, and its positive odd powers yield infinitely many distinct norm-minus-one solutions, hence infinitely many positive pairs by the formula.

**4. Thinness of the admissible parameters.** Fix a prime \(p\equiv7\pmod8\). The number \(8\) is a nonzero square modulo \(p\), so \(k^2\equiv8\pmod p\) has exactly two residue classes. If an odd admissible \(k\) lay in either, then \(p\mid k^2-8\), and its negative-Pell equation would imply \(s^2\equiv-1\pmod p\), impossible because \(p\equiv3\pmod4\). Hence every such \(p\) excludes two classes of \(k\).

For \(X\) large let \(z=\sqrt{\log X}\), and let \(M\) be the product of primes \(p\le z\) with \(p\equiv7\pmod8\). The Chinese remainder theorem shows that permitted residues modulo \(M\) occupy exactly the fraction \(\prod_{p\mid M}(1-2/p)\). Consequently the number of candidates \(k\le X\) is bounded by
\[
 X\prod_{p\mid M}(1-2/p)+M.
\]
The elementary bound \(M\le z^z\le\sqrt X\) holds for this choice of \(z\) when \(X\) is sufficiently large. The classical Mertens estimate in the progression \(7\pmod8\) gives
\[
 \sum_{\substack{p\le z\\p\equiv7\, (\mathrm{mod}\,8)}}\frac1p
 =\frac14\log\log z+O(1),\qquad
 \prod_{p\mid M}(1-2/p)\ll(\log z)^{-1/2}.
\]
Since \(\log z=\tfrac12\log\log X\), the desired bound follows, after including the single even parameter \(k=4\). This proves the classification and density statement. \(\square\)

## Verification

The standalone standard-library script `check.py` checks all positive pairs up to coordinate \(240\), independently compares divisibility and conic conditions, verifies the parity/Pell split, tests sample Pell-to-divisibility converses, and checks the first six \(7\pmod8\) local exclusions. Its expected terminal line begins `VERIFY_OK`. These tests are finite consistency checks; the infinite classification, infinite Pell families, and density estimate rest on the preceding proofs and the explicitly invoked classical theorems.

## Relationship to prior work

Alekseyev and Khomovsky (2026), Sections 4–5, develop rational gauge reduction of quadratic divisibility chains to fixed conics and analyze a different nonunit quadratic system. The present system is a first asymmetric leading-coefficient example with distinct integral behavior in the two parity chambers, and its exact parameter spectrum is not stated there. Mills (1953) classifies the symmetric monic case, whereas Mills (1956) requires global coefficient divisibility for full integer-root jumping; the coefficient \(2\) in \(x^2+2y^2+1=kxy\) does not divide the \(xy\) coefficient \(1\). Fouvry–Klüners (2010) study negative-Pell solubility over families of discriminants; the present polynomial discriminant family \(k^2-8\) and the derived divisor-pair spectral bound are distinct. Each classical result supplies context or a tool, not the stated combined classification.

## Limitations

The criterion for each odd \(k\) remains the solvability of a specific negative-Pell equation; no elementary congruence-only characterization or matching lower bound is proved. The upper estimate is not asserted optimal. The relation to prior generalized conic classifications is bounded by the primary texts inspected; unindexed special cases or computational tables are a residual priority for independent literature review. No independent mathematical validation is asserted.

## References

1. M. A. Alekseyev and D. I. Khomovsky, *Congruence Jumping in Polynomial Divisibility Systems: Arithmetic Structure and Solution Sets*, arXiv:2610.00808v1 (first posted September 30, 2026), https://arxiv.org/html/2610.00808v1.
2. W. H. Mills, *A System of Quadratic Diophantine Equations*, Pacific Journal of Mathematics 3 (1953), 209–220, https://msp.org/pjm/1953/3-1/pjm-v3-n1-p15-p.pdf.
3. W. H. Mills, *Certain Diophantine Equations Linear in One Unknown*, Canadian Journal of Mathematics 8 (1956), DOI:10.4153/CJM-1956-003-2.
4. É. Fouvry and J. Klüners, *On the Negative Pell Equation*, Annals of Mathematics 172 (2010), 2035–2104, https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n3-p13-p.pdf.

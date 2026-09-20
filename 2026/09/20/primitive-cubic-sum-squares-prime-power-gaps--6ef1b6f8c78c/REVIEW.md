# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**  The proof was checked independently from the finite verification.

The classical Gaussian-integer reduction is valid for primitive positive solutions: coprimality forces opposite parity, so \(x+iy\) and \(x-iy\) are coprime in \(\mathbb Z[i]\); unique factorization then gives the cubic parametrization.  The two formulas for the gap were re-expanded:
\[
A+B=(a-b)(a^2+4ab+b^2),
\]
when \(A=a(a^2-3b^2)<0\), and
\[
A-B=(a+b)(a^2-4ab+b^2)
\]
when \(A>0\).

For the first factorization, with \(u=a-b\),
\[
\gcd\!\left(u,a^2+4ab+b^2\right)=\gcd(u,3).
\]
For the second, with \(s=a+b\) and \(Q=a^2-4ab+b^2\),
\[
\gcd(s,Q)=\gcd(s,3),
\qquad Q\equiv1\pmod4.
\]
These identities are sufficient to force one factor to be \(1\) whenever the gap is an \(\ell\)-power with \(\ell\ne3\), producing respectively \(a=b+1\) and \(Q=1\).

The \(3\)-adic case was checked separately.  If \(3\mid(a-b)\) in the first regime, the second factor has exactly one factor of \(3\) and is too large to equal \(3\).  In the second regime, \(3\mid(a+b)\) implies \(v_3(Q)=1\), while \(Q\equiv1\pmod4\) forces \(Q=-3\).  This reduces the remaining problem to
\[
d^2+2=3^{2r-1}.
\]
The cited Nagell theorem, corroborated by Cohn's historical summary and Sury's later theorem statement, gives only the \(r=2,d=5\) solution for exponent \(>1\), while \(r=1,d=1\) is elementary.

The converse directions were checked: Pell solutions have odd coprime \(s,d\); for \(s>1\), \(s>d>0\), so \((a,b)=((s+d)/2,(s-d)/2)\) are positive, coprime and of opposite parity.  The condition \(Q=1\) then yields the required gap.  In the star branch, \(b\ge2\) is exactly the range in which \(a=b+1\) lies in the \(A<0\) regime.

The standalone exact-integer verification checks all normalized parameter pairs with \(a\le500\), 50,765 pairs in total, and reports zero discrepancies between direct prime-power detection and the theorem.

## Originality

**PASS, to the best of our knowledge.**  The known ingredients were separated from the claimed contribution.

Beukers' 1998 paper was inspected at the relevant passage.  It explicitly factors \(x^2+u^2=z^3\) in \(\mathbb Z[i]\) and obtains
\[
x=a^3-3ab^2,\qquad u=b(3a^2-b^2);
\]
it also places \(\{2,2,k\}\) among the elementary spherical generalized-Fermat signatures.  That parametrization is therefore treated as prior art.

The \(X^2+2=Y^n\) theorem is also prior art.  Cohn's 1993 article states that Nagell proved the \(C=2\) case has no solution beyond \(X=5,Y=3,n=3\), and Sury's 2000 article states the same complete classification for \(n>1\).

Searches were made for exact and synonymous formulations involving \(x^2+y^2=z^3\), primitive solutions, coordinate difference/gap, prime-power difference, the explicit cubic-coordinate formulas, the factors \(a-b\) and \(a+b\), the polynomial \(6b^2+6b+1\), star/centered-dodecagonal numbers, and the Pell equation \(s^2-3d^2=-2\).  No source located the stated prime-power-gap classification or a stronger result that directly implies it.  OEIS A003154 confirms the star-number identification but does not make the Diophantine connection.  The current SCOPE archive was also searched under the equation, Gaussian-integer, prime-power-gap, star-number and Pell formulations without a collision.

Residual risk remains because this is an elementary refinement of a classical parametrization.  An equivalent observation could be buried in older books, theses, problem collections, or literature on spherical generalized-Fermat equations under terminology not captured by the searches.  No concrete evidence of such prior coverage was found.

## Value

**PASS.**  The result is not merely another finite example.  It gives an exact structural classification over an infinite two-parameter family: imposing the arithmetic condition that \(|x-y|\) have only one prime divisor collapses all primitive solutions to two explicit one-parameter mechanisms, plus two exceptional \(3\)-power triples.  The complete exclusion of every other \(3\)-power gap and the star/Pell dichotomy provide reusable structure for subsequent questions about prime, prime-square, or restricted-factor gaps.

## Limitations

The theorem does not determine all \(b\) for which the star number \(6b^2+6b+1\) is a prime power, nor all Pell indices for which \(s\) is a prime power.  It is restricted to primitive positive solutions and to exponent \(3\) on the right side.

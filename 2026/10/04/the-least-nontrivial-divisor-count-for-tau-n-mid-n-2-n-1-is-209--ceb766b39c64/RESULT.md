# The least nontrivial divisor count for \(\tau(n)\mid n^2+n-1\) is \(209\)

## Finding
Let \(\tau(n)\) denote the number of positive divisors of \(n\). Then
\[
\min\{\tau(n):n>1,\ \tau(n)\mid n^2+n-1\}=209=11\cdot19.
\]
Moreover, this minimum is attained infinitely often: for every prime
\[
p\equiv4\pmod{19},
\]
the integer
\[
n=p^{10}31^{18}
\]
has
\[
\tau(n)=209
\qquad\text{and}\qquad
209\mid n^2+n-1.
\]

The first member of this explicit family is obtained from \(p=23\):
\[
23^{10}31^{18}
=
28959352627832366137714333358514333819409.
\]

## Assumptions and scope
A positive integer \(n\) is a \(\tau\)-number relative to a polynomial \(Q(x)\in\mathbb Z[x]\) when
\[
\tau(n)\mid Q(n).
\]
The source paper of Abel, Lauer and Redi studies this notion and lists
\[
Q(x)=x^2+x-1
\]
among type-II polynomials for which a computer search through \(10^8\) found only \(n=1\). Their Open Problem 2 asks for the possible values of \(\tau(n)\) for a fixed polynomial.

The claim here determines the least nontrivial possible value of \(\tau(n)\) for this specific polynomial. It does not classify every possible value of \(\tau(n)\), nor does it claim that the displayed \(41\)-digit integer is the least nontrivial \(n\).

## Proof
Set
\[
Q(x)=x^2+x-1.
\]

First suppose that \(n>1\) and
\[
\tau(n)\mid Q(n).
\]
Since \(n(n+1)\) is even,
\[
Q(n)=n^2+n-1
\]
is odd. Hence \(\tau(n)\) is odd, so \(n\) is a perfect square.

Let \(r\) be a prime divisor of \(\tau(n)\). Then
\[
Q(n)\equiv0\pmod r.
\]
Also \(r\nmid n\), because \(r\mid n\) would give \(Q(n)\equiv-1\pmod r\). Because \(n\) is a square, its residue modulo \(r\) is a nonzero quadratic residue.

For primes \(r<19\), examine whether \(Q(x)\equiv0\pmod r\) has a nonzero quadratic-residue root. For
\[
r\in\{3,7,13,17\},
\]
the discriminant \(5\) is a quadratic nonresidue, so \(Q\) has no root at all. For \(r=5\), the unique root is \(x\equiv2\pmod5\), which is not a quadratic residue. For \(r=11\), by contrast,
\[
Q(3)=11
\]
and \(3\) is a quadratic residue modulo \(11\). Therefore every prime factor of \(\tau(n)\) below \(19\) must be \(11\).

If \(\tau(n)<209=11\cdot19\), it follows that
\[
\tau(n)\in\{11,121\}.
\]

If \(\tau(n)=11\), then the divisor-count factorization forces
\[
n=a^{10}
\]
for some prime \(a\). Since \(11\nmid a\), Fermat's theorem gives
\[
a^{10}\equiv1\pmod{11},
\]
hence
\[
Q(n)\equiv Q(1)\equiv1\pmod{11},
\]
contradicting \(11\mid Q(n)\).

If \(\tau(n)=121=11^2\), then either
\[
n=a^{120}
\]
for a prime \(a\), or
\[
n=a^{10}b^{10}
\]
for distinct primes \(a,b\). None of these primes is \(11\). In both cases Fermat's theorem gives
\[
n\equiv1\pmod{11},
\]
so again
\[
Q(n)\equiv1\pmod{11},
\]
a contradiction.

Thus every nontrivial relative \(\tau\)-number satisfies
\[
\tau(n)\ge209.
\]

It remains to attain \(209\). Let \(p\) be any prime with
\[
p\equiv4\pmod{19},
\]
and define
\[
n=p^{10}31^{18}.
\]
The two prime factors are distinct, so
\[
\tau(n)=(10+1)(18+1)=209.
\]

Modulo \(11\), Fermat's theorem gives \(p^{10}\equiv1\). Also \(31\equiv9\pmod{11}\), and
\[
31^{18}\equiv9^8\equiv3\pmod{11}.
\]
Hence
\[
n\equiv3\pmod{11},
\qquad
Q(n)\equiv Q(3)=11\equiv0\pmod{11}.
\]

Modulo \(19\),
\[
31^{18}\equiv1\pmod{19},
\]
and
\[
p^{10}\equiv4^{10}\equiv4\pmod{19}.
\]
Thus
\[
n\equiv4\pmod{19},
\qquad
Q(n)\equiv Q(4)=19\equiv0\pmod{19}.
\]

Because \(11\) and \(19\) are coprime,
\[
209\mid Q(n).
\]
Dirichlet's theorem gives infinitely many primes \(p\equiv4\pmod{19}\), so the minimum divisor count \(209\) is attained infinitely often.

## Verification
The accompanying `verify.py` checks all finite residue facts used in the lower bound, verifies that \(11\) is the only prime below \(19\) admitting a quadratic-residue root of \(x^2+x-1\), checks the two excluded divisor-count shapes \(11\) and \(121\), and verifies the congruence construction for the first several primes \(p\equiv4\pmod{19}\).

The infinitude assertion uses Dirichlet's theorem and is not inferred from finite computation.

## Relationship to prior work
Abel, Lauer and Redi prove general sufficient conditions for a polynomial to have infinitely many relative \(\tau\)-numbers. Their Theorem 3 can supply an upper-bound construction for \(Q(x)=x^2+x-1\): the residue data \(11,19\) fit its hypotheses. However, that theorem gives no lower bound on possible values of \(\tau(n)\), and therefore does not imply the exact minimum \(209\).

More importantly for the source paper's open problems, the authors explicitly report that their computation through \(10^8\) found only \(n=1\) for \(x^2+x-1\), and Open Problem 2 asks for possible divisor-count values. The exact minimum above identifies the first nontrivial value and explains why their finite search did not encounter the displayed family: its first member already has \(41\) decimal digits.

Targeted searches for the exact polynomial, the divisibility \(\tau(n)\mid n^2+n-1\), the value \(209\), and the residue construction did not locate a published statement of this exact minimum.

## Limitations
The result does not determine the least nontrivial integer \(n\) satisfying the divisibility, only the least possible value of \(\tau(n)\). It also does not classify all larger divisor counts that occur.

Literature non-detection is not a proof that no unindexed note contains the same observation.

## References
1. M. Abel, H. Lauer and E. Redi, “About the number of \(\tau\)-numbers relative to polynomials with integer coefficients,” *Acta et Commentationes Universitatis Tartuensis de Mathematica* 25 (2021), 107–117, DOI 10.12697/ACUTM.2021.25.07.
2. G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, for the standard facts that \(\tau(n)\) is odd exactly when \(n\) is a square and for Dirichlet's theorem on primes in arithmetic progressions.

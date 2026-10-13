# Strict root monotonicity at square arguments of the prime-counting function
## Finding
For every integer \(n\ge3\),
\[
\pi(n^2)^{1/n}>\pi((n+1)^2)^{1/(n+1)}.
\]
Consequently,
\[
\bigl(\pi(n^2)^{1/n}\bigr)_{n\ge3}
\]
is strictly decreasing. This proves Conjecture 2.14(ii) in Sun's paper *Problems on combinatorial properties of primes*.

## Assumptions and scope
Here \(\pi(x)\) denotes the number of primes not exceeding \(x\), and \(\log\) is the natural logarithm.

Two classical explicit estimates are used.

First, the Montgomery--Vaughan form of the Brun--Titchmarsh inequality gives, for \(x\ge1\) and \(y\ge2\),
\[
\pi(x+y)-\pi(x)\le\frac{2y}{\log y}.
\]

Second, Rosser and Schoenfeld proved
\[
\pi(x)>\frac{x}{\log x}
\qquad(x\ge17).
\]

The proof below uses these estimates only for the infinite tail \(n\ge1000\). The finite range \(3\le n\le999\) is checked exhaustively by exact integer arithmetic in the attached verifier.

## Proof
Fix \(n\ge3\), and write
\[
A=\pi(n^2),
\qquad
B=\pi((n+1)^2)=A+d.
\]
The required inequality is equivalent to
\[
B^n<A^{n+1}.
\tag{1}
\]
Since \(A>0\), (1) is in turn equivalent to
\[
n\log\!\left(1+\frac dA\right)<\log A.
\tag{2}
\]

We first prove (2) for every \(n\ge1000\).

The interval from \(n^2\) to \((n+1)^2\) has length
\[
2n+1.
\]
Brun--Titchmarsh therefore gives
\[
d
=
\pi(n^2+2n+1)-\pi(n^2)
\le
\frac{2(2n+1)}{\log(2n+1)}.
\tag{3}
\]

Rosser--Schoenfeld gives
\[
A
>
\frac{n^2}{\log(n^2)}
=
\frac{n^2}{2\log n}.
\tag{4}
\]

For real \(x\ge1000\), the function
\[
\frac{x}{100}-\log x
\]
is increasing because its derivative is
\[
\frac1{100}-\frac1x>0.
\]
At \(x=1000\) it is positive: indeed \(e>2\) implies
\[
e^{10}>2^{10}>1000,
\]
so \(\log1000<10\). Hence
\[
\log n<\frac n{100}
\qquad(n\ge1000).
\tag{5}
\]
Combining (4) and (5),
\[
A>50n\ge50000.
\]
Also \(e<3\), so
\[
e^9<3^9=19683<50000,
\]
and therefore
\[
\log A>9.
\tag{6}
\]

Using \(\log(1+u)<u\) for \(u>0\), together with (3) and (4), we obtain
\[
n\log\!\left(1+\frac dA\right)
<
\frac{nd}{A}
<
\frac{4(2n+1)\log n}{n\log(2n+1)}.
\]
Because
\[
\log n<\log(2n+1),
\]
the last expression is less than
\[
\frac{4(2n+1)}n
=
8+\frac4n
<
9.
\tag{7}
\]
Equations (6) and (7) imply (2). Thus (1) holds for every \(n\ge1000\).

It remains to treat
\[
3\le n\le999.
\]
The attached verifier sieves every prime through \(10^6\), computes
\[
A=\pi(n^2),
\qquad
B=\pi((n+1)^2)
\]
exactly for each of the \(997\) integers in this range, and verifies the integer inequality
\[
B^n<A^{n+1}.
\]
No floating-point comparison is used in this finite closure.

The finite range and the analytic tail together cover every \(n\ge3\), proving the theorem.

## Verification
The attached `verify.py` is a standalone exact check of the finite portion of the proof.

It constructs the complete prime table through
\[
10^6,
\]
forms the exact prefix prime-counting table, and for every
\[
3\le n\le999
\]
checks
\[
\pi((n+1)^2)^n<\pi(n^2)^{n+1}
\]
using arbitrary-precision integers.

It also checks the elementary numerical anchors used to start the analytic tail:
\[
\log1000<10,
\qquad
e<3,
\qquad
3^9<50000.
\]

The finite verifier does not certify the infinite tail by enumeration. That tail follows from the two explicit prime-counting estimates and the symbolic inequalities in the proof.

## Relationship to prior work
Sun stated Conjecture 2.14(ii) in 2014 as the assertion that
\[
\bigl(\pi(n^2)^{1/n}\bigr)_{n\ge3}
\]
is strictly decreasing. The current arXiv revision still presents it as a conjecture. OEIS A038107 records the same conjecture for the sequence
\[
\pi(n^2).
\]

A nearby conjecture in the same paper, Conjecture 2.7(i), compares
\[
\pi(kn)^{1/k}
\quad\text{and}\quad
\pi((k+1)n)^{1/(k+1)}
\]
with the scale \(n\) held fixed. That statement does not imply the square-argument comparison here. Taking \(k=n\) compares \(\pi(n^2)\) with \(\pi(n(n+1))\), whose right argument is smaller than \((n+1)^2\); taking scale \(n+1\) makes the left argument larger than \(n^2\). Neither comparison yields the required inequality.

Targeted searches for the exact conjecture, its square-argument formulation, its equivalent integer-power inequality, and later references to Conjecture 2.14(ii) found the primary paper and OEIS entry but no later proof of the full statement.

## Limitations
The theorem concerns the square arguments \(n^2\) and exponent \(1/n\). It does not prove analogous root monotonicity for \(\pi(n^k)\) at other powers \(k\), nor does it imply Firoozbakht's conjecture for the primes themselves.

The proof uses two established explicit prime-distribution estimates as external lemmas. Their proofs are not reproduced here.

The originality comparison included the primary full text, the exact OEIS entry, targeted exact-phrase and semantic searches, and the closest related monotonicity conjecture in the same source. An equivalent proof in unindexed notes remains a residual risk.

## References
1. Z.-W. Sun, “Problems on combinatorial properties of primes,” arXiv:1402.6641v1, first public 25 February 2014; current revision arXiv:1402.6641v12.
2. H. L. Montgomery and R. C. Vaughan, “The large sieve,” *Mathematika* 20 (1973), 119–134, doi:10.1112/S0025579300004708.
3. J. B. Rosser and L. Schoenfeld, “Approximate formulas for some functions of prime numbers,” *Illinois Journal of Mathematics* 6 (1962), 64–94, doi:10.1215/ijm/1255631807.
4. OEIS Foundation, A038107, the sequence \(\pi(n^2)\).

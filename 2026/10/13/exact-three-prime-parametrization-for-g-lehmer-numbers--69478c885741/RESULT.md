# Exact three-prime parametrization for \(G\)-Lehmer numbers
## Finding
Let \(\Phi\) denote the Gaussian Euler function of Grau, Oller-Marcén, Rodríguez and Sadornil. For odd \(n\), put
\[
\mathcal F(n)=n-\left(\frac{-1}{n}\right),
\]
where the symbol is the Jacobi symbol. A composite integer \(n\) is \(G\)-Lehmer when
\[
\Phi(n)\mid\mathcal F(n).
\]

Every odd \(G\)-Lehmer number with exactly three distinct prime factors actually lies on the equality locus
\[
\Phi(n)=\mathcal F(n).
\]
Moreover, the three-prime layer has an exact finite divisor parametrization.

**Family I.** Choose a prime \(t\equiv3\pmod4\) and a factor pair
\[
de=t^2+t+1,\qquad 1\le d<e,
\]
such that
\[
q=t+1+d,\qquad r=t+1+e
\]
are primes congruent to \(1\pmod4\). Then \(tqr\) is \(G\)-Lehmer, and every three-prime \(G\)-Lehmer number having exactly one prime congruent to \(3\pmod4\) arises uniquely in this way.

**Family II.** Choose a prime \(s\equiv1\pmod4\) and a factor pair
\[
de=s^2-s+1,\qquad 1\le d<e,
\]
such that
\[
p=s-1+d,\qquad q=s-1+e
\]
are primes congruent to \(3\pmod4\). Then \(spq\) is \(G\)-Lehmer, and every three-prime \(G\)-Lehmer number having exactly one prime congruent to \(1\pmod4\) arises uniquely in this way.

Equivalently, if the primes themselves are used as variables, the two equations are
\[
(q-t-1)(r-t-1)=t^2+t+1
\]
and
\[
(p-s+1)(q-s+1)=s^2-s+1.
\]
Thus the proper-divisor question for odd \(G\)-Lehmer numbers cannot first occur at three prime factors: any odd example with
\[
\Phi(n)<\mathcal F(n)
\]
must have at least four distinct prime factors.

## Assumptions and scope
For an odd prime \(p\), write
\[
\beta(p)=\left(\frac{-1}{p}\right)\in\{-1,1\}.
\]
The Gaussian Euler function satisfies
\[
\Phi(p^a)=p^{a-1}(p-\beta(p)),
\]
and it is multiplicative on coprime arguments. For odd \(n\), the comparison function is
\[
\mathcal F(n)=n-\beta(n),
\qquad
\beta(n)=\left(\frac{-1}{n}\right).
\]

The theorem concerns odd composite \(G\)-Lehmer numbers with exactly three distinct prime factors. It does not classify four-prime or higher-support \(G\)-Lehmer numbers, and it does not address even inputs.

## Proof
First, any odd \(G\)-Lehmer number is squarefree. Indeed, if \(p^2\mid n\), then the prime-power formula shows that \(p\mid\Phi(n)\). But \(p\mid n\) while
\[
\mathcal F(n)=n\pm1,
\]
so \(p\nmid\mathcal F(n)\), contradicting \(\Phi(n)\mid\mathcal F(n)\).

Now assume that \(n\) is odd, \(G\)-Lehmer, and has three prime factors. By squarefreeness,
\[
n=pqr
\]
with three distinct odd primes. For each odd prime \(u\),
\[
\frac{u-\beta(u)}u\ge\frac45:
\]
if \(u\equiv1\pmod4\), then \(u\ge5\) and the left side is \(1-1/u\ge4/5\); if \(u\equiv3\pmod4\), the left side is \(1+1/u>1\). Hence
\[
\Phi(n)
=n\prod_{u\mid n}\left(1-\frac{\beta(u)}u\right)
\ge\frac{64}{125}n.
\]
Also \(n\ge3\cdot5\cdot7=105\), and therefore
\[
\mathcal F(n)\le n+1<\frac{128}{125}n\le2\Phi(n).
\]
Since \(\Phi(n)\) is a positive divisor of \(\mathcal F(n)\), the quotient is a positive integer smaller than \(2\). Thus
\[
\Phi(n)=\mathcal F(n).
\tag{1}
\]

Let the three primes be \(p_1,p_2,p_3\), put \(\varepsilon_i=\beta(p_i)\), and define the signed primes
\[
x_i=\varepsilon_i p_i.
\]
Expanding (1), using multiplicativity of the Jacobi symbol, and cancelling the common highest-degree and constant terms gives the symmetric equation
\[
x_1x_2+x_1x_3+x_2x_3=x_1+x_2+x_3.
\tag{2}
\]
All three signs cannot be positive, because then the left side of (2) exceeds the right side; all three cannot be negative, because then the left side is positive and the right side negative. Thus precisely one or precisely two of the signed primes are negative.

Suppose first that the unique negative signed prime is \(-t\), where \(t\equiv3\pmod4\), and the positive signed primes are \(q,r\equiv1\pmod4\). Equation (2) becomes
\[
qr-tq-tr=-t+q+r.
\]
Rearrangement yields
\[
(q-t-1)(r-t-1)=t^2+t+1.
\tag{3}
\]
The two factors on the left have the same sign. They cannot both be negative. Indeed, if they were, then \(q,r\ge5\) would give
\[
0<(t+1-q)(t+1-r)\le(t-4)^2<t^2+t+1,
\]
contradicting (3). Thus both factors are positive. Setting
\[
d=q-t-1,\qquad e=r-t-1
\]
produces Family I. Since the primes are distinct, \(d\ne e\), and ordering them gives \(d<e\). Conversely, expanding (3) recovers (2), hence (1), so every prime triple in Family I is \(G\)-Lehmer.

Suppose instead that the unique positive signed prime is \(s\), where \(s\equiv1\pmod4\), and the negative signed primes are \(-p,-q\) with \(p,q\equiv3\pmod4\). Equation (2) becomes
\[
pq-sp-sq=s-p-q,
\]
and rearrangement gives
\[
(p-s+1)(q-s+1)=s^2-s+1.
\tag{4}
\]
Again the two left factors have the same sign. If both were negative, then \(p,q\ge3\) would imply
\[
0<(s-1-p)(s-1-q)\le(s-4)^2<s^2-s+1,
\]
contradicting (4). Thus both are positive. Setting
\[
d=p-s+1,\qquad e=q-s+1
\]
gives Family II, and the converse follows by reversing the algebra.

This proves the complete three-prime parametrization. The primary source already proves that the two-prime odd \(G\)-Lehmer family also satisfies equality. Consequently, any odd \(G\)-Lehmer number on which \(\Phi(n)\) is a proper divisor of \(\mathcal F(n)\) must have at least four distinct prime factors.

## Verification
The accompanying `verify.py` independently checks the algebraic classification on every product of three distinct odd primes up to
\[
5\,000\,000.
\]
For each such product it computes \(\Phi(n)\) and \(\mathcal F(n)\) exactly, tests the \(G\)-Lehmer divisibility condition, tests the two factorization criteria, and verifies that the two predicates agree.

The check finds exactly the following seven three-prime \(G\)-Lehmer numbers in that range:
\[
255,\ 385,\ 34561,\ 195841,\ 1034881,\ 4070401,\ 4746241.
\]
These agree with the corresponding entries in the published equality sequence. The finite computation is corroborative only; the theorem for all three-prime inputs is proved symbolically above.

## Relationship to prior work
The 2014 primary paper introduces \(G\)-Lehmer numbers by the divisibility condition \(\Phi(n)\mid\mathcal F(n)\). Its Proposition 13 completely treats the two-prime case, where the factors are a special twin-prime pair and equality \(\Phi(n)=\mathcal F(n)\) holds. The paper then lists examples with more than two prime factors and asks whether any \(G\)-Lehmer number can have \(\Phi(n)\) as a proper divisor of \(\mathcal F(n)\). It does not classify the three-prime layer.

OEIS A235864 is the exact database sequence of \(G\)-Lehmer numbers. OEIS A182140 is the earlier exact equality sequence \(\Phi(n)=\mathcal F(n)\), and OEIS A182221 records composite equality cases outside the special two-prime branch. These tables contain the initial examples recovered by the theorem but do not provide a three-prime parametrization or a proof that divisibility forces equality when exactly three primes occur.

Targeted searches for the three-prime formulation, both quadratic factorization identities, the proper-divisor problem, and the exact sequence identifiers located the primary paper and the database entries but no theorem covering this layer. The result therefore supplies the first structural barrier beyond the published two-prime classification: the quotient \(\mathcal F(n)/\Phi(n)\) cannot exceed \(1\) until at least four odd prime factors are present.

## Limitations
The result does not decide whether either divisor-parametrized family is infinite. It does not classify \(G\)-Lehmer numbers with four or more prime factors and does not resolve the global proper-divisor question. It is restricted to odd inputs.

The originality comparison covered the full primary section defining and studying \(G\)-Lehmer numbers, the exact OEIS divisibility and equality sequences, targeted exact-formula searches, and semantic searches for stronger statements. An equivalent argument in unindexed notes remains a residual risk.

## References
1. J. M. Grau, A. M. Oller-Marcén, M. Rodríguez and D. Sadornil, “Fermat test with Gaussian base and Gaussian pseudoprimes,” arXiv:1401.4708v1, first public 19 January 2014; *Czechoslovak Mathematical Journal* 65 (2015), 969–982, doi:10.1007/s10587-015-0221-2.
2. OEIS Foundation, A235864, \(G\)-Lehmer numbers; entry authored 16 January 2014.
3. OEIS Foundation, A182140, integers satisfying \(\Phi(n)=\mathcal F(n)\); entry authored 14 April 2012.
4. OEIS Foundation, A182221, composite equality cases outside the special two-prime branch; entry authored 19 April 2012.

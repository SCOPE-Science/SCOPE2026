# Consecutive-collision rigidity for weighted powers of the divisor sum

## Finding
For a positive integer \(m\), put
\[
\sigma(m)=\sum_{d\mid m}d,\qquad
\tau(m)=\sum_{d\mid m}1,\qquad
F(m)=\sigma(m)^{m-\tau(m)}.
\]
For every integer \(n\ge2\), the following conditions are equivalent:
\[
F(n)=F(n+1),
\]
and
\[
\sigma(n)=\sigma(n+1)\quad\text{and}\quad \tau(n+1)=\tau(n)+1.
\]
If they hold, the common divisor sum is odd and, for some positive integers \(x,y\), the pair \((n,n+1)\) is either \((x^2,2y^2)\) or \((2y^2,x^2)\), with \(x^2-2y^2=\pm1\). Thus the number of collisions starting at \(n\le X\) is \(O(\log X)\); in fact for \(X\ge2\) it is at most
\[
\left\lfloor\frac{\log(2\sqrt{X+1})}{\log(1+\sqrt2)}\right\rfloor.
\]
The endpoint \(n=1\) is different: \(F(1)=F(2)=1\) because both exponents vanish.

## Assumptions and scope
All functions are ordinary positive-integer divisor functions. Exponentiation is integer exponentiation with the convention that any positive base to exponent zero is \(1\). The equivalence is unconditional for every integer \(n\ge2\). It does not resolve the conjecture from OEIS A236288 that \(n=1\) is the only consecutive collision.

## Proof
Write
\[
a=n-\tau(n),\quad b=n+1-\tau(n+1),\quad A=\sigma(n),\quad B=\sigma(n+1).
\]
For \(n\ge10000\), the familiar bound \(\tau(m)\le2\sqrt m\), obtained by pairing divisors, gives \(a,b>0\). Suppose \(A^a=B^b\). We show \(a=b\).

Assume instead \(a\ne b\) and put \(g=\gcd(a,b)\), \(r=a/g\), \(s=b/g\). Unique prime factorization, together with \(\gcd(r,s)=1\), gives an integer \(C\ge2\) with
\[
A=C^s,\qquad B=C^r.
\]
In particular \(s\le\log_2 A\). On the other hand,
\[
g\le|a-b|=|\tau(n+1)-\tau(n)-1|\le1+4\sqrt{n+1}.
\]
With \(t=\sqrt{n+1}\), we have \(b\ge t^2-2t\), so
\[
s=\frac bg\ge\frac{t(t-2)}{1+4t}>\frac t5-1.
\]
For the opposite bound, divisor complementation gives
\[
A=n\sum_{d\mid n}\frac1d\le n\sum_{j=1}^n\frac1j\le n(1+\log n),
\]
hence
\[
s\le\log_2 A\le\log_2\bigl(n(1+\log n)\bigr).
\]
For every \(n\ge10000\), the rightmost quantity is strictly below \(\sqrt{n+1}/5-1\). Indeed, at \(n=10000\) the former is less than \(17\) while the latter is greater than \(19\); the derivative of the latter is \(1/(10\sqrt{n+1})\), and the derivative of the former is at most \(3/n\). The derivative comparison follows because \(n>30\sqrt{n+1}\) for all \(n\ge10000\). This contradicts the two bounds on \(s\). Therefore \(a=b\), hence \(A=B\). Rewriting \(a=b\) gives \(\tau(n+1)=\tau(n)+1\).

For the finite interval \(2\le n<10000\), the exact divisor sieve in `verify.py` checks all pairs using integer arithmetic, and the separately implemented `verify_valuations.py` compares prime valuations. Both find no collision in this interval. Therefore the forward implication holds throughout \(n\ge2\). The reverse implication follows immediately by substituting the two equalities into the definition of \(F\).

Now suppose the equivalent conditions hold. Exactly one of the consecutive divisor counts \(\tau(n),\tau(n+1)\) is odd, so exactly one of \(n,n+1\) is a perfect square. A classical parity criterion, proved by factoring \(\sigma(p^k)\) modulo \(2\), says \(\sigma(m)\) is odd precisely when \(m\) is a square or twice a square. We must show the common divisor sum is odd: this follows from the square member because \(\sigma(x^2)\) is odd. Then both members are squares or twice squares; the nonsquare member is twice a square. It is even, so the square member is odd. Consequently \(x^2-2y^2=\pm1\), with the sign specifying the order.

All positive solutions of either Pell equation are given by
\[
x+y\sqrt2=(1+\sqrt2)^j,\qquad j\ge1.
\]
The index \(j=1\) gives the excluded pair \((1,2)\); any \(n\ge2\) uses \(j\ge2\). If \(n\le X\), both numbers in the pair are at most \(X+1\), giving
\[
(1+\sqrt2)^j=x+y\sqrt2\le2\sqrt{X+1}.
\]
There is at most one possible consecutive starting index for each \(j\), so counting the admissible Pell indices proves the displayed logarithmic bound.

## Verification
Run `python3 verify.py` and `python3 verify_valuations.py` from the directory containing the embedded scripts. Both are standard-library-only Python 3 programs. The first exactly computes \(\sigma\), \(\tau\), and the complete finite interval \(1\le n<10000\), using a necessary integer perfect-power condition to skip impossible expensive power evaluations. The second independently factors divisor sums and checks all prime-exponent equalities, without taking logarithms or constructing enormous powers. Successful outputs are `VERIFY_OK` and `VALUATION_VERIFIED [1] range 9999`. The sole small collision is \(n=1\).

The unbounded portion of the proof is symbolic, using divisor bounds and the strict derivative comparison. The finite checks are confined to the explicitly stated interval.

## Relationship to prior work
OEIS A236288 (entry authored 23 January 2014) defines exactly the function \(F\), records the consecutive-collision conjecture, and notes that its stronger global injectivity conjecture is false: nonconsecutive indices can share a value when both their exponents and divisor sums coincide. The entry does not state that these equalities are necessary for consecutive collisions beyond the finite range. This theorem proves that necessity and yields an unconditional counting bound.

Lourdes Benito, arXiv:0707.2190v1 (15 July 2007), Theorem 3, proves that a consecutive pair with equal **odd** divisor sums must lie on one of the two Pell equations. That Pell observation is prior work and not claimed here as original. The new part is ruling out unequal positive exponents in the weighted power equality for all sufficiently large indices, combining it with a complete finite endpoint, and thereby imposing the odd-divisor-sum Pell restriction on every possible nontrivial powered collision.

OEIS A002961 records consecutive equal ordinary divisor sums, without the additional divisor-count condition. Published mathematical results on five-term constant *proper*-divisor sums, and on equal divisor sums of two-almost-prime neighbors, do not imply this weighted-power equivalence.

## Limitations
The theorem does not prove that no nontrivial consecutive collision exists. The Pell sieve is a necessary condition only: most Pell candidates need not have equal divisor sums or the required divisor-count difference. The logarithmic upper bound is not a count of actual solutions. No new statement is made about nonconsecutive collisions.

## References
1. OEIS Foundation, A236288, “\(\sigma(n)^{n-\tau(n)}\)”, first authored 23 January 2014. https://oeis.org/A236288
2. L. Benito, “Solutions of the problem of Erdős–Sierpiński: \(\sigma(n)=\sigma(n+1)\)”, arXiv:0707.2190v1, 15 July 2007, Theorem 3. https://arxiv.org/html/0707.2190v1
3. OEIS Foundation, A002961, “Numbers \(k\) such that \(k\) and \(k+1\) have same sum of divisors.” https://oeis.org/A002961

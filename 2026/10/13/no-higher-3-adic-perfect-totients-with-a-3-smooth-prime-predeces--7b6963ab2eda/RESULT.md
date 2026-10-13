# No higher-\(3\)-adic perfect totients with a \(3\)-smooth prime predecessor
## Finding
Let \(k\ge2\) and let \(p>3\) be prime. Suppose
\[
p-1=2^a3^b
\]
with integers \(a\ge1\) and \(b\ge0\). Then
\[
3^k p
\]
is not a perfect totient number.

In fact, the full classification in this subclass is
\[
3^k p\text{ is perfect totient}
\quad\Longleftrightarrow\quad
k=1,\ a=2,
\]
with \(p=4\cdot3^b+1\) prime. The positive \(k=1\) branch is the classical Venkataraman family; the new content is that every higher \(3\)-adic layer is empty when \(p-1\) has no prime factors other than \(2\) and \(3\).

## Assumptions and scope
For \(n>2\), let \(\varphi\) denote Euler's totient function and define
\[
S(n)=\varphi(n)+\varphi^2(n)+\cdots+1,
\]
where iteration stops at \(1\). A perfect totient number is an integer \(n\) satisfying
\[
S(n)=n.
\]

The theorem concerns the prime-cofactor family \(3^k p\) under the structural hypothesis that
\[
p-1=2^a3^b.
\]
It does not rule out perfect totient numbers \(3^k p\) when \(p-1\) has a prime divisor at least \(5\).

## Proof
We first evaluate the complete totient tail of a \(3\)-smooth integer. For integers \(A\ge1\) and \(B\ge0\), put
\[
H(A,B)=2^A3^B+\varphi(2^A3^B)+\varphi^2(2^A3^B)+\cdots+1.
\]
While the exponent of \(3\) is positive, successive totients are
\[
2^A3^B,
2^A3^{B-1},
\ldots,
2^A.
\]
After that, the tail is
\[
2^{A-1},2^{A-2},\ldots,2,1.
\]
Therefore
\[
\begin{aligned}
H(A,B)
&=2^A\left(3^B+3^{B-1}+\cdots+1\right)+(2^A-1)\\
&=2^{A-1}\left(3^{B+1}+1\right)-1.
\end{aligned}
\tag{1}
\]

Now let
\[
n=3^k p,
\qquad
p-1=2^a3^b.
\]
Since \(p\ne3\), multiplicativity gives
\[
\varphi(n)
=\varphi(3^k)\varphi(p)
=2^{a+1}3^{k+b-1}.
\]
Using (1) with \(A=a+1\) and \(B=k+b-1\),
\[
S(n)=2^a\left(3^{k+b}+1\right)-1.
\tag{2}
\]
On the other hand,
\[
n=3^k\left(2^a3^b+1\right)
=2^a3^{k+b}+3^k.
\tag{3}
\]
Equating (2) and (3), the perfect-totient condition is equivalent to
\[
2^a-1=3^k,
\]
or
\[
2^a=3^k+1.
\tag{4}
\]

Equation (4) has only one solution with \(a\ge1\) and \(k\ge1\). If \(k\) is even, then
\[
3^k\equiv1\pmod8,
\]
so
\[
2^a\equiv2\pmod8,
\]
forcing \(a=1\); equation (4) would then give \(3^k=1\), impossible. If \(k\) is odd, then
\[
3^k\equiv3\pmod8,
\]
so
\[
2^a\equiv4\pmod8,
\]
forcing \(a=2\). Equation (4) then gives
\[
3^k=3,
\]
hence \(k=1\).

Thus no solution exists for \(k\ge2\). When \(k=1\) and \(a=2\), equation (2) equals (3) for every \(b\ge0\) for which \(p=4\cdot3^b+1\) is prime. This proves the stated classification.

## Verification
The attached checker independently verifies three finite consequences of the proof using exact integer arithmetic.

First, for a rectangle of values \(A\) and \(B\), it computes the actual iterated-totient tail and compares it with
\[
2^{A-1}\left(3^{B+1}+1\right)-1.
\]

Second, it enumerates many primes of the form
\[
p=2^a3^b+1
\]
and directly evaluates the iterated totient sum of \(3^k p\). In the tested range it finds perfect-totient equality only on the \(k=1,a=2\) branch.

Third, it checks the reduction to
\[
2^a=3^k+1
\]
over a much larger exponent box and finds only \((a,k)=(2,1)\).

These computations are corroborative. The universal result follows from the exact formulas and the modulo-\(8\) argument above.

## Relationship to prior work
Iannucci, Moujie, and Cohen made the family \(3^k p\) the central subject of their 2003 paper. They completely describe the \(k=1\) case through earlier work and investigate higher layers by imposing nested prime-predecessor chains such as
\[
p=2^c3^d q+1,
\qquad
q=2^a3^b+1.
\]
Their Theorem 5 excludes \(k\ge4\) in that nested two-prime-predecessor setting, and the paper explicitly leaves the unrestricted existence problem for \(3^k p\), \(k\ge4\), open.

The present theorem treats a different endpoint of the predecessor tree: there is no extra prime \(q\); instead
\[
p-1=2^a3^b.
\]
Consequently the prior nested-chain theorem does not specialize to this case. A 2009 sequel treats still longer nested prime chains and likewise does not include the \(3\)-smooth predecessor endpoint.

A previously published support sieve for \(3^k p\) with
\[
p-1=2^a3^b u,
\qquad
\gcd(u,6)=1,
\]
requires a lower bound on \(\varphi(u)/u\). At the present endpoint \(u=1\), that condition is automatically satisfied and therefore gives no exclusion. The exact calculation here supplies the missing conclusion.

OEIS A082897 records the ambient perfect-totient sequence and the classical primes \(p=4\cdot3^b+1\) giving the \(k=1\) family. A finite term table does not imply the uniform nonexistence theorem for all \(k\ge2\).

## Limitations
The theorem uses the strong structural hypothesis that \(p-1\) is \(3\)-smooth. It does not resolve the general open problem of whether a perfect totient \(3^k p\) exists for \(k\ge4\).

The literature comparison included the complete seven-page 2003 primary article, the relevant formulation and main theorem of the 2009 sequel, the exact OEIS sequence, and targeted searches for the displayed predecessor condition and its equivalent equation. A 2006 master's thesis with an abstract announcing additional forms of perfect totient numbers was identified, but its full-text download was access-blocked; its repository abstract was inspected and exact-form searches did not surface the theorem proved here. This remains a residual originality risk.

## References
1. D. E. Iannucci, D. Moujie, and G. L. Cohen, “On Perfect Totient Numbers,” *Journal of Integer Sequences* 6 (2003), Article 03.4.5; published 18 December 2003.
2. M. Deng, “A Note On Perfect Totient Numbers,” *Journal of Integer Sequences* 12 (2009), Article 09.6.2.
3. OEIS Foundation, A082897, “Perfect totient numbers.”
4. T. Venkataraman, “Perfect totient number,” *The Mathematics Student* 43 (1975), 178.

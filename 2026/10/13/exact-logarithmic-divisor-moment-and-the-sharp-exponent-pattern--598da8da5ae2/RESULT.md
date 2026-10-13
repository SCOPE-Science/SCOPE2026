# Exact logarithmic divisor moment and the sharp exponent-pattern envelope
## Finding
For
\[
n=\prod_{i=1}^r p_i^{a_i}>1,
\]
with distinct primes \(p_i\) and positive integers \(a_i\), write
\[
\tau(n)=\prod_{i=1}^r(a_i+1)
\]
and define
\[
P_3(n)=\prod_{d\mid n} d^{\log d},
\]
where \(\log\) is the natural logarithm. Then
\[
\log P_3(n)=\frac{\tau(n)}4(\log n)^2+
\frac{\tau(n)}{12}\sum_{i=1}^r a_i(a_i+2)(\log p_i)^2.
\]

If
\[
B(a_1,\ldots,a_r)=\sum_{i=1}^r\frac{a_i}{a_i+2},
\]
then
\[
\log P_3(n)\ge
\left(\frac14+\frac{1}{12B(a_1,\ldots,a_r)}\right)
\tau(n)(\log n)^2.
\]
For \(r=1\) equality holds. For each fixed exponent vector with \(r\ge2\), the coefficient is the exact infimum over all choices of distinct primes, but the infimum is not attained.

Two useful specializations are
\[
\frac{\log P_3(p^a)}{\tau(p^a)(\log p^a)^2}=\frac13+\frac{1}{6a}
\]
for prime powers, and, for squarefree integers with exactly \(r\) prime factors,
\[
\frac{\log P_3(n)}{\tau(n)(\log n)^2}>\frac{r+1}{4r}
\]
when \(r\ge2\), with \((r+1)/(4r)\) the sharp infimum for that squarefree layer.

## Assumptions and scope
The theorem concerns positive integers \(n>1\) and the product \(P_3\) introduced in the cited 2024 paper. Prime factors are distinct and exponents are positive. The sharpness statement fixes the exponent vector and varies the distinct prime bases. No asymptotic assertion about the distribution of integers is made.

## Proof
Choose a divisor of \(n\) uniformly. It has the unique form
\[
D=\prod_{i=1}^r p_i^{J_i},
\]
where the random variables \(J_i\) are independent and uniform on \(\{0,1,\ldots,a_i\}\). Hence
\[
\mathbb E J_i=\frac{a_i}{2},
\qquad
\operatorname{Var}(J_i)=\frac{a_i(a_i+2)}{12}.
\]
Writing \(X=\log D\), independence gives
\[
\mathbb E X=\frac12\log n
\]
and
\[
\operatorname{Var}(X)=\frac1{12}
\sum_{i=1}^r a_i(a_i+2)(\log p_i)^2.
\]
Because every divisor occurs once,
\[
\log P_3(n)=\sum_{d\mid n}(\log d)^2
=\tau(n)\,\mathbb E(X^2).
\]
Using \(\mathbb E(X^2)=(\mathbb E X)^2+\operatorname{Var}(X)\) proves the exact identity.

For the lower envelope, set
\[
Q=\sum_{i=1}^r a_i(a_i+2)(\log p_i)^2,
\qquad
B=\sum_{i=1}^r\frac{a_i}{a_i+2}.
\]
Cauchy--Schwarz gives
\[
(\log n)^2
=\left(\sum_i a_i\log p_i\right)^2
\le QB,
\]
so \(Q\ge(\log n)^2/B\), which yields the displayed bound.

Equality in Cauchy--Schwarz requires
\[
(a_i+2)\log p_i
\]
to be independent of \(i\). Equivalently, all numbers \(p_i^{a_i+2}\) would be equal. This is impossible for two distinct primes, so equality in the bound occurs exactly in the one-prime case.

It remains to prove optimality for a fixed exponent vector. Let \(T\to\infty\). Choose real targets whose logarithms are
\[
\frac{T+c_i}{a_i+2},
\]
with fixed constants \(c_i\) selected so that targets belonging to equal exponents have disjoint doubling intervals. For unequal exponents the corresponding scales are eventually exponentially separated. Bertrand's postulate supplies a prime in each doubling interval; call it \(p_i(T)\). The primes can therefore be chosen distinct and satisfy
\[
(a_i+2)\log p_i(T)=T+O(1).
\]
Consequently the Cauchy--Schwarz quotient tends to equality, so the coefficient is the infimum. For \(r\ge2\) it is not attained by the preceding equality analysis.

For squarefree integers, every \(a_i=1\), so \(B=r/3\), which gives \((r+1)/(4r)\). For a prime power, \(B=a/(a+2)\), giving \(1/3+1/(6a)\).

## Verification
A standalone verifier directly enumerates all divisors for every \(2\le n\le20000\), compares the direct value \(\sum_{d\mid n}(\log d)^2\) with the factorization formula, checks the exponent-pattern bound, and checks equality for prime powers versus strictness for integers with at least two distinct prime factors. It also checks the squarefree coefficient formula for support sizes \(1\) through \(8\). The largest observed absolute floating-point discrepancy in the exact identity is below \(5\times10^{-13}\). This finite computation is regression evidence only; the proof above is symbolic and unbounded.

## Relationship to prior work
Sándor defines \(P_3(n)=\prod_{d\mid n}d^{\log d}\) and proves
\[
\frac14\tau(n)(\log n)^2<\log P_3(n)\le\frac12\tau(n)(\log n)^2
\]
for \(n>1\). The cited paper also records the upper-end limsup \(1/2\). It does not give a prime-factor formula for the second logarithmic divisor moment, nor an exponent-pattern sharp lower coefficient. The present identity identifies the exact variance term that is discarded by the mean-square lower bound and optimizes it at fixed exponent pattern.

A 1997 paper by Tóth and Sándor with a similar title was inspected because it studies arithmetical products and regular convolutions. Its products are built from trigonometric and gamma functions and generalized von Mangoldt functions; it does not study the product \(\prod_{d\mid n}d^{\log d}\) or the divisor-logarithm moment above.

## Limitations
The originality check found no source stating the combined exact identity and sharp fixed-exponent infimum. The second-moment identity is elementary once the divisor exponents are viewed as independent uniform variables, and an equivalent formula could exist in literature on random divisors or derivatives of generalized divisor sums under different notation. The claim therefore concerns the explicit identity together with its sharp exponent-pattern optimization and its relationship to Sándor's \(P_3\) inequality; it does not claim that the underlying variance computation is a new probabilistic technique.

## References
1. J. Sándor, “On certain arithmetical products involving the divisors of an integer,” *Notes on Number Theory and Discrete Mathematics* 30 (2024), 111–115, DOI 10.7546/nntdm.2024.30.1.111-115. Online First: 2024-03-06.
2. L. Tóth and J. Sándor, “On certain arithmetical products involving regular convolutions,” *Notes on Number Theory and Discrete Mathematics* 3 (1997), 159–166.

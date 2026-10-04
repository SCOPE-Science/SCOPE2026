# Exact two-prime-support criterion and density for strong Achilles numbers
## Finding
Fix an odd prime \(p\), and factor
\[
p-1=2^t\prod_{j=1}^r q_j^{c_j},
\]
with \(t\ge1\), distinct odd primes \(q_j\), and an empty product if \(p-1\) is a power of \(2\). Then \(2^a p^b\) is a strong Achilles number exactly when
\[
a\ge2,\quad b\ge3,\quad \gcd(a,b)=1,
\]
every \(c_j\ge2\), and
\[
\gcd(a+t-1,b-1,c_1,\ldots,c_r)=1.
\]
For an empty odd part the last condition is \(\gcd(a+t-1,b-1)=1\).

Thus the support \(\{2,p\}\) occurs at all if and only if the odd part of \(p-1\) is powerful, where \(1\) is allowed. Whenever it occurs, it occurs infinitely often. Let \(F_p(X)\) count the strong Achilles numbers of this support up to \(X\). If the odd part of \(p-1\) is not powerful then \(F_p(X)=0\). If \(p-1\) is a power of \(2\), then
\[
F_p(X)\sim \frac{C_*}{2\log 2\,\log p}(\log X)^2,
\qquad
C_*:=\prod_{\ell\ \mathrm{prime}}\left(1-\frac{2}{\ell^2}\right).
\]
If the odd part is nontrivial and powerful, write \(g=\gcd(c_1,\ldots,c_r)\). Then
\[
F_p(X)\sim \frac{C_p}{2\log 2\,\log p}(\log X)^2,
\qquad
C_p:=\frac{1}{\zeta(2)}\prod_{\ell\mid g}\frac{\ell^2-2}{\ell^2-1}.
\]

## Assumptions and scope
A positive integer is powerful when every prime in its factorization occurs with exponent at least \(2\). It is an Achilles number when it is powerful but not a perfect power. A strong Achilles number is an integer \(n\) for which both \(n\) and Euler's totient \(\varphi(n)\) are Achilles numbers. The result concerns exactly two prime supports containing \(2\), namely \(n=2^a p^b\) with a fixed odd prime \(p\). It does not classify supports containing two odd primes, supports of larger size, or the global counting function over varying \(p\).

## Proof
For any integer with prime factorization \(\prod_i r_i^{e_i}\), powerfulness is equivalent to \(e_i\ge2\) for every \(i\), while being a perfect power is equivalent to \(\gcd_i e_i>1\). Therefore
\[
2^a p^b\text{ is Achilles}\iff a,b\ge2\text{ and }\gcd(a,b)=1.
\]

Using the displayed factorization of \(p-1\),
\[
\varphi(2^a p^b)=2^{a-1}p^{b-1}(p-1)
=2^{a+t-1}p^{b-1}\prod_{j=1}^r q_j^{c_j}.
\]
The primes in this factorization are distinct: no \(q_j\) equals \(2\) or \(p\). Hence \(\varphi(2^a p^b)\) is powerful exactly when
\[
a+t-1\ge2,\qquad b-1\ge2,
\qquad c_j\ge2\ \text{for all }j.
\]
Under \(a\ge2\) and \(t\ge1\), the first inequality is automatic. Thus the new requirements are precisely \(b\ge3\) and \(c_j\ge2\) for all \(j\). The same exponent criterion says that this totient is not a perfect power exactly when
\[
\gcd(a+t-1,b-1,c_1,\ldots,c_r)=1.
\]
Combining the two Achilles conditions proves the exact classification.

It remains to count exponent pairs. Put \(L=\log X\), \(\alpha=\log2\), and \(\beta=\log p\). Ignoring the fixed lower bounds on \(a,b\), which changes the count by only \(O(L)\), the admissible exponent pairs lie in the triangle
\[
\alpha a+\beta b\le L,
\]
whose lattice-point count is asymptotic to \(L^2/(2\alpha\beta)\).

First suppose the odd part of \(p-1\) is nontrivial and powerful, and put \(g=\gcd(c_1,\ldots,c_r)\). For each prime \(\ell\nmid g\), the condition \(\gcd(a,b)=1\) excludes the single residue pair \((a,b)\equiv(0,0)\pmod\ell\), giving local density \(1-1/\ell^2\). For each prime \(\ell\mid g\), the second gcd additionally excludes
\[
(a,b)\equiv(1-t,1)\pmod\ell.
\]
These two forbidden pairs are distinct because their second coordinates are \(0\) and \(1\). The local density is therefore \(1-2/\ell^2\). Chinese remaindering over any finite set of primes gives the product of these local densities. The contribution of omitted primes larger than \(y\) is at most a constant multiple of \(\sum_{\ell>y}\ell^{-2}\), uniformly after normalizing by the area of the expanding triangle. Letting first \(L\to\infty\) and then \(y\to\infty\) gives
\[
C_p=\prod_{\ell\nmid g}\left(1-\frac1{\ell^2}\right)
\prod_{\ell\mid g}\left(1-\frac2{\ell^2}\right)
=\frac1{\zeta(2)}\prod_{\ell\mid g}\frac{\ell^2-2}{\ell^2-1}.
\]

If \(p-1\) is a power of \(2\), the two gcd conditions \(\gcd(a,b)=1\) and \(\gcd(a+t-1,b-1)=1\) apply at every prime. At each \(\ell\) they exclude the same two distinct residue pairs as above, so the limiting density is
\[
C_* = \prod_{\ell}\left(1-\frac2{\ell^2}\right)>0.
\]
Multiplying the appropriate density by the triangle area proves both asymptotic formulas. Positivity of the Euler products also proves infinitude on every admissible support.

## Verification
The accompanying checker independently factors integers and their totients, tests the definition of a strong Achilles number, and compares it against the criterion for every odd prime \(p<200\) and all \(2\le a,b\le18\). It performs \(13005\) direct exponent-pair comparisons. It also checks all \(21\) exact-two-prime-support terms occurring in the displayed OEIS A194085 prefix through \(135000\), and numerically approximates \(C_*\) using primes through \(100000\), obtaining approximately \(0.322634616605\). These finite computations test formulas and boundary cases; they are not substitutes for the proof of the infinite classification or asymptotic.

## Relationship to prior work
Project Euler Problem 302 introduced strong Achilles numbers publicly in 2010 and supplied benchmark counts below \(10^4\) and \(10^8\). OEIS A194085 records the sequence and definition-level programs. A detailed public solution explains the general exponent-vector criterion for Achilles numbers and the contribution of the factors \(p_i-1\) to the exponents in \(\varphi(n)\). Those general ingredients already imply the exact support classification after specialization to \(2^a p^b\), so that classification component is not treated as independent novelty here. The added assertion assessed for originality is the support-wise quadratic logarithmic asymptotic with its explicit Euler-product constant (and the resulting quantitative infinitude law). Focused searches for that asymptotic formulation or a stronger implication did not locate a matching statement.

## Limitations
The theorem is restricted to exact support \(\{2,p\}\). The asymptotic keeps \(p\) fixed while \(X\to\infty\); it is not uniform in \(p\) and does not yield the global density of strong Achilles numbers. The originality check is necessarily limited by discoverability: strong Achilles numbers have substantial recreational and implementation-oriented discussion, so an equivalent unindexed derivation may exist. No claim is made about historical priority beyond the inspected and searched sources.

## References
1. Project Euler, Problem 302, “Strong Achilles Numbers,” published 2010-09-18: https://projecteuler.net/problem=302
2. OEIS A194085, “Strong Achilles numbers”: https://oeis.org/A194085
3. Quant Academy mirror of Project Euler Problem 302, recording the original publication date 2010-09-18: https://quantacademy.art/euler/problem-302
4. EulerSolve, “Problem 302: Strong Achilles Numbers,” detailed mathematical approach: https://eulersolve.org/problem/302/

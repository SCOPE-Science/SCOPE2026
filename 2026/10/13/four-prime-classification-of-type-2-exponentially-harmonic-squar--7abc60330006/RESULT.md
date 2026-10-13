# Four-prime classification of type-2 exponentially harmonic squarefree squares
## Finding
For a positive integer \(n=\prod_p p^{a_p}\), an exponential divisor is a number \(d=\prod_p p^{b_p}\) with \(b_p\mid a_p\). Let \(d^{(e)}(n)\) count these divisors, and write
\[
S_e(n)=\sum_{d\mid_e n}\frac{n}{d}.
\]
Following the type-2 definition of Sándor, call \(n\) *exponentially harmonic of type 2* precisely when
\[
S_e(n)\mid n\,d^{(e)}(n).
\]
**Theorem.** Let \(m\ge1\) be squarefree, with at most four distinct prime factors. Then \(m^2\) is exponentially harmonic of type 2 if and only if
\[
\boxed{m\in\{1,6,30,42,66,138,210,546,570,1722,2838,4074,5970,12306,15906\}.}
\]
There is also an *unrestricted-support obstruction*: whenever \(m\) is squarefree, \(m^2\) is type 2, and \(\omega(m)\ge3\), necessarily \(6\mid m\), and the smallest prime \(q>3\) dividing \(m\) belongs to
\[
\boxed{\{5,7,11,23\}.}
\]
All four values of \(q\) occur, witnessed by \(m=6q\). The theorem makes no finiteness assertion for squarefree \(m\) with more than four distinct primes.

## Assumptions and scope
All integers and primes are positive unless explicitly stated otherwise. The squarefree condition means that each prime factor of \(m\) occurs exactly once. The function \(\omega(m)\) counts its distinct prime factors, with \(\omega(1)=0\). We use \(S_e(1)=d^{(e)}(1)=1\) as in the standard convention. The theorem has **no bound on the magnitude** of \(m\), including in the four-prime classification; the only size bound below is a *proved consequence* of the divisor condition.

For a squarefree \(m\) with \(r=\omega(m)\), every exponential divisor of \(m^2\) chooses the exponent \(1\) or \(2\) for every prime factor. Thus
\[
d^{(e)}(m^2)=2^r,\qquad
S_e(m^2)=\prod_{p\mid m}(p+1),
\]
and type-2 harmonicity is *equivalent* to the exact integer divisibility
\[
\tag{1}\prod_{p\mid m}(p+1)\ \mid\ 2^r m^2.
\]
The proof uses (1) throughout.

## Proof
**1. The empty support and odd supports.** For \(m=1\), condition (1) holds. Suppose \(m>1\) is odd, and write \(r=\omega(m)\). Because each odd \(p\mid m\) contributes one factor of \(2\) to \(p+1\),
\[
\sum_{p\mid m}v_2(p+1)\ge r
=v_2(2^r m^2).
\]
If (1) holds, equality is necessary, hence every \(p\mid m\) has \(v_2(p+1)=1\). Let \(p\) be the smallest prime dividing \(m\). Because \(p\ge5\), the number \((p+1)/2\) is an odd integer greater than \(1\). Any prime divisor \(\ell\) of it is strictly smaller than \(p\), yet (1) requires \(\ell\mid m\): contradiction. Hence every nontrivial \(m\) satisfying (1) is even.

**2. The compulsory prime \(3\).** If \(2\mid m\), the denominator of (1) contains \(2+1=3\). Consequently \(3\mid m\), because its numerator has no new odd prime factors beyond those of \(m\). Thus \(6\mid m\). If \(r=2\), necessarily \(m=6\); direct substitution gives \(12\mid4\cdot36=144\).

**3. Exact least-prime obstruction for arbitrary support.** Assume \(r\ge3\), and let \(q>3\) be the smallest prime of \(m\) exceeding \(3\). Every odd prime divisor \(\ell\) of \(q+1\) satisfies \(\ell<q\) and, by (1), divides \(m\). By minimality of \(q\), necessarily \(\ell=3\). Hence \(q+1=2^a3^b\) for integers \(a\ge1\) and \(b\ge0\).

The factor \(2+1=3\) already contributes one factor \(3\) to the denominator of (1), while \(v_3(2^r m^2)=2\). Therefore \(b\le1\). At the prime \(2\), the factor \(3+1=4\) contributes valuation \(2\), the \(q+1\) factor contributes \(a\), and each other prime of \(m\) greater than \(3\) contributes at least \(1\). Thus
\[
2+a+(r-3)\le v_2(2^r m^2)=r+2,
\]
so \(a\le3\). The only prime values greater than \(3\) among \(2^a3^b-1\) for \(1\le a\le3\), \(0\le b\le1\), are exactly \(5,7,11,23\). This proves the unrestricted-support obstruction.

**4. Three prime factors.** Now \(m=6q\), with \(q>3\) prime. Condition (1) reduces to
\[
12(q+1)\mid 8(6q)^2=288q^2,
\]
or equivalently \(q+1\mid24q^2\). Since \(\gcd(q+1,q^2)=1\), this is equivalent to \(q+1\mid24\). With \(q>3\) prime, the possibilities are exactly \(q\in\{5,7,11,23\}\), producing \(m\in\{30,42,66,138\}\). In particular, each obstruction value is attained.

**5. Four prime factors and a proved finite bound.** Now \(m=6qr\), where \(3<q<r\) are primes and \(q\) is in the four-element set above. Condition (1) is exactly
\[
12(q+1)(r+1)\mid16(6qr)^2,
\]
i.e.
\[
\tag{2}(q+1)(r+1)\mid48q^2r^2.
\]
As \(\gcd(r+1,r^2)=1\), (2) implies
\[
\tag{3}r+1\mid48q^2,\qquad r\le48q^2-1.
\]
The right-hand side is at most \(25391\), uniformly for these four possible \(q\). Consequently the following *finite, exhaustive* arithmetic classification follows directly: for each \(q\), test every integer \(r\) with \(q<r<48q^2\), retain primes meeting (3), then check exact divisibility (2). The standalone verifier includes these precise loops and deterministic trial-division primality tests; there is no assumption about untested larger \(r\), because (3) rules them out.

The complete qualifying pairs are
\[
\begin{array}{c|l}
q&r\\\hline
5&7,19,199\\
7&13,41,97,293\\
11&43,241\\
23&\varnothing
\end{array}.
\]
Their products \(m=6qr\) are
\[
\{210,546,570,1722,2838,4074,5970,12306,15906\}.
\]
All nine have been individually checked by (2), and (3) proves that the finite sweep is exhaustive. Together with steps 1–4, this proves the theorem.

## Verification
The included standard-library script `verify.py` is run by `python3 verify.py`. It reconstructs exponential divisors of \(m^2\) directly, computes their cleared-denominator harmonic mean, and independently compares with (1) for every squarefree \(m\le12000\). It additionally tests the four three-support cases and performs the *proof-bounded exhaustive* four-support search \(q<r<48q^2\), using deterministic integer primality checks. The expected output is:

`EXACT_CERTIFICATE_OK q_spectrum=5,7,11,23 four_support=9 largest_base=15906 finite_regression=12000`

The finite regression alone does **not** justify the theorem for infinitely many \(m\); steps 1–5 do. The four-prime enumeration is exhaustive because of the separately proved bound (3), not merely because a loop finished.

## Relationship to prior work
Sándor introduced the two exponential harmonic notions and showed that every squarefree integer itself is harmonic of both types. His 2005 monograph, section “Exponentially harmonic numbers”, and his 2006 Scientia Magna article state the type-2 divisor criterion and certain e-perfect/modified-e-perfect implications, but they do not classify the squarefree-square family. Minculete's 2012 thesis, section 4.3, explicitly notes that \(900\) is type 2 but not type 1; it does not present the universal least-prime obstruction or a four-support classification. OEIS A348964 and A348965 enumerate examples, not a proof-bounded complete four-support table.

A published rational-semigroup test for products \(\prod_p(1+1/p)^{a_p}\) classifies *semigroup membership*, not divisibility of \(\prod_{p\mid m}(p+1)\) into \(2^{\omega(m)}m^2\). These assertions do not imply the nine-value classification or the sharp four-value least-prime spectrum. Similarly, results on exponential-perfect numbers (equality of an exponential divisor sum with twice the input) impose a different condition from type-2 harmonicity; for example \(m=30\) gives a type-2 square \(m^2=900\) that is not exponential-perfect.

## Limitations
The classification is complete only for squarefree bases with \(\omega(m)\le4\); for larger supports only the compulsory factors \(2\), \(3\) and the least additional prime spectrum are established. No density or finiteness theorem for the unrestricted family is claimed. Originality is assessed against the cited full source passages, accessible indexed records, and semantic results; previously unindexed work might exist. The 2005 monograph's preface is explicitly dated \(16\) August \(2005\), but this source dateline is not independent evidence for the exact day on which electronic access began.

## References
1. József Sándor, *Selected Chapters of Geometry, Analysis and Number Theory*, dated 16 August 2005, section “Exponentially harmonic numbers”, pp. 141–145. Public PDF: https://blngcc.wordpress.com/wp-content/uploads/2008/11/jozsel-sandor-selected-chaters-of-geometry-analysis-and-number-theory.pdf.
2. József Sándor, “On exponentially harmonic numbers,” *Scientia Magna* **2** (2006), no. 3, pp. 44–47; original full issue: https://fs.unm.edu/ScientiaMagna2no3.pdf.
3. Nicuşor Minculete, *Contribuţii la studiul proprietăţilor analitice ale funcţiilor aritmetice – Utilizarea e-divizorilor*, Ph.D. thesis, February 2012, §4.3, pp. 90–94. https://www.imar.ro/~purice/Inst/2012/Minculete-Dr.pdf.
4. OEIS A348964, “Exponential harmonic (or e-harmonic) numbers of type 2”, and OEIS A348965, nonsquarefree members. https://oeis.org/A348964 and https://oeis.org/A348965.

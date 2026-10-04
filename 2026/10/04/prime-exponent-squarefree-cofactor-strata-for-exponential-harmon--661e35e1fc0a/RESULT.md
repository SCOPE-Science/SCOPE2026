# Prime-exponent squarefree-cofactor strata for exponential harmonic numbers
## Finding
Let \(\ell\) be a prime, let \(p\) be a prime, and let \(m\ge 1\) be squarefree with \(\gcd(p,m)=1\). Put \(n=p^{\ell}m\). Then \(n\) is never exponential harmonic of type 1, while \(n\) is exponential harmonic of type 2 exactly when
\[
p^{\ell-1}+1\mid 2m.
\]
Writing
\[
M=\frac{p^{\ell-1}+1}{\gcd(p^{\ell-1}+1,2)},
\]
the type-2 condition is equivalent to \(M\) being squarefree and \(m=Ms\) with \(s\) squarefree and \(\gcd(s,pM)=1\). Therefore, in the two-prime-support subfamily \(n=p^{\ell}q\), type 2 occurs exactly when \(q=M\) is prime.

## Assumptions and scope
For an integer \(n=\prod_i p_i^{a_i}>1\), an exponential divisor has the form \(\prod_i p_i^{b_i}\) with \(b_i\mid a_i\). Let \(d_e(n)\) be the number of exponential divisors and \(\sigma_e(n)\) their sum. Following the standard definitions, type 1 means \(\sigma_e(n)\mid n d_e(n)\). Type 2 means \(S_e(n)\mid n d_e(n)\), where
\[
S_e(n)=\prod_i\left(\sum_{d\mid a_i}p_i^{a_i-d}\right).
\]
The theorem concerns the first non-squarefree exponent layer in which exactly one prime has a prime exponent \(\ell\) and every other exponent is \(1\). No assertion is made for composite repeated exponents.

## Proof
Because \(\ell\) is prime, its positive divisors are \(1\) and \(\ell\). Every prime dividing \(m\) has exponent \(1\). Hence
\[
d_e(n)=2,
\qquad
\sigma_e(n)=m(p+p^{\ell})=mp(1+p^{\ell-1}),
\]
and
\[
S_e(n)=1+p^{\ell-1}.
\]
For type 1, the divisibility condition becomes
\[
mp(1+p^{\ell-1})\mid 2p^{\ell}m,
\]
so
\[
1+p^{\ell-1}\mid 2p^{\ell-1}.
\]
Since \(\gcd(1+p^{\ell-1},p)=1\), this would force \(1+p^{\ell-1}\mid 2\), impossible because \(p\ge2\) and \(\ell\ge2\). Thus type 1 never occurs in this stratum.

For type 2, the condition is
\[
1+p^{\ell-1}\mid 2p^{\ell}m.
\]
Again \(\gcd(1+p^{\ell-1},p)=1\), so this is equivalent to
\[
1+p^{\ell-1}\mid 2m.
\]
Let \(g=\gcd(1+p^{\ell-1},2)\) and \(M=(1+p^{\ell-1})/g\). If \(g=1\), then \(M\) is odd and the preceding divisibility is equivalent to \(M\mid m\). If \(g=2\), cancellation of the common factor \(2\) gives the same equivalence. Since \(m\) is squarefree, \(M\mid m\) is possible exactly when \(M\) is squarefree, in which case \(m=Ms\) with \(s\) squarefree and \(\gcd(s,M)=1\). Also \(\gcd(p,M)=1\), so this is equivalent to \(\gcd(s,pM)=1\). If \(m=q\) is prime, then \(M>1\) and \(M\mid q\), hence \(M=q\), giving the final statement.

## Verification
The accompanying checker evaluates the two defining divisibilities directly, independently of the simplified criterion, for primes \(p<60\), prime exponents \(\ell<12\), and every squarefree \(m\le1000\) coprime to \(p\). It checks 47,460 triples and finds no discrepancy. It also checks representative type-2 values including \(12,18,40,60,75,84,132,135,156,204\). This finite computation is corroborative only; the proof above establishes the theorem for all allowed \(p,\ell,m\).

## Relationship to prior work
Laugier, Saikia, and Sarmah record the two exponential-harmonic definitions and give criteria only under the additional hypothesis that the number is multiplicatively exponential-perfect or multiplicatively exponential-superperfect. Their first public arXiv version is dated 2016-03-11 and lists primary MSC 11A25. Sándor's 2006 paper introduces the two notions, proves that squarefree integers are of both types, characterizes exponential-perfect integers that are of type 1, and gives a sufficient modified-exponential-perfect condition for type 2. Neither inspected source states the prime-exponent squarefree-cofactor classification above.

The current OEIS entries A348961, A348964, and A348965 give the type-1 and type-2 sequences and examples. Their tabulated values agree with the theorem, but the entries do not state this exact stratum criterion.

## Limitations
The result does not classify repeated exponents that are composite, where more than two exponent divisors enter the local factors. It also does not assert that the two-prime-support condition produces infinitely many examples, since primality of \(M\) is an additional arithmetic constraint. The literature comparison covers the inspected primary papers, the exact current OEIS entries, targeted public searches, and the available research-result index; an equivalent statement in unindexed literature remains a residual possibility.

## References
1. A. Laugier, M. P. Saikia, U. Sarmah, “Some Results on Generalized Multiplicative Perfect Numbers,” arXiv:1603.04382, first version 2016-03-11; primary MSC 11A25.
2. J. Sándor, “On exponentially harmonic numbers,” Scientia Magna 2 (2006), no. 3, 44–47.
3. OEIS A348961, “Exponential harmonic numbers of type 1.”
4. OEIS A348964, “Exponential harmonic numbers of type 2.”
5. OEIS A348965, “Exponential harmonic numbers of type 2 that are not squarefree.”

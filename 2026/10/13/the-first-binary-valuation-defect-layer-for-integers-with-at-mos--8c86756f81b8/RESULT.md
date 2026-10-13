# The first binary valuation-defect layer for integers with at most two prime factors

## Finding
Let \(\sigma(n)=\sum_{d\mid n}d\), let \(\nu_2(m)\) be the exponent of \(2\) in a positive integer \(m\), and let \(\Omega(n)\) count prime factors with multiplicity. Define the binary valuation defect
\[
\delta(n)=\lceil\log_2 n\rceil-\nu_2(\sigma(n)).
\]
For every integer \(n\ge2\) with \(\Omega(n)\le2\), the complete first positive defect fiber is
\[
\boxed{\delta(n)=1\iff n=2\ \text{or}\ n=15\ \text{or}\ n=2(2^r-1),\quad 2^r-1\text{ prime},\ r\ge2.}
\]
Thus \(15\) is the only odd member of this fiber with at most two prime factors, and the composite even members are exactly twice Mersenne primes. No infinitude assertion concerning Mersenne primes is made.

## Assumptions and scope
All integers are positive, \(n\ge2\), and \(\Omega(n)\le2\). In particular the possible prime-factor shapes are \(p\), \(p^2\), and \(pq\) for distinct primes \(p<q\). The source paper proves the universal inequality \(\delta(n)\ge0\) and classifies its zero fiber. This result instead classifies the adjacent fiber only in the stated low-multiplicity domain. It does not assert a classification for \(\Omega(n)\ge3\).

## Proof
First, \(\delta(n)=\lceil\log_2(n/2^v)\rceil\), where \(v=\nu_2(\sigma(n))\). For a prime power \(p^a\) with odd \(p\), the elementary valuation formula is
\[
\nu_2(\sigma(p^a))=
\begin{cases}
0,&a\text{ even},\\
\nu_2(p+1)+\nu_2((a+1)/2),&a\text{ odd}.
\end{cases}
\]
For \(p\) odd and \(a=1\), write \(p+1=2^r u\) with \(r\ge1\) and odd \(u\). If \(u=1\), then \(p=2^r-1\) is Mersenne and \(\delta(p)=0\). Otherwise \(u\ge3\) and \(p\ge3\cdot2^r-1>2^{r+1}\), yielding \(\delta(p)\ge2\). For \(p=2\), \(\sigma(2)=3\), so \(\delta(2)=1\).

If \(p\) is odd and \(a=2\), then \(\sigma(p^2)\) is odd, so \(\delta(p^2)\ge4\). For completeness the same method excludes every larger odd-prime exponent from this defect fiber: if \(a=2t-1\ge3\), then \(t\ge2\), and the displayed valuation formula gives \(2^{\nu_2(\sigma(p^a))}\le(p+1)t\). But \(p^{2t-1}>2(p+1)t\) for \(p\ge3,t\ge2\). Indeed \(p+1\le4p/3\) and \(p^{2t-2}\ge3^{2t-2}>8t/3\); the last inequality holds at \(t=2\) and persists as the left side grows ninefold on incrementing \(t\). Hence \(\delta(p^a)\ge2\). If \(p=2\) and \(a\ge2\), then \(\sigma(2^a)=2^{a+1}-1\) is odd and \(\delta(2^a)=a\ge2\).

It remains to treat two distinct primes. For \(n=2q\), where \(q\) is odd, multiplicativity gives \(\sigma(n)=3(q+1)\). Consequently
\[
\delta(2q)=1+\bigl(\lceil\log_2q\rceil-\nu_2(q+1)\bigr).
\]
The prime case above shows that this equals \(1\) precisely when \(q=2^r-1\) is Mersenne.

Now suppose \(n=pq\) for odd primes \(p<q\). Write
\[
p+1=2^r u,\qquad q+1=2^s w,
\]
with \(r,s\ge1\) and odd positive \(u,w\). Since \(\nu_2(\sigma(pq))=r+s\), put
\[
R=\frac{pq}{2^{r+s}}=(u-2^{-r})(w-2^{-s}),\qquad \delta(pq)=\lceil\log_2 R\rceil.
\]
Thus \(\delta(pq)=1\) exactly when \(1<R\le2\). If \(u=w=1\), then \(1/2<R<1\) (both primes are Mersenne), giving defect zero. If \(u,w\ge3\), then \(R\ge(3-1/2)^2>2\). If \(u\ge3,w=1\), then \(q\) is a Mersenne prime greater than \(p\), hence \(s\ge3\), and
\[
R\ge(3-1/2)(1-1/8)=35/16>2.
\]
Finally, if \(u=1,w\ge3\), then \(p\) is Mersenne and \(r\ge2\). When \(r\ge3\),
\[
R\ge(1-1/8)(3-1/2)=35/16>2.
\]
For \(r=2\), necessarily \(p=3\), and \(R=(3/4)(w-2^{-s})\). The condition \(R\le2\) forces \(w=3,s=1\) (for \(w\ge5\) or \(s\ge2\) the product exceeds \(2\)). It gives \(q=5\), \(n=15\), and \(R=15/8\), so \(\delta(15)=1\). All possibilities are exhausted.

## Verification
The complete proof is symbolic. The accompanying standalone script `verify.py` independently computes \(\sigma(n)\), \(\Omega(n)\), and \(\delta(n)\) for all \(2\le n\le200000\), and compares the resulting low-multiplicity first-defect fiber with the proposed description. It returns:

`VERIFY_OK n_max=200000 first_defect=[2, 6, 14, 15, 62, 254, 16382] exact_integer_sieve=PASS`

The finite check is diagnostic and is not used to infer completeness beyond the tested interval.

## Relationship to prior work
Amdeberhan, Moll, Sharma, and Villamizar proved \(\nu_2(\sigma(n))\le\lceil\log_2 n\rceil\), with equality characterized by products of distinct Mersenne primes, and gave the prime-power \(2\)-adic valuation formula (their Theorems 1.1 and 1.3 and Theorem 3.2). Those results supply essential premises here but do not state or imply a classification of the first positive defect, which includes the non-Mersenne integer \(15\). Work on the odd-prime valuation bound treats a different valuation and does not furnish the present fiber. A comparison with the closest accessible records found no matching statement; this is not a proof of uniqueness in the literature.

## Limitations
This theorem concerns only \(\Omega(n)\le2\), and makes no claim for higher prime-factor multiplicity. It neither establishes nor assumes infinitely many Mersenne primes. The external originality search may miss unindexed equivalent formulations; independent validation has not been performed.

## References
1. T. Amdeberhan, V. H. Moll, V. Sharma, and D. Villamizar, *Arithmetic properties of the sum of divisors*, arXiv:2007.03088v1, first posted 2020-07-06, later *Journal of Number Theory* 223 (2021), 325–349, DOI:10.1016/j.jnt.2020.11.014.
2. J. Zhao and Y. Chen, *p-adic Valuation of the Sum of Divisors*, *Frontiers of Mathematics* 20 (2025), 795–827, DOI:10.1007/s11464-023-0154-2 (context for the distinct odd-prime valuation problem).

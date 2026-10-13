# Exact escape families and a sharp cubic cutoff for shifted rational-perfect numbers

## Finding

Let \(\sigma(n)=\sum_{d\mid n}d\). For fixed positive integer \(r\), consider positive integers \(k\ge2\) and \(n\ge2\) satisfying
\[
\sigma(n)=\frac{k+1}{k}n+r. \tag{1}
\]
Then the following is a complete classification outside an explicit finite range.

For \(r=1\), every solution and only every solution is \((k,n)=(p,p^2)\), with \(p\) prime. For \(r=2\), the sole solution is \((k,n)=(4,4)\). For \(r=3\), the solutions are exactly \((k,n)=(2,8),(9,9)\) and \((k,n)=(2,2q)\), for arbitrary odd prime \(q\).

For every fixed \(r\ge4\), every solution of (1) satisfies at least one of the following alternatives:
\[
(k,n)=(p,pq),\quad p=r-1,\quad p,q\text{ distinct primes}; \tag{2}
\]
or
\[
n\le(r-1)^3. \tag{3}
\]
Every pair in (2) satisfies (1), and the bound (3) is best possible for infinitely many fixed offsets: whenever \(p\ge3\) is prime, \((r,k,n)=(p+1,p,p^3)\) is a solution on its boundary, not in (2).

Consequently, for fixed \(r\ge2\), the collection of solutions is infinite **if and only if** \(r-1\) is prime. The case \(r=1\) is also infinite, through prime squares. The bound (3) concerns the unrestricted number of prime factors of \(n\); it is not a cutoff on \(\Omega(n)\) or \(\omega(n)\).

## Assumptions and scope

All variables are ordinary positive integers; \(r\) is fixed, \(k\ge2\) and \(n\ge2\). The prime \(q\) in (2) is unrestricted except for being distinct from \(p\). A family indexed by primes is infinite by Euclid's theorem. The cutoff is explicit for each fixed offset, not an assertion that finitely many exceptions have been enumerated for every offset simultaneously.

## Proof

Multiplying (1) by \(k\) shows \(k\mid n\), since \(k\mid k\sigma(n)-(k+1)n\). Write \(n=kA\), where \(A\ge1\). Multiplication by \(A\) sends distinct divisors of \(k\) to distinct divisors of \(kA\), hence
\[
\sigma(kA)\ge A\sigma(k),\qquad
A\big(\sigma(k)-k-1\big)\le r. \tag{4}
\]

**Composite parameters.** Suppose \(k\) is composite. Let \(p\) be its least prime divisor and put \(h=k/p\), so \(h\ge p\). Because \(h\) is a proper divisor other than \(1\), \(\sigma(k)-k-1\ge h\). By (4), \(Ah\le r\), and therefore
\[
n=pAh\le pr\le r^2. \tag{5}
\]
In particular, no composite-\(k\) solution escapes the quadratic bound.

**Prime parameters.** Now let \(k=p\) be prime and factor \(n=p^aN\) with \(a\ge1\), \(p\nmid N\), and \(N\ge1\). Write \(T=\sigma(N)-N\ge0\). Multiplicativity and the prime-power sum give the exact identity
\[
(p^{a-1}-1)N+(p^{a+1}-1)T=r(p-1). \tag{6}
\]

If \(a=1\), (6) reduces to \((p+1)T=r\), so \(T\ge1\). When \(T=1\), the equality \(\sigma(N)=N+1\) forces \(N=q\) prime, necessarily distinct from \(p\). Thus \(r=p+1\), \(n=pq\), and we have precisely the escape family (2). Conversely, for distinct primes \(p,q\),
\[
\sigma(pq)=(p+1)(q+1)=\frac{p+1}{p}\,pq+(p+1),
\]
so every such pair really is a solution. If instead \(T\ge2\), then \(N\) is composite. Let \(\ell\) be its least prime factor and let \(h=N/\ell\ge\ell\). The proper-divisor sum \(T\) contains the distinct divisors \(1\) and \(h\), giving \(h\le T-1\), and thus
\[
N=h\ell\le h^2\le(T-1)^2\le T^2,
\qquad n=pN\le pT^2\le rT\le r^2. \tag{7}
\]
Here \(pT\le(p+1)T=r\) and \(T\le r\).

If \(a\ge2\) and \(T\ge1\), then (6), after dividing by \(p-1\), gives \((1+p+\cdots+p^a)T\le r\), so \(p^aT\le r\). Its other nonnegative term gives
\[
N\le\frac{r(p-1)}{p^{a-1}-1}\le r.
\]
Consequently \(n=p^aN\le r^2\).

Finally, if \(a\ge2\) and \(T=0\), then \(N=1\) and (6) reduces to
\[
r=1+p+\cdots+p^{a-2}. \tag{8}
\]
When \(a=2\), this is \(r=1\) and \(n=p^2\). When \(a\ge3\), one has \(r-1\ge p^{a-2}\) and \(3(a-2)\ge a\), hence
\[
n=p^a\le (r-1)^3. \tag{9}
\]
At \(a=3\) there is equality in (9): \(r=p+1\) and \(n=p^3\).

Together (5), (7), and (9) show that for \(r\ge2\) every solution outside the escape family has
\[
n\le\max\{r^2,(r-1)^3\}. \tag{10}
\]
For \(r\ge4\), \(r^2\le(r-1)^3\), proving (3). For \(r=1\), the composite and positive-\(T\) branches are impossible, leaving only (8) with \(a=2\). For \(r=2\), (10) gives \(n\le4\), and direct divisor sums show only \((4,4)\). For \(r=3\), (10) gives \(n\le9\) outside (2); checking \(k\mid n\) shows exactly \((2,8)\) and \((9,9)\). The escape family for \(r=3\) is \((2,2q)\) with \(q\) an odd prime. This proves every asserted case.

For any \(r\ge2\), if \(r-1\) is not prime, (2) cannot occur and the finite bound applies. If \(r-1=p\) is prime, (2) contributes infinitely many solutions from distinct primes \(q\). Infinitude for \(r=1\) follows from the prime-square solutions. Finally, (8) with \(a=3\) and any odd prime \(p\) witnesses sharpness of the cubic cutoff for infinitely many values \(r=p+1\). \(\square\)

## Verification

The standalone script `verify.py` independently computes the ordinary sum-of-divisors function by a divisor sieve, enumerates all \(2\le k\mid n\le200000\) with \(1\le r\le35\), and checks the exact \(r=1,2,3\) classifications, the converse prime-semiprime family, the cubic cutoff for \(4\le r\le35\), and ten boundary prime-cube instances. Run `python3 verify.py`; its recorded output is in `verification_output.txt`.

The proof of the theorem is the symbolic argument above; the finite regression is not used to deduce unbounded statements.

## Relationship to prior work

Sándor, *On certain rational perfect numbers* (2022), studies precisely equation (1). Its Theorems 1–4 treat small offsets and Theorem 5 gives a qualitative fixed-offset description with finitely many exceptional solutions and possible prime-indexed families. The present statement supplies the exact infinitude criterion, identifies every escape family, gives a uniform explicit cutoff over **all** prime-support sizes, and proves that its cubic exponent is optimal infinitely often. In particular, direct substitution shows that \((k,n)=(2,8)\) satisfies the \(r=3\) equation but is absent from the printed list in that paper's Theorem 4. That observation is included as part of the complete classification, not presented as the sole contribution.

Sándor's sequel *On certain rational perfect numbers, II* (2022) treats related equations for Dedekind's \(\psi\) and Euler's \(\varphi\), rather than providing this cutoff for \(\sigma\). A previously available low-prime-multiplicity classification of general affine divisor-sum equations addresses \(\Omega(n)\le2\), including the semiprime branch, but does not imply the unrestricted cutoff for arbitrary prime multiplicity. The shared semiprime family is not claimed to be new by itself.

## Limitations

This theorem does not give an enumeration of every solution below the explicit cutoff for each \(r\ge4\); some such finite problems may remain difficult. For some offsets the bound may be improvable. The cubic exponent is optimal over the full collection of fixed offsets, but its boundary is not asserted to be attained at every offset. The literature search cannot exclude an unindexed equivalent result, and no independent audit has been performed.

## References

1. J. Sándor, “On certain rational perfect numbers,” *Notes on Number Theory and Discrete Mathematics* **28** (2022), 281–285, DOI: 10.7546/nntdm.2022.28.2.281-285. First online 2022-05-12. https://nntdm.net/papers/nntdm-28/NNTDM-28-2-281-285.pdf
2. J. Sándor, “On certain rational perfect numbers, II,” *Notes on Number Theory and Discrete Mathematics* **28** (2022), 525–532, DOI: 10.7546/nntdm.2022.28.3.525-532. https://nntdm.net/papers/nntdm-28/NNTDM-28-3-525-532.pdf

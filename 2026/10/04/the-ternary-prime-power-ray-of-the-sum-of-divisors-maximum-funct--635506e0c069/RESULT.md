# The ternary prime-power ray of the sum-of-divisors maximum function is constant
## Finding
Define the ordinary sum-of-divisors maximum function by
\[\Sigma^{*}(N)=\max\{k\ge 1:\sigma(k)\mid N\}.\]
Then, for every integer \(a\ge1\),
\[\Sigma^{*}(3^a)=2.\]
Equivalently,
\[\sigma(n)=3^b\quad(b\ge0)\qquad\Longleftrightarrow\qquad n\in\{1,2\}.\]
Thus the values \(\Sigma^{*}(3)=\Sigma^{*}(9)=\Sigma^{*}(27)=2\) recorded in the foundational table extend to the entire ternary prime-power ray.

## Assumptions and scope
Here \(\sigma(n)=\sum_{d\mid n}d\) is the ordinary sum of positive divisors and all variables are positive integers unless explicitly stated otherwise. The exponent \(b\) is allowed to be zero, so \(3^0=1\). No assertion is made here for prime-power arguments \(p^a\) with \(p\ne3\).

## Proof
Suppose first that \(\sigma(n)=3^b\). If \(b=0\), then \(\sigma(n)=1\), hence \(n=1\). Assume henceforth that \(b\ge1\).

Because \(\sigma(n)\) is odd, every odd prime in \(n\) occurs to an even exponent. Indeed, for an odd prime \(p\), the factor \(1+p+\cdots+p^e\) is odd exactly when \(e\) is even, while \(\sigma(2^c)=2^{c+1}-1\) is always odd. Hence
\[n=2^c m^2\]
with \(m\) odd.

First take \(m=1\), so \(n=2^c\). We must solve
\[2^{c+1}-1=3^b.\]
The case \(c=0\) gives \(1=3^b\), impossible because \(b\ge1\). The case \(c=1\) gives \(n=2\). If \(c\ge2\) and \(c+1\) is odd, then \(2^{c+1}-1\equiv1\pmod3\), impossible because \(b\ge1\). If \(c+1=2t\) is even, then \(t\ge2\) and
\[3^b=(2^t-1)(2^t+1).\]
The two factors are positive odd coprime integers differing by \(2\), so both would have to be powers of \(3\). The only two nonnegative powers of \(3\) differing by \(2\) are \(1\) and \(3\), forcing \(t=1\), a contradiction. Thus the only solution with \(m=1\) and \(b\ge1\) is \(n=2\).

Now suppose \(m>1\). Choose an odd prime \(p\mid m\), and write the exponent of \(p\) in \(n\) as \(2e\) with \(e\ge1\). Multiplicativity gives \(\sigma(p^{2e})\mid\sigma(n)=3^b\), so \(\sigma(p^{2e})\) must itself be a positive power of \(3\).

If \(p=3\), then \(\sigma(p^{2e})\equiv1\pmod3\), impossible. If \(p\equiv2\pmod3\), the odd-length alternating sum \(1+p+\cdots+p^{2e}\) is again \(1\pmod3\), impossible. It remains to consider \(p\equiv1\pmod3\). Then
\[\sigma(p^{2e})\equiv 2e+1\pmod3,\]
so divisibility by \(3\) forces \(2e+1=3t\) for some \(t\ge1\). The factorization
\[\sigma(p^{2e})=\frac{p^{3t}-1}{p-1}=\frac{p^t-1}{p-1}\bigl(p^{2t}+p^t+1\bigr)\]
contains
\[G=p^{2t}+p^t+1.\]
Since \(p^t\equiv1\pmod3\), the lifting-the-exponent identity gives
\[v_3(G)=v_3(p^{3t}-1)-v_3(p^t-1)=v_3(3)=1.\]
But \(G>3\). Therefore \(G\) has a prime divisor different from \(3\), contradicting that \(\sigma(p^{2e})\) is a power of \(3\). Hence \(m>1\) is impossible.

We have proved that \(\sigma(n)\) is a power of \(3\) only for \(n=1,2\), and both do occur because \(\sigma(1)=1\) and \(\sigma(2)=3\). Finally, for every \(a\ge1\), \(\sigma(2)=3\mid3^a\), so \(\Sigma^{*}(3^a)\ge2\). If \(\sigma(k)\mid3^a\), then \(\sigma(k)\) is a power of \(3\), hence \(k\in\{1,2\}\). Thus \(\Sigma^{*}(3^a)=2\).

## Verification
A standalone checker enumerates \(\sigma(n)\) exactly for \(n\le200000\), confirms that only \(n=1,2\) have divisor sum a power of \(3\) in that range, and independently computes \(\Sigma^{*}(3^a)=2\) for \(1\le a\le8\). This finite computation is corroborative only; the proof above is unrestricted.

## Relationship to prior work
Sándor introduced \(\Sigma^{*}\), tabulated \(\Sigma^{*}(3)=\Sigma^{*}(9)=\Sigma^{*}(27)=2\), proved the general lower bound \(\Sigma^{*}(N)\ge2\) when \(3\mid N\), and used the parity characterization of odd divisor sums in a general upper-bound theorem. The inspected paper does not state a formula for \(\Sigma^{*}(3^a)\) for arbitrary \(a\), nor does it classify the solutions of \(\sigma(n)=3^b\). OEIS A319068 records the same maximum function and Sándor's formula at arguments one more than a prime, but does not give this ternary prime-power identity. The later unitary-divisor analogue studies a different function built from the unitary divisor sum and therefore does not imply the ordinary-divisor result here.

## Limitations
The originality search included the foundational full text, the present OEIS entry, a later unitary analogue, web searches for the exact inverse-image equation, and semantic database searches for equivalent formulations. No covering statement was found, but elementary inverse divisor-sum facts can occur in older or poorly indexed literature; that is the principal residual originality risk. The bibliographic date \(2005\text{-}01\text{-}01\) is the explicit publication date reported by a bibliographic database for Sándor's 2005 paper; the scanned paper itself prints the year but not a day. The subject assignment is independently checked against the Encyclopedia of Mathematics entry for the ordinary sum-of-divisors function, which lists 2020 MSC Primary 11A25.

## References
1. J. Sándor, “The sum-of-divisors minimum and maximum functions,” Research Report Collection 8(1), 2005; also Notes on Number Theory and Discrete Mathematics 11(2), 1–8 (2005). Public full text: https://rgmia.org/papers/v8n1/art4.pdf
2. OEIS A319068, “Greatest \(k\) such that \(\sigma(k)\) divides \(n\),” https://oeis.org/A319068
3. B. Das and H. K. Saikia, “On the Sum of Unitary Divisors Maximum Function,” AIMS Mathematics 2(1) (2017), 96–101, DOI 10.3934/Math.2017.1.96.
4. Encyclopedia of Mathematics, “Sum of divisors,” 2020 Mathematics Subject Classification: Primary 11A25, Secondary 11A51, https://encyclopediaofmath.org/wiki/Sum_of_divisors

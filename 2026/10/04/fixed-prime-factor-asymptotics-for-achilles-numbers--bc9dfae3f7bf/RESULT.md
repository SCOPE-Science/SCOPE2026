# Fixed-prime-factor asymptotics for Achilles numbers
## Finding
For a fixed integer \(r\ge 2\), define \(A_r(X)\) to be the number of positive integers \(n\le X\) that are Achilles numbers and satisfy \(\omega(n)=r\). Thus, if
\[n=\prod_{i=1}^r p_i^{e_i},\]
then every \(e_i\ge 2\) and \(\gcd(e_1,\ldots,e_r)=1\). The asymptotic is
\[A_r(X)\sim \kappa\,rac{\sqrt X\,(\log\log X)^{r-2}}{(r-2)!\,\log X},\qquad
\kappa=2\sum_prac{p^{-3/2}}{1-p^{-1}}.\]
The prime sum converges absolutely. For \(r=1\), there are no Achilles numbers, so \(A_1(X)=0\).

The leading contribution consists precisely of the exponent signatures having one odd exponent \(2j+1\ge3\) and all remaining exponents equal to \(2\). In particular, fixed-prime-factor Achilles numbers lie one logarithmic layer below the dominant square layer among powerful numbers.

## Assumptions and scope
The variable \(r\) is fixed while \(X	o\infty\). An Achilles number is a powerful number that is not a perfect power; equivalently, all prime-factor exponents are at least \(2\) and their greatest common divisor is \(1\). The proof uses the standard fixed-\(k\) Landau asymptotic for squarefree integers with exactly \(k\) distinct prime factors, together with its standard uniform upper bound on intervals whose endpoints differ from the main scale by powers of \(\log X\).

No claim is made about uniformity when \(r\) grows with \(X\), or about a second-order term.

## Proof
Every Achilles number has at least one odd prime-factor exponent. Indeed, if all exponents were even, their greatest common divisor would be at least \(2\).

Call an Achilles number *principal* if exactly one prime has an odd exponent and every other prime has exponent \(2\). Such a number has a unique form
\[n=p^{2j+1}m^2,\qquad j\ge1,\quad p
mid m,\quad m	ext{ squarefree},\quad \omega(m)=r-1.\]
Conversely, every integer of this form is Achilles because \(\gcd(2j+1,2)=1\).

Let \(Q_k(Y;p)\) count squarefree \(m\le Y\) with \(\omega(m)=k\) and \(p
mid m\). For fixed \(k\) and fixed \(p\), Landau's theorem gives
\[Q_k(Y;p)\sim rac{Y(\log\log Y)^{k-1}}{(k-1)!\log Y}.\]
Excluding one fixed prime changes only lower-order terms. Therefore the principal count is
\[M_r(X)=\sum_p\sum_{j\ge1}Q_{r-1}\!\left(\sqrt{X/p^{2j+1}};pight).\]

To justify summation of the individual asymptotics, split at \(p^{2j+1}\le (\log X)^{12}\). On this range the square-root argument lies between \(\sqrt X/(\log X)^6\) and \(\sqrt X\), so the fixed-order Landau asymptotic is uniform; moreover \(\log Y=(	frac12+o(1))\log X\) and \(\log\log Y=\log\log X+o(1)\). Hence
\[M_r(X)\sim rac{2\sqrt X(\log\log X)^{r-2}}{(r-2)!\log X}
\sum_p\sum_{j\ge1}p^{-(2j+1)/2}.\]
The double series is absolutely convergent and
\[\sum_{j\ge1}p^{-(2j+1)/2}=rac{p^{-3/2}}{1-p^{-1}}.\]
The complementary tail is negligible: the tail of the convergent weight series beyond \((\log X)^{12}\) is \(O((\log X)^{-2})\), and the elementary fixed-order upper bound for \(Q_k\) makes its contribution \(o(\sqrt X(\log\log X)^{r-2}/\log X)\).

It remains to bound nonprincipal Achilles numbers. Such a number has at least two exceptional exponents: one odd exponent at least \(3\), and at least one further exponent at least \(3\). Ignoring the greatest-common-divisor restriction only enlarges this remainder. For \(r\ge3\), designate two exceptional primes and sum over their exponents. The remaining \(r-2\) primes occur at exponent at least \(2\); replacing those exponents by \(2\) gives an upper bound controlled by the fixed-order Landau estimate. Since
\[\sum_p\sum_{e\ge3}p^{-e/2}<\infty,\]
the remainder is
\[O_r\!\left(rac{\sqrt X(\log\log X)^{r-3}}{\log X}ight),\]
which is lower order. When \(r=2\), both prime exponents are at least \(3\), so \((pq)^3\le X\); the resulting semiprime count is \(X^{1/3+o(1)}\), again \(o(\sqrt X/\log X)\). This proves the stated asymptotic for every fixed \(r\ge2\).

## Verification
The accompanying `verify.py` independently generates every powerful number up to \(10^8\) through the unique representation \(n=a^2b^3\) with squarefree \(b\), reconstructs its prime exponents, and applies the Achilles criterion directly. It checks that the total number below \(10^8\) is \(10553\), matching the published A052486 count, and records the exact distribution by \(\omega\) as well as the principal-signature subcounts. This finite computation is corroborative only; it does not prove the asymptotic.

The constant \(\kappa\) is also approximated by summing its convergent prime series to a finite cutoff. The proof of convergence and the asymptotic itself is symbolic and does not depend on that numerical approximation.

## Relationship to prior work
OEIS A052486 gives the Achilles definition, examples, aggregate counts, and a creation date of 2000-03-16. Its page does not state a fixed-\(\omega\) asymptotic. OEIS A393816 separately tabulates Achilles numbers with exactly two distinct prime factors; it supplies a direct database comparison for the \(r=2\) stratum but gives no asymptotic formula.

Das, Kuo, and Liu study \(\omega(n)\) over \(h\)-full integers. Their Theorem 1.2 gives first and second moments over all \(h\)-full integers, and their primary MSC is 11N37. Their inspected full text does not discuss Achilles numbers or perfect-power deletion, and moment information over the full \(h\)-full set does not imply the fixed-\(r\) Achilles asymptotic here. The present result isolates the first nonsquare exponent layer and shows that deleting perfect powers changes the leading fixed-\(r\) scale.

## Limitations
The result is asymptotic for each fixed \(r\); it is not uniform in growing \(r\). No effective error constant is supplied. The originality comparison covers published-finding corpus semantic searches, the exact OEIS Achilles tables, and the inspected full text of the recent \(h\)-full \(\omega\)-distribution paper; unindexed literature using different terminology remains a residual literature risk.

## References
- OEIS A052486, *Achilles numbers - powerful but imperfect*; sequence author entry Henry Bottomley, 2000-03-16.
- OEIS A393816, *Achilles numbers with exactly 2 distinct prime factors*.
- S. Das, W. Kuo, and Y.-R. Liu, *Distribution of \(\omega(n)\) over \(h\)-free and \(h\)-full numbers*, arXiv:2409.10430v1, 2024-09-16; 2020 MSC 11N37, 11N05, 11N56.

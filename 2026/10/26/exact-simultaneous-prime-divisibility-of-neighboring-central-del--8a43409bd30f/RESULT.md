# Exact simultaneous prime divisibility of neighboring central Delannoy numbers

## Finding

Write the central Delannoy numbers as
\[
D_n=\sum_{k=0}^{n}\binom nk\binom{n+k}{k}=\sum_{k=0}^{n}\binom nk^2 2^k\quad(n\ge0).
\]
For a prime \(p\ge5\), define the forbidden digits
\[
Z_p=\{d\in\{0,1,\ldots,p-1\}:D_d\equiv0\pmod p\},\qquad a_p=p-|Z_p|,
\]
and the number of nonzero adjacent digit pairs
\[
c_p=\#\{d:0\le d<p-1,\ d\notin Z_p,\ d+1\notin Z_p\}.
\]
For every integer \(L\ge1\), the **exact simultaneous-divisibility count** is
\[
\boxed{\#\{0\le n<p^L:p\mid D_n\text{ and }p\mid D_{n+1}\}=p^L-2a_p^L+1+c_p\frac{a_p^L-1}{a_p-1}.}
\]
For every prime \(p\equiv3\pmod4\) with \(p\ge7\), at least one digit is forbidden. Consequently, for each such fixed prime, **the set of indices at which it divides both consecutive Delannoy numbers has natural density one**. In particular,
\[
\boxed{\lim_{X\to\infty}\frac1X\#\{0\le n<X:\gcd(D_n,D_{n+1})>B\}=1\quad(B>0\text{ fixed}).}
\]
For \(p=7\) the forbidden-digit set is \(\{3\}\) and the formula becomes
\[
\#\{0\le n<7^L:7\mid\gcd(D_n,D_{n+1})\}=7^L-\frac{6^{L+1}-1}{5}.
\]
For example, the exact counts for \(L=2,3,4\) are \(6,84,846\), respectively.

## Assumptions and scope

All indices \(n\) and digit lengths \(L\) are integers with \(n\ge0\), \(L\ge1\); primes are ordinary positive rational primes. The exact closed count is valid for **every prime \(p\ge5\)**, including primes for which \(Z_p\) is empty. The density-one corollaries concern primes \(p\equiv3\pmod4\) of size at least \(7\); \(B\) is any fixed positive real number. These are natural densities over indices, not over primes, and the prime is held fixed before taking the limit. No assertion is made about the value or size of the gcd at every individual index.

## Proof

**1. Digitwise congruence.** By the binomial-square representation and Lucas's theorem, if \(n=\sum_{j\ge0}n_jp^j\), then
\[
D_n\equiv\prod_{j\ge0}D_{n_j}\pmod p.
\]
Indeed, write each \(k\) in base \(p\). Lucas's theorem gives \(\binom nk\equiv\prod_j\binom{n_j}{k_j}\pmod p\), and Fermat's theorem gives \(2^k\equiv\prod_j2^{k_j}\pmod p\). The sum over all digit strings factorizes, with vanishing binomial terms when \(k_j>n_j\). It follows that \(p\nmid D_n\) exactly when all base-\(p\) digits of \(n\) avoid \(Z_p\). Note \(D_0=1\), \(D_1=3\), and \(D_{p-1}\equiv\sum_{k=0}^{p-1}2^k\equiv1\pmod p\), so for \(p\ge5\), the three digits \(0,1,p-1\) are allowed. In particular \(a_p\ge3\).

**2. Exact adjacent counts with carries.** Let \(I_L\) denote the number of \(0\le n<p^L\) for which neither \(D_n\) nor \(D_{n+1}\) is divisible by \(p\). Set \(I_0=1\), justified by \(D_0,D_1\not\equiv0\pmod p\). For the least significant digit \(d\le p-2\), there is no carry. Exactly \(c_p\) choices make \(d,d+1\) both allowed, while all \(L-1\) higher digits must independently be among \(a_p\) allowed digits. These contribute \(c_pa_p^{L-1}\). For \(d=p-1\), the added unit creates a carry; since \(0,p-1\) are allowed, the higher block \(r\) must satisfy that both \(D_r,D_{r+1}\) are nonzero modulo \(p\). This contributes precisely \(I_{L-1}\), including the last-block case \(r=p^{L-1}-1\). Thus
\[
I_L=c_pa_p^{L-1}+I_{L-1}=1+c_p\frac{a_p^L-1}{a_p-1}.
\]
Exactly \(a_p^L\) indices \(0\le n<p^L\) have \(p\nmid D_n\). The same count holds with \(n+1\) in place of \(n\): shifting the interval replaces \(0\) by \(p^L\), whose residue satisfies \(D_{p^L}\equiv D_1=3\not\equiv0\pmod p\). Inclusion-exclusion now gives
\[
\#\{n<p^L:p\mid D_n,D_{n+1}\}=p^L-2a_p^L+I_L,
\]
which is the asserted formula.

**3. A forbidden digit for primes \(p\equiv3\pmod4\).** Fix an odd prime \(p\equiv3\pmod4\) and write \(m=(p-1)/2\), so \(m\) is odd. Over \(\mathbf F_p\), take \(f(x)=x(x-1)(x-2)\). The involution \(x\mapsto2-x\) sends \(f(x)\) to \(-f(x)\); therefore \(\sum_{x\in\mathbf F_p}f(x)^m=0\). On the other hand \(f(x)^m\) has degree \(3m<2(p-1)\) and vanishes at \(x=0\). The finite-field power-sum identity \(\sum_xx^j=-1\) if \(j>0\) is a multiple of \(p-1\), and zero otherwise, shows that
\[
0=\sum_{x\in\mathbf F_p}f(x)^m=-[x^{p-1}]f(x)^m.
\]
Since \(p-1=2m\), expansion of the coefficient gives
\[
[x^{p-1}]f(x)^m=[x^m](x-1)^m(x-2)^m=(-1)^m\sum_{k=0}^m\binom mk^2 2^k=(-1)^mD_m.
\]
Thus \(p\mid D_{(p-1)/2}\). When \(p\ge7\) the digit \(m\in Z_p\) is strictly interior, so \(a_p<p\).

**4. Density-one common divisors and unboundedness in density.** If \(a_p<p\), then at most \(2a_p^L\) of the indices below \(p^L\) fail simultaneous divisibility, by the union bound in step 2. For arbitrary \(X\), choose \(L\) with \(p^{L-1}\le X<p^L\). The exceptional proportion is bounded by \(2a_p^L/p^{L-1}=2p(a_p/p)^L\), which tends to zero. Hence each fixed prime \(p\equiv3\pmod4\), \(p\ge7\), divides the gcd of the consecutive terms for a density-one set of indices. There are infinitely many such primes: if \(p_1,\ldots,p_s\) were all primes congruent to \(3\pmod4\), the integer \(4p_1\cdots p_s-1\) would have a new prime factor congruent to \(3\pmod4\). Given any \(B>0\), choose a finite product \(M>B\) of these primes. The intersection of finitely many density-one sets has density one, and on that intersection \(M\mid\gcd(D_n,D_{n+1})\). This proves the final density statement.

**5. The concrete prime seven.** Directly from \(D_0,\ldots,D_6=(1,3,13,63,321,1683,8989)\), reduction modulo seven gives \(Z_7=\{3\}\), hence \(a_7=6\) and \(c_7=4\). Substitution into the exact formula gives the displayed closed form.

## Verification

The accompanying file `verify.py` uses the independent integral recurrence \((n+1)D_{n+1}=3(2n+1)D_n-nD_{n-1}\) rather than Lucas digit multiplication to obtain the integers. It checks 45 independent binomial-square expansions, 19 entire prime-power blocks, full digit-product congruences in those blocks, and the midpoint divisibility assertion for primes congruent to three modulo four through 199. Run with `python3 verify.py`. All stated finite certificates reproduced without external dependencies. The proof above, not these finite checks, establishes the assertions for all primes and indices.

## Relationship to prior work

Eu, Liu, and Yeh (first made public 2005-12-20) explicitly treat central Delannoy congruences by Lucas's theorem. Noe (2006, §§6–8) proves a general digit-divisibility theorem for generalized central trinomial coefficients, encompassing the base-digit criterion for the central Delannoy specialization. Those components are not claimed as new. Sun's 2010–2014 papers address sums, congruences and divisibility of Delannoy and generalized central trinomial coefficients. The finding here concerns instead exact *simultaneous* zero counts at consecutive indices, including base-\(p\) carry transitions, and the density-one divergence of neighboring gcds. Its exact counting formula is a further consequence of the digit criterion and should be regarded as a specific distributional refinement, not a strengthening of the underlying Lucas theorem.

## Limitations

The exact formula uses the finite zero set \(Z_p\) as input rather than giving a closed classification of those sets for every prime. A separately known or unlocated general consecutive-index automatic-sequence counting theorem might imply this specialization; the assessment retains literature-coverage uncertainty. The proof gives density-one growth, not pointwise growth, and does not determine the distribution of full gcd values or simultaneous prime-power valuations. The accessible 2005 Eu–Liu–Yeh abstract was checked, but its primary full text could not be read, leaving a specific literature-overlap risk.

## References

1. S.-P. Eu, S.-C. Liu, Y.-N. Yeh, *On the Congruences of Some Combinatorial Numbers*, Studies in Applied Mathematics 116 (2006), 135–144. First published online 20 December 2005. DOI: 10.1111/j.1467-9590.2006.00337.x.
2. T. D. Noe, *On the Divisibility of Generalized Central Trinomial Coefficients*, Journal of Integer Sequences 9 (2006), Article 06.2.7. https://cs.uwaterloo.ca/journals/JIS/VOL9/Noe/noe35.pdf.
3. Z.-W. Sun, *On Delannoy Numbers and Schröder Numbers*, arXiv:1009.2486, first submitted 13 September 2010; Journal of Number Theory 131 (2011), 2387–2397. https://arxiv.org/abs/1009.2486.
4. Z.-W. Sun, *Congruences Involving Generalized Central Trinomial Coefficients*, arXiv:1008.3887, first submitted 23 August 2010; Science China Mathematics 57 (2014), 1375–1400. https://arxiv.org/abs/1008.3887.

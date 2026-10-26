# Complete Harshad-base classification for even semiprimes

## Finding
For any integer \(n\ge1\), let \(s_b(n)\) be its ordinary base-\(b\) digit sum for \(b\ge2\), and put \(s_1(n)=n\), corresponding to unary notation. Define the all-base Harshad count
\[
H(n)=\#\{b:1\le b\le n,\ s_b(n)\mid n\}.
\]
For every odd prime \(p\), the following are **exactly** the Harshad bases of \(2p\):
\[
\begin{split}
\mathcal B(2p)={}&\{1,p,p+1,2p-1,2p\}\\
&\cup\bigl(\{2\}\text{ if }p=2^{2^a}+1\text{ for an integer }a\ge0\bigr)\\
&\cup\{b\ge3: b^{2^t}=2p-1\text{ for an integer }t\ge1\}.
\end{split}
\]
The displayed subsets are pairwise disjoint, and each root is counted once for each distinct base. Thus, writing \(e(p)\) for the number of positive integers \(t\) for which \(2p-1\) is an integral \(2^t\)-th power,
\[
H(2p)=5+\mathbf1_{\{p\text{ is a Fermat prime}\}}+e(p).
\]
If \(2p-1=\prod_{\ell}\ell^{a_\ell}\) is its prime factorization, then \(e(p)=\nu_2(\gcd_\ell a_\ell)\); here the finite gcd is positive because \(2p-1>1\). In particular,
\[
H(2p)=5\quad\Longleftrightarrow\quad p\text{ is not a Fermat prime and }2p-1\text{ is not a perfect square}.
\]
For every real \(X\ge3\), the number of odd primes \(p\le X\) not satisfying \(H(2p)=5\) is \(O(\sqrt X)\). Consequently, a density-one set of primes satisfies \(H(2p)=5\):
\[
\lim_{X\to\infty}\frac{\#\{p\le X:p\text{ odd prime},\ H(2p)=5\}}{\pi(X)}=1.
\]
An explicit higher-multiplicity instance is \(p=21523361\), an odd prime, for which \(2p-1=3^{16}\), the valid bases are \(1,3,9,81,6561,21523361,21523362,43046721,43046722\), and \(H(2p)=9\).

## Assumptions and scope
All variables \(p\) in the theorem range over odd rational primes. A base is an integer \(1\le b\le2p\), not a congruence class of bases. Unary digit sum is the number of unary unit symbols; a base exceeding \(2p\) is not counted. Fermat-prime means a prime of the form \(2^{2^a}+1\) with \(a\ge0\). No claim is made that the exceptional perfect-square prime family is infinite, nor that there are arbitrarily large counts \(H(2p)\).

## Proof
**1. Constrain possible digit sums.** For \(2\le b\le2p\), positivity and the radix expansion imply \(1\le s_b(2p)<2p\). As \(p\) is an odd prime, the only proper positive divisors of \(2p\) are \(1,2,p\). We classify bases giving each sum.

**2. Sum one.** The representation has one nonzero digit, which is \(1\), so \(2p=b^j\) for some \(j\ge1\). Squarefreeness of \(2p\) forces \(j=1\) and \(b=2p\).

**3. Sum \(p\).** Writing \(2p=\sum_{j\ge0}d_jb^j\) and \(\sum_jd_j=p\) gives
\[
p=2p-p=\sum_{j\ge1}d_j(b^j-1).
\]
Thus \(b-1\mid p\), which implies \(b=2\) or \(b=p+1\). At \(b=2\), the binary digit sum satisfies \(s_2(2p)=s_2(p)<p\) for \(p\ge3\), excluding this branch. In base \(p+1\), the digits of \(2p\) are \(1,p-1\), with sum \(p\). Hence this branch gives exactly \(b=p+1\).

**4. Sum two.** For \(b\ge3\), a radix expansion whose digit sum is two consists either of one digit \(2\) or of two digits \(1\). The first case gives \(2p=2b^j\) with \(j\ge1\), so primality of \(p\) yields \(j=1\) and \(b=p\). (In binary there is no digit \(2\).) In the second case, for \(b\ge2\),
\[
2p=b^i+b^j,\qquad i>j\ge0.
\]
If \(j\ge1\), then \(b\mid2p\), so \(b\in\{2,p,2p\}\). The size bound excludes \(p\) and \(2p\); hence \(b=2\). Since \(\nu_2(2p)=1\) and \(\nu_2(2^i+2^j)=j\), necessarily \(j=1\) and \(p=2^{i-1}+1\). If \(i-1\) had any odd factor \(h>1\), then \(2^{i-1}+1\) would be divisible by \(2^{(i-1)/h}+1\), strictly between \(1\) and \(p\). Thus \(i-1=2^a\). Conversely, each prime \(p=2^{2^a}+1\) gives \(2p=2^{2^a+1}+2\), whose binary digit sum is two. This is the unique additional base \(2\).

If \(j=0\), then \(b^i=2p-1\). For \(i=1\) this is \(b=2p-1\). For \(i\ge2\), the integer \(b\) is odd and at least three. If \(i\) has an odd divisor \(h\ge3\), write \(i=hm\); then \(b^{hm}+1\) is divisible by \(b^m+1\), and
\[
p=\frac{b^m+1}{2}\cdot\frac{b^{hm}+1}{b^m+1}
\]
is a product of two integers exceeding one, contradicting primality. Therefore \(i=2^t\) for \(t\ge1\). Conversely any odd integral root \(b^{2^t}=2p-1\) gives the base-\(b\) expansion with ones at positions \(2^t\) and zero, hence digit sum two.

**5. Union and counting.** The baseline bases \(1,p,p+1,2p-1,2p\) are distinct. Any additional base \(2\) is distinct from them for odd \(p\). For \(b^{2^t}=2p-1\), necessarily \(3\le b<p\), so the roots are distinct from all previous cases; different positive exponents yield distinct roots since \(2p-1>1\). Steps 2–4 exhaust every possible digit sum, and unary contributes \(b=1\), proving the exact set and count. The power-root multiplicity equals \(\nu_2(\gcd_\ell a_\ell)\) by uniqueness of prime factorization.

**6. Density.** If \(H(2p)\ne5\), then either \(p=2^{2^a}+1\), or \(2p-1\) is a perfect square. For \(p\le X\), the first possibility allows only \(O(\log\log X)\) indices \(a\), and the second admits at most \(\lfloor\sqrt{2X}\rfloor\) square roots. Their union has \(O(\sqrt X)\) members. The prime number theorem (indeed any standard bound \(\pi(X)\gg X/\log X\)) implies the asserted relative density.

## Verification
A standalone, standard-library-only Python checker (`verify.py`) independently computes actual Harshad bases for every odd prime \(p\le1200\) and compares them with the closed classification. It also tests the Fermat-prime and fourth-power boundary cases, checks the deterministic primality of \(21523361\) by trial division, and tests each of its nine asserted bases. The expected output begins `VERIFY_OK`. These finite computations corroborate examples and boundary conditions; they are not used to infer the universal theorem.

## Relationship to prior work
The all-base counting function is OEIS A080221 (2003), and OEIS A100263 (2004) tabulates integers having exactly five Harshad bases. OEIS A271311 and A271313 (2016) identify square-root, fourth-root and binary patterns in the six- and seven-base cases; the instance \(2p=82\) already has two root bases \(3\) and \(9\). These finite patterns and their examples are prior knowledge. The claim here is the *universal no-other-bases classification*, the exact count for arbitrary higher power roots, and the quantitative density-one result for prime arguments. Fixed-base Harshad counting results address a different quantifier and do not automatically imply an all-base classification for \(2p\). No claim of an independently audited priority search is made.

## Limitations
The exceptional-square prime family might be finite or infinite; this proof does not decide it. It does not establish any upper bound uniform in \(p\) for the number of additional power roots beyond the explicit logarithmic factorization count. Literature coverage is bounded to the named full sequence entries and targeted accessible source searches, so a stronger, unlocated result remains a priority risk. The verifier checks finite examples only.

## References
- M. Vandermast, OEIS A080221, *Number of bases in which an integer is a Harshad number*, initial entry 2003-03-16. https://oeis.org/A080221
- J. W. Layman, OEIS A100263, *Exactly five Harshad bases*, initial entry 2004-11-10. https://oeis.org/A100263
- D. Mondot, OEIS A271311, *Exactly six Harshad bases*, initial entry 2016-04-03. https://oeis.org/A271311
- D. Mondot, OEIS A271313, *Exactly seven Harshad bases*, initial entry 2016-04-03. https://oeis.org/A271313
- MSC2020, class 11A63, *Radix representation; digital problems*. https://msc2020.org/MSC_2020.pdf

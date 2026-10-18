# Exact first-five-window LCM quotient spectrum of the eighth cyclotomic polynomial

## Finding

Let \(F(t)=t^4+1=\Phi_8(t)\). For every positive integer \(n\) and each \(1\le k\le5\), define the integer
\[
G_k(n)=\frac{\prod_{j=0}^{k} F(n+j)}{\operatorname{lcm}(F(n),F(n+1),\ldots,F(n+k))}.
\]
The following gives the **complete value**, not merely a period or an asymptotic, of all five arithmetic functions. Define sets of least residues
\[
A_k=\{8-j\pmod {17}:0\le j\le k-1\}\ \cup\ \begin{cases}\{15-j\pmod {17}:0\le j\le k-4\},&k\ge4,\\\varnothing,&k\le3,\end{cases}
\]
\[
B_k=\begin{cases}\{47-j\pmod {97}:0\le j\le k-3\},&k\ge3,\\\varnothing,&k\le2,\end{cases}\quad
C_k=\begin{cases}\{318\pmod {641}\},&k=5,\\\varnothing,&k\le4.\end{cases}
\]
Let \(o_k(n)=\#\{0\le j\le k:n+j\text{ is odd}\}\). The exact formula is
\[
\boxed{G_k(n)=2^{o_k(n)-1}\,17^{\mathbf1_{n\bmod17\in A_k}}\,97^{\mathbf1_{n\bmod97\in B_k}}\,641^{\mathbf1_{n\bmod641\in C_k}}.}
\]
The **least positive periods** (respectively for \(k=1,2,3,4,5\)) are
\[
\boxed{17,\quad34,\quad1649,\quad3298,\quad1057009.}
\]
At \(k=5\), the quotient takes precisely eight values; the number of occurrences of each value in **any complete least period** is:

| Value | Occurrences |
| ---: | ---: |
| \(4\) | 601600 |
| \(68\) | 421120 |
| \(388\) | 19200 |
| \(6596\) | 13440 |
| \(2564\) | 940 |
| \(43588\) | 658 |
| \(248708\) | 30 |
| \(4228036\) | 21 |

In particular, passing from a five-term window to a six-term window introduces the exceptional prime \(641\) while eliminating the parity contribution to the *least* period.

## Assumptions and scope

All statements are unconditional, for **every integer** \(n\ge1\), with the window length exactly \(k+1\) for \(1\le k\le5\). The polynomial has no positive integral zero, so the least-common-multiple quotient is always defined. The indicator of an empty residue set equals zero. Set membership is interpreted modulo the indicated prime, including negative representatives.

## Proof

**1. Isolate candidate primes by polynomial resultants.** For a shift \(h\ge1\), denote the integral resultant of \(F(X)\) and \(F(X+h)\) by \(R_h\). A direct exact 8-by-8 Sylvester determinant computation gives:

| \(h\) | \(R_h\) | Prime factorization |
| ---: | ---: | --- |
| 1 | 153 | \(3^2\cdot17\) |
| 2 | 73728 | \(2^{13}\cdot3^2\) |
| 3 | 46584153 | \(3^4\cdot7^2\cdot11^2\cdot97\) |
| 4 | 4421910528 | \(2^{16}\cdot3^4\cdot7^2\cdot17\) |
| 5 | 154497425625 | \(3^6\cdot5^4\cdot23^2\cdot641\) |

Here \(F(X+h)=X^4+4hX^3+6h^2X^2+4h^3X+h^4+1\). The accompanying checker constructs these determinants afresh using exact integer arithmetic and proves the factorizations by trial division, rather than assuming numerical values. The standard integral resultant identity supplies polynomials \(U_h,V_h\in\mathbb Z[X]\) such that \(U_hF+V_hF(X+h)=R_h\). Consequently,
\[
\gcd(F(n+i),F(n+j))\mid R_{j-i}\qquad(0\le i<j\le k).
\]

If an odd prime \(p\) divides \(F(t)\), then \(t^4\equiv-1\pmod p\), whence the residue of \(t\) has multiplicative order exactly eight. Thus \(p\equiv1\pmod8\). Inspection of the factored five resultants therefore leaves, among odd primes, **only** \(17,97,641\). Moreover, each of these occurs to the *first power* in every resultant in which it appears; hence the common \(p\)-valuation of any two distinct entries of a window is at most one.

**2. Classify the close collisions.** Exhaustive, exact root calculations in these three finite prime fields give
\[
\begin{array}{c|l}
p&\{x\bmod p:F(x)\equiv0\pmod p\}\\\hline
17&\{2,8,9,15\}\\
97&\{33,47,50,64\}\\
641&\{256,318,323,385\}
\end{array}
\]
Among ordered pairs of roots with positive separation at most five (without wrapping the integer gap), the entire list is
\[
(p,\text{initial root},\text{gap})=(17,8,1),\ (17,15,4),\ (97,47,3),\ (641,318,5).
\]
For a length-at-most-six window, no three entries can be roots of the same prime. A \(p\)-factor appears in the product-over-lcm precisely when two distinct entries share \(p\). Because their common \(p\)-valuation is exactly one, the total \(p\)-valuation of \(G_k(n)\) is precisely one in that case and zero otherwise. The allowed start positions for each of the four listed root-pair types are exactly the residue sets \(A_k,B_k,C_k\) in the finding.

**3. The power of two.** For even \(t\), \(F(t)\) is odd; for odd \(t\), \(t^4\equiv1\pmod{16}\), so \(v_2(F(t))=1\). A window of at least two successive integers contains at least one odd integer. Subtracting the largest entry valuation from their sum gives \(v_2(G_k(n))=o_k(n)-1\). Combining with Step 2 proves the formula for **all** \(n,k\) in the stated range.

**4. Exact least periods.** The nontrivial prime indicators have nonempty proper support modulo their respective primes, with support sizes
\[
\begin{array}{c|ccccc}
k&1&2&3&4&5\\\hline
|A_k|&1&2&3&5&7\\
|B_k|&0&0&1&2&3\\
|C_k|&0&0&0&0&1
\end{array}
\]
Each nonconstant indicator of residue modulo a prime \(p\) has least period \(p\). For the factor \(2^{o_k(n)-1}\), the exponent is constant at \(k=1,3,5\) (respectively zero, one, two), but alternates with period two at \(k=2,4\). Distinct prime valuations of \(G_k(n)\) recover these indicators individually. Therefore any period of \(G_k\) must be divisible by each active prime and, in the alternating cases, by two; their product is also manifestly a period. This proves exactly the displayed five least periods.

**5. Complete six-term value frequencies.** For \(k=5\), \(o_5(n)=3\) always, so every value has an initial factor four. The sets \(A_5,B_5,C_5\) have sizes \(7,3,1\) in moduli \(17,97,641\). By the Chinese remainder theorem, each of the eight independent indicator combinations has count equal to the product of the selected set sizes (respectively their complements \(10,94,640\)). These eight counts are the displayed table; they sum to the least period \(17\cdot97\cdot641=1057009\). Each count is positive, so all eight values genuinely occur.

## Verification

The standalone `CHECKER.py` uses only the Python standard library. Running `python3 CHECKER.py` computes all five Sylvester determinants with the fraction-free Bareiss algorithm; verifies their exact prime factorizations; exhausts all roots and close-root pairs modulo \(17,97,641\); independently evaluates product and least common multiple against the formula for \(25000\) starts for each of \(k=1,2,3,4\) and \(60000\) starts at \(k=5\); enumerates all \(1057009\) residues for the value-frequency table; and supplies a witness showing each proper maximal divisor of every period is not a period. The observed terminal marker is `VERIFY_OK`. The finite checks corroborate the resultant tables and arithmetic; the mathematical argument above, not finite sampling, proves the universal formulas and minimality.

## Relationship to prior work

Farhi and Kane (2008) determined exact periods for the corresponding quotients of consecutive **linear** integer values. Hong and Qian (2009) extended exact-period analysis to linear arithmetic progressions. Hong and Qian (2012) treated **quadratic** polynomial values, and Lin and Hong (2020) studied a **cubic** polynomial progression. Those results do not claim these cyclotomic-quartic five least periods or the six-term eight-value distribution. Bodin and Drouin (2024) give general resultant/gcd methods; the present use of resultants is consistent with that framework, but the exact prime-collision taxonomy, periods, and counts are concrete information not supplied by their general results. No broader theorem in the inspected sources was found that directly implies the numerical classification.

## Limitations

The exact classification is restricted to \(k\le5\), not all window lengths or arbitrary quartic polynomials. The earliest new collision at gap five is tied to the exceptional prime \(641\); longer gaps may introduce further primes and higher valuations. The arithmetic proof is self-contained apart from the standard resultant identity and the Chinese remainder theorem. A literature or database result not surfaced by the specified searches might already contain some or all of this exact example; the search is not a uniqueness theorem.

## References

1. B. Farhi and D. Kane, *New results on the least common multiple of consecutive integers*, arXiv:0808.1507 (first posted August 11, 2008), https://arxiv.org/abs/0808.1507.
2. S. Hong and G. Qian, *The least common multiple of consecutive arithmetic progression terms*, arXiv:0903.0530 (first posted March 3, 2009), https://arxiv.org/abs/0903.0530.
3. S. Hong and G. Qian, *The least common multiple of consecutive quadratic progression terms*, arXiv:1208.5119 (first posted August 25, 2012), https://arxiv.org/abs/1208.5119.
4. Lin and Hong, *The least common multiple of consecutive terms in a cubic progression*, Mathematics 8 (2020), DOI:10.3934/math.2020119, https://doi.org/10.3934/math.2020119.
5. A. Bodin and A. Drouin, *Around the gcd of the values of two polynomials*, arXiv:2409.01224 (2024), https://arxiv.org/abs/2409.01224.

# The first-order prime-power discrepancy of hook and core Euler products

## Finding

Let \(E(q)=\prod_{n\ge1}(1-q^n)\) in \(\mathbb Z[[q]]\). For a prime \(p\), integer \(a\ge1\), and \(t=p^a\), define
\[
 F_t(q)=E(q)^{t^2-1}=\sum_{n\ge0}A_t(n)q^n,\qquad
 C_t(q)=\frac{E(q^t)^t}{E(q)}=\sum_{n\ge0}B_t(n)q^n.
\]
Let \(\sigma_1(m)=\sum_{d\mid m}d\), and in \(\mathbb F_p[[q]]\) define the (coefficientwise well-defined) Lambert series
\[
 \mathscr L_{p,a}(q)=
 \sum_{\substack{m\ge1\\p\nmid m}}
 \bigl(\sigma_1(m)m^{-1}\bmod p\bigr)
 \sum_{j\ge a-1}q^{mp^j}.
\]
The **complete first-order coefficientwise discrepancy** is
\[
 \boxed{\quad
 \sum_{n\ge0}\frac{A_t(n)-B_t(n)}{p^{a+1}}q^n
 \equiv -\frac{E(q^{p^{2a}})}{E(q)}\,\mathscr L_{p,a}(q)
 \pmod p.\quad}
\]
This states both the integrality of every coefficient on the left and its exact residue modulo \(p\), for every prime \(p\), every \(a\ge1\), and every \(n\ge0\). In particular, the first nonzero coefficient modulo \(p\) occurs at degree \(p^{a-1}\), with residue \(-1\).

## Assumptions and scope

All power series are formal; the quotient by a series with constant coefficient one is well-defined. The symbol \(m^{-1}\bmod p\) is used only when \(p\nmid m\). For finite computation the Euler powers are polynomials truncated at a stated degree; the assertion above is infinite and requires no truncation. There is no restriction to odd primes. These Euler products are the standard generating series attached respectively to Nekrasov--Okounkov hook-length coefficients and to \(t\)-core partitions.

## Proof

Set \(s=p^a\) and introduce the unit series
\[
 U(q)=\frac{E(q)^{p^{2a}}}{E(q^{p^a})^{p^a}}.
\]
The defining expressions give \(F_t=C_tU\), hence \(F_t-C_t=C_t(U-1)\). Since \(E\in1+q\mathbb Z[[q]]\), all identities may be computed in \(\mathbb Q_p[[q]]\), and the logarithm is well-defined formally. The classical logarithmic derivative of Euler's product gives
\[
 \log E(q)=-\sum_{n\ge1}\frac{\sigma_1(n)}n q^n.
\]
Consequently,
\[
 \log U(q)=-p^{2a}\sum_{n\ge1}\frac{\sigma_1(n)}n q^n
 +p^a\sum_{n\ge1}\frac{\sigma_1(n)}n q^{p^a n}.
\]
Write a positive degree uniquely as \(n=p^ju\), with \(p\nmid u\), and put \(S_j=1+p+\cdots+p^j\). Multiplicativity of \(\sigma_1\) yields \(\sigma_1(p^ju)=S_j\sigma_1(u)\). If \(j<a\), the coefficient at degree \(n\) is exactly
\[
 -p^{2a-j}S_j\frac{\sigma_1(u)}u.
\]
If \(j\ge a\), subtracting the two divisor sums instead gives
\[
 -p^{2a-j}(S_j-S_{j-a})\frac{\sigma_1(u)}u
 =-p^{a+1}S_{a-1}\frac{\sigma_1(u)}u.
\]
In the boundary case \(j=a-1\), the first expression equals the same latter expression. For \(j\le a-2\), the coefficient is divisible by \(p^{a+2}\). Thus every coefficient of \(\log U\) is divisible by \(p^{a+1}\) in \(\mathbb Z_p\), and
\[
 \frac{\log U(q)}{p^{a+1}}\equiv-\mathscr L_{p,a}(q)\pmod p
\]
because \(S_{a-1}\equiv1\pmod p\).

We next justify passing from the logarithm to the series itself, including \(p=2\). The coefficient of any term of order \(k\ge2\) in \(\exp(\log U)\) has valuation at least \(k(a+1)-\nu_p(k!)\). Since \(\nu_p(k!)\le k-1\), this is at least \(a+2\) for every \(k\ge2\) and \(a\ge1\). Hence
\[
 U(q)\equiv1+\log U(q)\pmod {p^{a+2}},
 \qquad
 \frac{U(q)-1}{p^{a+1}}\equiv-\mathscr L_{p,a}(q)\pmod p.
\]
Finally, the freshman's-dream identity in \(\mathbb F_p[[q]]\) gives
\[
 C_t(q)=\frac{E(q^{p^a})^{p^a}}{E(q)}
 \equiv\frac{E(q^{p^{2a}})}{E(q)}\pmod p.
\]
Multiplying the last two congruences proves the boxed claim. The smallest exponent appearing in \(\mathscr L_{p,a}\) is \(p^{a-1}\), contributed only by \(u=1,j=a-1\) with coefficient one. The prefactor has constant coefficient one, so the normalized discrepancy vanishes at all smaller degrees and equals \(-1\) at this degree. This also confirms the attained power \(p^{a+1}\).

## Verification

The attached standalone `verify.py` uses only the Python standard library. It constructs \(E(q)^k\) with the exact recurrence
\[
 n[q^n]E(q)^k=-k\sum_{j=1}^n\sigma_1(j)[q^{n-j}]E(q)^k
\]
and multiplies series by exact integer convolutions. For nine parameter choices
\[
 (p,a)\in\{(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2),(7,1),(11,1)\},
\]
it checks every index \(0\le n\le96\) for divisibility by \(p^{a+1}\), agreement of the normalized difference with the proposed series modulo \(p\), and the sharp first index. The exact output is `VERIFY_OK cases=9 coefficients=873 max_index=96`. The infinite theorem follows from the proof above, not from this bounded check.

## Relationship to prior work

Sharma's 2026 preprint studies the prime-power criterion for coefficientwise congruence between these hook and core generating functions, and establishes the prime-case refinement modulo \(p^2\). An earlier exact coefficient-gcd and first-witness statement settles the **largest common power** \(p^{a+1}\) and the first sharp degree \(p^{a-1}\); those facts alone do not specify the infinite sequence of residues after normalization. The formula proved here instead recovers that entire first-order residue series, through a prime-adically filtered divisor-sum Lambert series, for all primes and all exponents. Han's foundational work gives the Euler-product/hook-length setting but does not in its accessible description state this first-order congruence. General Euler-product logarithmic identities are used explicitly as established techniques, not claimed as discoveries.

## Limitations

No claim is made about the next \(p\)-adic layer modulo \(p^2\) after normalization or about asymptotic statistics of nonzero residues. The motivating preprint's full text was not accessible in the present comparison, so an implicit or explicit earlier appearance of this coefficientwise first-order refinement remains a material originality risk. The comparison of accessible results and records does not establish global uniqueness, and independent mathematical review has not been performed.

## References

1. M. Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and \(t\)-Core Partitions*, arXiv:2610.01422 (first public version 2026-10-01), https://arxiv.org/abs/2610.01422.
2. G.-N. Han, *The Nekrasov-Okounkov hook length formula: refinement, elementary proof, extension and applications*, Ann. Inst. Fourier **60** (2010), 1–29, https://doi.org/10.5802/aif.2515.
3. G.-N. Han, *An explicit expansion formula for the powers of the Euler Product in terms of partition hook lengths*, arXiv:0804.1849.

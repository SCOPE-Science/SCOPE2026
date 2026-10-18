# Density-one common divisors for consecutive central Delannoy numbers

## Finding

Define the central Delannoy numbers by
\[
D_n=\sum_{k=0}^{n}\binom{n}{k}^{2}2^k\qquad(n\ge0).
\]
For any odd prime \(p\), put
\[
Z_p=\{a\in\{0,1,\ldots,p-1\}:D_a\equiv0\pmod p\},
\qquad z_p=|Z_p|.
\]
Then \(0,p-1\notin Z_p\), no two members of \(Z_p\) are consecutive, and \(0\le z_p\le(p-1)/2\). For every integer \(L\ge1\), the **exact number of indices** \(0\le n<p^L\) for which \(p\nmid\gcd(D_n,D_{n+1})\) is
\[
E_p(L)=1+(p-1)\sum_{h=0}^{L-1}(p-z_p)^h
=1+\frac{(p-1)((p-z_p)^L-1)}{p-z_p-1}.
\]
In particular, every prime \(p\equiv3\pmod4\) has \(z_p\ge1\), and hence
\[
\#\{0\le n<N:p\nmid\gcd(D_n,D_{n+1})\}
=O_p\bigl(N^{\log_p(p-z_p)}\bigr).
\]
Thus \(p\mid\gcd(D_n,D_{n+1})\) for a natural-density-one set of \(n\) for every such prime. Consequently, for every real \(B>0\),
\[
\lim_{N\to\infty}\frac1N\#\{0\le n<N:\gcd(D_n,D_{n+1})>B\}=1.
\]
Indeed, for any finite set of primes congruent to \(3\pmod4\), their product divides the gcd for a density-one set of indices. For the smallest prime, \(p=3\), one has \(Z_3=\{1\}\) and \(E_3(L)=2^{L+1}-1\).

## Assumptions and scope

All indices are nonnegative integers. Every prime is a positive rational prime; congruences are taken in \(\mathbb F_p\). Here \(p\nmid\gcd(D_n,D_{n+1})\) means that the two integers are not simultaneously divisible by \(p\), not that either one must be coprime to \(p\). Natural density uses arbitrary cutoffs \(N\), not only prime-power endpoints. The asymptotic estimate is asserted only when \(z_p>0\); for \(z_p=0\), no index has \(p\) dividing the gcd.

## Proof

**1. Lucas factorization.** Let \(n=\sum_{i\ge0}a_ip^i\) be the base-\(p\) expansion with \(0\le a_i<p\). Lucas's binomial congruence and Fermat's congruence give
\[
D_n\equiv\prod_{i\ge0}D_{a_i}\pmod p.\tag{1}
\]
Indeed, in the defining sum, write \(k=\sum k_ip^i\); Lucas's congruence factors \(\binom nk^2\), while \(2^k\) has the digit factorization \(2^k\equiv\prod_i2^{k_i}\pmod p\), since \(2^{p^i}\equiv2\pmod p\). Summation over the independent digits factors the sum. Zero padding is harmless since \(D_0=1\).

**2. Endpoint and adjacent-digit obstructions.** Clearly \(D_0=1\). For \(0\le k<p\), \(\binom{p-1}{k}\equiv(-1)^k\pmod p\), hence
\[
D_{p-1}\equiv\sum_{k=0}^{p-1}2^k=2^p-1\equiv1\pmod p.\tag{2}
\]
The constant-term representation \(D_n=[u^0](3+u+2/u)^n\) gives the generating function \(\sum_{n\ge0}D_nt^n=(1-6t+t^2)^{-1/2}\), by extracting the constant coefficient of \(1/(1-t(3+u+2/u))\). Comparison with the generating function of Legendre polynomials gives \(D_n=P_n(3)\). Its recurrence is
\[
(j+1)D_{j+1}=3(2j+1)D_j-jD_{j-1}\qquad(j\ge1).\tag{3}
\]
For any \(1\le j\le p-2\), simultaneous vanishing of \(D_j,D_{j+1}\) modulo \(p\) would force \(D_{j-1}\equiv0\pmod p\) because \(j\) is invertible. Repeating contradicts \(D_0=1\). Together with (2), this excludes adjacent zero digits and shows \(Z_p\subseteq\{1,\ldots,p-2\}\), with \(z_p\le(p-1)/2\).

**3. The exact adjacent-index test.** Fix \(n\ge0\), and let \(r\) be the number of trailing digits equal to \(p-1\) in its base-\(p\) expansion. The digits of \(n+1\) have zeroes below position \(r\), the digit at \(r\) increases from \(a_r\) to \(a_r+1\) (where \(0\le a_r\le p-2\)), and every digit above \(r\) is unchanged. The trailing digits are all nonzero with respect to (1) by (2); the pair \(a_r,a_r+1\) cannot both belong to \(Z_p\). Therefore
\[
p\mid\gcd(D_n,D_{n+1})
\iff \text{some unchanged digit }a_j\in Z_p\text{ at a position }j>r.\tag{4}
\]
The definition of \(r\) also applies to the finite base-\(p\) expansion when a higher digit is zero: the implicit leading zeros are non-roots.

**4. Counting exact digit blocks.** For \(0\le n<p^L\), either \(n=p^L-1\), which has no common factor \(p\) by (2), or its first non-\((p-1)\) digit is at a unique position \(r\in\{0,\ldots,L-1\}\). In the latter case there are \(p-1\) choices for \(a_r\), the \(r\) trailing digits are prescribed, and each of the \(L-r-1\) higher digits has exactly \(p-z_p\) choices for avoiding the simultaneous divisibility in (4). Thus the number with no common factor is precisely
\[
1+\sum_{r=0}^{L-1}(p-1)(p-z_p)^{L-r-1},
\]
which is \(E_p(L)\) as stated. Its denominator \(p-z_p-1\) is positive, including at \(p=3\).

**5. A guaranteed zero digit for primes \(3\pmod4\).** Put \(m=(p-1)/2\) and
\[
H_m(X)=\sum_{j=0}^m\binom mj^2X^j.
\]
Its coefficients satisfy the exact differential equation
\[
X(1-X)H_m''+[1+(2m-1)X]H_m'-m^2H_m=0.\tag{5}
\]
Because \(2m\equiv-1\pmod p\), this becomes
\[
X(1-X)H_m''+(1-2X)H_m'-m^2H_m=0\pmod p.\tag{6}
\]
Equation (6) is invariant under replacing \(X\) by \(1-X\). Among polynomials of degree at most \(m\), its solutions are determined by their constant coefficient: the coefficient of \(X^j\), for \(0\le j<m\), determines the next coefficient through the invertible factor \((j+1)^2\pmod p\). Moreover,
\[
H_m(1)=\binom{2m}{m}=\binom{p-1}{m}\equiv(-1)^m\pmod p.
\]
Thus uniqueness gives the polynomial identity
\[
H_m(1-X)\equiv(-1)^mH_m(X)\pmod p.\tag{7}
\]
If \(p\equiv3\pmod4\), then \(m\) is odd and the pairing \(j\leftrightarrow m-j\) in the sum yields \(H_m(-1)=0\) **as an integer**. Evaluate (7) at \(X=2\) to obtain \(D_m=H_m(2)\equiv0\pmod p\). Therefore \(m\in Z_p\) and \(z_p\ge1\) for every such prime.

**6. Arbitrary cutoffs and unbounded common divisors in density.** If \(z_p\ge1\), let \(\alpha_p=\log_p(p-z_p)<1\). Given \(N\ge1\), choose \(L\) with \(p^{L-1}\le N<p^L\). Monotonicity and the exact block formula show that the number of exceptions below \(N\) is \(O_p((p-z_p)^L)=O_p(N^{\alpha_p})\). Hence divisibility of both neighboring terms by this prime has natural density one. Finite intersections of density-one sets still have density one. Since infinitely many primes are \(3\pmod4\), for any prescribed \(B>0\) choose one such prime exceeding \(B\). Its density-one divisibility assertion implies the claimed divergence of \(\gcd(D_n,D_{n+1})\) in natural density. (Infinitely many such primes follow directly by applying prime factorization to \(4p_1\cdots p_t-1\) under an assumed finite list.)

## Verification

A standalone standard-library checker, `verify.py`, replays independent finite consequences of (1)--(7): direct coefficients versus the recurrence, Lucas digit products, the finite-field polynomial involution, the nonadjacent zero sets, and the exact counts for complete small prime-power blocks. Run `python3 verify.py` and expect `VERIFY_OK`. The finite computations are regression checks; all infinite quantifiers follow from the preceding algebraic proof.

## Relationship to prior work

Central Delannoy numbers and their congruences have a substantial literature. Sun's *On Delannoy numbers and Schröder numbers* (2010 first public version, subsequently 2011 journal) studies weighted reciprocal prime sums and the central Delannoy sequence; it does not give the adjacent gcd count. Sun's *Arithmetic properties of Delannoy numbers and Schröder numbers* (2016 first public version) proves polynomial identities and supercongruences, but the examined text does not state this digitwise adjacent-gcd classification. Lengyel's *On some p-adic properties and supercongruences of Delannoy and Schröder numbers* (2021) studies individual special-index congruences and differences of prime-power-indexed terms, notably Theorems 13–14, not adjacent gcd at arbitrary indices. Rowland and Yassawi's automatic-congruence framework establishes broader automaticity and Lucas-type methods; such ingredients motivate (1) but do not supply the evaluated formula (4), its exact fiber count, or the density-one gcd divergence. OEIS A001850 tabulates the central Delannoy sequence, not these consecutive gcd statistics. The guaranteed middle-digit root and polynomial symmetry in step 5 are proved here and are not represented as new general theories of Deuring polynomials. A separate accessible result on least periods modulo powers of two concerns different moduli and a different invariant.

## Limitations

This theorem does not classify the set \(Z_p\) explicitly for every odd prime, nor the valuations \(\nu_p(\gcd(D_n,D_{n+1}))\). Its exact formula is expressed in the natural local invariant \(z_p\), which can be evaluated by \(p\) finite Delannoy residues. The growth is in natural density, not a pointwise lower bound for every sufficiently large index. No claim of independent verification or exhaustive proof of novelty is made. An earlier equivalent gcd-density statement in unindexed literature or a stronger published implication remains possible.

## References

1. Zhi-Wei Sun, *On Delannoy numbers and Schröder numbers*, arXiv:1009.2486, first posted 2010-09-13; *Journal of Number Theory* 131 (2011), 2387–2397. https://arxiv.org/abs/1009.2486
2. Zhi-Wei Sun, *Arithmetic properties of Delannoy numbers and Schröder numbers*, arXiv:1602.00574, first posted 2016-02-01. https://arxiv.org/abs/1602.00574
3. Eric Rowland and Reem Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, first posted 2013-10-31. https://arxiv.org/abs/1310.8635
4. Tamás Lengyel, *On some p-adic properties and supercongruences of Delannoy and Schröder numbers*, *Integers* 21 (2021), A86. https://sites.oxy.edu/lengyel/morepapers.html
5. *The On-Line Encyclopedia of Integer Sequences*, A001850 (central Delannoy numbers). https://oeis.org/A001850

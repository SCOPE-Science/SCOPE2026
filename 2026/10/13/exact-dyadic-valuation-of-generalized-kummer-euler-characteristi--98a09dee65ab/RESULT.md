# Exact dyadic valuation of generalized Kummer Euler characteristics
## Finding
Let \(A\) be a complex abelian surface. For an integer
\[
m\ge2,
\]
define the generalized Kummer variety
\[
K_m(A)
=
\left\{
\xi\in A^{[m]}:
\sum_{x\in\operatorname{Supp}(\xi)}
\operatorname{mult}_x(\xi)\,x=0
\right\}.
\]
Thus
\[
\dim_{\mathbb C}K_m(A)=2m-2.
\]

Write the prime factorization of \(m\) as
\[
m=2^a\prod_{i=1}^r p_i^{e_i},
\]
where the \(p_i\) are odd primes. Then
\[
\boxed{
\nu_2\!\left(\chi_{\mathrm{top}}(K_m(A))\right)
=
3a+
\sum_{\substack{1\le i\le r\\ e_i\ \mathrm{odd}}}
\left(
\nu_2(p_i+1)+\nu_2(e_i+1)-1
\right)
}.
\]

In particular,
\[
\boxed{
\chi_{\mathrm{top}}(K_m(A))\ \text{is odd}
\iff
m\ \text{is an odd perfect square}.
}
\]

The first positive-dimensional odd case is
\[
m=9,
\]
for which
\[
\dim_{\mathbb C}K_9(A)=16
\]
and
\[
\chi_{\mathrm{top}}(K_9(A))
=
9^3(1+3+9)
=
9477.
\]

## Assumptions and scope
The base field is \(\mathbb C\), and \(A\) is an abelian surface. The Euler characteristic is the ordinary topological Euler characteristic.

The notation \(K_m(A)\) is fixed here by the displayed Hilbert-scheme fiber definition. Some sources shift the Kummer index by one; the parameter \(m\) in this note is the length of the zero-dimensional subscheme.

The geometric input is the classical formula
\[
\chi_{\mathrm{top}}(K_m(A))
=
m^3\sigma(m),
\]
where
\[
\sigma(m)=\sum_{d\mid m}d.
\]
The new statement is the exact two-adic decomposition of this Euler characteristic and its complete parity classification.

## Proof
Debarre, Göttsche--Soergel, and later Gulbrandsen prove
\[
\chi_{\mathrm{top}}(K_m(A))
=
m^3\sigma(m).
\]
Therefore
\[
\nu_2\!\left(\chi_{\mathrm{top}}(K_m(A))\right)
=
3\nu_2(m)+\nu_2(\sigma(m)).
\]

Write
\[
m=2^a\prod_i p_i^{e_i},
\]
with every \(p_i\) odd. Since the divisor-sum function is multiplicative,
\[
\sigma(m)
=
\sigma(2^a)\prod_i\sigma(p_i^{e_i}).
\]
The factor
\[
\sigma(2^a)=2^{a+1}-1
\]
is odd, so it contributes no power of two.

Fix an odd prime \(p\) and an exponent \(e\ge1\). If \(e\) is even, then
\[
\sigma(p^e)=1+p+\cdots+p^e
\]
is a sum of \(e+1\) odd terms, with \(e+1\) odd. Hence
\[
\nu_2(\sigma(p^e))=0.
\]

Now suppose \(e\) is odd. Then
\[
\sigma(p^e)=\frac{p^{e+1}-1}{p-1}.
\]
Because \(e+1\) is even, the standard two-adic lifting-the-exponent identity gives
\[
\nu_2(p^{e+1}-1)
=
\nu_2(p-1)+\nu_2(p+1)+\nu_2(e+1)-1.
\]
Subtracting \(\nu_2(p-1)\) yields
\[
\nu_2(\sigma(p^e))
=
\nu_2(p+1)+\nu_2(e+1)-1.
\]
Summing these local contributions proves the exact formula.

For parity, the valuation vanishes precisely when
\[
a=0
\]
and every exponent \(e_i\) is even. This is exactly the condition that \(m\) be an odd perfect square.

## Verification
The bundled checker independently factors every integer
\[
2\le m\le100000,
\]
computes
\[
m^3\sigma(m)
\]
exactly, and compares its direct two-adic valuation with the closed prime-factor formula above.

It also verifies that the odd values in this range occur exactly at odd squares, and separately checks the local prime-power valuation identity for odd primes and exponents in a finite test range.

These computations are regression evidence only. The theorem for all \(m\) follows from the geometric Euler formula, multiplicativity of \(\sigma\), and the two-adic lifting-the-exponent identity.

## Relationship to prior work
Debarre's archival paper computes the Euler characteristic of generalized Kummer varieties and concludes that it is
\[
m^3\sigma(m).
\]
Gulbrandsen later gives an elementary proof of exactly the same formula, while Shen places it inside a broader generating-function theory for generalized Kummer schemes.

Those sources determine the integer itself but do not, in the inspected full texts, state its exact two-adic valuation, a parity theorem, or the odd-square classification. Targeted literature searches using generalized Kummer, Euler characteristic, parity, oddness, two-adic valuation, divisor sums, and odd squares likewise did not locate an equivalent statement.

The arithmetic step is not a finite pattern extraction: it is a prime-by-prime factorization of the published geometric formula.

## Limitations
The statement concerns only the ordinary topological Euler characteristic. It does not classify two-adic valuations of individual Betti numbers, Hodge numbers, elliptic genera, or other refined invariants.

The result is a concise arithmetic consequence of the classical Euler formula. An older or unindexed source may contain the same consequence without using two-adic or parity terminology.

The formula is specific to generalized Kummer varieties attached to abelian surfaces; higher-dimensional generalized Kummer schemes have different Euler formulas.

## References
Olivier Debarre, *On the Euler Characteristic of Generalized Kummer Varieties*, arXiv:alg-geom/9711035, first submitted 28 November 1997; *American Journal of Mathematics* 121 (1999), 577--586, DOI 10.1353/ajm.1999.0018.

Martin G. Gulbrandsen, *Computing the Euler Characteristic of Generalized Kummer Varieties*, *Arkiv för Matematik* 45 (2007), 49--60, DOI 10.1007/s11512-006-0032-7.

Junliang Shen, *The Euler Characteristics of Generalized Kummer Schemes*, arXiv:1502.03973, first submitted 13 February 2015; *Mathematische Zeitschrift* 281 (2015), 1183--1189.

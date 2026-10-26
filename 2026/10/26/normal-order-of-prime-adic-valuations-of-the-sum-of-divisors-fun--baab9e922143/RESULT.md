# Normal order of prime-adic valuations of the sum-of-divisors function

## Finding

For every fixed prime \(\ell\), let \(\nu_\ell(m)\) be the exponent of \(\ell\) in a positive integer \(m\), and let \(\sigma(n)=\sum_{d\mid n}d\). Then

\[
\nu_\ell(\sigma(n))=\left(\frac{\ell}{(\ell-1)^2}+o(1)\right)\log\log n
\]

for a set of integers of natural density one. Equivalently, for every fixed \(\varepsilon>0\),

\[
\lim_{x\to\infty}\frac1x\#\left\{3\le n\le x:\left|\frac{\nu_\ell(\sigma(n))}{\log\log n}-\frac{\ell}{(\ell-1)^2}\right|>\varepsilon\right\}=0.
\]

The prime \(\ell\) is fixed throughout; the result asserts no uniformity as \(\ell\) varies.

## Assumptions and scope

All logarithms are natural. The phrase “normal order” means convergence in natural density, not pointwise convergence and not an asymptotic valid for every integer. The statement applies separately to each fixed prime \(\ell\), including \(\ell=2\), for which the constant is \(2\).

## Proof

Define the strongly additive function

\[
g_\ell(n)=\sum_{p\mid n}\nu_\ell(p+1).
\]

Since \(\sigma\) is multiplicative,

\[
\nu_\ell(\sigma(n))=\sum_{p^e\parallel n}\nu_\ell(\sigma(p^e)).
\]

For \(e=1\), the local term is exactly \(\nu_\ell(p+1)\). For \(e\ge2\), the difference between \(\nu_\ell(\sigma(p^e))\) and \(\nu_\ell(p+1)\) is bounded in absolute value by \(C_\ell e\log p\). Also, at most \(x/p^e\) integers up to \(x\) have exact exponent \(e\) at \(p\). Consequently,

\[
\frac1{\lfloor x\rfloor}\sum_{n\le x}\left|\nu_\ell(\sigma(n))-g_\ell(n)\right|
\ll_\ell \sum_p\sum_{e\ge2}\frac{e\log p}{p^e}<\infty.
\]

Thus the difference is \(o(\log\log n)\) in natural density, by Markov's inequality.

It remains to find the normal order of \(g_\ell\). For a fixed integer \(J\ge1\), truncate the prime values by setting

\[
g_{\ell,J}(n)=\sum_{p\mid n}\min\{\nu_\ell(p+1),J\}.
\]

This is a strongly additive function with bounded prime values. Since

\[
\min\{\nu_\ell(p+1),J\}=\sum_{j=1}^{J}\mathbf 1_{p\equiv-1\pmod{\ell^j}},
\]

Mertens' theorem for primes in a fixed reduced residue class gives

\[
\sum_{p\le x}\frac{\min\{\nu_\ell(p+1),J\}}p
=\left(\sum_{j=1}^{J}\frac1{\varphi(\ell^j)}\right)\log\log x+O_{\ell,J}(1).
\]

The Turán–Kubilius inequality therefore implies that, for each fixed \(J\), \(g_{\ell,J}(n)\) has normal order \(c_{\ell,J}\log\log n\), where

\[
c_{\ell,J}=\sum_{j=1}^{J}\frac1{\varphi(\ell^j)}.
\]

The discarded tail is nonnegative and has mean bounded by

\[
\frac1x\sum_{n\le x}(g_\ell(n)-g_{\ell,J}(n))
\le\sum_{j>J}\sum_{\substack{p\le x\\p\equiv-1\pmod{\ell^j}}}\frac1p.
\]

A uniform Brun–Titchmarsh bound for moduli \(\ell^j\le x^\delta\), together with the elementary estimate for \(\ell^j>x^\delta\), bounds this by \(O_\ell(\ell^{-J}\log\log x)+o(\log\log x)\), for any fixed \(0<\delta<1\). Markov's inequality lets \(J\to\infty\) after \(x\to\infty\). Hence \(g_\ell\) has normal order

\[
\left(\sum_{j=1}^{\infty}\frac1{\varphi(\ell^j)}\right)\log\log n
=\frac{\ell}{(\ell-1)^2}\log\log n,
\]

because \(\varphi(\ell^j)=\ell^{j-1}(\ell-1)\). Combining this with the bounded-mean comparison proves the claim.

## Verification

The proof uses multiplicativity of \(\sigma\), the standard Mertens estimate in fixed reduced residue classes, the Turán–Kubilius inequality for bounded strongly additive functions, a uniform Brun–Titchmarsh tail estimate, and Markov's inequality. The constant is the convergent Euler-class sum \(\sum_{j\ge1}1/\varphi(\ell^j)=\ell/(\ell-1)^2\). No finite computation is used as evidence for an infinite statement.

## Relationship to prior work

A public note dated 2026-10-04, “Exact 5-divisibility criterion for the sum-of-divisors function,” gives a density-one criterion for \(5\mid\sigma(n)\) and a refinement for the case \(\nu_5(\sigma(n))=1\); those statements do not determine a normal-order constant. Amdeberhan, Moll, Sharma, and Villamizar derive local formulas for \(\nu_\ell(\sigma(n))\) and valuation bounds, but do not state the normal order proved here. The present result combines the prime-power local comparison with the normal-order theory of additive functions; it is not a claim of uniformity in \(\ell\).

## Limitations

The theorem gives a density-one asymptotic only for each fixed prime. It does not give an explicit exceptional-set bound, a distribution theorem on the scale \(\sqrt{\log\log n}\), or uniformity in the prime \(\ell\). The tail estimate relies on standard uniform prime-progression bounds; constants may depend on \(\ell\).

## References

1. T. Amdeberhan, V. H. Moll, V. Sharma, and D. Villamizar, “Arithmetic properties of the sum of divisors,” arXiv:2007.03088 (submitted 2020-07-06). The full text gives local valuation formulas in Theorems 1.1–1.2: https://arxiv.org/abs/2007.03088.
2. G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, 3rd ed., Graduate Studies in Mathematics 163, American Mathematical Society, 2015 (Mertens estimates in arithmetic progressions and the Turán–Kubilius inequality).
3. “Exact 5-divisibility criterion for the sum-of-divisors function,” public research note dated 2026-10-04 (local criterion and density-one divisibility statement; no normal-order constant stated).

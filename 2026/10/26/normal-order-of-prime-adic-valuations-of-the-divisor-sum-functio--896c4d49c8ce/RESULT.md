# Normal order of prime-adic valuations of the divisor-sum function

## Finding
For every fixed prime \(p\), the normal order of the valuation of the divisor-sum function is

\[
\nu_p(\sigma(n))=\left(\frac{p}{(p-1)^2}+o(1)\right)\log\log n.
\]

Precisely, if \(C_p=p/(p-1)^2\), then for each \(\varepsilon>0\),

\[
\#\left\{n\le x:\left|\frac{\nu_p(\sigma(n))}{C_p\log\log n}-1\right|>\varepsilon\right\}=o(x).
\]

Here \(p\) is fixed as \(x\to\infty\); no uniformity in a prime \(p=p(x)\) is asserted.

## Assumptions and scope
Write \(\sigma(n)=\sum_{d\mid n}d\), and let \(\nu_p(m)\) be the exponent of \(p\) in a positive integer \(m\). “Normal order” means that the displayed estimate holds outside a set of natural density zero. The proof uses the prime number theorem in fixed arithmetic progressions, the Brun–Titchmarsh inequality for a uniform tail bound, and the Turán–Kubilius inequality for strongly additive functions. These are used in their standard forms. The statement concerns the first-order typical size only; it gives neither a second-order term nor a central limit theorem.

## Proof
Set
\[
f_p(n)=\nu_p(\sigma(n)),\qquad a_q=\nu_p(q+1),\qquad F_p(n)=\sum_{q\mid n}a_q,
\]
where sums over \(q\) are over primes. Since \(\sigma\) is multiplicative,
\[
f_p(n)=\sum_{q^a\parallel n}g_p(q,a),\qquad g_p(q,a)=\nu_p(1+q+\cdots+q^a).
\]
For every prime \(q\) and \(a\ge1\),
\[
0\le g_p(q,a)\le \log_p\sigma(q^a)\le a\log_p q+\log_p(a+1).
\]
Consequently,
\[
\sum_q\sum_{a\ge2}\frac{g_p(q,a)+a_q}{q^a}<\infty,
\]
because the summand is bounded by a constant depending on \(p\) times \((a\log q+\log(a+1))/q^a\), and the sum over prime powers with \(a\ge2\) converges. Counting integers divisible exactly by \(q^a\) therefore gives
\[
\frac1x\sum_{n\le x}|f_p(n)-F_p(n)|=O_p(1).
\]
Markov's inequality implies \(f_p(n)-F_p(n)=o(\log\log x)\) for all but \(o(x)\) integers \(n\le x\).

It remains to find the normal order of the strongly additive function \(F_p\). Put
\[
S_j(x)=\sum_{\substack{q\le x\;q\text{ prime}\\q\equiv-1\pmod{p^j}}}\frac1q.
\]
Since \(a_q=\sum_{j\ge1}\mathbf1_{q\equiv-1\, (\mathrm{mod}\,p^j)}\),
\[
A_p(x):=\sum_{q\le x}\frac{a_q}{q}=\sum_{j\ge1}S_j(x).
\]
For each fixed \(j\), Mertens' theorem for primes in arithmetic progressions gives
\[
S_j(x)=\frac{\log\log x}{\varphi(p^j)}+O_{p,j}(1).
\]
To justify summing the coefficients, split the tail at \(p^j=\sqrt{x}\). For \(p^j\le\sqrt{x}\), the integers in the progression below \(p^{2j}\) contribute \(O(j/p^j)\) by direct summation, and Brun–Titchmarsh with partial summation bounds the part above \(p^{2j}\) by \(O(\log\log x/\varphi(p^j))\). For \(p^j>\sqrt{x}\), direct counting gives an unweighted total \(O_p(1)\). For the weighted tail needed below, dyadic Brun–Titchmarsh bounds give \(S_j(x)\ll (\log x)/\varphi(p^j)\) when \(p^j\le x/2\), while \(S_j(x)\ll 1/x\) when \(p^j>x/2\); hence \(\sum_{p^j>\sqrt{x}}jS_j(x)=o(1)\). Thus, for every fixed \(J\),
\[
\sum_{j>J}S_j(x)\ll_p \log\log x\sum_{j>J}\frac1{\varphi(p^j)}+O_p(1+Jp^{-J}).
\]
Taking first \(x\to\infty\) and then \(J\to\infty\) yields
\[
A_p(x)=\left(\sum_{j\ge1}\frac1{\varphi(p^j)}+o(1)\right)\log\log x
=\left(\frac{p}{(p-1)^2}+o(1)\right)\log\log x,
\]
since \(\varphi(p^j)=p^{j-1}(p-1)\).

Similarly, the identity \(a_q^2=\sum_{j=1}^{a_q}(2j-1)\) gives
\[
\sum_{q\le x}\frac{a_q^2}{q}=\sum_{j\ge1}(2j-1)S_j(x)\ll_p\log\log x,
\]
using the same estimate for \(p^j\le\sqrt{x}\), and the weighted high-modulus bound above; the series \(\sum_{j\ge1}j/\varphi(p^j)\) converges. The Turán–Kubilius inequality now implies
\[
\sum_{n\le x}|F_p(n)-A_p(x)|^2\ll_p x\log\log x.
\]
Chebyshev's inequality shows that \(F_p(n)=A_p(x)+o(\log\log x)\) outside a set of size \(o(x)\). For \(n\ge\sqrt{x}\), \(\log\log n\sim\log\log x\), while \(n<\sqrt{x}\) accounts for only \(o(x)\) integers. Thus \(F_p(n)=(C_p+o(1))\log\log n\) in natural density. The bounded-mean comparison between \(f_p\) and \(F_p\) transfers this normal order to \(\nu_p(\sigma(n))\), as claimed. ∎

## Verification
The local factor identity \(\sigma(q^a)=1+q+\cdots+q^a\) and additivity of \(\nu_p(\sigma(n))\) across coprime prime-power factors are exact. The coefficient comes from the convergent series \(\sum_{j\ge1}1/\varphi(p^j)=p/(p-1)^2\). The prime-power correction has bounded mean, and the variance proxy for \(F_p\) is \(O_p(\log\log x)\), which is sufficient for a normal-order conclusion by Chebyshev. No finite computation is used as evidence for the infinite statement.

## Relationship to prior work
Luca and Pomerance proved a density-one divisibility statement for \(\sigma(n)\) involving small prime powers; it gives a qualitative precursor but not the leading normal-order constant. Amdeberhan, Moll, Sharma, and Villamizar derived local formulas and pointwise upper bounds for \(\nu_p(\sigma(n))\). Zhao and Chen later established an unconditional pointwise ceiling bound and classified some equality cases. These works study local valuations or extreme values, rather than the normal order proved here. A search of the available research index found no exact match for the constant \(p/(p-1)^2\); this search is evidence of comparison, not a proof of uniqueness. The main residual risk is an unindexed treatment of this particular additive-function application.

## Limitations
The prime \(p\) is fixed. The proof does not provide an explicit error term uniform in \(p\), does not describe the second-order distribution, and does not prove an Erdős–Kac central limit theorem. The method depends on standard prime-distribution and additive-function theorems. An independent audit has not been performed.

## References
1. F. Luca and C. Pomerance, “The range of the sum-of-proper-divisors function,” *Acta Arithmetica* 168 (2015), 187–199. DOI: 10.4064/aa168-2-6. Preprint: https://math.dartmouth.edu/~carlp/LucaPomeranceAA.pdf.
2. T. Amdeberhan, V. H. Moll, V. Sharma, and D. Villamizar, “Arithmetic properties of the sum of divisors,” *Journal of Number Theory* 223 (2021), 325–349. Preprint first posted 2020: https://arxiv.org/abs/2007.03088.
3. J. Zhao and Y. Chen, “p-adic Valuation of the Sum of Divisors,” *Frontiers of Mathematics* 20 (2025), 795–827. DOI: 10.1007/s11464-023-0154-2.
4. G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, 3rd ed., American Mathematical Society, 2015.
5. H. Halberstam and H.-E. Richert, *Sieve Methods*, Academic Press, 1974.

# A finite-CRT proof of zero density for the divisor-sum GCD equality

## Finding
Let \(\sigma(n)\) be the sum of positive divisors of the positive integer \(n\), and put
\[
\mathscr A=\{m\in\mathbb N:\gcd(m,\sigma(m^2))=\gcd(m^2,\sigma(m^2))\}.
\]
Then
\[
\boxed{\lim_{X\to\infty}\frac{1}{X}\#\{m\le X:m\in\mathscr A\}=0.}
\]
This proves the zero-density assertion conjectured by Dris for this precise set. The proof obtains the limit from finite Chinese-remainder calculations; it does not assume independence among infinitely many prime conditions.

## Assumptions and scope
All integers \(m\) are positive; no squarefreeness, parity, or odd-perfect-number hypothesis is imposed. The variable \(X\) tends through positive real values. A set \(S\subseteq\mathbb N\) has upper natural density \(\overline d(S)=\limsup_{X\to\infty}\#(S\cap[1,X])/X\).

The only analytic number theory input is the classical divergence
\[
\sum_{q\ \mathrm{prime},\ q\equiv a\ (\mathrm{mod}\ b)}\frac1q=\infty
\]
for any fixed relatively prime residue class \(a\pmod b\). In particular, it applies both to \(q\equiv1\pmod6\) and to any nonzero cubic-root residue modulo such a prime. The density conclusion is qualitative, without a numerical convergence rate.

## Proof
For a prime \(\ell\), set \(\delta_\ell=(\ell-1)/\ell^2\). The integer condition \(\ell\parallel m\), meaning \(v_\ell(m)=1\), depends only on \(m\pmod{\ell^2}\), and has natural density \(\delta_\ell\), since exactly \(\ell-1\) residue classes modulo \(\ell^2\) have valuation one. For any finite set of distinct primes, these valuation-one events are independent under natural density by the Chinese remainder theorem.

**Lemma (a fixed bad prime has negligible coexistence with the equality).** If \(p\equiv1\pmod6\) is prime, then
\[
\overline d\{m\in\mathscr A:p\parallel m\}=0.
\]
Indeed, the cyclic group \((\mathbb Z/p\mathbb Z)^\times\) has an element \(r\) of exact order three, so \(r^2+r+1\equiv0\pmod p\), with \(r\not\equiv0\pmod p\). Let \(Q\) be any finite set of primes \(q\equiv r\pmod p\), excluding \(p\). Define the finite counting variable
\[
Z_Q(m)=\sum_{q\in Q}\mathbf1_{q\parallel m},
\qquad \mu_Q=\sum_{q\in Q}\delta_q.
\]
For uniformly distributed integers, the indicators are independent Bernoulli variables, so their mean is \(\mu_Q\) and their variance is
\[
V_Q=\sum_{q\in Q}\delta_q(1-\delta_q)\le\mu_Q.
\]
The prime reciprocal series in the class \(r\pmod p\) diverges. Since \(\delta_q=1/q-1/q^2\) and \(\sum_q1/q^2<\infty\), finite sets \(Q\) can be chosen with \(\mu_Q\to\infty\).

Suppose now that \(p\parallel m\) and \(Z_Q(m)\ge2\). There exist two different primes \(q_1,q_2\) with \(q_i\parallel m\) and \(q_i\equiv r\pmod p\). Multiplicativity and the prime-power factorization of the divisor sum give
\[
\sigma(m^2)=\prod_{\ell^e\parallel m}(1+\ell^2+\cdots+\ell^{2e}),
\]
so each \(\sigma(q_i^2)=q_i^2+q_i+1\) occurs as a factor and is divisible by \(p\). Thus \(p^2\mid\sigma(m^2)\). Because \(p\parallel m\), the two gcds in the definition of \(\mathscr A\) have different valuations at \(p\): respectively one and two. Consequently \(m\notin\mathscr A\). We have proved the containment
\[
\mathscr A\cap\{m:p\parallel m\}
\subseteq\{m:p\parallel m,\ Z_Q(m)\le1\}.
\]
For each fixed finite \(Q\), all events on the right depend on finitely many pairwise-coprime prime-square moduli, hence have an exact natural density. Chebyshev's inequality, for \(\mu_Q>1\), gives
\[
\begin{aligned}
\overline d\bigl(\mathscr A\cap\{m:p\parallel m\}\bigr)
&\le \delta_p\,\Pr(Z_Q\le1)\\
&\le\delta_p\frac{V_Q}{(\mu_Q-1)^2}
\le\delta_p\frac{\mu_Q}{(\mu_Q-1)^2}.
\end{aligned}
\]
Letting the chosen finite sets \(Q\) increase, the final expression tends to zero. This proves the lemma. Note carefully that the limit in \(X\) was taken for each fixed finite \(Q\) *before* increasing \(Q\); no infinite independence hypothesis is needed.

**Completion.** Let \(P\) be any finite set of primes congruent to \(1\pmod6\). The lemma and the finite union bound show that the part of \(\mathscr A\) with \(p\parallel m\) for at least one \(p\in P\) has upper natural density zero. Every remaining element of \(\mathscr A\) avoids all these valuation-one conditions. Applying CRT to this finite family,
\[
\overline d(\mathscr A)\le
\prod_{p\in P}(1-\delta_p).
\]
Finally, the prime harmonic series in the progression \(1\pmod6\) diverges, while \(\sum_p1/p^2\) converges. It follows that
\[
\sum_{p\equiv1\ (\mathrm{mod}\ 6)}\delta_p=\infty,
\qquad
\prod_{p\equiv1\ (\mathrm{mod}\ 6)}(1-\delta_p)=0,
\]
where the product is interpreted as a limit of *finite* partial products; the second statement follows also from \(\log(1-t)\le-t\) for \(0<t<1\). Taking larger finite \(P\) therefore forces \(\overline d(\mathscr A)=0\). As the lower density is nonnegative, the natural density exists and equals zero. \(\square\)

## Verification
The standalone `verify.py` deterministically computes \(\sigma(m^2)\) by the prime factorization of \(m\) and checks the defining gcd equality for every positive integer through one million. Its cumulative counts at \(10\), \(100\), \(1000\), \(10000\), \(100000\), and \(1000000\) are respectively \(10\), \(99\), \(974\), \(9561\), \(93845\), and \(923464\). It separately checks the requisite cubic-residue obstruction for \(p=7\) and \(p=13\), and enumerates valuation-one residue classes for nine small primes. These are finite regression tests, not evidence that a density limit holds by extrapolation.

The infinite argument rests on the explicitly stated CRT counting, elementary variance bound, multiplicativity of the divisor sum, and established divergence of reciprocal primes in reduced arithmetic progressions. No unproved numerical certificate is needed to establish the theorem.

## Relationship to prior work
Dris's original GCD framework appeared in an April 15, 2020 public answer on Mathematics Stack Exchange, and his August 18, 2020 MathOverflow question asked whether this exact set has density zero. Dris's February 10, 2022 preprint, Section 5, proves only that its density is strictly less than one and explicitly formulates the zero-density statement as Conjecture 5.1.

Aaron Meyerowitz's August 18--19, 2020 MathOverflow answer already described the essential local cubic-root obstruction for primes \(p\equiv1\pmod6\). Crucially, that answer stated the product-zero conclusion conditionally on justifying simultaneous asymptotic behavior; it did not supply a finite-prime limiting argument. The present proof makes that step rigorous by fixing one prime \(p\), replacing the informal probability-one assertion with a finite CRT/variance estimate, and then applying a second finite truncation across \(p\). The local mechanism is therefore credited to Meyerowitz; the new assertion is a completed unconditional proof of the density-zero conclusion, not a claim to have independently invented the obstruction.

A published squarefree subfamily result establishes a lower bound of order \(X/\sqrt{\log X}\) for the number of solutions, which is compatible with density zero and does not imply the full statement. Classical Mertens theory in progressions supplies the only non-elementary analytic input. Neither a search for the exact gcd identity nor a comparison with the inspected primary discussions disclosed an existing unconditional proof; this does not establish global publication priority.

## Limitations
No effective rate for the decay of \(\#(\mathscr A\cap[1,X])/X\) is proved. The argument proves natural density zero but not that the set is finite; indeed the known squarefree subfamily is infinite. The proof relies on the classical reciprocal-prime divergence for reduced arithmetic progressions. The underlying local obstruction and the expected Euler-product conclusion were anticipated by Meyerowitz in 2020, and unindexed or later work might already contain an equivalent formalization.

## References
1. Jose Arnaldo Bebita Dris, “On GCDs and odd perfect numbers,” Mathematics Stack Exchange, answer of 15 April 2020, https://math.stackexchange.com/questions/3131818/on-gcds-and-odd-perfect-numbers.
2. Jose Arnaldo Bebita Dris, “Is the asymptotic density of positive integers ... equal to zero?”, MathOverflow question 369441, 18 August 2020; Aaron Meyerowitz's answer, 18--19 August 2020, https://mathoverflow.net/questions/369441/is-the-asymptotic-density-of-positive-integers-n-satisfying-gcdn-sigman.
3. Jose Arnaldo Bebita Dris, “A new approach to odd perfect numbers via GCDs,” arXiv:2202.08116v1, first posted 10 February 2022; Section 5, Conjecture 5.1, https://arxiv.org/abs/2202.08116.
4. “A squarefree \(2\bmod3\) subfamily in Dris's GCD set,” published-finding corpus mathematical record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-a-squarefree-2-bmod-3-subfamily-in-dris-s-gcd-set--3181e476c480/RESULT.md.
5. A. Languasco and A. Zaccagnini, “Computing the Mertens and Meissel-Mertens constants for sums over arithmetic progressions,” arXiv:0906.2132 (2009), https://arxiv.org/abs/0906.2132; the prime reciprocal divergence in reduced progressions is classical.

# Prime-by-prime density dichotomy for denominators of reciprocal gcd sums
## Finding
For each positive integer \(n\), let
\[\mathcal H(n)=\sum_{j=1}^{n}\frac1{\gcd(n,j)},\qquad d(n)=\operatorname{den}(\mathcal H(n)),\]
where \(d(n)\) is the positive denominator in lowest terms. For each prime \(\ell\), the natural density \(\delta_\ell\) of positive integers \(n\) for which \(\ell\mid d(n)\) exists. The classification is
\[
\delta_2=\frac12,\qquad \delta_\ell=0\quad(\ell=3\text{ or }\ell\equiv1\pmod6),\qquad 0<\delta_\ell<\frac1\ell\quad(\ell\equiv5\pmod6).
\]
For the last class, define \(h_p(a)=(p^{2a+1}+1)/(p+1)\) for \(a\ge0\), where \(h_p(0)=1\). There is the absolutely convergent explicit Euler product
\[
\boxed{\displaystyle \delta_\ell=\frac1\ell\prod_{p\ne\ell}\left(1-\frac1p\right)\sum_{a=0}^{\infty}\frac{\ell^{-\nu_\ell(h_p(a))}}{p^a}.}
\]
In particular,
\[
\boxed{\displaystyle \delta_5=\frac15\prod_{p\equiv4\ (\mathrm{mod}\ 5)}\left(1-\frac1p\right)\sum_{a=0}^{\infty}\frac{5^{-\nu_5(2a+1)}}{p^a}.}
\]
The latter has numerical value approximately \(0.1992415\); this numerical approximation is not required for either proof.

## Assumptions and scope
All densities refer to the limit as \(X\to\infty\) of \(X^{-1}\#\{1\le n\le X:\ell\mid d(n)\}\) for a *fixed* prime \(\ell\); no uniformity in the prime is asserted. A valuation of an integer not divisible by \(\ell\) is zero. The empty product is one. Every \(p\) appearing in the Euler product ranges over rational primes. This result concerns denominators rather than the much rarer integrality of the full rational value.

## Proof
**1. Exact denominator identity.** For every positive integer \(n\), grouping terms according to their gcd with \(n\) gives
\[
\mathcal H(n)=\frac1n\sum_{t\mid n}t\varphi(t)=\frac{h(n)}n,
\qquad h(n)=\prod_{p^a\parallel n}\frac{p^{2a+1}+1}{p+1}.
\]
The integer-valued factors \(h_p(a)\) satisfy \(h_p(0)=1\) and \(h_p(1)=p^2-p+1=\Phi_6(p)\). Therefore
\[
\ell\mid d(n)\quad\Longleftrightarrow\quad\nu_\ell(n)>\nu_\ell(h(n)).\tag{1}
\]
For \(p=\ell\) one has \(h_\ell(a)\equiv1\pmod\ell\) for every \(a\ge0\), so the valuation of \(h(n)\) is contributed entirely by primes distinct from \(\ell\).

**2. The prime two.** For every prime \(p\) and \(a\ge0\), \(h_p(a)\) is odd: for \(p\) odd, use the divisor-sum expression \(h_p(a)=1+\sum_{b=1}^a p^b\varphi(p^b)\), and for \(p=2\) use the same expression. Hence \(h(n)\) is always odd. By (1), \(2\mid d(n)\) if and only if \(2\mid n\), giving density \(1/2\).

**3. Split primes have density zero.** Suppose \(\ell=3\), or \(\ell\equiv1\pmod6\). The polynomial \(\Phi_6(z)=z^2-z+1\) has a nonzero root \(r\pmod\ell\): for \(\ell=3\) take \(r=2\), and for \(\ell\equiv1\pmod6\) this follows from the existence of elements of order six. Every prime \(p\equiv r\pmod\ell\) therefore satisfies \(\ell\mid h_p(1)\). The sum \(\sum_{p\equiv r\ (\mathrm{mod}\ \ell)}1/p\) diverges by the prime number theorem for arithmetic progressions.

Fix an integer \(T\ge1\), and choose a finite set \(S\) of such primes, excluding \(\ell\). For uniform \(n\le X\), as \(X\to\infty\), the indicators \(\mathbf1_{\nu_p(n)=1}\) for \(p\in S\) jointly converge to independent Bernoulli variables of means \((p-1)/p^2\), by the Chinese remainder theorem (or the elementary distribution of finitely many prime valuations). Their sum has mean \(\sum_{p\in S}(p-1)/p^2\) and variance at most that mean. By enlarging \(S\), Chebyshev's inequality makes the limiting probability of fewer than \(T\) indicators arbitrarily small. Whenever at least \(T\) occur, \(\nu_\ell(h(n))\ge T\); then (1) forces \(\nu_\ell(n)>T\). The natural upper density of integers with \(\nu_\ell(n)>T\) is \(\ell^{-(T+1)}\). First choose \(T\) large, then \(S\) large; the upper density in (1) is zero. The lower density is nonnegative, hence \(\delta_\ell=0\).

**4. Inert primes admit an Euler product.** Now suppose \(\ell\equiv5\pmod6\). The equation \(z^2-z+1\equiv0\pmod\ell\) has no solutions, since a root would have multiplicative order six and \(6\nmid\ell-1\). Consequently \(\nu_\ell(h_p(1))=0\) for every prime \(p\ne\ell\). Define the nonnegative integer
\[K_\ell(m)=\sum_{p^a\parallel m,\ p\ne\ell}\nu_\ell(h_p(a)).\]
By (1), \(\ell\mid d(n)\) if and only if \(\nu_\ell(n)>K_\ell(n)\).

For a finite set \(S\) of primes distinct from \(\ell\), retain in \(K_\ell\) only factors at primes in \(S\). By finite-prime valuation independence, the proportion satisfying the truncated inequality converges to
\[
\frac1\ell\prod_{p\in S}\left(1-\frac1p\right)\sum_{a\ge0}p^{-a}\ell^{-\nu_\ell(h_p(a))}.
\tag{2}
\]
Indeed, conditional on \(K_\ell=k\), the limiting probability \(\Pr(\nu_\ell(n)>k)\) is \(\ell^{-(k+1)}\). The truncated and complete indicators can differ only if some prime outside \(S\) contributes a positive valuation. Since the \(a=0,1\) factors contribute zero, such a prime must divide \(n\) to at least the second power. Taking \(S\) to contain all primes at most \(Y\) other than \(\ell\), the upper density of this exceptional event is at most \(\sum_{p>Y}p^{-2}\), which tends to zero. This proves the existence of the limiting density and the claimed infinite product.

Each local factor in (2) equals \(1+O(p^{-2})\), uniformly in \(p\), because its contributions at exponents zero and one are unchanged and all subsequent weights lie in \([0,1]\). Thus the Euler product converges absolutely to a positive number. Each factor is at most one, so \(\delta_\ell\le1/\ell\). For strict inequality, choose by Dirichlet's theorem a prime \(p\equiv-1\pmod\ell\). At \(a=(\ell-1)/2\ge2\), the lifting-the-exponent lemma gives \(\nu_\ell(h_p(a))=\nu_\ell(2a+1)=1\); hence its factor in the product is strictly less than one. Thus \(0<\delta_\ell<1/\ell\).

**5. The factor at five.** Let \(\ell=5\). If \(p\not\equiv-1\pmod5\), \(p^{2a+1}+1\) is never divisible by five: in \((\mathbb Z/5\mathbb Z)^\times\) an element with odd power equal to \(-1\) must have order two. If \(p\equiv-1\pmod5\), the odd-exponent lifting-the-exponent identity gives \(\nu_5(h_p(a))=\nu_5(2a+1)\), including \(a=0\). Substitution yields the displayed simplified Euler product. This completes the proof.

## Verification
The standalone `verify.py` checks the divisor identity independently against exact rational summation, checks reduced denominator valuations for several small primes and integers, checks the finite counting function for the prime five, and checks the numerical Euler-product approximation. It is not an infinite certificate: the proof of the density dichotomy is the finite-prime independence/tail and prime-divergence argument above.

## Relationship to prior work
De Koninck and Letendre, *The Integer Values of* \(\sum_{i=1}^n1/\gcd(n,i)\) (2026), introduce the same multiplicative numerator \(h(n)\) and study the much more restrictive condition \(n\mid h(n)\), proving a sparse-count bound. Their full 12-page preprint addresses the integrality counting problem, not the present complete density classification by primes dividing the *reduced denominator*. The OEIS denominator table A333696 gives arithmetic data, not this asymptotic classification. An earlier, sharper result for \(\ell=3\) is compatible with, and strictly more informative than, the corresponding zero-density branch here; that special branch is not claimed as independently novel. The principal contribution is the all-prime dichotomy and positive Euler products for the inert prime class.

## Limitations
The prime \(\ell\) is fixed in the density limit, and no rate of convergence is asserted. The Euler product need not give a closed elementary constant. A numerical approximation for \(\delta_5\) depends on truncation and is not an exact equality. Any implicit earlier derivation in the broader literature remains a residual originality risk; mathematical searches cannot establish uniqueness. No independent audit has been performed.

## References
- Jean-Marie De Koninck and Patrick Letendre, *The Integer Values of* \(\sum_{i=1}^n1/\gcd(n,i)\), arXiv:2610.10572v1 (first public version 2026-10-04), https://arxiv.org/abs/2610.10572 .
- The On-Line Encyclopedia of Integer Sequences, A333696, denominator terms for the same reciprocal gcd sum, https://oeis.org/A333696 .
- The On-Line Encyclopedia of Integer Sequences, A071000 and A070999, related denominator behavior, https://oeis.org/A071000 and https://oeis.org/A070999 .
- Classical prime number theorem in arithmetic progressions, finite-dimensional Chinese remainder theorem, and lifting-the-exponent lemma are used in their standard forms.

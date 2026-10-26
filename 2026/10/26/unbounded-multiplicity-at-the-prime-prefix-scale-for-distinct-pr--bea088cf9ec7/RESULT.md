# Unbounded multiplicity at the prime-prefix scale for distinct-prime partition discrepancies

## Finding

For a nonnegative integer \(n\), let \(L(n)\) be the largest number of distinct primes whose sum is \(n\), and let \(K(n)\) be the number of parts in the unique distinct-prime partition of \(n\) whose product is maximal. Set both quantities to zero if no such partition exists. For every fixed integer \(r\ge1\), define

\[
E_r(X)=\#\{n\in\mathbb Z_{\ge1}:n\le X,\ L(n)-K(n)\ge r\}.
\]

**Theorem.** For every fixed integer \(r\ge1\),

\[
\boxed{\lim_{X\to\infty}E_r(X)\sqrt{\frac{\log X}{X}}=+\infty.}
\]

More precisely, for every pair of fixed integers \(r,J\ge1\), there are \(J\) distinct positive integers \(d_1,\ldots,d_J\) and an integer \(H\ge1\) with the following property. Write \(\Sigma(p)=\sum_{q\le p,\ q\text{ prime}}q\), let \(p^+\) denote the next prime after \(p\), and set

\[
\mathcal T_{r,J}=\{\Sigma(p)-d_i:\ 1\le i\le J,\ p\text{ prime},\ p>\max_i d_i,\ p^+-p>H\}.
\]

Every element of \(\mathcal T_{r,J}\) has \(L(n)-K(n)\ge r\), and

\[
\boxed{\#(\mathcal T_{r,J}\cap[1,X])\sim 2J\sqrt{\frac{X}{\log X}}.}
\]

The statement counts *integers*, rather than choices of their representations; the \(J\) prime-prefix translates become disjoint after discarding finitely many initial terms.

## Assumptions and scope

All primes are ordinary positive rational primes. Prime partitions are finite **sets of distinct primes** with exact sum \(n\). The parameters \(r\) and \(J\) are held fixed before \(X\to\infty\); the construction is not uniform when they grow with \(X\). No assumption such as the twin-prime conjecture or the Riemann hypothesis is made. The cited product-minimal extension lemma, distinct-prime ternary representation lemma, and large-prime-gap product maximization lemma are used in their precise published forms.

## Proof

**1. Choosing many different deletion patterns.** Fix \(r,J\ge1\) and put \(t=r+3\). Campbell's Lemma 3 [1] states that arbitrarily large odd integers \(d\) have product-minimal distinct-prime sets of cardinality exactly \(t\): for such an integer \(d\), there is a finite set \(A\) of \(t\) distinct primes summing to \(d\), and its product \(M=\prod_{q\in A}q\) is minimal among products of all prime sets with sum \(d\). The lemma constructs these sets by repeated addition of an isolated prime and establishes that their sums are odd. Campbell's Lemma 4 [1], following Vinogradov's three-primes theorem, states that every sufficiently large odd integer is a sum of three *pairwise distinct* primes. Choose \(J\) **distinct** such odd integers \(d_1,\ldots,d_J\), beyond that threshold, with product-minimal sets \(A_i\) of \(t\) primes and separate three-prime sets \(C_i\), where

\[
\sum_{q\in A_i}q=\sum_{q\in C_i}q=d_i,\qquad |A_i|=t,\quad |C_i|=3.
\]

Let \(M_i=\prod_{q\in A_i}q\), and take the fixed integer \(H=11\max_{1\le i\le J}M_i\).

**2. A common set of eligible primes.** Let \(p>\max_i d_i\) be a prime with \(p^+-p>H\). Denote by \(B_p\) the set of all primes not exceeding \(p\). For each \(i\), Campbell's Lemma 6 [1] applies because \(p^+-p>11M_i\): the **unique product-maximizing** distinct-prime partition of \(n_{p,i}=\Sigma(p)-d_i\) is \(B_p\setminus A_i\). Thus

\[
K(n_{p,i})=\pi(p)-t.
\]

But \(B_p\setminus C_i\) is also a distinct-prime partition of precisely the same integer, with \(\pi(p)-3\) parts. Hence

\[
L(n_{p,i})-K(n_{p,i})\ge(\pi(p)-3)-(\pi(p)-t)=t-3=r.
\]

Campbell's Lemma 6 itself separates alternative partitions that use only primes \(\le p\) (where product-minimality governs) from partitions containing a prime \(>p\) (where its product inequality and the following prime gap force strict loss). We use the exact hypothesis \(p^+-p>11M_i\), rather than an unverified extension to short gaps.

**3. Eligible primes have prime-relative density one.** Fix the integer \(H\) above. The classical fixed-shift two-prime upper-bound sieve asserts that, for every fixed positive integer \(h\),

\[
\#\{p\le y:\ p\text{ and }p+h\text{ are prime}\}\ll_h\frac{y}{(\log y)^2}.
\]

This is the standard two-linear-form upper-bound consequence of Brun's or Selberg's sieve [2]; the finitely many local exceptions for shifts of odd parity do not affect it. If \(p^+-p\le H\), then \(p\) and \(p+h\) are both prime for some integer \(1\le h\le H\). Summing the bound over these finitely many shifts gives

\[
\#\{p\le y:p^+-p\le H\}=O_H\!\left(\frac{y}{(\log y)^2}\right)=o(\pi(y)).
\]

The last equality uses the prime number theorem. Consequently the primes eligible in step 2, after removing the fixed finite initial range, number \((1+o(1))\pi(y)\) up to \(y\). In particular the argument does **not** require infinitely many primes in any fixed prime-pair pattern.

**4. Translates are eventually pairwise disjoint.** Write \(D=\max_{i,j}|d_i-d_j|\). For any primes \(p'<p''\),

\[
\Sigma(p'')-\Sigma(p')=\sum_{p'<q\le p'',\ q\text{ prime}}q\ge p''.
\]

If \(p''>D\), the difference cannot equal \(d_j-d_i\); therefore \(\Sigma(p'')-d_j\ne\Sigma(p')-d_i\). For a common prime \(p\), distinct offsets \(d_i\) also give distinct integers. Thus the \(J\) families are mutually disjoint aside from finitely many initial terms, even if the same eligible prime is used in each family.

**5. Exact prime-prefix counting asymptotic.** Partial summation and the prime number theorem give

\[
\Sigma(y)=\sum_{p\le y}p\sim\frac{y^2}{2\log y}.
\]

If \(y_X\) is the largest prime with \(\Sigma(y_X)\le X\), then \(y_X\sim\sqrt{X\log X}\) and

\[
\pi(y_X)\sim2\sqrt{\frac{X}{\log X}}.
\]

For all sufficiently large eligible primes \(p\le y_X\), all \(J\) values \(\Sigma(p)-d_i\) lie in \([1,X]\), and are pairwise distinct. Conversely, an eligible prime with \(\Sigma(p)-d_i\le X\) but \(\Sigma(p)>X\) contributes at most one extra value for each fixed \(i\) when \(X\) is large, since successive prime-prefix sums have increments tending to infinity while \(d_i\) is fixed. Hence the count from the \(J\) translates equals

\[
J(1+o(1))\pi(y_X)\sim 2J\sqrt{\frac{X}{\log X}}.
\]

Since this set is contained in the exceptional set counted by \(E_r(X)\), for **every fixed** \(J\) we obtain

\[
\liminf_{X\to\infty}E_r(X)\sqrt{\frac{\log X}{X}}\ge2J.
\]

There is no upper restriction on \(J\). Therefore the liminf is infinite, and the asserted limit is \(+\infty\). \(\square\)

## Verification

The key implications were checked against their precise source statements: [1, Lemmas 3, 4, and 6] provide infinitely many distinct offsets, genuine three-distinct-prime partitions, and product-maximality under the required **next-prime** gap. The sieve estimate supplies relative density one for that one-sided gap condition, rather than merely infinitude. The disjointness inequality and the inversion of \(\Sigma(y)\sim y^2/(2\log y)\) were checked with their quantifiers fixed in the correct order: first \(r,J\), then \(X\). No finite enumeration is offered as proof of these unbounded conclusions.

## Relationship to prior work

Campbell [1] resolved Guy's question by proving infinitely many integers with \(L(n)-K(n)\ge r\) for each fixed \(r\). His proof uses one product-minimal deletion pattern and infinitely many suitably isolated primes. The present theorem **counts** an asymptotically full proportion of eligible primes for every fixed pattern and, crucially, uses arbitrarily many different patterns with eventual cross-pattern disjointness. Campbell's stated infinitude theorem alone does not imply an unbounded multiplier in a quantitative lower bound for \(E_r(X)\).

Deléglise and Nicolas [3] study the maximum product when the **sum is at most** a bound, whereas \(K(n)\) here concerns exact-sum partitions. The OEIS sequence A053020 [4] enumerates some integers where \(L(n)>K(n)\); its displayed terms do not furnish a quantitative counting theorem. A public note on greedy consecutive-product constructions involving prime gaps concerns a different object and does not imply the displayed counting result.

## Limitations

The theorem proves a lower bound and a sharp asymptotic for its **constructed** \(J\)-translate subfamily, not an asymptotic formula for the full set counted by \(E_r(X)\). The divergence can be arbitrarily slow in this non-effective proof: the construction and the prime-pair sieve constants depend on fixed \(r,J\). It does not establish a positive natural density of discrepancy-rich integers or uniformity when \(r\) or \(J\) grow with \(X\). The result relies on the classical sieve and prime number theorems and on cited product-minimality lemmas, and has not undergone independent verification.

## References

1. John M. Campbell, *On a problem on partitions into distinct primes*, arXiv:2610.19534v1 (first public version 14 October 2026), especially Lemmas 3, 4, 6 and Theorem 1. https://arxiv.org/html/2610.19534v1
2. Classical Brun–Selberg fixed-shift two-prime upper-bound sieve; for a reference treating sieve upper bounds for pairs of primes with fixed even difference, see *The Sieves of Brun and Selberg*, chapter 2 of *Bounded Gaps Between Primes*, Cambridge University Press (2021), DOI 10.1017/9781108872201.004. https://doi.org/10.1017/9781108872201.004
3. Marc Deléglise and Jean-Louis Nicolas, *On the Largest Product of Primes with Bounded Sum*, Journal of Integer Sequences 18 (2015), article 15.2.8. https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Deleglise/deleglise3.pdf
4. OEIS A053020, *Numbers which, when expressed as a sum of distinct primes with maximum product, use a non-maximal number of primes*. https://oeis.org/A053020

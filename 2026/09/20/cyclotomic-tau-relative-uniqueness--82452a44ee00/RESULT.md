# A cyclotomic family with a unique tau-number relative to the polynomial

Let \(\tau(n)\) denote the number of positive divisors of \(n\). Following Zelinsky, a positive integer \(n\) is a **tau-number relative to** \(Q\in\mathbb Z[x]\) when \(\tau(n)\mid Q(n)\).

## Theorem

Let \(p\equiv 3\pmod 4\) be an odd prime and let \(k\ge 1\). Then
\[
\tau(n)\mid \Phi_{2p^k}(n)
\]
for a positive integer \(n\) if and only if \(n=1\).

Equivalently, every cyclotomic polynomial \(\Phi_{2p^k}\) with \(p\equiv3\pmod4\) has exactly one tau-number relative to it. In particular,
\[
\tau(n)\mid n^2-n+1 \quad\Longrightarrow\quad n=1,
\]
since \(\Phi_6(x)=x^2-x+1\).

The same conclusion holds with \(\Phi_{2p^k}(x)\) replaced by any positive power \(\Phi_{2p^k}(x)^e\), \(e\ge1\).

## Context

Abel, Lauer and Redi (2021) proved that every integer polynomial \(Q\) with \(|Q(0)Q(1)|\ne1\) has infinitely many tau-numbers relative to it. For the remaining type-II case \(|Q(0)Q(1)|=1\), they recorded that exhaustive computation through \(10^8\) found no relative tau-number other than 1 for several polynomials, explicitly including \(x^2-x+1\), and posed the classification of type-II behavior as an open problem. They also observed that prime-power-index cyclotomic polynomials \(\Phi_{p^j}\) lie on the infinite side because \(\Phi_{p^j}(1)=p\).

The theorem above supplies an infinite cyclotomic family on the opposite side: for odd prime powers with index doubled, \(\Phi_{2p^k}(0)=\Phi_{2p^k}(1)=1\), and when \(p\equiv3\pmod4\) the relative tau-number set collapses to \(\{1\}\).

## Proof

Write
\[
Q(x)=\Phi_{2p^k}(x)=\Phi_{p^k}(-x)
      =\sum_{j=0}^{p-1}(-1)^j x^{j p^{k-1}},
\]
and put \(L=2p^k\). Suppose \(n>1\) and \(T=\tau(n)\mid Q(n)\). Write
\[
n=\prod_{i=1}^s q_i^{a_i}.
\]

### 1. Parity forces \(n\) to be a square

The value \(Q(n)\) is odd for every integer \(n\): if \(n\) is even only the constant term survives modulo 2, while if \(n\) is odd the \(p\) alternating terms are all 1 modulo 2 and \(p\) is odd. Hence \(T\) is odd. Since
\[
T=\prod_i(a_i+1),
\]
every exponent \(a_i\) is even. Thus \(n\) is a perfect square.

Also \(\gcd(n,T)=1\). Indeed, if a prime \(\ell\mid n\) also divided \(T\), then \(T\mid Q(n)\) would give \(Q(n)\equiv0\pmod\ell\), whereas \(Q(n)\equiv Q(0)=1\pmod\ell\).

### 2. The prime \(p\) cannot divide \(T\)

In \(\mathbb F_p[x]\),
\[
Q(x)=\Phi_{p^k}(-x)
\equiv (x+1)^{p^{k-1}(p-1)}.
\]
Consequently, if \(p\mid T\), then \(p\mid Q(n)\) and therefore \(n\equiv-1\pmod p\). But \(p\nmid n\) by \(\gcd(n,T)=1\), and \(n\) is a square. This would make \(-1\) a quadratic residue modulo \(p\), impossible because \(p\equiv3\pmod4\). Thus \(p\nmid T\).

### 3. Every prime divisor of \(T\) imposes exact order \(L\)

Let \(\ell\) be a prime divisor of \(T\). Then \(\ell\ne2,p\), \(\ell\nmid n\), and \(\ell\mid Q(n)\). The identity
\[
(n^{p^{k-1}}+1)Q(n)=n^{p^k}+1
\]
gives \(n^{p^k}\equiv-1\pmod\ell\). If \(n^{p^{k-1}}\equiv-1\pmod\ell\), then the displayed sum for \(Q\) would give \(Q(n)\equiv p\pmod\ell\), contradicting \(\ell\ne p\). Therefore
\[
\operatorname{ord}_{\ell}(n)=2p^k=L.
\]
In particular, \(L\mid \ell-1\). Since this holds for every prime \(\ell\mid T\), every prime factor of each \(a_i+1\) is \(1\pmod L\). Hence
\[
a_i+1\equiv1\pmod L,
\]
so \(L\mid a_i\) for every \(i\).

### 4. Infinite divisibility bootstrap

Assume inductively that \(L^r\mid a_i\) for every \(i\), for some \(r\ge1\). Then \(n=u^{L^r}\) for an integer \(u\). Fix a prime \(\ell\mid T\), and set \(d=\operatorname{ord}_{\ell}(u)\). Since \(\operatorname{ord}_{\ell}(n)=L\),
\[
\frac{d}{\gcd(d,L^r)}=L.
\]
Because \(L=2p^k\), comparison of the 2-adic and \(p\)-adic valuations in this equality gives
\[
v_2(d)=r+1,
\qquad
v_p(d)=k(r+1),
\]
and no other prime can divide \(d\). Thus \(d=L^{r+1}\), so \(L^{r+1}\mid\ell-1\).

Again every prime factor of every \(a_i+1\) is congruent to 1 modulo \(L^{r+1}\). Hence \(a_i+1\equiv1\pmod{L^{r+1}}\), and therefore \(L^{r+1}\mid a_i\) for all \(i\).

By induction every fixed positive exponent \(a_i\) would be divisible by \(L^r\) for all \(r\), impossible. Hence no \(n>1\) exists. Finally \(n=1\) works because \(\tau(1)=1\).

For \(Q(x)^e\), any prime divisor of \(T\) dividing \(Q(n)^e\) already divides \(Q(n)\), so the identical argument applies.

## Computational consistency check

A standalone exact-integer program in `artifacts/verify.py` computes divisor counts and evaluates \(\Phi_{2p^k}(n)\) modulo \(\tau(n)\) without constructing the potentially large polynomial value. For every \(2\le n\le10^6\), it found no nontrivial solutions for
\[
(p,k)=(3,1),(3,2),(3,3),(7,1),(7,2),(11,1),(19,1).
\]
This finite check is supporting evidence only; the theorem is proved above without a cutoff.

## Originality and limitations

To the best of our knowledge, the theorem and its \(x^2-x+1\) specialization were not previously proved in the checked literature. Abel--Lauer--Redi (2021) explicitly left \(x^2-x+1\) at the computational level through \(10^8\), while Muttika's 2023 thesis continued the same type-II problem and still described the general case as unresolved.

There is a material residual originality uncertainty: Muttika's thesis notes that, near completion, the author learned of an article then in preparation describing some class of polynomials for which 1 is the only relative tau-number. The note gives no title, authors, identifier, or class. Searches for the theorem, the polynomial \(x^2-x+1\), cyclotomic formulations, the cited authors, and subsequent publications did not identify such an article through the checked current sources. Because the unspecified class could overlap the family proved here, this remains the principal literature risk.

The proof uses \(p\equiv3\pmod4\) only to exclude \(p\mid\tau(n)\). Computation suggests that additional primes may also have uniqueness, but no claim is made for \(p\equiv1\pmod4\).

## References

1. M. Abel, H. Lauer, E. Redi, *About the number of tau-numbers relative to polynomials with integer coefficients*, Acta et Commentationes Universitatis Tartuensis de Mathematica 25 (2021), 107--117. https://doi.org/10.12697/ACUTM.2021.25.07
2. E.-M. Muttika, *Results about tau-numbers relative to polynomials* (Bachelor's thesis, University of Tartu, 2023). https://dspace.ut.ee/bitstreams/df20b790-5ecb-488b-99e6-202b65ac8a7a/download

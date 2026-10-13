# Exact coefficient content of prime-detecting divisor-sum forms

## Finding
For positive integers \(1\le k<\ell\), write
\[
\sigma_j(n)=\sum_{d\mid n}d^j,\qquad
c_{k,\ell}(n)=(n^\ell+1)\sigma_k(n)-(n^k+1)\sigma_\ell(n).
\]
The common content of all positive-index coefficients is exactly the fixed divisor of a single polynomial:
\[
\boxed{\gcd_{n\ge2}c_{k,\ell}(n)=\gcd_{a\ge1}(a^\ell-a^k)=H_{k,\ell}.}
\]
Here the greatest common divisor of an infinite set means its positive generator as an ideal of \(\mathbb Z\); these gcds are finite because the coefficient at \(n=4\) is nonzero.

Set \(t=\ell-k\). The exact prime exponents of \(H_{k,\ell}\) are
\[
\nu_2(H_{k,\ell})=\begin{cases}
\min(k,1),&t\text{ odd},\\
\min(k,\nu_2(t)+2),&t\text{ even},
\end{cases}
\]
and, for every odd prime \(p\),
\[
\nu_p(H_{k,\ell})=\begin{cases}
\min(k,1+\nu_p(t)),&p-1\mid t,\\
0,&p-1\nmid t.
\end{cases}
\]
All other prime exponents vanish. In particular \(H_{3,7}=120\), so every positive-index coefficient of the established prime-detecting form \(f_{3,7}\) is divisible by \(120\), and no larger positive integer divides all of them. For odd \(k,\ell\), the generating function of \(c_{k,\ell}(n)\) is the nonconstant part of the quasimodular Eisenstein combination considered by Craig–van Ittersum–Ono and Allen–Craig.

## Assumptions and scope
All powers and divisor sums use ordinary positive integers; \(k\ge1\) and \(\ell>k\). There is no requirement that the exponents be odd for this arithmetic identity. The quasimodular-form interpretation requires odd \(k,\ell\) and is only for the positive-index Fourier coefficients, **not** the generally rational constant term. The formulas characterize the largest integer dividing every coefficient and do not assert congruences along individual progressions or the divisibility of the constant term.

## Proof
We prove the exact equality prime-power by prime-power. Let \(G=\gcd_{a\ge1}(a^\ell-a^k)\) and \(H=\gcd_{n\ge2}c_{k,\ell}(n)\). Since every power difference \(a^\ell-a^k\) is divisible by \(G\), the two identities
\[
\sigma_k(n)-\sigma_\ell(n)=\sum_{d\mid n}(d^k-d^\ell),\quad
c_{k,\ell}(n)=(n^\ell-n^k)\sigma_k(n)+(n^k+1)(\sigma_k(n)-\sigma_\ell(n))
\]
show \(G\mid H\).

Conversely fix a prime \(p\) and \(e\ge1\) for which \(p^e\mid H\). Direct expansion at the prime square gives
\[
c_{k,\ell}(p^2)=(p^k-p^\ell)(1-p^{k+\ell}),
\]
whose \(p\)-adic valuation is exactly \(k\); consequently \(e\le k\). Choose any integer \(a\ge1\) with \(ak\ge e\), and set \(S_j=\sigma_j(p^a)\). Both \((p^a)^k\) and \((p^a)^\ell\) vanish modulo \(p^e\), so the hypothesis applied to \(p^a\) gives
\[S_k\equiv S_\ell\pmod{p^e}.\]
Now let \(u\ge1\) be coprime to \(p\). Multiplicativity of the divisor sums and the same vanishing at \(up^a\) imply
\[
0\equiv c_{k,\ell}(up^a)
\equiv S_k\sigma_k(u)-S_\ell\sigma_\ell(u)
\equiv S_k(\sigma_k(u)-\sigma_\ell(u))\pmod{p^e}.
\]
The factor \(S_k\equiv1\pmod p\) is invertible modulo \(p^e\). Thus \(\sigma_k(u)\equiv\sigma_\ell(u)\pmod{p^e}\) for every \(p\)-coprime \(u\). Möbius inversion on the divisor poset of such \(u\) yields \(u^k\equiv u^\ell\pmod{p^e}\), because \(\sigma_j=\mathbf 1*\operatorname{id}^j\). For an integer \(u\) divisible by \(p\), both powers vanish modulo \(p^e\) since \(e\le k\). Therefore \(p^e\) divides \(u^\ell-u^k\) for every positive integer \(u\), and \(p^e\mid G\). Every prime power in \(H\) is in \(G\), proving \(H=G\).

It remains to calculate the fixed divisor. For \(t=\ell-k\), the polynomial difference is \(a^k(a^t-1)\). Its minimum valuation among multiples of a prime \(p\) is exactly \(k\), achieved at \(a=p\); among \(p\)-adic units its common valuation threshold is the largest \(e\) for which every unit modulo \(p^e\) has \(t\)-th power one, equivalently \(\lambda(p^e)\mid t\), where \(\lambda\) is the Carmichael exponent. The classical formulas \(\lambda(p^e)=p^{e-1}(p-1)\) for odd \(p\), and \(\lambda(2)=1\), \(\lambda(4)=2\), \(\lambda(2^e)=2^{e-2}\) for \(e\ge3\), give precisely the asserted exponents after taking the minimum with \(k\). Only primes \(p\le t+1\) can occur; the product is finite. This completes the proof.

## Verification
The standalone `verify.py` independently computes the divisor sums by both direct divisor enumeration and the multiplicative prime-power formula. It checks \(60\) exponent pairs \(1\le k\le8\), \(k<\ell\le12\), all indices \(2\le n\le180\), their observed gcd against the formula, and \(24\) prime-square identities. The output is preserved in `verification_output.txt`. These are finite cross-checks only; the proof above establishes the infinite identity. Reproduce with `python3 verify.py` in an ordinary Python 3 environment without extra packages.

## Relationship to prior work
Craig, van Ittersum, and Ono (2024) introduce the prime-detecting coefficient family and prove prime-vanishing and a classification of Eisenstein-space prime detectors; their Lemma 12 separately proves integrality and a unit-content property for certain distinguished forms \(H_j\). Allen and Craig (2026) analyze growth, prime-factor bounds, and prime intervals using precisely \(c_{k,\ell}\). The present statement is a **different, coefficientwise universal-divisibility classification**: it gives the greatest common integer divisor of all coefficients in each member of the two-parameter family, explicitly including its prime-power valuation. Prime-vanishing, positivity, prime-interval bounds, and unit content of different distinguished forms do not imply this sharp two-parameter formula without additional argument.

The right-hand gcd is the classical fixed divisor of the polynomial \(a^k(a^t-1)\), evaluable by elementary properties of finite unit groups. The newly established part for this particular family is the equality between that polynomial fixed divisor and the global Fourier-coefficient content, proved through the prime-power padding and Möbius-inversion argument. Targeted searches of available literature and published findings did not reveal an equivalent published statement; this is not a proof of uniqueness or comprehensive novelty.

## Limitations
The result gives no nontrivial uniform information on the normalized constant term of the quasimodular forms, no control on individual arithmetic progressions, and no improvement in bounds for prime gaps. The originality comparison is subject to unindexed or inaccessible equivalent treatments. Independent mathematical auditing has not been performed.

## References
1. K. Allen and W. Craig, *Quasimodular Forms, Partitions, and Primes in Intervals*, arXiv:2609.32053v1 (first publicly posted 2026-09-25), especially the coefficient definition in Section 2 and results in Sections 3–7. https://arxiv.org/pdf/2609.32053
2. W. Craig, J.-W. van Ittersum, and K. Ono, *Integer partitions detect the primes*, Proceedings of the National Academy of Sciences **121** (2024), e2409417121; especially Lemma 9 and Lemma 12. https://doi.org/10.1073/pnas.2409417121

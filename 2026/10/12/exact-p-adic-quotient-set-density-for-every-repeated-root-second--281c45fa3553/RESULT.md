# Exact \(p\)-adic quotient-set density for every repeated-root second-order recurrence

## Finding
Let \(p\) be any prime. Fix integers \(a,x_0,x_1\) and define the integer sequence by
\[
x_{n+2}=2a x_{n+1}-a^2x_n\qquad(n\ge0).
\]
Let
\[
R=\{x_m/x_n:m,n\in\mathbb Z_{\ge0},\ x_n\ne0\},\qquad D=x_1-a x_0.
\]
Then **the complete density criterion**, including primes dividing the recurrence coefficients, is
\[
\boxed{\overline R^{\,\mathbb Q_p}=\mathbb Q_p
\quad\Longleftrightarrow\quad
 aD\ne0\ \text{ and }\ \nu_p(a x_0)\ge\nu_p(D).}
\]
Here \(\nu_p(0)=+\infty\). When \(aD\ne0\), the valuation condition is equivalent to the shift \(c=a x_0/D\) being a \(p\)-adic integer.

For example, at \(p=2\), the data \((a,x_0,x_1)=(2,1,4)\) give \(D=2\) and \(c=1\), hence a dense quotient set despite \(p\mid aD\). In contrast, \((a,x_0,x_1)=(2,1,6)\) give \(D=4\) and \(c=1/2\), hence a non-dense quotient set. These cases demonstrate that the earlier sufficient restriction \(p\nmid aD\) is not necessary and that the excluded primes can have either outcome.

## Assumptions and scope
The integers \(a,x_0,x_1\) are arbitrary (including zero), \(p\) is any rational prime (including \(2\)), and the recurrence holds at every index \(n\ge0\). A quotient requires only a nonzero denominator; zero numerators are allowed. The density is with respect to the usual \(p\)-adic topology on \(\mathbb Q_p\). The claim concerns this repeated-characteristic-root family, not unrestricted order-two recurrences. The primary MSC2020 is \(11B37\).

## Proof
**1. Closed form and exceptional degeneracies.** For every \(n\ge1\), direct substitution or induction gives
\[
x_n=a^{n-1}(a x_0+nD).
\]
When \(a=0\), only \(x_0,x_1\) can be nonzero and the quotient set is finite. When \(a\ne0\) and \(D=0\), the sequence is \(x_n=a^nx_0\). It is identically zero if \(x_0=0\); otherwise its nonzero quotients form the geometric group \(\{a^j:j\in\mathbb Z\}\), which is not dense in \(\mathbb Q_p\): if \(p\nmid a\), its valuations are all zero, and if \(p\mid a\), the only quotient with valuation zero is \(1\). Thus density requires \(aD\ne0\).

Assume henceforth \(aD\ne0\), and set \(c=a x_0/D\in\mathbb Q\). For \(n\ge1\),
\[
x_n=a^{n-1}D(n+c).
\]
Consequently, for \(n\ge1\), \(d\ge1\), and \(n+c\ne0\),
\[
\frac{x_{n+d}}{x_n}
=a^d\frac{n+c+d}{n+c}=a^d+\frac{da^d}{n+c}.\tag{1}
\]

**2. Necessity.** Suppose \(c\notin\mathbb Z_p\). Then \(\nu_p(c)<0\), and for every nonnegative integer \(n\) the ultrametric inequality gives \(\nu_p(n+c)=\nu_p(c)\). In particular \(x_0\ne0\). The closed form yields, for every \(n\ge0\),
\[
\nu_p(x_n)=\nu_p(x_0)+n\nu_p(a).\tag{2}
\]
If \(p\nmid a\), every nonzero quotient has valuation zero and therefore the quotient set misses the nonempty open ball of valuation one. If \(p\mid a\), the valuations in (2) strictly increase with \(n\); a quotient has valuation zero only if its indices coincide, in which case it equals \(1\). The open set of \(p\)-adic units excluding \(1\) consequently contains a nonempty open ball disjoint from the quotient set. This proves non-density for \(\nu_p(a x_0)<\nu_p(D)\).

**3. Sufficiency.** Suppose \(c\in\mathbb Z_p\). Put \(L=1\) when \(p\nmid a\), and \(L=0\) when \(p\mid a\). There exists a sequence of positive integers \(d_j\to\infty\) for which
\[
a^{d_j}\longrightarrow L,
\qquad d_j a^{d_j}\longrightarrow0\quad\text{in }\mathbb Q_p.
\]
Indeed, if \(p\nmid a\), set \(d_j=(p-1)p^j\): Euler's theorem modulo \(p^{j+1}\) implies \(a^{d_j}\equiv1\pmod{p^{j+1}}\), and \(\nu_p(d_j)\to\infty\). If \(p\mid a\), set \(d_j=j\); then \(\nu_p(a^{d_j})\to\infty\) and \(\nu_p(d_j a^{d_j})\to\infty\).

Fix any \(z\in\mathbb Q_p\) with \(z\ne L\). For sufficiently large \(j\), both \(z-a^{d_j}\) and \(d_j a^{d_j}\) are nonzero and
\[
q_j=\frac{d_j a^{d_j}}{z-a^{d_j}}\in\mathbb Z_p\setminus\{0\},\tag{3}
\]
since the numerator tends \(p\)-adically to zero while the denominator tends to the nonzero number \(z-L\). Positive integers are dense in \(\mathbb Z_p\); hence we may choose positive integers \(n_\ell\) with \(n_\ell+c\to q_j\). For sufficiently large \(\ell\), the denominator in (1) is nonzero, and (1) gives
\[
\frac{x_{n_\ell+d_j}}{x_{n_\ell}}
\longrightarrow a^{d_j}+\frac{d_j a^{d_j}}{q_j}=z.
\]
Thus every \(z\ne L\) lies in the closure of \(R\). If \(L=1\), this point already occurs as \(x_n/x_n=1\) for any nonzero \(x_n\). If \(L=0\), choose one nonzero \(x_k\); then, as \(n\to\infty\), \(x_n=a^{n-1}D(n+c)\to0\) in \(\mathbb Q_p\), since \(n+c\in\mathbb Z_p\), so \(x_n/x_k\to0\). Thus \(L\) also belongs to the closure. We have proved that \(R\) is dense in \(\mathbb Q_p\) exactly under the asserted condition. \(\square\)

## Verification
The standalone Python verifier checks the closed form for all \(891\) integer parameter triples with \(-5\le a\le5\), \(-4\le x_0,x_1\le4\), through \(n=30\). It independently verifies the rigid valuation formula for \(460\) parameter/prime combinations with nonintegral shift, and constructs \(23\) nontrivial rational quotient approximants with at least four correct \(p\)-adic digits for several dense parameter sets and primes. Run `python3 verify.py`; the recorded output is in `verification.out`. These finite checks are not substitutes for the unrestricted proof above.

## Relationship to prior work
Antony and Barman, *\(p\)-adic quotient sets: linear recurrence sequences* (arXiv:2207.07084, initially submitted 14 July 2022), Theorem 1.7 of its 2022 preprint, proves density for the **same recurrence with arbitrary initial data** under the sufficient hypothesis \(p\nmid a(x_1-a x_0)\); its proof uses uniform distribution. The present criterion is necessary and sufficient, allowing the complementary primes and proving non-density in the opposite valuation regime. The authors' later paper *\(p\)-Adic quotient sets: linear recurrence sequences with reducible characteristic polynomials* (arXiv:2408.06949), Theorem 1.4, treats repeated roots at higher order under special initial data and the condition \(p\nmid a\); it does not settle the exceptional primes or arbitrary initial data here. Garcia and collaborators, *\(p\)-adic quotient sets* (arXiv:1607.07951), Theorem 5.2, concerns second-order recurrences with canonical initial data and leaves the case where the prime divides both recurrence coefficients open to distinct outcomes. Their geometric-progression obstruction is compatible with the degenerate case here. These prior theorems do not imply the claimed complete classification, although they motivate it.

## Limitations
The theorem treats only characteristic polynomial \((X-a)^2\), not general split or nonsplit second-order polynomials. It classifies density but not the closure of every non-dense quotient set. The literature comparison covers the cited primary papers and targeted searches but cannot exclude an equivalent statement in unindexed literature; no independent validation is asserted.

## References
1. Deepa Antony and Rupam Barman, *\(p\)-adic quotient sets: linear recurrence sequences*, arXiv:2207.07084v1 (14 July 2022), Theorem 1.7 in v2. https://arxiv.org/abs/2207.07084
2. Deepa Antony and Rupam Barman, *\(p\)-Adic quotient sets: linear recurrence sequences with reducible characteristic polynomials*, arXiv:2408.06949v1 (13 August 2024), Theorem 1.4. https://arxiv.org/abs/2408.06949
3. S. R. Garcia, Y. X. Hong, F. Luca, E. Pinsker, C. Sanna, E. Schechter, and A. Starr, *\(p\)-adic quotient sets*, arXiv:1607.07951v1 (27 July 2016), Theorem 5.2 and Lemma 2.2. https://arxiv.org/abs/1607.07951

# Prime-power towers for the prime-base binomial congruence
## Finding
Let \(p\ge 5\) and \(q\ne p\) be primes, and for \(r\ge 1\) define
\[
B_r=\binom{q p^r}{p^r}.
\]
The sequence \((B_r)\) converges in \(\mathbb Z_p^\times\); write
\[
\beta_{p,q}=\lim_{r\to\infty}B_r.
\]
Let \(\omega_p(q)\) be the Teichmuller lift of \(q\bmod p\), equivalently
\[
\omega_p(q)=\lim_{m\to\infty}q^{p^m}.
\]
Set
\[
H_{p,q}=v_p\!\left(\beta_{p,q}-\omega_p(q)\right),
\]
with \(H_{p,q}=\infty\) if the two p-adic units are equal. Then for every integer \(r\ge1\),
\[
\binom{q p^r}{p^r}\equiv q^{p^r}\pmod{p^r}
\quad\Longleftrightarrow\quad
r\le H_{p,q}.
\]
Thus, for fixed \((p,q)\), the prime-power members \(p^r\) of the prime-base binomial-congruence sequence form an initial segment of the tower \(p,p^2,p^3,\ldots\).

The first two nontrivial thresholds have a familiar form:
\[
H_{p,q}\ge2\iff q^{p-1}\equiv1\pmod{p^2},
\qquad
H_{p,q}\ge3\iff q^{p-1}\equiv1\pmod{p^3}.
\]
The first equivalence recovers the published square/Wieferich theorem; the second gives its cubic higher-Wieferich analogue. From the fourth power onward the governing invariant is the distance between the p-adic binomial limit and the Teichmuller lift, rather than only the Fermat quotient.

## Assumptions and scope
The statement is for distinct primes \(p,q\) with \(p\ge5\). It concerns only the subfamily \(n=p^r\) of the congruence
\[
\binom{qn}{n}\equiv q^n\pmod n.
\]
No claim is made here for \(p=2\) or \(p=3\), where the standard Jacobsthal modulus has exceptional small-prime behavior. The result does not assert that \(H_{p,q}\) is always finite.

## Proof
A standard Ljunggren--Jacobsthal congruence for \(p\ge5\) gives, after substituting \(a=q p^{j-1}\) and \(b=p^{j-1}\),
\[
B_j\equiv B_{j-1}\pmod{p^{3j}}
\qquad(j\ge1).
\]
Indeed, the Jacobsthal modulus contains \(p^3ab(a-b)\) up to a p-adic unit, and \(ab(a-b)\) contains \(p^{3(j-1)}\). Hence \((B_j)\) is p-adically Cauchy. More precisely, summing the tail congruences gives
\[
\beta_{p,q}\equiv B_r\pmod{p^{3(r+1)}},
\]
so in particular
\[
B_r\equiv\beta_{p,q}\pmod{p^r}.
\]

Fermat's theorem gives \(q^{p-1}\equiv1\pmod p\). By the lifting-the-exponent lemma,
\[
v_p\!\left(q^{p^{m+1}}-q^{p^m}\right)
=v_p\!\left(q^{p-1}-1\right)+m\ge m+1.
\]
Therefore \(q^{p^m}\) is p-adically Cauchy and converges to the unique \((p-1)\)-st root of unity congruent to \(q\pmod p\), namely \(\omega_p(q)\). Its tail satisfies
\[
q^{p^r}\equiv\omega_p(q)\pmod{p^r}.
\]
Combining the two approximations,
\[
B_r\equiv q^{p^r}\pmod{p^r}
\iff
\beta_{p,q}\equiv\omega_p(q)\pmod{p^r}
\iff
r\le H_{p,q}.
\]
This proves the tower classification.

For the low layers, the \(j=1\) Ljunggren congruence yields
\[
B_1=\binom{qp}{p}\equiv q\pmod{p^3},
\]
and the tail begins at a multiple of \(p^6\), so
\[
\beta_{p,q}\equiv q\pmod{p^3}.
\]
For any p-adic unit \(u\equiv1\pmod p\), LTE and \(p\nmid p-1\) give \(v_p(u^{p-1}-1)=v_p(u-1)\). Applying this to \(u=q/\omega_p(q)\) shows, for \(k=2,3\),
\[
q\equiv\omega_p(q)\pmod{p^k}
\iff
q^{p-1}\equiv1\pmod{p^k}.
\]
Together with \(\beta_{p,q}\equiv q\pmod{p^3}\), this proves the two threshold equivalences.

## Verification
The proof is infinite and rests on the stated Jacobsthal lifting plus elementary p-adic convergence and LTE. The accompanying `verify.py` is corroborative, not a replacement for that proof. It directly evaluates sixty cases with \(p\in\{5,7,11}\), \(q\in\{2,3,5,7,11,13}\setminus\{p}\), and \(1\le r\le4\), compares the original congruence with the p-adic-limit criterion, and also checks thirty selected Jacobsthal increments. Its expected terminal line is:

`VERIFY_OK cases=60 lifts=30 primes=[5, 7, 11] bases=[2, 3, 5, 7, 11, 13] r=1..4`

## Relationship to prior work
Guedes and Machado study \(\binom{qn}{n}\equiv q^n\pmod n\) for prime \(q\), with primary MSC 11B65. Their Theorem 6.2 proves, for \(p\ge5\), that the square \(p^2\) is a solution exactly when \(q^{p-1}\equiv1\pmod{p^2}\). Their proof uses Babbage--Jacobsthal lifting only at the square level. The present statement classifies every exponent in the entire prime-power tower by a single p-adic distance and recovers their square theorem as the \(r=2\) layer. It also identifies the cubic layer with the higher congruence \(q^{p-1}\equiv1\pmod{p^3}\).

Jacobsthal/Ljunggren congruences and higher-order Wieferich congruences are classical separately; the contribution here is their combination into the exact initial-segment criterion for this specific prime-base binomial congruence. Targeted searches found no published statement with this implication profile.

## Limitations
The novelty check cannot exclude every unindexed or differently phrased source. The classification packages the tower in the p-adic invariant \(H_{p,q}\); it does not give a closed formula for \(H_{p,q}\) beyond the first three layers, nor prove finiteness. Small primes \(p=2,3\) are excluded rather than forced into the same formula.

## References
1. G. A. Guedes and R. N. Machado Jr., *Structured Solutions of Prime-Base Binomial Congruences*, arXiv:2606.30232v1, first submitted 29 June 2026; primary MSC 11B65.
2. A. Granville, *Arithmetic properties of binomial coefficients I: Binomial coefficients modulo prime powers*, CMS Conference Proceedings 20 (1997), 253--275.
3. W. Keller and J. Richstein, *Solutions of the congruence \(a^{p-1}\equiv1\pmod{p^r}\)*, Mathematics of Computation 74 (2005), 927--936.

# Prime-pair densities for arithmetic numbers with two prime-power blocks
## Finding
Fix primes \(\ell<m\). For \(x\ge 2\), let \(T_{\ell,m}(x)\) count ordered pairs of distinct primes \((P,Q)\) with \(P,Q\le x\), \(P,Q\notin\{\ell,m\}\), for which
\[
N=P^{\ell-1}Q^{m-1}
\]
is arithmetic, meaning that \(\tau(N)\mid\sigma(N)\). Then
\[
T_{\ell,m}(x)\sim c_{\ell,m}\,\pi(x)^2,
\]
where
\[
c_{\ell,m}=
\frac{1}{(\ell-1)(m-1)}+
\mathbf 1_{\ell\mid m-1}\frac{m-2}{(m-1)^2}.
\]

When \(\ell\mid m-1\), the subfamily in which \(N\) is arithmetic but the prime-power factor \(Q^{m-1}\) is not arithmetic has the sharper asymptotic
\[
\#\left\{(P,Q):N\text{ arithmetic and }Q^{m-1}\text{ non-arithmetic}\right\}
\sim \frac{m-2}{(m-1)^2}\,\pi(x)^2.
\]
Thus a positive proportion of this thin two-block family is made arithmetic by a genuine cross-factor cyclotomic divisibility rather than by integrality of both prime-power factors separately.

## Assumptions and scope
The primes \(\ell<m\) are fixed. The variable primes \(P,Q\) are ordered, distinct, at most \(x\), and exclude the two fixed primes \(\ell,m\). Excluding finitely many primes and the diagonal \(P=Q\) changes the count by only \(O(\pi(x))\), which is negligible compared with \(\pi(x)^2\).

The arithmetic mean of the divisors is
\[
A(n)=\frac{\sigma(n)}{\tau(n)}.
\]
The statement concerns integrality of \(A(N)\) on the specified sparse family; it does not assert a new global density theorem for all arithmetic numbers.

## Proof
Oller-Marcén's Proposition 6 applies to
\[
N=P^{\ell-1}Q^{m-1}
\]
with the fixed exponent primes ordered as \(\ell<m\). It gives the exact criterion
\[
N\text{ is arithmetic}
\quad\Longleftrightarrow\quad
\ell\mid P-1
\quad\text{and}\quad
\left(m\mid Q-1\ \text{or}\ \operatorname{ord}_m(P)=\ell\right).
\]
The first condition is unavoidable because there is no smaller exponent-prime that can supply the factor \(\ell\). The second condition either comes from the \(Q\)-block itself or is supplied by the \(P\)-block through the cyclotomic factor corresponding to order \(\ell\) modulo \(m\).

Let
\[
\mathcal A=\{P:P\equiv1\pmod\ell\},\qquad
\mathcal B=\{Q:Q\equiv1\pmod m\},
\]
and
\[
\mathcal D=\{P:P\equiv1\pmod\ell,
\ \operatorname{ord}_m(P)=\ell\}.
\]
For each of these sets, write \(\mathcal X(x)=\{R\le x:R\in\mathcal X\}\). For fixed moduli, the prime number theorem in arithmetic progressions gives
\[
\#\{P\le x:P\in\mathcal A\}
\sim\frac{\pi(x)}{\ell-1},
\qquad
\#\{Q\le x:Q\in\mathcal B\}
\sim\frac{\pi(x)}{m-1}.
\]

If \(\ell\nmid m-1\), the cyclic group \((\mathbb Z/m\mathbb Z)^\times\) has no element of order \(\ell\), so \(\mathcal D\) is empty apart from excluded finite degeneracies. Therefore
\[
T_{\ell,m}(x)
\sim \frac{1}{(\ell-1)(m-1)}\pi(x)^2.
\]

Now suppose \(\ell\mid m-1\). Since \((\mathbb Z/m\mathbb Z)^\times\) is cyclic of order \(m-1\), it contains exactly \(\varphi(\ell)=\ell-1\) residue classes of exact order \(\ell\). Combining each of these with the single condition \(P\equiv1\pmod\ell\) by the Chinese remainder theorem produces exactly \(\ell-1\) reduced residue classes modulo \(\ell m\). Hence
\[
\#\{P\le x:P\in\mathcal D\}
\sim
\frac{\ell-1}{\varphi(\ell m)}\pi(x)
=
\frac{1}{m-1}\pi(x).
\]

The arithmetic pairs are the disjoint union of pairs with \(P\in\mathcal A\) and \(Q\in\mathcal B\), together with pairs with \(P\in\mathcal D\) and \(Q\notin\mathcal B\). Consequently
\[
T_{\ell,m}(x)
=
\#\mathcal A(x)\#\mathcal B(x)
+
\#\mathcal D(x)\left(\pi(x)-\#\mathcal B(x)\right)
+o(\pi(x)^2),
\]
where finite exclusions and the diagonal contribute only \(o(\pi(x)^2)\). Substituting the three prime-density estimates yields
\[
T_{\ell,m}(x)
\sim
\left(
\frac{1}{(\ell-1)(m-1)}
+
\frac{m-2}{(m-1)^2}
\right)\pi(x)^2.
\]
This proves the displayed formula for \(c_{\ell,m}\).

Finally, for a prime \(Q\neq m\), Oller-Marcén's prime-power criterion with exponent \(m-1\) says that \(Q^{m-1}\) is arithmetic exactly when \(m\mid Q-1\). Therefore the cross-compensated subfamily is precisely \(P\in\mathcal D\) and \(Q\notin\mathcal B\), whose density is
\[
\frac{1}{m-1}\left(1-\frac{1}{m-1}\right)
=
\frac{m-2}{(m-1)^2}.
\]

## Verification
The standalone script `verify.py` checks two independent finite consequences. First, for eight fixed pairs \((\ell,m)\), it compares the direct divisibility test \(\tau(N)\mid\sigma(N)\) against the structural criterion above for all admissible ordered variable-prime pairs up to \(500\). Second, it checks that the number of reduced residue classes modulo \(\ell m\) satisfying \(P\equiv1\pmod\ell\) and \(\operatorname{ord}_m(P)=\ell\) is exactly \(\ell-1\) when \(\ell\mid m-1\), and zero otherwise. The replay result is `VERIFY_OK pair_checks=68448 exponent_pairs=8 prime_bound=500`.

These computations are corroborative only. The infinite asymptotic rests on the exact cyclotomic criterion, cyclicity of \((\mathbb Z/m\mathbb Z)^\times\), the Chinese remainder theorem, and the prime number theorem in fixed arithmetic progressions.

## Relationship to prior work
Oller-Marcén gives a general characterization of arithmetic numbers and, in Proposition 6, the exact finite congruence/order criterion for products \(P_i^{q_i-1}\) with distinct exponent primes \(q_i\). The present finding specializes the two-block case and then derives an exact prime-pair density law and a separate positive-density cross-compensation term. Those asymptotic constants are not stated in the inspected source.

Bateman, Erdős, Pomerance and Straus prove global distribution theorems for arithmetic numbers, including density one for the full set of arithmetic integers. Their global theorem does not determine the density inside the sparse fixed-exponent family \(P^{\ell-1}Q^{m-1}\), where the cyclotomic interaction between the two blocks is visible at leading order.

OEIS entries for arithmetic numbers record the global sequence and characteristic function, but no fixed-exponent prime-pair density or cross-compensation constant was found there.

## Limitations
The theorem is restricted to two prime-power blocks whose exponents are one less than two fixed distinct primes. It does not give a comparable closed density formula for three or more blocks, where several directed order conditions can overlap. It also does not quantify secondary terms in the prime-pair asymptotic.

The originality comparison is strongest against Oller-Marcén's full characterization, the global Bateman–Erdős–Pomerance–Straus distribution theorem, published-finding corpus semantic searches for the exact fixed-family density and cross-compensation formulation, and the standard OEIS records. A differently phrased later corollary in the literature could still reproduce this specialization, although focused searches did not locate one.

## References
1. Antonio M. Oller-Marcén, "On arithmetic numbers," arXiv:1206.1823v1, 8 June 2012; later published in *Mathematische Nachrichten* 288 (2015), 665–669. Proposition 6 gives the exact criterion used here.
2. Paul T. Bateman, Paul Erdős, Carl Pomerance, and E. G. Straus, "The arithmetic mean of the divisors of an integer," *Lecture Notes in Mathematics* 899 (1981), 197–220.
3. OEIS A003601 and A245656, arithmetic numbers and their characteristic function.

# Exact prime periods of the second-symmetric four-part partition statistic

## Finding
For every integer \(n\ge0\), let
\[
a(n)=\sum_{\substack{\lambda\vdash n\\\ell(\lambda)=4}}e_2(\lambda),\qquad
e_2(\lambda)=\sum_{1\le i<j\le4}\lambda_i\lambda_j.
\]
The least positive period valid from \(n=0\) modulo every prime \(p\) is
\[
\boxed{T_p=\begin{cases}
48,&p=2,\\
54,&p=3,\\
300,&p=5,\\
12p,&p\ge7.
\end{cases}}
\]
In particular, for every prime \(p\ge7\), \(a(n+12p)\equiv a(n)\pmod p\) for all nonnegative integers \(n\), and no smaller positive translation is a period.

## Assumptions and scope
A partition has positive parts in weakly decreasing order; exactly four parts are required, including repeated parts. The sum over an empty set is zero (hence \(a(n)=0\) for \(0\le n<4\)). The modulus \(p\) is prime. "Least period" means least positive \(T\) satisfying the congruence for **every** \(n\ge0\), not only eventually. These are all prime moduli, not a claim for arbitrary composites.

## Proof
**Step 1: An exact rational generating function.** Write a four-part partition uniquely as
\[
\lambda=(a+b+c+d,\ b+c+d,\ c+d,\ d),\quad
 a,b,c\ge0,\ d\ge1.
\]
Its size is \(n=a+2b+3c+4d\), and direct expansion gives
\[
e_2(\lambda)=ab+2ac+3ad+b^2+4bc+6bd+3c^2+9cd+6d^2.
\]
Apply the exact geometric-power sums
\[
\sum_{k\ge0}z^k=\frac1{1-z},\quad
\sum_{k\ge0}kz^k=\frac z{(1-z)^2},\quad
\sum_{k\ge0}k^2z^k=\frac{z(1+z)}{(1-z)^3}.
\]
For the variable \(d\), the exponent-zero sum instead starts at one and is \(z/(1-z)\); its first- and second-power sums agree with the displayed expressions. Combining the nine quadratic monomials and cancelling a common factor gives, **as an identity in the integer formal power series ring**,
\[
F(q):=\sum_{n\ge0}a(n)q^n=\frac{P(q)}{D(q)},
\]
where
\[
\begin{aligned}
P(q)=q^4(&6+15q+34q^2+57q^3+95q^4+121q^5+146q^6\\
&+126q^7+106q^8+72q^9+50q^{10}+25q^{11}+11q^{12}),\\
D(q)&=(1-q)^6(1+q)^4(1+q^2)^3(1+q+q^2)^3.
\end{aligned}
\]
The polynomial identity can be reproduced from the displayed parametrization without relying on numerical coefficients: before cancellation the denominator is \(D_0(q)=\prod_{j=1}^{4}(1-q^j)^3\), and the numerator is \(P(q)(1-q)^6(1+q)^2\). The accompanying verifier recomputes this identity by integer polynomial multiplication. In particular, \(D(0)=1\), \(\deg P=16<22=\deg D\).

**Step 2: Minimal-period lemma.** Fix a prime \(p\). Reduce \(F=P/D\) in \(\mathbb F_p(q)\) to a coprime fraction \(P_p/D_p\), normalized by \(D_p(0)=1\), with \(\deg P_p<\deg D_p\). The coefficient sequence of \(F\bmod p\) has a period \(T\) from index zero **if and only if**
\[
D_p(q)\mid(1-q^T)\quad\text{in }\mathbb F_p[q].
\]
Indeed, exact periodicity implies \((1-q^T)F\) is a polynomial of degree less than \(T\), so coprimality implies the divisibility. Conversely the divisibility makes \((1-q^T)F=P_p(q)(1-q^T)/D_p(q)\) a polynomial; since \(\deg P_p<\deg D_p\), its degree is strictly smaller than \(T\), giving periodicity from the zeroth coefficient.

**Step 3: Cyclotomic cancellations in each characteristic.** Set \(\Phi_3(q)=1+q+q^2\) and \(\Phi_4(q)=1+q^2\). Direct polynomial reductions of the explicit numerator yield
\[
P(1)=864=2^5 3^3,\quad P(-1)=32=2^5,\quad
P\bmod\Phi_3=6q,\quad P\bmod\Phi_4=-12.
\]
Therefore \(P\) and \(D\) are coprime modulo every prime \(p\ge5\), since \(D\) is a product only of the four displayed cyclotomic factors. Direct Euclidean division in the two exceptional characteristics gives
\[
\begin{array}{c|c|c}
p&\gcd(P,D)\text{ over }\mathbb F_p[q]&D_p(q)\text{ up to units}\\\hline
2&(q+1)^4\Phi_3(q)&(q+1)^{12}\Phi_3(q)^2\\
3&(q-1)^2\Phi_4(q)^3&(q-1)^{10}(q+1)^4.
\end{array}
\]
All the gcd identities are exactly reproducible by finite-field polynomial Euclidean division in the verifier; factors may be taken monic.

**Step 4: Pole multiplicities give both the period and its minimality.** In characteristic \(p\), write \(T=p^k m\) with \(p\nmid m\). By Frobenius,
\[
1-q^T=(1-q^m)^{p^k};
\]
each \(m\)-th root of unity occurs with multiplicity exactly \(p^k\). For \(p=2\), the reduced denominator has multiplicity \(12\) at the root one and primitive third roots as zeros; hence \(16\mid T\) and \(3\mid T\). It divides \(1-q^{48}\), proving \(T_2=48\). For \(p=3\), root one has multiplicity \(10\) and root minus one occurs, so \(27\mid T\) and \(2\mid T\); the denominator divides \(1-q^{54}\), proving \(T_3=54\). For \(p=5\), the pole order \(6\) at one forces \(25\mid T\), while \(\Phi_3\) and \(\Phi_4\) force \(12\mid T\); the reduced denominator divides \(1-q^{300}\), so \(T_5=300\). Finally, for \(p\ge7\), the pole order \(6\) at one forces \(p\mid T\); primitive third and fourth roots force \(12\mid T\), and \(D\mid1-q^{12p}\). Thus the exact least period is \(12p\) for every such prime. All conclusions hold from \(n=0\) by Step 2.

## Verification
Run `python3 verify_periods.py` from the package directory with Python 3.8 or later; no third-party packages or remote services are required. It reconstructs the weighted monomial identity and full rational numerator/denominator over the integers, performs exact gcd computations modulo small primes, verifies polynomial divisibility and failure for maximal proper divisors of each predicted period for twelve primes, and independently enumerates every four-part partition for \(0\le n\le150\) to check the first 151 exact coefficients. These finite checks supplement the all-prime symbolic argument in Steps 2–4; they do **not** replace it.

## Relationship to prior work
Ballantine, Beck, and Merca [1, introduction and Theorem 2] defined the same statistic, conjectured a recurrence and a table of minimal periods for selected moduli, and proved that 48, 54 and 96 are periods modulo 2, 3 and 4, respectively. They did not establish least periods for all primes. The present rational-function argument proves the least periods modulo **every** prime, including the arbitrarily large prime range, and proves minimality in the first two cases. The unweighted partition-count period theorems mentioned in [1] apply to \(p_4(n)\), not to the distinct weighted statistic \(e_2p_4(n)\). The related follow-up [2] studies multiplicities of parts of images of elementary-symmetric partition maps rather than the periods of this weighted four-part sum. The exact period theorem does not follow from the finite conjectural table alone.

## Limitations
Only prime moduli are classified here, although the rational generating function also yields a route to prime-power and composite cases. The claim is mathematical originality relative to the inspected literature, not proof that no independently discovered or unpublished formula exists. This proof does not establish any unrelated conjecture about the injectivity of elementary-symmetric partition maps.

## References
[1] C. Ballantine, G. Beck, M. Merca, *Partitions and elementary symmetric polynomials—an experimental approach*, arXiv:2408.13346v1 (public 23 August 2024), The Ramanujan Journal 66, article 34 (2025), doi:10.1007/s11139-024-01001-6. See Introduction and Theorem 2.

[2] C. Ballantine, G. Beck, M. Merca, B. Sagan, *Elementary symmetric partitions*, arXiv:2409.11268 (first publicly posted September 2024; consulted version v3), Introduction and Sections 2–4.

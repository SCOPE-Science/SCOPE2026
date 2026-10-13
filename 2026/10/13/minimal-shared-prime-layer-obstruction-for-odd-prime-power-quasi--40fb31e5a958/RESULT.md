# Minimal shared-prime layer obstruction for odd prime-power quasi-friendly divisors
## Finding
Let \(q\) be an odd prime and let \(b\ge 3\) be odd. Call \(q^b\) a quasi-friendly divisor of \(N\) when \(q^b\mid N\) and
\[
\frac{\sigma(N)}{N}=\frac{\sigma(q^b)+1}{q^b}.
\]
If \(\nu_q(N)=b+1\), then \(N\) has at least three distinct prime divisors. Therefore, in the unresolved branch where \(q\mid N/q^b\), a host with exactly two distinct prime divisors, if one exists, must satisfy \(\nu_q(N)\ge b+3\).

## Assumptions and scope
Here \(\sigma(n)\) is the sum of the positive divisors of \(n\), \(\nu_q(N)\) is the exponent of \(q\) in \(N\), and all integers are positive. The restriction \(b\ge3\) isolates the odd prime-power cases beyond the prime case \(b=1\), for which a stronger two-prime-support obstruction is already known in the comparison database. The conclusion is a structural obstruction, not a proof that odd prime-power quasi-friendly divisors do not exist.

## Proof
Put \(S=\sigma(q^b)\). First, any such \(N\) is odd. Indeed, if \(2\mid N\), then \(\sigma(N)/N\ge3/2\). For \(q\ge5\),
\[
\frac{S+1}{q^b}<\frac{q}{q-1}+\frac1q<\frac32,
\]
a contradiction. For \(q=3\), divisibility by both \(2\) and \(3\) gives \(\sigma(N)/N\ge\sigma(6)/6=2\), whereas the same upper estimate is less than \(2\).

Because \(b\) is odd, \(S\) is even, so \(S+1\) is odd. From \(q^b\sigma(N)=N(S+1)\), and from oddness of \(q\), \(N\), and \(S+1\), it follows that \(\sigma(N)\) is odd. For odd \(N\), the product formula for \(\sigma\) shows that \(\sigma(N)\) is odd exactly when every prime exponent of \(N\) is even. Hence \(N\) is a square.

Suppose toward a contradiction that \(N\) has exactly two distinct prime divisors and \(\nu_q(N)=b+1\). Then
\[
N=q^{b+1}p^{2a}
\]
for some prime \(p\ne q\) and integer \(a\ge1\). Since \(q^bp\mid N\), monotonicity of the abundancy index under divisibility gives
\[
\frac{S}{q^b}\left(1+\frac1p\right)\le\frac{S+1}{q^b},
\]
so \(p\ge S\).

Let \(H=\sigma(q^{b+1})=S+q^{b+1}\). Multiplicativity and the defining equality give
\[
\frac{\sigma(p^{2a})}{p^{2a}}
=\frac{q(S+1)}{H}
=1+\frac{q-1}{H},
\]
because \(q(S+1)-H=q-1\). Subtracting \(1\) yields
\[
\frac{\sigma(p^{2a-1})}{p^{2a}}=\frac{q-1}{H},
\]
therefore
\[
\sigma(p^{2a-1})H=(q-1)p^{2a}.
\]
Now \(p\ge S>q\), so \(p\nmid q-1\), while \(\sigma(p^{2a-1})\equiv1\pmod p\). Thus \(p^{2a}\mid H\).

On the other hand, \(p^{2a}\ge p^2\ge S^2\), whereas
\[
S^2>H.
\]
To see the last inequality, note that \(S-1=q+\cdots+q^b\ge q^b\) and \(S>q\), so \(S(S-1)>q^{b+1}\); equivalently, \(S^2>S+q^{b+1}=H\). Hence a positive integer at least \(S^2\) cannot divide \(H<S^2\), a contradiction.

Thus the minimal shared-prime layer \(\nu_q(N)=b+1\) cannot have two-prime support. In the shared-prime branch \(\nu_q(N)>b\); since \(N\) is a square and \(b\) is odd, the next possible exponent after the excluded even integer \(b+1\) is at least \(b+3\).

## Verification
The proof is symbolic and uses only multiplicativity of \(\sigma\), monotonicity of \(\sigma(n)/n\) under divisibility, parity of divisor sums, and exact divisibility. The bundled `verify.py` independently checks the central rational identity and the inequality \(S^2>\sigma(q^{b+1})\) for all odd primes \(q<200\) and odd \(3\le b\le13\), and performs a direct finite regression over small two-prime candidates. Its output is recorded in `verification_output.txt`.

## Relationship to prior work
Holdener and Holdener prove that for an odd prime \(q\), every host of the ratio \( (\sigma(q^b)+1)/q^b \) is odd; they show every other prime divisor \(p\) of the host satisfies \(p\ge\sigma(q^b)\), and they note that the host is a square when \(b\) is odd. They explicitly state that existence of quasi-friendly divisors \(q^{2\ell+1}\) is unknown and identify the shared-prime case as unresolved. The present finding combines those structural facts with an exact minimal-layer identity to eliminate the first possible shared \(q\)-adic exponent for every odd \(b\ge3\) in the two-prime-support case.

A separate published-database finding rules out all two-prime-support hosts when the divisor itself is prime, corresponding to \(b=1\). That stronger prime case does not imply the statement here for \(b\ge3\). Current OEIS records A240991 and A387406 provide computational and structural context but do not state this valuation-layer obstruction.

## Limitations
The result does not exclude hosts with at least three distinct prime divisors, nor two-prime-support hosts with \(\nu_q(N)\ge b+3\). It therefore narrows, but does not resolve, the open existence problem for odd prime-power quasi-friendly divisors. No claim is made about even \(b\).

## References
C. A. Holdener and J. A. Holdener, “Characterizing Quasi-Friendly Divisors,” Journal of Integer Sequences 23 (2020), Article 20.8.4, published September 2, 2020. https://cs.uwaterloo.ca/journals/JIS/VOL23/Holdener/holdener4.html

OEIS A240991, integers associated with quasi-friendly-divisor abundancy ratios. https://oeis.org/A240991

OEIS A387406, a related largest-prime-factor construction. https://oeis.org/A387406

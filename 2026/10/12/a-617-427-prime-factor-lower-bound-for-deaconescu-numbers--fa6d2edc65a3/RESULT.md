# A 617,427-prime-factor lower bound for Deaconescu numbers
## Finding
Let \(S_2\) be Schemmel's second totient. Every composite integer \(n\) satisfying \(S_2(n)\mid\varphi(n)-1\) has at least \(617427\) distinct prime factors: \(\omega(n)\ge617427\). The proof combines the forced residue patterns modulo \(3\) with a modulo-\(5\) incompatibility in the only low-multiplier branches and exact integer interval certificates for the resulting extremal prime products. No existence of a Deaconescu number is asserted.

## Assumptions and scope
Schemmel's second totient is multiplicative, with
\[
S_2(p^a)=p^{a-1}(p-2)
\]
for odd primes \(p\), and \(S_2(2^a)=0\). A Deaconescu number is a composite positive integer \(n\) for which \(S_2(n)\mid\varphi(n)-1\).

Such an \(n\) is odd and squarefree. If \(2\mid n\), then \(S_2(n)=0\), which cannot divide the positive integer \(\varphi(n)-1\). If \(p^2\mid n\) for an odd prime \(p\), then \(p\mid S_2(n)\) and \(p\mid\varphi(n)\), contradicting \(S_2(n)\mid\varphi(n)-1\). Thus
\[
n=\prod_{i=1}^r p_i,\qquad r=\omega(n).
\]
There is a positive integer \(M\) satisfying
\[
M\prod_{i=1}^r(p_i-2)=\prod_{i=1}^r(p_i-1)-1.
\]
The quotient \(M\) is odd. Also \(M\ne1\): for \(r\ge2\), setting \(a_i=p_i-2\ge1\) gives \(\prod(a_i+1)-1>\prod a_i\). Hence \(M\ge3\).

The theorem is a necessary condition only; it does not assert the existence of a Deaconescu number.

## Proof
The defining equation gives
\[
M<\frac{\varphi(n)}{S_2(n)}
=\prod_{p\mid n}\frac{p-1}{p-2}.
\]
The factor \(1+1/(p-2)\) strictly decreases with \(p\), so under any fixed congruence restrictions the largest product with a fixed number of prime factors comes from the smallest admissible primes.

First reduce modulo \(3\). If \(3\nmid n\), primes congruent to \(1\) and \(2\) modulo \(3\) cannot both divide \(n\): a \(2\pmod3\) factor makes the left side zero, while a \(1\pmod3\) factor makes the right side \(-1\). Hence all prime factors lie in a single nonzero residue class. If all are \(1\pmod3\), then
\[
M\equiv(-1)^{r+1}\pmod3,
\]
so \(M\ge5\).

If \(3\mid n\), no other prime factor can be \(2\pmod3\); otherwise the left side is zero modulo \(3\), while the right side is either \(-1\) or \(1\). Thus every other prime factor is \(1\pmod3\), and
\[
M\equiv(-1)^r\pmod3.
\]
Therefore \(M\ge7\) when \(r\) is even and \(M\ge5\) when \(r\) is odd.

Put \(N=617426\). The certified extremal inequalities are as follows.

For the first \(N\) primes \(q_j\equiv1\pmod3\),
\[
\prod_{j=1}^{N}\frac{q_j-1}{q_j-2}<5,
\]
with terminal prime \(19404061\). This excludes all \(3\nmid n\) cases with all factors \(1\pmod3\) and \(r\le N\).

Now suppose \(3\nmid n\) and all prime factors are \(2\pmod3\). For the first \(N\) such primes the unrestricted extremal product is below \(5\), with terminal prime \(19394777\). Thus any solution with \(r\le N\) would have \(M=3\).

In this branch reduce the defining equation modulo \(5\). If one factor is \(2\pmod5\), then \(\prod(p-2)\equiv0\pmod5\); if another factor is \(1\pmod5\), then \(\prod(p-1)\equiv0\pmod5\). Both types together would force \(0\equiv-1\pmod5\), impossible. Therefore at least one of the residue classes \(1\pmod5\) and \(2\pmod5\) is absent. The first \(N\) primes with \(p\equiv2\pmod3\) and \(p\not\equiv1\pmod5\) have product
\[
\prod\frac{p-1}{p-2}<3,
\]
with terminal prime \(26374847\); the corresponding product for \(p\not\equiv2\pmod5\) is also below \(3\), with terminal prime \(26375759\). Either alternative contradicts \(M=3<\varphi(n)/S_2(n)\).

It remains to treat \(3\mid n\). For even \(r\le N\), the first \(N-1\) primes \(q\equiv1\pmod3\) satisfy
\[
2\prod\frac{q-1}{q-2}<7,
\]
with terminal prime \(19404043\), contradicting \(M\ge7\).

For odd \(r\le N\), one has \(r\le617425\). The preceding bound implies the ratio is below \(7\), so \(M\equiv2\pmod3\) forces \(M=5\). Modulo \(5\), any remaining factor \(q\equiv1\pmod5\) would make the right-hand product zero and force \(0\equiv-1\pmod5\). Thus every \(q\ne3\) satisfies \(q\equiv1\pmod3\) and \(q\not\equiv1\pmod5\). For the first \(617424\) such primes,
\[
2\prod\frac{q-1}{q-2}<5,
\]
with terminal prime \(26375263\). This contradicts \(M=5\).

Every case with \(r\le617426\) is impossible. Therefore
\[
\omega(n)\ge617427.
\]

For calibration, adjoining the next prime \(26375269\) in the final restricted stream makes the last extremal product exceed \(5\). Thus this specific modulo-\(3\)/modulo-\(5\) sieve reaches its natural endpoint here.

## Verification
The accompanying `verify.py` uses no floating-point comparison. It sieves primes through \(30000000\) and certifies all seven endpoint inequalities by summing outward-rounded integer intervals for logarithms.

For each factor \(1+1/m\), the checker encloses \(\log(1+1/m)\) with a twelve-term alternating series and its next-term remainder. Threshold logarithms are enclosed with the positive atanh series. All interval endpoints are integers after scaling by \(10^{24}\).

A successful replay ends with:
`VERIFY_OK lower_bound=617427 crossing_prime=26375269`

The finite computation certifies only the extremal inequalities; the reduction from an arbitrary Deaconescu number to those inequalities is the symbolic proof above.

## Relationship to prior work
Hasanalizade proved that a Deaconescu number is odd, squarefree, and has at least seven distinct prime factors. Mandal's 2025 paper raised the general lower bound to \(17\), proved a \(48\)-factor bound in its multiplier-\(3\) branch, and used a modulo-\(5\) exclusion in a smaller multiplier argument.

A public 2026 record with opaque identifier `25be8c179689` proved the stronger general bound \(2859\) from a complete modulo-\(3\) classification and exact extremal products. The present proof adds the modulo-\(5\) incompatibilities that become available after the ratio estimate forces \(M=3\) or \(M=5\). This thins the extremal prime streams and raises the general lower bound to \(617427\).

Targeted searches for the exact bound, the adjacent cutoff, the crossing prime, modulo-\(5\) refinements, and equivalent Schemmel-totient formulations found no prior theorem implying the result. Search non-detection is supporting evidence only; the originality comparison rests on direct inspection of the closest theorem statements and proofs.

## Limitations
The theorem does not settle Deaconescu's conjecture and gives no example of a Deaconescu number. The number \(617427\) is the endpoint of this particular modulo-\(3\)/modulo-\(5\) extremal-product sieve, not a claim of an optimal lower bound under all possible methods.

A later or poorly indexed source could contain the same strengthening; the literature checks reduce but cannot eliminate that residual originality risk.

## References
1. Sagar Mandal, “A Note on Deaconescu's Conjecture,” arXiv:2507.02930v1, first public 26 June 2025; MSC 11A25.
2. Elchin Hasanalizade, “On a conjecture of Deaconescu,” arXiv:2206.10355v1, first public 14 June 2022.
3. “Deaconescu numbers require at least 2859 distinct prime factors,” public research record, 4 October 2026, opaque identifier `25be8c179689`.
4. M. Deaconescu, “Adding units mod \(n\),” Elemente der Mathematik 55 (2000), 123–127.

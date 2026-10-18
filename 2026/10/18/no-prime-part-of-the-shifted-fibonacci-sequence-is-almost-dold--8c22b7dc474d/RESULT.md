# No prime part of the shifted Fibonacci sequence is almost Dold

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). For each prime \(p\), define the sequence \(b^{(p)}=(b^{(p)}_n)_{n\ge1}\) by
\[
b^{(p)}_n=p^{\nu_p(F_{n+1})}.
\]
**Theorem.** For every prime \(p\) and every positive integer \(K\), the sequence \(K b^{(p)}\) fails the Dold congruences. Thus the one-step-shifted Fibonacci sequence \((F_{n+1})_{n\ge1}\) has no almost-Dold prime parts, and consequently has no almost-realizable prime parts. Its good-prime sets for both properties are empty (and hence have relative prime density zero).

## Assumptions and scope
The \(p\)-part of a positive integer \(a\) means \(p^{\nu_p(a)}\). A sequence \(u=(u_n)_{n\ge1}\) is Dold if
\[
\sum_{d\mid n}\mu(n/d)u_d\equiv0\pmod n
\]
for every positive integer \(n\). It is almost Dold if some positive integer multiple is Dold. In particular, a Dold sequence satisfies
\[
u_{q^s}\equiv u_{q^{s-1}}\pmod{q^s}
\]
for every prime \(q\) and positive integer \(s\). The theorem applies to all primes \(p\), including \(2\) and \(5\), and uses this necessary congruence with a possibly different index prime \(q\).

## Proof
Fix \(p\) and suppose \(K b^{(p)}\) is Dold for a fixed positive integer \(K\). It suffices to exhibit a prime \(q\), infinitely many unbounded exponents \(s\), and a fixed nonzero integer \(c\) satisfying
\[
b^{(p)}_{q^s}-b^{(p)}_{q^{s-1}}=c.
\]
Indeed, Dold would then imply \(q^s\mid Kc\) for arbitrarily large \(s\), which is impossible.

**Case 1: \(p\ne2,5\).** Let \(r\) be the least positive index with \(p\mid F_r\), and let \(e=\nu_p(F_r)\ge1\). The classical rank-of-apparition theorem gives \(r\ge3\), \(r\mid p-(5/p)\) (Legendre symbol), and hence \(\gcd(p,r)=1\). The standard Fibonacci valuation formula is
\[
\nu_p(F_m)=
\begin{cases}
e+\nu_p(m/r),&r\mid m,\\
0,&r\nmid m.
\end{cases}
\]
The Chinese remainder theorem and Dirichlet's theorem supply a prime \(q\) with \(q\equiv-1\pmod r\) and \(q\equiv1\pmod p\): the combined residue class is coprime to \(pr\). For each even integer \(s\ge2\), \(q^s+1\equiv2\pmod r\), so \(r\nmid(q^s+1)\), and therefore \(b^{(p)}_{q^s}=1\). At the preceding odd exponent, \(q^{s-1}+1\equiv0\pmod r\) and \(q^{s-1}+1\equiv2\pmod p\). Thus \(\nu_p((q^{s-1}+1)/r)=0\), so \(b^{(p)}_{q^{s-1}}=p^e\). Their difference is the fixed nonzero integer \(1-p^e\).

**Case 2: \(p=2\).** Set \(q=5\). At each even \(s\ge2\), \(5^s+1\equiv2\pmod3\), so \(2\nmid F_{5^s+1}\) and \(b^{(2)}_{5^s}=1\). At odd \(s-1\), the integer \(m=5^{s-1}+1\) is divisible by \(6\), but \(m\equiv6\pmod8\). The exact formula \(\nu_2(F_m)=\nu_2(m)+2\) for \(6\mid m\) gives \(b^{(2)}_{5^{s-1}}=2^3=8\). The difference is always \(-7\).

**Case 3: \(p=5\).** Set \(q=19\) and restrict to \(s=10j+2\) with \(j\ge0\). Then \(19^s+1\equiv2\pmod5\), hence \(b^{(5)}_{19^s}=1\) by \(\nu_5(F_m)=\nu_5(m)\). For the preceding odd exponent \(s-1\), the lifting-the-exponent lemma gives
\[
\nu_5(19^{s-1}+1)=\nu_5(19+1)+\nu_5(s-1)=1,
\]
since \(s-1\equiv1\pmod5\). Thus \(b^{(5)}_{19^{s-1}}=5\), and the difference is always \(-4\).

Every prime lies in exactly one of these cases, proving the theorem. Realizability, even after an integer multiplier, implies the Dold congruences, so the final assertion follows.

## Verification
The proof is unconditional and uses only classical rank, valuation, Dirichlet, and lifting-the-exponent results. The accompanying exact-integer program `artifacts/check.py` computes the rank and an admissible prime \(q\) for each of the first \(16\) primes (through \(53\)), then directly checks \(63\) of the claimed consecutive prime-power differences by modular fast doubling. Run `python3 artifacts/check.py` from the extracted package. This finite verification is supplementary and does not prove the universal quantifiers.

## Relationship to prior work
Chuysurichay, Jaidee, Panraksa, and Ward prove in their Theorem 2.4 that every prime part of the *unshifted* Fibonacci sequence \((F_n)_{n\ge1}\) is almost Dold and determine its finite repair multiplier. They also state the relevant rank-of-apparition valuation formulas and the prime-power criterion for Dold sequences. The theorem above gives the opposite extreme for the adjacent shifted sequence \((F_{n+1})_{n\ge1}\): no local prime part admits any finite repair multiplier. Their results do not imply this because taking prime parts does not commute with changes of the index, and their explicit Dold transforms apply to the unshifted sequence. Related studies of trace-type companion Lucas sequences and of unmodified linear recurrences do not cover this shifted nonlinear prime-part sequence. The comparison concerns mathematical implications, not a claim that literature search proves uniqueness.

## Limitations
The theorem concerns precisely the shift \(F_{n+1}\) and integer repair multipliers; it neither classifies all shifts \(F_{n+h}\) nor supplies quantitative minimal-failure exponents for arbitrary \(K\). Dirichlet's theorem proves existence of index primes in the general case but gives no explicit least prime. Unindexed or less accessible earlier results could cover the same theorem; independent review has not been performed.

## References
1. S. Chuysurichay, S. Jaidee, C. Panraksa, and T. Ward, *The local Dold congruence for Fibonacci and Lucas sequences*, arXiv:2609.24544v1, first public 2026-09-21. https://arxiv.org/html/2609.24544v1 . Section 1 and Theorem 2.4, equations (2.8) and the subsequent valuation formula.
2. J. Byszewski and collaborators, *Dold sequences, periodic points, and dynamics*, Bulletin of the London Mathematical Society (2021). https://doi.org/10.1112/blms.12531 . Background on Dold sequences and realizability.
3. Classical Dirichlet theorem on primes in reduced arithmetic progressions, Chinese remainder theorem, and lifting-the-exponent lemma.

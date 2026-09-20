# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

### Local criterion
The proof was checked algebraically from the defining Egyptian fraction. With \(P_i=p_i^{a_i}\), \(m_i=n/P_i\), and \(U_i=(P_i-1)/(p_i-1)\), multiplying by \(n\) gives
\[
nH(n)=1+\sum_i m_iU_i.
\]
Modulo \(P_i\), every term except the \(i\)-th vanishes. Because \(p_i-1\) is invertible modulo \(P_i\),
\[
1+m_iU_i\equiv0\pmod{P_i}
\]
is equivalent to \(m_i\equiv p_i-1\pmod{P_i}\). Pairwise coprimality of the \(P_i\) then gives the claimed equivalence with integrality of \(H(n)\).

For \(\omega(n)\le4\), the geometric-series bound was checked separately for support sizes 1 through 4. In every case \(0<H(n)<2\), so an integral value must be 1. The squarefree specialization gives \(n/p\equiv-1\pmod p\), agreeing with the known weak-primary-pseudoperfect/1-Sondow condition.

### Three-support rigidity
The proof was checked case by case. Odd smallest prime is excluded by the strict reciprocal upper bound \(389/420<1\). After setting \(A=2^a\), \(R=r^c\), \(V=(R-1)/(r-1)\), and \(d=q-A\), the defining equation reduces to
\[
d-1=[Aq-d(r-1)]V.
\]
If \(d=1\), primality modulo 3 forces \(A=2,q=3,r=7\). If \(d>1\), positivity forces \(V\le d-1\), excluding \(c\ge2\). For \(c=1\), one obtains \(d(r-A)=A^2+1\); modulo 3, one of the two larger prime candidates is divisible by 3 and greater than 3, contradiction. The converse family identity for \(6\cdot7^c\) telescopes exactly.

A standalone exact-rational program checks all 98,158 integers up to 100,000 having at most four distinct prime divisors and reports zero disagreements between the local congruence test and prime power pseudoperfectness. The same program directly verifies the first twelve values of \(6\cdot7^c\). This computation supports but is not needed for the general proofs.

**Correctness verdict: PASS.**

## Originality
The main older source inspected was Machacek's 2018 paper introducing prime power pseudoperfect numbers. Its Theorem 3 proves that the A073935 construction supplies prime power pseudoperfect numbers, and Proposition 5 gives closure constructions, including the family obtained by adjoining powers of \(n+1\) when \(n+1\) is prime. It explicitly notes that the converse from prime power pseudoperfect numbers to A073935 fails, using 23994 as an example. No theorem in the inspected paper states the local congruence criterion above or a converse/uniqueness classification for the three-support slice with middle exponent one.

OEIS A283423 was checked for its definition, listed terms, formulas, comments, and references. It records the sequence and the A073935 inclusion but does not state the two results here. Searches were also made using exact and synonymous phrases involving prime power pseudoperfect numbers, prime-power divisibility, local congruences, three prime factors/supports, and the family \(6\cdot7^c\).

The closest established local analogue located is the squarefree weak-primary-pseudoperfect/1-Sondow condition. The μ-Sondow framework studies integrality of \(\mu/n+\sum_{p\mid n}1/p\), whose prime-power-divisor characterization is different from the present sum over every power \(p^k\mid n\). Wang's 2026 work develops local residual equations for primary pseudoperfect numbers but is likewise squarefree. These sources were checked because an equivalent local formulation would be the principal originality risk.

No source located in this search states either (i) the all-\(n\) equivalence between integrality of \(H(n)\) and \(n/p^a\equiv p-1\pmod{p^a}\), together with its \(\omega(n)\le4\) consequence, or (ii) the uniqueness of \(6\cdot7^c\) among three-support prime power pseudoperfect numbers with middle exponent one. The current SCOPE archive was also searched by the mathematical object, sequence identifier A283423, and related terminology, with no overlapping record found.

Originality remains **to the best of our knowledge**. The main residual risk is an equivalent statement in literature indexed under generalized Egyptian fractions, weak primary pseudoperfect numbers, or Sondow-type congruences rather than the phrase "prime power pseudoperfect". The relevant sources above were accessible and inspected; no specific inaccessible paper was identified as likely to overturn the claim.

**Originality verdict: PASS.**

## Value
The local theorem converts a global reciprocal identity into independent congruences at each maximal prime power, and is exact for every number with at most four prime supports. The three-support theorem then gives a genuine converse to a known construction in a natural infinite slice: Machacek's closure rule produces \(6\cdot7^c\), while the present result proves these are the only possibilities when the middle support is simple. It also isolates where any different three-support examples must occur, namely with middle exponent at least two.

**Value verdict: PASS.**

## Scientific limitations
The support-size cutoff in the equality criterion is essential to the present proof: for larger support the local congruences guarantee integrality, but an additional argument is needed to force the integral value to be 1. The three-support theorem does not treat middle exponent \(b\ge2\). The computational check is finite and is not a substitute for either proof. No formal proof-assistant verification is claimed.

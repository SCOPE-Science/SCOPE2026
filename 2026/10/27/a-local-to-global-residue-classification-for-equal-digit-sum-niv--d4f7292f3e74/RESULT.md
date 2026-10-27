# A local-to-global residue classification for equal-digit-sum Niven numbers in power-related bases

## Finding
Fix integers \(b\ge2\) and \(k\ge2\), and put \(B=b^k\). Let \(s_a(n)\) denote the digit sum of a positive integer \(n\) in base \(a\). For every modulus \(m\ge1\), write \(m_0\) for the largest divisor of \(m\) whose prime factors all divide \(b\), and \(m_1=m/m_0\). Define \(v\ge0\) to be the least integer such that \(m_0\mid B^v\), and define the finite set of permitted low-block prefixes
\[
\mathcal C_v=\left\{\sum_{j=0}^{v-1}d_jB^j:0\le d_j<b\right\},\qquad \mathcal C_0=\{0\}.
\]
For each \(0\le r<m\), the following are equivalent:

1. There is at least one positive integer \(n\equiv r\pmod m\) with \(s_b(n)=s_B(n)\).
2. The residue of \(r\) modulo \(m_0\) belongs to the reduction of \(\mathcal C_v\) modulo \(m_0\).
3. There exist infinitely many positive integers \(n\equiv r\pmod m\) for which
   \[
   s_b(n)=s_B(n)\quad\text{and}\quad s_b(n)\mid n.
   \]
The common digit sums in assertion 3 can be chosen arbitrarily large. In particular, every admissible progression contains infinitely many integers simultaneously Niven in bases \(b\) and \(b^k\), even when \(\gcd(m,b)>1\).

For \(m=B^v\), \(v\ge1\), there are exactly \(b^v\) admissible residue classes among the \(B^v\) classes: they are precisely the base-\(B\) words of length \(v\) over \(\{0,1,\ldots,b-1\}\). The other classes contain no positive integer with equal digit sums in the two bases.

## Assumptions and scope
All variables \(b,k,m,v\) are integers in the ranges above. The base \(B=b^k\) is a genuine power with \(k\ge2\). The integer \(m_0\) is uniquely defined by retaining in \(m\) exactly the prime powers supported on the primes dividing \(b\); thus \(\gcd(m_1,b)=1\). The definition of \(v\) permits \(v=0\), including \(m_0=1\). For the empty prefix, the digit sum and numerical value are both zero. An integer is Niven in base \(a\) precisely when its positive base-\(a\) digit sum divides it. All congruences in the proof are ordinary integer congruences.

## Proof
**Digit-block necessity.** Write \(n=\sum_{j\ge0}d_jB^j\), with \(0\le d_j<B\). Expanding each digit \(d_j\) into its \(k\) base-\(b\) digits involves no overlapping positions. Consequently \(s_b(n)=\sum_j s_b(d_j)\), whereas \(s_B(n)=\sum_jd_j\). For a nonnegative integer \(d\), one has \(s_b(d)\le d\), with equality if and only if \(0\le d<b\). Indeed, replacing a digit at any position \(\ell\ge1\) by its numerical value strictly increases its contribution from \(d_\ell\) to \(d_\ell b^\ell\). Therefore equality of the two digit sums forces every base-\(B\) digit into \(\{0,\ldots,b-1\}\). Since \(m_0\mid B^v\), the first \(v\) digits determine \(n\pmod{m_0}\), establishing 1 implies 2. Assertion 3 trivially implies 1.

**A bounded-length repunit coin lemma.** For \(B\ge2\), put \(U_j=(B^j-1)/(B-1)\) for \(j\ge1\). Every nonnegative integer \(R\) is a sum of \(K\) terms drawn from \(\{U_j:j\ge1\}\), where \(K\le B\log_B(1+(B-1)R)\) for \(R\ge1\), and \(K=0\) for \(R=0\). To see this, take the largest \(U_J\le R\), subtract its integer quotient, and repeat on the remainder. The recurrence \(U_{j+1}=BU_j+1\) ensures that no quotient exceeds \(B\), and \(J\le\log_B(1+(B-1)R)\). This proves the claimed bound by a finite greedy descent.

**Constructive sufficiency.** Suppose 2 holds. Choose a prefix \(c=\sum_{j=0}^{v-1}d_jB^j\in\mathcal C_v\) with \(c\equiv r\pmod{m_0}\); put \(d=\sum_{j=0}^{v-1}d_j\). Because \(B\equiv1\pmod{B-1}\), the integer
\[
T=\frac{c-d}{B-1}\ge0
\]
is well-defined. Choose a positive integer \(s\) as large as needed, satisfying \(s\equiv r\pmod{m_1}\) and \(\gcd(s,B)=1\). There are arbitrarily large such \(s\): the Chinese remainder theorem combines the congruence modulo \(m_1\) with \(s\equiv1\) modulo the radical of \(b\). In the case \(m_1=1\), the first condition is vacuous.

Set \(N=\operatorname{lcm}(s,m_1)\) and \(q=N/\gcd(N,B-1)\). Choose the representative \(R\in\{0,\ldots,q-1\}\) of \(-T\pmod q\). By the coin lemma, write \(R=\sum_{i=1}^{K}U_{j_i}\). For fixed \(b,k,m,c\) and growing \(s\), one has \(N\le sm_1\), hence \(R<sm_1\) and \(K=O_{B,m}(\log(s+1))\). We may therefore require \(K\le s-d\).

Since \(\gcd(N,B)=1\), let \(L\ge1\) be the multiplicative order of \(B\) modulo \(N\) (when \(N=1\), set \(L=1\)). Choose \(K\) pairwise distinct exponents \(e_i\ge v\) with \(e_i\equiv j_i\pmod L\), and another \(s-d-K\) distinct exponents \(f_i\ge v\) with \(f_i\equiv0\pmod L\), all disjoint from the first group. Such exponents exist because every specified residue class modulo \(L\) contains infinitely many sufficiently large integers. Set
\[
n=c+\sum_{i=1}^{K}B^{e_i}+\sum_{i=1}^{s-d-K}B^{f_i}.
\]
All base-\(B\) digits of \(n\) lie below \(b\). They consist of the prescribed prefix and \(s-d\) additional unit digits, so \(s_b(n)=s_B(n)=d+(s-d)=s\). Each added term is divisible by \(m_0\), giving \(n\equiv c\equiv r\pmod{m_0}\). Modulo \(N\) we have
\[
\begin{aligned}
n&\equiv c+(s-d-K)+\sum_{i=1}^{K}B^{j_i}\\
 &=s+(c-d)+\sum_{i=1}^{K}(B^{j_i}-1)\\
 &=s+(B-1)(T+R)\equiv s\pmod N,
\end{aligned}
\]
since \(q\mid T+R\) and \(N=\gcd(N,B-1)q\) divides \((B-1)(T+R)\). Hence \(s\mid n\) and \(n\equiv s\equiv r\pmod{m_1}\). Coprimality of \(m_0\) and \(m_1\) now gives \(n\equiv r\pmod m\). Letting the unbounded admissible values of \(s\) vary produces distinct \(n\), completing 2 implies 3.

**Exact power-modulus count.** If \(m=B^v\), the reduction map \(\mathcal C_v\to\mathbb Z/B^v\mathbb Z\) is injective by uniqueness of base-\(B\) expansions. Each of the \(v\) digits has exactly \(b\) choices, giving precisely \(b^v\) admissible classes. The previous necessity excludes the remaining classes.

## Verification
The supplied `verify.py` implements the prefix criterion, greedily decomposes the modular correction into repunits, constructs disjoint high exponents, and checks all relevant congruences using exact modular exponentiation. It additionally materializes moderate-size constructed integers and checks the digit sums independently. The program tests all modulus/residue pairs for \(2\le b\le5\), \(1\le k\le3\), and \(1\le m\le30\), using the known \(k=1\) case as a consistency test. See `VERIFICATION.md` for results and finite-test limitations. The unrestricted theorem is established by the proof, not by the finite experiments.

## Relationship to prior work
Kominers, *Simultaneous Niven Numbers in Arithmetic Progressions for Power-Related Bases* (first public arXiv version February 1, 2026), proves infinitude for \(\gcd(m,b)=1\), using a fixed-spaced unit-digit construction; it also notes that this condition is an assumption of that method. The present theorem determines exactly which noncoprime progressions can contain **equal-digit-sum** simultaneous Niven numbers, proving sufficiency in every locally admissible class with a logarithmic-length repunit correction. Harrington–Litman–Wong (2023/2024) prove the single-base Niven result in all progressions but do not impose simultaneous equal digit sums. Witno (2016), Theorems 4.2–4.4, treats sparse generalized repunits, prescribed digit sums and specified trailing digits for single-base Niven numbers, but not the complete local residue spectrum of equal-digit-sum two-base Niven numbers. These results are used as context; the proof here is independent of them.

## Limitations
The theorem does not characterize all integers that are simultaneously Niven without equality of digit sums. No asymptotic density or efficient minimal-witness estimate is asserted for the constructed infinite families. The greedy-digit construction can produce very large exponents. Novelty is assessed against the identified literature and research records; an unindexed equivalent result cannot be categorically excluded. Independent scholarly audit has not been performed.

## References
1. S. D. Kominers, *Simultaneous Niven Numbers in Arithmetic Progressions for Power-Related Bases*, arXiv:2602.01252v1 (2026-02-01), especially Theorem 1.1, Proposition 2.1, Sections 3–7. https://arxiv.org/abs/2602.01252
2. J. Harrington, M. Litman, and T. W. H. Wong, *Every Arithmetic Progression Contains Infinitely Many b-Niven Numbers*, arXiv:2303.06534v1 (2023-03-12), Bull. Aust. Math. Soc. 109 (2024), 409–413. https://arxiv.org/html/2303.06534v1
3. A. Witno, *Niven Repunits in General Bases*, Fibonacci Quarterly 54 (2016), no. 1, 59–64, especially Theorem 1.3 and Sections 2–4. https://www.fq.math.ca/Papers1/54-1/Witno11122015.pdf

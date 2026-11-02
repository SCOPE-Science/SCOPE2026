# Sharp six-support maximum for unitary phi-practical integers

## Finding
An integer \(n\ge1\) is **unitary \(\varphi\)-practical** when each integer from \(0\) through \(n\) is a sum of the unitary-totient values \(\varphi^*(d)\) associated with distinct unitary divisors \(d\) of \(n\). Here \(d\) is unitary if \(\gcd(d,n/d)=1\), and \(\varphi^*(p^e)=p^e-1\) for prime powers. Repeated numerical values still count as distinct items when their divisor indices differ.

**Theorem.** Among all unitary \(\varphi\)-practical positive integers with exactly six distinct prime factors, the unique largest is
\[
\boxed{N=2^{32}(2^{32}-1)=18446744069414584320.}
\]
Its factorization into distinct prime-power components, in increasing component order, is
\[
N=3\cdot5\cdot17\cdot257\cdot65537\cdot2^{32}.
\]
The universal six-component greedy upper bound \(2^{64}-1\) is thus missed by **exactly** \(2^{32}-1=4294967295\). This is the *first* support size at which the general greedy upper bound cannot be attained: it is attained uniquely at each support size \(1,2,3,4,5\).

## Assumptions and scope
All integers and exponents are positive unless explicitly stated otherwise. The support size \(\omega(n)\) is the number of distinct prime bases, regardless of their exponents; it must equal six in the maximum theorem. Write
\[
n=Q_1Q_2\cdots Q_r,\qquad Q_1<Q_2<\cdots<Q_r,
\]
where each \(Q_i=p_i^{e_i}\) is a prime power and the \(p_i\) are pairwise distinct. Put \(M_0=1\) and \(M_i=\prod_{j=1}^iQ_j\). The unitary-divisor multiset of weights is indexed by subsets \(J\subseteq\{1,\ldots,r\}\):
\[
w_J=\varphi^*\!\left(\prod_{j\in J}Q_j\right)=\prod_{j\in J}(Q_j-1).
\]
In particular, the empty subset contributes \(1\), and the sum of all \(2^r\) indexed weights equals \(\prod_i(1+Q_i-1)=n\).

## Proof
**Lemma (exact prefix criterion).** The integer \(n\) is unitary \(\varphi\)-practical if and only if
\[
Q_i\le M_{i-1}+2\qquad(1\le i\le r).
\]
For necessity, suppose the inequality fails at index \(i\). All weights indexed by subsets of the earlier components sum to \(M_{i-1}\). Every weight involving any later component is at least \(Q_i-1>M_{i-1}+1\), because the components are sorted and all other factors \(Q_j-1\) are positive integers. Therefore the integer \(M_{i-1}+1\), which is strictly between \(0\) and \(n\), cannot be represented.

For sufficiency, use induction on the number of components. Before adjoining \(Q_i\), assume the prior indexed weights represent all integers \(0,1,\ldots,M_{i-1}\). The new unitary weights are exactly \((Q_i-1)\) times an independently indexed copy of the old weights. Hence every integer in each interval
\[
[(Q_i-1)t,\ (Q_i-1)t+M_{i-1}],\qquad 0\le t\le M_{i-1},
\]
is representable. The intervals are consecutive or overlapping precisely when \(Q_i-1\le M_{i-1}+1\). Their union is the full interval \(0\) through \(M_{i-1}Q_i=M_i\). The empty prefix provides the base case. This proves the lemma.

Set \(G_0=1\) and \(G_i=G_{i-1}(G_{i-1}+2)\). The lemma gives \(M_i\le G_i\) by induction, because \(x(x+2)\) is strictly increasing for positive \(x\). Moreover,
\[
G_i=2^{2^i}-1,
\]
and equality \(M_i=G_i\) forces equality at every preceding stage and the components
\[
Q_j=G_{j-1}+2=2^{2^{j-1}}+1\quad(1\le j\le i).
\]
These are consecutive Fermat numbers. The first five, \(3,5,17,257,65537\), are distinct primes, so the bounds \(G_1,\ldots,G_5\) are each attained by a unique integer with that support size.

Now let \(\omega(n)=6\). If \(M_5<G_5=2^{32}-1\), integrality and the prefix criterion give
\[
 n=M_6\le M_5(M_5+2)\le (G_5-1)(G_5+1)=G_5^2-1<G_5(G_5+1).
\]
It remains to consider \(M_5=G_5\), which forces
\[
(Q_1,Q_2,Q_3,Q_4,Q_5)=(3,5,17,257,65537).
\]
The sixth prime-power component must satisfy
\[
Q_6\le G_5+2=2^{32}+1=641\cdot6700417.
\]
The two displayed factors are distinct primes; thus \(2^{32}+1\) is **not** a prime power, and an admissible \(Q_6\) cannot equal it. Consequently \(Q_6\le2^{32}\), and therefore
\[
n=G_5Q_6\le(2^{32}-1)2^{32}=N.
\]
Equality is attained with \(Q_6=2^{32}\), a power of the prime \(2\), larger than \(65537\) and with a prime base distinct from the preceding five. Every prefix inequality holds, so the lemma proves that \(N\) is unitary \(\varphi\)-practical. Strictness in both cases above proves uniqueness.

Finally \(G_6=2^{64}-1\) and \(G_6-N=2^{32}-1\). This completes the proof.

## Verification
Run \(\texttt{python3 verify.py}\) from the extracted files. The standalone standard-library checker independently reconstructs the five early Fermat primes, trial-divides both distinct factors of \(2^{32}+1\), checks the six prime-power components and the exact integer equalities, and compares the prefix criterion with explicit subset-sum bitsets in \(1252\) small prime-power configurations. It also checks \(15\) initial terms of OEIS A286906 using the same unitary-divisor convention. The expected output begins with \(\texttt{VERIFY_OK}\). Those finite checks support the exact constants and definitions; the universal maximum follows from the mathematical inequalities above, not finite extrapolation.

## Relationship to prior work
The unitary \(\varphi\)-practical condition appears explicitly in OEIS A286906 (first dated 15 May 2017), with its unitary-divisor definition, initial examples and a test. Schwab and Thompson's 2017 study of \(f\)-practical numbers treats values of arithmetic functions on **all ordinary divisors**; its discussion of the unitary totient is therefore distinct from the present restriction to *unitary divisors*. The cited materials provide motivating definitions and general subset-sum methods, not a maximum at exactly six prime supports.

The closest inspected published comparison on \(\varphi\)-practical degree multiplicities studies ordinary Euler-totient weights of all divisors on a two-prime-support family, and does not imply a six-prime-support extremum for unitary weights. The present sharp maximum is the first Fermat-number obstruction to attaining the natural greedy envelope.

## Limitations
This theorem determines the largest integer in the exact-six-prime-support class and establishes the first failure of the greedy upper envelope. It does not classify all such integers, nor determine the maximum for seven or more distinct prime factors. The exact prefix criterion itself is elementary; novelty is claimed for the sharp six-support extremum and its uniqueness, not for subset-sum interval methods or Fermat-number factorization. Searches cannot rule out an unindexed equivalent extremal statement; no independent mathematical audit is claimed.

## References
1. A. Eldar, “Unitary phi-practical numbers,” OEIS A286906, first dated 15 May 2017. https://oeis.org/A286906 .
2. N. Schwab and L. Thompson, “A generalization of the practical numbers,” arXiv:1701.08504v1, first public 30 January 2017. https://arxiv.org/abs/1701.08504 .
3. “Interior divisor degrees are never unique for two-prime φ-practical numbers,” public mathematical result (2026), for a comparison with the ordinary-divisor notion.

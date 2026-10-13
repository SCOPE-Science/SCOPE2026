# Fixed-order additive powers in generalized Thue–Morse words: a divisibility dichotomy

## Finding
For every integer \(q\ge2\), let \(s_q(n)\) be the base-\(q\) digit sum of the nonnegative integer \(n\). Define the generalized Thue–Morse word by \(t_q(n)=s_q(n)\bmod q\), interpreted as an integer in \(\{0,1,\ldots,q-1\}\). Fix an integer block order \(\ell\ge1\). An **additive \(k\)-power of order \(\ell\)** consists of \(k\) successive blocks, each containing \(\ell\) letters, all with the same integer sum (not a congruence modulo \(q\)).

**Theorem.** For every \(q\ge2\) and \(\ell\ge1\), the generalized Thue–Morse word contains additive \(k\)-powers of order \(\ell\) for arbitrarily large integers \(k\) if and only if \(q\mid\ell\). When \(q\nmid\ell\), there is an effective finite bound \(K(q,\ell)\) on the exponent of every such additive power, regardless of its starting position.

## Assumptions and scope
The alphabet is the ordered, integer-weighted alphabet \(\{0,1,\ldots,q-1\}\), with the usual integer sum. Both \(q\) and \(\ell\) are fixed when taking the supremum over starting positions and exponents. The statement does not assert a bound uniform as \(\ell\) varies. All positions are indexed from zero, and a factor starts at an arbitrary nonnegative integer.

## Proof
**1. Cyclic substitution and bounded prefix discrepancy.** The digit-sum identity gives
\[
t_q(qn+a)=(t_q(n)+a)\bmod q\quad(0\le a<q).
\]
Hence every aligned block of length \(q\) is a permutation of the entire alphabet. Put \(B=q(q-1)/2\), \(\mu=(q-1)/2\), and \(P(N)=\sum_{n=0}^{N-1}t_q(n)\). For \(N=qm+r\), \(0\le r<q\), define
\[
F_r(a)=\sum_{v=0}^{r-1}((a+v)\bmod q),\qquad F_0(a)=0.
\]
The exact identity
\[
P(qm+r)=mB+F_r(t_q(m))
\]
shows that \(D(N)=P(N)-\mu N=F_r(t_q(m))-\mu r\), with \(|D(N)|\le (q-1)^2/2\) for all \(N\). For every \(1\le r<q\), the function \(F_r\) is nonconstant: \(F_r(1)-F_r(0)=r\).

**2. Uniform digit-sum phases on arbitrary arithmetic progressions.** We prove a lemma independent of additive powers.

**Lemma.** Given \(q\ge2\) and \(h\ge1\), there exists \(L\ge1\) such that for every residue \(b\pmod h\) and every residue \(c\pmod q\), some integer \(r\) with \(0\le r<q^L\) satisfies \(r\equiv b\pmod h\) and \(s_q(r)\equiv c\pmod q\). Consequently there exists \(M(q,h)\) such that every progression \(t_q(m+sh)\), with arbitrary \(m\ge0\), displays every alphabet symbol among its first \(M(q,h)\) terms.

*Proof of lemma.* The sequence \(q^u\bmod h\) is eventually periodic. Choose \(p\ge2\) and sufficiently large exponents \(u_1<\cdots<u_{q-1}\), spaced so that the digit positions in different gadgets do not overlap, and such that \(q^{u_i+jp}\equiv q^{u_i}\pmod h\) for all integers \(j\ge0\). For each index \(i\), form
\[
H_i=\sum_{j=0}^{q-1}q^{u_i+jp},\qquad L_i=q^{u_i+1}.
\]
Both integers have the same residue modulo \(h\), because \(H_i\equiv q q^{u_i}\equiv L_i\pmod h\). Their base-\(q\) digit sums are respectively \(q\) and \(1\). Choose the exponents larger than the digit positions of all integers below \(h\), and make all the supports of the gadgets pairwise disjoint. Fix a residue \(b\pmod h\), and choose a low-digit seed \(z_b\in[0,h)\) such that \(z_b+\sum_i H_i\equiv b\pmod h\). Replacing precisely \(j\) of the \(q-1\) high gadgets \(H_i\) by \(L_i\) leaves the integer residue \(b\pmod h\) unchanged, while its digit sum modulo \(q\) increases by \(j\). The \(q\) choices \(j=0,1,\ldots,q-1\) therefore exhaust all digit-sum residues. Taking \(L\) large enough to contain all finitely many witnesses for all \(b\) proves the first assertion.

Now each aligned interval \([a q^L,(a+1)q^L)\) contains, for any fixed congruence class modulo \(h\), indices realizing all \(q\) values of \(t_q\), since \(t_q(aq^L+r)=(t_q(a)+s_q(r))\bmod q\). Every interval of \(2q^L\) consecutive indices contains an entire such aligned block. For any initial \(m\ge0\), this yields the stated uniform bound, for example \(M(q,h)=3+\lceil2q^L/h\rceil\), on the number of progression points required. This proves the lemma.

**3. Additive powers with orders divisible by the base.** If \(\ell\) is a multiple of \(q\), start at an aligned index \(i=0\). Every complete aligned length-\(q\) block has sum \(B\), so every consecutive block of length \(\ell\) has sum \(\ell\mu\). The entire infinite word, viewed in consecutive \(\ell\)-blocks starting at zero, is an additive power of every finite exponent.

**4. Excluding unbounded exponents at other orders.** Let \(q\nmid\ell\), and suppose an additive \(k\)-power of order \(\ell\) starts at position \(i\) with common block sum \(S\). At endpoints \(N_j=i+j\ell\) for \(0\le j\le k\),
\[
D(N_j)=D(i)+j(S-\mu\ell).
\]
The bound on \(D\) implies that if \(S\ne\mu\ell\), then \(k\) is uniformly bounded in terms of \(q\), because the nonzero half-integer \(S-\mu\ell\) has absolute value at least \(1/2\).

It remains to exclude an arbitrarily long power with \(S=\mu\ell\). Write \(g=\gcd(q,\ell)\) and \(p=q/g\ge2\). The residues \(i+j\ell\pmod q\) cycle over \(p\) distinct residues, at least one of which is a nonzero \(r\). Choose \(j_0\in\{0,\ldots,p-1\}\) for that residue. At the selected endpoints \(j=j_0+tp\), integer division gives
\[
N_j=q(m_0+t\ell/g)+r
\]
for a nonnegative \(m_0\), hence
\[
D(N_j)=F_r(t_q(m_0+t\ell/g))-\mu r.
\]
The lemma with \(h=\ell/g\) implies that, in a uniformly bounded number of such endpoints, the inner symbol takes every value, including \(0\) and \(1\). But \(F_r(1)-F_r(0)=r>0\), so \(D(N_j)\) cannot remain constant. This contradicts \(S=\mu\ell\) when \(k\) is large enough. Both cases provide an effective uniform exponent bound, and the theorem follows. \(\square\)

## Verification
The accompanying standalone `verify.py` checks the cyclic prefix identity against direct digit-sum generation, checks that each tested residue class modulo an arithmetic-step modulus contains every digit-sum phase, and compares sampled maximal additive exponents with the divisibility dichotomy. These are finite consistency checks; the all-base, all-order assertion rests on the symbolic modular-gadget lemma and bounded-discrepancy argument above. Run `python3 verify.py` from a directory containing this document's embedded checker.

## Relationship to prior work
Popoli, Shallit, and Stipulanti (arXiv:2410.02409v1, 2024) study additive complexity and powers; their Section 3.1.2 computes the additive complexity of the ternary generalized Thue–Morse word, while Section 5 studies orders of additive powers in the Tribonacci word and asks for further order classifications. The fixed-order unbounded-exponent spectrum in this theorem is a different invariant and is not stated there. Chen and Wen (arXiv:1809.06554) give exact abelian-complexity counts and Parikh-vector decompositions for the same generalized Thue–Morse family. Those formulas underlie its balanced substitution structure but do not themselves assert the fixed-order additive-power exclusion shown here. Blondin-Massé, Brlek, Glen, and Labbé (arXiv:0710.4031) study ordinary equality powers; ordinary powers impose stronger conditions than additive powers, and their critical-exponent statement does not supply this additive classification.

## Limitations
The effective upper bound supplied by the digit-gadget proof may be very large and is not asserted sharp. The result classifies which **fixed** block orders allow arbitrarily high additive exponents; it does not enumerate exact maximal exponents at the excluded orders. Prior-source comparisons are not a proof of priority: unindexed equivalent work may exist. The checks are finite and do not independently certify the infinite proof.

## References
1. P. Popoli, J. Shallit, and M. Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409v1 (first public 2024-10-03), https://arxiv.org/html/2410.02409v1.
2. J. Chen and Z.-X. Wen, *On the abelian complexity of generalized Thue-Morse sequences*, arXiv:1809.06554 (first public 2018-09-18), https://arxiv.org/html/1809.06554v2.
3. A. Blondin-Massé, S. Brlek, A. Glen, and S. Labbé, *On the critical exponent of generalized Thue-Morse words*, arXiv:0710.4031 (2007), https://arxiv.org/abs/0710.4031.

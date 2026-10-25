# Coprime adjacent-sum Hamiltonian cycles at every multiple of six

## Finding
For every positive integer \(k\), put \(n=6k\). There exists a permutation \((i_0,i_1,\ldots,i_n)\) of \(\{0,1,\ldots,n\}\) with \(i_0=0\) and \(i_n=n\) such that every one of the \(n+1\) cyclic adjacent sums
\[
i_0+i_1,\ i_1+i_2,\ldots,\ i_{n-1}+i_n,\ i_n+i_0
\]
is coprime to both \(n-1\) and \(n+1\). This proves Zhi-Wei Sun's adjacent-sum coprimality conjecture (Conjecture 3.9 in the cited article) throughout the infinite arithmetic progression \(n\equiv0\pmod6\). Explicit constructive formulas are supplied below.

## Assumptions and scope
All variables are integers. The theorem assumes \(n\ge6\) and \(6\mid n\). It establishes existence and gives a deterministic construction; it does not resolve the remaining even classes \(n\equiv2,4\pmod6\), nor the separate conjecture replacing \(n\pm1\) by \(2n\pm1\). The odd case was proved in the source paper.

## Proof
**1. Safe sums.** If \(6\mid n\), then each integer in
\[
\{n-5,n-3,n-2,n,n+2,n+3,n+5\}
\]
is coprime to \((n-1)(n+1)\). Indeed, \(n\pm1\) are odd and nonmultiples of three. For an offset \(d\in\{0,\pm2,\pm3,\pm5\}\), every common divisor of \(n+d\) and \(n\pm1\) divides \(d\mp1\), one of \(1,2,3,4,6\), or the unit in the case \(d=0\). No odd prime factor in this set can divide \(n\pm1\). This observation also applies to sums \(n\pm3\) used below.

**2. Auxiliary cyclic order.** Let \(m\ge10\). Construct a cyclic listing \(\pi=(\pi_0,\ldots,\pi_{m-1})\) of \(\{0,\ldots,m-1\}\), with \(\pi_0=0\), such that every consecutive absolute difference, including the wraparound difference, belongs to \(\{2,3\}\). The following explicit formulas prove existence (ranges proceed by steps of two, and empty ranges are omitted):

For \(m=2r\), \(r\ge5\), take
\[
(0,2,\ 5,7,\ldots,2r-5,\ 2r-2,2r-4,2r-1,2r-3,\ 2r-6,2r-8,\ldots,4,\ 1,3).
\]
For \(m=2r+1\), \(r\ge5\), take
\[
(0,2,\ 5,7,\ldots,2r-5,\ 2r-2,2r,2r-3,2r-1,\ 2r-4,2r-6,\ldots,4,\ 1,3).
\]
In both formulas, each integer in the required interval occurs once: the opening and closing portions cover the small values, the ascending odd part covers middle odd values, and the remaining four high values plus the descending even part cover the rest. Consecutive jumps are \(\pm2\) or \(\pm3\), including the last jump \(3\to0\).

For the two exceptional auxiliary sizes we shall need, the cycles
\[
(0,2,4,1,3,5)\quad(m=6),\qquad
(0,2,7,5,8,6,4,1,3)\quad(m=9)
\]
visit each index exactly once and have cyclic jump sizes in \(\{2,3,5\}\).

**3. Reflection lift.** Let \(n=2m\), where \(6\mid n\) and \(m\ge6\); thus \(3\mid m\). Use the auxiliary cycle in step 2 (with \(m=6,9\), or \(m\ge12\)). Form the list
\[
P=(0,\ n-\pi_1,\pi_1,\ n-\pi_2,\pi_2,\ldots,\ n-\pi_{m-1},\pi_{m-1},\ n).
\]
It visits every integer \(0,1,\ldots,n\) exactly once *except* \(m\): the \(\pi_j\) occupy \(0,\ldots,m-1\) and their reflections occupy \(m+1,\ldots,2m\). Adjacent sums of reflection-paired entries equal \(n\); sums at other edges equal \(n+\pi_j-\pi_{j+1}\), using \(\pi_m=\pi_0=0\). Their offsets belong to \(\{0,\pm2,\pm3,\pm5\}\), and therefore are coprime to \(n-1\) and \(n+1\) by step 1.

Since \(m-3\) appears in \(\pi\) and is different from \(\pi_0=0\), the list contains the adjacent pair \((n-(m-3),m-3)=(m+3,m-3)\), whose sum is \(n\). Replace this pair by the triple \((m+3,m,m-3)\). The two new sums are \(n+3\) and \(n-3\), both safe. This inserts the one omitted integer without changing either endpoint. The closing edge from \(n\) back to \(0\) has sum \(n\), also safe. Thus the required permutation exists for \(n=12,18\) and every multiple of six \(n\ge24\).

**4. Smallest case.** For \(n=6\), the explicit permutation \((0,4,2,1,3,5,6)\) has successive cyclic sums \((4,6,3,4,8,11,6)\), each coprime to \(5\) and \(7\). (The final closing sum is \(6\).) This completes the proof for every positive multiple of six. \(\square\)

## Verification
The included standard-library Python script `verify.py` implements precisely the auxiliary cycles, reflection lift, and exceptional case. It checks permutation completeness, prescribed endpoints, each cyclic adjacent-sum gcd, and, in the general range, the auxiliary cycle differences. Exact integer checks passed for the first \(1000\) multiples of six, up to \(n=6000\). A sample for \(n=24\) is
\[
(0,22,2,19,5,17,7,14,10,16,8,13,11,15,12,9,18,6,20,4,23,1,21,3,24).
\]
The infinite theorem follows from the explicit formulas and proof, not from finite tests.

## Relationship to prior work
Sun's Conjecture 3.9, documented in arXiv:1309.1679, requires these cyclic sums to be coprime to \(n-1\) and \(n+1\) for all positive \(n\notin\{2,4\}\). The paper proves the odd-\(n\) cases with different explicit permutations but does not establish the even cases considered here. OEIS A228886, first attributed to Sun on September 7, 2013, records the exact enumeration of suitable permutations, examples, and the general conjecture. Its finite table does not imply the present unbounded family or reflection construction. This theorem resolves all multiples of six, a previously untreated natural infinite congruence class, not the full conjecture.

## Limitations
The other even residue classes are not addressed. The construction establishes existence only, not enumeration or optimality of permutations. The bibliographic comparison covers identified primary sources and database records; an equivalent unindexed construction could exist. Independent mathematical validation is not asserted.

## References
1. Zhi-Wei Sun, *Some New Problems in Additive Combinatorics*, arXiv:1309.1679, Conjecture 3.9 and Remark 3.9, first preprint 2013; inspected version 9 (2020), pp. 11–12. https://arxiv.org/pdf/1309.1679
2. OEIS Foundation, A228886, *Number of permutations ... with all adjacent sums coprime to both \(n-1\) and \(n+1\)*, contributed by Zhi-Wei Sun, September 7, 2013. https://oeis.org/A228886
3. M. H. Bani Mostafa A. and E. Ghorbani, *Hamiltonicity of a coprime graph*, arXiv:2005.06308 (2020), studies edges given by gcd of vertex labels, rather than gcd of their sums with two varying moduli.

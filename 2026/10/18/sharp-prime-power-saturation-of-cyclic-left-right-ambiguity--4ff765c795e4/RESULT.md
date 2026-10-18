# Sharp prime-power saturation of cyclic left-right ambiguity

## Finding
Let \(n\ge 2\), and let \(x_1<\cdots<x_n\) be an ordered set. For a permutation \(\sigma\) consisting of one \(n\)-cycle, its **left-right orbit signature** is the binary table
\[
L_\sigma(i,t)=\mathbf 1_{\{\sigma^t(x_i)\le x_i\}},\qquad 1\le i\le n,\quad 0\le t<n.
\]
Write \(M(n)\) for the maximum number of distinct \(n\)-cycles with one and the same complete signature. Then
\[
\boxed{\displaystyle M(n)\le U(n):=\prod_{i=1}^{n-1}\gcd(n,i),}
\]
and equality holds **if and only if** \(n\) is a power of a single prime. More precisely, for each prime \(p\) and integer \(k\ge1\),
\[
\boxed{\displaystyle M(p^k)=p^{\frac{p^k-1}{p-1}-k}.}
\]
Thus \(M(8)=16\), \(M(9)=9\), \(M(16)=2048\), and \(M(25)=625\). For an integer with at least two distinct prime factors, the universal product bound is strict. The assertion concerns full time-indexed signatures on a *known ordered orbit*, not reconstruction solely from unlabeled periodic-orbit sets.

## Assumptions and scope
An \(n\)-cycle permutes all \(n\) labeled, increasingly ordered points transitively. The signature records, at every time \(t=0,\ldots,n-1\), whether the iterate of each point lies at or to its left. In particular the time-zero entry in every row is one. Equivalent choices of increasing real coordinates lead to the same combinatorial problem. Each different cyclic permutation of the ordered points is counted separately; choosing a different phase origin for the same permutation does not create a new object. The full signature includes intermediate iterate times, not merely an unordered orbit or a cycle's period.

## Proof
**1. Phase reconstruction and the universal bound.** Identify time with the cyclic group \(G=\mathbb Z/n\mathbb Z\). Every \(n\)-cycle has a unique phase sequence \(a_1,\ldots,a_n\) with \(a_1=0\), pairwise distinct \(a_i\in G\), and \(\sigma^{a_i}(x_1)=x_i\). Put \(S_i=\{a_1,\ldots,a_i\}\). Then
\[
L_\sigma(i,t)=\mathbf1_{\{a_i+t\in S_i\}}.
\]
For \(i\ge2\), replace the time-zero entry of the \(i\)-th row by zero, calling the resulting word \(B_i\). Since \(a_i\notin S_{i-1}\) and \(a_i+t\ne a_i\) for \(0<t<n\),
\[
B_i(t)=\mathbf1_{\{a_i+t\in S_{i-1}\}},\qquad 0\le t<n.
\]
Once phases \(a_1,\ldots,a_{i-1}\) have been chosen, the possible phases \(a_i\) are exactly the shifts matching the known indicator of \(S_{i-1}\) to the known row \(B_i\). If at least one shift exists, all such shifts form a coset of the translation stabilizer
\[
H(S_{i-1})=\{h\in G:S_{i-1}+h=S_{i-1}\}.
\]
Its order divides \(n\) and divides \(i-1\), because translation by this subgroup acts freely on \(G\) and decomposes \(S_{i-1}\) into whole cosets. Hence at most \(\gcd(n,i-1)\) choices can occur at this step. Multiplication over all \(n-1\) extensions, and the fact that each complete phase sequence determines exactly one \(n\)-cycle, gives the stated universal bound.

**2. Prime-power prefixes with maximal stabilizers.** Suppose \(n=p^k\). Express \(j\in\{0,\ldots,p^k-1\}\) with exactly \(k\) base-\(p\) digits (allowing leading zeroes), and let \(r(j)\) be the integer with those digits reversed. Choose the ordered phase sequence
\[
a_i=r(i-1),\qquad 1\le i\le p^k.
\]
For \(0\le r\le k\), let \(H_r\le G\) be the unique subgroup of order \(p^r\). The digit-reversal image of each aligned index block of \(p^r\) consecutive integers is a coset of \(H_r\): the varying last \(r\) source digits become the first \(r\) target digits. Consequently the prefix \(S_i\) is invariant under \(H_{v_p(i)}\), where \(v_p(i)\) is the largest \(r\) with \(p^r\mid i\). Since the order of any stabilizer of a set of size \(i\) divides \(i\), its stabilizer is **exactly** \(H_{v_p(i)}\).

**3. Every available stabilizer choice is realized simultaneously.** Consider any phase sequence whose prefix \(S_i\) is invariant under \(h\in G\). Add \(h\) to all phases of rank \(>i\), leaving the first \(i\) unchanged. The modified phases remain pairwise distinct because \(S_i+h=S_i\); they define another \(n\)-cycle. For each \(j>i\), its new prefix and its new individual phase are
\[
S_j'=S_i\cup\big((S_j\setminus S_i)+h\big),\qquad a_j'=a_j+h.
\]
Membership \(a_j'+t\in S_j'\) is equivalent to \(a_j+t\in S_j\), as \(S_i+h=S_i\); rows of rank \(\le i\) are unchanged. Thus the **entire** left-right signature is preserved.

Moreover, starting from the digit-reversal order, all later designated prefix stabilizers survive these suffix translations. Indeed, if \(j>i\), the subgroups \(H_{v_p(j)}\) and \(H_{v_p(i)}\) are nested. If the former is smaller, both \(S_i\) and \(S_j\setminus S_i\) are invariant under it, as is \(S_j'\). If it is larger, \(h\) belongs to it and translates each of \(S_i\) and \(S_j\) into itself, so \(S_j'=S_j\). The exact stabilizer order remains \(p^{v_p(j)}\), because it cannot exceed the largest power of \(p\) dividing \(j\).

Therefore, successively and independently, for every \(1\le i<n\) choose any \(h_i\in H_{v_p(i)}\) and translate the suffix of ranks \(>i\). All these choices preserve the same signature. They produce pairwise different phase sequences: the final phase at rank \(j\) is \(a_j+\sum_{i<j}h_i\), and successive phase differences recover each \(h_i\). There are precisely
\[
\prod_{i=1}^{p^k-1}|H_{v_p(i)}|
=p^{\sum_{i=1}^{p^k-1}v_p(i)}
=p^{\sum_{r=1}^{k}(p^{k-r}-1)}
=p^{\frac{p^k-1}{p-1}-k}
\]
such cycles, meeting the upper bound.

**4. Strictness for mixed-prime lengths.** Let distinct primes \(p<q\) divide \(n\). If any signature had exactly \(U(n)\) realizations, the reconstruction tree in step 1 would have the maximum allowed number of children at every node on every level: otherwise its number of leaves would be strictly smaller than the product of the levelwise upper bounds. In particular, on any realizing phase sequence, \(S_p\) would have a translation stabilizer of order \(p\), and \(S_q\) one of order \(q\). Both contain \(a_1=0\) and have exactly the corresponding number of points, so they would equal the unique subgroups \(K_p\) and \(K_q\) of orders \(p\) and \(q\) in \(G\). But \(S_p\subset S_q\) would force \(K_p\subset K_q\), impossible because \(p\nmid q\). Thus equality is impossible if \(n\) has two distinct prime divisors. Combined with steps 2 and 3, this proves the if-and-only-if statement.

## Verification
A standalone standard-library script `check_signatures.py` is supplied. It computes the digit-reversal construction, verifies all prefix stabilizers, reconstructs all cycles compatible with the resulting signature by an independently written row-shift search, and checks equality with the universal product for \(n\in\{4,8,9,16,25\}\). It separately enumerates all labeled cycles at \(n=4,6,8,9\) by cycle notation and groups them by signatures obtained through direct orbit iteration; a second enumeration via all phase orders independently checks \(n=9\). The exhaustive nine-point distribution is \(37584\) one-to-one signatures, \(864\) three-to-one signatures, and \(16\) nine-to-one signatures (a total of \(40320\) cyclic permutations). The script completed with `ALL_CHECKS_PASSED`. These finite checks test the algorithm and examples; the all-length claims are proved by the four steps above, not by enumeration.

## Relationship to prior work
Fuhrmann, Gröger and Passeggi, *Period spectrum and rigidity of interval maps* (arXiv:2610.07435v1, first publicly submitted 5 October 2026), prove that a prime-length ordered cycle is uniquely determined by its left-right behavior (Lemma 2.1) and observe that ambiguity exists for every composite length (Section 2, Figure 2). Those assertions neither determine the maximal ambiguity nor yield the arithmetic product bound, prime-power saturation, or strict mixed-prime obstruction proved here. The online note *Quadratic-time reconstruction of prime cycles from left-right orbit signatures* develops an efficient prime-case cyclic-shift reconstruction. Its phase matching is closely related to step 1 above, but it assumes prime length throughout and does not cover the maximal multiplicity for composite lengths. Archer and Elizalde's older work on periodic ordinal patterns of signed shifts counts different objects, not complete time-indexed left-right tables on all ordered cycles.

## Limitations
For mixed-prime \(n\), only the strict upper bound \(M(n)<U(n)\) is established in general, not an exact formula for \(M(n)\). The complete nine-point histogram is a finite checked corollary, not an all-length multiplicity distribution. No claim is made that every abstract binary table is realizable; the maximum ranges over realized signatures. The statement does not directly resolve rigidity of continuous interval maps from unordered periodic orbit sets, since recovering the comparison table from orbit sets is a separate question.

## References
1. G. Fuhrmann, M. Gröger, A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1 (5 October 2026), especially Lemma 2.1, Remark 2.4, and Section 2. https://arxiv.org/html/2610.07435v1
2. *Quadratic-time reconstruction of prime cycles from left-right orbit signatures*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-quadratic-time-reconstruction-of-prime-cycles-from-left-right-or--f270190d0cd7/RESULT.md
3. K. Archer, S. Elizalde, *Cyclic permutations realized by signed shifts*, arXiv:1304.7790 (29 April 2013). https://arxiv.org/abs/1304.7790

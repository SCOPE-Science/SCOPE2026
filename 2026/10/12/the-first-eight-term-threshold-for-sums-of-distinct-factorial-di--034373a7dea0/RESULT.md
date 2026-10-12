# The first eight-term threshold for sums of distinct factorial divisors

## Finding

For a practical positive integer \(N\), define
\[
h(N)=\min\left\{k\ge1:\text{every }1\le m\le N\text{ is a sum of at most }k\text{ distinct positive divisors of }N\right\}.
\]
The complete factorial profile through the first occurrence of eight terms is
\[
(h(1!),h(2!),\ldots,h(12!))=(1,1,2,3,4,5,5,6,7,7,7,8).
\]
In particular, \(n=12\) is the first factorial index for which \(h(n!)=8\).

For \(N=12!=479001600\), exactly \(175\) integers in \([1,N]\) require eight distinct divisors. The smallest and largest are, respectively,
\[
475785157\quad\text{and}\quad479001547.
\]
A constructive eight-term representation of the least exceptional integer is
\[
475785157=239500800+159667200+68428800+7983360+201600+3360+36+1.
\]
Every summand divides \(12!\).

## Assumptions and scope

All divisors are positive; each divisor can occur at most once. An integer \(m\) is counted as requiring \(k\) terms when its minimum-length distinct-divisor decomposition has length exactly \(k\). Factorial indices are the integers \(1\le n\le12\) only. The zero sum is included in the finite dynamic program as an empty subset, but not counted in the stated \(m\in[1,N]\) classification.

## Proof

Fix \(N=n!\), and order its \(t=\tau(N)\) divisors as \(d_1,\ldots,d_t\). For \(0\le i\le t\), let \(R_{i,j}\subseteq\{0,\ldots,N\}\) consist of sums of exactly \(j\) distinct divisors chosen from \(d_1,\ldots,d_i\), with sums exceeding \(N\) discarded. Initialize \(R_{0,0}=\{0\}\) and \(R_{0,j}=\varnothing\) for \(j>0\). Inclusion or omission of the last divisor proves the exact recurrence
\[
R_{i,j}=R_{i-1,j}\cup\bigl((d_i+R_{i-1,j-1})\cap[0,N]\bigr).
\]
The recurrence is an identity of sets, proved by splitting each admissible subset according to whether it contains \(d_i\). Hence its final union over \(0\le j\le k\) is exactly the set of integers representable by at most \(k\) distinct positive divisors of \(N\), not a statistical sample or heuristic approximation.

The accompanying verifier represents \(R_{i,j}\) as an arbitrary-precision bitset. If bit \(u\) is one precisely when \(u\in R_{i,j}\), the exact update is a Boolean union with a left shift by \(d_i\), masked to bits \(0,\ldots,N\). Updating \(j\) in descending order ensures that \(d_i\) cannot be reused. Two independent exact constructions of the divisor list, one by divisor pairs and one by prime-power products, agree for every tested factorial. A second permuted-order traversal independently reproduces the decisive \(12!\) exceptional bitset. Direct set-based subset-sum enumeration agrees for \(1\le n\le5\).

The exhaustive recurrence produces the following finite table. The final two columns count the integers whose minimum-length representation uses \(h(n!)\) terms and give the least such integer:

| \(n\) | \(n!\) | \(\tau(n!)\) | \(h(n!)\) | Count in maximal layer | Least in maximal layer |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 1 | 2 | 1 |
| 3 | 6 | 4 | 2 | 2 | 4 |
| 4 | 24 | 8 | 3 | 5 | 17 |
| 5 | 120 | 16 | 4 | 9 | 97 |
| 6 | 720 | 30 | 5 | 14 | 659 |
| 7 | 5040 | 60 | 5 | 343 | 3733 |
| 8 | 40320 | 96 | 6 | 306 | 33473 |
| 9 | 362880 | 160 | 7 | 1 | 362783 |
| 10 | 3628800 | 270 | 7 | 7150 | 2979161 |
| 11 | 39916800 | 540 | 7 | 272934 | 29749079 |
| 12 | 479001600 | 792 | 8 | 175 | 475785157 |

For each row, the check that all \(N+1\) bits are set at \(k=h(n!)\) proves the upper bound; a nonzero complement after \(k-1\) terms proves the matching lower bound. For \(12!\), that complement has exactly \(175\) one-bits, with smallest and largest set-bit indices \(475785157\) and \(479001547\). The accompanying 175-line artifact lists all these indices in increasing order. Thus all asserted exact numbers follow from an exhaustive, independently reproducible finite algorithm.

## Verification

Execute `python3 artifacts/verify.py` in the same directory as the embedded artifacts. It uses Python's standard library, arbitrary-precision integer arithmetic, and no external packages. The verifier constructs all factorials, both sets of positive divisors, exact bitset layers, the small-case set-enumeration check, and the permuted-order replication. It checks the complete table, the exact 175-element exception set, its endpoints, and the displayed eight-divisor witness. The included `artifacts/eight_term_layer.txt` contains the exact list, and `artifacts/replay.txt` records the replay output. The verifier checks the content of the list against the freshly computed bitset.

## Relationship to prior work

Hughes (2026) studies exactly \(h(n!)\), proving \(h(n!)\le(2\log2+o(1))n/\log n\) and recalling Erdős's question about its true growth; the paper gives no finite initial-value table or count of maximal-length integers. Tenenbaum and Yokota (1990, Lemma 4) establish an asymptotic representation-length bound using factorial divisors, not this exact finite profile. Yokota's earlier divisor-sum work addresses the same type of invariant; the accessible abstract does not give the present 12-factorial count, but its full text was not obtained and remains a residual literature-access risk. Exact-value, sequence, and published-finding corpus searches found no equivalent coverage of the threshold and its 175 exceptional integers. A published divisor-subset-sum classification restricted to \(2^{a}p^{b}\) does not apply to \(12!\), which has five distinct prime factors.

## Limitations

This is an exact finite result, not an asymptotic bound or an infinite structural classification. The finite recurrence requires significant memory at \(12!\), and no computation for larger factorials is claimed. The precise 175-element list is reproducible, but it is not characterized by a simple closed-form congruence rule. The full text of Yokota's 1992 paper and 1995 knapsack note was not independently accessed; searches and the accessible primary works supplied no implication covering the stated finite theorem.

## References

1. Scott D. Hughes, *Sums of distinct divisors of factorials*, arXiv:2609.10902v1 (2026-09-09), especially Sections 1 and 4. https://arxiv.org/html/2609.10902v1
2. Gérald Tenenbaum and Hisashi Yokota, *Length and Denominators of Egyptian Fractions, III*, Journal of Number Theory 35 (1990), 150–156, especially Lemma 4. https://tenenb.perso.math.cnrs.fr/PPP/Egyptian.pdf
3. Hisashi Yokota, *On a Sum of Divisors*, Canadian Mathematical Bulletin 35 (1992), 423–430, DOI 10.4153/CMB-1992-056-7 (abstract and citation record consulted; full text unavailable).
4. Hisashi Yokota, *On a Knapsack Problem involving Divisors of n!*, Research Bulletin of the Hiroshima Institute of Technology 29 (1995), 25–28 (citation/abstract record consulted; full text unavailable).

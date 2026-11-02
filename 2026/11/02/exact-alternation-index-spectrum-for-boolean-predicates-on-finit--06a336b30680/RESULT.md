# Exact alternation-index spectrum for Boolean predicates on finite weak orders

## Finding
Let \(P=A_1\oplus\cdots\oplus A_h\) be an ordinal sum of nonempty antichains, with \(|A_i|=n_i\ge1\). Write \(b_i=2^{n_i}-1\). For a Boolean predicate \(f:P\to\{0,1\}\), its **positive-start alternation index** \(a(f)\) is the maximum integer \(j\ge0\) for which there are \(x_1<\cdots<x_j\) with \(f(x_t)=1\) for odd \(t\) and \(f(x_t)=0\) for even \(t\). If no true point exists, the index is zero.

**Theorem (complete exact spectrum).** For every \(0\le j\le h\),
\[
|\{f:P\to\{0,1\}:a(f)=j\}|=e_j(b_1,\ldots,b_h)
=\sum_{1\le i_1<\cdots<i_j\le h}\prod_{t=1}^{j}(2^{n_{i_t}}-1),
\]
where \(e_0=1\). Thus for any integer \(k\ge0\), the number \(M_k(P)\) of predicates with no forbidden length-\(k+1\) increasing chain with the alternating pattern \(1,0,1,\ldots\) is
\[
M_k(P)=\sum_{j=0}^{\min(k,h)}e_j(b_1,\ldots,b_h).
\]
In particular, if all levels have size \(r\),
\[
M_k(P)=\sum_{j=0}^{\min(k,h)}\binom hj(2^r-1)^j.
\]
The complete spectrum depends only on the **multiset** of level sizes, not their order. This counting invariant therefore cannot recover the ordering of the levels. For instance, \((n_1,n_2,n_3)=(2,2,2)\) gives exact index counts \((1,9,27,27)\), hence \(M_1=10\), \(M_2=37\), and \(M_3=64\).

## Assumptions and scope
All posets, levels, and functions are finite. Every level is an antichain; any vertex in an earlier level is below every vertex in a later one, and two vertices in the same level are incomparable. A strictly increasing chain selects at most one point per level. The definition of \(k\)-monotonicity uses the **one-sided, positive-start** forbidden pattern from Grigorescu--Kumar--Wimmer: it is not the alternative convention that forbids either starting bit. The case \(h=0\) has exactly one predicate and \(e_0=1\). For \(k\ge h\), all \(2^{\sum_i n_i}\) predicates are allowed.

## Proof
Fix a predicate \(f\), and put \(B_i=\{f(x):x\in A_i\}\subseteq\{0,1\}\), a nonempty set. Let \(w=(1,0,1,0,\ldots)\) be the infinite alternating word. Let \(q_i\) be the maximum length of an initial segment of \(w\) realizable by a chain drawn from the first \(i\) levels. Start with \(q_0=0\). The ordinary greedy subsequence argument gives
\[
q_i=\begin{cases}
q_{i-1}+1,&w_{q_{i-1}+1}\in B_i,\\
q_{i-1},&w_{q_{i-1}+1}\notin B_i.
\end{cases}
\]
Indeed a chain can take at most one point at level \(i\). If the needed bit is present, append a point carrying it to a previously matched prefix; otherwise no longer prefix can be completed at that level. Hence \(q_h=a(f)\), and each increment identifies one distinct level.

Conversely, choose any set \(I\subseteq\{1,\ldots,h\}\) of increment levels. Scan the levels in increasing order, starting in greedy state zero. If \(i\notin I\), every vertex of \(A_i\) must carry the complement of the next required bit, leaving exactly one assignment. If \(i\in I\), the next required bit must appear at least once, leaving exactly \(2^{n_i}-1=b_i\) assignments. Each such assignment increments the greedy state exactly once. Thus a prescribed increment set \(I\) admits precisely \(\prod_{i\in I} b_i\) predicates, and no predicate belongs to two different increment sets. Summing over increment sets of size \(j\) proves the exact index formula; summing over sizes at most \(k\) proves the \(k\)-monotone count.

Since \(e_j\) is symmetric, changing the order of levels cannot change the spectrum. Replacing every \(b_i\) with \(2^r-1\) proves the uniform-level formula. Summing all elementary symmetric sums gives \(\prod_i(1+b_i)=2^{\sum_i n_i}\), which also checks the unrestricted boundary.

## Verification
A standalone standard-library Python program `verify_weak_order_monotone_counts.py` independently enumerates every Boolean coloring of each of 141 selected weak-order level-size profiles and explicitly searches their strictly increasing chains for alternating positive-start patterns. It compares the full index histogram with the elementary-symmetric expression. It examined 26,939 complete colorings, including empty profiles, mixed level sizes, lengths through six, and several level-order permutations. The output is recorded in `weak_order_verification_output.txt` and is reproducible with `python3 verify_weak_order_monotone_counts.py`. These finite tests corroborate, but do not replace, the unrestricted proof above.

## Relationship to prior work
Grigorescu, Kumar and Wimmer develop testing lower bounds for \(k\)-monotone Boolean functions over Boolean cubes and formally define the forbidden alternating pattern; their inspected 2018 open-access paper is about query complexity, not enumeration over arbitrary weak-order level-size vectors. Published investigations of finite weak-order mapping spaces count order-preserving maps; those classes differ from the nonmonotone predicate expansions allowed here whenever \(k\ge2\). Standard subsequence-automaton methods provide a related counting viewpoint but do not by themselves supply this explicit all-parameter symmetric level-size spectrum without the level-type analysis. No historical-uniqueness claim is made.

## Limitations
The formula requires all cross-level comparisons and within-level incomparability. It is not asserted for arbitrary graded posets, nor does it give testing complexity, VC dimension, Littlestone dimension, or a unique reconstruction of level order. Direct historical priority remains incompletely checked, especially the general literature on subsequence-avoidance automata and finite-model counting.

## References
1. E. Grigorescu, A. Kumar and K. Wimmer, *Flipping out with Many Flips: Hardness of Testing \(k\)-Monotonicity*, arXiv:1705.04205 (first posted May 11, 2017); APPROX/RANDOM 2018, DOI: 10.4230/LIPIcs.APPROX-RANDOM.2018.40.
2. C. L. Canonne, E. Grigorescu, S. Guo, A. Kumar and K. Wimmer, *Testing \(k\)-Monotonicity*, arXiv:1609.00265 (prior development of the forbidden-pattern framework).

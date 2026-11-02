# Two new sharp prime-root lengths for completely unclustered Burrows–Wheeler images

## Finding
For an ordered alphabet of size \(k\ge3\), let \(U_k(n)\) be the minimum number of *cyclic* equal-letter runs of any primitive length-\(n\) necklace whose Burrows–Wheeler transform (BWT) has \(n\) *ordinary* equal-letter runs (equivalently, adjacent BWT symbols are unequal). Then for every prime \(p\equiv5\pmod8\) such that \(2\) is a primitive root modulo \(p\),
\[
U_k(p+2)=U_k(p+3)=\frac{p+3}{2}.
\]
The construction uses only the ordered ternary subalphabet \(0<1<2\). Put \(r=(p-5)/2\), an integer divisible by four, and define the following BWT last columns:
\[
L_2=(10)^r1012021,\qquad L_3=(10)^r10120121.
\]
They have lengths \(p+2\) and \(p+3\), respectively, and each has precisely one cycle in its stable last-to-first permutation. Their inverse BWT necklaces attain the universal lower bound \(\lceil n/2\rceil\).

## Assumptions and scope
All words are over the ordered alphabet \(0<1<2\), embedded into any ordered alphabet containing at least three letters. The input necklace is primitive: its \(n\) cyclic rotations are distinct. The BWT is the last column of its lexicographically sorted cyclic rotations. A cyclic run boundary in the input includes the last-to-first comparison, while the maximal-BWT-run condition compares consecutive *linear* output positions only. For a last column \(L\), write \(F=\operatorname{sort}(L)\); the zero-based stable last-to-first permutation sends row \(i\) to the position occupied by \(L_i\) in the stable sort. The condition on \(2\) is its exact multiplicative order \(p-1\) modulo the prime \(p\). In particular, the theorem is a conditional family indexed by eligible primes, not a proof that there are infinitely many of them.

## Proof
**Step 1: stable permutation.** Set \(p=2r+5\). Both displayed last columns have alternating adjacent letters, including the junction between the alternating prefix and the suffix. The symbol multiplicities in \(L_2\) are \((r+2,r+3,2)\), and in \(L_3\) they are \((r+2,r+4,2)\), in the order \(0,1,2\). Let \(\pi_j\) be the stable last-to-first permutation of \(L_j\) for \(j\in\{2,3\}\). Directly counting preceding equal letters gives, for all \(0\le i\le p-3\),
\[
\pi_j(i)=f(i),\qquad f(i)=2^{-1}(i-1)\pmod p,
\]
where the residue is in \(\{0,\ldots,p-1\}\). This formula is a statement about the actual integer row positions, not merely an isomorphism of permutations.

The remaining arrows, after the untouched rows, are completely determined by the suffix. For \(L_2\), the route replacing the arrow out of row \(p-2\) is
\[
p-2\ \longrightarrow\ p\ \longrightarrow\ p+1\ \longrightarrow\ p-1\ \longrightarrow\ r+1.
\]
For \(L_3\), the replacement route is
\[
p-2\ \longrightarrow\ p+1\ \longrightarrow\ p+2\ \longrightarrow\ p\ \longrightarrow\ p-1\ \longrightarrow\ r+1.
\]
In both cases the old map satisfies \(f(p-2)=r+1\) and fixes \(p-1\). To see that \(f\) otherwise forms one cycle, use the coordinate \(y=i+1\pmod p\): under \(f\), this coordinate becomes \(y/2\pmod p\). Because \(2\) generates \((\mathbb Z/p\mathbb Z)^\times\), the \(p-1\) nonzero coordinates form a single cycle, while the zero coordinate (row \(p-1\)) is fixed. Each displayed replacement breaks the long cycle at exactly one edge, then inserts every new row and the formerly fixed row before returning to the old successor. Therefore each \(\pi_j\) consists of **one cycle of its full length**.

**Step 2: valid primitive BWT images.** A last column has a primitive single-necklace inverse under the cyclic BWT precisely when its stable last-to-first permutation is one cycle; following that cycle reconstructs the necklace. Thus the two last columns are BWTs of primitive necklaces. The construction is uniform in every eligible prime, and the alphabet stays ternary.

**Step 3: exact cyclic input runs.** By the standard BWT cyclic-run/Hamming identity (Kumallagov, Proposition 4.3), the cyclic input run count is \(d_H(L,F)\), the number of positions at which the last column differs from its stable sorted column. Since \(r\) is divisible by four, the number of matching positions within the successive sorted \(0\)-, \(1\)- and \(2\)-blocks is
\[
\begin{array}{c|ccc|c}
 &0\text{-block}&1\text{-block}&2\text{-block}&\text{total}\ 
L_2 & r/2+1&r/2+1&1&r+3\\
L_3 & r/2+1&r/2+2&1&r+4
\end{array}
\]
(the same formulas also hold when \(r=0\)). Subtracting these totals from the lengths \(2r+7\) and \(2r+8\) gives the common exact distance \(r+4=(p+3)/2\). In each case this equals \(\lceil n/2\rceil\). The universal lower bound \(U_k(n)\ge\lceil n/2\rceil\) (Kumallagov, Theorem 4.4) proves optimality and the two claimed equalities.

## Verification
The accompanying standalone Python program independently computes stable sorting, checks each arrow of both splice formulas, confirms that each permutation is a single cycle, verifies every sorted-block match count, and independently reconstructs a primitive cyclic word whose BWT is the prescribed last column. It also recomputes the cyclic run count directly from the reconstructed word. The program passed on 61 eligible primes up to \(2000\), checking both lengths for each; for all eligible primes up to \(181\) it additionally performed complete cyclic-rotation reconstruction. Representative new lengths beyond earlier small-length tables are \(103,104\) (from \(p=101\)) and \(151,152\) (from \(p=149\)). The exhaustive sample does not prove the infinite theorem; Steps 1–3 provide the proof.

## Relationship to prior work
Kumallagov (arXiv:2606.01267, first publicly posted 2026-05-31) introduced the minimum \(U_k(n)\), proved the universal lower bound and the BWT Hamming identity, and established sharpness for the two prime-root lengths \(p-1,p\). The present construction supplies the different lengths \(p+2,p+3\); neither an unclustered last column nor sharpness for \(p-1,p\) alone implies those new values. Fici, Gabory, Romana and Sciortino (arXiv:2508.20879; CPM 2026) proved that completely unclustered BWT images exist for every length and every alphabet size at least three, but their existence result does not minimize the cyclic run count of the original necklace. The earlier finite numerical findings for lengths at most \(64\) do not establish this uniform prime-root theorem, which includes arbitrarily large *eligible* primes if such primes exist. Thus this is a new structural splice construction relative to the inspected works, without a claim of proven priority against all possible unindexed literature.

## Limitations
The theorem is restricted to primes \(p\equiv5\pmod8\) with \(2\) a primitive root. It does not assert their infinitude, settle lengths \(p+1\), classify all optimal necklaces, or extend to binary alphabets. No claim of independent mathematical validation is made. Equivalent unindexed literature remains a priority risk.

## References
1. D. Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, arXiv:2606.01267v1 (2026-05-31), https://arxiv.org/abs/2606.01267.
2. G. Fici, E. Gabory, G. Romana, and M. Sciortino, *Unclustered BWTs of any Length over Non-Binary Alphabets*, arXiv:2508.20879v1 (2025-08-28), https://arxiv.org/abs/2508.20879; conference version *Totally Unclustered BWT Images of Any Length over Non-Binary Alphabets*, CPM 2026, https://doi.org/10.4230/LIPIcs.CPM.2026.13.

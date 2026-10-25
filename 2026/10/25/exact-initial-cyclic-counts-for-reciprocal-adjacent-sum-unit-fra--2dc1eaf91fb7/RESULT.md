# Exact initial cyclic counts for reciprocal adjacent-sum unit-fraction permutations

## Finding
For \(n\ge3\), let \(C_n\) be the number of dihedral orbits of circular arrangements of the distinct integers \(1,\ldots,n\) satisfying
\[
\sum_{i=1}^{n}\frac{1}{a_i+a_{i+1}}=1,\qquad a_{n+1}=a_1.
\]
The following finite classification is exact:

| \(n\) | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(C_n\) | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 6 | 38 | 79 | 224 |

At the first feasible size, \(n=8\), the **complete** list of two classes has the canonical representatives
\((1,3,5,4,6,2,7,8)\) and \((1,5,2,4,3,7,8,6)\).

## Assumptions and scope
All arrangement entries are pairwise distinct positive integers, exactly \(\{1,\ldots,n\}\). Two cycles are equivalent precisely if one is a rotation or reversal of the other. No identification by value relabeling is allowed. The result is a finite, exhaustive census, restricted to \(3\le n\le13\). It does not claim a formula or asymptotics for unrestricted \(n\).

## Proof
Put \(L_n=\operatorname{lcm}(3,4,\ldots,2n-1)\). Every adjacent sum of two distinct entries lies between \(3\) and \(2n-1\); hence \(L_n\) is divisible by every possible denominator. The displayed rational equality is **equivalent**, with no rounding, to the integer equality
\[
\sum_{i=1}^n\frac{L_n}{a_i+a_{i+1}}=L_n.
\]

Each dihedral orbit contains exactly one representative with \(a_1=1\) and \(a_2<a_n\). Indeed, there are \(n\) rotations placing \(1\) first, and reversal swaps the distinct second and last entries. Conversely any permutation of \(2,\ldots,n\) in the remaining positions with this strict inequality specifies exactly one orbit.

The complete depth-first search implemented in `verify_counts.c` starts with \(a_1=1\), recursively appends **each** unused integer from \(2\) through \(n\) **once**, and maintains the integer weight \(S=\sum_{i=1}^{d-1}L_n/(a_i+a_{i+1})\) for the current path. On reaching length \(n\), it increments the count if and only if \(a_2<a_n\) and \(S+L_n/(a_n+1)=L_n\). Since this is an exhaustive rooted permutation tree and the acceptance test is equivalent to the target identity, its count is exactly \(C_n\), not a sampled estimate.

All calculations are exact in unsigned 64-bit arithmetic: the largest \(L_n\) in the stated range is \(L_{13}=26771144400\), and every accumulated positive weight is bounded above by \(nL_n/3\), which is less than \(2^{64}\) for \(n\le13\). The recursion's bitmask supports all indices in the domain. The expected counts are asserted at runtime. Exact rational enumeration, independent of the LCM-weight criterion, confirms the complete \(n=8\) classification and \(C_9=5\).

## Verification
Compile `verify_counts.c` using `cc -O3 -std=c11 -Wall -Wextra -pedantic verify_counts.c -o verify_counts` and run `./verify_counts`. The program exhausts all rooted cycles up to \(n=13\), checks the displayed table, checks the denominator LCMs, and prints `VERIFY_OK`. Run `python3 crosscheck.py` for independent standard-library `fractions.Fraction` checks through the first nonzero cases, yielding `CROSSCHECK_OK`. The same exact enumeration method additionally reproduces OEIS A322070's **linear** (not circular) numbers through \(n=12\); those previously published numbers are a reproducibility calibration, not a new claim.

## Relationship to prior work
Ai, Hu, and Yan (arXiv:2610.18431, first public October 13, 2026) construct at least one solution for every circular \(n>7\); an existence proof does not determine the number of dihedral classes. The available portions of that manuscript describe constructions and tables of base cases, not this complete cyclic multiplicity census. OEIS A322070 records exact counts of **linear** permutations satisfying the unclosed adjacent-sum identity, so none of its recorded counts imply the circular entries above. OEIS A040018 treats circular arrangements with all adjacent sums **distinct** rather than with reciprocal sum one; its counts do not imply ours.

## Limitations
This is a finite complete classification, not a universal formula. For \(n\ge14\), the number of qualifying cycles is not determined here. The analogous linear counts are already publicly tabulated and are used only as verification. A broader previously published cyclic table not located by the documented comparisons remains a possible originality risk; the relevant recent manuscript could not be read in its entirety from the accessible text extraction. No independent mathematical audit has been performed.

## References
1. Jinggao Ai, Dingsheng Hu, Junmin Yan, *On Permutations Whose Adjacent-Sum Reciprocals Sum to One*, arXiv:2610.18431 (first submitted 2026-10-13), https://arxiv.org/abs/2610.18431 .
2. OEIS A322070, *Number of permutations f of {1,...,n} with f(1) < f(n) such that Sum 1/(f(k)+f(k+1)) = 1*, https://oeis.org/A322070 .
3. OEIS A040018, *Circular permutations with all adjacent sums distinct*, https://oeis.org/A040018 .
4. AMS Mathematics Subject Classification 2020, entry 11B75, *Other combinatorial number theory*, https://mathscinet.ams.org/msc/msc2020.html?t=11B75 .

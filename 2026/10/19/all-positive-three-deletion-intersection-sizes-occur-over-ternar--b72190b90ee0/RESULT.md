# All positive three-deletion intersection sizes occur over ternary alphabets

## Finding
Let \(\Sigma_q\) be an alphabet of \(q\geq 3\) symbols. For every integer \(m\) with \(1\leq m\leq 20\), there are equal-length words \(x\neq y\) over \(\Sigma_q\) for which their sets of distinct two-deletion descendants are disjoint, but their sets of common three-deletion descendants have cardinality exactly \(m\):
\[
D_2(x)\cap D_2(y)=\varnothing,\qquad |D_3(x)\cap D_3(y)|=m.
\]
No greater positive integer is possible under the disjointness hypothesis. Hence the set of \((q,3)\)-deletion-feasible positive integers is **exactly** \(\{1,2,\ldots,20\}\) for each \(q\ge3\).

The examples for all values other than \(18\) use only two symbols. In particular the value \(18\) has the length-nine ternary witness
\[
x=\texttt{100110210},\qquad y=\texttt{010101201}.
\]
As a separate finite boundary result, exhaustive enumeration of all unordered binary word pairs at every length \(3\le n\le13\) produces **no** disjoint-two-deletion pair with exactly \(18\) common three-deletion descendants. It does not rule out such binary pairs at longer lengths.

## Assumptions and scope
For a word \(w=w_1\cdots w_n\), define \(D_t(w)\) to be the **set**, with duplicates eliminated, of all length-\(n-t\) subsequences obtained by deleting exactly \(t\) positions; here \(0\le t\le n\). The two words in a witness have the same length \(n\ge3\). Feasibility uses the existential quantifier over finite lengths \(n\), with the alphabet fixed; only **positive** values \(m\) enter this definition. The result concerns deletion descendants, not insertion descendants or multiplicity-weighted observations. The finite binary search asserts only lengths through \(13\).

## Proof
**Universal upper bound.** Sun and Ge's Theorem 1.1 [1], specialized to \(s=t=3\), says that for all alphabets and all equal-length words with \(D_2(x)\cap D_2(y)=\varnothing\),
\[
|D_3(x)\cap D_3(y)|\le\binom{6}{3}=20.
\]
This is a previously published bound, not a new proof or new upper bound.

**Twenty explicit witnesses.** File `certificates/witnesses.tsv` lists one pair for every \(m=1,\ldots,20\), each at length at most \(11\). Columns give the desired intersection size, minimum alphabet needed by the displayed pair, length, and the two words. For each row, enumerate all \(\binom n2\) ways to delete two positions and all \(\binom n3\) ways to delete three positions, deduplicate outputs, and take set intersections. These exact finite sets have sizes \(0\) at radius two and precisely the displayed \(m\) at radius three. The independent implementation in `verification/verify_witnesses.py` checks every row by **retained-position combinations**, not by interpreting the target size as input to the deletion routine.

For the exceptional ternary pair, the complete common three-deletion set is

```
001010 001020 001021 001101 001120 001121
011010 011020 011021
100101 100120 100121
101010 101020 101021 101101 101120 101121
```

These are 18 distinct six-symbol words. The two-deletion intersection is empty. The explicit enumeration verifies each fact by finite, bounded sets, not by an unproved generalization from a sample. The binary pairs use symbols `0` and `1`, the exceptional pair uses `0`, `1`, `2`. Any injection of the used symbols into a larger alphabet preserves every relevant subsequence equality. Therefore all 20 positive values occur for every alphabet with at least three symbols. Combined with the universal bound, these are **all** positive feasible values.

**Finite binary exclusion.** The source `verification/verify_binary_census.cpp` independently enumerates every binary word of length \(3\le n\le13\), builds distinct two- and three-deletion descendant bitsets using deleted-position triples, and compares every **unordered pair of distinct words**. It applies no orbit reduction, pruning or probabilistic sampling. For all these lengths the count for radius-three intersection size \(18\), subject to radius-two disjointness, is zero. This proves the finite absence statement. Nothing here addresses the infinitely many longer binary lengths.

## Verification
Run `python3 verification/verify_witnesses.py` from any working directory (the script locates its own certificate by script path). Run `g++ -O3 -std=c++17 verification/verify_binary_census.cpp -o verify_binary_census && ./verify_binary_census`. The former tests all 20 witnesses using explicit subsequence sets, including an independently written list of the 18 ternary common descendants. The latter exhausts all \(2^n(2^n-1)/2\) unordered binary pairs for each \(3\le n\le13\), including all disallowed pairs before applying the separation test. Its last length yields every intersection count from \(0\) through \(20\) except \(18\). The binary calculation can be verified without trusting the finite certificates for the positive cases.

## Relationship to prior work
Sun and Ge [1] define \((q,s)\)-deletion feasibility (Definition 1.5) and conjecture that all positive values below \(\binom{2s}{s}\) are feasible. Their displayed examples address only \(s=1,2\), and their Theorem 1.1 proves the upper bound used here. Their Theorem 1.7 makes the existence of individual feasible seed values relevant to leading coefficients in run-constrained deletion-ball intersection problems. The present work resolves **the entire positive feasibility spectrum for \(s=3\) and \(q\ge3\)**, rather than merely reproving the known endpoint bound.

Zhang, Ge and Zhang [2] previously studied extremal pairs for which the three-deletion intersection has size \(19\) or \(20\) and the two-deletion intersection is empty. Those endpoint values and their general extremal characterization are **not** claimed as discoveries here. Wang, Li and Fu [3] examine larger-radius intersection extrema for fixed alphabets; such maximum results do not by themselves supply representatives for each intermediate cardinality. The central new finite construction here is the omitted interior spectrum, especially the ternary value \(18\).

## Limitations
The binary case \(q=2\) is not completely classified: positive values \(1\) through \(17\) and \(19,20\) are exhibited here, and the value \(18\) cannot occur at lengths at most \(13\), but occurrence at length \(14\) or above remains unproved either way. The theorem does not classify all witness pairs or optimize their lengths for \(q\ge3\). The proof of the universal upper bound is cited rather than independently reconstructed. An earlier unindexed realization of some interior values may exist; the conference full text of [2] was not available for a complete comparison.

## References
[1] Yubo Sun and Gennian Ge, *Extremal Deletion-Ball Intersections under Run-Count and Lower-Order Deletion-Ball Intersection Constraints*, arXiv:2606.25822, first posted June 24, 2026; especially Theorem 1.1, Definition 1.5, Theorem 1.7 and Section 6. https://arxiv.org/html/2606.25822v1

[2] Di Zhang, Gennian Ge and Yiwei Zhang, *Sequence Reconstruction over 3-Deletion Channels*, IEEE International Symposium on Information Theory (ISIT 2024), DOI:10.1109/ISIT57864.2024.10619639. An abstract-level comparison is possible; the full conference text was not examined.

[3] Wang, Li and Fu, *On Sequence Reconstruction Problem for q-ary Deletion Channels*, arXiv:2609.16837, first posted September 2026; related q-ary extremal deletion intersections. https://arxiv.org/abs/2609.16837

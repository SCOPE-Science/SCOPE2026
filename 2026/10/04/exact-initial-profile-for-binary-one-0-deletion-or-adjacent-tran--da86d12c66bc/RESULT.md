# Exact initial profile for binary one-\(0\)-deletion-or-adjacent-transposition codes
## Finding
For a binary word \(x\in\{0,1\}^n\), let \(B(x)\) contain \(x\), every word obtained by deleting one occurrence of \(0\), and every length-\(n\) word obtained by swapping one adjacent unequal pair. Define \(A_{0\mathrm D\lor\mathrm{AT}}(n)\) as the largest cardinality of a code \(C\subseteq\{0,1\}^n\) for which \(B(x)\cap B(y)=\varnothing\) whenever \(x\ne y\) are in \(C\). Then
\[
\bigl(A_{0\mathrm D\lor\mathrm{AT}}(1),\ldots,A_{0\mathrm D\lor\mathrm{AT}}(7)\bigr)=(2,3,4,7,11,17,30).
\]
Thus the exact optimum at length \(7\) is \(30\), and the displayed tuple is the complete initial profile through length \(7\).

## Assumptions and scope
The channel is the asymmetric setting in which the allowed error is either one \(0\)-deletion or one adjacent transposition; the error count is at most one, so the unchanged word is included in \(B(x)\). An adjacent transposition swaps \(01\) to \(10\) or \(10\) to \(01\). Deleting \(1\) is not allowed. The claim does not concern the different model in which a deletion and a transposition may both occur on the same transmitted word.

Only binary block lengths \(1\le n\le7\) are claimed. No extrapolation to larger lengths is made.

## Proof
For each \(n\), form a graph \(G_n\) whose vertices are all \(2^n\) binary length-\(n\) words. Distinct vertices \(x,y\) are adjacent exactly when \(B(x)\cap B(y)=\varnothing\). A set of codewords corrects the stated channel exactly when every pair of its vertices is adjacent, so
\[
A_{0\mathrm D\lor\mathrm{AT}}(n)=\omega(G_n).
\]

The accompanying verifier constructs every error ball twice: once with string slicing and once with tuple operations. It checks equality of the two constructions for every vertex. It then constructs \(G_n\) by direct ball-intersection tests.

For the lower bounds, `artifacts/optimal_codes.json` gives explicit codes of sizes \(2,3,4,7,11,17,30\). The verifier checks every listed word, checks the cardinalities, and directly verifies pairwise disjointness of their error balls. In particular, the length-\(7\) certificate contains \(30\) codewords.

For the upper bounds, `verify.py` runs an exact maximum-clique branch-and-bound search on each \(G_n\). At every recursive node, the remaining candidate subgraph is greedily colored into independent color classes. Any clique uses at most one vertex from each color class, so the number of colors is a rigorous upper bound on any extension of the current partial clique. A branch is pruned only when this bound cannot exceed the verified lower bound. All candidate vertices are otherwise branched on, so exhaustion proves that no larger clique exists. The resulting clique numbers are exactly \(2,3,4,7,11,17,30\).

## Verification
Run

```text
python3 verify.py
```

from the directory containing the package. The verifier reads only the included `artifacts/profile.csv` and `artifacts/optimal_codes.json`, reconstructs the channel from the definitions above, checks the explicit lower certificates, and proves matching upper bounds by exhaustive branch-and-bound. The recorded run in `artifacts/verification_output.txt` ends with

```text
VERIFY_OK profile=2,3,4,7,11,17,30
```

For length \(7\), the compatibility graph has \(128\) vertices and the exact search visits \(100221\) recursive nodes after the \(30\)-word lower certificate is established. These node counts are diagnostic only; correctness comes from the exhaustive branching and sound coloring bound, not from the counts themselves.

## Relationship to prior work
Wang, Vu, and Tan introduced the asymmetric setting with \(0\)-deletions and adjacent transpositions and gave a code correcting a single \(0\)-deletion or a single adjacent transposition with redundancy \(\log n+2\) bits in their 2022 IEEE Information Theory Workshop paper. Their expanded 2023 treatment gives constructions for asymmetric adjacent transpositions and deletions, including the same one-error alternative, but does not state the exact finite profile above.

Ye and Ge later derived asymptotic upper bounds for code sizes under related Damerau--Levenshtein models and showed that the Wang--Vu--Tan construction has asymptotically optimal redundancy up to an additive constant. Their results are asymptotic and do not determine the exact values at lengths \(1\) through \(7\).

Targeted searches under the exact channel description, the asymmetric Damerau--Levenshtein terminology, the sequence \(2,3,4,7,11,17,30\), and the length-\(7\) value \(30\) found no inspected source stating or implying this finite profile. The closest indexed exact small-parameter coding result located in the checked repository concerns a different quinary deletion-only channel.

## Limitations
The result is finite: it gives no formula or bound for \(n\ge8\). It addresses an either/or error channel, not simultaneous occurrence of one \(0\)-deletion and one transposition. The verification is exact for the stated finite domains, but it is software-assisted; the source code and explicit witnesses are included so the computation can be replayed. A residual originality risk remains that an unindexed finite table or unpublished computation could contain some or all of the same small values.

## References
1. Shuche Wang, Van Khu Vu, Vincent Y. F. Tan, “Codes for the Asymmetric Damerau–Levenshtein Distance,” 2022 IEEE Information Theory Workshop, DOI `10.1109/ITW54588.2022.9965921`.
2. Shuche Wang, Van Khu Vu, Vincent Y. F. Tan, “Codes for Correcting Asymmetric Adjacent Transpositions and Deletions,” arXiv:`2301.11680`.
3. Zuo Ye, Gennian Ge, “On the Maximum Size of Codes Under the Damerau-Levenshtein Metric,” arXiv:`2507.04806`.

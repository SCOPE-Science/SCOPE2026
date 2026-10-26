# The exact ternary finite synchronization frontier at parameter \(9/10\)

## Finding

Let \(\Sigma=\{0,1,2\}\), and define an \(\varepsilon\)-synchronization word \(w\) by requiring, for every \(0\le i<j<k\le |w|\), that the insertion-and-deletion edit distance satisfy
\[
\operatorname{ED}(w[i:j],w[j:k])>(1-\varepsilon)(k-i).
\]
At the fixed parameter \(\varepsilon=9/10\), **the greatest possible ternary word length is exactly \(32\)**. Up to arbitrary permutations of the three letters there are **exactly ten** maximizing words, displayed below. Consequently, there are exactly \(60\) labeled maximum-length words. The length-\(32\) classification and the sharp length-\(33\) obstruction are both exact, not statistical estimates.

```
01020120212012101201020120212012
01021012102120210201021012102120
01021201210120102012021201210120
01201020120212012101201020120210
01201020120212012101201020120212
01202102010210121021202102010210
01202120121012010201202120121012
01202120121012010201202120121020
01210120102012021201210120102012
01210212021020102101210212021020
```

## Assumptions and scope

All words are finite, over an alphabet of at most three symbols. Indices in the definition are zero-based, intervals half-open, and both consecutive intervals must be nonempty. Edit distance allows insertions and deletions only (not substitutions). The strict inequality is important, including when its right-hand side is integral. Alphabet permutations are the only symmetry quotient used; reversal is not identified. This result concerns the exact finite regime at \(\varepsilon=9/10\), not the optimal parameter for infinite ternary synchronization words.

## Proof

For strings \(a,b\), the insertion/deletion identity
\[
\operatorname{ED}(a,b)=|a|+|b|-2\operatorname{LCS}(a,b)
\]
shows that the defining inequality at \(\varepsilon=9/10\) is exactly
\[
20\operatorname{LCS}(w[i:j],w[j:k])<9(k-i).
\]
These are integer comparisons, without numerical approximation.

Every nonempty word is uniquely equivalent, under alphabet renaming, to a **restricted-growth word** starting in \(0\), in which each next symbol belongs to \(\{0,\ldots,\min(2,1+\max\text{(previous symbols)})\}\). Indeed, map its first previously unseen letter to \(0\), the next to \(1\), and the next to \(2\). Every alphabet-renaming orbit has exactly one representative satisfying this rule. The LCS predicate is invariant under bijective letter renaming.

Let \(F_n\) consist of valid restricted-growth words of length \(n\). It follows from prefix heredity and the preceding normalization that \(F_1=\{0\}\), and \(F_{n+1}\) comprises precisely those restricted-growth extensions \(wa\) of members \(w\in F_n\) for which
\[
20\operatorname{LCS}((wa)[i:j],(wa)[j:n+1])<9(n+1-i)
\quad(0\le i<j<n+1).
\]
All comparisons with right endpoint at most \(n\) were already satisfied by \(w\); those with right endpoint \(n+1\) are exactly the newly required constraints. Induction proves that this recurrence neither omits nor adds any valid orbit representative.

The complete recurrence is executed using exact integer dynamic programming in the accompanying standalone `verify.py`. Its exhaustive level cardinalities \((|F_1|,\ldots,|F_{33}|)\) are

```
1, 1, 2, 3, 5, 7, 10, 13, 18, 24, 27, 33, 36, 41, 39, 40, 44, 50, 57, 46, 50, 34, 30, 29, 27, 26, 26, 13, 11, 12, 11, 10, 0
```

The ten members of \(F_{32}\) are precisely the ten words printed in the Finding, and \(F_{33}=\varnothing\). All ten use all three symbols, so each has an alphabet-permutation orbit of cardinality \(3!=6\). Prefix heredity rules out all greater lengths once \(F_{33}\) is empty. Hence the greatest length is \(32\) and the labeled maximum-word count is \(10\cdot 6=60\).

This is a finite exhaustive proof with a supplied, inspectable implementation of the exact recurrence. The mathematical completeness of the enumeration follows from the proved recurrence and normalization; the cardinality evaluation is performed by the supplied code, not inferred from sample data.

## Verification

Run `python3 verify.py` from a directory containing that file. It enumerates all restricted-growth prefixes through length \(33\), prints the complete ten-word set at length \(32\), and asserts the entire level-cardinality array and the absence of length-\(33\) words. LCS uses a standard integer dynamic program. A separate insertion/deletion distance dynamic program checks **54,560** interval triples on the ten maximizing words, independently of the LCS recurrence, and also checks all \(3^8\) labeled length-\(8\) words; exactly \(78\) qualify. Recorded program output is in `checks.txt`. The exact proof is specifically the exhaustive recurrence, not extrapolation from the auxiliary cross-checks.

## Relationship to prior work

Xu, Fu, Qiao, and Tao (September 2026) establish existence of ternary synchronization strings of **arbitrary length** for parameters sufficiently close to \(1\); their main focus is an infinite-length constructive regime. Cheng, Haeupler, Li, Shahrasbi, and Wu (2018), Appendix A, already give a **stronger asymptotic obstruction**: the ternary infinite-word critical parameter is at least \(12/13\). Consequently, the weaker deduction that ternary \(9/10\)-synchronization words cannot be arbitrarily long is **not claimed as new**. Their paper does not report the exact length-\(32\) frontier or the ten maximizing classes at this parameter. Camungol and Rampersad study related LCS avoidance for *equal-length* adjacent halves and do not supply an enumeration for all possible splits of finite ternary words. A related earlier exact finite result at \(\varepsilon=7/8\) determines a different, stricter parameter and does not determine this frontier or its maximizing words.

## Limitations

The result does not improve the known lower bound \(12/13\) for the critical infinite ternary synchronization parameter. It neither addresses four-symbol words nor parameter values other than \(9/10\). Its new content is an exact finite optimum and complete extremizer enumeration at a natural fixed edit-distance threshold. The computation is exhaustive up to the obstruction depth and does not establish an independent theorem about arbitrary infinite synchronization words. An equivalent finite-length census may exist outside the examined searchable literature.

## References

1. H. Xu, S. Fu, Y. Qiao, D. Tao, *Synchronization Strings over the Optimal Alphabet*, arXiv:2609.04122v1 (first public September 3, 2026), Sections 1 and Appendix D/E. https://arxiv.org/abs/2609.04122
2. K. Cheng, B. Haeupler, X. Li, A. Shahrasbi, K. Wu, *Synchronization Strings: Efficient and Fast Deterministic Constructions over Small Alphabets*, arXiv:1803.03530v1 (2018), Definition 2.4, Section 6, Appendix A Table 1. https://arxiv.org/abs/1803.03530
3. S. Camungol, N. Rampersad, *Avoiding approximate repetitions with respect to the longest common subsequence distance*, arXiv:1308.1620v1 (2013), Sections 2–3. https://arxiv.org/abs/1308.1620

# Sharp constituent-square threshold for nine overlap-free binary squares

## Finding
Let \(u_1,\ldots,u_9\) be nonempty binary words and let \(w=u_1u_1\cdots u_9u_9\). Suppose \(w\) is **overlap-free**, meaning that none of its contiguous factors has the form \(axaxa\), with \(a\) a single symbol and \(x\) any binary word, possibly empty. Then
\[
\max_{1\le i\le9}|u_i|\ge6.
\]
The inequality is sharp. There are **exactly two** binary words admitting such a nine-square factorization with \(\max_i|u_i|\le6\):

```
001001101001011010011001011001101001011010011011
110110010110100101100110100110010110100101100100
```

Each has exactly one such ordered nine-square factorization. The two words are complements and reversals of one another, and the unique ordered list of square-root lengths is \((3,2,2,2,6,2,2,2,3)\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); a square is \(uu\) for a nonempty word \(u\). The nine constituent squares are contiguous and occupy the entire word; their roots can vary. Overlaps include the three-letter cube \(aaa\) (when \(x\) is empty). The result concerns the minimum possible **maximum constituent root length**, not just the minimum total word length. There is no a priori restriction on total length.

## Proof
Define \(S_R=\{uu: u\in\{0,1\}^{+},\ |u|\le R,\ uu\text{ is overlap-free}\}\). For each \(R\in\{1,2,3,4,5,6\}\), set \(F_R(0)=\{(\varepsilon,())\}\) and define the finite recursion
\[
F_R(k+1)=\{(vs,(r_1,\ldots,r_k,|s|/2)):\ (v,(r_1,\ldots,r_k))\in F_R(k),\ s\in S_R,\ vs\text{ is overlap-free}\}.
\]
Here the second coordinate records the lengths of all constituent roots, so different factorizations are not silently identified. By induction on \(k\), the set \(F_R(k)\) lists **every** overlap-free concatenation of exactly \(k\) binary squares whose constituent roots have lengths at most \(R\), and lists no others. The induction is direct: delete the last square from a product, or append each allowable square to every shorter product and reject precisely those creating an overlap.

The source file `checker.py` computes \(S_R\) by testing all \(2^r\) binary roots of each length \(1\le r\le R\), then evaluates this recursion with exhaustive, integer-only string comparisons. The actual certified cardinalities, including factorization multiplicity, are:

| Root cap \(R\) | Eligible square blocks | Ordered-product counts at depths zero through nine |
|:--:|--:|:--|
| 1 | 2 | \((1,2,2,2,2,0,0,0,0,0)\) |
| 2 | 4 | \((1,4,4,4,4,0,0,0,0,0)\) |
| 3 | 10 | \((1,10,14,16,22,10,8,8,8,0)\) |
| 4 | 14 | \((1,14,20,24,30,12,8,8,8,0)\) |
| 5 | 14 | \((1,14,20,24,30,12,8,8,8,0)\) |
| 6 | 26 | \((1,26,30,40,56,34,24,26,28,2)\) |

Thus \(F_5(9)\) is empty. Every nine-square overlap-free product must consequently contain a root of length at least \(6\). The last line gives exactly two decompositions at cap \(6\), which the reproducible enumeration identifies as the two displayed words, with the displayed common root-length vector. Since these decompositions have different resulting binary words, the words and the factorizations are both uniquely classified at the threshold. This proves both sharpness and rigidity.

The check is **finite and globally exhaustive** for this claim: at root cap \(R\), any nine-square product has at most \(18R\) symbols. Thus the cap-6 search covers every possible candidate of length at most \(108\), with no unstated length truncation. A separate method enumerates all overlap-free binary prefixes through length \(18R\) and stores a bitmask of achievable square counts using a suffix-square recurrence. Every root cap produces exactly the same final words as the square-block method. The two methods test overlaps differently: one checks every start and period in each completed word, the other checks only new suffix overlaps under one-letter extension.

## Verification
Run `python3 checker.py` with Python 3.9 or later, without dependencies. It prints each root-cap count and both witnesses, and ends with `ALL CHECKS PASSED`. The saved exact output is `checker_output.txt`. For the cap-6 search, the number of eligible square blocks is \(26\) and the nine-square layer contains \(2\) factorizations; for cap \(5\) the corresponding layer is empty. Both independent enumerations agree for all six root caps. The claimed theorem is not inferred from a finite sample of an infinite family: the bounded-root hypothesis implies the proved absolute length bound \(108\).

## Relationship to prior work
Shallit, *Ten Squares Force an Overlap* (2026), proves that ten binary squares cannot be concatenated without producing an overlap and exhibits the same length-\(48\) nine-square example. His Lemma 7 enumerates products from a four-block set and Theorem 8 controls the number of squares plus extendability. Neither statement gives an upper bound on the length of every constituent square or classifies every nine-square product with root lengths at most six. The present claim gives the complementary **sharp local root-length obstruction**, rather than a new upper bound on the number of squares or another shortest-total-length result. The restriction to roots at most six permits total lengths up to \(108\), so a shortest-total-length classification alone does not supply this result.

## Limitations
The classification applies only when each square root has length at most \(6\). It does not classify all unrestricted nine-square concatenations, nor claim a new asymptotic bound. The finite proof relies on a fully specified exhaustive recurrence and two replayable implementations; independent scientific validation and historical-priority certification have not been performed.

## References
- Jeffrey Shallit, *Ten Squares Force an Overlap*, arXiv:2605.28570 (first publicly submitted 2026-05-27; version 2, 2026-08-15), Sections 2–3. https://arxiv.org/html/2605.28570v2
- Tero Harju, *A Note on Squares in Binary Words*, International Journal of Foundations of Computer Science 34 (2023), DOI:10.1142/S0129054123480052. This analyzes counts of square centers, a different invariant.

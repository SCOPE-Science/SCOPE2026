# First circular prefix-normal obstructions and the complete three-one classification

## Finding

For a binary circular word \(W\) of length \(n\), let \(M_W(\ell)\) be the maximum number of symbols \(1\) in any circular factor of length \(\ell\), where \(1\leq\ell\leq n\). A *prefix-maximal root* is a starting position \(s\) such that the length-\(\ell\) prefix of the linearization starting at \(s\) contains exactly \(M_W(\ell)\) ones for every \(\ell\). Different starting positions are counted separately, even if a circular word is periodic.

**Theorem.** Suppose \(W\) has exactly three ones. Read those ones cyclically as \(p_0,p_1,p_2\) and let \(g_i\) be the number of zeros immediately after \(p_i\) and before \(p_{i+1}\), with indices modulo three. Then the prefix-maximal root positions are exactly
\[
\{p_i:g_i=\min_j g_j\ \text{and}\ g_{i-1}=\max_j g_j\}.
\]
Thus the number of such positions is \(3\) if all gaps coincide, \(1\) if exactly two gap values occur, and either \(0\) or \(1\) if all three values are distinct. In the last case there is **no** prefix-maximal root precisely when, in the cyclic sequence of gaps, the largest gap is not immediately followed by the smallest gap.

Let \(B_n\) count binary necklaces of length \(n\) and Hamming weight three having no prefix-maximal root. Then
\[
\sum_{n\geq3}B_nz^n=\frac{z^6}{(1-z)(1-z^2)(1-z^3)},
\qquad
B_n=\#\{(a,b,c)\in\mathbb Z_{\geq0}^3:a<b<c,\ a+b+c=n-3\}.
\]
Consequently the shortest binary circular word with no prefix-maximal root has length \(6\), and its unique necklace is represented by `001011`. Such necklaces exist at every length \(n\geq6\); the explicit family `11` followed by \(n-4\) zeros and then `10` is obstructed. Every binary circle of length less than six has a prefix-maximal root. Among length-\(n\) necklaces of weight three, the proportion without such a root tends to \(1/2\) as \(n\to\infty\).

## Assumptions and scope

A *circular factor* may wrap across the linear boundary; factors have lengths between \(1\) and the full circle length \(n\). All circles are binary and nonempty. A *necklace* is an equivalence class under cyclic rotation alone, not reversal or complementation. Root positions are positions in a labeled circular representative. A *gap* counts zeros, so \(g_0+g_1+g_2=n-3\), and \(g_i\) may be zero. The theorem applies to all \(n\geq3\), including periodic words.

The statement is stronger than the usual *linear* prefix-normal condition: the prefix at each length must dominate factors that cross the chosen cut. It does not merely ask whether one rotation is prefix normal with respect to non-wrapping factors.

## Proof

**Lemma 1 (windows can start at a one).** If \(W\) contains a one, then for each \(\ell\) between \(1\) and \(n\), some circular factor attaining \(M_W(\ell)\) begins with a one. Indeed, take any optimal length-\(\ell\) factor. If its first symbol is zero, move the start to the first one within the factor, dropping only leading zeros and appending the same number of symbols at the other end. This never decreases its one-count. Such a one exists because the optimal count is at least one for all \(1\leq\ell\leq n\). This also works for \(\ell=n\).

**Lemma 2 (threshold dominance).** In a circle with exactly three ones, a root beginning at \(p_i\) sees its second one in position
\[
D_{2,i}=g_i+2
\]
and its third one in position
\[
D_{3,i}=g_i+g_{i+1}+3=n-g_{i-1}.
\]
Here positions within a rooted word are counted from one. Its number of ones in the prefix of length \(\ell\) is
\[
1+\mathbf1_{\ell\geq D_{2,i}}+\mathbf1_{\ell\geq D_{3,i}}.
\]
By Lemma 1 the maximal circular window count is the maximum of these three step functions. One of them equals that maximum at **every** length exactly when its second-one threshold is the smallest of the three second-one thresholds and its third-one threshold is the smallest of the three third-one thresholds. Necessity follows by testing the smallest second and third thresholds separately. For sufficiency, both indicator summands of the chosen root dominate the corresponding indicator summands of every other root at every length.

Because the first threshold is minimized when \(g_i\) is smallest and the second when \(g_{i-1}\) is largest, Lemma 2 proves the asserted exact root-position formula. If all three gaps are equal, all three positions qualify. If precisely two gap values occur, exactly one minimum has a maximum immediately before it. If all three are distinct, the unique minimum follows the unique maximum in exactly one of the two possible cyclic orders; those are respectively the admissible and inadmissible orders.

**Counting the failures.** Rotating a weight-three circular binary word rotates its ordered gap triple. Conversely, every cyclic triple of nonnegative gaps reconstructs a unique weight-three necklace. For each distinct sorted triple \(0\leq a<b<c\) with \(a+b+c=n-3\), there are exactly two cyclic orderings, interchanged by reversal; the root criterion admits one and rejects the other. Triples with repeated entries never fail. Thus the number of failing necklaces is exactly the number of distinct sorted nonnegative triples. Writing
\[
a=t,\qquad b=t+1+u,\qquad c=t+2+u+v,
\]
with \(t,u,v\geq0\), gives \(n=6+3t+2u+v\), proving the generating function. The smallest possible length is \(6\); its sole failing gap-necklace gives `001011`. Taking \((t,u,v)=(0,0,n-6)\) yields a failure at each larger length. In that case the bad orientation has gap triple \((0,n-4,1)\), represented by `11` followed by \(n-4\) zeros and `10`.

**No shorter counterexample of any weight.** Any binary circle with at most two ones has a prefix-maximal root: if it has two ones, root at the one followed by the shorter zero gap, attaining the earliest possible second one; the cases of zero or one one are immediate. Any circle with at most two zeros also has such a root: with two zeros, root immediately after the zero preceding a longest all-one run of length \(r\). Prefixes through length \(r\) contain zero zeros, prefixes of lengths \(r+1,\ldots,n-1\) contain one zero and no circular factor of those lengths can contain zero zeros, and the full-length prefix has the unavoidable two zeros. The zero- and one-zero cases are immediate. Every binary circle of length at most five has at most two ones or at most two zeros, so none fails.

**Asymptotic proportion.** The generating function has a third-order pole at \(z=1\), with leading singular term \(1/(6(1-z)^3)\); its other poles are of lower order. Hence \(B_n=n^2/12+O(n)\). Every weight-three necklace is primitive except for the single equally spaced necklace when \(3\mid n\). Consequently, the total number of weight-three necklaces is
\[
T_n=\frac{(n-1)(n-2)}6+\frac23\mathbf1_{3\mid n}
=\frac{n^2}{6}+O(n).
\]
Therefore \(B_n/T_n\to1/2\).

## Verification

The standalone `check_cyclic_prefix_normal.py` uses literal circular-window one-counts, independently of the gap criterion. It checks every binary word of length at most \(11\) for the first failing necklace, and every weight-three word for lengths \(3\) through \(41\) against both the gap criterion and the generating-function coefficient. It prints `VERIFY_OK` if every test agrees. Run `python3 check_cyclic_prefix_normal.py` using Python 3 and no additional packages. The theorem and the generating function are proved for unbounded lengths; finite tests are only sanity checks.

As a direct short witness, `001011` has one-rooted rotations `101100`, `110010`, and `100101`. The first and third fail at length \(2\), because `11` is a circular factor. The middle fails at length \(4\): its prefix `1100` has two ones, while `1011` is a circular factor with three.

## Relationship to prior work

Prefix-normal words and their relation to jumbled matching were introduced by Fici and Lipták and studied algorithmically by Burcsi, Fici, Lipták, Ruskey, and Sawada. Their prefix-normal form permits a newly constructed linear word with the same maximal substring Parikh counts. The present question instead restricts the realization to a *rotation of the original circle*, and allows crossing circular factors. In particular, `110010` occurs in the published list of ordinary prefix-normal words of length six, but its necklace does not have a prefix-maximal root in the stronger circular sense.

The fixed-density gap inequalities in the 2014 literature are the closest structural precursor; the circular threshold comparison here gives an orientation-sensitive all-length classification and an exact necklace-generating function. No priority claim is made for the general prefix-normal framework or its gap method. A limited literature comparison did not locate a previous statement of this exact cyclic weight-three classification; independent historical-priority verification remains open.

## Limitations

The classification and rational generating function concern weight exactly three. The proof that words with at most two zeros or at most two ones always have a root does not classify larger weights. An asymptotic half of the weight-three necklaces fail, but this is not a statement about random binary necklaces with unrestricted weight. No independent audit is claimed.

## References

- G. Fici and Z. Lipták, *On Prefix Normal Words*, Developments in Language Theory (2011), pp. 228–238. DOI: https://doi.org/10.1007/978-3-642-22321-1_20. Author manuscript: https://arxiv.org/abs/1805.12405.
- P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, and J. Sawada, *On Combinatorial Generation of Prefix Normal Words*, arXiv:1401.6346 (first posted January 24, 2014). https://arxiv.org/abs/1401.6346.
- P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, and J. Sawada, *Normal, Abby Normal, Prefix Normal*, arXiv:1404.2824 (first posted April 1, 2014), especially Section 4 on fixed-density gap inequalities. https://arxiv.org/abs/1404.2824.
- P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, and J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017 (first posted November 28, 2016). https://arxiv.org/abs/1611.09017.

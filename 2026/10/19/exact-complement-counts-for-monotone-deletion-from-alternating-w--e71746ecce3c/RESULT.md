# Exact complement counts for monotone deletion from alternating words

## Finding
For distinct letters \(a,b\), integers \(k\ge2\) and \(m\ge1\), consider the set \(C((ab)^m,a^k b^k)\) of distinct complementary scattered factors: the residual words after deleting any increasing-position embedding of \(a^k b^k\) from \((ab)^m\). The set is empty for \(m<2k-1\). For \(m\ge2k-1\) it has the exact cardinality
\[
|C((ab)^m,a^k b^k)|=\binom{m-1}{2k-2}+\binom m{2k}.
\]
Writing \(r=m-k\), the entire set is a disjoint union of two uniquely parameterized families \(\mathcal L_{r,k-1}\) and \(\mathcal L_{r,k}\), where
\[
\mathcal L_{r,j}=\left\{(ab)^{t_0}b(ab)^{t_1}\cdots b(ab)^{t_j}a(ab)^{t_{j+1}}\cdots a(ab)^{t_{2j}}:\ t_i\in\mathbb Z_{\ge0},\ \sum_{i=0}^{2j}t_i=r-j\right\}
\]
for \(0\le j\le r\), and \(\mathcal L_{r,j}=\varnothing\) otherwise. There are exactly \(j\) isolated letters \(b\), then exactly \(j\) isolated letters \(a\), with \(2j+1\) gaps of intact \(ab\) pairs. Different gap tuples give different residual words. Relabeling \(a,b\) produces the same theorem for any two-letter alphabet.

## Assumptions and scope
Words and embeddings are linear, not cyclic. The parent word has \(m\) consecutive ordered blocks \(ab\). A scattered embedding chooses \(k\) increasing positions carrying \(a\), followed by \(k\) increasing positions carrying \(b\). No quotient by reversal, rotation, or alphabet relabeling is used in the count; the two letters are distinguished. Binomial coefficients are zero when the upper index is less than the nonnegative lower index. The case \(k=1\) also satisfies the formula, but it is excluded from the new scoped result because a previously studied repeated-permutation deletion case already covers it.

## Proof
**Feasibility.** The \(k\)-th chosen \(a\) is at earliest in the \(k\)-th \(ab\) block. All \(k\) chosen \(b\)'s must occur there or in later blocks, requiring at least \(k-1\) later blocks. Thus \(m\ge2k-1\) is necessary; choosing the first \(k\) letters \(a\) and last \(k\) letters \(b\) establishes sufficiency.

**Two deletion types.** Examine each full parent block \(ab\): its two letters are (I) both retained, (II) only \(b\) retained (its \(a\) is deleted), (III) only \(a\) retained (its \(b\) is deleted), or (IV) both deleted. Because all deleted \(a\)'s occur before all deleted \(b\)'s, every type-II block precedes every type-III block. At most one type-IV block can exist: after deleting its \(b\), no further \(a\) may be deleted, and before deleting its \(a\), no earlier \(b\) may have been deleted. Let \(d\in\{0,1\}\) be the number of type-IV blocks. There are exactly \(j=k-d\) type-II and \(j\) type-III blocks, and \(m-(2j+d)=r-j\) type-I blocks. Removing the type-IV block if it exists, and concatenating surviving block outputs, gives precisely a word in \(\mathcal L_{r,j}\), with \(j=k\) when \(d=0\) and \(j=k-1\) when \(d=1\).

**Converse.** Given a gap tuple for \(\mathcal L_{r,k}\), realize each \(ab\) pair as a fully retained parent block, each isolated \(b\) as a block with its \(a\) deleted, and each isolated \(a\) as a block with its \(b\) deleted. The deleted letters form exactly \(a^k b^k\). For \(\mathcal L_{r,k-1}\), insert one additional completely deleted \(ab\) block between the isolated \(b\)'s and isolated \(a\)'s (in the central gap). The deleted sequence again equals \(a^k b^k\). Each construction has exactly \(m\) parent blocks and realizes the designated residual word.

**Unambiguity.** For any produced residual word, define its prefix excess \(h(t)\) as the number of \(b\)'s minus the number of \(a\)'s in its first \(t\) positions, starting with \(h(0)=0\). A full \(ab\) pair makes a downward step followed by an upward step, returning to the same height. Each isolated \(b\) makes an upward step, and each isolated \(a\) makes a downward step. Thus for every word in \(\mathcal L_{r,j}\), the maximum of \(h(t)\) is exactly \(j\), proving the families with different \(j\) are disjoint. For a fixed \(j\), the first attainment of height \(j\) determines the entire ascending portion: read from the beginning, parsing an initial \(a\) together with its following \(b\) as one full \(ab\) pair, and parsing an initial \(b\) as a solitary \(b\), until exactly \(j\) solitary \(b\)'s have been read. The last attainment of height \(j\) similarly determines the entire descending portion: parse backward from the end, parsing terminal \(b\) with its preceding \(a\) as one full pair and terminal \(a\) as a solitary \(a\), until \(j\) solitary \(a\)'s have been read. Between these first and last peak positions there are only complete \(ab\) pairs. This recovers the unique tuple \((t_0,\ldots,t_{2j})\); for \(j=0\) the only word is \((ab)^r\).

**Counting.** The number of nonnegative \((2j+1)\)-tuples summing to \(r-j\) is, by stars and bars,
\[
|\mathcal L_{r,j}|=\binom{r+j}{2j}.
\]
Since \(r=m-k\), the disjoint classes \(j=k-1\) and \(j=k\) contribute \(\binom{m-1}{2k-2}\) and \(\binom m{2k}\), respectively. This completes the exact formula.

## Verification
The standalone Python 3 checker `check_new.py` independently constructs all admissible embedding complements, constructs all words from the gap-tuple normal form, and compares them as literal string sets for every feasible parameter pair with \(1\le m\le11\). It checks the formula and disjointness/normal-form injectivity as well as direct shape checks when the residual half-length is at most eight. It reports 36 feasible pairs checked, with all assertions passing. These finite checks are supplementary; the preceding argument proves every permitted \(m,k\).

## Relationship to prior work
Adamson, Fleischmann and Huch (2026) introduced complement scattered factors and gave general algorithms for constructing their sets, along with structural observations, but concluded that closed formulas for special families remain an open direction (their conclusion, Section 5). Their general enumeration algorithm permits computing this family individually but does not state the two-binomial formula or the peak-index normal form. There is also an earlier formula for complements of a **repeated permutation word** removed from a repeated permutation word. Here the deleted word is \(a^k b^k\), not \((ab)^k\); for \(k\ge2\) these are non-equivalent deletion patterns and that earlier statement does not imply the present result. The two-binomial formula supplies a particularly small closed-form test family for algorithms on complementary subsequences.

## Limitations
This result concerns distinct residual words from exactly one specified parent and one specified deletion pattern. It does not enumerate the number of embeddings producing each residual, extend to arbitrary parent words or alphabet sizes, or establish a universal upper bound for complement scattered factor sets. No claim of independent external certification is made; prior-work completeness cannot be guaranteed beyond the literature examined.

## References
Adamson, D., Fleischmann, P., and Huch, A. (2026), *(Sets of) Complement Scattered Factors*, arXiv:2603.20790, first submitted 21 March 2026. https://arxiv.org/abs/2603.20790; HTML version https://arxiv.org/html/2603.20790v1.

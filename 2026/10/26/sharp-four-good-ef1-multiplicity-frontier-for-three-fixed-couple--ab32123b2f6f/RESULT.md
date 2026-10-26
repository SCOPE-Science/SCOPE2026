# Sharp four-good EF1 multiplicity frontier for three fixed couples

## Finding

There are three predetermined groups, each containing two agents, and exactly four distinct indivisible goods. Each agent has an arbitrary nonnegative additive value for every good; both agents in a group enjoy the full value of the group's common bundle. An allocation is **balanced** when its three bundle sizes are \((2,1,1)\), and it is **EF1** when, for every agent, envy of every other group's bundle disappears after removing at most one good from that other bundle.

**Theorem.** Every such instance admits **at least two distinct labeled, complete, balanced EF1 allocations**. The constant two is sharp even when all six agents' values for the four goods are strictly positive and pairwise distinct.

More precisely, for strict within-agent rankings, let \(N\) be the number of balanced EF1 allocations. The following is its complete distribution among the \(24^5=7{,}962{,}624\) normalized rank profiles (the first agent's ranking is fixed by simultaneous relabeling of goods). Equivalently, a uniformly random independent strict ranking for each of the six agents has \(\Pr(N=j)=h_j/24^5\):

| \(j\) | \(h_j\) | \(j\) | \(h_j\) |
|---:|---:|---:|---:|
| 2 | 6912 | 11 | 295296 |
| 3 | 129024 | 12 | 209792 |
| 4 | 701184 | 13 | 55680 |
| 5 | 1215744 | 14 | 80064 |
| 6 | 1499776 | 15 | 15360 |
| 7 | 1387008 | 16 | 6528 |
| 8 | 1026816 | 17 | 1152 |
| 9 | 934272 | 18 | 7872 |
| 10 | 390144 | — | — |

No other value of \(N\) occurs under strict rankings. In particular, \(2\le N\le18\), the minimum occurs with probability \(1/1152\), and \(\mathbb{E}[N]=64/9\).

Together with the existing five-good three-couple nonexistence example in Gölz and Yaghoubizade, this establishes **five as the smallest number of goods allowing EF1 nonexistence for three fixed couples with nonnegative additive values**. The five-good negative example itself is due to that prior work, not to the present theorem.

## Assumptions and scope

Groups are fixed and labeled \(0,1,2\); each group has exactly two fixed agents. Goods are distinct and labeled \(0,1,2,3\). Every one of the six utility functions is additive with nonnegative singleton values; ties and zeros are allowed for the universal existence assertion. The exact frequency distribution concerns six independent uniformly random *strict* orders of the four goods, or equivalently all such ordinal profiles counted uniformly. The bundle sizes are required to be \((2,1,1)\), but which group holds two goods is unrestricted. The number \(N\) counts labeled allocations of the actual goods to actual groups, not symmetry classes of allocations.

## Proof

**1. EF1 is ordinal for a balanced four-good allocation.** Suppose group \(A\) receives the pair \(\{p,q\}\) and the other two groups receive singleton goods \(b\) and \(c\). An agent in the two-good group cannot envy either singleton after removing its unique good, because her own bundle has nonnegative value. Likewise, a singleton-group agent cannot envy the *other* singleton after removal. For an agent in the group assigned \(b\), the sole potentially nontrivial inequality is

\[
 u(b)\ge \min\{u(p),u(q)\}.
\]

The analogous inequality holds for each agent in the group assigned \(c\). Thus for strict orders, exactly one type of EF1 violation is possible: a singleton agent ranks both paired goods *strictly above* her singleton. Only the six rankings matter, not cardinal gaps between values.

**2. All rank profiles reduce to a finite complete certificate.** A simultaneous permutation of the four good labels induces a bijection on balanced allocations and preserves EF1. Because the first member of the first group has a strict order, relabel the goods so that this order is \((0,1,2,3)\), best first. Each of the other five agents now has exactly \(4!=24\) possible rankings, giving \(24^5\) cases, one representative from each good-relabeling orbit. Every balanced allocation is determined by choosing (a) the group holding the pair, (b) its unordered pair of goods and (c) which of the two remaining groups receives which of the remaining goods. The number is \(3\binom42\cdot2=36\).

For each group \(g\) and each of its \(24\) possible rankings \(r\), form the exact \(36\)-bit set \(B_{g,r}\) of allocations in which a singleton member with that ranking prefers **both** paired goods to her singleton. The set is empty at allocations in which \(g\) owns the pair. For each normalized six-agent rank profile \((r_0,\ldots,r_5)\), the number of EF1 allocations is exactly

\[
 36-\left|B_{0,r_0}\cup B_{0,r_1}\cup B_{1,r_2}\cup B_{1,r_3}\cup B_{2,r_4}\cup B_{2,r_5}\right|.
\]

In the normalized count \(r_0=(0,1,2,3)\). The accompanying `verify_four_goods.cpp` builds each of the \(36\) allocations and all \(72\) invalidity masks directly from these definitions, then executes all \(24^5\) combinations using integer bitwise unions and exact population counts. It reports precisely the table above; in particular the minimum is two and no normalized profile is omitted. This is an exhaustive finite proof, not a sample or a claim inferred from a non-exhaustive experiment. The source code and its output are part of the result's reproducibility package.

**3. Ties and zeros do not weaken the guarantee.** For arbitrary nonnegative cardinal utilities, break each agent's value ties in any fixed fashion to obtain a strict ranking that preserves every weak value comparison. At least two balanced allocations pass the strict-ranking criterion by Step 2. For every such allocation, each singleton agent has a good weakly valued at least as highly as at least one good held by the paired group. Therefore the actual cardinal EF1 inequality in Step 1 holds. Both allocations remain distinct. This proves the universal assertion.

**4. Sharpness at four goods.** For goods \((0,1,2,3)\), take the following six strictly positive additive singleton-value vectors, with rows grouped by couple:

| Group | Agent 1 | Agent 2 |
|---:|:---:|:---:|
| 0 | \((4,3,2,1)\) | \((4,1,2,3)\) |
| 1 | \((4,3,2,1)\) | \((1,2,4,3)\) |
| 2 | \((4,1,3,2)\) | \((2,4,1,3)\) |

Checking the \(36\) balanced allocations by the literal EF1 formula leaves **exactly two**: the vectors of group assignments to goods \((0,1,2,3)\) are \((0,1,1,2)\) and \((0,2,1,2)\). The standalone `check_examples.py` evaluates the literal additive EF1 inequalities for each labeled allocation, independently of the rank-mask computation.

**5. Sharpness of the number of goods for existence.** With at most three goods, allocate at most one good to each group; then every agent is EF1 by nonnegativity. The theorem handles four goods. The five-good three-couple instance in Gölz and Yaghoubizade, Theorem 3.3, has value pairs

\[
\begin{array}{c|cc}
 & \text{first agent}&\text{second agent}\\
0&(2,2,0,0,1)&(0,0,2,2,1)\\
1&(0,2,0,2,1)&(2,0,2,0,1)\\
2&(2,0,0,2,1)&(0,2,2,0,1)
\end{array}
\]

and no EF1 allocation. That literature construction is also checked directly against all \(3^5=243\) labeled allocations in `check_examples.py`.

**6. An analytic cross-check of the distribution.** For a uniformly sampled strict profile and a fixed balanced allocation, four agents are in singleton groups. Each one independently has probability \(2/3\) of not ranking her singleton last among the three goods comprising her singleton and the paired bundle. Consequently, linearity of expectation gives

\[
 \mathbb E[N]=36(2/3)^4=64/9.
\]

This agrees exactly with the weighted sum of the displayed histogram, checked using integer arithmetic in the certificate. It is an independent mathematical identity, not a replacement for the complete enumeration of the distribution.

## Verification

Execute the self-contained source files from the same directory:

```
c++ -std=c++17 -O2 verify_four_goods.cpp -o verify_four_goods
./verify_four_goods
python3 check_examples.py
```

The C++ certificate enumerates precisely \(7{,}962{,}624\) normalized strict profiles and \(36\) balanced allocations per profile via exact bit masks. It prints the complete histogram, confirms a minimum of two and maximum of eighteen, and checks the first-moment identity using integer arithmetic. The independent Python program checks all \(36\) candidate allocations in the sharpness witness and all \(243\) allocations in the five-good literature counterexample using the direct cardinal EF1 definition. `verification_output.txt` records the deterministic outputs. No approximate arithmetic or external data are used in the proofs.

## Relationship to prior work

Gölz and Yaghoubizade (2025, arXiv:2508.13432v1), Section 3.2 and Theorem 3.3, establish EF1 nonexistence for three couples using five goods; Section 3.1 establishes EF1 existence for *two* couples. Their inspected results do not state the exact four-good minimum, the four-good universal multiplicity of at least two, or the strict-profile frequency law. The five-good negative direction is prior work, not asserted as new.

Kyropoulou, Suksompong, and Voudouris (2020) treat primarily two *fixed* groups and also a setting allowing group memberships to change. Their fixed-group results do not give three predetermined couples the asserted four-good multiplicity. Bu, Li, Liu, Song, and Tao (arXiv:2310.03475v2) investigate double fairness with allocator preferences, including a two-agent theorem; those results do not imply the stated fixed-three-couple distribution.

Deligkas, Eiben, Ganian, Goldsmith, Gründel, and Wietheger (arXiv:2610.28213v1, 20 October 2026) prove NP-completeness for three fixed couples with unrestricted item count. Their inspected construction starts from five special goods and additional partition items, and does not imply the exact four-good histogram or fixed-small-instance guarantee.

## Limitations

The complete distribution is for independently uniform **strict ordinal preferences**, not for a distribution of real cardinal values with ties. The universal lower bound uses nonnegative additive valuations and does not extend by the proof to chores, arbitrary nonadditive valuations, more goods, more couples, or an arbitrary larger group size. The certificate yields an exact theorem at four goods and is not a statement about efficient fair-division algorithms for variable item counts. As with any literature comparison, unindexed or not-yet-inspected results may overlap despite the targeted checks described separately in the review.

## References

1. Paul Gölz and Hannane Yaghoubizade. *Fair Division Among Couples and Small Groups*. arXiv:2508.13432v1, first posted 19 August 2025. https://arxiv.org/abs/2508.13432
2. Maria Kyropoulou, Warut Suksompong, Alexandros A. Voudouris. *Almost Envy-Freeness in Group Resource Allocation*. Theoretical Computer Science 841 (2020), 110–123. https://repository.essex.ac.uk/28254/1/group-EF.revision.pdf
3. Xiaolin Bu, Zihao Li, Shengxin Liu, Jiaxin Song, Biaoshuai Tao. *Fair Division with Allocator's Preference*. arXiv:2310.03475v2, 2025 version. https://arxiv.org/abs/2310.03475
4. Argyrios Deligkas, Eduard Eiben, Robert Ganian, Tiger-Lily Goldsmith, Marlene Gründel, Simon Wietheger. *Subjective Valuations Make It Hard to be Fair: The Complexity of Resource Allocation to Groups of Agents*. arXiv:2610.28213v1, 20 October 2026. https://arxiv.org/abs/2610.28213

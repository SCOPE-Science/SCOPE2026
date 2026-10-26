# An unbounded VC–Littlestone gap in fixed-quota path matchings

## Finding

For every integer \(s\ge1\), let \(F_s\) be the disjoint union of \(s\) copies of the eight-vertex path \(P_8\). Define \(\mathcal H_s\) to be the class of Boolean edge-incidence functions \(h_M(e)=\mathbf1[e\in M]\), where \(M\) selects **exactly three pairwise disjoint edges in each component** of \(F_s\). Then

\[
\operatorname{VCdim}(\mathcal H_s)=2s,\qquad
\operatorname{Ldim}(\mathcal H_s)=3s.
\]

Thus this natural family of component-quota matching classes has an arbitrarily large additive gap, \(\operatorname{Ldim}-\operatorname{VCdim}=s\), although every concept has exactly \(3s\) positive coordinates. The single eight-vertex path is the smallest path whose fixed-cardinality matching class can have Littlestone dimension three; its rank-three class has VC dimension two.

## Assumptions and scope

A matching is a set of graph edges without common endpoints. Each path has ordered edges \(e_0,e_1,\ldots,e_6\), with consecutive edges sharing a vertex. The domain of a concept is the full edge set of \(F_s\). Queries ask whether a particular edge belongs to the unknown matching. VC dimension uses one fixed shattered subset of the domain; Littlestone dimension permits the queried edge to depend on previous binary answers. All dimensions use deterministic binary incidence, not multiclass matching predictions or relaxed weight constraints. The quota of three is imposed **separately** in each component; the claim does not concern all arbitrary matchings having total size \(3s\).

## Proof

**Base class.** For \(s=1\), the ten possible rank-three matchings of the path, written as zero-indexed edge triples, are

```
024 025 026 035 036 046 135 136 146 246
```

These are all possibilities because three chosen indices must have pairwise gaps at least two. Equivalently, for a path with \(N\) ordered edges, the number of rank-\(r\) matchings is \(\binom{N-r+1}{r}\), when \(0\le r\le\lceil N/2\rceil\).

**Static shattering.** The pair \(\{e_0,e_2\}\) is shattered: the four traces \(11,10,01,00\) are supplied respectively by matchings `024`, `035`, `246`, and `135`. No three-edge set is shattered. Indeed, to realize trace \(111\), a candidate queried triple \(Q\) must itself be one of the ten rank-three matchings shown above. The following exhaustive certificate gives, for each such \(Q\), an absent three-bit trace (bits are ordered by increasing queried edge index):

| Queried triple | Absent trace |
|---|---|
| `024` | `010` |
| `025` | `011` |
| `026` | `010` |
| `035` | `001` |
| `036` | `000` |
| `046` | `010` |
| `135` | `101` |
| `136` | `100` |
| `146` | `110` |
| `246` | `010` |

Every entry is checked directly against the complete ten-matchings list; the accompanying standalone checker repeats the test. Hence \(\operatorname{VCdim}(\mathcal H_1)=2\).

**Adaptive shattering.** Use the following depth-three binary tree. The root queries \(e_0\); after answer \(0\), query \(e_3\), and after answer \(1\), query \(e_2\). The third query, indexed by the first two answers, is

```
00 -> e1   01 -> e5   10 -> e3   11 -> e4
```

All eight complete answer paths are witnessed as follows:

| Answers | Witness matching |
|---|---|
| `000` | `246` |
| `001` | `146` |
| `010` | `136` |
| `011` | `135` |
| `100` | `046` |
| `101` | `035` |
| `110` | `025` |
| `111` | `024` |

For example, `101` queries \(e_0,e_2,e_3\) and is realized by `035`; every other row is checked analogously. Thus \(\operatorname{Ldim}(\mathcal H_1)\ge3\). Since there are only ten distinct hypotheses and a shattered tree of depth four needs sixteen distinct root-to-leaf witnesses, \(\operatorname{Ldim}(\mathcal H_1)\le\lfloor\log_2 10\rfloor=3\). This proves the base case.

**Additivity on disjoint query domains.** For nonempty binary classes \(\mathcal C\) and \(\mathcal D\) on disjoint domains, denote by \(\mathcal C\otimes\mathcal D\) all functions that restrict to one member of each factor. Then

\[
\operatorname{VCdim}(\mathcal C\otimes\mathcal D)
 =\operatorname{VCdim}(\mathcal C)+\operatorname{VCdim}(\mathcal D),
\]

because a set is shattered by the product precisely when its intersections with the two domains are each shattered. Likewise

\[
\operatorname{Ldim}(\mathcal C\otimes\mathcal D)
 =\operatorname{Ldim}(\mathcal C)+\operatorname{Ldim}(\mathcal D).
\]

For the lower bound, append a shattered tree for \(\mathcal D\) at every leaf of a shattered tree for \(\mathcal C\). For the upper bound, induct on the sum of the factor dimensions. At a proposed root from the first domain, at least one nonempty binary-answer restriction of \(\mathcal C\) has dimension at most one below the original dimension; by induction, that branch of the product has dimension at most the sum minus one. The argument is symmetric for a root from the second domain. A split with an empty branch cannot shatter even one additional level. This proves the upper bound. Iterating with \(\mathcal C=\mathcal D=\mathcal H_1\) gives the displayed \(2s\) and \(3s\) formulas.

**Sharp first depth-three path.** Every fixed-cardinality matching class on a path with at most six edges has Littlestone dimension at most two. If its matching rank is at most two, no fully positive branch can be longer than two (every concept selects at most two edges). If the rank is three, the only possible paths with at most six edges supporting that rank have five or six edges, with respectively one or four matching hypotheses by the counting formula, again precluding a shattered tree of depth three. Thus seven edges, or eight vertices, is the least path order allowing depth three; the base construction attains it with VC dimension two.

## Verification

The standalone file `verify_uniform_matchings.py` generates every matching of the base path, independently computes exact VC and Littlestone dimensions via enumeration and the binary game recurrence, replays all eight depth-three root-to-leaf certificates, and checks all ten missing static traces. It also enumerates all fixed-rank path matching families on paths with at most six edges to check minimality. Run with Python 3:

```
python3 verify_uniform_matchings.py
```

The recorded output is in `verification_output.txt` and ends with `ALL_MATCHING_CHECKS_PASS`. The unrestricted product result follows from the proved additivity lemma rather than from numerical experiments. The listed dimensions for multiple components in the output are derived analytically, not obtained by enumerating their exponentially large full concept matrices.

## Relationship to prior work

General learning-theoretic literature distinguishes static VC shattering from adaptive Littlestone shattering. Manurangsi's 2022 preprint (published at ITCS in 2023) studies hardness of computing these invariants on explicitly represented classes, while Hanneke's 2024 paper develops relationships between them and other combinatorial dimensions. Neither of the inspected relevant results supplies the rank-three matching calculation on \(P_8\), its sharp path-size boundary, or this exact quota-class product formula. The additive-product argument itself is elementary and is not asserted to be new. The finding is the exact matching-specific witness and its consequence, not the abstract existence of a VC/Littlestone gap.

## Limitations

No exact formula for matchings of arbitrary rank on arbitrary paths or graphs is claimed. The componentwise quota is essential to the product formula; it must not be confused with a single total quota. An independent scientific review has not been carried out, and exhaustive historical publication priority remains unverified. The small base-class computation is fully reproducible but does not itself establish novelty.

## References

1. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443v1 (first posted 2022-11-02), and ITCS 2023, DOI:10.4230/LIPIcs.ITCS.2023.85.
2. S. Hanneke, *The Star Number and Eluder Dimension: Elementary Observations About the Dimensions of Disagreement*, Proceedings of Machine Learning Research 247 (2024), pp. 2308–2359, https://proceedings.mlr.press/v247/hanneke24a.html.

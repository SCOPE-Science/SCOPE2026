# Exact finite rectangular classification of two-dimensional complete sparse rulers through \(6\times6\)

## Finding

For integers \(1\le a\le b\le5\), define \(R(a,b)\) as the smallest size of a set \(P\subseteq\{0,1,\ldots,a\}\times\{0,1,\ldots,b\}\) such that for every vector \((u,v)\in\mathbb{Z}^2\) with \(|u|\le a\) and \(|v|\le b\), some \(p,q\in P\) satisfy \(p-q=(u,v)\). This is the full rectangular difference-coarray criterion, not a vector sumset condition.

The exact minimum mark counts are:

| Span \(a\) | \(b=1\) | \(b=2\) | \(b=3\) | \(b=4\) | \(b=5\) |
|---|---:|---:|---:|---:|---:|
| 1 | 4 | 5 | 6 | 7 | 8 |
| 2 | — | 7 | 8 | 9 | 10 |
| 3 | — | — | 9 | 11 | 12 |
| 4 | — | — | — | 12 | 13 |
| 5 | — | — | — | — | 15 |

In particular, \(R(5,5)=15\). The source paper defines \(M_2(n,m)\) using a grid of \(n\) by \(m\) points (indices \(0\) through \(n-1\)); therefore the source's invariant is \(M_2(a+1,b+1)=R(a,b)\), **not** \(M_2(a,b)=R(a,b)\).

## Assumptions and scope

The positions are integer-coordinate points; differences are taken in \(\mathbb{Z}^2\), not modulo coordinate periods. All ordered differences, including zero, are allowed. The finite classification includes every positive rectangular span with \(a\le b\le5\); rectangles with exchanged axes follow by transposition. This is a minimum-cardinality classification for uncolored difference rulers, and makes no assertion about fixed-alphabet unbordered partial words.

## Proof

**Corner forcing.** The extreme difference \((a,b)\) can only arise from \((a,b)-(0,0)\); the extreme difference \((a,-b)\) can only arise from \((a,0)-(0,b)\). Thus every feasible set contains the four corners. The hypothesis \(a,b\ge1\) makes these distinct.

**Difference classes and initial lower bound.** Ignore \((0,0)\), which every nonempty set realizes, and identify opposite displacements \(d\sim-d\). Represent the resulting classes uniquely by \(u>0,-b\le v\le b\), or by \(u=0,1\le v\le b\). The number of required classes is exactly \(D=a(2b+1)+b=2ab+a+b\). Each unordered pair of distinct selected points contributes just one such class, hence every ruler with \(k\) points must obey \(\binom{k}{2}\ge D\) and \(k\ge4\).

**Finite exhaustive exclusion.** The accompanying `verify.cpp` implements a depth-first enumeration of all \(k\)-point subsets containing the four forced corners. All other grid points occur in a fixed lexicographic order, and branches select strictly increasing point indices, so every relevant set appears exactly once unless excluded by the following sound bound. Let \(c\) be the current number of chosen points, \(r\) the number of points still to choose, and \(U\) the number of distinct required displacement classes not yet covered. Adding these \(r\) points creates at most \(cr+\binom{r}{2}\) additional unordered point-pairs. Therefore, when \(U>cr+\binom{r}{2}\), no completion is feasible and the branch can safely be pruned. The program records covered classes with exact 64-bit masks; the largest case has \(D=60\). It tries each cardinality from the proven counting lower bound through the first success. Exhaustive nonexistence at each smaller cardinality and a successful complete-cover witness establish each of the fifteen exact minima.

**Upper-bound witnesses.** `witnesses.json` contains one integer-coordinate point set for every entry. `check_witnesses.py` checks directly, without relying on the enumeration implementation, that each witness uses the stated number of distinct in-range points and that its full ordered difference set contains every required vector. This provides independently recomputed upper bounds. The lower bounds use exact exhaustive enumeration and the completeness/pruning argument above, not an asymptotic or extrapolated assertion.

## Verification

With a C++17 compiler, run `c++ -std=c++17 -O2 verify.cpp -o verify && ./verify 5`. The program checks that the first feasible cardinality for each of the fifteen rectangles agrees with the hardcoded theorem table and prints `VERIFY_OK`. With Python 3 standard library, run `python3 check_witnesses.py` in the same directory as `witnesses.json`; it independently verifies all fifteen upper-bound certificates. All enumerations use integer arithmetic and exact bit operations; no external solver or platform-specific libraries are required.

The most demanding exact rejection is the \(5\)-by-\(5\) span with \(14\) marks; the depth-first search considers all feasible branches after proved pair-count pruning and finds none. The search then constructs a \(15\)-mark witness. The printed leaf totals are diagnostic counts after safe pruning, **not** estimates or claims about how many subsets exist before pruning.

## Relationship to prior work

Saarela and Vanhatalo (2024 preprint, later 2026 journal article), Section 4, define the two-dimensional ruler and \(M_2\), prove a general pair-counting lower bound and give asymptotic constructions; the inspected source does not include this finite exact table. Their indexing of rectangular *dimensions* differs from the span notation used here by one in each coordinate. The construction and general lower bound in that paper are not claimed as new.

Kohonen, Koivunen, and Rajamäki (2018) give exact small *planar additive-basis* data for \(A+A\), including a 2018 table and OEIS A306608. Those values do not assert the present \(A-A\) difference-base minimum; the two coverage conditions are different, even though both are used in sensor-array design. Existing two-dimensional coarray constructions provide useful coverage upper bounds, but the checked results do not state matching optimality for every rectangle listed here.

## Limitations

The theorem covers exactly \(1\le a\le b\le5\), not arbitrary rectangle sizes. No optimality claim is made for unbordered partial words over a specified alphabet, and no classification of all minimum witness sets is asserted. The literature priority search is not exhaustive: relevant older engineering sources on hole-free planar **difference** coarrays may contain unindexed computational tables or stronger statements. A plausible 2018 publisher text was not accessible via available lawful routes, and a verified absence of equivalent earlier work is not claimed. The 15-entry theorem itself requires the distributed exact enumeration source for its finite lower bounds; the witness table alone certifies only the upper bounds.

## References

1. A. Saarela and A. Vanhatalo, *A Connection Between Unbordered Partial Words and Sparse Rulers*, arXiv:2408.16335, version 1 publicly submitted 29 August 2024, Section 4. Later: *Electronic Journal of Combinatorics* 33 (2026), #P1.40. https://arxiv.org/abs/2408.16335
2. J. Kohonen, V. Koivunen and R. Rajamäki, *Planar Additive Bases for Rectangles*, *Journal of Integer Sequences* 21 (2018), Article 18.9.8, especially Sections 1–3 and 7, Table 2. https://cs.uwaterloo.ca/journals/JIS/VOL21/Rajamaki/raj.pdf
3. C. L. Liu and P. P. Vaidyanathan, *Two-dimensional sparse arrays with hole-free coarray and reduced mutual coupling*, Asilomar Conference (2016), DOI: 10.1109/ACSSC.2016.7869629 (bibliographic comparison; complete text not inspected).
4. R. Rajamäki and V. Koivunen, *Sparse Active Rectangular Array with Few Closely Spaced Elements*, IEEE Signal Processing Letters (2018), arXiv:1803.02219 (abstract inspected; full text not accessible).

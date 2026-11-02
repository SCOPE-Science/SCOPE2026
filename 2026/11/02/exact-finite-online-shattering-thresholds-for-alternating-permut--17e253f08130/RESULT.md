# Exact finite online-shattering thresholds for alternating permutations

## Finding
For every integer \(2\le n\le8\), let \(\mathcal Z_n\) consist of the permutations \(\pi=(\pi_1,\ldots,\pi_n)\) of \([n]\) satisfying
\[\pi_1<\pi_2>\pi_3<\pi_4>\cdots.\]
Each query compares two distinct positions \(i<j\), with Boolean answer \(1\) exactly when \(\pi_i<\pi_j\). Then
\[\operatorname{VCdim}(\mathcal Z_n)=n-2,\]
and the exact Littlestone dimensions, for \(n=2,3,4,5,6,7,8\) in that order, are
\[0,1,2,4,5,7,9.\]
In particular, the first gap of at least three between the two dimensions is attained at eight positions:
\[\operatorname{VCdim}(\mathcal Z_8)=6,\qquad \operatorname{Ldim}(\mathcal Z_8)=9.\]
The first strict loss relative to the cardinality bound occurs at seven positions: there are \(272\) concepts, so the bound is eight, but the Littlestone dimension is seven. At eight positions there are \(1385\) concepts, the cardinality bound is ten, and the dimension is nine.

## Assumptions and scope
All permutations have distinct entries. A shattered static set of queries supports every Boolean labeling by some member of \(\mathcal Z_n\). A complete depth-\(d\) adaptive tree may choose its query separately at each internal node, and all \(2^d\) answer paths must be realized. Repeated queries and adjacent-position comparisons cannot improve depth. All reported adaptive values are finite and restricted to \(2\le n\le8\); no extrapolation to larger \(n\) is claimed.

## Proof
**Static upper bound.** Represent the queried pairs by a graph on the \(n\) positions. If it contains a cycle, choosing Boolean comparison outcomes that orient that cycle cyclically produces an impossible strict order. Otherwise, a support with \(n-1\) queried pairs is a spanning tree. Fix an adjacent pair \(i,i+1\). Its comparison direction is predetermined by the alternating inequalities. On the unique tree path between these two vertices, orient the queried comparisons in the opposite direction; that labeling contradicts the fixed comparison by transitivity. Thus no \(n-1\) queries can be shattered. Larger shattered supports would contain such a subset, so \(\operatorname{VCdim}\le n-2\).

**Static lower bound.** The even-indexed positions \(1,3,5,\ldots\) and odd-indexed positions \(2,4,6,\ldots\) each form an unconstrained group internally. In each group, select comparisons between its first member and every other member. These supports have altogether \(n-2\) queries. Any labeling of the selected star comparisons is realizable by a suitable strict order within each group. Assign all values on the first group smaller than all values on the second group; the resulting permutation satisfies the alternating inequalities, and its responses realize the chosen labeling. Hence \(\operatorname{VCdim}\ge n-2\).

**Exact adaptive recurrence.** Index the finite concepts, and represent a nonempty version space by a bit mask \(S\) of its possible concepts. For a comparison query \(q\), let \(S_{q,1}\) and \(S_{q,0}\) be its two response subsets. Define \(R(S)=0\) if \(|S|\le1\) and otherwise
\[R(S)=\max_{q: S_{q,0},S_{q,1}\ne\varnothing}\bigl(1+\min\{R(S_{q,0}),R(S_{q,1})\}\bigr),\]
where the maximum of an empty set is zero. Both children are strictly smaller, so induction on \(|S|\) proves this recurrence computes the exact Littlestone dimension. Query outcomes fixed across all members never split and are excluded. The only upper-bound pruning in the supplied exact implementation is the necessary condition that a state supporting depth \(d\) contains at least \(2^d\) distinct concepts. Specifically, once a current candidate depth is \(b\), a query branch containing fewer than \(2^b\) concepts cannot improve \(b\).

The complete computation enumerates respectively \(1,2,5,16,61,272,1385\) alternating permutations for \(n=2,\ldots,8\), and solves the recurrence without a depth cutoff. For \(n=8\), the initial state has rank nine. A separate Boolean recursion that asks only whether depth ten is possible also returns false (\(75{,}626\) memoized state-depth pairs). To expose the lower bound independently of the rank computation, `certificate.json` contains a complete depth-nine comparison tree with \(511\) internal nodes and \(512\) distinct permutation witnesses. `verify.py` rechecks every witness against its full root-to-leaf answer path. This proves both directions of every displayed finite dimension claim.

## Verification
Run `python verify.py certificate.json` with Python 3 and the standard library. The verifier enumerates alternating permutations directly and independently as topological sorts of the height-two zigzag poset, comparing the two complete sets at each size. It tests the explicit static-shattering supports, computes all the reported adaptive ranks, separately rules out depth ten at eight positions, and validates every branch and leaf witness in the supplied tree. A successful replay ends with `ZIGZAG_ALL_CHECKS_PASS`. The full certificate is self-contained and does not depend on external files.

## Relationship to prior work
Alternating permutations are linear extensions of the zigzag (or fence) poset; their Euler-number enumeration is classical. Chan and Pak's *Linear extensions of finite posets* (arXiv:2311.02743, first posted 2023-11-05), §11.4, discusses zigzag linear extensions and their enumeration; its treatment is not an adaptive comparison-shattering classification. General results on shattering comparison queries over a finite poset already give the static formula \(n-\mathrm{height}(P)\), which specializes to the static result above because the zigzag poset has height two. The static formula is included for comparison and is **not** claimed as new. General exact dimensions for unrestricted permutations do not determine the present restricted-family dimensions. The claimed contribution is the exact adaptive sequence and its first three-unit gap.

## Limitations
The exact adaptive table stops at eight positions. An exhaustive computation over a finite class does not establish any large-order formula. Equivalence under alternate terminology for adaptive comparison trees and historical priority beyond the examined references remain possible. No independent external scientific audit has been conducted.

## References
- S. H. Chan and I. Pak, *Linear extensions of finite posets*, arXiv:2311.02743 (initial posting 2023-11-05), §11.4. https://arxiv.org/abs/2311.02743
- P. Manurangsi and A. Rubinstein, *Inapproximability of VC Dimension and Littlestone's Dimension*, arXiv:1705.09517 (2017), for the general explicit-class computation setting. https://arxiv.org/abs/1705.09517
- R. P. Stanley, *A Survey of Alternating Permutations*, arXiv:0912.4240 (2009), for the classical enumeration and zigzag structure. https://arxiv.org/abs/0912.4240

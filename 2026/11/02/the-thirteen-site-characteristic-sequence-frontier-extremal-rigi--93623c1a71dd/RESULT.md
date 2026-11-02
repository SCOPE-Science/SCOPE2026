# The thirteen-site characteristic-sequence frontier: extremal rigidity and its first stability shell

## Finding

Let \(\pi\) be a permutation of \(\{1,\ldots,13\}\) consisting of one cycle of length \(13\). For each \(i=1,\ldots,12\), let \(A_i=\{i,i+1\}\). Define \(T_\pi(S)\) as the integer convex hull of \(\pi(S)\), and define
\[
 c_i(\pi)=\min\{\ell\ge1:T_\pi^\ell(A_i)\supseteq A_i\}.
\]
Write \(c'_1\le\cdots\le c'_{12}\) for the sorted characteristic numbers, and \(S(\pi)=\sum_{i=1}^{12}c_i(\pi)\). Then:

1. Every such \(13\)-cycle satisfies \(c'_k\le k\) for all \(1\le k\le12\). Thus Wang's characteristic-sequence conjecture holds for the new order \(13\).
2. One has \(S(\pi)\le78\). Equality occurs **precisely** for the twelve modular translations \(\pi(j)=1+((j-1+q)\bmod 13)\), with \(1\le q\le12\).
3. Among the remaining permutations, \(S(\pi)\le77\), with equality for **exactly two** permutations, given in one-line notation by
\[
 (3,4,5,6,7,8,9,10,11,13,12,2,1)
 \quad\text{and}\quad
 (13,12,2,1,3,4,5,6,7,8,9,10,11).
\]
Both have the sorted characteristic sequence \((1,2,3,4,5,6,6,8,9,10,11,12)\). In particular, the first non-maximal shell is exactly two points, not an arbitrary collection of near-maximizers.

## Assumptions and scope

The site set is ordered and finite, the permutation is a **single** \(13\)-cycle, and convexification is performed after **every** application of the permutation. The statement concerns the specific finite order \(13\). It neither assumes nor establishes Wang's conjecture at larger orders. The symbol \(S(\pi)\) is the sum of **all twelve** return characteristics, not the sum of ordinary permutation cycle lengths.

## Proof

**The interval graph.** Associate to \(\pi\) a digraph on vertices \(\{1,\ldots,12\}\), with an edge \(i\to j\) exactly when
\[
 \min\{\pi(i),\pi(i+1)\}\le j<\max\{\pi(i),\pi(i+1)\}.
\]
For any consecutive integer block \([a,b]\cap\mathbb Z\), the intervals joining successive images \(\pi(j),\pi(j+1)\), for \(a\le j<b\), form a connected union. Their union is the entire real interval from \(\min_{a\le j\le b}\pi(j)\) to \(\max_{a\le j\le b}\pi(j)\). Therefore the adjacent-cell graph obtained from the integer convex-hull iteration agrees, step for step, with reachability in the directed graph. The first return of \(A_i\) is the length of the shortest positive closed directed walk starting at \(i\), as in Wang's Proposition 3.5. A shortest positive closed walk is a directed simple cycle, of length at most twelve.

**Complete finite enumeration.** Every permutation consisting of a single thirteen-cycle has a unique orbit encoding beginning with site \(1\). Fix its successor \(a+1\), with \(a\in\{1,\ldots,12\}\); the other eleven sites can appear in the orbit in any order, producing exactly \(11!=39,916,800\) distinct cycles for that \(a\). These twelve disjoint blocks exhaust \(12!=479,001,600\) cycles.

In `verify_characteristic13.cpp` the sites are zero-based. For each block the code constructs the unique mapping of each cyclic ordering, builds its twelve graph adjacency masks exactly by integer interval arithmetic, and uses bitset breadth-first search to determine the shortest positive closed walk through each graph vertex. The breadth-first search maintains successive exact-length reachable sets and omits previously expanded vertices; such omission cannot eliminate a shortest return, because a shortest path has no repeated interior vertex. The code sorts the twelve return lengths and checks every inequality \(c'_k\le k\).

The exhaustive outputs in `census.tsv` give, **for each** fixed successor, \(39,916,800\) checked cycles, zero inequality violations, exactly one case with the entire profile \((1,2,\ldots,12)\), and zero such cases outside the modular translation \(j\mapsto j+a\pmod {13}\). Hence the first claim and the extremal classification are established. Since \(\sum_{k=1}^{12}k=78\), equality in the sum is possible exactly when every individual bound is sharp.

The same enumeration calculates the least strictly positive value of \(78-S(\pi)\) and its frequency within each fixed-successor block. Exactly the two blocks with successor \(3\) or \(13\) (one-based labels) have minimum positive deficit \(1\), each attained exactly once. All other blocks have larger positive deficits. Thus exactly the two displayed one-line permutations attain \(S=77\), and every other nontranslation has \(S\le76\). Direct convex-hull iteration independently verifies their displayed characteristic sequences.

All integer arithmetic in the census is exact. The proof depends on the full finite enumeration, not on a random sample or a heuristic numerical extrapolation.

## Verification

Compile `verify_characteristic13.cpp` using a conforming C++17 compiler and run the executable for each integer first-successor argument from \(1\) through \(12\). It checks a total of \(479,001,600\) cycles and produces the twelve rows reported in `census.tsv`. Each row has zero violations, exactly one maximal profile, and no non-modular maximal profile. The minimum strictly positive deficit is \(1\) with total multiplicity \(2\).

The separate `check_direct.py` uses literal repeated convexification of all integer images rather than the directed-graph breadth-first search. It compares the two algorithms for **all** single-cycle permutations on \(3\) through \(8\) symbols, and for \(10,000\) reproducibly selected thirteen-cycles: \(15,912\) independent objectwise comparisons. It also directly checks the two near-maximal representatives and the twelve modular translations. No external data or nonstandard libraries are needed.

## Relationship to prior work

Yihan Wang (2022) formulated the characteristic-sequence conjecture in Definition 1.6 and Conjecture 1.7, established the equivalence with a covering-interval conjecture (Theorem 1.8), and recorded exhaustive computational verification for orders through \(12\) in Example 3.7. Wang also calculated the profile of a distinguished cyclic translation. The present result addresses the **first order beyond that reported finite range**, establishing the complete first and second extremal tiers at order \(13\). Known modular-shift profiles alone do not imply either that all thirteen-cycles obey the inequalities or that no other thirteen-cycle is extremal.

## Limitations

The result is exact but finite. It does **not** prove the conjecture for general \(n\), settle the continuous covering-system conjecture for arbitrary numbers of intervals, or classify near-maximizers at arbitrary order. The exhaustive proof relies on correct implementation of the transparent finite checker; an independent formal or human proof has not been supplied. Broader publication-priority verification is still open.

## References

Yihan Wang, *On an existence problem of periodic points in intervals whose images cover themselves*, arXiv:2205.07225v1, first publicly posted 2022-05-15. https://arxiv.org/abs/2205.07225 . See Definition 1.6, Conjecture 1.7, Proposition 3.5, Theorem 1.8, and Example 3.7.

Uhland Burkart, *Interval mapping graphs and periodic points of continuous functions*, Journal of Combinatorial Theory, Series B 32(1) (1982), 57–68. Cited here for the established graph interpretation; the complete article was not inspected.
